import unittest
import logging
from inspectorgadget import InspectorGadget
import logging
import logging.config
import json


class TestGadgetX64(unittest.TestCase):

  def do(self, gadget):
        InspectorGadget.doAnalysis(gadget, "x86-64")

  def test_gadget_sub_180A43430(self):
		#sub_180A43430
		gadget = "488954241048894C2408488B442408448B4848448B40448B4840488B5424108B404C8902894A044489420844894A0CC3"
		self.do(gadget)

		#mov     [rsp+arg_8], rdx
		#mov     [rsp+arg_0], rcx
		#mov     rax, [rsp+arg_0]
		#mov     r9d, [rax+48h]
		#mov     r8d, [rax+44h]
		#mov     ecx, [rax+40h]
		#mov     rdx, [rsp+arg_8]
		#mov     eax, [rax+4Ch]
		#mov     [rdx], eax
		#mov     [rdx+4], ecx
		#mov     [rdx+8], r8d
		#mov     [rdx+0Ch], r9d
		#retn
			


  def test_gadget_sub_180DEED20(self):
		#sub_180DEED20
		gadget = "488B512831C0483B51204889D0C3"
		self.do(gadget)

		#mov     rdx, [rcx+28h]
		#xor     eax, eax
		#cmp     rdx, [rcx+20h]
		#cmovnz  rax, rdx
		#retn
		


  def test_gadget_sub_18009EEF0(self):
		#sub_18009EEF0
		gadget = "488BC44C8948204C8940184889501048894808498BC98B01FFC08941088B4104FFC089410CC3"
		self.do(gadget)

		#mov     rax, rsp
		#mov     [rax+20h], r9
		#mov     [rax+18h], r8
		#mov     [rax+10h], rdx
		#mov     [rax+8], rcx
		#mov     rcx, r9
		#mov     eax, [rcx]
		#inc     eax
		#mov     [rcx+8], eax
		#mov     eax, [rcx+4]
		#inc     eax
		#mov     [rcx+0Ch], eax
		#retn




  def test_gadget_sub_1802AF0F0(self):
		#sub_1802AF0F0
		gadget = "4C8BDC488BC2498BC04D8943184989531049894B08488B8A900000000FB6915E04000083E207891033C0C3"
		self.do(gadget)

		#mov     r11, rsp
		#mov     rax, rdx
		#mov     rax, r8
		#mov     [r11+18h], r8
		#mov     [r11+10h], rdx
		#mov     [r11+8], rcx
		#mov     rcx, [rdx+90h]
		#movzx   edx, byte ptr [rcx+45Eh]
		#and     edx, 7
		#mov     [rax], edx
		#xor     eax, eax
		#retn
		
if __name__ == '__main__':
    path = "../log-config.json"
    with open(path, 'rt') as f:
        print "Loading log configuration from %s " % path
        config = json.load(f)
        logging.config.dictConfig(config)
    unittest.main()
    

