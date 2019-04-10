from capstone import *

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
        
    def setPreconds(self, preconds):
        self.preconditions = preconds
    
    def setPostconds(self, postconds):
        self.postconditions = postconds
    
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