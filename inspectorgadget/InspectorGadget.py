import gadgetfinder.filters as filters
from gadgetfinder import extractor as extractor
import gadgetfinder.storage as storage
#
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
import Options
import traceback
import operator
import logging

logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)
log = logging.getLogger(__name__)

archlen = 0
EQUAL = " = "

def getRightHandSide(p):
    assert EQUAL in p
    sp = p.split(EQUAL)
    assert len(sp) is 2
    return sp[1]

def getLeftHandSide(p):
    assert EQUAL in p
    sp = p.split(EQUAL)
    assert len(sp) is 2
    return sp[0]

##############################################################
# takes a string of arbitrary length and formats it 0x for Capstone
def convertXCS(s):
    assert type(s) is type("a")
    if len(s) < 2: 
        print("Input too short!")
        return 0
    
    if len(s) % 2 != 0:
        print("Input must be multiple of 2!")
        return 0

    conX = b''
    
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
                #print(p)
                if not "store" in post:
                    nonmempostconds += 1
            
            usedregs = len(summarizePreconds(g.preconditions))
            
            grade = usedregs * 1.2 + nonmempostconds * 0.8
            print(g.address)
            f.write(str(g.address) + "\n")
            print(g.instructions)
            
            for i in g.instructions:
                f.write(i + "\n")
            
            #f.write(str(g.instructions) + "\n")
            print("len: " + str(g.length))
            f.write("len: " + str(g.length) + "\n")
            print("regsused: %s" % str(usedregs)) # preconditions; dereferenced registers, need to be attacker-controlled!)
            f.write("regsused: %s \n" % str(usedregs))
            print("nonmempostconds: %s" % str(nonmempostconds)) # postconds; overwritten registers)
            f.write("nonmempostconds: %s \n" % str(nonmempostconds))
            print("grade: " + str(grade))
            f.write("grade: %s" % str(grade))
            print("\n")
            f.write("\n")
            hb.append([g,g.length - grade])
    
    hb.sort(key=operator.itemgetter(1))
    
    for b in hb:
        #print(b[0].address + " _ " + str(b[0].length))
        print("@%s - length: %i - score: %f" %(b[0].address, b[0].length, b[1]))
        f.write("@%s - length: %i - score: %f\n" %(b[0].address, b[0].length, b[1]))
   

    f.close()
    


#gets a line with a put(reg) = something
#returns reg
def getRegInPut(l):
    offl = l.find("(")
    offr = l.find(")")
    
    return l[offl + 1:offr]
    

#returns all gadgets that load a register with either 
# another register, or a value from another register
# e.g., pop rax
# push rbx, pop rax, ret
# mov rax, rbx
def goodLoads(gadgets):
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", \
            "rbp", "r8", "r9", "r10", "r11", "r12",  \
            "r13", "r14", "r15"]
    gl = []
    for g in gadgets:
        goodloads = []
        
        if g.address == 4653335:
            pass
        
        for p in g.postconditions:
            log.info("postcondition: %s" % p)
            if "store" in p:
                continue
            
            reg = getRegInPut(p)
            
            # check if the same value occurs more than once
            if p.find(reg, p.find(reg) + 1) > 0:
                continue
                #print(p)
            # check if any other registers appear, otherwise a constant value is assigned, which is also not what we want
            
            rhs = getRightHandSide(p)
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
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", \
            "rbp", "r8", "r9", "r10", "r11", "r12", \
            "r13", "r14", "r15"]
    bl = []
    
    for g in gadgets:
        loadedregs = []
                
        for p in g.postconditions:
            if "store" in p:
                continue
            
            if not "load" in p:
                continue
            
            rhs = getRightHandSide(p)
            
            if not "rsp" in rhs:
                continue
            
            bad = 0
            for r in regs:
                if r in rhs:
                    bad = 1
                    break
            if bad == 0:
                #print(p)
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
        print("Nothing found...")
        return
    elif len(reg_rec) == 0:
        print("Solved!")
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
                print("Couldn't solve!!")
                return 0
            else:
                print("Solved!")
                solved = 1
      
      
    return satchain

# reg is the register that needs to be attacker controlled
def satPrecond(reg, topgadgets, propgadgets):
    
    regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    simp = []
    print("Solving for " + reg)
    
#     print("Top gadgets")
#     for g in topgadgets:
#         print(g.instructions)
#     
#     print("---")
    
    for t in topgadgets:
        if not reg in t.greatload:
            #print("skip")
            #print(t.instructions)
            continue
        else:
            for p in t.postconditions:
                lhs = getLeftHandSide(p)
                if reg in lhs:
                    if not "store" in lhs:
                        simp.append(t)
                        break
    
#     print("Good ones:")
#     for g in simp:
#         print(g.postconditions)
        
    # ideal case, there's a gadget that loads reg with a value relative to rsp (like pop reg)
    if len(simp) > 0:
        best = getBestQualityGadget(simp)
        print("Using: ")
        print(best.postconditions)
        return best, []

    # maybe the more likely case, there is no such gadget, so we need to propagate gadget values till we
    # maybe end up at a gadget that loads a register with a value relative to rsp
    # e.g., reg = "r8"; topgadgets are "pop rax ; pop rdx" ; propgadgets are "mov r8, rdx"
    # put together: pop rdx ; mov r8, rdx; therefore, r8 is attacker-controlled via rdx
    
    #print("Propgadgets:")
    for pg in propgadgets:
        if not reg in pg.goodload:
            continue
        for p in pg.postconditions:
            lhs = getLeftHandSide(p)
            if reg in lhs:
                simp.append(pg)
                break
    
    if len(simp) > 0:
        best = getBestQualityGadget(simp)
        
        for p in best.postconditions:
            lhs = getLeftHandSide(p)
            rhs = getRightHandSide(p)
            if reg in lhs:
                reg_rec = []
                for r in regs:
                    if r in rhs:
                        reg_rec.append(r)
                        
                print("Using:")
                print(p)
                print("Require solving for: ")
                print(reg_rec)
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
                #print(p)
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
    conv = conv #convertXCS(conv)
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
                #print(reg)
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
            #print("Loaded relative to RSP:" + g.opcodes)
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
    assert type(g) is type(b'')

    if g[len(g) - 1] == b'\xc3':
        return 0
    elif g[len(g) - 3] == b'\xc2':
        offset = g[len(g) - 2 : len(g)]
        offset = reverseBytes(offset)
        offset = int(offset, 16)
        return offset
    else:
        print("Gadget doesn't end with RET")
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
        print(g.opcodes)
    
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
    
#     print("Printing candidates...")
#     
#     print("rdi:")
#     for g in rdi_candidate:
#         print(g.opcodes)
#     
#     print("rsi:")
#     for g in rsi_candidate:
#         print(g.opcodes)
#     
#     print("rcx:")
#     for g in rcx_candidate:
#         print(g.opcodes)
#     
#     print("rdx:")
#     for g in rdx_candidate:
#         print(g.opcodes)
#     
#     print("r8:")
#     for g in r8_candidate:
#         print(g.opcodes)
#     
#     print("r9:")
#     for g in r9_candidate:
#         print(g.opcodes)
    
    
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
#         #print(best_rdi.opcodes)
#         print(best_rdi.instructions)
#     
#     if best_rsi != 0:
#         #print(best_rsi.opcodes)
#         print(best_rsi.instructions)
#     
#     if best_rcx != 0:
#         #print(best_rcx.opcodes)
#         print(best_rcx.instructions)
#     
#     if best_rdx != 0:  
#         #print(best_rdx.opcodes)
#         print(best_rdx.instructions)
#     
#     if best_r8 != 0:
#         #print(best_r8.opcodes)
#         print(best_r8.instructions)
#     
#     if best_r9 != 0:
#         #print(best_r9.opcodes)
#         print(best_r9.instructions)
    
    return best_rdi, best_rsi, best_rcx, best_rdx, best_r8, best_r9
    

# Concatenates gadgets, removes all RETs though, because 
# we only care about side effects on registers.
# Maybe a bad idea to remove the RETs, might change the disassembly?
def concatenate_gadgets(gadgetList):
    assert len(gadgetList) > 0, "gadgetList has no element"
    for g in gadgetList:
        log.debug("    g: %s %s %s" % (str(g), g.instructions, g.opcodes))
    gadget = b''
    
    for g in gadgetList:
        
        oc = g.opcodes
        assert type(oc) is type(b'')
        
        if oc[-1:len(oc)] == b'\xc3':
            gadget += oc[0 : len(oc) - 1]
        
        if oc[-1:len(oc)] == b'\xcb':
            gadget += oc[0 : len(oc)- 1]
        
        if oc[len(oc)-3:len(oc)-2] == b'\xc2':
            gadget += oc[0 : len(oc) - 2]
            
        if oc[len(oc)-3:len(oc)-2] == b'\xca':
            gadget += oc[0 : len(oc) - 2]
       
    return gadget
    
    
def combineGadgetsPE2(rcx, rdx):

    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print("Couldn't find gadget for rdx!")
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0

    gadgets = []
    gadgets.append(rcx)
    gadgets.append(rdx)

    
    res = list(permutations(gadgets))
       
#     gadget = rcx.opcodes + rdx.opcodes + r8.opcodes + r9.opcodes
#     gadget = gadget.replace("c3", "")
#     print(gadget)
    return res

def combineGadgetsPE3(rcx, rdx, r8):

    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print("Couldn't find gadget for rdx!")
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print("Couldn't find gadget for r8!")
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    
    res = list(permutations(gadgets))
       
#     gadget = rcx.opcodes + rdx.opcodes + r8.opcodes + r9.opcodes
#     gadget = gadget.replace("c3", "")
#     print(gadget)
    return res


def combineGadgetsPE4(rcx, rdx, r8, r9):

    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print("Couldn't find gadget for rdx!")
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print("Couldn't find gadget for r8!")
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r9 == 0:
        print("Couldn't find gadget for r9!")
        r9 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    gadgets.append(r9)
    
    res = list(permutations(gadgets))
       
#     gadget = rcx.opcodes + rdx.opcodes + r8.opcodes + r9.opcodes
#     gadget = gadget.replace("c3", "")
#     print(gadget)
    return res



def combineGadgetsELF2(rdi, rsi):

    if rdi == 0:
        print("Couldn't find gadget for rdi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print("Couldn't find gadget for rsi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    log.debug("  rdi: %s" % rdi.instructions)
    log.debug("  rsi: %s" % rsi.instructions)
    gadgets.append(rdi)
    gadgets.append(rsi)
    
    res = list(permutations(gadgets))
    
    return res


def combineGadgetsELF3(rdi, rsi, rcx):

    if rdi == 0:
        print("Couldn't find gadget for rdi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print("Couldn't find gadget for rsi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    
    res = list(permutations(gadgets))
    
    return res

def combineGadgetsELF4(rdi, rsi, rcx, rdx):

    if rdi == 0:
        print("Couldn't find gadget for rdi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print("Couldn't find gadget for rsi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print("Couldn't find gadget for rdx!")
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    gadgets.append(rdx)
    
    res = list(permutations(gadgets))
    
    return res

def combineGadgetsELF5(rdi, rsi, rcx, rdx, r8):

    if rdi == 0:
        print("Couldn't find gadget for rdi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print("Couldn't find gadget for rsi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print("Couldn't find gadget for rdx!")
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print("Couldn't find gadget for r8!")
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    
    res = list(permutations(gadgets))
    
    return res

def combineGadgetsELF6(rdi, rsi, rcx, rdx, r8, r9):

    if rdi == 0:
        print("Couldn't find gadget for rdi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rsi == 0:
        print("Couldn't find gadget for rsi!")
        rdi = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rcx == 0:
        print("Couldn't find gadget for rcx!")
        rcx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if rdx == 0:
        print("Couldn't find gadget for rdx!")
        rdx = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r8 == 0:
        print("Couldn't find gadget for r8!")
        r8 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    if r9 == 0:
        print("Couldn't find gadget for r9!")
        r9 = Gadget(0, "c3", "","", "", "", 0,"", 0,0, "", "", "")
        return 0
    
    gadgets = []
    
    gadgets.append(rdi)
    gadgets.append(rsi)
    gadgets.append(rcx)
    gadgets.append(rdx)
    gadgets.append(r8)
    gadgets.append(r9)
    
    res = list(permutations(gadgets))
    
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


class Task():
    def __init__(self):
        self.hexdata = None
        self.arch = None
        self.foffset = None
        self.maxlen = None
        self.minlen = None

def getRetOffsets(hexdata, queue, arch, foffset, maxlen, minlen):
    pass
    

def cleanInputList(statementList):
    cleanStatementList = []
    
    # Clean list from instructions we're not interested in atm
    # All flag-instructions (cc) and instructions that change IP
    for stmt in statementList:
        #print(ir.__str__())
        if "PUT" in stmt.__str__():
            if "eip" in stmt.__str__():
                #print("removing", stmt)
                #stmtsb.statements.remove(ir)
                pass
            if "rip" in stmt.__str__():
                pass
            elif "cc" in stmt.__str__():
                #print("removing", stmt)
                #stmtsb.statements.remove(ir)
                pass
            else:
                cleanStatementList.append(stmt);
        elif "IR-NoOp" in stmt.__str__():
            #stmtsb.statements.remove(ir)
            pass
        elif "IMark" in stmt.__str__():
            pass
        elif "eip" in stmt.__str__():
            pass
        elif "rip" in stmt.__str__():
            pass
        elif "cc_" in stmt.__str__():
            pass
        elif "calculate" in stmt.__str__():
            pass
        elif "AbiHint" in stmt.__str__():
            pass
        elif "CAS" in stmt.__str__():
            pass
        elif "ITE" in stmt.__str__():
            pass
        elif "amd64g_dstmttyhelper" in stmt.__str__():
            pass
        elif "Sar" in stmt.__str__():
            pass
        elif "F64toI64S" in stmt.__str__():
            pass
        elif "DivMod" in stmt.__str__():
            pass
        elif "128HIto64" in stmt.__str__():
            pass
        elif "1Uto8" in stmt.__str__():
            pass
        elif "F64toI32" in stmt.__str__():
            pass
        elif "MullU8" in stmt.__str__():
            pass
        elif "Not" in stmt.__str__():
            pass
        elif "8Uto64" in stmt.__str__():
            pass
        elif "8Sto32" in stmt.__str__():
            pass
        elif "MullS8" in stmt.__str__():
            pass
        elif "amd64g_create" in stmt.__str__():
            pass
        elif "GetMSBs8x8" in stmt.__str__():
            pass
        elif "GetMSBs8x16" in stmt.__str__():
            pass
        else:
            cleanStatementList.append(stmt)
    
    return cleanStatementList

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
    #print(retrange  )
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
                    #print(load[0 : index + 1])
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
    lhs = getLeftHandSide(l)
    rhs = getRightHandSide(l)
    log.info("lhs: "+ lhs)
    log.info("rhs: "+ rhs)
    
    precond = []
    
    # Check lhs first
    if "ST" in lhs and "GET" in lhs : 
        #print("Writable memory required at: " + lhs[lhs.find("(") : lhs.find(" = ")])
        precond.append("Writable memory required at: " + lhs[lhs.find("(") : lhs.find(" = ")] + ")") # Alex: unsure about =
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
        #print("Readable memory required: " + subl)
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
                    #print("KEEPING:" + l)
                    #print("Removing from list of registers to find:" + reg)
                    regstofind.remove(reg)
                    keepList.append(l)
    
    return keepList


def passOne32(myList):
    #log.warning("------PASS ONE------")
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
        l_st = l;
        lhs = getLeftHandSide(l_st)
        rhs = getRightHandSide(l_st)
        #print(rhs)
        #print(lhs)
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
            #print(l_st)
            if "eax" in rhs and eax_cnt > 0 :
                l_st = l_st.replace(rhs, eax_rhs)
            elif "ebx" in rhs and ebx_cnt > 0 :
                l_st = l_st.replace(rhs, ebx_rhs)
            elif "esp" in rhs and esp_cnt > 0 :
                l_st = l_st.replace(rhs, esp_rhs) 
            elif "ecx" in rhs and ecx_cnt > 0 :
                l_st = l_st.replace(rhs, ecx_rhs)
            elif "edx" in rhs and edx_cnt > 0 :
                l_st = l_st.replace(rhs, edx_rhs)
            elif "ebp" in rhs and ebp_cnt > 0 :
                l_st = l_st.replace(rhs, ebp_rhs)
            elif "esi" in rhs and esi_cnt > 0 :
                l_st = l_st.replace(rhs, esi_rhs)
            elif "edi" in rhs and edi_cnt > 0 :
                l_st = l_st.replace(rhs, edi_rhs)
         
        retList.append(l_st)
    return retList

def getStatementStrWithExplicitRegisters(irsb, s):
    stmt_str = None
    if isinstance(s, pyvex.stmt.Put):
        stmt_str = s.__str__(reg_name=irsb.arch.translate_register_name(s.offset, s.data.result_size(irsb.tyenv) // 8)) 
    elif isinstance(s, pyvex.stmt.WrTmp) and isinstance(s.data, pyvex.expr.Get):
        stmt_str = s.__str__(reg_name=irsb.arch.translate_register_name(s.data.offset, s.data.result_size(irsb.tyenv) // 8)) 
    elif isinstance(s, pyvex.stmt.Exit):
        stmt_str = s.__str__(reg_name=irsb.arch.translate_register_name(s.offsIP, irsb.arch.bits // 8)) 
    else:
        stmt_str = s.__str__()
    return stmt_str



def passOne64(statementList):
    #log.warning("------PASS ONE------")
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
    
    retStatementStrList = []
    
    for l in statementList :
        l_st = l
        lhs = getLeftHandSide(l_st)
        rhs = getRightHandSide(l_st)
        #print(rhs)
        #print(lhs)
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
            #print(l_st)
            if "rax" in rhs and rax_cnt > 0 :
                l_st = l_st.replace(rhs, rax_rhs)
            elif "rbx" in rhs and rbx_cnt > 0 :
                l_st = l_st.replace(rhs, rbx_rhs)
            elif "rsp" in rhs and rsp_cnt > 0 :
                l_st = l_st.replace(rhs, rsp_rhs) 
            elif "rcx" in rhs and rcx_cnt > 0 :
                l_st = l_st.replace(rhs, rcx_rhs)
            elif "rdx" in rhs and rdx_cnt > 0 :
                l_st = l_st.replace(rhs, rdx_rhs)
            elif "rbp" in rhs and rbp_cnt > 0 :
                l_st = l_st.replace(rhs, rbp_rhs)
            elif "rsi" in rhs and rsi_cnt > 0 :
                l_st = l_st.replace(rhs, rsi_rhs)
            elif "rdi" in rhs and rdi_cnt > 0 :
                l_st = l_st.replace(rhs, rdi_rhs)
            elif "r8" in rhs and r8_cnt > 0 :
                l_st = l_st.replace(rhs, r8_rhs)
            elif "r9" in rhs and r9_cnt > 0 :
                l_st = l_st.replace(rhs, r9_rhs)
            elif "r10" in rhs and r10_cnt > 0 :
                l_st = l_st.replace(rhs, r10_rhs)
            elif "r11" in rhs and r11_cnt > 0 :
                l_st = l_st.replace(rhs, r11_rhs)
            elif "r12" in rhs and r12_cnt > 0 :
                l_st = l_st.replace(rhs, r12_rhs)
            elif "r13" in rhs and r13_cnt > 0 :
                l_st = l_st.replace(rhs, r13_rhs)
            elif "r14" in rhs and r14_cnt > 0 :
                l_st = l_st.replace(rhs, r14_rhs)
            elif "r15" in rhs and r15_cnt > 0 :
                l_st = l_st.replace(rhs, r15_rhs)     
         
        retStatementStrList.append(l_st)

    return retStatementStrList


# Propagates ST statements to LD statements
def passTwo(myList, architecture):
    #log.warning("--- PASS TWO ---")
    #print("------PASS TWO------")
    i = len(myList) - 1
    j = 0
       
    while i >= 0 : 
        ir_s = myList[i]
        if ir_s[0] != "t" : 
            if "STle" in ir_s : 
                j = i + 1
                rhs = getRightHandSide(ir_s)
                lhs = getLeftHandSide(ir_s)
                while j < len(myList) :
                    ir_s2 = myList[j].__str__()
                    
                    if architecture == "x86" :
                        rep = "LDle:I32"+lhs[lhs.find("(") : len(lhs)]
                    elif architecture == "x86-64" :
                        rep = "LDle:I64"+lhs[lhs.find("(") : len(lhs)]
                    else : # Shouldn't happen
                        rep = "ERR"
                        
                    if (rep in ir_s2) :
                        #print("ir_s2 before:" + ir_s2)
                        ir_s2 = ir_s2.replace(rep, rhs)
                        #print("ir_s2 after:" + ir_s2)
                        myList[j] = ir_s2
                    j += 1
                # removed on 18.2 - produces crash if ST is last instruction
                # also, doesn't seem to have any use, so...
                #ir_s = ir_s2
        i -= 1

                
    #for line in myList : 
        #if line[0] != "t" :
            #log.warning(line)
    
    return myList



# Forward propagation
# Returns posts, pres, post, pre
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
    else:
        raise Exception("unsupported architecture: %s" % architecture)
      
    log.warning("------------ original list -----------")
    for ir in irsb.statements :
        log.info(ir)
   
    #sr.putExplicitRegistersInIRSBStatements(irsb)

    myList = cleanInputList(irsb.statements)
    log.warning("------------ clean list -----------")
    for ir in myList:
        log.info(ir)
    
    log.warning("----------------")

    statementStrList = []
    for s in myList: 
        s_str = getStatementStrWithExplicitRegisters(irsb, s)
        statementStrList.append(s_str)

    
    if architecture == "x86" :
        statementStrList = passOne32(statementStrList)
    elif architecture == "x86-64" :
        statementStrList = passOne64(statementStrList)
        
    log.warning("------------ clean list (after 1st pass) -----------")
    for ir in statementStrList:
        log.info("statementStrList element: " + str(ir))
    #quit()
    
    #statementStrList = []
#     statementStrList.append("t1 = GET:I32(eax)")
#     statementStrList.append("t2 = Add32(t1,0x00000040)")
#     statementStrList.append("PUT(eax) = t2")
#     statementStrList.append("t1 = 0x00000001")
#     statementStrList.append("t2 = 0x00000002")
#     statementStrList.append("t3 = Add32(GET:I32(Add32(GET:I32(eax),t2)),t1)")
#      
#     print("------------ fake list -----------")
#     for ir in statementStrList:
#         print(ir)
#      
#     print("----------------")
    
    #err = open("err.txt", "wb")

    #statementStrList = putExplicitRegistersInGadgets(statementStrList)
   
    i = 0
    j = 0
    
    #print("Entering...")
    #print(hex(ra))
    #print(gr)
    
    while i < len(statementStrList) :
        log.info("i is "+ str(i) +": '"+ statementStrList[i] +"'")
        ir_s = statementStrList[i]
        tregex = getRightHandSide(ir_s).strip()
        treg = getLeftHandSide(ir_s).strip()
        log.info("tregex: " + str(tregex))
        log.info("treg: " + str(treg))
        #print("tregex:", tregex)
        #print("treg:", treg)
        
        if (treg[0] != "t") : 
            treg = "NOREG";
        
        i += 1
        j = i
        
        while j < len(statementStrList) : 
            log.info("j is " +  str(j) + ": '" + statementStrList[i] +"'")
            ir_s2 = statementStrList[j]
            #print("Looking for {0} in {1}".format(treg, ir_s2))
            # Get the right hand side of the assignment
            rhs = getRightHandSide(ir_s2)
            lhs = getLeftHandSide(ir_s2)
            log.info("lhs: "+ str(lhs))
            log.info("rhs: "+ str(rhs))
            #print("RHS:", rhs)
            off = rhs.find(treg)
            if off == -1:
                pass
            if off == 0:
                pass
            #print("off:", off)
            #print("rhs:", rhs)
            #print("len", len(ir_s2[off:len(ir_s2)]))
            off_l = lhs.find(treg)
            
            # Check if the treg has been found
            if (off != -1) :
                # Check if the right hand side is treg
                if (rhs == treg) :
                    # Must be a simple assignment like PUT(esi) = t1 or t8 = t1 ; but cannot be t5 = t11
                    #print("Simple Assignment"; ###correct!)
                    #print("rhs before:", rhs)
                    rhs = rhs.replace(treg, tregex)
                    #print("Replaced {0} with {1}".format(treg, tregex))
                    #print("rhs after",rhs)

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
                            #print("Complex Assignment (one Op)", ir_s2)
                            #print("rhs before:", rhs)
                            rhs = rhs.replace(treg, tregex)
                            #print("Replaced {0} with {1}".format(treg, tregex))
                            #print("rhs after",rhs)
                    else : # there are commas, so check all operands                       
                        line = ""
                        lines = rhs.split(",")
                        for lin in lines : 
                            log.info("line: " + lin)
#                             print("----")
#                             print("treg:", treg)
#                             print("tregex:", tregex)
#                             print("LIN:", lin)
                            # FIX 18.2
                            # added len(treg) < len(lin) otherwise it might crash if the treg is longer
                            # than an element of the line
                            if (len(treg) < len(lin) and lin[len(treg)] == ")" and treg in lin) :
                                #replace
                                lin = lin.replace(treg, tregex)
                                #print("Replaced {0} with {1}".format(treg, tregex))
                                #print("line after",lin)
                            elif (lin[len(lin) - len(treg) == "("] and treg in lin and (lin.find(treg) + len(treg) == len(lin))) :
                                #print("lin", line)
                                #print(ir_s2)
                                #print("FOUND LEFT111111")
                                lin = lin.replace(treg, tregex)
                            line = line + lin + ","
                        #print("AFTER REPLACEMETNS:", line)
                        #print("RHS:", rhs)
                        rhs = line[0 : len(line) - 1]
                                
                        #print("the following line was split:", rhs)
                        #for lin in lines : 
                            #print("split line", lin)
                        
                            
                                    
                ir_s2 = lhs + EQUAL + rhs
                #print("******* NEW:", ir_s2)
                log.info("******* NEW: "+ str(ir_s2))
                statementStrList[j] = ir_s2
            
            if (off_l != -1 and lhs[0] != "t") : 
                if (lhs[off_l + len(treg)] == ")") :
                    lhs = lhs.replace(treg, tregex)
                    # Just replace lhs
                    ir_s2 = lhs + EQUAL + rhs
                    statementStrList[j] = ir_s2
            
            j += 1
        
    log.info("end of while loop.")
    #err.close()
    #log.warning("######################")
    #for elem in statementStrList: 
        #if elem.__str__()[0] != "t" :
            #print(elem)
        #log.warning(elem)
        
    #statementStrList = filterTRegs(statementStrList)
    
    #print("Filtered (Removed Tregs)")
    #for elem in statementStrList: 
        #print(elem)
       
 
    preconds = []
        
    # Finding preconditions BEFORE multiple assignments are removed
    # E.g. in case of pop eax # mov eax, 5
    log.info("start finding preconditions")
    for elem in statementStrList : 
        pre = getPreconditions(elem)
        preconds = preconds + pre
    log.info("end finding preconditions")
    
    # Get rid of multiple preconditions the cheap way (convert to set and back to list)
    # Since the order of the elements does not matter, this is fine
    preconds = list((set(preconds)))
        
    statementStrList = passTwo(statementStrList, architecture)
    statementStrList = filterDuplicateAssignments(statementStrList, architecture)
    
    #log.warning("------Cleaned output from multiple assignments to the same register------")
    #for elem in statementStrList: 
        #if elem.__str__()[0] != "t" :
            #print(elem)
        #log.warning(elem)
    
    postconds_simple = []
    postconds = []
    log.warning("------Finding Postconditions------")
    for elem in statementStrList : 
        post = getPostconditions(elem)
        postconds.append(post)
        log.info("post: " + str(post))
        sr_left = SymRepresentation(post.split(EQUAL)[0])
        sr_right = SymRepresentation(post.split(EQUAL)[1])
        log.info("left: "+ str(sr_left))
        log.info("right: "+ str(sr_right))
        simp_left = sr_left.simplify()
        simp_right = sr_right.simplify()
        log.warning("    ----> simplified: [%s]  =  [%s]", simp_left, simp_right)
        postconds_simple.append(str(simp_left) + EQUAL + str(simp_right))
    
    preconds_simple = []
    log.warning("------Finding Preconditions------")
    for pre in preconds :
        log.info("pre: " + str(pre))
        substr = pre[pre.find(":") + 3 : len(pre) - 1]
        log.info("substr: "+ substr)
        sr = SymRepresentation(substr)
        log.info("sr: "+ str(sr))
        simp = sr.simplify()
        #simp = sr
        log.warning("    ----> simplified: [%s]", simp)
        preconds_simple.append(str(simp))
  

    #postconds_simple = putExplicitRegistersInGadgets(postconds_simple)
    #preconds_simple = putExplicitRegistersInGadgets(preconds_simple)
    #postconds = putExplicitRegistersInGadgets(postconds)
    #preconds = putExplicitRegistersInGadgets(preconds)
    log.info("returning results")
    return postconds_simple, preconds_simple, preconds, postconds

    # WIP
#     log.warning("------Simplified Preconditions------")
#     ranges = getRangePreconditions(simplist, "x86")
#     for elem in ranges : 
#         log.warning(elem)
    
# def unusedCode():
#     
#     # DoMath sucks
#     flatList = []
#     
#     for elem in statementStrList :
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
# #     for elem in statementStrList:
# #         lhs = elem[0 : elem.find("=") -1]
# #         rhs = elem[elem.find("=") + 2 : len(elem)]
# #         flat = lhs + " = " + doMath(rhs)
# #         flatList.append(flat)
#         
#     print("------ FLATLIST OUTPUT ------")
#     for e in flatList :
#         print(e)
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

    log.info("target is %s. Regstocheck are '%s'." % (target, regstocheck))
    
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

# main 
def ROPunzel(arch, bin_in, minlenp, maxlenp, argnum, spm, output_directory, test_hexdata=None):
    global archlen
    global hexdata
    global progress
    allgg = []
   
    goodgadgets = None
    #if input ends with .pkl, skip everything regarding gadget discovery!
    if bin_in.endswith(".pkl"):
        print("[+] Reading pkl file...")
        goodgadgets = storage.readGadgets(bin_in)
        print("[+] Done. Loaded %i gadgets" %len(goodgadgets))
    else:
        # check if gadgets were already extracted
        pkl_fn = os.path.join(out_dir, os.path.basename(bin_in) + ".pkl")
        if os.path.isfile(pkl_fn):
            print("[+] Reading gadgets from existing pkl file '%s'" % pkl_fn)
            goodgadgets = storage.readGadgets(pkl_fn)
        else:
            print("[+] Extracting gadget from binary file '%s'" % bin_in)
            goodgadgets = extractor.extractGadgets(arch, bin_in, out_dir, maxlenp, minlenp, Options.NBR_PROCESSES, spm) 

#    for g in goodgadgets:
#        print("gg: %s" % g.instructions)
#        print("   %s" % g.postconditions)
#        print("   %s" % g.preconditions)


    # Below it's all gadget discovery and analysis, i.e., computing summaries    

    target_gadgets = None
    TARGET_CALLPREC_GADGETS_ONLY = False # TODO: add option for this

    if TARGET_CALLPREC_GADGETS_ONLY:
        callprec = findCallPrecGadgets(goodgadgets)
        log.info("Call-preceded gadgets: %d" % len(callprec))
    
        callprec = filters.filterSemiStrict(callprec)
        log.info("Call-preceded gadgets without bad instructions: %d" % len(callprec))
    
        for g in callprec:
            g.instructions = g.instructions[1:len(g.instructions)]
    
        target_gadgets = callprec
    else:
        target_gadgets = goodgadgets

    goodgadgets, badgadgets = filters.filterStrict(goodgadgets)
    print("[+] Good gadgets #: %d" % len(goodgadgets))
    
    badgadgets = []
    allgadgets = []
    
#    # for some reason (something must have broke) i have to 
#    # reanalyze the gadgets, otherwise some are weird. no idea...
#    gadget_i = 0
#    for g in goodgadgets:
#        gadget = g.opcodes
#        assert type(gadget) is type(b'\x00')
#        log.info("gadget (%d/%d): %s" % (gadget_i,len(goodgadgets),str(gadget)))
#        gadget_i += 1
#
#        # handle calls. doesn't work with r8-r15 calls yet, which are prefixed with 41.
#        if gadget[0:1] == b'\xe8': # check if starts with "0xe8"
#            gadget = gadget[5 : len(gadget)]
#        elif gadget[0:2] == b'\xff\x15': # check if starts with "0xff15"
#            #print(gadget)
#            gadget = gadget[6 : len(gadget)]
#        elif gadget[0:1] == b'\xff' and gadget[1] & 0x10: # check if starts with "0xff1"
#            gadget = gadget[2 : len(gadget)]
#            #print(gadget)
#        elif gadget[0:1] == b'\xff' and gadget[1] & 0xd0: # check if starts with "0xffd"
#            gadget = gadget[2 : len(gadget)]
#            #print(gadget)
#        elif gadget[0:1] == b'\xff': # check if starts with "0xff"
#            #print(gadget)
#            gadget = gadget[3 : len(gadget)]
#        
#
#        #gadget_c = convertXCS(gadget)
#        instructions = []
#        
#        md = Cs(CS_ARCH_X86, CS_MODE_64)
#        disas = ""
#        
#        for (address, size, mnemonic, op_str) in md.disasm_lite(gadget, 0):
#            disas += mnemonic + " " + op_str + " ; "
#            instructions.append(mnemonic + " " + op_str)
#            log.info("   instruction: " + mnemonic + " " + op_str)
#    
#        posts, pres, pre, post = passZero(gadget, arch)
#                    
#        if posts != "err":
#            gtype = determine_type(posts)
#        gadget = Gadget(g.address, gadget, pres, pre, posts, post, 0, gtype, 0, len(instructions), instructions, "", "")
#        allgadgets.append(gadget)
#    
#    goodgadgets = allgadgets
       
    print("[+] Grading gadgets...")
    print("[+] Goodgadgets: %d" % len(goodgadgets))
    for g in goodgadgets:
        g.calcGadgetQuality()
    
    print("[+] Revising gadget types...")
    for g in goodgadgets:
        g.changeType()
    print("[+] Goodgadgets: %d" % len(goodgadgets))
      
    
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
#     print("%i gadgets after filtering for minimum length.\n" %len(goodgadgets))
    
    #for g in goodgadgets:
        #print("@" + str(g.opcodes) + " - " + str(g.address) + " - " + str(g.instructions))
   
        
    goodloads = goodLoads(goodgadgets)
    print("[+] goodloads: %d" % len(goodloads))
    bestloads = bestLoads(goodgadgets)
    print("[+] bestloads: %d" % len(bestloads))
    
    minglen = 0
    
    # find most suitable gadget(s) to initialize each register
    rdi, rsi, rcx, rdx, r8, r9 = find_gadget_candidates(goodgadgets, minglen)
    
    print("[+] Using the following gadgets:")
    try:
        print("   rdi: " + str(rdi.instructions) + "@" + str(rdi.address))
    except:
        print("   No gadget found for rdi.")
    
    try:    
        print("   rsi: " + str(rsi.instructions) + "@" + str(rsi.address))
    except:
        print("   No gadget found for rsi.")
        
    try:
        print("   rcx: " + str(rcx.instructions) + "@" + str(rcx.address))
    except:
        print("   No gadget found for rcx.")
        
    try:
        print("   rdx: " + str(rdx.instructions) + "@" + str(rdx.address))
    except:
        print("   No gadget found for rdx.")
        
    try: 
        print("   r8 : " + str(r8.instructions) + "@" + str(r8.address))
    except:
        print("   No gadget found for r8.")
    
    try:
        print("   r9 : " + str(r9.instructions) + "@" + str(r9.address))
    except:
        print("   No gadget found for r9.")
    
   
    if in_bin_path.endswith(".dll") or in_bin_path.endswith(".exe"):
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
        print("[-] Input file is not ELF or PE!")
        return
        

    if perm_gadgets == 0:
        print("[-] No gadget permutation. Exiting...")
        return
    else:
        print("[+] Argument #: %d" % argnum)
        i = 0
        for p in perm_gadgets:
            log.debug("  perm_gadget %d/%d: %s" % (i, 0, p))
            i += 1

    if args.architecture == "x86" :
        md = Cs(CS_ARCH_X86, CS_MODE_32)
        archlen = 4
    elif args.architecture == "x86-64" : 
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        archlen = 8
    else :
        print("Error: Bitlength needs to be 32 or 64!")
        return
            
    # evaluate permutations, stop after the first one is found
    # loop through them, check if all registers required are rsp-relative
    gadget = None
    firstchain = None
    for index, gadgets in enumerate(perm_gadgets):
        print("[+] Trying permutation ", index)
        conc = concatenate_gadgets(gadgets)
        gadget_readable = conc
        gadget = conc
        firstchain = gadgets
        log.debug("  gadget: %s" % gadget)
        
        if gadget != 0:
            post_simple, pre_simple, pre, post = passZero(gadget, arch)
            gadget = Gadget(0, gadget_readable, pre_simple, pre, post_simple, post, "grade", "notype", 0, 0, "", "", "")
            
            if checkPostconditions(gadget, argnum, ftype) == -1:
                print("  fail")
            else:
                print("  success")
                break
    
    if gadget is None:
        print("[-] did not find good permutation.")
        return
 
    firstgadget = gadget
    for g in firstchain:
        ins = ""
        for i in g.instructions:
            ins += i + " ; "
        print("[+] 0x%x:\t%s" %(g.address, ins))
        
    # summarize pre and postconditions
    #print(firstgadget.opcodes)
    print("---------------------")
    print("[+] Dereferenced registers:")
    print("  %s" % summarizePreconds(firstgadget.preconditions))
    print("[+] Postconditions:")
    print("  %s" % interestingPostconds(firstgadget.postconditions))
    print("---------------------")
   

    satchain = []
    for p in summarizePreconds(firstgadget.preconditions):
        if p != "rsp":
            satadd = initSatPrecond(p, bestloads, goodloads)
            if satadd == 0:
                print("Exiting...")
                return
            else:
                satchain += satadd
    
    satchain += firstchain
    
    
    return
    
    print("THE FINAL CHAIN:")
    for g in satchain:
        ins = ""
        for i in g.instructions:
            ins += i + " ; "
        print("0x%x:\t%s" %(g.address, ins))
        padding = rspPadding(g)
        if padding != "":
            print(padding)
    
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
            print("unknow file: ", filename)
            sys.exit(-1)
        try:
            s = getHexStreamsFromElfExecutableSections(filename)
            for section in s:
                print("ELF", filename, section['name'], section['addr'], section['hexStream'])
        except:
            try:
                s = getHexStreamFromPE(filename)
                for section in s:
                    print("PE", filename, section['name'], section['addr'], section['hexStream'])
            except:
                print("not a binary: ", filename)
        exit(0)
    
    if not args.show_post_memory is None:
        spm = 1
    else:
        spm = 0
    
    
    if not args.code_size is None:
        print("code size: ")
        dirn = args.code_size
        total_length = 0
        for fn in os.listdir(dirn):
            filename = dirn + "/" +fn
            try:
                s = getHexStreamsFromElfExecutableSections(filename)
                print("ELF binary code sections : ", len(s))
                for section in s:
                    hs = section['hexStream']
                    total_length += len(hs)
            except:
                try:
                    s = getHexStreamFromPE(filename)
                    print("PE binary: ", len(s) )
                    for section in s:
                        hs = section['hexStream']
                        total_length += len(hs)
                except:
                    print("not a binary: ", filename)
        print("total length of all code sections: ", total_length / 2 / 1024)
        sys.exit(0)
    

    if args.binary == None:
        parser.error("no binary specified!")
        print("no binary specified!")

        
    if int(args.arguments) < 2:
        parser.error("number of arguments for the autochainer must be at least 2!")
        print("number of arguments for the autochainer must be at least 2!")

    
    if not args.processes is None:
        Options.NBR_PROCESSES = int(args.processes)
        print("Number of processes: ", Options.NBR_PROCESSES)
    
    print("[+] Starting inspector gadget...")
    
    out_dir = os.path.abspath(args.output_directory)
    in_bin_path = os.path.abspath(args.binary)
    print("[+] Target binary   : '%s'" % in_bin_path)
    print("[+] Output directory: '%s'" % out_dir)
    # ROPunzel / Inspector Gadget / PSHAPE
    ROPunzel(args.architecture, in_bin_path, int(args.minimum_length), int(args.maximum_length), int(args.arguments), spm, out_dir)
    

def doAnalysis(gadget, architecture):
    print("in doAnalysis")
    postcond = passZero(convertXCS(gadget), architecture) 
    print("postcond: %s" % str(postcond))
    #ROPunzel(architecture, None, 10, 12, 2, None, None, test_hexdata=gadget)
