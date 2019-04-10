from capstone import *
import os
import sys
import pyvex
import archinfo
from SymRepresentation import SymRepresentation
import argparse
import re
from Gadget import Gadget
from ElfBinary import getHexStreamsFromElfExecutableSections
from PEBinary import getHexStreamFromPE
from itertools import permutations
import dill
import time
from multiprocessing import Pool, Queue, Manager, Array
import Options
from time import sleep
import traceback
import myshare
import operator

archlen = 0
bin_in = ""


##############################################################
# takes a string of arbitrary length and formats it 0x for Capstone
def convertXCS(s):
    if len(s) < 2: 
        print "Input too short!"
        return 0
    
    if len(s) % 2 != 0:
        print "Input must be multiple of 2!"
        return 0

    conX = ''
    
    for i in range(0, len(s), 2):
        b = s[i:i+2]
        b = chr(int(b, 16))
        conX = conX + b
    return conX


##############################################################


# gets a set of gadgets, returns the one with the best quality
def getBestQualityGadget(gadgets):
    best = gadgets[0]
    
    for g in gadgets:
        if g.grade < best.grade:
            best = g
    
    return best



def findCallPrecGadgets(gadgets):
    callprec = []
    
    for g in gadgets:
        if "call" in g.instructions[0]:
            callprec.append(g)

    return callprec

def findHeuristicBreaker(gadgets, fname):
    hb = []
    f = open(fname + "_heuristic_breakers", "w")
    # what do we want?
    # as little preconditions and postconditions as possible
    # maybe not touch important registers?
    # maybe grade pre- / postconds differently?
    # avoid push / ret
    for g in gadgets:
        if g.length >= 20:
            grade = 0
            nonmempostconds = 0
            #grade += calcQualityRegisterDerefences(g)
            #grade += calcQualityBadIns(g)
            for post in g.postconditions:
                #print p
                if not "store" in post:
                    nonmempostconds += 1
            
            usedregs = len(summarizePreconds(g.preconditions))
            
            grade = usedregs * 1.2 + nonmempostconds * 0.8
            print g.address
            f.write(str(g.address) + "\n")
            print g.instructions
            
            for i in g.instructions:
                f.write(i + "\n")
            
            #f.write(str(g.instructions) + "\n")
            print "len: " + str(g.length)
            f.write("len: " + str(g.length) + "\n")
            print "regsused: " + str(usedregs) # preconditions; dereferenced registers, need to be attacker-controlled!
            f.write("regsused: " + str(usedregs) + "\n")
            print "nonmempostconds: " + str(nonmempostconds) # postconds; overwritten registers
            f.write("nonmempostconds: " + str(nonmempostconds) + "\n")
            print "grade: " + str(grade)
            f.write("grade: " + str(grade) + "\n")
            print "\n"
            f.write("\n")
            hb.append([g,g.length - grade])
    
    hb.sort(key=operator.itemgetter(1))
    
    for b in hb:
        #print b[0].address + " _ " + str(b[0].length)
        print "@%s - length: %i - score: %f" %(b[0].address, b[0].length, b[1])
        f.write("@%s - length: %i - score: %f\n" %(b[0].address, b[0].length, b[1]))
   

    f.close()
    

def calcQualityBadIns(gadget):
    postconds = gadget.postconditions
    
    res = 0
    
    for i in gadget.instructions:
        if "cli" in i:
            res += 10
    
    if "exctract" in postconds:
        res += 2
    
    if "|" in postconds:
        res += 2
    
    if "~" in postconds:
        res += 2
        
    return res


# we want the data as close to rsp/whatever as possible
def calcQualityRegisterDerefences(gadget):
    preconds = gadget.preconditions
    res = getRangePreconditions(preconds, "x86-64")
    
    for r in res:
        if "LB:" in r:           
            try:
                lb = r[r.find("LB:") + 3 : r.find(" ")]
                ub = r[r.find("UB") + 3 : r.find("]")]
                lb_int = int(lb)
                ub_int = int(ub)
            except:
                lb_int = 0
                ub_int = 0
            
            if lb_int + 100000 < ub_int:
                #print "OMG THE BADNESS IS SO BAD111"
                #print gadget.instructions
                return 6
            elif lb_int + 10000 < ub_int:
                #print "OMG THE BADNESS IS BAD1" 
                #print gadget.instructions
                return 4
            elif lb_int + 1000 < ub_int:
                #print "OMG THE BADNESS"  
                #print gadget.instructions        
                return 2
    return 0

def calcGadgetQuality(gadgets):
    for g in gadgets:
        res_reg_derefs = calcQualityRegisterDerefences(g)
        res_bad_ins = calcQualityBadIns(g)
        grade = len(g.preconditions) + len(g.postconditions) + g.length / 2 + len(g.opcodes) / 2 + res_reg_derefs + res_bad_ins
                
        g.grade = grade
    
    return gadgets


#gets a line with a put(reg) = something
#returns reg
def getRegInPut(l):
    offl = l.find("(")
    offr = l.find(")")
    
    return l[offl + 1:offr]
    

#returns all gadgets that load a register with either another register, or a value from another register
# e.g., pop rax
# push rbx, pop rax, ret
# mov rax, rbx
def goodLoads(gadgets):
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    gl = []
    for g in gadgets:
        goodloads = []
        
        if g.address == 4653335:
            pass
        
        for p in g.postconditions:
            if "store" in p:
                continue
            
            reg = getRegInPut(p)
            
            # check if the same value occurs more than once
            if p.find(reg, p.find(reg) + 1) > 0:
                continue
                #print p
            # check if any other registers appear, otherwise a constant value is assigned, which is also not what we want
            
            rhs = p[p.find("=") : len(p)]
            for r in regs:
                if r in rhs:
                    goodloads.append(reg)
                    break
        
        if len(goodloads) > 0:
            g.goodload = goodloads
            gl.append(g)
            
    return gl
    
#returns all gadgets that load a register with an rsp-relative value
# e.g. pop reg, mov reg, [rsp]
def bestLoads(gadgets):
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    bl = []
    
    for g in gadgets:
        loadedregs = []
                
        for p in g.postconditions:
            if "store" in p:
                continue
            
            if not "load" in p:
                continue
            
            rhs = p[p.find("=") : len(p)]
            
            if not "rsp" in rhs:
                continue
            
            bad = 0
            for r in regs:
                if r in rhs:
                    bad = 1
                    break
            if bad == 0:
                #print p
                loadedregs.append(getRegInPut(p))
        
        if len(loadedregs) > 0:
            g.greatload = loadedregs
            bl.append(g)
        

        
    return bl
                
            


def initSatPrecond(reg, topgadgets, propgadgets):

    satchain = []
      
    gadget, reg_rec = satPrecond(reg, topgadgets, propgadgets)
    solved = 0
      
    if gadget == "err":
        print "Nothing found..."
        return
    elif len(reg_rec) == 0:
        print "Solved!"
        satchain.append(gadget)
    else:
        satchain.append(gadget)
          
        for rr in reg_rec:
            if solved == 1:
                break
            iteration = 0
            reg_dep = reg_rec
            while len(reg_dep) > 0:
                for rr in reg_dep:
                    gadget, reg_dep = satPrecond(rr, topgadgets, propgadgets)
                    satchain.append(gadget)
                iteration += 1
                if iteration > 5:
                    break
              
            if iteration > 5:
                print "Couldn't solve!!"
                return 0
            else:
                print "Solved!"
                solved = 1
      
      
    return satchain

# reg is the register that needs to be attacker controlled
def satPrecond(reg, topgadgets, propgadgets):
    
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    simp = []
    print "Solving for " + reg
    
#     print "Top gadgets"
#     for g in topgadgets:
#         print g.instructions
#     
#     print "---"
    
    for t in topgadgets:
        if not reg in t.greatload:
            #print "skip"
            #print t.instructions
            continue
        else:
            for p in t.postconditions:
                lhs = p[0 : p.find("=")]
                if reg in lhs:
                    if not "store" in lhs:
                        simp.append(t)
                        break
    
#     print "Good ones:"
#     for g in simp:
#         print g.postconditions
        
    # ideal case, there's a gadget that loads reg with a value relative to rsp (like pop reg)
    if len(simp) > 0:
        best = getBestQualityGadget(simp)
        print "Using: "
        print best.postconditions
        return best, []

    # maybe the more likely case, there is no such gadget, so we need to propagate gadget values till we
    # maybe end up at a gadget that loads a register with a value relative to rsp
    # e.g., reg = "r8"; topgadgets are "pop rax ; pop rdx" ; propgadgets are "mov r8, rdx"
    # put together: pop rdx ; mov r8, rdx; therefore, r8 is attacker-controlled via rdx
    
    #print "Propgadgets:"
    for pg in propgadgets:
        if not reg in pg.goodload:
            continue
        for p in pg.postconditions:
            lhs = p[0 : p.find("=")]
            if reg in lhs:
                simp.append(pg)
                break
    
    if len(simp) > 0:
        best = getBestQualityGadget(simp)
        
        for p in best.postconditions:
            lhs = p[0 : p.find("=")]
            rhs = p[p.find("=") : len(p)]
            if reg in lhs:
                reg_rec = []
                for r in regs:
                    if r in rhs:
                        reg_rec.append(r)
                        
                print "Using:"
                print p
                print "Require solving for: "
                print reg_rec
                return best, reg_rec #returning the gadget (will be added to the chain by the caller) AND the new dependency, i.e., the caller will call this function again with reg_rec
    
    return "err", 0

#takes a gadget and the set of all gadgets, returns a chain of gadgets that makes sure all preconditions of gadget are satisfied
#iterates of preconditions of gadget
#if: get(rsp) -> fine
#else: -> [reg]
#iterate through gadgets
#look for gadget with postcondition reg = get(rsp)
#if that doesn't exist, use any one with reg = get(reg')
#look for another gadget that has reg' = get(rsp)
def satPreconds(gadget, gadgets):
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
        
    for p in gadget.preconditions:
        for r in regs:
            if r in p:
                #print p
                pass
                # "offending" register is r, now find a gadget that sets r relative to rsp
            else:
            # the precondition uses only rsp, so it should be fine (unless it's something like [rsp + ff939234802fff]
                pass



# 000000000040160b
def reverseBytes(s):
    out = ""
    for i in range(len(s), -1 , -2):
        b = s[ i - 2 : i  ]
        out += b
    
    return out
        

def convertAddress(s):
    conv = str(hex(s))
    conv = conv.rjust(18, "0")
    conv = conv.replace("0x", "")
    conv = reverseBytes(conv)
    conv = convertXCS(conv)
    return conv
    
    

def interestingPostconds(postconds):
    post = []
    for p in postconds:
        if "put(rdi)" in p:
            post.append(p)   
        if "put(rsi)" in p:
            post.append(p) 
        if "put(rcx)" in p:
            post.append(p)
        if "put(rdx)" in p:
            post.append(p)
        if "put(r8)" in p:
            post.append(p)
        if "put(r9)" in p:
            post.append(p)
    
    return post

def summarizePreconds(preconds):
    usedregs = []
    
    for p in preconds:
        off = 0
        #iterate through all get(reg), add reg to set
        while off != -1:
            off = p.find("get(",off)
            if off != -1:
                reg = p[off+4 : off+7]
                #print reg
                off += 4
                if reg != "25)":
                    usedregs.append(reg)
        
    return list(set(usedregs))


def determine_type(postconds):
    gtype = []
        
    for p in postconds:
        if "put(rdi)" in p and "get(rdi)" in p:
            gtype.append("mod rdi")
        elif "put(rdi)" in p and "get" in p:
            gtype.append("ld rdi")   
            
        if "put(rsi)" in p and "get(rsi)" in p:
            gtype.append("mod rsi")
        elif "put(rsi)" in p and "get" in p:
            gtype.append("ld rsi")      
        
        if "put(rcx)" in p and "get(rcx)" in p:
            gtype.append("mod rcx")
        elif "put(rcx)" in p and "get" in p:
            gtype.append("ld rcx")
        
        if "put(rdx)" in p and "get(rdx)" in p:
            gtype.append("mod rdx")
        elif "put(rdx)" in p and "get" in p:
            gtype.append("ld rdx")
    
        if "put(r8)" in p and "get(r8)" in p:
            gtype.append("mod r8")
        elif "put(r8)" in p and "get" in p:
            gtype.append("ld r8")

        if "put(r9)" in p and "get(r9)" in p:
            gtype.append("mod r9")
        elif "put(r9)" in p and "get" in p:
            gtype.append("ld r9")
            
    return gtype


def changeType(gadgets):
    
    for g in gadgets:
        gtype = []
        g.gadgetype = []
        
        for p in g.postconditions:
            if "put(rdi)" in p and "get(rdi)" in p:
                gtype.append("mod rdi")
            elif "put(rdi)" in p and "get" in p:
                gtype.append("ld rdi")   
                        
            if "put(rsi)" in p and "get(rsi)" in p:
                gtype.append("mod rsi")
            elif "put(rsi)" in p and "get" in p:
                gtype.append("ld rsi")      
                    
            if "put(rcx)" in p and "get(rcx)" in p:
                gtype.append("mod rcx")
            elif "put(rcx)" in p and "get" in p:
                gtype.append("ld rcx")
                    
            if "put(rdx)" in p and "get(rdx)" in p:
                gtype.append("mod rdx")
            elif "put(rdx)" in p and "get" in p:
                gtype.append("ld rdx")
                
            if "put(r8)" in p and "get(r8)" in p:
                gtype.append("mod r8")
            elif "put(r8)" in p and "get" in p:
                gtype.append("ld r8")
            
            if "put(r9)" in p and "get(r9)" in p:
                gtype.append("mod r9")
            elif "put(r9)" in p and "get" in p:
                gtype.append("ld r9")
                        
        g.gadgetype = gtype

    return gadgets


def get_shortest_gadget(Gadgets):

    if len(Gadgets) == 0:
        return 0
    
    shortest = Gadgets[0]
    for g in Gadgets:
        if g.length < shortest.length:
            shortest = g
    
    return shortest

def isSPrelative(gadget, reg):
    
    exp = "put(" + reg
    
    for p in gadget.postconditions:
        if exp in p:
            #found the postcondition we care about, now see how that register is loaded
            #ideally, only rsp related loads
            rsp = p.count("get(rsp)")
            other = p.count("get(")
            if rsp == other and rsp > 0:
                return 1
            else:
                return 0

def get_best_gadget(Gadgets, treg):
    # Check for fewest side-effects and easiest to fulfill preconditions
    
    if len(Gadgets) == 0:
        return 0
    
    gadgets_rsp = []
    
    for g in Gadgets:
        sprel = isSPrelative(g, treg)
        if sprel == 1:
            #print "Loaded relative to RSP:" + g.opcodes
            gadgets_rsp.append(g)
    
    if len(gadgets_rsp) == 0:
        return getBestQualityGadget(Gadgets)
        #return get_shortest_gadget(Gadgets)
    else:
        return getBestQualityGadget(gadgets_rsp)
        #return get_shortest_gadget(gadgets_rsp)

    
    

# returns 0 for c3 or the int offset of any c2
def getRet(gadget):
    g = gadget.opcodes
    if g[len(g) - 2 : len(g)] == "c3":
        return 0
    elif g[len(g) - 6 : len(g) - 4] == "c2":
        offset = g[len(g) - 4 : len(g)]
        offset = reverseBytes(offset)
        offset = int(offset, 16)
        return offset
    else:
        print "Gadget doesn't end with RET"
        return 0


# takes a gadget, checks postconditions, returns padding
# required for e.g. c21000 (pops off two arguments)
# or also additional pops or arithmetic on rsp
# go through postconds till we find rsp, if the constant is larger than 16 (pop + ret), something's weird and we need padding
def rspPadding(gadget):
    for p in gadget.postconditions:
        if "put(rsp)" in p:
            # found the right postcondition, check rsp offset
            break
        
    offsets = [int(s) for s in re.findall(r'\b\d+\b', p)]
    if len(offsets) != 1:
        #shouldn't happen
        return 0
        
    padding = ""
    offset = offsets[0]
    if offset != 2 * archlen: #i.e., 8 for x86, 16 for x86-64
        #needs padding
        padding = 'A' * (int(offset) - 2 * archlen)
    
    return padding



def pStart(adr):
    conv = str(hex(adr))
    conv = conv[0:len(conv)-3] + "000"
    conv = conv.rjust(18, "0")
    conv = conv.replace("0x", "")
    conv = reverseBytes(conv)
    return conv
        


# unused at the moment
def getStackPivotCandidates(gadgets):
    
    r64 = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    spcand = []

    for g in gadgets:
        for p in g.postconditions:
            if "put(rsp)" in p:
                offsets = [int(s) for s in re.findall(r'\b\d+\b', p)]
                break
        
        if len(offsets) == 1:
            offset = offsets[0]
            
            if offset >= 200 or any(r in p for r in r64):
                spcand.append(g)
        else:
            spcand.append(g)

    for g in spcand:
        print g.opcodes
    
    return spcand

    

def find_gadget_candidates(Gadgets, minglen):
    
    rdi_candidate = []
    rsi_candidate = []
    rcx_candidate = []
    rdx_candidate = []
    r8_candidate = []
    r9_candidate = []
    
    for g in Gadgets:
        if g.length >= minglen:
            if "ld rdi" in g.gadgetype:
                rdi_candidate.append(g)
            if "ld rsi" in g.gadgetype:
                rsi_candidate.append(g)
            if "ld rcx" in g.gadgetype:
                rcx_candidate.append(g)
            if "ld rdx" in g.gadgetype:
                rdx_candidate.append(g)
            if "ld r8" in g.gadgetype:
                r8_candidate.append(g)
            if "ld r9" in g.gadgetype:
                r9_candidate.append(g)
    
#     print "Printing candidates..."
#     
#     print "rdi:"
#     for g in rdi_candidate:
#         print g.opcodes
#     
#     print "rsi:"
#     for g in rsi_candidate:
#         print g.opcodes
#     
#     print "rcx:"
#     for g in rcx_candidate:
#         print g.opcodes
#     
#     print "rdx:"
#     for g in rdx_candidate:
#         print g.opcodes
#     
#     print "r8:"
#     for g in r8_candidate:
#         print g.opcodes
#     
#     print "r9:"
#     for g in r9_candidate:
#         print g.opcodes
    
    
    # if no gadgets that write a fixed value (either a constant or from memory/reg)
    # are found, look for ones that modify the value, they might be useful
    if len(rdi_candidate) == 0:
        for g in Gadgets:
            if "mod rdi" in g.gadgetype:
                rcx_candidate.append(g)
    
    if len(rsi_candidate) == 0:
        for g in Gadgets:
            if "mod rsi" in g.gadgetype:
                rcx_candidate.append(g)
    
    if len(rcx_candidate) == 0:
        for g in Gadgets:
            if "mod rcx" in g.gadgetype:
                rcx_candidate.append(g)
    
    if len(rdx_candidate) == 0:
        for g in Gadgets:
            if "mod rdx" in g.gadgetype:
                rcx_candidate.append(g)
    
    if len(r8_candidate) == 0:
        for g in Gadgets:
            if "mod r8" in g.gadgetype:
                rcx_candidate.append(g)

    if len(r9_candidate) == 0:
        for g in Gadgets:
            if "mod r9" in g.gadgetype:
                rcx_candidate.append(g)
                
    
    #write all those interesting gadgets to a file
#     f = open("coolgadgets", "w")
#     
#     for g in rdi_candidate:
#         f.write("Address: 0x%x:\n" %(g.address))
#         f.write("Opcodes: " + g.opcodes + "\n")
#     
#     for g in rsi_candidate:
#         f.write("Address: 0x%x:\n" %(g.address))
#         f.write("Opcodes: " + g.opcodes + "\n")
#     
#     for g in rdx_candidate:
#         f.write("Address: 0x%x:\n" %(g.address))
#         f.write("Opcodes: " + g.opcodes + "\n")
#     
#     for g in rcx_candidate:
#         f.write("Address: 0x%x:\n" %(g.address))
#         f.write("Opcodes: " + g.opcodes + "\n")
#     
#     f.close()
    

    best_rdi = get_best_gadget(rdi_candidate, "rdi")
    best_rsi = get_best_gadget(rsi_candidate, "rsi")
    best_rcx = get_best_gadget(rcx_candidate, "rcx")
    best_rdx = get_best_gadget(rdx_candidate, "rdx")
    best_r8 = get_best_gadget(r8_candidate, "r8")
    best_r9 = get_best_gadget(r9_candidate, "r9")
    
#     if best_rdi != 0:
#         #print best_rdi.opcodes
#         print best_rdi.instructions
#     
#     if best_rsi != 0:
#         #print best_rsi.opcodes
#         print best_rsi.instructions
#     
#     if best_rcx != 0:
#         #print best_rcx.opcodes
#         print best_rcx.instructions
#     
#     if best_rdx != 0:  
#         #print best_rdx.opcodes
#         print best_rdx.instructions
#     
#     if best_r8 != 0:
#         #print best_r8.opcodes
#         print best_r8.instructions
#     
#     if best_r9 != 0:
#         #print best_r9.opcodes
#         print best_r9.instructions
    
    return best_rdi, best_rsi, best_rcx, best_rdx, best_r8, best_r9
    

def conc_gadgets(gadgets):
    # concatenates gadgets, removes all RETs though, because we only care about side effects on registers
    # maybe a bad idea to remove the RETs, might change the disassembly?
    gadget = ""
    
    for ga in gadgets:
        
        g = ga.opcodes
        
        if g[len(g) - 2 : len(g)] == "c3":
            gadget += g[0 : len(g) - 2]
        
        if g[len(g) - 2 : len(g)] == "cb":
            gadget += g[0 : len(g)- 2]
        
        if g[len(g) - 6 : len(g) - 4] == "c2":
            gadget += g[0 : len(g) - 6]
            
        if g[len(g) - 6 : len(g) - 4] == "ca":
            gadget += g[0 : len(g) - 6]
       
    #print "Concatenated gadget:"
    #print gadget
    return gadget
    
    
def combineGadgetsPE2(rcx, rdx):

    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print "Couldn't find gadget for rdx!"
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0

    gadgets = []
    gadgets.append(rcx)
    gadgets.append(rdx)

    
    res = permutations(gadgets)
       
#     gadget = rcx.opcodes + rdx.opcodes + r8.opcodes + r9.opcodes
#     gadget = gadget.replace("c3", "")
#     print gadget
    return res

def combineGadgetsPE3(rcx, rdx, r8):

    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print "Couldn't find gadget for rdx!"
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print "Couldn't find gadget for r8!"
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    
    res = permutations(gadgets)
       
#     gadget = rcx.opcodes + rdx.opcodes + r8.opcodes + r9.opcodes
#     gadget = gadget.replace("c3", "")
#     print gadget
    return res


def combineGadgetsPE4(rcx, rdx, r8, r9):

    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print "Couldn't find gadget for rdx!"
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print "Couldn't find gadget for r8!"
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r9 == 0:
        print "Couldn't find gadget for r9!"
        r9 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    gadgets.append(r9)
    
    res = permutations(gadgets)
       
#     gadget = rcx.opcodes + rdx.opcodes + r8.opcodes + r9.opcodes
#     gadget = gadget.replace("c3", "")
#     print gadget
    return res



def combineGadgetsELF2(rdi, rsi):

    if rdi == 0:
        print "Couldn't find gadget for rdi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print "Couldn't find gadget for rsi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    
    res = permutations(gadgets)
    
    return res


def combineGadgetsELF3(rdi, rsi, rcx):

    if rdi == 0:
        print "Couldn't find gadget for rdi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print "Couldn't find gadget for rsi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    
    res = permutations(gadgets)
    
    return res

def combineGadgetsELF4(rdi, rsi, rcx, rdx):

    if rdi == 0:
        print "Couldn't find gadget for rdi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print "Couldn't find gadget for rsi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print "Couldn't find gadget for rdx!"
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    gadgets.append(rdx)
    
    res = permutations(gadgets)
    
    return res

def combineGadgetsELF5(rdi, rsi, rcx, rdx, r8):

    if rdi == 0:
        print "Couldn't find gadget for rdi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print "Couldn't find gadget for rsi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print "Couldn't find gadget for rdx!"
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print "Couldn't find gadget for r8!"
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    
    res = permutations(gadgets)
    
    return res

def combineGadgetsELF6(rdi, rsi, rcx, rdx, r8, r9):

    if rdi == 0:
        print "Couldn't find gadget for rdi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print "Couldn't find gadget for rsi!"
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print "Couldn't find gadget for rcx!"
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print "Couldn't find gadget for rdx!"
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print "Couldn't find gadget for r8!"
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r9 == 0:
        print "Couldn't find gadget for r9!"
        r9 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    gadgets.append(r9)
    
    res = permutations(gadgets)
    
    return res


def writeGadgetsToDisk(gadgets, fn):
    
    #myfile = open(fn, "ab+")
    
    outfile = open (fn+"_gadgets", "ab+")
    
    for g in gadgets:
        outfile.write("0x%x : " %(g.address))
        for i in g.instructions:
            outfile.write(i + " ; ")
        outfile.write("\nPreconditions: %s\n" %(g.preconditions))
        outfile.write("Postconditions: %s\n" %(g.postconditions))
        outfile.write("Bytestream: %s\n" %(g.opcodes))
        outfile.write("Length: %i\n\n" %(g.length))
    
    outfile.close()


def filterStrict(gadgets):
    badins = ["ret", "retf", "iretd", "iret", "call", "lcall", "syscall", "int3", "loop", "loope", "loopne", "jmp", "je", "jne", "jg", "jng", "jge", "jnge", "jl", "jnl", "jle", "jnle", "jb", "jbe", "ja", "jna", "jae", "jnae", "js", "jnp", "jo", "jno", "fist" "hlt", "int", "in", "out", "enter"]
    #regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    gg = []
    bg = []
    
    for g in gadgets:
        bad = 0
        for i in g.instructions:
            instr = i[0 : i.find(" ")]
            if instr in badins:
                bad += 1
            
        # Check if a gadget changes rsp too much
#         for p in g.postconditions:
#             if "put(rsp)" in p:
#                 for r in regs:
#                     if r in p:
#                         bad += 1
            
        if bad == 1:
            gg.append(g)
        else:
            bg.append(g)
            
    return gg, bg

def filterSemiStrict(gadgets):
    badins = ["ret", "retf", "syscall", "int3", "loop", "loopne", "loope", "jmp", "je", "jne", "jg", "jng", "jge", "jnge", "jl", "jnl", "jle", "jnle", "jb", "jbe", "ja", "jna", "jae", "jnae", "js", "jnp", "jo", "jno", "fist" "hlt", "int", "in", "out", "enter"]
    #regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    gg = []
    
    for g in gadgets:
        bad = 0
        calls = 0
        for i in g.instructions:
            instr = i[0 : i.find(" ")]
            if instr in badins:
                bad += 1
            
            if "call" in instr:
                calls += 1
            
        # Check if a gadget changes rsp too much
#         for p in g.postconditions:
#             if "put(rsp)" in p:
#                 for r in regs:
#                     if r in p:
#                         bad += 1
            
        if bad == 1 & calls == 1:
            gg.append(g)

    return gg
    

def getCodeSegments(inputbinary):
    #check whether it's elf or pe
    # we'll do it cheap, extension .exe and .dll is PE, anything else is ELF
       
    if inputbinary[len(inputbinary) - 4 : len(inputbinary)] == ".exe":
        return getHexStreamFromPE(inputbinary)
    
    if inputbinary[len(inputbinary) - 4 : len(inputbinary)] == ".dll":
        return getHexStreamFromPE(inputbinary)
    
    return getHexStreamsFromElfExecutableSections(inputbinary)


class Task():
    def __init__(self):
        self.hexdata = None
        self.arch = None
        self.foffset = None
        self.maxlen = None
        self.minlen = None

def getRetOffsets(hexdata, queue, arch, foffset, maxlen, minlen):
    pass
    


def find_gadgets(arch, hexdata, foffset, off, maxlen, minlen):
    
    #start_time = time.time()
    #print "Starting at addres " + str(off) 
    
    if arch == "x86":
        bitlength = 32
    elif arch == "x86-64":
        bitlength = 64
    else:
        raise Exception("bitlength must be either 32 or 64. Got ", bitlength)
    
        
    #Reads a bytestream - better for testing specific gadgets
    #myfile = open("in_test", "r")
    #bin_in = "in_test"
    #foffset = 0
    #hexdata = myfile.read().lower() # Convert input to lowercase
    #myfile.close()
    
    #Reads a real binary (only .code / .text sections!)
    #data = getHexStreamFromElf("/home/user/workspace/InspectorGadget/src/InspectorGadget/dbus-daemon").lower() # good!
    #data = getHexStreamFromElf("/home/user/workspace/InspectorGadget/src/InspectorGadget/gcc-4.9").lower() # good!
    #data = getHexStreamsFromElfExecutableSections("/home/user/workspace/InspectorGadget/src/InspectorGadget/nginx")


    #Collects all found gagdets
    Gadgets = []
    
    if bitlength == 32 :
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif bitlength == 64 : 
        md = Cs(CS_ARCH_X86, CS_MODE_64)
    else :
        raise Exception( "Bitlength needs to be 32 or 64!")

    offset = off
    ret = ["c3", "c2"]
    retn = ["c2"]

    #badins = ["ret", "retf", "call"]
    badins = ["ret", "retf"]   
     
#     if offset % 1024 == 0:
#         print "Checking %i / %i\n" %(offset, len(hexdata))
    
    # read a byte
    opcode = hexdata[offset : offset + 2]
    
    if opcode in ret :
        if opcode in retn :
            retn_offset = 4
        else :
            retn_offset = 0
        offset_back = offset + 2 + retn_offset
        
        while offset_back > 0:
            offset_back -= 2
            opcode = hexdata[offset_back : offset_back + 2]
            gadget = hexdata[offset_back : offset + 2 + retn_offset]           
            gadget_readable = gadget
                                   
            gadget = convertXCS(gadget)
            
            if gadget != 0:
                i = "err"
                length = 0
                badins_cnt = 0
                endswithret = 0
                total_size = 0
                                    
                for (address, size, mnemonic, op_str) in md.disasm_lite(gadget, offset):
                    i = "k"
                    length += 1
                    total_size += size
                    if mnemonic in badins:
                        badins_cnt += 1
                    if badins_cnt > 1:
                        break
                
                # Adding a threshold is important, because a gadget might disassemble to something shorter if we go back far enough!
                # E.g., 4158415948B89090909090909090C3 disassembles to:
                # nop  ; ret # nop ; nop ; ret # etc., and if we stop when reaching the maximum of 5 instructions we miss the following:
                # pop r8 ; pop r9 ; movabs rax,0x9090909090909090 ; ret
                # Length +5 = ~10% slowdown
                
                if length > maxlen + 5:
                    break
              
#                 if total_size < ((offset - offset_back) / 2 + 1):                     
#                     #continue
#                     pass
                
                if i != "err" and mnemonic == "ret":
                    endswithret = 1
                    
                if badins_cnt == 1 and i != "err" and endswithret == 1 and length >= minlen and length <= maxlen:
                    
                    if total_size < ((offset - offset_back) / 2 + 1):
                        continue
                    
                    disas = ""
                    instructions = []
                    for (address, size, mnemonic, op_str) in md.disasm_lite(gadget, offset):
                        disas += mnemonic + " " + op_str + " ; "
                        instructions.append(mnemonic + " " + op_str)
                    realaddress = offset / 2 - len(gadget_readable) / 2 + 1 + retn_offset / 2 + foffset
                    posts, pres, pre, post = passZero(gadget, arch)
                    
                    if posts != "err":
                        gtype = determine_type(posts)
                        gadget = Gadget(realaddress, gadget_readable, pres, pre, posts, post, 0, gtype, 0, length, instructions, "", "")
                        Gadgets.append(gadget)
                    
      
    goodgadgets, badgadgets = filterStrict(Gadgets)
    #print "Stopped at addres " + str(offset_back) 
    #print "Found gadgets: " + str(len(Gadgets))
    #print("Good gadgets: %i\nBad gadgets: %i\n" %(len(goodgadgets), len(badgadgets)))   
    #print("--- %s seconds ---" % (time.time() - start_time))
    
    return goodgadgets, badgadgets



#old, not used anymore, but contains good ideas for restrictions (e.g., finding if a gadget is call-preceded etc.)
# def find_gadgets_old(m):
# 
#     myfile = open("in_test", "r")
#     data = myfile.read().lower() # Convert input to lowercase
#     myfile.close()
#     
#     myfile = open("gadgets", "w+")
#     
#     # Assuming 32 bit (otherwise change mode to CS_MODE_64)
#     if m == 32 :
#         md = Cs(CS_ARCH_X86, CS_MODE_32)
#     elif m == 64 : 
#         md = Cs(CS_ARCH_X86, CS_MODE_64)
#     else :
#         print "Bitlength needs to be 32 or 64!"
#         return
#     
#     offset = 0
#     gadget_len = 0
#     
#     # As long as new c3 instructions are found, starting at offset
#     while data.find("c3", offset) != -1:
#         # Store old offset for later
#         offset_old = offset
#     
#         # Set offset to the start of the newly found ret
#         offset = data.find("c3", offset)
#     
#         # Copy the offset to tmp, which is used to go back in the bytestream
#         tmp = offset
#     
#         # For now we're going back till we arrive at the old offset or find a c2 (RET)
#         # In reality we'll stop after X instructions
#     
#         while (tmp >= offset_old):
#             # offset+2 includes the c3, and we go back -2, -4, -6, -8, etc. to create longer and longer gadgets
#             new_gadget = data[tmp:offset+2]
#     
#             # Check for c2 ret
#             # TODO check other rets, jmps etc. anything that disturbs control flow!
#             if data[tmp:tmp+2] == "c2":
#                 break
#     
#             tmp = tmp - 2
#     
#             # Convert format of the gadget (required for Capstone)
#             new_gadget_CS = convertXCS(new_gadget)
#     
#             # Required because for some reason Capstone disassembles e.g. 81c3 to RET, so I set
#             # a trigger only if bla
#             # Might Try to use a variable that stores the last instruction of the last successful
#             # disassembly, and check against that instead of the trigger
#             ins_valid = 0
#             
#             # Disassemble gadget, print it
#             for i in md.disasm(new_gadget_CS, 0x0):
#                 print("0x%x:\t%s\t\t\t%s\t%s" %(i.address, binascii.hexlify(i.bytes), i.mnemonic, i.op_str))
#                 ins_valid = 1
#             print "\n"
#     
#             # Check if last instruction was a c3, if yes, write gadget to file
#             if i.mnemonic == "ret" and ins_valid == 1:
#                 
#                 for (address, size, mnemonic, op_str) in md.disasm_lite(new_gadget_CS, 0x0):
#                     myfile.write("0x%x:\t%s\t%s\n" %(address, mnemonic, op_str))
#                                         
#                 # Check whether the gadget is call-preceded
#                 if data[tmp-2:tmp+2] in ['ffd0', 'ffd3', 'ffd1', 'ffd2', 'ffd4', 'ffd5', 'ffd6', 'ffd7']:
#                     myfile.write("Gadget is call-preceded (ind. call)\n")
#     
#                 # Check for intramodular calls (e8 <4 byte offset>)
#                 if data[tmp-8:tmp-6] == 'e8':
#                     myfile.write("Gadget is call-preceded (dir. call)\n")
#     
#                 # TODO - FF15 calls (intermodular calls)
#                 
#                 myfile.write("\n")
#                 # Problem: VEX shits its pants when it encounters an "invalid" bytestream and crashes
#                 # Therefore, only if disassembling with Capstone yields a good result, we convert to VEX
#                 # There's probably a nicer way of doing that.
#                 for (address, size, mnemonic, op_str) in md.disasm_lite(new_gadget_CS, 0x0):
#                     irsb = pyvex.IRSB(new_gadget_CS, 0x0, archinfo.ArchX86())
#     
#                     #print len(irsb.statements)
#                     #for ir in irsb.statements :
#                         #print ir
#                     #irsb.pp()
#                     #break
#     
#         # Increase the offset, to set it after this c3 (otherwise it would always find the same c3)
#         offset = offset + 2
#     
#     myfile.close()
# 
#     return



def cleanInputList(inList):
    myList = []
    
    # Clean list from instructions we're not interested in atm
    # All flag-instructions (cc) and instructions that change IP
    for ir in inList:
        #print ir.__str__()
        if "PUT" in ir.__str__():
            if "eip" in ir.__str__():
                #print "removing", ir
                #irsb.statements.remove(ir)
                pass
            if "rip" in ir.__str__():
                pass
            elif "cc" in ir.__str__():
                #print "removing", ir
                #irsb.statements.remove(ir)
                pass
            else:
                myList.append(ir);
        elif "IR-NoOp" in ir.__str__():
            #irsb.statements.remove(ir)
            pass
        elif "IMark" in ir.__str__():
            pass
        elif "eip" in ir.__str__():
            pass
        elif "rip" in ir.__str__():
            pass
        elif "cc_" in ir.__str__():
            pass
        elif "calculate" in ir.__str__():
            pass
        elif "AbiHint" in ir.__str__():
            pass
        elif "CAS" in ir.__str__():
            pass
        elif "ITE" in ir.__str__():
            pass
        elif "amd64g_dirtyhelper" in ir.__str__():
            pass
        elif "Sar" in ir.__str__():
            pass
        elif "F64toI64S" in ir.__str__():
            pass
        elif "DivMod" in ir.__str__():
            pass
        elif "128HIto64" in ir.__str__():
            pass
        elif "1Uto8" in ir.__str__():
            pass
        elif "F64toI32" in ir.__str__():
            pass
        elif "MullU8" in ir.__str__():
            pass
        elif "Not" in ir.__str__():
            pass
        elif "8Uto64" in ir.__str__():
            pass
        elif "8Sto32" in ir.__str__():
            pass
        elif "MullS8" in ir.__str__():
            pass
        elif "amd64g_create" in ir.__str__():
            pass
        elif "GetMSBs8x8" in ir.__str__():
            pass
        elif "GetMSBs8x16" in ir.__str__():
            pass
        else:
            myList.append(ir)
    
    #print "------------ new list -----------"
    #for ir in myList:
        #print ir
        
    return myList

# returns a new list that contains only lines which contain reg
def filterForReg(reg, myList):
    retlist = []
    for l in myList :
        if reg in l.__str__() and l.__str__()[0] != "t":
            retlist.append(l)
    return retlist

# Removes all lines that assign to t-registers
def filterTRegs(myList):
    for l in myList : 
        if l[0] == "t" :
            myList.remove(l)
    
    return myList


def isNumber(s):
    try:
        int(s,0)
        return int(s,0)
    except ValueError:
        return False


def getSignedNumber(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask


# Extracts constant, e.g. IN [0x4 + get(esp)]
# OUT 4
def extractConstant(expression):
    #val = re.search('0x[0-9abcdefABCDEF]*', expression)
    val = re.search('\d+', expression)
    if val is not None : 
        val = int(val.group(0))
    else : 
        val = 0
    
    return getSignedNumber(val, 64)

# Gets a list of preconditions that all share a common register, e.g.
# [esp]
# [esp + 8]
# [esp + 10]
# need to be writable
# Returns the range of memory affected, e.g. [esp] to [esp + 10] needs to be writable
def computeRange(preconditions):
    ranges = []
    for precond in preconditions : 
        ranges.append(extractConstant(precond))
        
    ranges.sort()
    
    # if it is an actual range and not just one or several accesses to the same memory offset
    if len(ranges) > 1 and (ranges[0] != ranges[len(ranges) - 1]):
        retrange = "LB:" + str(ranges[0]) + " UB:" + str(ranges[len(ranges) - 1])
    else : 
        retrange = str(ranges[0])
    #print retrange  
    return retrange


def getRangePreconditions(preconditions, architecture):
    regs32 = ["eax", "ebx", "ecx", "edx", "esi", "edi", "ebp", "esp"]
    regs64 = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    mem = []

    ranges = []
    loadlines = []
    
    for l in preconditions : 
        if "load" in l : 
            loadlines.append(l)
            preconditions.remove(l)
    
    # Find all load instructions, treat them like registers
    for l in loadlines : 
        load = l[l.find("load(") : len(l)]
        openbr = 0
        for index, c in enumerate(load) :
            if c == "(" :
                openbr += 1
            elif c == ")" :
                openbr -= 1
                if openbr == 0 :
                    #print load[0 : index + 1]
                    mem.append(load[0 : index + 1])
                    break
    
    #Get rid of duplicate memory regions the cheap way (convert to set, back to list)
    mem = list((set(mem)))           
    
    for m in mem : 
        lines = []
        for l in loadlines : 
            if m in l :
                lines.append(l)
        
        if len(lines) > 0 :
            myrange = m + "{" + computeRange(lines) + "}"
            ranges.append(myrange)
    
    if architecture == "x86" :
        for r in regs32 : 
            lines = []
            for l in preconditions :
                if r in l :
                    lines.append(l)

            if len(lines) > 0 :
                myrange = r + "[" + computeRange(lines) + "]"
                ranges.append(myrange)
    
    elif architecture == "x86-64" :
        for r in regs64 : 
            lines = []
            for l in preconditions :
                if r in l :
                    lines.append(l)

            if len(lines) > 0 :
                myrange = r + "[" + computeRange(lines) + "]"
                ranges.append(myrange)

    return ranges

# Takes a line and extracts preconditions
# Two possible preconditions:
# lhs: contain STle and a GET (stores something in memory, dereferincing a register
# -> that register has to point to writable memory
# rhs: any LD instruction, dereferencing a register
def getPreconditions(l):
    # Split in lhs and rhs
    lhs = l[0 : l.find("=") - 1]
    rhs = l[l.find("=") + 2 : len(l)]
    
    precond = []
    
    # Check lhs first
    if "ST" in lhs and "GET" in lhs : 
        #print "Writable memory required at: " + lhs[lhs.find("(") : lhs.find("=")]
        precond.append("Writable memory required at: " + lhs[lhs.find("(") : lhs.find("=")] + ")")
    elif "ST" in lhs :
        precond.append("Constant has to point to writable memory: (" + lhs + ")")
    
    # Check rhs
    if "LD" in rhs :
        subl = rhs[rhs.find("LD") : len(rhs)]
        subl = subl[subl.find("(") : len(subl)]

        b = 0
        i = 0
              
        for i in range(len(subl)) :
            if subl[i] == "(" :
                b += 1
            elif subl[i] == (")") :
                b -= 1
                if b == 0 : break
        
        subl = subl[0 : i]
        #print "Readable memory required: " + subl
        precond.append("Readable memory required: " + subl + ")")
            
    return precond
    

# Takes a line and extracts postconditions
# Since I've only encountered PUT and STle instructions after
# all passes, basically every line is a postcondition.
# Any given line can only contain one postcondition, so we just return the line
def getPostconditions(l):  
    return l


# For postconditions we're only interested in the last assignment to any register
# Before calling this function, simplify store instructions, then this check should be simple
# We start with a list of all regs, go through the input list backwards, if a PUT(reg) is found
# we remove reg from the list of regs. Hence, only the last assignment is taken into account. Booyakasha!
def filterDuplicateAssignments(myList, architecture):
    
    regstofind32 = ["eax", "ebx", "ecx", "edx", "esi", "edi", "ebp", "esp"]
    regstofind64 = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    if architecture == "x86" :
        regstofind = regstofind32
    elif architecture == "x86-64" : 
        regstofind = regstofind64
        
    keepList = []
    
    revList = myList[::-1]
       
    for l in revList : 
        if ("ST" in l) :
            keepList.append(l)
        else :
            for reg in regstofind : 
                if ("PUT("+reg in l) :
                    #print "KEEPING:" + l
                    #print "Removing from list of registers to find:" + reg
                    regstofind.remove(reg)
                    keepList.append(l)
    
    return keepList


def passOne32(myList):
    #logger.warning("------PASS ONE------")
    eax_cnt = 0
    ebx_cnt = 0
    ecx_cnt = 0
    edx_cnt = 0
    esp_cnt = 0
    ebp_cnt = 0
    esi_cnt = 0
    edi_cnt = 0
    
    retList = []
    
    for l in myList :
        l_st = l.__str__();
        lhs = l_st[0 : l_st.find("=") - 1]
        rhs = l_st[l_st.find("=") + 2 : len(l_st)]
        #print rhs
        #print lhs
        if "PUT" in lhs :
            if "eax" in lhs :
                eax_cnt += 1
                eax_rhs = rhs
            elif "ebx" in lhs : 
                ebx_cnt += 1
                ebx_rhs = rhs
            elif "esp" in lhs :
                esp_cnt += 1
                esp_rhs = rhs
            elif "ecx" in lhs :
                ecx_cnt += 1
                ecx_rhs = rhs
            elif "edx" in lhs :
                edx_cnt += 1
                edx_rhs = rhs
            elif "ebp" in lhs :
                ebp_cnt += 1
                ebp_rhs = rhs
            elif "esi" in lhs :
                esi_cnt += 1
                esi_rhs = rhs
            elif "edi" in lhs :
                edi_cnt += 1
                edi_rhs = rhs
        
        if "GET" in rhs : # and eax_cnt > 0
            #l_st = l_st.replace("eax", "eax"+str(eax_cnt).zfill(3))
            #print l_st
            if "eax" in rhs and eax_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], eax_rhs)
            elif "ebx" in rhs and ebx_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], ebx_rhs)
            elif "esp" in rhs and esp_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], esp_rhs) 
            elif "ecx" in rhs and ecx_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], ecx_rhs)
            elif "edx" in rhs and edx_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], edx_rhs)
            elif "ebp" in rhs and ebp_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], ebp_rhs)
            elif "esi" in rhs and esi_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], esi_rhs)
            elif "edi" in rhs and edi_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], edi_rhs)
         
        retList.append(l_st)
    return retList


def passOne64(myList):
    #logger.warning("------PASS ONE------")
    rax_cnt = 0
    rbx_cnt = 0
    rcx_cnt = 0
    rdx_cnt = 0
    rsp_cnt = 0
    rbp_cnt = 0
    rsi_cnt = 0
    rdi_cnt = 0
    r8_cnt = 0
    r9_cnt = 0
    r10_cnt = 0
    r11_cnt = 0
    r12_cnt = 0
    r13_cnt = 0
    r14_cnt = 0
    r15_cnt = 0
    
    retList = []
    
    for l in myList :
        l_st = l.__str__();
        lhs = l_st[0 : l_st.find("=") - 1]
        rhs = l_st[l_st.find("=") + 2 : len(l_st)]
        #print rhs
        #print lhs
        if "PUT" in lhs :
            if "rax" in lhs :
                rax_cnt += 1
                rax_rhs = rhs
            elif "rbx" in lhs : 
                rbx_cnt += 1
                rbx_rhs = rhs
            elif "rsp" in lhs :
                rsp_cnt += 1
                rsp_rhs = rhs
            elif "rcx" in lhs :
                rcx_cnt += 1
                rcx_rhs = rhs
            elif "rdx" in lhs :
                rdx_cnt += 1
                rdx_rhs = rhs
            elif "rbp" in lhs :
                rbp_cnt += 1
                rbp_rhs = rhs
            elif "rsi" in lhs :
                rsi_cnt += 1
                rsi_rhs = rhs
            elif "rdi" in lhs :
                rdi_cnt += 1
                rdi_rhs = rhs
            elif "r8" in lhs :
                r8_cnt += 1
                r8_rhs = rhs
            elif "r9" in lhs :
                r9_cnt += 1
                r9_rhs = rhs 
            elif "r10" in lhs :
                r10_cnt += 1
                r10_rhs = rhs
            elif "r11" in lhs :
                r11_cnt += 1
                r11_rhs = rhs
            elif "r12" in lhs :
                r12_cnt += 1
                r12_rhs = rhs
            elif "r13" in lhs :
                r13_cnt += 1
                r13_rhs = rhs
            elif "r14" in lhs :
                r14_cnt += 1
                r14_rhs = rhs
            elif "r15" in lhs :
                r15_cnt += 1
                r15_rhs = rhs
        
        if "GET" in rhs : # and eax_cnt > 0
            #l_st = l_st.replace("eax", "eax"+str(eax_cnt).zfill(3))
            #print l_st
            if "rax" in rhs and rax_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rax_rhs)
            elif "rbx" in rhs and rbx_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rbx_rhs)
            elif "rsp" in rhs and rsp_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rsp_rhs) 
            elif "rcx" in rhs and rcx_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rcx_rhs)
            elif "rdx" in rhs and rdx_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rdx_rhs)
            elif "rbp" in rhs and rbp_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rbp_rhs)
            elif "rsi" in rhs and rsi_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rsi_rhs)
            elif "rdi" in rhs and rdi_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], rdi_rhs)
            elif "r8" in rhs and r8_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r8_rhs)
            elif "r9" in rhs and r9_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r9_rhs)
            elif "r10" in rhs and r10_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r10_rhs)
            elif "r11" in rhs and r11_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r11_rhs)
            elif "r12" in rhs and r12_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r12_rhs)
            elif "r13" in rhs and r13_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r13_rhs)
            elif "r14" in rhs and r14_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r14_rhs)
            elif "r15" in rhs and r15_cnt > 0 :
                l_st = l_st.replace(l_st[l_st.find("=") + 2 : len(l_st)], r15_rhs)     
         
        retList.append(l_st)
    return retList


# Propagates ST statements to LD statements
def passTwo(myList, architecture):
    #logger.warning("--- PASS TWO ---")
    #print "------PASS TWO------"
    i = len(myList) - 1
    j = 0
       
    while i >= 0 : 
        ir_s = myList[i].__str__()
        if ir_s[0] != "t" : 
            if "STle" in ir_s : 
                j = i + 1
                rhs = ir_s[ir_s.find("=") + 2 : len(ir_s)].strip()
                lhs = ir_s[0 : ir_s.find("=")].strip()
                while j < len(myList) :
                    ir_s2 = myList[j].__str__()
                    
                    if architecture == "x86" :
                        rep = "LDle:I32"+lhs[lhs.find("(") : len(lhs)]
                    elif architecture == "x86-64" :
                        rep = "LDle:I64"+lhs[lhs.find("(") : len(lhs)]
                    else : # Shouldn't happen
                        rep = "ERR"
                        
                    if (rep in ir_s2) :
                        #print "ir_s2 before:" + ir_s2
                        ir_s2 = ir_s2.replace(rep, rhs)
                        #print "ir_s2 after:" + ir_s2
                        myList[j] = ir_s2
                    j += 1
                # removed on 18.2 - produces crash if ST is last instruction
                # also, doesn't seem to have any use, so...
                #ir_s = ir_s2
        i -= 1

                
    #for line in myList : 
        #if line[0] != "t" :
            #logger.warning(line)
    
    return myList



# Forward propagation
def passZero(new_gadget_CS, architecture):
       
    if architecture == "x86" :
        md = Cs(CS_ARCH_X86, CS_MODE_32)
        for (address, size, mnemonic, op_str) in md.disasm_lite(new_gadget_CS, 0x0):
            irsb = pyvex.IRSB(new_gadget_CS, 0x0, archinfo.ArchX86())
            bitlength = 32
            break
    elif architecture == "x86-64" :
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        for (address, size, mnemonic, op_str) in md.disasm_lite(new_gadget_CS, 0x0):
            try:
                irsb = pyvex.IRSB(new_gadget_CS, 0x0, archinfo.ArchAMD64())
            except:
                return "err", "err", "err", "err"
            bitlength = 64
            break
      
    #logger.warning("------------ original list -----------")
    #for ir in irsb.statements :
        #logger.warning(ir)
    
    myList = cleanInputList(irsb.statements)
    #logger.warning("------------ clean list -----------")
    #for ir in myList:
        #logger.warning(ir)
    
    #logger.warning("----------------")
    
    if architecture == "x86" :
        myList = passOne32(myList)
    elif architecture == "x86-64" :
        myList = passOne64(myList)
        
    #logger.warning("------------ clean list (after 1st pass) -----------")
    #for ir in myList:
        #logger.warning(ir)
    #quit()
    
    #myList = []
#     myList.append("t1 = GET:I32(eax)")
#     myList.append("t2 = Add32(t1,0x00000040)")
#     myList.append("PUT(eax) = t2")
#     myList.append("t1 = 0x00000001")
#     myList.append("t2 = 0x00000002")
#     myList.append("t3 = Add32(GET:I32(Add32(GET:I32(eax),t2)),t1)")
#      
#     print "------------ fake list -----------"
#     for ir in myList:
#         print ir
#      
#     print "----------------"
    
    #err = open("err.txt", "wb")
   
    i = 0
    j = 0
    
    #print "Entering..."
    #print(hex(ra))
    #print(gr)
    
    while i < len(myList) :
        ir_s = myList[i].__str__()
        tregex = ir_s[ir_s.find("=") + 2 : len(ir_s)].strip()
        treg = ir_s[0 : ir_s.find("=")].strip()
        #print "tregex:", tregex
        #print "treg:", treg
        
        if (treg[0] != "t") : 
            treg = "NOREG";
        
        i += 1
        j = i
        
        while j < len(myList) : 
            ir_s2 = myList[j].__str__()
            #print "Looking for {0} in {1}".format(treg, ir_s2)
            # Get the right hand side of the assignment
            rhs = ir_s2[ir_s2.find("=") + 2 : len(ir_s2)]
            lhs = ir_s2[0 : ir_s2.find("=") - 1]
            #print "RHS:", rhs
            off = rhs.find(treg)
            if off == -1:
                pass
            if off == 0:
                pass
            #print "off:", off
            #print "rhs:", rhs
            #print "len", len(ir_s2[off:len(ir_s2)])
            off_l = lhs.find(treg)
            
            # Check if the treg has been found
            if (off != -1) :
                # Check if the right hand side is treg
                if (rhs == treg) :
                    # Must be a simple assignment like PUT(esi) = t1 or t8 = t1 ; but cannot be t5 = t11
                    #print "Simple Assignment"; ###correct!
                    #print "rhs before:", rhs
                    rhs = rhs.replace(treg, tregex)
                    #print "Replaced {0} with {1}".format(treg, tregex)
                    #print "rhs after",rhs

                # Check if rhs is a complex assignment (e.g., Add or Sub)
                # Can easily be done by checking if it starts with a "t"

                elif (rhs[0] != "t") :
                    off_comma = rhs.find(",")
                    if (off_comma == -1) :
                        # check once
                        #print("off" , off)
                        #print("treg", treg)
                        #print("rhs", rhs)
                        if ( (off + len(treg)) < len(rhs) and rhs[off + len(treg)] == ")") :
                            #print "Complex Assignment (one Op)", ir_s2
                            #print "rhs before:", rhs
                            rhs = rhs.replace(treg, tregex)
                            #print "Replaced {0} with {1}".format(treg, tregex)
                            #print "rhs after",rhs
                    else : # there are commas, so check all operands                       
                        line = ""
                        lines = rhs.split(",")
                        for lin in lines : 
#                             print "----"
#                             print "treg:", treg
#                             print "tregex:", tregex
#                             print "LIN:", lin
                            # FIX 18.2
                            # added len(treg) < len(lin) otherwise it might crash if the treg is longer
                            # than an element of the line
                            if (len(treg) < len(lin) and lin[len(treg)] == ")" and treg in lin) :
                                #replace
                                lin = lin.replace(treg, tregex)
                                #print "Replaced {0} with {1}".format(treg, tregex)
                                #print "line after",lin
                            elif (lin[len(lin) - len(treg) == "("] and treg in lin and (lin.find(treg) + len(treg) == len(lin))) :
                                #print "lin", line
                                #print ir_s2
                                #print "FOUND LEFT111111"
                                lin = lin.replace(treg, tregex)
                            line = line + lin + ","
                        #print "AFTER REPLACEMETNS:", line
                        #print "RHS:", rhs
                        rhs = line[0 : len(line) - 1]
                                
                        #print "the following line was split:", rhs
                        #for lin in lines : 
                            #print "split line", lin
                        
                            
                                    
                ir_s2 = lhs + " = " + rhs
                #print "******* NEW:", ir_s2
                myList[j] = ir_s2
            
            if (off_l != -1 and lhs[0] != "t") : 
                if (lhs[off_l + len(treg)] == ")") :
                    lhs = lhs.replace(treg, tregex)
                    # Just replace lhs
                    ir_s2 = lhs + " = " + rhs
                    myList[j] = ir_s2
            
            j += 1
        
    #err.close()
    #logger.warning("######################")
    #for elem in myList: 
        #if elem.__str__()[0] != "t" :
            #print elem
        #logger.warning(elem)
        
    #myList = filterTRegs(myList)
    
    #print "Filtered (Removed Tregs)"
    #for elem in myList: 
        #print elem
        
    preconds = []
        
    # Finding preconditions BEFORE multiple assignments are removed
    # E.g. in case of pop eax # mov eax, 5
    for elem in myList : 
        pre = getPreconditions(elem)
        preconds = preconds + pre
    
    # Get rid of multiple preconditions the cheap way (convert to set and back to list)
    # Since the order of the elements does not matter, this is fine
    preconds = list((set(preconds)))
        
    myList = passTwo(myList, architecture)
    myList = filterDuplicateAssignments(myList, architecture)
    
    #logger.warning("------Cleaned output from multiple assignments to the same register------")
    #for elem in myList: 
        #if elem.__str__()[0] != "t" :
            #print elem
        #logger.warning(elem)
    
    postconds_simple = []
    postconds = []
    #logger.warning("------Finding Postconditions------")
    for elem in myList : 
        post = getPostconditions(elem)
        postconds.append(post)
        #logger.warning(post)
        sr_left = SymRepresentation(post.split("=")[0])
        simp_left = sr_left.simplify()
        sr_right = SymRepresentation(post.split("=")[1])
        simp_right = sr_right.simplify()
        #logger.warning("    ----> simplified: [%s]  =  [%s]", simp_left, simp_right)
        postconds_simple.append(str(simp_left) + " = " + str(simp_right))
    
    preconds_simple = []
    #logger.warning("------Finding Preconditions------")
    for pre in preconds :
        #logger.warning(pre)
        sr = SymRepresentation(pre[pre.find(":") + 3 : len(pre) - 1])
        simp = sr.simplify()
        #logger.warning("    ----> simplified: [%s]", simp)
        preconds_simple.append(str(simp))
    
    return postconds_simple, preconds_simple, preconds, postconds

    # WIP
#     logger.warning("------Simplified Preconditions------")
#     ranges = getRangePreconditions(simplist, "x86")
#     for elem in ranges : 
#         logger.warning(elem)
    
# def unusedCode():
#     
#     # DoMath sucks
#     flatList = []
#     
#     for elem in myList :
#         lhs = elem[0 : elem.find("=") -1]
#         rhs = elem[elem.find("=") + 2 : len(elem)]
#         lhs_flat = lhs
#         rhs_flat = rhs
#         
#         if "ST" in lhs : 
#             lhs_flat = "STORE : " + doMath(lhs)
#         
#         rhs_flat = doMath(rhs)
#         flat = lhs_flat + " = " + rhs_flat
#         flatList.append(flat)
#     
# #     for elem in myList:
# #         lhs = elem[0 : elem.find("=") -1]
# #         rhs = elem[elem.find("=") + 2 : len(elem)]
# #         flat = lhs + " = " + doMath(rhs)
# #         flatList.append(flat)
#         
#     print "------ FLATLIST OUTPUT ------"
#     for e in flatList :
#         print e
#        
#     return flatList


##############################################################



def checkPostconditions(gadget, argnum, ftype):
    
    pe2 = ["rcx", "rdx"]
    pe3 = ["rcx", "rdx", "r8"]
    pe4 = ["rcx", "rdx", "r8", "r9"]
    elf2 = ["rdi", "rsi"]
    elf3 = ["rdi", "rsi", "rdx"]
    elf4 = ["rdi", "rsi", "rdx", "rcx"]
    elf5 = ["rdi", "rsi", "rdx", "rcx", "r8"]
    elf6 = ["rdi", "rsi", "rdx", "rcx", "r8", "r9"]
    
    target = ftype + str(argnum)
       
    regstocheck = []
    
    if target == "pe2": regstocheck = pe2
    elif target == "pe3": regstocheck = pe3
    elif target == "pe4": regstocheck = pe4
    elif target == "elf2": regstocheck = elf2
    elif target == "elf3": regstocheck = elf3
    elif target == "elf4": regstocheck = elf4
    elif target == "elf5": regstocheck = elf5
    elif target == "elf6": regstocheck = elf6
    
    loadableregs = []
    
    
    for p in gadget.postconditions:
        
        if "put(rdi)" in p:
            if "load" in p and "get(rsp)" in p:
                loadableregs.append("rdi")
        if "put(rsi)" in p:
            if "load" in p and "get(rsp)" in p:
                loadableregs.append("rsi")
        if "put(rcx)" in p:
            if "load" in p and "get(rsp)" in p:
                loadableregs.append("rcx")
        if "put(rdx)" in p:
            if "load" in p and "get(rsp)" in p:
                loadableregs.append("rdx")
        if "put(r8)" in p:
            if "load" in p and "get(rsp)" in p:
                loadableregs.append("r8")
        if "put(r9)" in p:
            if "load" in p and "get(rsp)" in p:
                loadableregs.append("r9")
                
    
    
    if len(set(loadableregs).intersection(set(regstocheck))) != argnum:
        return -1
    else:
        return 0


def dumpGadgets(gadgets, fn):
    f = open(fn, 'wb')
    dill.dump(gadgets, f)
    f.close()


def readGadgets(fn):
    gadgets = []

    f = open(fn, 'rb')
    while True:
        try:
            g = dill.load(f)
            gadgets += g
        except EOFError:
            break
    f.close()
       
    return gadgets


def worker_start(args):
#     results_good = []
#     results_bad = []
    
    if Options.DEBUG_PROCESSES:
        sys.stdout = open("/tmp/" + str(os.getpid()) +".out", "w")
    queue = args[0]
    result_queue = args[1]
    hexdata = myshare.array

    while True:
        try:
            task = queue.get()
            if type(task) is type("string"):
                print "Got RETURN message. Returning..."
                queue.task_done()
                break
             
            arch = task['arch']
            foffset = task['foffset']
            offset = task['offset']
            maxlen = task['maxlen']
            minlen = task['minlen']
            hexdata_i = task['hexdata_i']
            data = hexdata[hexdata_i]
              
            progress = (100. / len(data) * offset)
      
            print "", progress, "/100", offset, "/", len(data)
              
            gg, bg = find_gadgets(arch, data, foffset, offset, maxlen, minlen)
            result_queue.put([gg, bg])
#             for g in gg:
#                 results_good.append(g)
#             for g in bg:
#                 results_bad.append(g)
            queue.task_done()
        except:
            print "exception! ", traceback.format_exc()
            queue.task_done()
    
    print "finish process ", os.getpid()
    sys.stdout.flush()

#     return [results_good, results_bad]
    
def initProcess(share):
    myshare.array = share
  
 
# create new file 'fn', overwrite existing file if it exists
# returns file handler to 'fn'
def createCleanFile(fn):
    f = open(fn, "w")
    f.close()
    f = open(fn, "ab")
    return f 
  
# open all files to write gadgets
# returns file handlers to all files
def openGadgetFiles(bin_in, output_directory):

    if not output_directory is None:
        bin_in = os.path.join(output_directory, os.path.basename(bin_in))

    fn_objects = bin_in + ".pkl"
    f_objects = createCleanFile(fn_objects)
    
    fn_ggadgets = bin_in + "_gadgets"
    f_ggadgets = createCleanFile(fn_ggadgets)
    
    fn_all_gadgets = bin_in + "_all_gadgets"
    f_all_gadgets = createCleanFile(fn_all_gadgets)
    
    fn_bgadgets = bin_in + "_bad.pkl"
    f_bgadgets = createCleanFile(fn_bgadgets)
    
    return f_objects, f_ggadgets, f_all_gadgets, f_bgadgets

# close all file handlers
def closeGadgetFiles(files):
    for f in files:
        f.close()

# dump gadgets 'gadgets' to disk with file handler 'f'
def dumpGadgetsToFile(gadgets, f, spm):
        
    for g in gadgets:
        f.write("0x%x : " %(g.address))
        for i in g.instructions:
            f.write(i + " ; ")
        f.write("\nPreconditions: %s\n" %(g.preconditions))
        
        postconds_write = []
        for post in g.postconditions:
            if "store" not in post:
                postconds_write.append(post)
        
        if spm == 0:
            f.write("Postconditions: %s\n" %(postconds_write))
        else:
            f.write("Postconditions: %s\n" %(g.postconditions))
        f.write("Bytestream: %s\n" %(g.opcodes))
        f.write("Length: %i\n\n" %(g.length))
        
# dump gadgets 'gg' and 'bg' to disk using file handlers
# f_objects to write gadget objects, f_ggadgets to write good gadgets
# and f_all_gadgets to write all gadgets
def dumpCurrentGadgets(gg, bg, f_objects, f_ggadgets, f_all_gadgets, f_bad_gadgets, spm):
    
        dill.dump(gg + bg, f_objects)
        dumpGadgetsToFile(gg, f_ggadgets, spm)
        dumpGadgetsToFile(gg + bg, f_all_gadgets, spm)
        #dill.dump(bg, f_bad_gadgets)

def ROPunzel(arch, inputbinary, minlenp, maxlenp, argnum, spm, output_directory):
    global archlen
    global bin_in
    global hexdata
    global progress
    allgg = []
    
    
    start_time = time.time()
    
    bin_in = inputbinary
       
    #if input ends with .pkl, skip everything regarding gadget discovery!
    if bin_in.endswith(".pkl"):
        print "Reading pkl file..."
        goodgadgets = readGadgets(bin_in)
        print "Done. Loaded %i gadgets" %len(goodgadgets)
    else:
        # clean up first
        try:
            os.remove(bin_in + "_gadgets")
            os.remove(bin_in + "_gadgets_debug")
        except:
            pass
        
              
        maxlen = maxlenp
        minlen = minlenp
                
        ftype = ""
        data = getCodeSegments(bin_in)
        
        # quick and dirty, for now use file extensions, if it's exe or dll it's a PE, otherwise ELF
        # if the user uses a non-executable file he/she should reconsider their life choices
        if inputbinary[len(inputbinary) - 4 : len(inputbinary)] == ".exe":
            ftype = "pe"
        elif inputbinary[len(inputbinary) - 4 : len(inputbinary)] == ".dll":
            ftype = "pe"
        else:
            ftype = "elf"
        
        hexdata = []
        for s in data:
            print s['name']
            print s['addr']
            rawdata = s['hexStream']
            #rawdata = "5E584158C35FC3".lower()
            new_hexdata = Array('c', len(rawdata), lock=False)
            hexdata.append(new_hexdata)
            new_hexdata[:len(rawdata)] = rawdata
        
        print "# processes: ", Options.NBR_PROCESSES
        pool = Pool(processes=Options.NBR_PROCESSES, initializer=initProcess, initargs=(hexdata,));
        print "creating manager..."
        manager = Manager()    
        print "creating worker queue..."
        work_queue = manager.Queue()
        result_queue = manager.Queue()
        print "maping NBR_PROCESSES processes..."

        for i in range(Options.NBR_PROCESSES):
            pool.apply_async(worker_start, ([work_queue, result_queue,],))

        # create tasks for workers
        hexdata_i = 0
        for s in data:
            print "section name: ", s['name']
            print "section addr: ", s['addr']
                
            new_hexdata = hexdata[hexdata_i]

            # finding ret instruction in current code section
            print "Finding RET offsets...\n"    
            offset = 0
            ret = ["c3", "c2"]       
            while offset < len(new_hexdata):
                #read a byte
                opcode = new_hexdata[offset : offset + 2]   
                if opcode in ret :
                    task = {}
                    task['arch'] = arch
                    task['foffset'] = s['addr']
                    task['offset'] = offset
                    task['maxlen'] = maxlen
                    task['minlen'] = minlen
                    task['hexdata_i'] = hexdata_i
                    qsize = work_queue.qsize()
                    if qsize % 1000 == 0:
                        print "qsize: ", qsize
                    work_queue.put(task)
                offset += 2
            
            
            # processing next code section
            hexdata_i = hexdata_i +1

        len_gg = 0
        len_bg = 0
        
        # open files
        fo, fgg, fag, fb = openGadgetFiles(bin_in, output_directory)

        # consume results
        current_gg = []
        current_bg = []
        while not work_queue.empty():
            while not result_queue.empty():
                gg, bg = result_queue.get()
                len_gg += len(gg)
                len_bg += len(bg)
                
                current_gg += gg
                current_bg += bg
                
                if len(current_gg) + len (current_bg) > 1000:
                    print "dumping gadgets to disk..."
                    dumpCurrentGadgets(current_gg, current_bg, fo, fgg, fag, fb, spm)
                    allgg += gg
                    current_gg = []
                    current_bg = []  
                
                result_queue.task_done()
                qsize = result_queue.qsize()

        # dump remaining gadgets
        if len(current_gg) + len (current_bg) > 0:
            print "dumping remaining gadgets to disk..."
            dumpCurrentGadgets(current_gg, current_bg, fo, fgg, fag, fb, spm)
            
        # sending special message to workers to ask them to return
        print "waiting for processes to compute gadgets..."
        while not work_queue.empty():
            sleep(2)
#             print "size: ", work_queue.qsize()
#             print "pool processes: ", pool._processes
        pool.close()  
        print "sending RETURN messages..."
        for i in range(Options.NBR_PROCESSES):
            work_queue.put("RETURN") 
        print "pool: ", work_queue.qsize()
        while not work_queue.empty():
            sleep(2)
            print "size: ", work_queue.qsize()
            print "pool processes: ", pool._processes
        work_queue.join()
        print 'close pool'
        sleep(2) # do not remove
        pool.close()
        print "join pool"
        pool.join()
        print "processes ended."
        
        
        # empty results
        while not result_queue.empty():
            gg, bg = result_queue.get()
            len_gg += len(gg)
            len_bg += len(bg)
            
            print "dumping yet remaining gadgets to disk..."
            dumpCurrentGadgets(gg, bg, fo, fgg, fag, fb, spm)
            
            result_queue.task_done()
            qsize = result_queue.qsize()
                           
        print("Total: %i\tGood: %i\tBad: %i" %((len_gg + len_bg), len_gg, len_bg))
        
        # write summary
        summary = open(bin_in + "_summary", "w+")
        summary.write("Total: %i\tGood: %i\tBad: %i\n" %((len_gg + len_bg), len_gg, len_bg))
        summary.write("--- %s seconds ---" % (time.time() - start_time))
        summary.close()
        
        # close gadget files
        closeGadgetFiles([fo, fgg, fag])
        
        # read gadgets from file
        goodgadgets = readGadgets(bin_in + ".pkl")
                
        print("Finished!\n")
              
        
    # Till here it's all gadget discovery and analysis, i.e., computing summaries    
    
    callprec = findCallPrecGadgets(goodgadgets)
    print "Call-preceded gadgets: %i" %len(callprec)
    
    callprec = filterSemiStrict(callprec)
    print "Call-preceded gadgets without bad instructions: %i" %len(callprec)
    
    for g in callprec:
        g.instructions = g.instructions[1:len(g.instructions)]
    
    # uncomment to use only call-preceded, good gadgets!
    goodgadgets = callprec
           
    goodgadgets, badgadgets = filterStrict(goodgadgets)
    
    badgadgets = []
    allgadgets = []
    
    
    # for some reason (something must have broke) i have to reanalyze the gadgets, otherwise some are weird. no idea...
    for g in goodgadgets:
        gadget = g.opcodes
        
        # handle calls. doesn't work with r8-r15 calls yet, which are prefixed with 41.
        if gadget[0:2] == "e8":
            gadget = gadget[10 : len(gadget)]
        elif gadget[0:4] == "ff15":
            #print gadget
            gadget = gadget[12 : len(gadget)]
        elif gadget[0:3] == "ff1":
            gadget = gadget[4 : len(gadget)]
            #print gadget
        elif gadget[0:3] == "ffd":
            gadget = gadget[4 : len(gadget)]
            #print gadget
        elif gadget[0:2] == "ff":
            #print gadget
            gadget = gadget[6 : len(gadget)]
        
        gadget_c = convertXCS(gadget)
        instructions = []
        
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        disas = ""
        
        for (address, size, mnemonic, op_str) in md.disasm_lite(gadget_c, 0):
            disas += mnemonic + " " + op_str + " ; "
            instructions.append(mnemonic + " " + op_str)
    
        posts, pres, pre, post = passZero(gadget_c, arch)
                    
        if posts != "err":
            gtype = determine_type(posts)
        gadget = Gadget(g.address, gadget, pres, pre, posts, post, 0, gtype, 0, len(instructions), instructions, "", "")
        allgadgets.append(gadget)
    
    goodgadgets = allgadgets
       
    print "Grading gadgets...\n"
    goodgadgets = calcGadgetQuality(goodgadgets)
    
    print "Revising gadget types...\n"
    goodgadgets = changeType(goodgadgets)
      
    
    #findHeuristicBreaker(goodgadgets, inputbinary)
    
    #return
    
    #discard all gadgets under a certain length
#     minglen = minlenp # minimum gadget length to be used for chaining (for bypassing ropocop)
#     gg_tmp = goodgadgets
#     goodgadgets = []
#     for g in gg_tmp:
#         if g.length >= minglen:
#             goodgadgets.append(g)
#     
#     print "%i gadgets after filtering for minimum length.\n" %len(goodgadgets)
    
    #for g in goodgadgets:
        #print "@" + str(g.opcodes) + " - " + str(g.address) + " - " + str(g.instructions)
    
        
    goodloads = goodLoads(goodgadgets)
    bestloads = bestLoads(goodgadgets)
    
    minglen = 0
    
    # find most suitable gadget(s) to initialize each register
    rdi, rsi, rcx, rdx, r8, r9 = find_gadget_candidates(goodgadgets, minglen)
    
    print "Using the following gadgets:"
    try:
        print "rdi: " + str(rdi.instructions) + "@" + str(rdi.address)
    except:
        print "No gadget found for rdi."
    
    try:    
        print "rsi: " + str(rsi.instructions) + "@" + str(rsi.address)
    except:
        print "No gadget found for rsi."
        
    try:
        print "rcx: " + str(rcx.instructions) + "@" + str(rcx.address)
    except:
        print "No gadget found for rcx."
        
    try:
        print "rdx: " + str(rdx.instructions) + "@" + str(rdx.address)
    except:
        print "No gadget found for rdx."
        
    try: 
        print "r8: " + str(r8.instructions) + "@" + str(r8.address)
    except:
        print "No gadget found for r8."
    
    try:
        print "r9: " + str(r9.instructions) + "@" + str(r9.address)
    except:
        print "No gadget found for r9."
    
   
    if ".dll" in inputbinary or ".exe" in inputbinary:
        ftype = "pe"
        # we only prepare registers and on Windows only the first four arguments are passed in registers
        if argnum > 4:
            argnum = 4
    else:
        ftype = "elf"
        if argnum > 6:
            argnum = 6

    #all possible permutations
    #there's probably a much nicer way of doing this but this is a prototype
    if ftype == "elf":
        if argnum == 2:
            perm_gadgets = combineGadgetsELF2(rdi, rsi)
        elif argnum == 3:
            perm_gadgets = combineGadgetsELF3(rdi, rsi, rcx)
        elif argnum == 4:
            perm_gadgets = combineGadgetsELF4(rdi, rsi, rcx, rdx)
        elif argnum == 5:
            perm_gadgets = combineGadgetsELF5(rdi, rsi, rcx, rdx, r8)
        elif argnum == 6:
            perm_gadgets = combineGadgetsELF6(rdi, rsi, rcx, rdx, r8, r9)
    elif ftype == "pe":
        if argnum == 2:
            perm_gadgets = combineGadgetsPE2(rcx, rdx)
        elif argnum == 3:
            perm_gadgets = combineGadgetsPE3(rcx, rdx, r8)
        elif argnum == 4:
            perm_gadgets = combineGadgetsPE4(rcx, rdx, r8, r9)
    else:
        print "Input file is not ELF or PE!"
        return
        

    if perm_gadgets == 0:
        print "Exiting..."
        return

    if args.architecture == "x86" :
        md = Cs(CS_ARCH_X86, CS_MODE_32)
        archlen = 4
    elif args.architecture == "x86-64" : 
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        archlen = 8
    else :
        print "Bitlength needs to be 32 or 64!"
        return
            

    # evaluate permutations, stop after the first one is found
    # loop through them, check if all registers required are rsp-relative
    for index, r in enumerate(perm_gadgets):
        print "Trying permutation ", index
        conc = conc_gadgets(r)
        gadget_readable = conc
        gadget = convertXCS(conc)
        
        if gadget != 0:
            post_simple, pre_simple, pre, post = passZero(gadget, arch)
            gadget = Gadget(0, gadget_readable, pre_simple, pre, post_simple, post, "grade", "notype", 0, 0, "", "", "")
            
            if checkPostconditions(gadget, argnum, ftype) == -1:
                print "fail"
            else:
                print "success"
                break
    
    firstgadget = gadget
    firstchain = list(r)
    for g in firstchain:
        ins = ""
        for i in g.instructions:
            ins += i + " ; "
        print "0x%x:\t%s" %(g.address, ins)
        
        
    #return
    
    
    #summarize pre and postconditions
    print firstgadget.opcodes
    print "Dereferenced registers:"
    print summarizePreconds(firstgadget.preconditions)
    print "Postconditions:"
    print interestingPostconds(firstgadget.postconditions)
    print "---------------------"
   

    satchain = []
    for p in summarizePreconds(firstgadget.preconditions):
        if p != "rsp":
            satadd = initSatPrecond(p, bestloads, goodloads)
            if satadd == 0:
                print "Exiting..."
                return
            else:
                satchain += satadd
    
    satchain += firstchain
    
    
    return
    
    print "THE FINAL CHAIN:"
    for g in satchain:
        ins = ""
        for i in g.instructions:
            ins += i + " ; "
        print "0x%x:\t%s" %(g.address, ins)
        padding = rspPadding(g)
        if padding != "":
            print padding
    
    return
    

if __name__ == "__main__":
   
    
    parser = argparse.ArgumentParser(
        description="This is InspectorGaget, a tool to analyze gadgets")
    
    parser.add_argument(
        '-a',                
        '--architecture',
        help="Specify architecture (x86 or x86-64)",
        default="x86-64")
    
    parser.add_argument(
        '-b',
        '--binary',
        help="Input binary",
        default=None)

    parser.add_argument(
        '-o',
        '--output_directory',
        help="Output directory",
        default=None)
    
    parser.add_argument(
        '-minlen',
        '--minimum_length',
        help="Minimum length of gadgets (ignored if input is a pkl file)",
        default=1)

    parser.add_argument(
        '-maxlen',
        '--maximum_length',
        help="Maximum length of gadgets (ignored if input is a pkl file)",
        default=25)

    parser.add_argument(
        '-p',
        '--processes',
        help="Number of processes (Default 1)",
        default=None)
    
    parser.add_argument(
        '-s',
        '--code_size',
        help="Count the total size of all code section of all binaries in a directory (for debugging)",
        default=None)
    
    parser.add_argument(
        '-arg',
        '--arguments',
        help="Number of arguments the autochainer should set up. (2 to 6 for Linux, 2 to 4 for Windows)",
        default=None)
    
    parser.add_argument(
        '-spm',
        '--show_post_memory',
        help="Show postconditions of memory locations",
        default=None)
          
    parser.add_argument(
        '-d',                
        '--dump-hexa',
        help="Dump all code sections of the input binary in hexadecimal",
        default=None)
    

    args = parser.parse_args()
    
    if not args.dump_hexa is None:
        filename = args.dump_hexa
        if not os.path.isfile(filename):
            print "unknow file: ", filename
            sys.exit(-1)
        try:
            s = getHexStreamsFromElfExecutableSections(filename)
            for section in s:
                print "ELF", filename, section['name'], section['addr'], section['hexStream']
        except:
            try:
                s = getHexStreamFromPE(filename)
                for section in s:
                    print "PE", filename, section['name'], section['addr'], section['hexStream']
            except:
                print "not a binary: ", filename
        exit(0)
    
    if not args.show_post_memory is None:
        spm = 1
    else:
        spm = 0
    
    
    if not args.code_size is None:
        print "code size: "
        dirn = args.code_size
        total_length = 0
        for fn in os.listdir(dirn):
            filename = dirn + "/" +fn
            try:
                s = getHexStreamsFromElfExecutableSections(filename)
                print "ELF binary code sections : ", len(s)
                for section in s:
                    hs = section['hexStream']
                    total_length += len(hs)
            except:
                try:
                    s = getHexStreamFromPE(filename)
                    print "PE binary: ", len(s) 
                    for section in s:
                        hs = section['hexStream']
                        total_length += len(hs)
                except:
                    print "not a binary: ", filename
        print "total length of all code sections: ", total_length / 2 / 1024
        sys.exit(0)
    

    if args.binary == None:
        parser.error("no binary specified!")
        print "no binary specified!"

        
    if int(args.arguments) < 2:
        parser.error("number of arguments for the autochainer must be at least 2!")
        print "number of arguments for the autochainer must be at least 2!"

    
    if not args.processes is None:
        Options.NBR_PROCESSES = int(args.processes)
        print "Number of processes: ", Options.NBR_PROCESSES
    
    print "Starting inspector gadget..."
    
  
    
    #ROPunzel / Inspector Gadget / PSHAPE
    ROPunzel(args.architecture, args.binary, int(args.minimum_length), int(args.maximum_length), int(args.arguments), spm, args.output_directory)
    

def doAnalysis(gadget, architecture):
    pass # TODO
