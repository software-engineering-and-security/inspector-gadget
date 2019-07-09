#from SymRepresentation import SymRepresentation as sr
import InspectorGadget as ig
#
#import capstone as cs
import random

class Gadget:

    def __init__(self, adr, op, preconds, preconds_org, postconds, postconds_org, grade, gatype, cp, length, ins, greatload, goodload):
        self.address = adr
        self.opcodes = op

        self.preconditions = preconds
        self.preconditions_original = preconds_org
        self.postconditions = postconds
        self.postconditions_original = postconds_org

        self.grade = grade
        self.gadgetype = gatype
        self.callprec = cp
        self.length = length
        self.instructions = ins
        self.greatload = greatload
        self.goodload = goodload
    
    def PP(self):
        # pretty print using capstone TODO
        return "null"
    
    def setAddress(self, address):
        self.address = address
    
    def setOpcodes(self, opcodes):
        self.opcodes = opcodes

    def setUsability(self, grade):
        self.grade = grade
        
    def setGadgetType(self, gatype):
        self.gadgetype = gatype
        
    def setCallPreceded(self, cp):
        self.callprec = cp
    
    def setLength(self, length):
        self.length = length
    
    def setIns(self, ins):
        self.instructions = ins
        
    def setGreatLoad(self, gl):
        self.greatload = gl
        
    def setGoodLoad(self, gl):
        self.goodload = gl

    def calcGadgetQuality(self):
        res_reg_derefs = self.calcQualityRegisterDerefences()
        res_bad_ins = self.calcQualityBadIns()
        grade = len(self.preconditions) \
                + len(self.postconditions) \
                + self.length / 2 \
                + len(self.opcodes) / 2 \
                + res_reg_derefs \
                + res_bad_ins
        self.grade = grade
    
    def calcQualityBadIns(self):
        postconds = self.postconditions
        res = 0
        
        for i in self.instructions:
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
    def calcQualityRegisterDerefences(self):
        preconds = self.preconditions
        res = ig.getRangePreconditions(preconds, "x86-64")
        
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
                    #print("OMG THE BADNESS IS SO BAD111")
                    #print(gadget.instructions)
                    return 6
                elif lb_int + 10000 < ub_int:
                    #print("OMG THE BADNESS IS BAD1" )
                    #print(gadget.instructions)
                    return 4
                elif lb_int + 1000 < ub_int:
                    #print("OMG THE BADNESS"  )
                    #print(gadget.instructions        )
                    return 2
        return 0
    
    def changeType(self):
    
        gtype = []
        self.gadgetype = []
        
        for p in self.postconditions:
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
                        
        self.gadgetype = gtype



    
    
