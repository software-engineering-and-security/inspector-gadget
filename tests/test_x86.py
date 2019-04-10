import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetX86(unittest.TestCase):

  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x86")

  def test_gadget001(self):
      # mov eax, 4000; push eax ; pop eax; add eax, 40
      gadget = "b800400000505883c040"
      self.do(gadget)

#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())
#        self.assertEqual(s.split(), ['hello', 'world'])

  def test_gadget002(self):
     # mov eax, 4000 ; push eax; pop esi; add esi, 10; dec esi; mov [ebp+4],esi; ret
    gadget = "b800400000505e83c6104e897504c3"
    self.do(gadget)

  def test_gadget003(self):
     #pushad # popad
    gadget = "6061"
    self.do(gadget)     
     
  def test_gadget004(self):
    gadget = "8bc4c7042437130000c700341200008b0c24"
    self.do(gadget)
     
  def test_gadget005(self):
     # fake x86 attack
     #pop eax # pop esi # pop ecx # dec eax # pop ebp # pop ebx # mov esp, ebp # pop ebp # pop edx # and al,39
    gadget = "585e59485d5b8be55d5a2439"
    self.do(gadget)
     
  def test_gadget006(self):
     # ???
    gadget = "11d8"
    self.do(gadget)
     
  def test_gadget007(self):
     # add eax, 5 # add eax, 5 # add eax, 5
    gadget = "83c00583c00583c005"
    self.do(gadget)
     
  def test_gadget008(self):
     # mov eax, 20 # add eax, 5 # sub eax, 15 # add eax, ebx # add eax, 3
    gadget = "b82000000083c00583e81503c383c003"
    self.do(gadget)
     
  def test_gadget009(self):
     #sub eax, 5 # add eax, 20 # add eax, 10 # sub eax, 12 # add eax, 30
     #sub eax, 1 # add eax, 100 # add eax, 200 # add eax, 300 # sub eax, 50
    gadget = "83e80583c02083c01083e81283c03083e80105000100000500020000050003000083e850"
    self.do(gadget)
     
  def test_gadget010(self):
     # ror eax, 2
    gadget = "c1c802"
    self.do(gadget)
     
  def test_gadget011(self):
     # push eax # mov eax, 5 # pop eax # push ebx # mov ebx, 6 # pop ebx
    gadget = "50b8050000005853bb060000005b"
    self.do(gadget)
     
  def test_gadget012(self):
     # pop eax # mov eax, 5 # push eax # pop ebx # mov ebx, 6 # push ebx
    gadget = "58b805000000505bbb0600000053"
    self.do(gadget)
     
  def test_gadget013(self):
    print "gadget13"
     # imul ebx i.e. eax = eax*ebx
    gadget = "f7eb"
    self.do(gadget)
     
  def test_gadget014(self):
     # imul ebx, ecx i.e. ebx = ebx*ecx
    gadget = "0fafd9"
    self.do(gadget)
     
  def test_gadget015(self):
     # imul ebx,ecx,20 i.e. ebx = ecx*20
    gadget = "6bd920"
    self.do(gadget)
     
  def test_gadget016(self):
     # mov eax, 10 # mov ebx, 5 # imul eax, ebx
    gadget = "b810000000bb050000000fafc3"
    self.do(gadget)
     
  def test_gadget017(self):
     # mov eax, 20 # add eax, 50 # sub eax, 10 # mov ebx, 5 # mul ebx # add ebx, 1 # sub eax, ebx
    gadget = "b82000000083c05083e810f7e383c3012bc3"
    self.do(gadget)
     
  def test_gadget018(self):
    # mov eax, 20 # add eax, 50 # sub eax, 10 # mov ebx, 5 # add eax, ebx # add ebx, 1 # sub eax, ebx
    gadget = "b82000000083c05083e810bb0500000003c383c3012bc3"
    self.do(gadget)
     
  def test_gadget019(self):
     # use dis
     # add eax, 50 # sub eax, 10 # add eax, ebx # add ebx, 1 # sub eax, ebx
    gadget = "83c05083e81003c383c3012bc3"
    self.do(gadget)
     
  def test_gadget020(self): 
     # mov eax, 20 # push eax # mov eax, 666 # push ebx # mov eax, [esp+4]
    gadget = "b82000000050b866060000538b442404"
    self.do(gadget)
        
  def test_gadget021(self):
     # mov eax, [ebx]
    gadget = "8b03"
    self.do(gadget)
     
  def test_gadget022(self):
     # mov [esp], eax
    gadget = "890424"
    self.do(gadget)
     
  def test_gadget023(self):
     # mov [esp+eax*2], ebx
    gadget = "891c44"
    self.do(gadget)
     
  def test_gadget024(self):
     # add eax, 1 # add ax, 1 # add ah, 1 # add al, 1
    gadget = "83c0016683c00180c4010401"
    self.do(gadget)
     
  def test_gadget025(self):
     # mov eax, 12345678 # mov ax, 1 # mov ah, 2 # mov al, 3
    gadget = "b87856341266b80100b402b003b801000000"
    self.do(gadget)
     
  def test_gadget026(self):
     # mov eax, [ebp-8] # pop ecx # lea esp, [ebp-14] # pop edi # pop esi # pop ebx # mov ecx, [ebp-4] # xor ecx, ebp
    gadget = "8b45f8598d65ec5f5e5b8b4dfc33cd"
    self.do(gadget)

  def test_gadget027(self):     
     # geez
    gadget = "8b448ee489448fe48b448ee889448fe88b448eec89448fec8b448ef089448ff003f003f8"
    self.do(gadget)
     
  def test_gadget028(self):
    print "gadget 28"
     # geez2
    gadget = "8b3f897e08893e895e18895e04814e0c0211000033c05f405b"
    self.do(gadget)

  def test_gadget029(self):
    print "gadget 29"
    #push ebp
    #mov ebp, esp
    #push esi
    #mov esi,[ebp+8]
    #push edi
    #mov edi, [ebp+c]
    #push 16
    #pop esi
    #mov [eax], esi
    #mov eax, esi
    #pop edi
    #pop esi
    #pop ebp
    gadget = "558bec568b7508578b7d0c6a165e89308bc65f5e5d"
    self.do(gadget)

  def test_gadget030(self):  
    print "gadget 30"   
    #push ebp
    #mov ebp, esp
    #mov eax, [ebp+8]
    #xor ecx, ecx
    #inc ecx
    #lea ecx,[each-13]
    #push 0d
    #pop eax
    #pop ebp
    gadget = "558bec8b450833c9418d48ed6a0d585d"
    self.do(gadget)
    
    def test_gadget031(self):
    # mov eax, esp
    # mov [esp], 1337
    # mov [eax], 1234
    # mov ebx, [esp]
        print "gadget 31"
        gadget = "8bc4c7042437130000c700341200008b1c24"
        self.do(gadget)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()
    

     
     
     

     
     
