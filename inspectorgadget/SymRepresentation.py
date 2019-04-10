from z3 import *
import re
import logging

logger = logging.getLogger(__name__)

class SymRepresentation:
    
    def __init__(self, expr):
        self.expr = expr;
        
    def isOperation(self, array, expr):
        for e in array:
            if expr.startswith(e + "("):
                return e
        return None
        
    def parse(self, expr):
        
        expr = expr.strip()
        
        sub = ["Sub64", "Sub32", "Sub16", "Sub8"]
        add = ["Add64", "Add32", "Add16", "Add8"]
        mul = ["Mul32", "MullU32", "MullS32", "Mul64", "MullS64", "MullU64", "Mul16", "MullS16"]
        orOp = ["Or64", "Or32", "Or16", "Or8"]
        xorOp = ["Xor64", "Xor32", "Xor16", "Xor8"]
        andOp = ["And64", "And32", "And16", "And8"]
        shr = ["Shr32", "Shr64", "Shr8", "Shr16"]
        shl = ["Shl32", "Shl64", "Shl8", "Shl16"]
        from64to32 = ["64to32", "64HIto32", "8Uto32", "64to8", "16to8", "32to16", "F64toF32", "64to16", "32to8", "128to64", "32HIto16"]
        from32to64 = ["32Uto64", "16Sto32", "32Sto64", "8Sto64", "16Uto32", "16Uto64", "32HLto64", "16Sto64", "8Sto16"]
        load = ["LDle:I32", "LDle:I64", "LDle:I8", "LDle:I16"]
        store = ["STle"]
        calculateFlags = ["amd64g_calculate_rflags_c"]
        
        stack = []
        
        while len(expr) > 0:
            logger.debug("> expr : %s ", expr)
            logger.debug("> stack: %s ", stack)
            subType = self.isOperation(sub, expr)
            addType = self.isOperation(add, expr)
            mulType = self.isOperation(mul, expr)
            orType = self.isOperation(orOp, expr)
            xorType = self.isOperation(xorOp, expr)
            andType = self.isOperation(andOp, expr)
            shrType = self.isOperation(shr, expr)
            shlType = self.isOperation(shl, expr)
            loadType = self.isOperation(load, expr)
            storeType = self.isOperation(store, expr)
            from64to32Type = self.isOperation(from64to32, expr)
            from32to64Type = self.isOperation(from32to64, expr)
            calculateFlagsType = self.isOperation(calculateFlags, expr)
            if not addType is None:
                # push new add
                stack.append("add")
                expr = re.sub('^' + addType + "\(", "", expr)
            elif not mulType is None:
                # push new add
                stack.append("mul")
                expr = re.sub('^' + mulType + "\(", "", expr)
            elif not orType is None:
                # push new add
                stack.append("or")
                expr = re.sub('^' + orType + "\(", "", expr)
            elif not xorType is None:
                # push new add
                stack.append("xor")
                expr = re.sub('^' + xorType + "\(", "", expr)
            elif not andType is None:
                # push new add
                stack.append("and")
                expr = re.sub('^' + andType + "\(", "", expr)
            elif not shrType is None:
                # push new add
                stack.append("shr")
                expr = re.sub('^' + shrType + "\(", "", expr)
            elif not shlType is None:
                # push new add
                stack.append("shl")
                expr = re.sub('^' + shlType + "\(", "", expr)
            elif not from64to32Type is None:
                # push new add
                stack.append("from64to32")
                expr = re.sub('^' + from64to32Type + "\(", "", expr)
            elif not from32to64Type is None:
                # push new add
                stack.append("from32to64")
                expr = re.sub('^' + from32to64Type + "\(", "", expr)
            elif not calculateFlagsType is None:
                # push new add
                stack.append("calculateFlags")
                expr = re.sub('^' + calculateFlagsType + "\(", "", expr)
            elif not loadType is None:
                # push new add
                stack.append("load")
                expr = re.sub('^' + loadType + "\(", "", expr)
            elif not storeType is None:
                stack.append("store")
                expr = re.sub('^' + storeType + "\(", "", expr)
            elif not subType is None:
                # push new sub
                stack.append("sub")
                expr = re.sub('^' + subType + "\(", "", expr)
            elif expr.startswith("0x"):
                value = re.search('^0x[0-9abcdefABCDEF]*', expr).group(0)
                stack.append(BitVecVal(int(value, 16), 64)) #Int(int(value, 16)))
                expr = re.sub('^'+value, "", expr)
            elif expr.startswith("t"):
                value = re.search('^t[0-9]*', expr).group(0)
                stack.append(BitVec(value, 64)) #Symbol(value))
                expr = re.sub('^'+value, "", expr)
            elif expr.startswith(","):
                expr = re.sub('^,', "", expr)
            elif expr.startswith(")"):
                # pop and create expression
                values = []
                v = stack.pop()
                while type(v) != type("aaa"):
                    values.append(simplify(v))
                    v = stack.pop()
                m = v
                if (m == "add"):
                    newE = values[1] + values[0]
                    stack.append(newE)
                elif (m == "sub"):
                    newE = values[1] - values[0]
                    stack.append(newE)
                elif m == "mul":
                    newE = values[1] * values[0]
                    stack.append(newE)
                elif m == "or":
                    #newE = Or(values[1], values[0])
                    newE = values[1] | values[0]
                    stack.append(newE)
                elif m == "xor":
                    #newE = Xor(values[1], values[0])
                    newE = values[1] ^ values[0]
                    stack.append(newE)
                elif m == "and":
                    #newE = And(values[1], values[0])
                    newE = values[1] & values[0]
                    stack.append(newE)
                elif m == "shr":
                    ### TODO: logical or arithmetic shift?
                    #newE = ShiftR(values[1], values[0])
                    newE = values[1] >> values[0]
                    stack.append(newE)
                elif m == "shl":
                    ### TODO: logical or arithmetic shift?
                    #newE = ShiftL(values[1], values[0])
                    newE = values[1] << values[0]
                    stack.append(newE)
                elif m == "from64to32":
                    newE = values[0]
                    stack.append(newE)
                elif m == "from32to64":
                    newE = values[0]
                    stack.append(newE)
                elif m == "load":
                    logger.debug("load: %s", values)
                    newE = BitVec("load(" + str(values[0]) + ")", 64) #Symbol("load(" + str(values[0]) + ")")
                    stack.append(newE)
                elif m == "store":
                    logger.debug("store: %s", values)
                    newE = BitVec("store(" + str(values[0]) + ")", 64) #Symbol("load(" + str(values[0]) + ")")
                    stack.append(newE)
                elif m == "calculateFlags":
                    logger.debug("calculate flags: %s", values)
                    newE = BitVec("calculateFlags(" + str(values[0]) + ")", 64) #Symbol("load(" + str(values[0]) + ")")
                    stack.append(newE)
                else:
                    exceptionMsg = "unknown operation: %s" % m
                    logger.exception(exceptionMsg)
                    raise Exception(exceptionMsg)
                    
                # push new expression
                expr = re.sub('^\)', "", expr)
            elif expr.startswith("GET"):
                v = expr.split(")")[0].split("(")[1].strip()
                logger.debug("get: %s", v)
                s = BitVec("get(" + str(v) + ")", 64) #Symbol("get(" + str(v) + ")")
                stack.append(s)
                expr = re.sub('^[^\)]*\)', "", expr)
            elif expr.startswith("PUT"):
                v = expr.split(")")[0].split("(")[1].strip()
                logger.debug("put: %s", v)
                s = BitVec("put(" + str(v) + ")", 64) #Symbol("get(" + str(v) + ")")
                stack.append(s)
                expr = re.sub('^[^\)]*\)', "", expr)
            else:
                exceptionMsg = "unknown string format: %s", expr
                logger.exception(exceptionMsg)
                raise Exception(exceptionMsg)
            
                
        logger.debug("final stack: %s ", stack)
        assert len(stack) == 1
        return stack[0]

    def simplify(self):
        logger.debug("before parsing: %s ", self.expr)
        e = self.parse(self.expr)
        logger.debug("before simplification: %s ", e)
        simplifiedE = simplify(e);
        logger.debug("simplified: %s", simplifiedE)
        return simplifiedE
        

# run this program to test the simplification method
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    
    str = " Sub32(Add32(Sub32(Add32(0x00000020,0x00000050),0x00000010),0x00000005),Add32(0x00000005,0x00000001))"
    expected = 0x59
    
    print "testing with ", str
    
    # simplify Expression
    sr = SymRepresentation(str)
    value = sr.simplify()
    
    # verify
    assert value == expected