import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetX64(unittest.TestCase):

  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x86-64")

  def test_gadget001(self):
    #push rax
    #mov rax, 5
    #pop rax
    #push rbx
    #mov rbx, 6
    #pop rbx
    print "gadget 1"
    gadget = "5048C7C005000000585348C7C3060000005B"
    self.do(gadget)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()
    

     
     
     

     
     
