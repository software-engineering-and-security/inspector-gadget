import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetX86(unittest.TestCase):

  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x86")
      

  def test_gadget_sub_6DBB17B0(self):
		#sub_6DBB17B0
		gadget = "B838F4A16EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA1F438
		#retn


  def test_gadget_sub_6DBB6370(self):
		#sub_6DBB6370
		gadget = "83EC088B41E88B49EC250000FFFF8B90340400008B824C480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6DBC2370(self):
		#sub_6DBC2370
		gadget = "B8C012A26EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA212C0
		#retn


  def test_gadget_sub_6DBC2380(self):
		#sub_6DBC2380
		gadget = "B80814A26EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA21408
		#retn


  def test_gadget_sub_6DBC3BC0(self):
		#sub_6DBC3BC0
		gadget = "B88C18A26EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA2188C
		#retn


  def test_gadget_sub_6DBC4670(self):
		#sub_6DBC4670
		gadget = "8B410C8B40308A8834010000324C240480E101308834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+134h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC4690(self):
		#sub_6DBC4690
		gadget = "8B410C8A4C24048B403002C932883401000080E102308834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+134h]
		#and     cl, 2
		#xor     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC46C0(self):
		#sub_6DBC46C0
		gadget = "8B410C8A4C24048B403002C902C902C932883401000080E108308834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+134h]
		#and     cl, 8
		#xor     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC46F0(self):
		#sub_6DBC46F0
		gadget = "8B410C8A4C24048B4030C0E10432883401000080E110308834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+134h]
		#and     cl, 10h
		#xor     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC4710(self):
		#sub_6DBC4710
		gadget = "8B410C8A4C24048B4030C0E10532883401000080E120308834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+134h]
		#and     cl, 20h
		#xor     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC4730(self):
		#sub_6DBC4730
		gadget = "8B410C8A4C24048B4030C0E10632883401000080E140308834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+134h]
		#and     cl, 40h
		#xor     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC4750(self):
		#sub_6DBC4750
		gadget = "8B410C8B40308A88340100008A54240480E17FC0E2070ACA888834010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+134h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+134h], cl
		#retn    4


  def test_gadget_sub_6DBC4780(self):
		#sub_6DBC4780
		gadget = "8B410C8B40308A8835010000324C240480E101308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+135h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC47A0(self):
		#sub_6DBC47A0
		gadget = "8B410C8A4C24048B403002C932883501000080E102308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+135h]
		#and     cl, 2
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC47C0(self):
		#sub_6DBC47C0
		gadget = "8B410C8A4C24048B403002C902C932883501000080E104308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+135h]
		#and     cl, 4
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC47E0(self):
		#sub_6DBC47E0
		gadget = "8B410C8A4C24048B403002C902C902C932883501000080E108308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+135h]
		#and     cl, 8
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC4810(self):
		#sub_6DBC4810
		gadget = "8B410C8A4C24048B4030C0E10432883501000080E110308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+135h]
		#and     cl, 10h
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC4830(self):
		#sub_6DBC4830
		gadget = "8B410C8A4C24048B4030C0E10532883501000080E120308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+135h]
		#and     cl, 20h
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC4850(self):
		#sub_6DBC4850
		gadget = "8B410C8A4C24048B4030C0E10632883501000080E140308835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+135h]
		#and     cl, 40h
		#xor     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC4870(self):
		#sub_6DBC4870
		gadget = "8B410C8B40308A88350100008A54240480E17FC0E2070ACA888835010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+135h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+135h], cl
		#retn    4


  def test_gadget_sub_6DBC48A0(self):
		#sub_6DBC48A0
		gadget = "8B410C8B40308A8836010000324C240480E101308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+136h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC48C0(self):
		#sub_6DBC48C0
		gadget = "8B410C8A4C24048B403002C932883601000080E102308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+136h]
		#and     cl, 2
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC48E0(self):
		#sub_6DBC48E0
		gadget = "8B410C8A4C24048B403002C902C932883601000080E104308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+136h]
		#and     cl, 4
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC4900(self):
		#sub_6DBC4900
		gadget = "8B410C8A4C24048B403002C902C902C932883601000080E108308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+136h]
		#and     cl, 8
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC4930(self):
		#sub_6DBC4930
		gadget = "8B410C8A4C24048B4030C0E10432883601000080E110308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+136h]
		#and     cl, 10h
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC4950(self):
		#sub_6DBC4950
		gadget = "8B410C8A4C24048B4030C0E10532883601000080E120308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+136h]
		#and     cl, 20h
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC4970(self):
		#sub_6DBC4970
		gadget = "8B410C8A4C24048B4030C0E10632883601000080E140308836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+136h]
		#and     cl, 40h
		#xor     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC4990(self):
		#sub_6DBC4990
		gadget = "8B410C8B40308A88360100008A54240480E17FC0E2070ACA888836010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+136h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+136h], cl
		#retn    4


  def test_gadget_sub_6DBC49D0(self):
		#sub_6DBC49D0
		gadget = "8B410C8A4C24048B403002C932883701000080E102308837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+137h]
		#and     cl, 2
		#xor     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC49F0(self):
		#sub_6DBC49F0
		gadget = "8B410CDD4424048B4830DD99C8000000C20800"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#fld     [esp+arg_0]
		#mov     ecx, [eax+30h]
		#fstp    qword ptr [ecx+0C8h]
		#retn    8


  def test_gadget_sub_6DBC4A10(self):
		#sub_6DBC4A10
		gadget = "8B410C8A4C24048B403002C902C932883701000080E104308837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+137h]
		#and     cl, 4
		#xor     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC4A30(self):
		#sub_6DBC4A30
		gadget = "8B410C8A4C24048B403002C902C902C932883701000080E108308837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+137h]
		#and     cl, 8
		#xor     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC4A60(self):
		#sub_6DBC4A60
		gadget = "8B410C8A4C24048B4030C0E10432883701000080E110308837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+137h]
		#and     cl, 10h
		#xor     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC4A80(self):
		#sub_6DBC4A80
		gadget = "8B410C8A4C24048B4030C0E10532883701000080E120308837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+137h]
		#and     cl, 20h
		#xor     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC4AA0(self):
		#sub_6DBC4AA0
		gadget = "8B410C8A4C24048B4030C0E10632883701000080E140308837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+137h]
		#and     cl, 40h
		#xor     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC4AC0(self):
		#sub_6DBC4AC0
		gadget = "8B410C8B40308A88370100008A54240480E17FC0E2070ACA888837010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+137h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+137h], cl
		#retn    4


  def test_gadget_sub_6DBC4AF0(self):
		#sub_6DBC4AF0
		gadget = "8B410C8B40308A8838010000324C240480E101308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+138h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4B30(self):
		#sub_6DBC4B30
		gadget = "8B410C8A4C24048B403002C932883801000080E102308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+138h]
		#and     cl, 2
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4B50(self):
		#sub_6DBC4B50
		gadget = "8B410C8B48308B5424048991E0000000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+0E0h], edx
		#retn    4


  def test_gadget_sub_6DBC4B70(self):
		#sub_6DBC4B70
		gadget = "8B410C8A4C24048B403002C902C932883801000080E104308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+138h]
		#and     cl, 4
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4B90(self):
		#sub_6DBC4B90
		gadget = "8B410C8A4C24048B403002C902C902C932883801000080E108308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+138h]
		#and     cl, 8
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4BC0(self):
		#sub_6DBC4BC0
		gadget = "8B410C8B48308B5424048991E4000000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+0E4h], edx
		#retn    4


  def test_gadget_sub_6DBC4BE0(self):
		#sub_6DBC4BE0
		gadget = "8B410C8A4C24048B4030C0E10432883801000080E110308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+138h]
		#and     cl, 10h
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4C00(self):
		#sub_6DBC4C00
		gadget = "8B410C8A4C24048B4030C0E10532883801000080E120308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+138h]
		#and     cl, 20h
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4C20(self):
		#sub_6DBC4C20
		gadget = "8B410C8A4C24048B4030C0E10632883801000080E140308838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+138h]
		#and     cl, 40h
		#xor     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4C40(self):
		#sub_6DBC4C40
		gadget = "8B410C8B40308A88380100008A54240480E17FC0E2070ACA888838010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+138h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+138h], cl
		#retn    4


  def test_gadget_sub_6DBC4C70(self):
		#sub_6DBC4C70
		gadget = "8B410C8B40308A8839010000324C240480E101308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+139h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4C90(self):
		#sub_6DBC4C90
		gadget = "8B410C8A4C24048B403002C932883901000080E102308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+139h]
		#and     cl, 2
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4CB0(self):
		#sub_6DBC4CB0
		gadget = "8B410C8A4C24048B403002C902C932883901000080E104308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+139h]
		#and     cl, 4
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4CD0(self):
		#sub_6DBC4CD0
		gadget = "8B410C8A4C24048B403002C902C902C932883901000080E108308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+139h]
		#and     cl, 8
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4D00(self):
		#sub_6DBC4D00
		gadget = "8B410C8A4C24048B4030C0E10432883901000080E110308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+139h]
		#and     cl, 10h
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4D20(self):
		#sub_6DBC4D20
		gadget = "8B410C8A4C24048B4030C0E10632884101000080E140308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+141h]
		#and     cl, 40h
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC4D40(self):
		#sub_6DBC4D40
		gadget = "8B410C8A4C24048B4030C0E10532883901000080E120308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+139h]
		#and     cl, 20h
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4D60(self):
		#sub_6DBC4D60
		gadget = "8B410CDD4424048B4830DD99F8000000C20800"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#fld     [esp+arg_0]
		#mov     ecx, [eax+30h]
		#fstp    qword ptr [ecx+0F8h]
		#retn    8


  def test_gadget_sub_6DBC4D80(self):
		#sub_6DBC4D80
		gadget = "8B410C8A4C24048B4030C0E10632883901000080E140308839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+139h]
		#and     cl, 40h
		#xor     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4DA0(self):
		#sub_6DBC4DA0
		gadget = "8B410C8B40308A88390100008A54240480E17FC0E2070ACA888839010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+139h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+139h], cl
		#retn    4


  def test_gadget_sub_6DBC4DD0(self):
		#sub_6DBC4DD0
		gadget = "8B410C8B40308A883A010000324C240480E10130883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Ah]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4DF0(self):
		#sub_6DBC4DF0
		gadget = "8B410C8A4C24048B403002C932883A01000080E10230883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+13Ah]
		#and     cl, 2
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4E10(self):
		#sub_6DBC4E10
		gadget = "8B410C8B48308B542404899100010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+100h], edx
		#retn    4


  def test_gadget_sub_6DBC4E30(self):
		#sub_6DBC4E30
		gadget = "8B410C8A4C24048B403002C902C932883A01000080E10430883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Ah]
		#and     cl, 4
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4E50(self):
		#sub_6DBC4E50
		gadget = "8B410C8A4C24048B403002C902C902C932883A01000080E10830883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Ah]
		#and     cl, 8
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4E80(self):
		#sub_6DBC4E80
		gadget = "8B410C8A4C24048B4030C0E10432883A01000080E11030883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+13Ah]
		#and     cl, 10h
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4EA0(self):
		#sub_6DBC4EA0
		gadget = "8B410C8A4C24048B4030C0E10532883A01000080E12030883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+13Ah]
		#and     cl, 20h
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4EC0(self):
		#sub_6DBC4EC0
		gadget = "8B410C8A4C24048B4030C0E10632883A01000080E14030883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+13Ah]
		#and     cl, 40h
		#xor     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4EE0(self):
		#sub_6DBC4EE0
		gadget = "8B410C8B48308B542404899108010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+108h], edx
		#retn    4


  def test_gadget_sub_6DBC4F00(self):
		#sub_6DBC4F00
		gadget = "8B410C8B48308B54240489910C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+10Ch], edx
		#retn    4


  def test_gadget_sub_6DBC4F20(self):
		#sub_6DBC4F20
		gadget = "8B410C8B48308B542404899110010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+110h], edx
		#retn    4


  def test_gadget_sub_6DBC4F40(self):
		#sub_6DBC4F40
		gadget = "8B410C8B40308A883A0100008A54240480E17FC0E2070ACA88883A010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Ah]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+13Ah], cl
		#retn    4


  def test_gadget_sub_6DBC4F70(self):
		#sub_6DBC4F70
		gadget = "8B410C8B40308A883B010000324C240480E10130883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Bh]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC4F90(self):
		#sub_6DBC4F90
		gadget = "8B410C8A4C24048B403002C932883B01000080E10230883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+13Bh]
		#and     cl, 2
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC4FB0(self):
		#sub_6DBC4FB0
		gadget = "8B410C8A4C24048B403002C902C932883B01000080E10430883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Bh]
		#and     cl, 4
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC4FD0(self):
		#sub_6DBC4FD0
		gadget = "8B410C8B48308B542404899114010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+114h], edx
		#retn    4


  def test_gadget_sub_6DBC5010(self):
		#sub_6DBC5010
		gadget = "8B410C8A4C24048B403002C902C902C932883B01000080E10830883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Bh]
		#and     cl, 8
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC5040(self):
		#sub_6DBC5040
		gadget = "8B410C8A4C24048B4030C0E10432883B01000080E11030883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+13Bh]
		#and     cl, 10h
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC5060(self):
		#sub_6DBC5060
		gadget = "8B410C8A4C24048B4030C0E10532883B01000080E12030883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+13Bh]
		#and     cl, 20h
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC5080(self):
		#sub_6DBC5080
		gadget = "8B410C8A4C24048B4030C0E10632883B01000080E14030883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+13Bh]
		#and     cl, 40h
		#xor     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC50A0(self):
		#sub_6DBC50A0
		gadget = "8B410C8B40308A883B0100008A54240480E17FC0E2070ACA88883B010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Bh]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+13Bh], cl
		#retn    4


  def test_gadget_sub_6DBC50D0(self):
		#sub_6DBC50D0
		gadget = "8B410C8B40308A883C010000324C240480E10130883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Ch]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC50F0(self):
		#sub_6DBC50F0
		gadget = "8B410C8A4C24048B403002C932883C01000080E10230883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+13Ch]
		#and     cl, 2
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC5110(self):
		#sub_6DBC5110
		gadget = "8B410C8A4C24048B403002C902C932883C01000080E10430883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Ch]
		#and     cl, 4
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC5130(self):
		#sub_6DBC5130
		gadget = "8B410C8A4C24048B403002C902C902C932883C01000080E10830883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Ch]
		#and     cl, 8
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC5160(self):
		#sub_6DBC5160
		gadget = "8B410CDD4424048B4830DD9920010000C20800"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#fld     [esp+arg_0]
		#mov     ecx, [eax+30h]
		#fstp    qword ptr [ecx+120h]
		#retn    8


  def test_gadget_sub_6DBC5180(self):
		#sub_6DBC5180
		gadget = "8B410C8A4C24048B4030C0E10432883C01000080E11030883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+13Ch]
		#and     cl, 10h
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC51A0(self):
		#sub_6DBC51A0
		gadget = "8B410C8A4C24048B4030C0E10532883C01000080E12030883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+13Ch]
		#and     cl, 20h
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC51C0(self):
		#sub_6DBC51C0
		gadget = "8B410C8A4C24048B4030C0E10632883C01000080E14030883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+13Ch]
		#and     cl, 40h
		#xor     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC51E0(self):
		#sub_6DBC51E0
		gadget = "8B410C8B40308A883C0100008A54240480E17FC0E2070ACA88883C010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Ch]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+13Ch], cl
		#retn    4


  def test_gadget_sub_6DBC5210(self):
		#sub_6DBC5210
		gadget = "8B410C8B40308A883D010000324C240480E10130883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Dh]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC5230(self):
		#sub_6DBC5230
		gadget = "8B410C8A4C24048B403002C932883D01000080E10230883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+13Dh]
		#and     cl, 2
		#xor     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC5250(self):
		#sub_6DBC5250
		gadget = "8B410C8A4C24048B403002C902C932883D01000080E10430883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Dh]
		#and     cl, 4
		#xor     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC5280(self):
		#sub_6DBC5280
		gadget = "8B410C8A4C24048B4030C0E10432883D01000080E11030883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+13Dh]
		#and     cl, 10h
		#xor     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC52A0(self):
		#sub_6DBC52A0
		gadget = "8B410C8A4C24048B4030C0E10532883D01000080E12030883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+13Dh]
		#and     cl, 20h
		#xor     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC52C0(self):
		#sub_6DBC52C0
		gadget = "8B410C8A4C24048B4030C0E10632883D01000080E14030883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+13Dh]
		#and     cl, 40h
		#xor     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC52E0(self):
		#sub_6DBC52E0
		gadget = "8B410C8B40308A883D0100008A54240480E17FC0E2070ACA88883D010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Dh]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+13Dh], cl
		#retn    4


  def test_gadget_sub_6DBC5310(self):
		#sub_6DBC5310
		gadget = "8B410C8B48308B542404899128010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+128h], edx
		#retn    4


  def test_gadget_sub_6DBC5330(self):
		#sub_6DBC5330
		gadget = "8B410C8B40308A883E010000324C240480E10130883E010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Eh]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+13Eh], cl
		#retn    4


  def test_gadget_sub_6DBC5350(self):
		#sub_6DBC5350
		gadget = "8B410C8A4C24048B403002C932883E01000080E10230883E010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+13Eh]
		#and     cl, 2
		#xor     [eax+13Eh], cl
		#retn    4


  def test_gadget_sub_6DBC5370(self):
		#sub_6DBC5370
		gadget = "8B410C8A4C24048B403002C902C932883E01000080E10430883E010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Eh]
		#and     cl, 4
		#xor     [eax+13Eh], cl
		#retn    4


  def test_gadget_sub_6DBC53B0(self):
		#sub_6DBC53B0
		gadget = "8B410C8A4C24048B4030C0E10532883E01000080E12030883E010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+13Eh]
		#and     cl, 20h
		#xor     [eax+13Eh], cl
		#retn    4


  def test_gadget_sub_6DBC53D0(self):
		#sub_6DBC53D0
		gadget = "8B410C8A4C24048B4030C0E10632883E01000080E14030883E010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+13Eh]
		#and     cl, 40h
		#xor     [eax+13Eh], cl
		#retn    4


  def test_gadget_sub_6DBC53F0(self):
		#sub_6DBC53F0
		gadget = "8B410C8B40308A883E0100008A54240480E17FC0E2070ACA88883E010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Eh]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+13Eh], cl
		#retn    4


  def test_gadget_sub_6DBC5420(self):
		#sub_6DBC5420
		gadget = "8B410C8B40308A883F010000324C240480E10130883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Fh]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC5440(self):
		#sub_6DBC5440
		gadget = "8B410C8A4C24048B403002C932883F01000080E10230883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+13Fh]
		#and     cl, 2
		#xor     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC5460(self):
		#sub_6DBC5460
		gadget = "8B410C8A4C24048B403002C902C932883F01000080E10430883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Fh]
		#and     cl, 4
		#xor     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC5480(self):
		#sub_6DBC5480
		gadget = "8B410C8A4C24048B403002C902C902C932883F01000080E10830883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+13Fh]
		#and     cl, 8
		#xor     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC54B0(self):
		#sub_6DBC54B0
		gadget = "8B410C8A4C24048B4030C0E10432883F01000080E11030883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+13Fh]
		#and     cl, 10h
		#xor     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC54D0(self):
		#sub_6DBC54D0
		gadget = "8B410C8A4C24048B4030C0E10532883F01000080E12030883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+13Fh]
		#and     cl, 20h
		#xor     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC5500(self):
		#sub_6DBC5500
		gadget = "8B410C8B40308A883F0100008A54240480E17FC0E2070ACA88883F010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+13Fh]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+13Fh], cl
		#retn    4


  def test_gadget_sub_6DBC5530(self):
		#sub_6DBC5530
		gadget = "8B410C8B40308A8840010000324C240480E101308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+140h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC5550(self):
		#sub_6DBC5550
		gadget = "8B410C8A4C24048B403002C932884001000080E102308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+140h]
		#and     cl, 2
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC5570(self):
		#sub_6DBC5570
		gadget = "8B410C8A4C24048B403002C902C932884001000080E104308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+140h]
		#and     cl, 4
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC5590(self):
		#sub_6DBC5590
		gadget = "8B410C8A4C24048B403002C902C902C932884001000080E108308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+140h]
		#and     cl, 8
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC55C0(self):
		#sub_6DBC55C0
		gadget = "8B410C8A4C24048B4030C0E10432884001000080E110308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+140h]
		#and     cl, 10h
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC55E0(self):
		#sub_6DBC55E0
		gadget = "8B410C8A4C24048B4030C0E10532884001000080E120308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+140h]
		#and     cl, 20h
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC5600(self):
		#sub_6DBC5600
		gadget = "8B410C8A4C24048B4030C0E10632884001000080E140308840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 6
		#xor     cl, [eax+140h]
		#and     cl, 40h
		#xor     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC5620(self):
		#sub_6DBC5620
		gadget = "8B410C8B48308B542404899130010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+30h]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+130h], edx
		#retn    4


  def test_gadget_sub_6DBC5640(self):
		#sub_6DBC5640
		gadget = "8B410C8B40308A88400100008A54240480E17FC0E2070ACA888840010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+140h]
		#mov     dl, [esp+arg_0]
		#and     cl, 7Fh
		#shl     dl, 7
		#or      cl, dl
		#mov     [eax+140h], cl
		#retn    4


  def test_gadget_sub_6DBC5670(self):
		#sub_6DBC5670
		gadget = "8B410C8B40308A8841010000324C240480E101308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+30h]
		#mov     cl, [eax+141h]
		#xor     cl, [esp+arg_0]
		#and     cl, 1
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC5690(self):
		#sub_6DBC5690
		gadget = "8B410C8A4C24048B403002C932884101000080E102308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#xor     cl, [eax+141h]
		#and     cl, 2
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC56B0(self):
		#sub_6DBC56B0
		gadget = "8B410C8A4C24048B403002C902C932884101000080E104308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+141h]
		#and     cl, 4
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC56D0(self):
		#sub_6DBC56D0
		gadget = "8B410C8A4C24048B403002C902C902C932884101000080E108308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, [eax+141h]
		#and     cl, 8
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC5700(self):
		#sub_6DBC5700
		gadget = "8B410C8A4C24048B4030C0E10432884101000080E110308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 4
		#xor     cl, [eax+141h]
		#and     cl, 10h
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC5720(self):
		#sub_6DBC5720
		gadget = "8B410C8A4C24048B4030C0E10532884101000080E120308841010000C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     cl, [esp+arg_0]
		#mov     eax, [eax+30h]
		#shl     cl, 5
		#xor     cl, [eax+141h]
		#and     cl, 20h
		#xor     [eax+141h], cl
		#retn    4


  def test_gadget_sub_6DBC6450(self):
		#sub_6DBC6450
		gadget = "8B44240C8B54240489018B442408C741040000000089510889410CC7412C02000000C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [esp+arg_0]
		#mov     [ecx], eax
		#mov     eax, [esp+arg_4]
		#mov     dword ptr [ecx+4], 0
		#mov     [ecx+8], edx
		#mov     [ecx+0Ch], eax
		#mov     dword ptr [ecx+2Ch], 2
		#retn    0Ch


  def test_gadget_sub_6DBC6640(self):
		#sub_6DBC6640
		gadget = "8BC133C9894808BAFAFFFFFF89500C89501C894818895024894820C74028FFFFFFFF89482CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     edx, 0FFFFFFFAh
		#mov     [eax+0Ch], edx
		#mov     [eax+1Ch], edx
		#mov     [eax+18h], ecx
		#mov     [eax+24h], edx
		#mov     [eax+20h], ecx
		#mov     dword ptr [eax+28h], 0FFFFFFFFh
		#mov     [eax+2Ch], ecx
		#retn


  def test_gadget_sub_6DBC7230(self):
		#sub_6DBC7230
		gadget = "83EC088B41E88B49EC250000FFFF8B90340400008B824C480000894C240433C983B824580000FA0F95C083C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     [esp+8+var_4], ecx
		#xor     ecx, ecx
		#cmp     dword ptr [eax+5824h], 0FFFFFFFAh
		#setnz   al
		#add     esp, 8
		#retn


  def test_gadget_sub_6DBC7260(self):
		#sub_6DBC7260
		gadget = "83EC088B41E88B49EC250000FFFF8B90340400008B824C4800008B8074490000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+4974h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6DBC7530(self):
		#sub_6DBC7530
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B807C490000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+497Ch]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6DBCA2A0(self):
		#sub_6DBCA2A0
		gadget = "8B442408C700A09EBC6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DBC9EA0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DBCBB00(self):
		#sub_6DBCBB00
		gadget = "8B44240C8B500C0FB7523A8B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#movzx   edx, word ptr [edx+3Ah]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DBCC9C0(self):
		#sub_6DBCC9C0
		gadget = "8B442408C700F0C5BC6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DBCC5F0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DBCCD20(self):
		#sub_6DBCCD20
		gadget = "8B5424088BC18B4C240489480889500C33C9BAFAFFFFFF89501C894818895024894820C74028FFFFFFFF89482CC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#xor     ecx, ecx
		#mov     edx, 0FFFFFFFAh
		#mov     [eax+1Ch], edx
		#mov     [eax+18h], ecx
		#mov     [eax+24h], edx
		#mov     [eax+20h], ecx
		#mov     dword ptr [eax+28h], 0FFFFFFFFh
		#mov     [eax+2Ch], ecx
		#retn    8


  def test_gadget_sub_6DBD0BC0(self):
		#sub_6DBD0BC0
		gadget = "8B442408C700100BBD6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DBD0B10
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DBD45E0(self):
		#sub_6DBD45E0
		gadget = "8B442404C74004FFFFFFFFC7000D000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0Dh
		#retn


  def test_gadget_sub_6DBD4600(self):
		#sub_6DBD4600
		gadget = "8B442404C74004FFFFFFFFC70010000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 10h
		#retn


  def test_gadget_sub_6DBD4620(self):
		#sub_6DBD4620
		gadget = "8B442404C74004FFFFFFFFC70016000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 16h
		#retn


  def test_gadget_sub_6DBD4640(self):
		#sub_6DBD4640
		gadget = "8B442404C74004FFFFFFFFC70017000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 17h
		#retn


  def test_gadget_sub_6DBD4660(self):
		#sub_6DBD4660
		gadget = "8B442404C74004FFFFFFFFC70018000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 18h
		#retn


  def test_gadget_sub_6DBD4680(self):
		#sub_6DBD4680
		gadget = "8B442404C74004FFFFFFFFC7001A000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 1Ah
		#retn


  def test_gadget_sub_6DBD46A0(self):
		#sub_6DBD46A0
		gadget = "8B442404C74004FFFFFFFFC7001B000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 1Bh
		#retn


  def test_gadget_sub_6DBD46C0(self):
		#sub_6DBD46C0
		gadget = "8B442404C74004FFFFFFFFC7001C000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 1Ch
		#retn


  def test_gadget_sub_6DBD46E0(self):
		#sub_6DBD46E0
		gadget = "8B442404C74004FFFFFFFFC7001D000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 1Dh
		#retn


  def test_gadget_sub_6DBD63C0(self):
		#sub_6DBD63C0
		gadget = "8B4424108B5424048941048B4424088951088B54240CC7010200000089410C895110C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_C]
		#mov     edx, [esp+arg_0]
		#mov     [ecx+4], eax
		#mov     eax, [esp+arg_4]
		#mov     [ecx+8], edx
		#mov     edx, [esp+arg_8]
		#mov     dword ptr [ecx], 2
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], edx
		#retn    10h


  def test_gadget_sub_6DBDB1C0(self):
		#sub_6DBDB1C0
		gadget = "8B54240C8BC18B4C24048908C74004000000008B492089480889500CC20C00"
		self.do(gadget)

		#mov     edx, [esp+arg_8]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#retn    0Ch


  def test_gadget_j_j_nullsub_1(self):
		#j_j_nullsub_1
		gadget = "E9ABB70100"
		self.do(gadget)

		#jmp     j_nullsub_1


  def test_gadget_sub_6DBE2600(self):
		#sub_6DBE2600
		gadget = "8B442404C74004FFFFFFFFC70009000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 9
		#retn


  def test_gadget_sub_6DBE64B0(self):
		#sub_6DBE64B0
		gadget = "8B442408C7006061BE6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DBE6160
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DBE7B70(self):
		#sub_6DBE7B70
		gadget = "8B442404C74004FFFFFFFFC7000A000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0Ah
		#retn


  def test_gadget_sub_6DBE7B90(self):
		#sub_6DBE7B90
		gadget = "8B442404C74004FFFFFFFFC7000B000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0Bh
		#retn


  def test_gadget_sub_6DBE99D0(self):
		#sub_6DBE99D0
		gadget = "8B442408C700F095BE6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DBE95F0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DBF0B40(self):
		#sub_6DBF0B40
		gadget = "8B442408C700C007BF6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DBF07C0
		#mov     eax, 1
		#retn


  def test_gadget_j_nullsub_1(self):
		#j_nullsub_1
		gadget = "E93BD32900"
		self.do(gadget)

		#jmp     nullsub_1


  def test_gadget_sub_6DBFE5B0(self):
		#sub_6DBFE5B0
		gadget = "8B442404C74004FFFFFFFFC70007000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 7
		#retn


  def test_gadget_sub_6DBFE5D0(self):
		#sub_6DBFE5D0
		gadget = "8B442404C74004FFFFFFFFC7000E000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0Eh
		#retn


  def test_gadget_sub_6DBFE5F0(self):
		#sub_6DBFE5F0
		gadget = "8B442404C74004FFFFFFFFC7000F000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0Fh
		#retn


  def test_gadget_sub_6DBFE610(self):
		#sub_6DBFE610
		gadget = "8B442404C74004FFFFFFFFC70011000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 11h
		#retn


  def test_gadget_sub_6DBFE630(self):
		#sub_6DBFE630
		gadget = "8B442404C74004FFFFFFFFC70014000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 14h
		#retn


  def test_gadget_sub_6DBFE650(self):
		#sub_6DBFE650
		gadget = "8B442404C74004FFFFFFFFC70015000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 15h
		#retn


  def test_gadget_sub_6DBFE670(self):
		#sub_6DBFE670
		gadget = "8B442404C74004FFFFFFFFC70019000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 19h
		#retn


  def test_gadget_sub_6DC034B0(self):
		#sub_6DC034B0
		gadget = "8B4424048B088B54240833C03B0A0F94C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax]
		#mov     edx, [esp+arg_4]
		#xor     eax, eax
		#cmp     ecx, [edx]
		#setz    al
		#retn


  def test_gadget_sub_6DC0E330(self):
		#sub_6DC0E330
		gadget = "8B442408C70070DFC06DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC0DF70
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC0E610(self):
		#sub_6DC0E610
		gadget = "8B442404C74004FFFFFFFFC70008000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 8
		#retn


  def test_gadget_sub_6DC0E630(self):
		#sub_6DC0E630
		gadget = "8B442404C74004FFFFFFFFC70040000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 40h
		#retn


  def test_gadget_sub_6DC0E650(self):
		#sub_6DC0E650
		gadget = "8B442404C74004FFFFFFFFC70000020000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 200h
		#retn


  def test_gadget_sub_6DC0E670(self):
		#sub_6DC0E670
		gadget = "8B442404C74004FFFFFFFFC70000040000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 400h
		#retn


  def test_gadget_sub_6DC0E690(self):
		#sub_6DC0E690
		gadget = "8B442404C74004FFFFFFFFC70000100000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 1000h
		#retn


  def test_gadget_sub_6DC0E6B0(self):
		#sub_6DC0E6B0
		gadget = "8B442404C74004FFFFFFFFC70000200000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 2000h
		#retn


  def test_gadget_sub_6DC0E6D0(self):
		#sub_6DC0E6D0
		gadget = "8B442404C74004FFFFFFFFC70000400000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 4000h
		#retn


  def test_gadget_sub_6DC0E6F0(self):
		#sub_6DC0E6F0
		gadget = "8B442404C74004FFFFFFFFC70000800000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 8000h
		#retn


  def test_gadget_sub_6DC0E850(self):
		#sub_6DC0E850
		gadget = "8B44240C8B500C0FB7521C8B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#movzx   edx, word ptr [edx+1Ch]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DC0F6D0(self):
		#sub_6DC0F6D0
		gadget = "8B442408C70000F3C06DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC0F300
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC0FCB0(self):
		#sub_6DC0FCB0
		gadget = "8B44240C8B500C0FB752048B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#movzx   edx, word ptr [edx+4]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DC12640(self):
		#sub_6DC12640
		gadget = "8B442408C700A022C16DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC122A0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC135B0(self):
		#sub_6DC135B0
		gadget = "8B4C240C8B510C8B4424048B4A48C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+48h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC135D0(self):
		#sub_6DC135D0
		gadget = "8B4C240C8B510C8B4424048B4A4CC74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+4Ch]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC135F0(self):
		#sub_6DC135F0
		gadget = "8B44240C8B480C8B41508B4C24049983E23F03C2C1F8068901C74104FFFFFFFF8BC1C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [eax+0Ch]
		#mov     eax, [ecx+50h]
		#mov     ecx, [esp+arg_0]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#mov     [ecx], eax
		#mov     dword ptr [ecx+4], 0FFFFFFFFh
		#mov     eax, ecx
		#retn


  def test_gadget_sub_6DC13620(self):
		#sub_6DC13620
		gadget = "8B44240C8B480C8B41548B4C24049983E23F03C2C1F8068901C74104FFFFFFFF8BC1C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [eax+0Ch]
		#mov     eax, [ecx+54h]
		#mov     ecx, [esp+arg_0]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#mov     [ecx], eax
		#mov     dword ptr [ecx+4], 0FFFFFFFFh
		#mov     eax, ecx
		#retn


  def test_gadget_sub_6DC136D0(self):
		#sub_6DC136D0
		gadget = "8B44240C8B500C0FB792800000008B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#movzx   edx, word ptr [edx+80h]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DC15210(self):
		#sub_6DC15210
		gadget = "8B442408C7008050C16DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC15080
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC16750(self):
		#sub_6DC16750
		gadget = "8B442408C700E063C16DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC163E0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC18020(self):
		#sub_6DC18020
		gadget = "8B44240C8B500C0FB752488B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#movzx   edx, word ptr [edx+48h]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DC18F00(self):
		#sub_6DC18F00
		gadget = "8B442408C70010FFE36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE3FF10
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC1F040(self):
		#sub_6DC1F040
		gadget = "8B442404C74004FFFFFFFFC700FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0FFFFFFFFh
		#retn


  def test_gadget_sub_6DC1F060(self):
		#sub_6DC1F060
		gadget = "8B442404C74004FFFFFFFFC70020000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 20h
		#retn


  def test_gadget_sub_6DC1F080(self):
		#sub_6DC1F080
		gadget = "8B442404C74004FFFFFFFFC70080000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 80h
		#retn


  def test_gadget_sub_6DC1F0A0(self):
		#sub_6DC1F0A0
		gadget = "8B442404C74004FFFFFFFFC70000010000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 100h
		#retn


  def test_gadget_sub_6DC1F0C0(self):
		#sub_6DC1F0C0
		gadget = "8B442404C74004FFFFFFFFC70000080000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 800h
		#retn


  def test_gadget_sub_6DC21E90(self):
		#sub_6DC21E90
		gadget = "8B44240C8B500C0FB752388B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#movzx   edx, word ptr [edx+38h]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DC22680(self):
		#sub_6DC22680
		gadget = "8B442408C7000023C26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC22300
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC23050(self):
		#sub_6DC23050
		gadget = "8B442408C700B02CC26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC22CB0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC239A0(self):
		#sub_6DC239A0
		gadget = "8B442408C7002036C26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC23620
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC24D80(self):
		#sub_6DC24D80
		gadget = "8B442408C700004AC26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC24A00
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC262A0(self):
		#sub_6DC262A0
		gadget = "8B442404C74004FFFFFFFFC70002000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 2
		#retn


  def test_gadget_sub_6DC2B6F0(self):
		#sub_6DC2B6F0
		gadget = "8B442408C70030B3C26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC2B330
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC2CAA0(self):
		#sub_6DC2CAA0
		gadget = "8B4C240C8B510C8B4424048B4A3CC74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+3Ch]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC2DCC0(self):
		#sub_6DC2DCC0
		gadget = "8B442408C70000D9C26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC2D900
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC31100(self):
		#sub_6DC31100
		gadget = "8B442408C700400DC36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC30D40
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC314C0(self):
		#sub_6DC314C0
		gadget = "8B4C240C8B510C8B4424048B8A90000000C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+90h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC314E0(self):
		#sub_6DC314E0
		gadget = "8B4C240C8B510C8B4424048B8A94000000C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+94h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC320E0(self):
		#sub_6DC320E0
		gadget = "8B442408C700D008E26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE208D0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC34F10(self):
		#sub_6DC34F10
		gadget = "8B442408C7009001E26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE20190
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC36060(self):
		#sub_6DC36060
		gadget = "8B442408C700300AE36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE30A30
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC37A70(self):
		#sub_6DC37A70
		gadget = "8B4424048B542408C74128FFFFFFFFC7412C00000000C7010000000089411889511CC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     dword ptr [ecx+28h], 0FFFFFFFFh
		#mov     dword ptr [ecx+2Ch], 0
		#mov     dword ptr [ecx], 0
		#mov     [ecx+18h], eax
		#mov     [ecx+1Ch], edx
		#retn    8


  def test_gadget_sub_6DC3A970(self):
		#sub_6DC3A970
		gadget = "8B442408C70070A8C36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC3A870
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC3D890(self):
		#sub_6DC3D890
		gadget = "8B442408C70090D7C36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC3D790
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC3E580(self):
		#sub_6DC3E580
		gadget = "8B411C03C003C003C0C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#add     eax, eax
		#add     eax, eax
		#add     eax, eax
		#retn


  def test_gadget_sub_6DC40910(self):
		#sub_6DC40910
		gadget = "8B442408C7001008C46DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC40810
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC41F00(self):
		#sub_6DC41F00
		gadget = "8B411C03C003C0C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#add     eax, eax
		#add     eax, eax
		#retn


  def test_gadget_sub_6DC44230(self):
		#sub_6DC44230
		gadget = "8B442408C7003041C46DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC44130
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC52970(self):
		#sub_6DC52970
		gadget = "8B442408C7000029C56DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset loc_6DC52900
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC553C0(self):
		#sub_6DC553C0
		gadget = "8B442408C700C052C56DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC552C0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC55C70(self):
		#sub_6DC55C70
		gadget = "8B411CC3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#retn


  def test_gadget_sub_6DC57F80(self):
		#sub_6DC57F80
		gadget = "8B442408C700807EC56DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC57E80
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC5AC30(self):
		#sub_6DC5AC30
		gadget = "8B442408C70030ABC56DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC5AB30
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC5AC40(self):
		#sub_6DC5AC40
		gadget = "8B442404C74004FFFFFFFFC70004000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 4
		#retn


  def test_gadget_sub_6DC5DA10(self):
		#sub_6DC5DA10
		gadget = "8B442408C70010D9C56DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC5D910
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC5E360(self):
		#sub_6DC5E360
		gadget = "8B411C03C0C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#add     eax, eax
		#retn


  def test_gadget_sub_6DC60770(self):
		#sub_6DC60770
		gadget = "8B442408C7007006C66DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC60670
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC60780(self):
		#sub_6DC60780
		gadget = "8B442408C70050AAE26DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE2AA50
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC658C0(self):
		#sub_6DC658C0
		gadget = "8B442408C700F055C66DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC655F0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DC8D750(self):
		#sub_6DC8D750
		gadget = "8B442408C700E0D0C86DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DC8D0E0
		#mov     eax, 1
		#retn


  def test_gadget_j_j_j_nullsub_1(self):
		#j_j_j_nullsub_1
		gadget = "E9EB38F5FF"
		self.do(gadget)

		#jmp     j_j_nullsub_1


  def test_gadget_sub_6DC93FD0(self):
		#sub_6DC93FD0
		gadget = "8B4C240C8B510C8B4424048B8AB8000000C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+0B8h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC989D0(self):
		#sub_6DC989D0
		gadget = "8B4C240C8B510C8B4424048B4A34C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+34h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC9BE60(self):
		#sub_6DC9BE60
		gadget = "8B4C240C8B510C8B4424048B4A74C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+74h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC9BEB0(self):
		#sub_6DC9BEB0
		gadget = "8B4C240C8B510C8B4424048B4A70C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+70h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC9FBE0(self):
		#sub_6DC9FBE0
		gadget = "8B4C240C8B510C8B4424048B4A04C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+4]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DC9FC00(self):
		#sub_6DC9FC00
		gadget = "8B4C240C8B510C8B4424048B4A08C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+8]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DCA1CF0(self):
		#sub_6DCA1CF0
		gadget = "8B442408C700601BCA6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DCA1B60
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DCA9B70(self):
		#sub_6DCA9B70
		gadget = "8B4C240C8B510C8B4424048B4A1CC74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+1Ch]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DCA9B90(self):
		#sub_6DCA9B90
		gadget = "8B4C240C8B510C8B4424048B4A20C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+20h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DCA9BB0(self):
		#sub_6DCA9BB0
		gadget = "8B4C240C8B510C8B4424048B4A24C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+24h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DCE4050(self):
		#sub_6DCE4050
		gadget = "8B442408C700A03BCE6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DCE3BA0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DCE88B0(self):
		#sub_6DCE88B0
		gadget = "8B442404C74004FFFFFFFFC700FF000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0FFh
		#retn


  def test_gadget_sub_6DCEA620(self):
		#sub_6DCEA620
		gadget = "8B442408C7000038E46DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE43800
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DCF2C20(self):
		#sub_6DCF2C20
		gadget = "8B442408C7003028CF6DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DCF2830
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD04490(self):
		#sub_6DD04490
		gadget = "8B44240C8B480C8B4424048B490483CAFF8908895004C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [eax+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+4]
		#or      edx, 0FFFFFFFFh
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#retn


  def test_gadget_sub_6DD06200(self):
		#sub_6DD06200
		gadget = "8B442408C70070D03D6EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E3DD070
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD07160(self):
		#sub_6DD07160
		gadget = "8B442408C700A0093D6EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E3D09A0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD0C760(self):
		#sub_6DD0C760
		gadget = "8B442408C70080C6D06DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DD0C680
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD0F880(self):
		#sub_6DD0F880
		gadget = "8B442408C700F0F6D06DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DD0F6F0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD0F9E0(self):
		#sub_6DD0F9E0
		gadget = "8B442404C74004FFFFFFFFC70065000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 65h
		#retn


  def test_gadget_sub_6DD0FA00(self):
		#sub_6DD0FA00
		gadget = "8B442404C74004FFFFFFFFC70066000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 66h
		#retn


  def test_gadget_sub_6DD12E40(self):
		#sub_6DD12E40
		gadget = "8B442408C700602DD16DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DD12D60
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD13710(self):
		#sub_6DD13710
		gadget = "8B442404C74004FFFFFFFFC70033000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 33h
		#retn


  def test_gadget_sub_6DD13730(self):
		#sub_6DD13730
		gadget = "8B442404C74004FFFFFFFFC70034000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 34h
		#retn


  def test_gadget_sub_6DD17180(self):
		#sub_6DD17180
		gadget = "8B442408C700A070D16DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DD170A0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD183D0(self):
		#sub_6DD183D0
		gadget = "8B442408C700E082D16DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DD182E0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DD19800(self):
		#sub_6DD19800
		gadget = "33C0837908020F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx+8], 2
		#setz    al
		#retn


  def test_gadget_sub_6DD19820(self):
		#sub_6DD19820
		gadget = "B001C20800"
		self.do(gadget)

		#mov     al, 1
		#retn    8


  def test_gadget_sub_6DD1CB70(self):
		#sub_6DD1CB70
		gadget = "8B442404C74004FFFFFFFFC70003000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 3
		#retn


  def test_gadget_sub_6DD1CC20(self):
		#sub_6DD1CC20
		gadget = "8B4C240C8B510C8B4A148B4424048B11C74004FFFFFFFF8910C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     ecx, [edx+14h]
		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], edx
		#retn


  def test_gadget_sub_6DD20470(self):
		#sub_6DD20470
		gadget = "8B4C240C8B510C8B4A188B4424048B11C74004FFFFFFFF8910C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     ecx, [edx+18h]
		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], edx
		#retn


  def test_gadget_sub_6DD2A1E0(self):
		#sub_6DD2A1E0
		gadget = "8B442404C74004FFFFFFFFC70001000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 1
		#retn


  def test_gadget_j_j_j_j_nullsub_1(self):
		#j_j_j_j_nullsub_1
		gadget = "E93B13F4FF"
		self.do(gadget)

		#jmp     j_j_j_nullsub_1


  def test_gadget_sub_6DD57010(self):
		#sub_6DD57010
		gadget = "8B442404C74004FFFFFFFFC70000000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0
		#retn


  def test_gadget_sub_6DD6AFB0(self):
		#sub_6DD6AFB0
		gadget = "8B442404C74004FFFFFFFFC70067000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 67h
		#retn


  def test_gadget_sub_6DD6AFD0(self):
		#sub_6DD6AFD0
		gadget = "8B442404C74004FFFFFFFFC70068000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 68h
		#retn


  def test_gadget_sub_6DD6AFF0(self):
		#sub_6DD6AFF0
		gadget = "8B442404C74004FFFFFFFFC70069000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 69h
		#retn


  def test_gadget_sub_6DD6B010(self):
		#sub_6DD6B010
		gadget = "8B442404C74004FFFFFFFFC7006A000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 6Ah
		#retn


  def test_gadget_sub_6DD6B030(self):
		#sub_6DD6B030
		gadget = "8B442404C74004FFFFFFFFC7006B000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 6Bh
		#retn


  def test_gadget_sub_6DD6B050(self):
		#sub_6DD6B050
		gadget = "8B4C240C8B510C8B4424048B4A14C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+14h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DD74A90(self):
		#sub_6DD74A90
		gadget = "8B442404C74004FFFFFFFFC7000C000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 0Ch
		#retn


  def test_gadget_sub_6DD74AB0(self):
		#sub_6DD74AB0
		gadget = "8B442404C74004FFFFFFFFC70012000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 12h
		#retn


  def test_gadget_sub_6DD74AD0(self):
		#sub_6DD74AD0
		gadget = "8B442404C74004FFFFFFFFC70013000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 13h
		#retn


  def test_gadget_sub_6DD81960(self):
		#sub_6DD81960
		gadget = "8B44240C8B500C8B42140FB7108B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#mov     eax, [edx+14h]
		#movzx   edx, word ptr [eax]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DD81980(self):
		#sub_6DD81980
		gadget = "8B44240C8B500C8B42140FB750048B44240483C9FF8910894804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [eax+0Ch]
		#mov     eax, [edx+14h]
		#movzx   edx, word ptr [eax+4]
		#mov     eax, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn


  def test_gadget_sub_6DD85EE0(self):
		#sub_6DD85EE0
		gadget = "8B442404C74004FFFFFFFFC70005000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 5
		#retn


  def test_gadget_sub_6DD8B930(self):
		#sub_6DD8B930
		gadget = "8B4C240C8B510C8B4424048B8A14010000C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+114h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_j_j_j_j_j_j_nullsub_1(self):
		#j_j_j_j_j_j_nullsub_1
		gadget = "E93B0D0000"
		self.do(gadget)

		#jmp     j_j_j_j_j_nullsub_1


  def test_gadget_j_j_j_j_j_nullsub_1(self):
		#j_j_j_j_j_nullsub_1
		gadget = "E92B96FBFF"
		self.do(gadget)

		#jmp     j_j_j_j_nullsub_1


  def test_gadget_sub_6DD97BB0(self):
		#sub_6DD97BB0
		gadget = "8B442404C74004FFFFFFFFC70006000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     dword ptr [eax], 6
		#retn


  def test_gadget_sub_6DD9F380(self):
		#sub_6DD9F380
		gadget = "8B4C240C8B510C8B4424048B4A78C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+78h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget_sub_6DDA07B0(self):
		#sub_6DDA07B0
		gadget = "8B4C240C8B510C8B4424048B4A10C74004FFFFFFFF8908C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+0Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [edx+10h]
		#mov     dword ptr [eax+4], 0FFFFFFFFh
		#mov     [eax], ecx
		#retn


  def test_gadget__Java_com_sun_webkit_dom_CSSValueListImpl_getLengthImpl(self):
		#_Java_com_sun_webkit_dom_CSSValueListImpl_getLengthImpl16
		gadget = "8B44240C8B4020C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+20h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MediaListImpl_getLengthImpl(self):
		#_Java_com_sun_webkit_dom_MediaListImpl_getLengthImpl16
		gadget = "8B44240C8B48048B4110C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [eax+4]
		#mov     eax, [ecx+10h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_DocumentImpl_getXmlStandaloneImpl(self):
		#_Java_com_sun_webkit_dom_DocumentImpl_getXmlStandaloneImpl16
		gadget = "8B44240C8B882C04000080E10333C080F9010F94C0C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [eax+42Ch]
		#and     cl, 3
		#xor     eax, eax
		#cmp     cl, 1
		#setz    al
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_DocumentImpl_getWebkitIsFullScreenImpl(self):
		#_Java_com_sun_webkit_dom_DocumentImpl_getWebkitIsFullScreenImpl16
		gadget = "8B44240C83B828050000000F95C0C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#cmp     dword ptr [eax+528h], 0
		#setnz   al
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_ElementImpl_isHTMLElementImpl(self):
		#_Java_com_sun_webkit_dom_ElementImpl_isHTMLElementImpl16
		gadget = "8B44240C8B400CC1E8042401C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+0Ch]
		#shr     eax, 4
		#and     al, 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_getEventPhaseImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_getEventPhaseImpl16
		gadget = "8B44240C668B401CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ax, [eax+1Ch]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_getCancelableImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_getCancelableImpl16
		gadget = "8B44240C8A4015C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+15h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_getTimeStampImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_getTimeStampImpl16
		gadget = "8B4C240C8B41288B512CC21000"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     eax, [ecx+28h]
		#mov     edx, [ecx+2Ch]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_getDefaultPreventedImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_getDefaultPreventedImpl16
		gadget = "8B44240C8A4018C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+18h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_getCancelBubbleImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_getCancelBubbleImpl16
		gadget = "8B44240C8A401AC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+1Ah]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_setCancelBubbleImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_setCancelBubbleImpl20
		gadget = "807C2414008B4C240C0F95C088411AC21400"
		self.do(gadget)

		#cmp     [esp+arg_10], 0
		#mov     ecx, [esp+arg_8]
		#setnz   al
		#mov     [ecx+1Ah], al
		#retn    14h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_stopPropagationImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_stopPropagationImpl16
		gadget = "8B44240CC6401601C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     byte ptr [eax+16h], 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_stopImmediatePropagationImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_stopImmediatePropagationImpl16
		gadget = "8B44240CC6401701C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     byte ptr [eax+17h], 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_getReturnValueImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_getReturnValueImpl16
		gadget = "8B4C240C33C03841180F94C0C21000"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#xor     eax, eax
		#cmp     [ecx+18h], al
		#setz    al
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_EventImpl_setReturnValueImpl(self):
		#_Java_com_sun_webkit_dom_EventImpl_setReturnValueImpl20
		gadget = "807C2414008B4C240C0F94C0884118C21400"
		self.do(gadget)

		#cmp     [esp+arg_10], 0
		#mov     ecx, [esp+arg_8]
		#setz    al
		#mov     [ecx+18h], al
		#retn    14h


  def test_gadget__Java_com_sun_webkit_dom_KeyboardEventImpl_getKeyLocationImpl(self):
		#_Java_com_sun_webkit_dom_KeyboardEventImpl_getKeyLocationImpl16
		gadget = "8B44240C8B4050C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+50h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_KeyboardEventImpl_getAltGraphKeyImpl(self):
		#_Java_com_sun_webkit_dom_KeyboardEventImpl_getAltGraphKeyImpl16
		gadget = "8B44240C8A40542401C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+54h]
		#and     al, 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MouseEventImpl_getScreenXImpl(self):
		#_Java_com_sun_webkit_dom_MouseEventImpl_getScreenXImpl16
		gadget = "8B44240C8B4048C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+48h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MouseEventImpl_getScreenYImpl(self):
		#_Java_com_sun_webkit_dom_MouseEventImpl_getScreenYImpl16
		gadget = "8B44240C8B404CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+4Ch]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MouseEventImpl_getClientXImpl(self):
		#_Java_com_sun_webkit_dom_MouseEventImpl_getClientXImpl16
		gadget = "8B44240C8B40509983E23F03C2C1F806C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+50h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MouseEventImpl_getClientYImpl(self):
		#_Java_com_sun_webkit_dom_MouseEventImpl_getClientYImpl16
		gadget = "8B44240C8B40549983E23F03C2C1F806C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+54h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MouseEventImpl_getButtonImpl(self):
		#_Java_com_sun_webkit_dom_MouseEventImpl_getButtonImpl16
		gadget = "8B44240C668B8080000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ax, [eax+80h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_MutationEventImpl_getAttrChangeImpl(self):
		#_Java_com_sun_webkit_dom_MutationEventImpl_getAttrChangeImpl16
		gadget = "8B44240C668B4048C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ax, [eax+48h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_NodeImpl_isSameNodeImpl(self):
		#_Java_com_sun_webkit_dom_NodeImpl_isSameNodeImpl24
		gadget = "8B4C240C33C03B4C24140F94C0C21800"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#xor     eax, eax
		#cmp     ecx, [esp+arg_10]
		#setz    al
		#retn    18h


  def test_gadget__Java_com_sun_webkit_dom_NodeIteratorImpl_getPointerBeforeReferenceNodeImpl(self):
		#_Java_com_sun_webkit_dom_NodeIteratorImpl_getPointerBeforeReferenceNodeImpl16
		gadget = "8B44240C8A401CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+1Ch]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_UIEventImpl_getDetailImpl(self):
		#_Java_com_sun_webkit_dom_UIEventImpl_getDetailImpl16
		gadget = "8B44240C8B403CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+3Ch]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_WheelEventImpl_getWheelDeltaXImpl(self):
		#_Java_com_sun_webkit_dom_WheelEventImpl_getWheelDeltaXImpl16
		gadget = "8B44240C8B8090000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+90h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_WheelEventImpl_getWheelDeltaYImpl(self):
		#_Java_com_sun_webkit_dom_WheelEventImpl_getWheelDeltaYImpl16
		gadget = "8B44240C8B8094000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+94h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_WheelEventImpl_getDeltaModeImpl(self):
		#_Java_com_sun_webkit_dom_WheelEventImpl_getDeltaModeImpl16
		gadget = "8B44240C8B80A0000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+0A0h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_WheelEventImpl_getWebkitDirectionInvertedFromDeviceImpl(self):
		#_Java_com_sun_webkit_dom_WheelEventImpl_getWebkitDirectionInvertedFromDeviceImpl16
		gadget = "8B44240C8A80A4000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+0A4h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLInputElementImpl_getCheckedImpl(self):
		#_Java_com_sun_webkit_dom_HTMLInputElementImpl_getCheckedImpl16
		gadget = "8B44240C8A80860000002401C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+86h]
		#and     al, 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLInputElementImpl_getIndeterminateImpl(self):
		#_Java_com_sun_webkit_dom_HTMLInputElementImpl_getIndeterminateImpl16
		gadget = "8B44240C8A8086000000C0E8022401C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+86h]
		#shr     al, 2
		#and     al, 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLObjectElementImpl_checkValidityImpl(self):
		#_Java_com_sun_webkit_dom_HTMLObjectElementImpl_checkValidityImpl16
		gadget = "B001C21000"
		self.do(gadget)

		#mov     al, 1
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLSelectElementImpl_getMultipleImpl(self):
		#_Java_com_sun_webkit_dom_HTMLSelectElementImpl_getMultipleImpl16
		gadget = "8B44240C8A80C9000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     al, [eax+0C9h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLSelectElementImpl_getSizeImpl(self):
		#_Java_com_sun_webkit_dom_HTMLSelectElementImpl_getSizeImpl16
		gadget = "8B44240C8B80B8000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+0B8h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLTableColElementImpl_getSpanImpl(self):
		#_Java_com_sun_webkit_dom_HTMLTableColElementImpl_getSpanImpl16
		gadget = "8B44240C8B4034C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+34h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLTextAreaElementImpl_getColsImpl(self):
		#_Java_com_sun_webkit_dom_HTMLTextAreaElementImpl_getColsImpl16
		gadget = "8B44240C8B4074C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+74h]
		#retn    10h


  def test_gadget__Java_com_sun_webkit_dom_HTMLTextAreaElementImpl_getRowsImpl(self):
		#_Java_com_sun_webkit_dom_HTMLTextAreaElementImpl_getRowsImpl16
		gadget = "8B44240C8B4070C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     eax, [eax+70h]
		#retn    10h


  def test_gadget_sub_6DDCAB30(self):
		#sub_6DDCAB30
		gadget = "8BC18B4C2404890889480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483C894840894844894848C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#retn    4


  def test_gadget_sub_6DDD7540(self):
		#sub_6DDD7540
		gadget = "8B44240489410CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+0Ch], eax
		#retn    4


  def test_gadget_sub_6DDD7550(self):
		#sub_6DDD7550
		gadget = "8B442404894120C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+20h], eax
		#retn    4


  def test_gadget_sub_6DDD7560(self):
		#sub_6DDD7560
		gadget = "8B442404894124C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+24h], eax
		#retn    4


  def test_gadget_sub_6DDD7570(self):
		#sub_6DDD7570
		gadget = "8B442404894128C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+28h], eax
		#retn    4


  def test_gadget_sub_6DDD7580(self):
		#sub_6DDD7580
		gadget = "8B44240489412CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+2Ch], eax
		#retn    4


  def test_gadget_sub_6DDD7590(self):
		#sub_6DDD7590
		gadget = "8B442404894130C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+30h], eax
		#retn    4


  def test_gadget_sub_6DDD75A0(self):
		#sub_6DDD75A0
		gadget = "8B442404894134C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+34h], eax
		#retn    4


  def test_gadget_sub_6DDD75B0(self):
		#sub_6DDD75B0
		gadget = "8B44240489413CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+3Ch], eax
		#retn    4


  def test_gadget_sub_6DDD75C0(self):
		#sub_6DDD75C0
		gadget = "8B442404894140C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+40h], eax
		#retn    4


  def test_gadget_sub_6DDD75D0(self):
		#sub_6DDD75D0
		gadget = "8B442404894144C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+44h], eax
		#retn    4


  def test_gadget_sub_6DDD75E0(self):
		#sub_6DDD75E0
		gadget = "8B44240489414CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+4Ch], eax
		#retn    4


  def test_gadget_sub_6DDD75F0(self):
		#sub_6DDD75F0
		gadget = "8B442404894150C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+50h], eax
		#retn    4


  def test_gadget_sub_6DDD7600(self):
		#sub_6DDD7600
		gadget = "8B442404894154C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+54h], eax
		#retn    4


  def test_gadget_Get_deleter(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DE0BA10(self):
		#sub_6DE0BA10
		gadget = "8B412C83C00CC3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#add     eax, 0Ch
		#retn


  def test_gadget_sub_6DE0BA20(self):
		#sub_6DE0BA20
		gadget = "8B412C83C008C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#add     eax, 8
		#retn


  def test_gadget_sub_6DE0BA30(self):
		#sub_6DE0BA30
		gadget = "8B412C83C010C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#add     eax, 10h
		#retn


  def test_gadget_sub_6DE0BA70(self):
		#sub_6DE0BA70
		gadget = "518B442408C7042400000000C7000000000059C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    4


  def test_gadget_sub_6DE14EC0(self):
		#sub_6DE14EC0
		gadget = "B83895A46EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA49538
		#retn


  def test_gadget_sub_6DE17290(self):
		#sub_6DE17290
		gadget = "B8B497A46EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA497B4
		#retn


  def test_gadget_sub_6DE18510(self):
		#sub_6DE18510
		gadget = "B8C895836EC3"
		self.do(gadget)

		#mov     eax, offset off_6E8395C8
		#retn


  def test_gadget_sub_6DE18520(self):
		#sub_6DE18520
		gadget = "B82821846EC3"
		self.do(gadget)

		#mov     eax, offset off_6E842128
		#retn


  def test_gadget_sub_6DE1B4F0(self):
		#sub_6DE1B4F0
		gadget = "8BC133C9890889480489480889480CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn


  def test_gadget_sub_6DE1B520(self):
		#sub_6DE1B520
		gadget = "8BC1836008F880600CFEC70000000000C7400400000000C7401001000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#and     dword ptr [eax+8], 0FFFFFFF8h
		#and     byte ptr [eax+0Ch], 0FEh
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 0
		#mov     dword ptr [eax+10h], 1
		#retn


  def test_gadget_sub_6DE1C000(self):
		#sub_6DE1C000
		gadget = "8BC133C98908894804894808C6400C01894810894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     byte ptr [eax+0Ch], 1
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_6DE1C710(self):
		#sub_6DE1C710
		gadget = "8B41148B800401000083E03FC3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#and     eax, 3Fh
		#retn


  def test_gadget_sub_6DE1D0D0(self):
		#sub_6DE1D0D0
		gadget = "8BC18B4C24048B11568B7104C1E2068910C1E6068970048B51088B490CC1E206C1E10689500889480C5EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#push    esi
		#mov     esi, [ecx+4]
		#shl     edx, 6
		#mov     [eax], edx
		#shl     esi, 6
		#mov     [eax+4], esi
		#mov     edx, [ecx+8]
		#mov     ecx, [ecx+0Ch]
		#shl     edx, 6
		#shl     ecx, 6
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#pop     esi
		#retn    4


  def test_gadget_sub_6DE1D620(self):
		#sub_6DE1D620
		gadget = "8B41188B4058C1E81283E007C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 12h
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE1E1E0(self):
		#sub_6DE1E1E0
		gadget = "8D4120C3"
		self.do(gadget)

		#lea     eax, [ecx+20h]
		#retn


  def test_gadget_sub_6DE1F660(self):
		#sub_6DE1F660
		gadget = "83EC088B44240C8B48E88B40EC8B098B5104894424048B820003000083C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [esp+8+arg_0]
		#mov     ecx, [eax-18h]
		#mov     eax, [eax-14h]
		#mov     ecx, [ecx]
		#mov     edx, [ecx+4]
		#mov     [esp+8+var_4], eax
		#mov     eax, [edx+300h]
		#add     esp, 8
		#retn


  def test_gadget_sub_6DE1F7A0(self):
		#sub_6DE1F7A0
		gadget = "8B4424048B808448000083C004C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+4884h]
		#add     eax, 4
		#retn


  def test_gadget_sub_6DE1F7B0(self):
		#sub_6DE1F7B0
		gadget = "8B4424048B88844800008B412CC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+4884h]
		#mov     eax, [ecx+2Ch]
		#retn


  def test_gadget_sub_6DE20080(self):
		#sub_6DE20080
		gadget = "DD442404C20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#retn    8


  def test_gadget_sub_6DE21A50(self):
		#sub_6DE21A50
		gadget = "8B44240483C0BF66B91900663BC81BC040C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 0FFFFFFBFh
		#mov     cx, 19h
		#cmp     cx, ax
		#sbb     eax, eax
		#inc     eax
		#retn


  def test_gadget_sub_6DE284F0(self):
		#sub_6DE284F0
		gadget = "83EC088B41E88B49EC5633F6250000FFFF8B80340400008B804C480000BAFAFFFFFF89B020580000894C24088990245800005E83C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#push    esi
		#xor     esi, esi
		#and     eax, 0FFFF0000h
		#mov     eax, [eax+434h]
		#mov     eax, [eax+484Ch]
		#mov     edx, 0FFFFFFFAh
		#mov     [eax+5820h], esi
		#mov     [esp+0Ch+var_4], ecx
		#mov     [eax+5824h], edx
		#pop     esi
		#add     esp, 8
		#retn


  def test_gadget_sub_6DE28530(self):
		#sub_6DE28530
		gadget = "83EC088B41E88B49EC250000FFFF8B90340400008B44240C894C24048B8A4C4800008B91205800008B8924580000891089480483C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [esp+8+arg_0]
		#mov     [esp+8+var_4], ecx
		#mov     ecx, [edx+484Ch]
		#mov     edx, [ecx+5820h]
		#mov     ecx, [ecx+5824h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6DE2AB70(self):
		#sub_6DE2AB70
		gadget = "8B4424048981F8020000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+2F8h], eax
		#retn    4


  def test_gadget_sub_6DE2AB80(self):
		#sub_6DE2AB80
		gadget = "8B81F8020000C3"
		self.do(gadget)

		#mov     eax, [ecx+2F8h]
		#retn


  def test_gadget_sub_6DE2BC70(self):
		#sub_6DE2BC70
		gadget = "8B8104030000C3"
		self.do(gadget)

		#mov     eax, [ecx+304h]
		#retn


  def test_gadget_sub_6DE333F0(self):
		#sub_6DE333F0
		gadget = "8A4114C3"
		self.do(gadget)

		#mov     al, [ecx+14h]
		#retn


  def test_gadget_Get_deleter_UBEPAXABVtype_info(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_1
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_reserve_messageConcurrency(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_0
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6DE34AF0(self):
		#sub_6DE34AF0
		gadget = "8B442408C7002046E36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE34620
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DE392E0(self):
		#sub_6DE392E0
		gadget = "8BC18B4C24048908C74004000000008B4920894808C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#retn    8


  def test_gadget_sub_6DE395A0(self):
		#sub_6DE395A0
		gadget = "8B442408C700A093E36DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE393A0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DE39AF0(self):
		#sub_6DE39AF0
		gadget = "8B4424088B48D08B44240449C74004FCFFFFFFC70000000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [eax-30h]
		#mov     eax, [esp+arg_0]
		#dec     ecx
		#mov     dword ptr [eax+4], 0FFFFFFFCh
		#mov     dword ptr [eax], 0
		#retn    8


  def test_gadget_sub_6DE39C70(self):
		#sub_6DE39C70
		gadget = "83EC088B4424108B48E88B098B51048B8A8C0100008B40EC33D285C90F95C2894424048B44240C890883C2FA89500483C408C20800"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [esp+8+arg_4]
		#mov     ecx, [eax-18h]
		#mov     ecx, [ecx]
		#mov     edx, [ecx+4]
		#mov     ecx, [edx+18Ch]
		#mov     eax, [eax-14h]
		#xor     edx, edx
		#test    ecx, ecx
		#setnz   dl
		#mov     [esp+8+var_4], eax
		#mov     eax, [esp+8+arg_0]
		#mov     [eax], ecx
		#add     edx, 0FFFFFFFAh
		#mov     [eax+4], edx
		#add     esp, 8
		#retn    8


  def test_gadget_sub_6DE3E4B0(self):
		#sub_6DE3E4B0
		gadget = "8B442404C74004FCFFFFFFC70000000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFCh
		#mov     dword ptr [eax], 0
		#retn    8


  def test_gadget_sub_6DE43AC0(self):
		#sub_6DE43AC0
		gadget = "83EC088B41E88B49EC250000FFFF8B90340400008B824C4800008B8018580000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+5818h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6DE48390(self):
		#sub_6DE48390
		gadget = "8B5424048BC133C9890889480489480889480C89481089501489481888481C89482089482489482889482C894830894834894838C20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], edx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cl
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#retn    4


  def test_gadget_sub_6DE49850(self):
		#sub_6DE49850
		gadget = "8A442404884124C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+24h], al
		#retn    4


  def test_gadget_sub_6DE49860(self):
		#sub_6DE49860
		gadget = "8B44240489411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_sub_6DE49870(self):
		#sub_6DE49870
		gadget = "8A442404884120C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+20h], al
		#retn    4


  def test_gadget_sub_6DE498A0(self):
		#sub_6DE498A0
		gadget = "32C0C21800"
		self.do(gadget)

		#xor     al, al
		#retn    18h


  def test_gadget_sub_6DE4E7A0(self):
		#sub_6DE4E7A0
		gadget = "8B41088B4010C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     eax, [eax+10h]
		#retn


  def test_gadget_sub_6DE4E7B0(self):
		#sub_6DE4E7B0
		gadget = "8B41088B400CC3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     eax, [eax+0Ch]
		#retn


  def test_gadget_sub_6DE52650(self):
		#sub_6DE52650
		gadget = "8BC1C7000100000033C989480489480889480C89481089481489481889481C8B4C24048B500C568B710889700C8951088B318B500489700489118B71048B50088970088951045EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [eax+0Ch]
		#push    esi
		#mov     esi, [ecx+8]
		#mov     [eax+0Ch], esi
		#mov     [ecx+8], edx
		#mov     esi, [ecx]
		#mov     edx, [eax+4]
		#mov     [eax+4], esi
		#mov     [ecx], edx
		#mov     esi, [ecx+4]
		#mov     edx, [eax+8]
		#mov     [eax+8], esi
		#mov     [ecx+4], edx
		#pop     esi
		#retn    4


  def test_gadget_sub_6DE526A0(self):
		#sub_6DE526A0
		gadget = "8B54240C8BC1C7000100000033C989480489480889480C89501089481489481889481C8B500C8B4C2404568B710889700C8951088B318B500489700489118B71048B50088970088951048B4C240C8B71088B501C89701C8951088B318B501489701489118B71048B50188970188951045EC20C00"
		self.do(gadget)

		#mov     edx, [esp+arg_8]
		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], edx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     edx, [eax+0Ch]
		#mov     ecx, [esp+arg_0]
		#push    esi
		#mov     esi, [ecx+8]
		#mov     [eax+0Ch], esi
		#mov     [ecx+8], edx
		#mov     esi, [ecx]
		#mov     edx, [eax+4]
		#mov     [eax+4], esi
		#mov     [ecx], edx
		#mov     esi, [ecx+4]
		#mov     edx, [eax+8]
		#mov     [eax+8], esi
		#mov     [ecx+4], edx
		#mov     ecx, [esp+4+arg_4]
		#mov     esi, [ecx+8]
		#mov     edx, [eax+1Ch]
		#mov     [eax+1Ch], esi
		#mov     [ecx+8], edx
		#mov     esi, [ecx]
		#mov     edx, [eax+14h]
		#mov     [eax+14h], esi
		#mov     [ecx], edx
		#mov     esi, [ecx+4]
		#mov     edx, [eax+18h]
		#mov     [eax+18h], esi
		#mov     [ecx+4], edx
		#pop     esi
		#retn    0Ch


  def test_gadget_0facetlocalestdIAEIZ(self):
		#0facetlocalestdIAEIZ
		gadget = "8BC18B4C2404C70094E9846E894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E84E994
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DE58770(self):
		#sub_6DE58770
		gadget = "8BC18B4C2404C7400401000000C700ACE9846E894808C7400C00000000C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     dword ptr [eax], offset off_6E84E9AC
		#mov     [eax+8], ecx
		#mov     dword ptr [eax+0Ch], 0
		#retn    4


  def test_gadget_sub_6DE58790(self):
		#sub_6DE58790
		gadget = "32C0C21000"
		self.do(gadget)

		#xor     al, al
		#retn    10h


  def test_gadget_sub_6DE587A0(self):
		#sub_6DE587A0
		gadget = "8B442404C74004FAFFFFFFC70000000000C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFAh
		#mov     dword ptr [eax], 0
		#retn    0Ch


  def test_gadget_sub_6DE58C50(self):
		#sub_6DE58C50
		gadget = "A1C07EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EC0
		#retn


  def test_gadget_sub_6DE5B3D0(self):
		#sub_6DE5B3D0
		gadget = "8B442404C74004FCFFFFFFC70000000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFCh
		#mov     dword ptr [eax], 0
		#retn    10h


  def test_gadget_sub_6DE5EAF0(self):
		#sub_6DE5EAF0
		gadget = "8B410CC3"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#retn


  def test_gadget_sub_6DE5FD50(self):
		#sub_6DE5FD50
		gadget = "8B442408894108C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     [ecx+8], eax
		#retn    8


  def test_gadget_sub_6DE602B0(self):
		#sub_6DE602B0
		gadget = "8BC18B4C2408890833C9894804894808C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#retn    8


  def test_gadget_sub_6DE606B0(self):
		#sub_6DE606B0
		gadget = "8B442408C7003005E66DB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6DE60530
		#mov     eax, 1
		#retn


  def test_gadget_sub_6DE61880(self):
		#sub_6DE61880
		gadget = "8B5424108BC18B4C240C8908C74004000000008B492089480889500CC21000"
		self.do(gadget)

		#mov     edx, [esp+arg_C]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#retn    10h


  def test_gadget_sub_6DE62CC0(self):
		#sub_6DE62CC0
		gadget = "8B41F8C3"
		self.do(gadget)

		#mov     eax, [ecx-8]
		#retn


  def test_gadget_sub_6DE62CD0(self):
		#sub_6DE62CD0
		gadget = "8D4154C3"
		self.do(gadget)

		#lea     eax, [ecx+54h]
		#retn


  def test_gadget_sub_6DE648F0(self):
		#sub_6DE648F0
		gadget = "B840F4846EC3"
		self.do(gadget)

		#mov     eax, offset aNotificationco; "NotificationController"
		#retn


  def test_gadget_sub_6DE65340(self):
		#sub_6DE65340
		gadget = "8BC133C9890866894804884806C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], cx
		#mov     [eax+6], cl
		#retn


  def test_gadget_sub_6DE6B940(self):
		#sub_6DE6B940
		gadget = "8B5424048BC18B480481E10060F9FF81C9006001008948048A4C2408C7000100000089500888480CC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#and     ecx, 0FFF96000h
		#or      ecx, 16000h
		#mov     [eax+4], ecx
		#mov     cl, [esp+arg_4]
		#mov     dword ptr [eax], 1
		#mov     [eax+8], edx
		#mov     [eax+0Ch], cl
		#retn    8


  def test_gadget_Get_deleter3(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_3
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DE6C750(self):
		#sub_6DE6C750
		gadget = "D94108C20400"
		self.do(gadget)

		#fld     dword ptr [ecx+8]
		#retn    4


  def test_gadget_4(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_4
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DE6E730(self):
		#sub_6DE6E730
		gadget = "51DB01DC0D10E1846ED91C24D9042459C3"
		self.do(gadget)

		#push    ecx
		#fild    dword ptr [ecx]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+4+var_4]
		#fld     [esp+4+var_4]
		#pop     ecx
		#retn


  def test_gadget_sub_6DE6E770(self):
		#sub_6DE6E770
		gadget = "0FB6410583C0F5B9030000003BC81BC040C3"
		self.do(gadget)

		#movzx   eax, byte ptr [ecx+5]
		#add     eax, 0FFFFFFF5h
		#mov     ecx, 3
		#cmp     ecx, eax
		#sbb     eax, eax
		#inc     eax
		#retn


  def test_gadget_unknown_libname_1(self):
		#unknown_libname_1
		gadget = "8BC1C70000000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 0
		#retn


  def test_gadget_sub_6DE6E8E0(self):
		#sub_6DE6E8E0
		gadget = "8BC18B4C24048B11C701000000008910C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     dword ptr [ecx], 0
		#mov     [eax], edx
		#retn    4


  def test_gadget_1(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_1
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6DE70580(self):
		#sub_6DE70580
		gadget = "D9E88BC1DD10D9EEDD5008DD5010DD5018DD5020DD5030DD5038DD5040DD5048DD5058DD5060DD5068DD5870DD5028DD5050DD5878C3"
		self.do(gadget)

		#fld1
		#mov     eax, ecx
		#fst     qword ptr [eax]
		#fldz
		#fst     qword ptr [eax+8]
		#fst     qword ptr [eax+10h]
		#fst     qword ptr [eax+18h]
		#fst     qword ptr [eax+20h]
		#fst     qword ptr [eax+30h]
		#fst     qword ptr [eax+38h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+48h]
		#fst     qword ptr [eax+58h]
		#fst     qword ptr [eax+60h]
		#fst     qword ptr [eax+68h]
		#fstp    qword ptr [eax+70h]
		#fst     qword ptr [eax+28h]
		#fst     qword ptr [eax+50h]
		#fstp    qword ptr [eax+78h]
		#retn


  def test_gadget_sub_6DE70680(self):
		#sub_6DE70680
		gadget = "8B44240433D25633F689108B51288B492C89700489500889480C5EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     edx, edx
		#push    esi
		#xor     esi, esi
		#mov     [eax], edx
		#mov     edx, [ecx+28h]
		#mov     ecx, [ecx+2Ch]
		#mov     [eax+4], esi
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#pop     esi
		#retn    4


  def test_gadget_sub_6DE70AA0(self):
		#sub_6DE70AA0
		gadget = "518B442410C700070000008B442408C7042400000000C7000000000059C20C00"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_8]
		#mov     dword ptr [eax], 7
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    0Ch


  def test_gadget_sub_6DE73D70(self):
		#sub_6DE73D70
		gadget = "8BC18B4C24048B1189108B49048B5424088948048B4C240C89480C8B4C24188950088B118950108B49048B5424108948148A4C241489501888481CC7402000000000C21800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     ecx, [ecx+4]
		#mov     edx, [esp+arg_4]
		#mov     [eax+4], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+arg_14]
		#mov     [eax+8], edx
		#mov     edx, [ecx]
		#mov     [eax+10h], edx
		#mov     ecx, [ecx+4]
		#mov     edx, [esp+arg_C]
		#mov     [eax+14h], ecx
		#mov     cl, [esp+arg_10]
		#mov     [eax+18h], edx
		#mov     [eax+1Ch], cl
		#mov     dword ptr [eax+20h], 0
		#retn    18h


  def test_gadget_sub_6DE745C0(self):
		#sub_6DE745C0
		gadget = "8B41108B4068C1E81B83E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#mov     eax, [eax+68h]
		#shr     eax, 1Bh
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6DE74600(self):
		#sub_6DE74600
		gadget = "8B41108B4070C1E81B83E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#mov     eax, [eax+70h]
		#shr     eax, 1Bh
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6DE74640(self):
		#sub_6DE74640
		gadget = "8B41108B4078C1E81B83E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#mov     eax, [eax+78h]
		#shr     eax, 1Bh
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6DE74690(self):
		#sub_6DE74690
		gadget = "8B41108B8080000000C1E81B83E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#mov     eax, [eax+80h]
		#shr     eax, 1Bh
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6DE746C0(self):
		#sub_6DE746C0
		gadget = "8B410C8B4040C1E81B83E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     eax, [eax+40h]
		#shr     eax, 1Bh
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6DE74750(self):
		#sub_6DE74750
		gadget = "8B4108D9402CC3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#fld     dword ptr [eax+2Ch]
		#retn


  def test_gadget_sub_6DE74790(self):
		#sub_6DE74790
		gadget = "8B41148B88940000008B410CC3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+94h]
		#mov     eax, [ecx+0Ch]
		#retn


  def test_gadget_sub_6DE74940(self):
		#sub_6DE74940
		gadget = "8B41188B4058D1E883E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 1
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74980(self):
		#sub_6DE74980
		gadget = "8B41188B4058C1E81183E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 11h
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE749A0(self):
		#sub_6DE749A0
		gadget = "8B41148B8004010000C1E80D83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#shr     eax, 0Dh
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE749B0(self):
		#sub_6DE749B0
		gadget = "8B41148B482C8B411083E007C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+2Ch]
		#mov     eax, [ecx+10h]
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE749C0(self):
		#sub_6DE749C0
		gadget = "8B41148B482C8B4110C1E80683E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+2Ch]
		#mov     eax, [ecx+10h]
		#shr     eax, 6
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE749D0(self):
		#sub_6DE749D0
		gadget = "8B41148B482C8B4110C1E80583E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+2Ch]
		#mov     eax, [ecx+10h]
		#shr     eax, 5
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE749E0(self):
		#sub_6DE749E0
		gadget = "8B41148B482C8B4110C1E80383E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+2Ch]
		#mov     eax, [ecx+10h]
		#shr     eax, 3
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74A30(self):
		#sub_6DE74A30
		gadget = "8B41148B8000010000C1E80B83E007C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 0Bh
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE74A40(self):
		#sub_6DE74A40
		gadget = "8B41148B8000010000C1E80E83E007C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 0Eh
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE74A50(self):
		#sub_6DE74A50
		gadget = "8B41148B8000010000C1E81183E007C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 11h
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE74A60(self):
		#sub_6DE74A60
		gadget = "8B41148B48308B411483E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+30h]
		#mov     eax, [ecx+14h]
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74A70(self):
		#sub_6DE74A70
		gadget = "8B41148B48308B4114C1E80283E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+30h]
		#mov     eax, [ecx+14h]
		#shr     eax, 2
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74A80(self):
		#sub_6DE74A80
		gadget = "8B41148B8000010000C1E81483E007C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 14h
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE74A90(self):
		#sub_6DE74A90
		gadget = "8B41148B4054C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+54h]
		#retn


  def test_gadget_sub_6DE74AA0(self):
		#sub_6DE74AA0
		gadget = "8B41048B4040C1E80283E001C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     eax, [eax+40h]
		#shr     eax, 2
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74AB0(self):
		#sub_6DE74AB0
		gadget = "8B41048B4040D1E883E001C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     eax, [eax+40h]
		#shr     eax, 1
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74B00(self):
		#sub_6DE74B00
		gadget = "8B41148B48348B411483E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+34h]
		#mov     eax, [ecx+14h]
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B10(self):
		#sub_6DE74B10
		gadget = "8B41148B48348B4114C1E01BC1F81DC3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+34h]
		#mov     eax, [ecx+14h]
		#shl     eax, 1Bh
		#sar     eax, 1Dh
		#retn


  def test_gadget_sub_6DE74B20(self):
		#sub_6DE74B20
		gadget = "8B41188B4058C1E80483E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 4
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B30(self):
		#sub_6DE74B30
		gadget = "8B41148B8000010000C1E81783E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 17h
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B40(self):
		#sub_6DE74B40
		gadget = "8B41188B4058C1E80F83E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 0Fh
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B50(self):
		#sub_6DE74B50
		gadget = "8B41148B8000010000C1E81983E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 19h
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74B60(self):
		#sub_6DE74B60
		gadget = "8B41148B8000010000C1E81A83E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 1Ah
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B70(self):
		#sub_6DE74B70
		gadget = "8B41148B8000010000C1E81C83E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 1Ch
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B80(self):
		#sub_6DE74B80
		gadget = "8B41188B4058C1E80683E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 6
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74B90(self):
		#sub_6DE74B90
		gadget = "8B41188B4058C1E80883E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 8
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74BA0(self):
		#sub_6DE74BA0
		gadget = "8B41188B4058C1E80983E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 9
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74BB0(self):
		#sub_6DE74BB0
		gadget = "8B41188B4058C1E80A83E007C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 0Ah
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE74BC0(self):
		#sub_6DE74BC0
		gadget = "8B41188B4058C1E81583E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 15h
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74BD0(self):
		#sub_6DE74BD0
		gadget = "8B41148B8004010000C1E80683E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#shr     eax, 6
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74BE0(self):
		#sub_6DE74BE0
		gadget = "8B41188B4058C1E80D83E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 0Dh
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74BF0(self):
		#sub_6DE74BF0
		gadget = "8B41148B48388B4124C1E80783E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+24h]
		#shr     eax, 7
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74C00(self):
		#sub_6DE74C00
		gadget = "8B41148B48388B4124C1E80983E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+24h]
		#shr     eax, 9
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74C10(self):
		#sub_6DE74C10
		gadget = "8B41148B4838D94104C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#fld     dword ptr [ecx+4]
		#retn


  def test_gadget_sub_6DE74C20(self):
		#sub_6DE74C20
		gadget = "8B41148B48388A41202401C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     al, [ecx+20h]
		#and     al, 1
		#retn


  def test_gadget_sub_6DE74C40(self):
		#sub_6DE74C40
		gadget = "8B41148B48388A4120D0E82401C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     al, [ecx+20h]
		#shr     al, 1
		#and     al, 1
		#retn


  def test_gadget_sub_6DE74C60(self):
		#sub_6DE74C60
		gadget = "8B41148B48388A4120C0E8022401C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     al, [ecx+20h]
		#shr     al, 2
		#and     al, 1
		#retn


  def test_gadget_sub_6DE74C70(self):
		#sub_6DE74C70
		gadget = "8B41148B48388B4114C1E81B83E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+14h]
		#shr     eax, 1Bh
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6DE74CB0(self):
		#sub_6DE74CB0
		gadget = "8B41148B48388B412483E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+24h]
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74CC0(self):
		#sub_6DE74CC0
		gadget = "8B41148B48388B4124D1E883E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+24h]
		#shr     eax, 1
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74CD0(self):
		#sub_6DE74CD0
		gadget = "8B41148B48388B4124C1E80583E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+24h]
		#shr     eax, 5
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74CE0(self):
		#sub_6DE74CE0
		gadget = "8B41148B48388B4124C1E80383E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     eax, [ecx+24h]
		#shr     eax, 3
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74CF0(self):
		#sub_6DE74CF0
		gadget = "8B41148B8000010000C1E80383E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 3
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74D00(self):
		#sub_6DE74D00
		gadget = "8B41148B8000010000C1E80583E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 5
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74D10(self):
		#sub_6DE74D10
		gadget = "8B41148B8000010000D1E883E003C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 1
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74DB0(self):
		#sub_6DE74DB0
		gadget = "8B41188B4058C1E81783E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 17h
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74DC0(self):
		#sub_6DE74DC0
		gadget = "8B41188B4058C1E81B83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 1Bh
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74DD0(self):
		#sub_6DE74DD0
		gadget = "8B41188B405CC1E80C83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+5Ch]
		#shr     eax, 0Ch
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74DE0(self):
		#sub_6DE74DE0
		gadget = "8B41188B4058C1E81C83E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 1Ch
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74DF0(self):
		#sub_6DE74DF0
		gadget = "8B41148B8004010000C1E80783E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#shr     eax, 7
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74E00(self):
		#sub_6DE74E00
		gadget = "8B41148B800001000083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74E10(self):
		#sub_6DE74E10
		gadget = "8B41188B405CC1E80983E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+5Ch]
		#shr     eax, 9
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74E20(self):
		#sub_6DE74E20
		gadget = "8B41188B405CC1E80B83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+5Ch]
		#shr     eax, 0Bh
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74E30(self):
		#sub_6DE74E30
		gadget = "8B41148B8004010000C1E80883E007C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#shr     eax, 8
		#and     eax, 7
		#retn


  def test_gadget_sub_6DE74E40(self):
		#sub_6DE74E40
		gadget = "8B41148B8004010000C1E80B83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#shr     eax, 0Bh
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74E50(self):
		#sub_6DE74E50
		gadget = "8B41148B8000010000C1E80983E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 9
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74E60(self):
		#sub_6DE74E60
		gadget = "8B41148B8000010000C1E80A83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+100h]
		#shr     eax, 0Ah
		#and     eax, 1
		#retn


  def test_gadget_sub_6DE74E70(self):
		#sub_6DE74E70
		gadget = "8B4114D94010C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#fld     dword ptr [eax+10h]
		#retn


  def test_gadget_sub_6DE74F00(self):
		#sub_6DE74F00
		gadget = "8B41188B4058C1E80283E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+58h]
		#shr     eax, 2
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74F10(self):
		#sub_6DE74F10
		gadget = "8B41188B405CC1E80783E003C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+5Ch]
		#shr     eax, 7
		#and     eax, 3
		#retn


  def test_gadget_sub_6DE74F30(self):
		#sub_6DE74F30
		gadget = "8B41148B8004010000C1E80E83E01FC3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+104h]
		#shr     eax, 0Eh
		#and     eax, 1Fh
		#retn


  def test_gadget_sub_6DE74F40(self):
		#sub_6DE74F40
		gadget = "8B41048B403CC3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     eax, [eax+3Ch]
		#retn


  def test_gadget_sub_6DE74FF0(self):
		#sub_6DE74FF0
		gadget = "8B49108B51648A49688B44240480E1018910884804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+10h]
		#mov     edx, [ecx+64h]
		#mov     cl, [ecx+68h]
		#mov     eax, [esp+arg_0]
		#and     cl, 1
		#mov     [eax], edx
		#mov     [eax+4], cl
		#retn    4


  def test_gadget_sub_6DE75010(self):
		#sub_6DE75010
		gadget = "8B49108B516C8A49708B44240480E1018910884804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+10h]
		#mov     edx, [ecx+6Ch]
		#mov     cl, [ecx+70h]
		#mov     eax, [esp+arg_0]
		#and     cl, 1
		#mov     [eax], edx
		#mov     [eax+4], cl
		#retn    4


  def test_gadget_sub_6DE75030(self):
		#sub_6DE75030
		gadget = "8B49108B51748A49788B44240480E1018910884804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+10h]
		#mov     edx, [ecx+74h]
		#mov     cl, [ecx+78h]
		#mov     eax, [esp+arg_0]
		#and     cl, 1
		#mov     [eax], edx
		#mov     [eax+4], cl
		#retn    4


  def test_gadget_sub_6DE75050(self):
		#sub_6DE75050
		gadget = "8B49108B517C8A89800000008B44240480E1018910884804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+10h]
		#mov     edx, [ecx+7Ch]
		#mov     cl, [ecx+80h]
		#mov     eax, [esp+arg_0]
		#and     cl, 1
		#mov     [eax], edx
		#mov     [eax+4], cl
		#retn    4


  def test_gadget_sub_6DE75070(self):
		#sub_6DE75070
		gadget = "8B490C8B51348B4424048B49388910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+0Ch]
		#mov     edx, [ecx+34h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+38h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DE75090(self):
		#sub_6DE75090
		gadget = "8B41148B48388B51108A49148B44240480E1018910884804C20400"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+38h]
		#mov     edx, [ecx+10h]
		#mov     cl, [ecx+14h]
		#mov     eax, [esp+arg_0]
		#and     cl, 1
		#mov     [eax], edx
		#mov     [eax+4], cl
		#retn    4


  def test_gadget_sub_6DE750B0(self):
		#sub_6DE750B0
		gadget = "8B490C8B513C8A49408B44240480E1018910884804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+0Ch]
		#mov     edx, [ecx+3Ch]
		#mov     cl, [ecx+40h]
		#mov     eax, [esp+arg_0]
		#and     cl, 1
		#mov     [eax], edx
		#mov     [eax+4], cl
		#retn    4


  def test_gadget_sub_6DE750D0(self):
		#sub_6DE750D0
		gadget = "8B49188B511C8B4424048B49208910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+18h]
		#mov     edx, [ecx+1Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+20h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DE750F0(self):
		#sub_6DE750F0
		gadget = "8B49188B51148B4424048B49188910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+18h]
		#mov     edx, [ecx+14h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+18h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DE75110(self):
		#sub_6DE75110
		gadget = "8B49188B51088B4424048B490C8910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+18h]
		#mov     edx, [ecx+8]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_nullsub_5(self):
		#nullsub_5
		gadget = "C21000"
		self.do(gadget)

		#retn    10h


  def test_gadget_sub_6DE88BF0(self):
		#sub_6DE88BF0
		gadget = "8B442404C70000000000C7400400000000C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 0
		#retn    0Ch


  def test_gadget_sub_6DE89220(self):
		#sub_6DE89220
		gadget = "8B5424048BC18B480481E10040F8FFC7000100000081C9004000008948048A4C240889500888480C8B4C240C8B118950108B490489481433C989481888481C89482089482489482889482C894830C20C00"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#and     ecx, 0FFF84000h
		#mov     dword ptr [eax], 1
		#or      ecx, 4000h
		#mov     [eax+4], ecx
		#mov     cl, [esp+arg_4]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], cl
		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx]
		#mov     [eax+10h], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+14h], ecx
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cl
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#retn    0Ch


  def test_gadget_sub_6DE8A600(self):
		#sub_6DE8A600
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483C89484089484489484889484C89485089485489485889485C89486089486489486889486C89487089487489487889487C898880000000C680840000000189888800000089888C00000089889000000089889400000089889800000089889C0000008988A00000008988A40000008988A80000008988AC0000008988B00000008988B40000008988B80000008988BC0000008988C00000008988C40000008988C80000008988CC0000008988D00000008988D40000008988D8000000668988DC0000008988E00000008988E40000008988E8000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], ecx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+68h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], ecx
		#mov     [eax+74h], ecx
		#mov     [eax+78h], ecx
		#mov     [eax+7Ch], ecx
		#mov     [eax+80h], ecx
		#mov     byte ptr [eax+84h], 1
		#mov     [eax+88h], ecx
		#mov     [eax+8Ch], ecx
		#mov     [eax+90h], ecx
		#mov     [eax+94h], ecx
		#mov     [eax+98h], ecx
		#mov     [eax+9Ch], ecx
		#mov     [eax+0A0h], ecx
		#mov     [eax+0A4h], ecx
		#mov     [eax+0A8h], ecx
		#mov     [eax+0ACh], ecx
		#mov     [eax+0B0h], ecx
		#mov     [eax+0B4h], ecx
		#mov     [eax+0B8h], ecx
		#mov     [eax+0BCh], ecx
		#mov     [eax+0C0h], ecx
		#mov     [eax+0C4h], ecx
		#mov     [eax+0C8h], ecx
		#mov     [eax+0CCh], ecx
		#mov     [eax+0D0h], ecx
		#mov     [eax+0D4h], ecx
		#mov     [eax+0D8h], ecx
		#mov     [eax+0DCh], cx
		#mov     [eax+0E0h], ecx
		#mov     [eax+0E4h], ecx
		#mov     [eax+0E8h], ecx
		#retn


  def test_gadget_GetNumBorrowedCores(self):
		#GetNumBorrowedCoresSchedulerProxydetailsConcurrencyQBEIXZ
		gadget = "8B81A8000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0A8h]
		#retn


  def test_gadget_reserve_message2(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_2
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6DE90870(self):
		#sub_6DE90870
		gadget = "8B4424048B108951108B4004894114C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+10h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+14h], eax
		#retn    4


  def test_gadget_sub_6DE98F30(self):
		#sub_6DE98F30
		gadget = "8BC18B50048B4C240483E13FC70001000000C1E10D81E20000F8FF0BCA89480433C989480889480C89481089481489481889481C89482089482489482889482CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     edx, [eax+4]
		#mov     ecx, [esp+arg_0]
		#and     ecx, 3Fh
		#mov     dword ptr [eax], 1
		#shl     ecx, 0Dh
		#and     edx, 0FFF80000h
		#or      ecx, edx
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#retn    4


  def test_gadget_nullsub_1(self):
		#nullsub_1
		gadget = "C20400"
		self.do(gadget)

		#retn    4


  def test_gadget_sub_6DE9B6B0(self):
		#sub_6DE9B6B0
		gadget = "8B5424048BC18B480481E100A0FAFF81C900A00200C70001000000894804895008C20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#and     ecx, 0FFFAA000h
		#or      ecx, 2A000h
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], edx
		#retn    4


  def test_gadget_sub_6DE9E8D0(self):
		#sub_6DE9E8D0
		gadget = "8B81CC0800008981D4080000C3"
		self.do(gadget)

		#mov     eax, [ecx+8CCh]
		#mov     [ecx+8D4h], eax
		#retn


  def test_gadget_sub_6DE9E8E0(self):
		#sub_6DE9E8E0
		gadget = "8B4424048B89CC0800008B500403C983E2010BCA894804C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+8CCh]
		#mov     edx, [eax+4]
		#add     ecx, ecx
		#and     edx, 1
		#or      ecx, edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DE9F960(self):
		#sub_6DE9F960
		gadget = "8B8168080000898170080000C3"
		self.do(gadget)

		#mov     eax, [ecx+868h]
		#mov     [ecx+870h], eax
		#retn


  def test_gadget_sub_6DEC7B90(self):
		#sub_6DEC7B90
		gadget = "8B442410C70007000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_C]
		#mov     dword ptr [eax], 7
		#retn    10h


  def test_gadget_sub_6DEC7EE0(self):
		#sub_6DEC7EE0
		gadget = "8B5424048BC18B480481E15400F8FF83C954C70001000000894804895008C20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#and     ecx, 0FFF80054h
		#or      ecx, 54h
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], edx
		#retn    4


  def test_gadget_sub_6DEC7F10(self):
		#sub_6DEC7F10
		gadget = "DD4424048BC18B4C240CDD58088B500483E17F03C903C981E20000F8FF0BCAC70001000000894804C20C00"
		self.do(gadget)

		#fld     [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_8]
		#fstp    qword ptr [eax+8]
		#mov     edx, [eax+4]
		#and     ecx, 7Fh
		#add     ecx, ecx
		#add     ecx, ecx
		#and     edx, 0FFF80000h
		#or      ecx, edx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#retn    0Ch


  def test_gadget_sub_6DEC8A70(self):
		#sub_6DEC8A70
		gadget = "8B41048B5424042593FDFFFF0D90010000894104895108C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     edx, [esp+arg_0]
		#and     eax, 0FFFFFD93h
		#or      eax, 190h
		#mov     [ecx+4], eax
		#mov     [ecx+8], edx
		#retn    4


  def test_gadget_sub_6DEC8A90(self):
		#sub_6DEC8A90
		gadget = "8B41048B54240425BFFDFFFF0DBC010000894104895108C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     edx, [esp+arg_0]
		#and     eax, 0FFFFFDBFh
		#or      eax, 1BCh
		#mov     [ecx+4], eax
		#mov     [ecx+8], edx
		#retn    4


  def test_gadget_sub_6DEC9760(self):
		#sub_6DEC9760
		gadget = "8B41048B54240425C7FDFFFF0DC4010000894104895108C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     edx, [esp+arg_0]
		#and     eax, 0FFFFFDC7h
		#or      eax, 1C4h
		#mov     [ecx+4], eax
		#mov     [ecx+8], edx
		#retn    4


  def test_gadget_sub_6DECAEF0(self):
		#sub_6DECAEF0
		gadget = "8B41048B542404255FFCFFFF83C85C894104895108C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     edx, [esp+arg_0]
		#and     eax, 0FFFFFC5Fh
		#or      eax, 5Ch
		#mov     [ecx+4], eax
		#mov     [ecx+8], edx
		#retn    4


  def test_gadget_sub_6DECB2D0(self):
		#sub_6DECB2D0
		gadget = "8B41048B5424042563FCFFFF83C860894104895108C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     edx, [esp+arg_0]
		#and     eax, 0FFFFFC63h
		#or      eax, 60h
		#mov     [ecx+4], eax
		#mov     [ecx+8], edx
		#retn    4


  def test_gadget_sub_6DECB2F0(self):
		#sub_6DECB2F0
		gadget = "8B41048B54240425C3FDFFFF0DC0010000894104895108C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     edx, [esp+arg_0]
		#and     eax, 0FFFFFDC3h
		#or      eax, 1C0h
		#mov     [ecx+4], eax
		#mov     [ecx+8], edx
		#retn    4


  def test_gadget_ReaderWriterLockdetailsConcurrencyQAEXZ(self):
		#0_ReaderWriterLockdetailsConcurrencyQAEXZ
		gadget = "8BC1C70000000000C7400400000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_6DECE600(self):
		#sub_6DECE600
		gadget = "8B5424088BC18B4C24048908895004C20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#retn    8


  def test_gadget_sub_6DECE620(self):
		#sub_6DECE620
		gadget = "8B41042B01C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#sub     eax, [ecx]
		#retn


  def test_gadget_sub_6DECF550(self):
		#sub_6DECF550
		gadget = "8BC1C700D40D856EC3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_6E850DD4
		#retn


  def test_gadget_sub_6DECF560(self):
		#sub_6DECF560
		gadget = "C701D40D856EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E850DD4
		#retn


  def test_gadget_sub_6DECF590(self):
		#sub_6DECF590
		gadget = "8BC133C9C700F00D856E89480489480889480CC7401001000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E850DF0
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     dword ptr [eax+10h], 1
		#retn


  def test_gadget_sub_6DED5830(self):
		#sub_6DED5830
		gadget = "8BC18B4C2404894804C7000100000033C989480889480C8948108948148948188D502489501CC7402001000000894828C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#mov     dword ptr [eax], 1
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#lea     edx, [eax+24h]
		#mov     [eax+1Ch], edx
		#mov     dword ptr [eax+20h], 1
		#mov     [eax+28h], ecx
		#retn    4


  def test_gadget_sub_6DED7410(self):
		#sub_6DED7410
		gadget = "8B4118C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#retn


  def test_gadget_sub_6DED7420(self):
		#sub_6DED7420
		gadget = "8A410DC3"
		self.do(gadget)

		#mov     al, [ecx+0Dh]
		#retn


  def test_gadget_sub_6DED9040(self):
		#sub_6DED9040
		gadget = "8BC133C98908668948048848068948086689480C88480E894810668948148848168948186689481C88481EC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], cx
		#mov     [eax+6], cl
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cx
		#mov     [eax+0Eh], cl
		#mov     [eax+10h], ecx
		#mov     [eax+14h], cx
		#mov     [eax+16h], cl
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cx
		#mov     [eax+1Eh], cl
		#retn


  def test_gadget_sub_6DED9070(self):
		#sub_6DED9070
		gadget = "8B4C240433C03941080F94C0C20400"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#xor     eax, eax
		#cmp     [ecx+8], eax
		#setz    al
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_6(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_6
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_5(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_5
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6DED9270(self):
		#sub_6DED9270
		gadget = "518B44240833C9890866894804884806890C248948086689480C88480E59C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], cx
		#mov     [eax+6], cl
		#mov     [esp+4+var_4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cx
		#mov     [eax+0Eh], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6DED9290(self):
		#sub_6DED9290
		gadget = "518B442408D9EE33C9D918890C2466C740040002C640060159C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#fldz
		#xor     ecx, ecx
		#fstp    dword ptr [eax]
		#mov     [esp+4+var_4], ecx
		#mov     word ptr [eax+4], 200h
		#mov     byte ptr [eax+6], 1
		#pop     ecx
		#retn


  def test_gadget_sub_6DEDD670(self):
		#sub_6DEDD670
		gadget = "8BC18B50048B4C240483E13F81E20000F8FFC1E10D0BCA8B542408894804C700010000008D4810C1E20B894808C7400C04000000C740200000000033500481E200180000315004C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     edx, [eax+4]
		#mov     ecx, [esp+arg_0]
		#and     ecx, 3Fh
		#and     edx, 0FFF80000h
		#shl     ecx, 0Dh
		#or      ecx, edx
		#mov     edx, [esp+arg_4]
		#mov     [eax+4], ecx
		#mov     dword ptr [eax], 1
		#lea     ecx, [eax+10h]
		#shl     edx, 0Bh
		#mov     [eax+8], ecx
		#mov     dword ptr [eax+0Ch], 4
		#mov     dword ptr [eax+20h], 0
		#xor     edx, [eax+4]
		#and     edx, 1800h
		#xor     [eax+4], edx
		#retn    8


  def test_gadget_sub_6DEDD6C0(self):
		#sub_6DEDD6C0
		gadget = "8BC18B480481E10040FBFF81C9004003008948048B4C2404C700010000008D5010C1E10B895008C7400C04000000C740200000000033480481E100180000314804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#and     ecx, 0FFFB4000h
		#or      ecx, 34000h
		#mov     [eax+4], ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#lea     edx, [eax+10h]
		#shl     ecx, 0Bh
		#mov     [eax+8], edx
		#mov     dword ptr [eax+0Ch], 4
		#mov     dword ptr [eax+20h], 0
		#xor     ecx, [eax+4]
		#and     ecx, 1800h
		#xor     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DEDFD00(self):
		#sub_6DEDFD00
		gadget = "518B44240833C9890C24890866C74004000F88480659C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     word ptr [eax+4], 0F00h
		#mov     [eax+6], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6DEDFD20(self):
		#sub_6DEDFD20
		gadget = "518B44240833C9890C2489086689480488480659C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     [eax+4], cx
		#mov     [eax+6], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6DEDFD40(self):
		#sub_6DEDFD40
		gadget = "518B44240833C9890C24890866C74004000388480659C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     word ptr [eax+4], 300h
		#mov     [eax+6], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6DEDFD60(self):
		#sub_6DEDFD60
		gadget = "518B442408D905DC12856E33C9D918890C2466C740040002C640060159C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#fld     ds:flt_6E8512DC
		#xor     ecx, ecx
		#fstp    dword ptr [eax]
		#mov     [esp+4+var_4], ecx
		#mov     word ptr [eax+4], 200h
		#mov     byte ptr [eax+6], 1
		#pop     ecx
		#retn


  def test_gadget_sub_6DEDFD80(self):
		#sub_6DEDFD80
		gadget = "518B44240833C9890C24C7000600000066C74004000388480659C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     dword ptr [eax], 6
		#mov     word ptr [eax+4], 300h
		#mov     [eax+6], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6DEDFDA0(self):
		#sub_6DEDFDA0
		gadget = "518B442408D905E012856E33C9D918890C2466C740040002C640060159C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#fld     ds:flt_6E8512E0
		#xor     ecx, ecx
		#fstp    dword ptr [eax]
		#mov     [esp+4+var_4], ecx
		#mov     word ptr [eax+4], 200h
		#mov     byte ptr [eax+6], 1
		#pop     ecx
		#retn


  def test_gadget_sub_6DF07970(self):
		#sub_6DF07970
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483C89484089484489484889484C8948508948548948586689485C894860894864C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], cx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#retn


  def test_gadget_sub_6DF07FF0(self):
		#sub_6DF07FF0
		gadget = "8D4148C3"
		self.do(gadget)

		#lea     eax, [ecx+48h]
		#retn


  def test_gadget_sub_6DF08000(self):
		#sub_6DF08000
		gadget = "8D413CC3"
		self.do(gadget)

		#lea     eax, [ecx+3Ch]
		#retn


  def test_gadget_sub_6DF0A820(self):
		#sub_6DF0A820
		gadget = "8B442404DB00DC0D10E1846ED95C2404D9442404D84C2408D95C2404D9442404C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#fmul    [esp+arg_4]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn


  def test_gadget_sub_6DF0BE90(self):
		#sub_6DF0BE90
		gadget = "8BC133C9C7000100000089480489480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_6DF111F0(self):
		#sub_6DF111F0
		gadget = "8BC18B4C240489480433C9C7000100000089480889480C894810C7401401000000C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     dword ptr [eax+14h], 1
		#retn    4


  def test_gadget_sub_6DF123F0(self):
		#sub_6DF123F0
		gadget = "8B4108FF00C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#inc     dword ptr [eax]
		#retn


  def test_gadget_sub_6DF12440(self):
		#sub_6DF12440
		gadget = "FF4110C3"
		self.do(gadget)

		#inc     dword ptr [ecx+10h]
		#retn


  def test_gadget_sub_6DF12510(self):
		#sub_6DF12510
		gadget = "8B41088B4030C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     eax, [eax+30h]
		#retn


  def test_gadget_sub_6DF130E0(self):
		#sub_6DF130E0
		gadget = "8B5424048BC133C989480489500889480C8B4C24088948148B4808C700A417856EC7401001000000FF01C20800"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+14h], ecx
		#mov     ecx, [eax+8]
		#mov     dword ptr [eax], offset off_6E8517A4
		#mov     dword ptr [eax+10h], 1
		#inc     dword ptr [ecx]
		#retn    8


  def test_gadget_sub_6DF15620(self):
		#sub_6DF15620
		gadget = "8BC18B4C240483B9A4020000000F95C288108A89FC0400008B54240880E101884801895004C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#cmp     dword ptr [ecx+2A4h], 0
		#setnz   dl
		#mov     [eax], dl
		#mov     cl, [ecx+4FCh]
		#mov     edx, [esp+arg_4]
		#and     cl, 1
		#mov     [eax+1], cl
		#mov     [eax+4], edx
		#retn    8


  def test_gadget_sub_6DF18B50(self):
		#sub_6DF18B50
		gadget = "6AFF684804756E64A10000000050A1F44AA66E33C4508D44240464A3000000008BC18B48048B54241481E10060FAFF81C9006002008948048B4C2418C700010000008950088B54241C89480C8B4C24208950108B5424248948148B4C242889501889481C8B4C240464890D000000005983C40CC21800"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E750448
		#mov     eax, large fs:0
		#push    eax
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+10h+var_C]
		#mov     large fs:0, eax
		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#mov     edx, [esp+10h+arg_0]
		#and     ecx, 0FFFA6000h
		#or      ecx, 26000h
		#mov     [eax+4], ecx
		#mov     ecx, [esp+10h+arg_4]
		#mov     dword ptr [eax], 1
		#mov     [eax+8], edx
		#mov     edx, [esp+10h+arg_8]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+10h+arg_C]
		#mov     [eax+10h], edx
		#mov     edx, [esp+10h+arg_10]
		#mov     [eax+14h], ecx
		#mov     ecx, [esp+10h+arg_14]
		#mov     [eax+18h], edx
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+10h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 0Ch
		#retn    18h


  def test_gadget_sub_6DF19540(self):
		#sub_6DF19540
		gadget = "B828000000C3"
		self.do(gadget)

		#mov     eax, 28h
		#retn


  def test_gadget_sub_6DF1E190(self):
		#sub_6DF1E190
		gadget = "C7411000000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+10h], 0
		#retn


  def test_gadget_sub_6DF22F90(self):
		#sub_6DF22F90
		gadget = "33C0837908060F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx+8], 6
		#setz    al
		#retn


  def test_gadget_sub_6DF24270(self):
		#sub_6DF24270
		gadget = "518B442408C7042400000000C7000000000059C21400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    14h


  def test_gadget_sub_6DF28350(self):
		#sub_6DF28350
		gadget = "8BC18D4808890833C9898808020000BA4000000089500489881403000089901002000083C9FF568DB01402000089B00C02000089881803000089881C03000089882003000089882403000089882803000089882C030000C68030030000015EC3"
		self.do(gadget)

		#mov     eax, ecx
		#lea     ecx, [eax+8]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+208h], ecx
		#mov     edx, 40h
		#mov     [eax+4], edx
		#mov     [eax+314h], ecx
		#mov     [eax+210h], edx
		#or      ecx, 0FFFFFFFFh
		#push    esi
		#lea     esi, [eax+214h]
		#mov     [eax+20Ch], esi
		#mov     [eax+318h], ecx
		#mov     [eax+31Ch], ecx
		#mov     [eax+320h], ecx
		#mov     [eax+324h], ecx
		#mov     [eax+328h], ecx
		#mov     [eax+32Ch], ecx
		#mov     byte ptr [eax+330h], 1
		#pop     esi
		#retn


  def test_gadget_sub_6DF2F630(self):
		#sub_6DF2F630
		gadget = "518B44240833D2891089500489500883C9FF89480C89481089481489481889481C89482089502489142489502859C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     edx, edx
		#mov     [eax], edx
		#mov     [eax+4], edx
		#mov     [eax+8], edx
		#or      ecx, 0FFFFFFFFh
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], edx
		#mov     [esp+4+var_4], edx
		#mov     [eax+28h], edx
		#pop     ecx
		#retn


  def test_gadget_sub_6DF32620(self):
		#sub_6DF32620
		gadget = "8BC18B4C2404C1E10583C90189480433C9C7000100000089480889480CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#shl     ecx, 5
		#or      ecx, 1
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6DF32790(self):
		#sub_6DF32790
		gadget = "8BC133C9C70001000000C740040600000089480889480CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     dword ptr [eax+4], 6
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn


  def test_gadget_sub_6DF32890(self):
		#sub_6DF32890
		gadget = "8BC1C70001000000C7400405000000C7400800000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#mov     dword ptr [eax+4], 5
		#mov     dword ptr [eax+8], 0
		#retn


  def test_gadget_sub_6DF32A30(self):
		#sub_6DF32A30
		gadget = "8BC1C70001000000C740040400000033C989480889480C8948108B4C24088B5010568B71088970108951088B318B500889700889118B71048B500C89700C8951048B4C24088948145EC20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#mov     dword ptr [eax+4], 4
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     edx, [eax+10h]
		#push    esi
		#mov     esi, [ecx+8]
		#mov     [eax+10h], esi
		#mov     [ecx+8], edx
		#mov     esi, [ecx]
		#mov     edx, [eax+8]
		#mov     [eax+8], esi
		#mov     [ecx], edx
		#mov     esi, [ecx+4]
		#mov     edx, [eax+0Ch]
		#mov     [eax+0Ch], esi
		#mov     [ecx+4], edx
		#mov     ecx, [esp+4+arg_0]
		#mov     [eax+14h], ecx
		#pop     esi
		#retn    8


  def test_gadget_sub_6DF340B0(self):
		#sub_6DF340B0
		gadget = "C701DC11856EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E8511DC
		#retn


  def test_gadget_sub_6DF341C0(self):
		#sub_6DF341C0
		gadget = "80493C40C3"
		self.do(gadget)

		#or      byte ptr [ecx+3Ch], 40h
		#retn


  def test_gadget_sub_6DF341D0(self):
		#sub_6DF341D0
		gadget = "80613CBFC3"
		self.do(gadget)

		#and     byte ptr [ecx+3Ch], 0BFh
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6DF342F0(self):
		#sub_6DF342F0
		gadget = "33C039410C0F95C0034124034118C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+0Ch], eax
		#setnz   al
		#add     eax, [ecx+24h]
		#add     eax, [ecx+18h]
		#retn


  def test_gadget_sub_6DF35ED0(self):
		#sub_6DF35ED0
		gadget = "8BC18B4C240489480433C9C7000100000089480889480C894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6DF36140(self):
		#sub_6DF36140
		gadget = "DD4424048BC1DD18DD44240CDD5808DD442414DD5810DD44241CDD5818DD442424DD5820DD44242CDD5828DD442434DD5830DD44243CDD5838DD442444DD5840DD44244CDD5848DD442454DD5850DD44245CDD5858DD442464DD5860DD44246CDD5868DD442474DD5870DD44247CDD5878C28000"
		self.do(gadget)

		#fld     [esp+arg_0]
		#mov     eax, ecx
		#fstp    qword ptr [eax]
		#fld     [esp+arg_8]
		#fstp    qword ptr [eax+8]
		#fld     [esp+arg_10]
		#fstp    qword ptr [eax+10h]
		#fld     [esp+arg_18]
		#fstp    qword ptr [eax+18h]
		#fld     [esp+arg_20]
		#fstp    qword ptr [eax+20h]
		#fld     [esp+arg_28]
		#fstp    qword ptr [eax+28h]
		#fld     [esp+arg_30]
		#fstp    qword ptr [eax+30h]
		#fld     [esp+arg_38]
		#fstp    qword ptr [eax+38h]
		#fld     [esp+arg_40]
		#fstp    qword ptr [eax+40h]
		#fld     [esp+arg_48]
		#fstp    qword ptr [eax+48h]
		#fld     [esp+arg_50]
		#fstp    qword ptr [eax+50h]
		#fld     [esp+arg_58]
		#fstp    qword ptr [eax+58h]
		#fld     [esp+arg_60]
		#fstp    qword ptr [eax+60h]
		#fld     [esp+arg_68]
		#fstp    qword ptr [eax+68h]
		#fld     [esp+arg_70]
		#fstp    qword ptr [eax+70h]
		#fld     [esp+arg_78]
		#fstp    qword ptr [eax+78h]
		#retn    80h


  def test_gadget_sub_6DF36420(self):
		#sub_6DF36420
		gadget = "B813000000C3"
		self.do(gadget)

		#mov     eax, 13h
		#retn


  def test_gadget_sub_6DF387F0(self):
		#sub_6DF387F0
		gadget = "8BC133C9C70001000000894804894808C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#retn


  def test_gadget_sub_6DF390D0(self):
		#sub_6DF390D0
		gadget = "8B4104FF4004C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#inc     dword ptr [eax+4]
		#retn


  def test_gadget_sub_6DF39100(self):
		#sub_6DF39100
		gadget = "8B41108B4010C3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#mov     eax, [eax+10h]
		#retn


  def test_gadget_sub_6DF39110(self):
		#sub_6DF39110
		gadget = "8B41048B48108B4110C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     ecx, [eax+10h]
		#mov     eax, [ecx+10h]
		#retn


  def test_gadget_sub_6DF39C50(self):
		#sub_6DF39C50
		gadget = "8BC133C9C70001000000C740040700000089480889480C894810894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     dword ptr [eax+4], 7
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_6DF3AC80(self):
		#sub_6DF3AC80
		gadget = "B810000000C3"
		self.do(gadget)

		#mov     eax, 10h
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_0(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_0
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6DF3BB80(self):
		#sub_6DF3BB80
		gadget = "8B413083C00CC3"
		self.do(gadget)

		#mov     eax, [ecx+30h]
		#add     eax, 0Ch
		#retn


  def test_gadget_sub_6DF3BB90(self):
		#sub_6DF3BB90
		gadget = "8B413083C010C3"
		self.do(gadget)

		#mov     eax, [ecx+30h]
		#add     eax, 10h
		#retn


  def test_gadget_sub_6DF3BBA0(self):
		#sub_6DF3BBA0
		gadget = "8B413083C008C3"
		self.do(gadget)

		#mov     eax, [ecx+30h]
		#add     eax, 8
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_7(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_7
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_8(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_8
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DF3F680(self):
		#sub_6DF3F680
		gadget = "8BC18B4C2404C70000000000C74004010000008B118950088B510489500C8B51088950108B490C894814C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 1
		#mov     edx, [ecx]
		#mov     [eax+8], edx
		#mov     edx, [ecx+4]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+8]
		#mov     [eax+10h], edx
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+14h], ecx
		#retn    4


  def test_gadget_sub_6DF3F6B0(self):
		#sub_6DF3F6B0
		gadget = "D9EE8BC1C70000000000C7400401000000D95008D9500CD95010D95814C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 1
		#fst     dword ptr [eax+8]
		#fst     dword ptr [eax+0Ch]
		#fst     dword ptr [eax+10h]
		#fstp    dword ptr [eax+14h]
		#retn


  def test_gadget_sub_6DF3FA80(self):
		#sub_6DF3FA80
		gadget = "8B442404894108C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+8], eax
		#retn    4


  def test_gadget_sub_6DF40620(self):
		#sub_6DF40620
		gadget = "B808000000C3"
		self.do(gadget)

		#mov     eax, 8
		#retn


  def test_gadget_sub_6DF46320(self):
		#sub_6DF46320
		gadget = "8A44240CC20C00"
		self.do(gadget)

		#mov     al, [esp+arg_8]
		#retn    0Ch


  def test_gadget_sub_6DF46440(self):
		#sub_6DF46440
		gadget = "C7410800000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+8], 0
		#retn


  def test_gadget_1_StackGuarddetailsConcurrencyQAEXZ(self):
		#1_StackGuarddetailsConcurrencyQAEXZ
		gadget = "8B01FF08C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#dec     dword ptr [eax]
		#retn


  def test_gadget_sub_6DF46F30(self):
		#sub_6DF46F30
		gadget = "A01464A66EC3"
		self.do(gadget)

		#mov     al, byte_6EA66414
		#retn


  def test_gadget_sub_6DF46F40(self):
		#sub_6DF46F40
		gadget = "A01564A66EC3"
		self.do(gadget)

		#mov     al, byte_6EA66415
		#retn


  def test_gadget_sub_6DF47060(self):
		#sub_6DF47060
		gadget = "8D8114010000C3"
		self.do(gadget)

		#lea     eax, [ecx+114h]
		#retn


  def test_gadget_sub_6DF47140(self):
		#sub_6DF47140
		gadget = "33C0C20800"
		self.do(gadget)

		#xor     eax, eax
		#retn    8


  def test_gadget_sub_6DF473B0(self):
		#sub_6DF473B0
		gadget = "8A8194040000C3"
		self.do(gadget)

		#mov     al, [ecx+494h]
		#retn


  def test_gadget_sub_6DF47420(self):
		#sub_6DF47420
		gadget = "8A81A0050000C3"
		self.do(gadget)

		#mov     al, [ecx+5A0h]
		#retn


  def test_gadget_sub_6DF479E0(self):
		#sub_6DF479E0
		gadget = "8B81FC000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0FCh]
		#retn


  def test_gadget_sub_6DF47CF0(self):
		#sub_6DF47CF0
		gadget = "8B817C040000C3"
		self.do(gadget)

		#mov     eax, [ecx+47Ch]
		#retn


  def test_gadget_sub_6DF59050(self):
		#sub_6DF59050
		gadget = "8B81AC040000C3"
		self.do(gadget)

		#mov     eax, [ecx+4ACh]
		#retn


  def test_gadget_sub_6DF59060(self):
		#sub_6DF59060
		gadget = "FF41B0C3"
		self.do(gadget)

		#inc     dword ptr [ecx-50h]
		#retn


  def test_gadget_sub_6DF5F2E0(self):
		#sub_6DF5F2E0
		gadget = "B80B000000C3"
		self.do(gadget)

		#mov     eax, 0Bh
		#retn


  def test_gadget_sub_6DF60F30(self):
		#sub_6DF60F30
		gadget = "8BC133C9890889480489480889480C894810894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_6DF62630(self):
		#sub_6DF62630
		gadget = "8B442404014104014108C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     [ecx+4], eax
		#add     [ecx+8], eax
		#retn    4


  def test_gadget_sub_6DF62680(self):
		#sub_6DF62680
		gadget = "C701A035856EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E8535A0
		#retn


  def test_gadget_sub_6DF62950(self):
		#sub_6DF62950
		gadget = "8B5424088BC18B4C240489088B4C240C895004894808C7400C00000000C20C00"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#mov     dword ptr [eax+0Ch], 0
		#retn    0Ch


  def test_gadget_sub_6DF62D00(self):
		#sub_6DF62D00
		gadget = "518B44240833C98908894804890C2489480889480C89481059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6DF63900(self):
		#sub_6DF63900
		gadget = "C7410801000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+8], 1
		#retn


  def test_gadget_sub_6DF63910(self):
		#sub_6DF63910
		gadget = "C7410802000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+8], 2
		#retn


  def test_gadget_sub_6DF63920(self):
		#sub_6DF63920
		gadget = "C7410803000000C7411000000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+8], 3
		#mov     dword ptr [ecx+10h], 0
		#retn


  def test_gadget_sub_6DF63930(self):
		#sub_6DF63930
		gadget = "8BC1C740040100000033C989480888480C8B4C2404C700D435856E894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], 1
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cl
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8535D4
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6DF63960(self):
		#sub_6DF63960
		gadget = "C701D435856EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E8535D4
		#retn


  def test_gadget_sub_6DF66470(self):
		#sub_6DF66470
		gadget = "B80A000000C3"
		self.do(gadget)

		#mov     eax, 0Ah
		#retn


  def test_gadget_sub_6DF66950(self):
		#sub_6DF66950
		gadget = "8A4104C3"
		self.do(gadget)

		#mov     al, [ecx+4]
		#retn


  def test_gadget_0facetlocalestdIAEIZ_0(self):
		#0facetlocalestdIAEIZ_0
		gadget = "8BC18B4C2404C70000000000894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6DF69770(self):
		#sub_6DF69770
		gadget = "8BC1C7400400000000C7009C42856EC3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], 0
		#mov     dword ptr [eax], offset off_6E85429C
		#retn


  def test_gadget_sub_6DF697B0(self):
		#sub_6DF697B0
		gadget = "8B44240483C09F66B91900663BC81BC040C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 0FFFFFF9Fh
		#mov     cx, 19h
		#cmp     cx, ax
		#sbb     eax, eax
		#inc     eax
		#retn


  def test_gadget_sub_6DF69830(self):
		#sub_6DF69830
		gadget = "8B4108FF4008C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#inc     dword ptr [eax+8]
		#retn


  def test_gadget_sub_6DF6A390(self):
		#sub_6DF6A390
		gadget = "8B442404DB00DC0D10E1846ED95C2404D9442404D8742408D95C2404D9442404C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#fdiv    [esp+arg_4]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn


  def test_gadget_sub_6DF6A7F0(self):
		#sub_6DF6A7F0
		gadget = "518B5424088BC18B0A89088B4A04894804D94204D95C2408D94208D802D95808D9442408D9580CD94204D91C24D9420CD95C2408D94208D802D95810D9442408D80424D95814D94204D91C24D9420CD95C2408D902D95818D9442408D80424D9581C59C20400"
		self.do(gadget)

		#push    ecx
		#mov     edx, [esp+4+arg_0]
		#mov     eax, ecx
		#mov     ecx, [edx]
		#mov     [eax], ecx
		#mov     ecx, [edx+4]
		#mov     [eax+4], ecx
		#fld     dword ptr [edx+4]
		#fstp    [esp+4+arg_0]
		#fld     dword ptr [edx+8]
		#fadd    dword ptr [edx]
		#fstp    dword ptr [eax+8]
		#fld     [esp+4+arg_0]
		#fstp    dword ptr [eax+0Ch]
		#fld     dword ptr [edx+4]
		#fstp    [esp+4+var_4]
		#fld     dword ptr [edx+0Ch]
		#fstp    [esp+4+arg_0]
		#fld     dword ptr [edx+8]
		#fadd    dword ptr [edx]
		#fstp    dword ptr [eax+10h]
		#fld     [esp+4+arg_0]
		#fadd    [esp+4+var_4]
		#fstp    dword ptr [eax+14h]
		#fld     dword ptr [edx+4]
		#fstp    [esp+4+var_4]
		#fld     dword ptr [edx+0Ch]
		#fstp    [esp+4+arg_0]
		#fld     dword ptr [edx]
		#fstp    dword ptr [eax+18h]
		#fld     [esp+4+arg_0]
		#fadd    [esp+4+var_4]
		#fstp    dword ptr [eax+1Ch]
		#pop     ecx
		#retn    4


  def test_gadget_sub_6DF6AE40(self):
		#sub_6DF6AE40
		gadget = "8B4424048B48108B513083E21F33C080FA160F95C0C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+10h]
		#mov     edx, [ecx+30h]
		#and     edx, 1Fh
		#xor     eax, eax
		#cmp     dl, 16h
		#setnz   al
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_9(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_9
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_2(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_2
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6DF76240(self):
		#sub_6DF76240
		gadget = "8B018B400CC1E8072401C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     eax, [eax+0Ch]
		#shr     eax, 7
		#and     al, 1
		#retn


  def test_gadget_sub_6DF76250(self):
		#sub_6DF76250
		gadget = "8B018B400C2500800100F7D81BC0F7D8C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     eax, [eax+0Ch]
		#and     eax, 18000h
		#neg     eax
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_6DF76AA0(self):
		#sub_6DF76AA0
		gadget = "8BC166C7000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     word ptr [eax], 0
		#retn


  def test_gadget_sub_6DF771B0(self):
		#sub_6DF771B0
		gadget = "6AFF688091756E64A10000000050A1F44AA66E33C4508D44240464A3000000008BC18B4C24148B542418C7009C44856E8948048B4C241C89500889480C8B4C240464890D000000005983C40CC20C00"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E759180
		#mov     eax, large fs:0
		#push    eax
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+10h+var_C]
		#mov     large fs:0, eax
		#mov     eax, ecx
		#mov     ecx, [esp+10h+arg_0]
		#mov     edx, [esp+10h+arg_4]
		#mov     dword ptr [eax], offset off_6E85449C
		#mov     [eax+4], ecx
		#mov     ecx, [esp+10h+arg_8]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+10h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 0Ch
		#retn    0Ch


  def test_gadget_sub_6DF772A0(self):
		#sub_6DF772A0
		gadget = "6AFF681092756E64A1000000005083EC0CA1F44AA66E33C4508D44241064A3000000008BC18B4C24208B5424248948048B4C242889500889480CC700B044856EC74010000000008B4C241064890D000000005983C418C20C00"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E759210
		#mov     eax, large fs:0
		#push    eax
		#sub     esp, 0Ch
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+1Ch+var_C]
		#mov     large fs:0, eax
		#mov     eax, ecx
		#mov     ecx, [esp+1Ch+arg_0]
		#mov     edx, [esp+1Ch+arg_4]
		#mov     [eax+4], ecx
		#mov     ecx, [esp+1Ch+arg_8]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     dword ptr [eax], offset off_6E8544B0
		#mov     dword ptr [eax+10h], 0
		#mov     ecx, [esp+1Ch+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 18h
		#retn    0Ch


  def test_gadget_sub_6DF773B0(self):
		#sub_6DF773B0
		gadget = "8BC18B4C2404C7400401000000C700C444856E894808C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     dword ptr [eax], offset off_6E8544C4
		#mov     [eax+8], ecx
		#retn    4


  def test_gadget_sub_6DF79850(self):
		#sub_6DF79850
		gadget = "8BC18D48088908C7400402000000C7401800000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#lea     ecx, [eax+8]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 2
		#mov     dword ptr [eax+18h], 0
		#retn


  def test_gadget_sub_6DF7C860(self):
		#sub_6DF7C860
		gadget = "8BC18B4C24048908894804C6400800C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     byte ptr [eax+8], 0
		#retn    4


  def test_gadget_sub_6DF7D6C0(self):
		#sub_6DF7D6C0
		gadget = "C70110E8826EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E82E810
		#retn


  def test_gadget_sub_6DF7FF20(self):
		#sub_6DF7FF20
		gadget = "837910000F95C0C3"
		self.do(gadget)

		#cmp     dword ptr [ecx+10h], 0
		#setnz   al
		#retn


  def test_gadget_sub_6DF82680(self):
		#sub_6DF82680
		gadget = "8D4114C3"
		self.do(gadget)

		#lea     eax, [ecx+14h]
		#retn


  def test_gadget_sub_6DF84EB0(self):
		#sub_6DF84EB0
		gadget = "C6417900C3"
		self.do(gadget)

		#mov     byte ptr [ecx+79h], 0
		#retn


  def test_gadget_sub_6DF84EC0(self):
		#sub_6DF84EC0
		gadget = "8B41589983E23F03C2C1F806C3"
		self.do(gadget)

		#mov     eax, [ecx+58h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn


  def test_gadget_sub_6DF84ED0(self):
		#sub_6DF84ED0
		gadget = "8B415C9983E23F03C2C1F806C3"
		self.do(gadget)

		#mov     eax, [ecx+5Ch]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn


  def test_gadget_sub_6DF84EE0(self):
		#sub_6DF84EE0
		gadget = "8B41509983E23F03C2C1F806C3"
		self.do(gadget)

		#mov     eax, [ecx+50h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn


  def test_gadget_sub_6DF84EF0(self):
		#sub_6DF84EF0
		gadget = "8B41549983E23F03C2C1F806C3"
		self.do(gadget)

		#mov     eax, [ecx+54h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn


  def test_gadget_sub_6DF85E80(self):
		#sub_6DF85E80
		gadget = "518B44240833D28910895004895008568B71108970088951108B7108895424048B1089308951088B710C8B500489700489510C5E59C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     edx, edx
		#mov     [eax], edx
		#mov     [eax+4], edx
		#mov     [eax+8], edx
		#push    esi
		#mov     esi, [ecx+10h]
		#mov     [eax+8], esi
		#mov     [ecx+10h], edx
		#mov     esi, [ecx+8]
		#mov     [esp+8+var_4], edx
		#mov     edx, [eax]
		#mov     [eax], esi
		#mov     [ecx+8], edx
		#mov     esi, [ecx+0Ch]
		#mov     edx, [eax+4]
		#mov     [eax+4], esi
		#mov     [ecx+0Ch], edx
		#pop     esi
		#pop     ecx
		#retn    4


  def test_gadget_sub_6DF878D0(self):
		#sub_6DF878D0
		gadget = "8BC18A4C24088848148B4C240433D2891089500489500889500C895010568B3189308B710489118B50048970048B71088951048B50088970088B710C8951088B500C89700C8B711089510C8B50108970108951105EC20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     cl, [esp+arg_4]
		#mov     [eax+14h], cl
		#mov     ecx, [esp+arg_0]
		#xor     edx, edx
		#mov     [eax], edx
		#mov     [eax+4], edx
		#mov     [eax+8], edx
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], edx
		#push    esi
		#mov     esi, [ecx]
		#mov     [eax], esi
		#mov     esi, [ecx+4]
		#mov     [ecx], edx
		#mov     edx, [eax+4]
		#mov     [eax+4], esi
		#mov     esi, [ecx+8]
		#mov     [ecx+4], edx
		#mov     edx, [eax+8]
		#mov     [eax+8], esi
		#mov     esi, [ecx+0Ch]
		#mov     [ecx+8], edx
		#mov     edx, [eax+0Ch]
		#mov     [eax+0Ch], esi
		#mov     esi, [ecx+10h]
		#mov     [ecx+0Ch], edx
		#mov     edx, [eax+10h]
		#mov     [eax+10h], esi
		#mov     [ecx+10h], edx
		#pop     esi
		#retn    8


  def test_gadget_sub_6DF88630(self):
		#sub_6DF88630
		gadget = "B8E0A6A66EC3"
		self.do(gadget)

		#mov     eax, offset nullAtomWTF3VAtomicString1B; WTF::AtomicString const WTF::nullAtom
		#retn


  def test_gadget_sub_6DF888B0(self):
		#sub_6DF888B0
		gadget = "8B4114C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#retn


  def test_gadget_sub_6DF88BE0(self):
		#sub_6DF88BE0
		gadget = "8D411CC3"
		self.do(gadget)

		#lea     eax, [ecx+1Ch]
		#retn


  def test_gadget_sub_6DF893B0(self):
		#sub_6DF893B0
		gadget = "8D4108C3"
		self.do(gadget)

		#lea     eax, [ecx+8]
		#retn


  def test_gadget_sub_6DF893C0(self):
		#sub_6DF893C0
		gadget = "8B442404894110C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+10h], eax
		#retn    4


  def test_gadget_sub_6DF8B970(self):
		#sub_6DF8B970
		gadget = "8B442408C7000E000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], 0Eh
		#retn    8


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_11(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_11
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DF8BA30(self):
		#sub_6DF8BA30
		gadget = "8B49208B41048BD02B54240433D081E2FF03000033D0895104C20400"
		self.do(gadget)

		#mov     ecx, [ecx+20h]
		#mov     eax, [ecx+4]
		#mov     edx, eax
		#sub     edx, [esp+arg_0]
		#xor     edx, eax
		#and     edx, 3FFh
		#xor     edx, eax
		#mov     [ecx+4], edx
		#retn    4


  def test_gadget_sub_6DF8C170(self):
		#sub_6DF8C170
		gadget = "8B41148B50088BC22BC1F7D81BC023C2C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     edx, [eax+8]
		#mov     eax, edx
		#sub     eax, ecx
		#neg     eax
		#sbb     eax, eax
		#and     eax, edx
		#retn


  def test_gadget_sub_6DF8C400(self):
		#sub_6DF8C400
		gadget = "81490C00004000C3"
		self.do(gadget)

		#or      dword ptr [ecx+0Ch], 400000h
		#retn


  def test_gadget_sub_6DF97B80(self):
		#sub_6DF97B80
		gadget = "8BC18B5008335424088B4C240480600CFE83E2073150088908C7400400000000C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     edx, [eax+8]
		#xor     edx, [esp+arg_4]
		#mov     ecx, [esp+arg_0]
		#and     byte ptr [eax+0Ch], 0FEh
		#and     edx, 7
		#xor     [eax+8], edx
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#retn    8


  def test_gadget_sub_6DF97BB0(self):
		#sub_6DF97BB0
		gadget = "8B5424088BC18B4C240480600CFE89088B4808334C240C89500483E107314808C20C00"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#and     byte ptr [eax+0Ch], 0FEh
		#mov     [eax], ecx
		#mov     ecx, [eax+8]
		#xor     ecx, [esp+arg_8]
		#mov     [eax+4], edx
		#and     ecx, 7
		#xor     [eax+8], ecx
		#retn    0Ch


  def test_gadget_sub_6DF97BE0(self):
		#sub_6DF97BE0
		gadget = "8B5424088BC18B4C2404836008F880600CFE8908895004C20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#and     dword ptr [eax+8], 0FFFFFFF8h
		#and     byte ptr [eax+0Ch], 0FEh
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#retn    8


  def test_gadget_sub_6DF9B040(self):
		#sub_6DF9B040
		gadget = "B807000000C3"
		self.do(gadget)

		#mov     eax, 7
		#retn


  def test_gadget_sub_6DF9B050(self):
		#sub_6DF9B050
		gadget = "C6414600C3"
		self.do(gadget)

		#mov     byte ptr [ecx+46h], 0
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_13(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_13
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DFA30D0(self):
		#sub_6DFA30D0
		gadget = "FF410CC3"
		self.do(gadget)

		#inc     dword ptr [ecx+0Ch]
		#retn


  def test_gadget_sub_6DFA35D0(self):
		#sub_6DFA35D0
		gadget = "8061107FC3"
		self.do(gadget)

		#and     byte ptr [ecx+10h], 7Fh
		#retn


  def test_gadget_sub_6DFA54C0(self):
		#sub_6DFA54C0
		gadget = "C701ACA87F6EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E7FA8AC
		#retn


  def test_gadget_sub_6DFA7F40(self):
		#sub_6DFA7F40
		gadget = "8BC133C9C700A05D856E6689480489480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E855DA0
		#mov     [eax+4], cx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_6DFA94D0(self):
		#sub_6DFA94D0
		gadget = "8B412CC1E81C83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#shr     eax, 1Ch
		#and     eax, 1
		#retn


  def test_gadget_sub_6DFA94E0(self):
		#sub_6DFA94E0
		gadget = "8B412CC1E81D83E001C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#shr     eax, 1Dh
		#and     eax, 1
		#retn


  def test_gadget_sub_6DFA9700(self):
		#sub_6DFA9700
		gadget = "8B415881490C000040008D500133D081E2FFFFFF0F33D0895158C3"
		self.do(gadget)

		#mov     eax, [ecx+58h]
		#or      dword ptr [ecx+0Ch], 400000h
		#lea     edx, [eax+1]
		#xor     edx, eax
		#and     edx, 0FFFFFFFh
		#xor     edx, eax
		#mov     [ecx+58h], edx
		#retn


  def test_gadget_sub_6DFA9720(self):
		#sub_6DFA9720
		gadget = "8B51588D42FF33C225FFFFFF0F33C289415825FFFFFF0F33D23BD01BC0F7D8F7D833410C250000400031410CC3"
		self.do(gadget)

		#mov     edx, [ecx+58h]
		#lea     eax, [edx-1]
		#xor     eax, edx
		#and     eax, 0FFFFFFFh
		#xor     eax, edx
		#mov     [ecx+58h], eax
		#and     eax, 0FFFFFFFh
		#xor     edx, edx
		#cmp     edx, eax
		#sbb     eax, eax
		#neg     eax
		#neg     eax
		#xor     eax, [ecx+0Ch]
		#and     eax, 400000h
		#xor     [ecx+0Ch], eax
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_9(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_9
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6DFAD040(self):
		#sub_6DFAD040
		gadget = "8B4424048B800C030000FF401CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+30Ch]
		#inc     dword ptr [eax+1Ch]
		#retn    4


  def test_gadget_sub_6DFAFCF0(self):
		#sub_6DFAFCF0
		gadget = "6AFF6828F6756E64A10000000050A1F44AA66E33C4508D44240464A3000000008BC18B4C24148B54241889088B4C241C8950048A54242089480888500C8B4C240464890D000000005983C40CC21000"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E75F628
		#mov     eax, large fs:0
		#push    eax
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+10h+var_C]
		#mov     large fs:0, eax
		#mov     eax, ecx
		#mov     ecx, [esp+10h+arg_0]
		#mov     edx, [esp+10h+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+10h+arg_8]
		#mov     [eax+4], edx
		#mov     dl, [esp+10h+arg_C]
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], dl
		#mov     ecx, [esp+10h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 0Ch
		#retn    10h


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_14(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_14
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DFB1170(self):
		#sub_6DFB1170
		gadget = "8BC133C9C700E85F856E89480489480889480C89481089481489481889481C894820894824894828C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E855FE8
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#retn


  def test_gadget_sub_6DFB34A0(self):
		#sub_6DFB34A0
		gadget = "8BC18B0DBCD0A46E89088B15086BA66E895004C705BCD0A46E03000000C705086BA66E00000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, dword_6EA4D0BC
		#mov     [eax], ecx
		#mov     edx, dword_6EA66B08
		#mov     [eax+4], edx
		#mov     dword_6EA4D0BC, 3
		#mov     dword_6EA66B08, 0
		#retn


  def test_gadget_sub_6DFB34D0(self):
		#sub_6DFB34D0
		gadget = "8B01A3BCD0A46E8B4904890D086BA66EC3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     dword_6EA4D0BC, eax
		#mov     ecx, [ecx+4]
		#mov     dword_6EA66B08, ecx
		#retn


  def test_gadget_sub_6DFB3530(self):
		#sub_6DFB3530
		gadget = "33C03B41081BC0F7D8C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     eax, [ecx+8]
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_6DFB5430(self):
		#sub_6DFB5430
		gadget = "DD4140C3"
		self.do(gadget)

		#fld     qword ptr [ecx+40h]
		#retn


  def test_gadget_sub_6DFB5610(self):
		#sub_6DFB5610
		gadget = "8D4138C3"
		self.do(gadget)

		#lea     eax, [ecx+38h]
		#retn


  def test_gadget_sub_6DFB77F0(self):
		#sub_6DFB77F0
		gadget = "518B44240833C9890C24890889480489480859C20800"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#pop     ecx
		#retn    8


  def test_gadget_sub_6DFB98F0(self):
		#sub_6DFB98F0
		gadget = "8B81BC000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0BCh]
		#retn


  def test_gadget_IdSchedulingRingdetailsConcurrencyQBEHXZ(self):
		#IdSchedulingRingdetailsConcurrencyQBEHXZ
		gadget = "8B81B8000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0B8h]
		#retn


  def test_gadget_sub_6DFCE500(self):
		#sub_6DFCE500
		gadget = "B821000000C3"
		self.do(gadget)

		#mov     eax, 21h
		#retn


  def test_gadget_sub_6DFCEBA0(self):
		#sub_6DFCEBA0
		gadget = "B81A000000C3"
		self.do(gadget)

		#mov     eax, 1Ah
		#retn


  def test_gadget_sub_6DFCEBF0(self):
		#sub_6DFCEBF0
		gadget = "33C03981880100000F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+188h], eax
		#setnz   al
		#retn


  def test_gadget_sub_6DFD4040(self):
		#sub_6DFD4040
		gadget = "8B5424088BC18B4C240489088B4C240C8950048B54241089480889500CC21000"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+4], edx
		#mov     edx, [esp+arg_C]
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#retn    10h


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_15(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_15
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DFD74A0(self):
		#sub_6DFD74A0
		gadget = "8BC133C9C70001000000894804884808D905206BA66ED9580CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], cl
		#fld     flt_6EA66B20
		#fstp    dword ptr [eax+0Ch]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_16(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_16
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6DFEB1C0(self):
		#sub_6DFEB1C0
		gadget = "8B4424048B88B801000033C038412A0F95C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+1B8h]
		#xor     eax, eax
		#cmp     [ecx+2Ah], al
		#setnz   al
		#retn


  def test_gadget_sub_6DFEE810(self):
		#sub_6DFEE810
		gadget = "8BC1C70000000000C7400800000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+8], 0
		#retn


  def test_gadget_sub_6DFEF220(self):
		#sub_6DFEF220
		gadget = "518B89B80000008B442408FF01C7042400000000890859C20400"
		self.do(gadget)

		#push    ecx
		#mov     ecx, [ecx+0B8h]
		#mov     eax, [esp+4+arg_0]
		#inc     dword ptr [ecx]
		#mov     [esp+4+var_4], 0
		#mov     [eax], ecx
		#pop     ecx
		#retn    4


  def test_gadget_sub_6DFEF270(self):
		#sub_6DFEF270
		gadget = "B823000000C3"
		self.do(gadget)

		#mov     eax, 23h
		#retn


  def test_gadget_sub_6DFFE450(self):
		#sub_6DFFE450
		gadget = "33C03981D00000000F95C083C025C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+0D0h], eax
		#setnz   al
		#add     eax, 25h
		#retn


  def test_gadget_sub_6E0009B0(self):
		#sub_6E0009B0
		gadget = "B824000000C3"
		self.do(gadget)

		#mov     eax, 24h
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_17(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_17
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E00C6C0(self):
		#sub_6E00C6C0
		gadget = "8B54240C8BC18B4C240489480433C9C7007885856E89500889480C89481089481489481C8948208B4C2408C6401801894824C20C00"
		self.do(gadget)

		#mov     edx, [esp+arg_8]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E858578
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     byte ptr [eax+18h], 1
		#mov     [eax+24h], ecx
		#retn    0Ch


  def test_gadget_sub_6E00EA10(self):
		#sub_6E00EA10
		gadget = "B819000000C3"
		self.do(gadget)

		#mov     eax, 19h
		#retn


  def test_gadget_sub_6E010BE0(self):
		#sub_6E010BE0
		gadget = "8B81E8000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0E8h]
		#retn


  def test_gadget_sub_6E019EA0(self):
		#sub_6E019EA0
		gadget = "8D4118C3"
		self.do(gadget)

		#lea     eax, [ecx+18h]
		#retn


  def test_gadget_sub_6E01A0C0(self):
		#sub_6E01A0C0
		gadget = "8B44240489088B09894804C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#mov     ecx, [ecx]
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E01BF90(self):
		#sub_6E01BF90
		gadget = "8BC18B4C2404890833C989480489480889480C83C9FF894810894814894818C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#or      ecx, 0FFFFFFFFh
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#retn    4


  def test_gadget_sub_6E01BFC0(self):
		#sub_6E01BFC0
		gadget = "6AFF68E8B2766E64A10000000050A1F44AA66E33C4508D44240464A3000000008BC18B4C24148B542418890889500433C989480889480C83C9FF8948108948148948188B4C240464890D000000005983C40CC20800"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E76B2E8
		#mov     eax, large fs:0
		#push    eax
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+10h+var_C]
		#mov     large fs:0, eax
		#mov     eax, ecx
		#mov     ecx, [esp+10h+arg_0]
		#mov     edx, [esp+10h+arg_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#or      ecx, 0FFFFFFFFh
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+10h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 0Ch
		#retn    8


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_18(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_18
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E01FF50(self):
		#sub_6E01FF50
		gadget = "8B4424088B54240C8941348B4424108951388B54241489413C895140668B5424048D4168C6417C01668910894144C7414801000000C641640066895166C21400"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     edx, [esp+arg_8]
		#mov     [ecx+34h], eax
		#mov     eax, [esp+arg_C]
		#mov     [ecx+38h], edx
		#mov     edx, [esp+arg_10]
		#mov     [ecx+3Ch], eax
		#mov     [ecx+40h], edx
		#mov     dx, [esp+arg_0]
		#lea     eax, [ecx+68h]
		#mov     byte ptr [ecx+7Ch], 1
		#mov     [eax], dx
		#mov     [ecx+44h], eax
		#mov     dword ptr [ecx+48h], 1
		#mov     byte ptr [ecx+64h], 0
		#mov     [ecx+66h], dx
		#retn    14h


  def test_gadget_IsHillClimbingEnabledSchedulerProxydetailsConcurrencyQAE_NXZ(self):
		#IsHillClimbingEnabledSchedulerProxydetailsConcurrencyQAE_NXZ
		gadget = "8A81CD000000C3"
		self.do(gadget)

		#mov     al, [ecx+0CDh]
		#retn


  def test_gadget_sub_6E0254C0(self):
		#sub_6E0254C0
		gadget = "8A81CF000000C3"
		self.do(gadget)

		#mov     al, [ecx+0CFh]
		#retn


  def test_gadget_sub_6E0254D0(self):
		#sub_6E0254D0
		gadget = "8A4424048881CF000000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+0CFh], al
		#retn    4


  def test_gadget_sub_6E028960(self):
		#sub_6E028960
		gadget = "B822000000C3"
		self.do(gadget)

		#mov     eax, 22h
		#retn


  def test_gadget_sub_6E02BD80(self):
		#sub_6E02BD80
		gadget = "8BC133C98908894804B2FE20500C56BEF8FFFFFF21700821701820501C89481089481421702820502C89482089482421703820503C8948308948348948448A484880E1FD80C901C74040010000008848485EC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     dl, 0FEh
		#and     [eax+0Ch], dl
		#push    esi
		#mov     esi, 0FFFFFFF8h
		#and     [eax+8], esi
		#and     [eax+18h], esi
		#and     [eax+1Ch], dl
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#and     [eax+28h], esi
		#and     [eax+2Ch], dl
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#and     [eax+38h], esi
		#and     [eax+3Ch], dl
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+44h], ecx
		#mov     cl, [eax+48h]
		#and     cl, 0FDh
		#or      cl, 1
		#mov     dword ptr [eax+40h], 1
		#mov     [eax+48h], cl
		#pop     esi
		#retn


  def test_gadget_sub_6E0351C0(self):
		#sub_6E0351C0
		gadget = "8B41488B514CC3"
		self.do(gadget)

		#mov     eax, [ecx+48h]
		#mov     edx, [ecx+4Ch]
		#retn


  def test_gadget_sub_6E036480(self):
		#sub_6E036480
		gadget = "8BC133C98908C740040100000089480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_6E037460(self):
		#sub_6E037460
		gadget = "8A4139C3"
		self.do(gadget)

		#mov     al, [ecx+39h]
		#retn


  def test_gadget_sub_6E037470(self):
		#sub_6E037470
		gadget = "8B49308D4101F7D81BC023C1C3"
		self.do(gadget)

		#mov     ecx, [ecx+30h]
		#lea     eax, [ecx+1]
		#neg     eax
		#sbb     eax, eax
		#and     eax, ecx
		#retn


  def test_gadget_sub_6E0393B0(self):
		#sub_6E0393B0
		gadget = "8D4104C3"
		self.do(gadget)

		#lea     eax, [ecx+4]
		#retn


  def test_gadget_sub_6E0393C0(self):
		#sub_6E0393C0
		gadget = "DD4120C3"
		self.do(gadget)

		#fld     qword ptr [ecx+20h]
		#retn


  def test_gadget_sub_6E0393D0(self):
		#sub_6E0393D0
		gadget = "8D4110C3"
		self.do(gadget)

		#lea     eax, [ecx+10h]
		#retn


  def test_gadget_sub_6E0393E0(self):
		#sub_6E0393E0
		gadget = "8B4424048B1089512C8B4004894130C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+2Ch], edx
		#mov     eax, [eax+4]
		#mov     [ecx+30h], eax
		#retn    4


  def test_gadget_sub_6E039400(self):
		#sub_6E039400
		gadget = "33C089412C894130C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [ecx+2Ch], eax
		#mov     [ecx+30h], eax
		#retn


  def test_gadget_sub_6E039410(self):
		#sub_6E039410
		gadget = "D9442404D95934C20400"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+34h]
		#retn    4


  def test_gadget_sub_6E039420(self):
		#sub_6E039420
		gadget = "8A4151C3"
		self.do(gadget)

		#mov     al, [ecx+51h]
		#retn


  def test_gadget_sub_6E039430(self):
		#sub_6E039430
		gadget = "8A442404884151C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+51h], al
		#retn    4


  def test_gadget_sub_6E039440(self):
		#sub_6E039440
		gadget = "8D4144C3"
		self.do(gadget)

		#lea     eax, [ecx+44h]
		#retn


  def test_gadget_sub_6E039450(self):
		#sub_6E039450
		gadget = "33C039414C0F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+4Ch], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E039460(self):
		#sub_6E039460
		gadget = "8B818C000000C3"
		self.do(gadget)

		#mov     eax, [ecx+8Ch]
		#retn


  def test_gadget_sub_6E03BC90(self):
		#sub_6E03BC90
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_20(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_20
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E03CE70(self):
		#sub_6E03CE70
		gadget = "8B4104FF4008C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#inc     dword ptr [eax+8]
		#retn


  def test_gadget_sub_6E03CF50(self):
		#sub_6E03CF50
		gadget = "8BC18B4C2404C700E094856E894804C7400800000000C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8594E0
		#mov     [eax+4], ecx
		#mov     dword ptr [eax+8], 0
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_21(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_21
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_22(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_22
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E03E3E0(self):
		#sub_6E03E3E0
		gadget = "8BC1C740040100000033C9C700D897856E89480889480CC3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], 1
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8597D8
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn


  def test_gadget_sub_6E043110(self):
		#sub_6E043110
		gadget = "8A414CC0E8032401C3"
		self.do(gadget)

		#mov     al, [ecx+4Ch]
		#shr     al, 3
		#and     al, 1
		#retn


  def test_gadget_sub_6E043120(self):
		#sub_6E043120
		gadget = "8A44240402C002C002C032414C240830414CC20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#add     al, al
		#xor     al, [ecx+4Ch]
		#and     al, 8
		#xor     [ecx+4Ch], al
		#retn    4


  def test_gadget_sub_6E0431D0(self):
		#sub_6E0431D0
		gadget = "FF41D4C3"
		self.do(gadget)

		#inc     dword ptr [ecx-2Ch]
		#retn


  def test_gadget_sub_6E0462B0(self):
		#sub_6E0462B0
		gadget = "8BC133C9C7007CAB856E89480489480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E85AB7C
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_6E046540(self):
		#sub_6E046540
		gadget = "518B44240833C9890C24890889480459C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E0483E0(self):
		#sub_6E0483E0
		gadget = "518B44240833C98908894804890C2489480889480C59C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E04AA30(self):
		#sub_6E04AA30
		gadget = "8BC18B4C24048B1189108B490489480433C989480889480C894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E04DE90(self):
		#sub_6E04DE90
		gadget = "8A816D010000C3"
		self.do(gadget)

		#mov     al, [ecx+16Dh]
		#retn


  def test_gadget_sub_6E04ECA0(self):
		#sub_6E04ECA0
		gadget = "8B410CC1E8092401C3"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#shr     eax, 9
		#and     al, 1
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_5(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_5
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E0517A0(self):
		#sub_6E0517A0
		gadget = "8A442404884160C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+60h], al
		#retn    4


  def test_gadget_sub_6E052030(self):
		#sub_6E052030
		gadget = "8B41148B48088B4164C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     ecx, [eax+8]
		#mov     eax, [ecx+64h]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_25(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_25
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_26(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_26
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E057150(self):
		#sub_6E057150
		gadget = "8B4424048B083B0D6860A66E0F94C0C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax]
		#cmp     ecx, dword_6EA66068
		#setz    al
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_7(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_7
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E05DC30(self):
		#sub_6E05DC30
		gadget = "8A44240402C002C002C03241582408304158C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#add     al, al
		#xor     al, [ecx+58h]
		#and     al, 8
		#xor     [ecx+58h], al
		#retn    4


  def test_gadget_sub_6E05DC70(self):
		#sub_6E05DC70
		gadget = "8A414CC0E8022401C3"
		self.do(gadget)

		#mov     al, [ecx+4Ch]
		#shr     al, 2
		#and     al, 1
		#retn


  def test_gadget_sub_6E05DCB0(self):
		#sub_6E05DCB0
		gadget = "8A4158C0E8022401C3"
		self.do(gadget)

		#mov     al, [ecx+58h]
		#shr     al, 2
		#and     al, 1
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_28(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_28
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E05F180(self):
		#sub_6E05F180
		gadget = "518B44240833C98908890C2489480489480889480C59C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E05F620(self):
		#sub_6E05F620
		gadget = "8B4424048A5078885178C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax+78h]
		#mov     [ecx+78h], dl
		#retn    4


  def test_gadget_sub_6E061FF0(self):
		#sub_6E061FF0
		gadget = "8B4144C3"
		self.do(gadget)

		#mov     eax, [ecx+44h]
		#retn


  def test_gadget_sub_6E062090(self):
		#sub_6E062090
		gadget = "8B4C24048B1133C03B153C63A66E0F94C0C20400"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#xor     eax, eax
		#cmp     edx, dword_6EA6633C
		#setz    al
		#retn    4


  def test_gadget_sub_6E062DA0(self):
		#sub_6E062DA0
		gadget = "8B442404894138C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+38h], eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_30(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_30
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_9(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_9
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E064310(self):
		#sub_6E064310
		gadget = "837924000F95C0C3"
		self.do(gadget)

		#cmp     dword ptr [ecx+24h], 0
		#setnz   al
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_10(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_10
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_33(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_33
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_11(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_11
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E064FB0(self):
		#sub_6E064FB0
		gadget = "8A8184000000C0E8032401C3"
		self.do(gadget)

		#mov     al, [ecx+84h]
		#shr     al, 3
		#and     al, 1
		#retn


  def test_gadget_sub_6E066340(self):
		#sub_6E066340
		gadget = "8A8186000000C0E8042401C3"
		self.do(gadget)

		#mov     al, [ecx+86h]
		#shr     al, 4
		#and     al, 1
		#retn


  def test_gadget_sub_6E066350(self):
		#sub_6E066350
		gadget = "8A442404C0E0043281860000002410308186000000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 4
		#xor     al, [ecx+86h]
		#and     al, 10h
		#xor     [ecx+86h], al
		#retn    4


  def test_gadget_sub_6E0663C0(self):
		#sub_6E0663C0
		gadget = "8B8180000000C3"
		self.do(gadget)

		#mov     eax, [ecx+80h]
		#retn


  def test_gadget_sub_6E066410(self):
		#sub_6E066410
		gadget = "8A818C000000C0E8062401C3"
		self.do(gadget)

		#mov     al, [ecx+8Ch]
		#shr     al, 6
		#and     al, 1
		#retn


  def test_gadget_sub_6E06CA80(self):
		#sub_6E06CA80
		gadget = "8B81D0000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0D0h]
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_12(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_12
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E0717D0(self):
		#sub_6E0717D0
		gadget = "8B8188010000C3"
		self.do(gadget)

		#mov     eax, [ecx+188h]
		#retn


  def test_gadget_sub_6E071940(self):
		#sub_6E071940
		gadget = "8A8198010000D0E82401C3"
		self.do(gadget)

		#mov     al, [ecx+198h]
		#shr     al, 1
		#and     al, 1
		#retn


  def test_gadget_sub_6E071980(self):
		#sub_6E071980
		gadget = "FF8188FEFFFFC3"
		self.do(gadget)

		#inc     dword ptr [ecx-178h]
		#retn


  def test_gadget_sub_6E073810(self):
		#sub_6E073810
		gadget = "8B4134C3"
		self.do(gadget)

		#mov     eax, [ecx+34h]
		#retn


  def test_gadget_sub_6E0755C0(self):
		#sub_6E0755C0
		gadget = "8B4164C3"
		self.do(gadget)

		#mov     eax, [ecx+64h]
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_15(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_15
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_12(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_12
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E07B330(self):
		#sub_6E07B330
		gadget = "8B4424048981C4000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+0C4h], eax
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_18(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_18
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_20(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_20
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_21(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_21
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E0850F0(self):
		#sub_6E0850F0
		gadget = "8A414CD0E82401C3"
		self.do(gadget)

		#mov     al, [ecx+4Ch]
		#shr     al, 1
		#and     al, 1
		#retn


  def test_gadget_sub_6E085100(self):
		#sub_6E085100
		gadget = "0FB6414CD1E8F7D083E001C3"
		self.do(gadget)

		#movzx   eax, byte ptr [ecx+4Ch]
		#shr     eax, 1
		#not     eax
		#and     eax, 1
		#retn


  def test_gadget_sub_6E08C790(self):
		#sub_6E08C790
		gadget = "D94424048B442408DB00DC0D10E1846ED95C2404D8742404D95C2404D9442404C3"
		self.do(gadget)

		#fld     [esp+arg_0]
		#mov     eax, [esp+arg_4]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_0]
		#fdiv    [esp+arg_0]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_15(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_15
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E08EE30(self):
		#sub_6E08EE30
		gadget = "C701EC8D856EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E858DEC
		#retn


  def test_gadget_sub_6E08EE40(self):
		#sub_6E08EE40
		gadget = "DD050847A66EC3"
		self.do(gadget)

		#fld     dbl_6EA64708
		#retn


  def test_gadget_sub_6E08EE90(self):
		#sub_6E08EE90
		gadget = "8B44240CC7000B000000C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     dword ptr [eax], 0Bh
		#retn    0Ch


  def test_gadget_sub_6E091130(self):
		#sub_6E091130
		gadget = "6AFF68A956776E64A1000000005051A1F44AA66E33C4508D44240864A300000000C7442404000000008B4424188B4C241C89088B4C240864890D000000005983C410C20800"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7756A9
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#mov     [esp+14h+var_10], 0
		#mov     eax, [esp+14h+arg_0]
		#mov     ecx, [esp+14h+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn    8


  def test_gadget_sub_6E092720(self):
		#sub_6E092720
		gadget = "8BC133C98808894804894808C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], cl
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#retn


  def test_gadget___RTC_NumErrors_19(self):
		#__RTC_NumErrors_19
		gadget = "B804000000C3"
		self.do(gadget)

		#mov     eax, 4
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_38(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_38
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E095600(self):
		#sub_6E095600
		gadget = "8B442404C6401901C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     byte ptr [eax+19h], 1
		#retn    4


  def test_gadget_sub_6E095610(self):
		#sub_6E095610
		gadget = "8B41048A80860000002401C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     al, [eax+86h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E097A50(self):
		#sub_6E097A50
		gadget = "8B4124C3"
		self.do(gadget)

		#mov     eax, [ecx+24h]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_39(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_39
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E098F00(self):
		#sub_6E098F00
		gadget = "8B4110C3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#retn


  def test_gadget_sub_6E0992F0(self):
		#sub_6E0992F0
		gadget = "8BC18B4C2404894804C740087CA4866E33C9C700B4A4866EC7400898A4866E89480C89481089481489481889481CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#mov     dword ptr [eax+8], offset off_6E86A47C
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E86A4B4
		#mov     dword ptr [eax+8], offset off_6E86A498
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn    4


  def test_gadget_sub_6E09AF10(self):
		#sub_6E09AF10
		gadget = "8BC18B4C2404890833C989480889480C33D26689501089481489481889481CC6402001894824894828C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#xor     edx, edx
		#mov     [eax+10h], dx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     byte ptr [eax+20h], 1
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_16(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_16
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_17(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_17
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E09DA40(self):
		#sub_6E09DA40
		gadget = "8B5424048BC133C9894804C70014B2866E89500889480C89481089481489481889481CC20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     dword ptr [eax], offset off_6E86B214
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn    4


  def test_gadget_sub_6E09DF70(self):
		#sub_6E09DF70
		gadget = "D901D9442404D9C0DEEAD9C9D919D94108D8C1D8C1D95908D94104D8E1D95904D9410CD8C1DEC1D9590CC20400"
		self.do(gadget)

		#fld     dword ptr [ecx]
		#fld     [esp+arg_0]
		#fld     st
		#fsubp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [ecx]
		#fld     dword ptr [ecx+8]
		#fadd    st, st(1)
		#fadd    st, st(1)
		#fstp    dword ptr [ecx+8]
		#fld     dword ptr [ecx+4]
		#fsub    st, st(1)
		#fstp    dword ptr [ecx+4]
		#fld     dword ptr [ecx+0Ch]
		#fadd    st, st(1)
		#faddp   st(1), st
		#fstp    dword ptr [ecx+0Ch]
		#retn    4


  def test_gadget_sub_6E0A7DA0(self):
		#sub_6E0A7DA0
		gadget = "8BC18B4C24048908C7400400000000C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_40(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_40
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E0A8B90(self):
		#sub_6E0A8B90
		gadget = "B809000000C3"
		self.do(gadget)

		#mov     eax, 9
		#retn


  def test_gadget_sub_6E0A8F60(self):
		#sub_6E0A8F60
		gadget = "8BC133C9890889480489480889480C89481089481489481889481CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn


  def test_gadget_sub_6E0A9690(self):
		#sub_6E0A9690
		gadget = "8A415CC3"
		self.do(gadget)

		#mov     al, [ecx+5Ch]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_41(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_41
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E0AD910(self):
		#sub_6E0AD910
		gadget = "8B4174C70006000000C3"
		self.do(gadget)

		#mov     eax, [ecx+74h]
		#mov     dword ptr [eax], 6
		#retn


  def test_gadget_sub_6E0B05F0(self):
		#sub_6E0B05F0
		gadget = "33C039410C0F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+0Ch], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E0B0600(self):
		#sub_6E0B0600
		gadget = "8B4104C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#retn


  def test_gadget_sub_6E0B0980(self):
		#sub_6E0B0980
		gadget = "8B01C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_42(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_42
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E0B10A0(self):
		#sub_6E0B10A0
		gadget = "8BC133C9890889480489480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_6E0B10C0(self):
		#sub_6E0B10C0
		gadget = "8B0133C93948040F94C0C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#xor     ecx, ecx
		#cmp     [eax+4], ecx
		#setz    al
		#retn


  def test_gadget__Release_NonReentrantLockdetailsConcurrencyQAEXXZ(self):
		#_Release_NonReentrantLockdetailsConcurrencyQAEXXZ
		gadget = "C70100000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx], 0
		#retn


  def test_gadget_sub_6E0B77C0(self):
		#sub_6E0B77C0
		gadget = "33C03941100F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+10h], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E0B8CB0(self):
		#sub_6E0B8CB0
		gadget = "8BC133C9890889480866C7400C010089481089480489481889481C8948205333D26689501489482489482889482C89483066C740340001884836BA30B6266E89503889503C5633F6668970406689704289484866C7404C01008948508948446689705489485889485C89486089486489486889486C8948705E66C74074000188487689507889507C8988800000005BC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+8], ecx
		#mov     word ptr [eax+0Ch], 1
		#mov     [eax+10h], ecx
		#mov     [eax+4], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#push    ebx
		#xor     edx, edx
		#mov     [eax+14h], dx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     word ptr [eax+34h], 100h
		#mov     [eax+36h], cl
		#mov     edx, offset loc_6E26B630
		#mov     [eax+38h], edx
		#mov     [eax+3Ch], edx
		#push    esi
		#xor     esi, esi
		#mov     [eax+40h], si
		#mov     [eax+42h], si
		#mov     [eax+48h], ecx
		#mov     word ptr [eax+4Ch], 1
		#mov     [eax+50h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+54h], si
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], ecx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+68h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], ecx
		#pop     esi
		#mov     word ptr [eax+74h], 100h
		#mov     [eax+76h], cl
		#mov     [eax+78h], edx
		#mov     [eax+7Ch], edx
		#mov     [eax+80h], ecx
		#pop     ebx
		#retn


  def test_gadget_sub_6E0B8E60(self):
		#sub_6E0B8E60
		gadget = "8B4424042B410C8B89BC0E00008901C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#sub     eax, [ecx+0Ch]
		#mov     ecx, [ecx+0EBCh]
		#mov     [ecx], eax
		#retn    4


  def test_gadget_sub_6E0B8E80(self):
		#sub_6E0B8E80
		gadget = "8B91BC0E00008B4424042B410C8942048B91BC0E00008942088B89BC0E000089410CC20400"
		self.do(gadget)

		#mov     edx, [ecx+0EBCh]
		#mov     eax, [esp+arg_0]
		#sub     eax, [ecx+0Ch]
		#mov     [edx+4], eax
		#mov     edx, [ecx+0EBCh]
		#mov     [edx+8], eax
		#mov     ecx, [ecx+0EBCh]
		#mov     [ecx+0Ch], eax
		#retn    4


  def test_gadget_sub_6E0B8EB0(self):
		#sub_6E0B8EB0
		gadget = "8B4424042B410C8B89BC0E0000894108C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#sub     eax, [ecx+0Ch]
		#mov     ecx, [ecx+0EBCh]
		#mov     [ecx+8], eax
		#retn    4


  def test_gadget_sub_6E0B8ED0(self):
		#sub_6E0B8ED0
		gadget = "8B4424042B410C8B89BC0E000089410CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#sub     eax, [ecx+0Ch]
		#mov     ecx, [ecx+0EBCh]
		#mov     [ecx+0Ch], eax
		#retn    4


  def test_gadget_sub_6E0B9A70(self):
		#sub_6E0B9A70
		gadget = "8BC189401033C9668948148848168948608D502089501856BA2000000089501C89506889888C0000008D706C8970648990940000008B5424088988B80000008DB09800000089B0900000008B3289B0BC0000008B52048990C00000008908894808668948046689480C5EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     [eax+10h], eax
		#xor     ecx, ecx
		#mov     [eax+14h], cx
		#mov     [eax+16h], cl
		#mov     [eax+60h], ecx
		#lea     edx, [eax+20h]
		#mov     [eax+18h], edx
		#push    esi
		#mov     edx, 20h
		#mov     [eax+1Ch], edx
		#mov     [eax+68h], edx
		#mov     [eax+8Ch], ecx
		#lea     esi, [eax+6Ch]
		#mov     [eax+64h], esi
		#mov     [eax+94h], edx
		#mov     edx, [esp+4+arg_0]
		#mov     [eax+0B8h], ecx
		#lea     esi, [eax+98h]
		#mov     [eax+90h], esi
		#mov     esi, [edx]
		#mov     [eax+0BCh], esi
		#mov     edx, [edx+4]
		#mov     [eax+0C0h], edx
		#mov     [eax], ecx
		#mov     [eax+8], ecx
		#mov     [eax+4], cx
		#mov     [eax+0Ch], cx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E0BF870(self):
		#sub_6E0BF870
		gadget = "518B44240C8B088B442408FF01C7042400000000890859C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_4]
		#mov     ecx, [eax]
		#mov     eax, [esp+4+arg_0]
		#inc     dword ptr [ecx]
		#mov     [esp+4+var_4], 0
		#mov     [eax], ecx
		#pop     ecx
		#retn


  def test_gadget_CancelUMSThreadProxydetailsConcurrencyQAEXXZ(self):
		#CancelUMSThreadProxydetailsConcurrencyQAEXXZ
		gadget = "C7414801000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+48h], 1
		#retn


  def test_gadget_sub_6E0CB6B0(self):
		#sub_6E0CB6B0
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C83482403C6402001C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#or      dword ptr [eax+24h], 3
		#mov     byte ptr [eax+20h], 1
		#retn


  def test_gadget_nullsub_2(self):
		#nullsub_2
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_19(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_19
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E0D0C20(self):
		#sub_6E0D0C20
		gadget = "8B49288B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+28h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E0D0C30(self):
		#sub_6E0D0C30
		gadget = "8B492C8B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+2Ch]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E0D0C40(self):
		#sub_6E0D0C40
		gadget = "8B49388B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+38h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E0D0C50(self):
		#sub_6E0D0C50
		gadget = "8B493C8B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+3Ch]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E0D0F70(self):
		#sub_6E0D0F70
		gadget = "8B442404C70000000000C7400400000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 0
		#retn    4


  def test_gadget_sub_6E0D0F90(self):
		#sub_6E0D0F90
		gadget = "8B44240433C9890889480489480889480CC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn    8


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_25(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_25
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_26(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_26
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E0D9EB0(self):
		#sub_6E0D9EB0
		gadget = "8B5424088BC18B4C240489480433C9C700A0FD866E89500889480C89481089481489481889481CC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E86FDA0
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn    8


  def test_gadget_sub_6E0E1D70(self):
		#sub_6E0E1D70
		gadget = "33C089410489410889410C894110C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [ecx+4], eax
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#retn


  def test_gadget_sub_6E0E1FD0(self):
		#sub_6E0E1FD0
		gadget = "518B44240833C9C7001CC77F6E890C2489480459C20800"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E7FC71C
		#mov     [esp+4+var_4], ecx
		#mov     [eax+4], ecx
		#pop     ecx
		#retn    8


  def test_gadget_sub_6E0E42F0(self):
		#sub_6E0E42F0
		gadget = "8B442404894118C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+18h], eax
		#retn    4


  def test_gadget_sub_6E0E4E80(self):
		#sub_6E0E4E80
		gadget = "8B44240483C01C894118C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 1Ch
		#mov     [ecx+18h], eax
		#retn    4


  def test_gadget_sub_6E0E4E90(self):
		#sub_6E0E4E90
		gadget = "8B510433C0894230894118C3"
		self.do(gadget)

		#mov     edx, [ecx+4]
		#xor     eax, eax
		#mov     [edx+30h], eax
		#mov     [ecx+18h], eax
		#retn


  def test_gadget_sub_6E0E67A0(self):
		#sub_6E0E67A0
		gadget = "8B44240483C02489411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 24h
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_sub_6E0E7410(self):
		#sub_6E0E7410
		gadget = "518B442408D9EE33C98908894804DD5810890C2489480889481889481C59C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#fldz
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#fstp    qword ptr [eax+10h]
		#mov     [esp+4+var_4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E0F0F20(self):
		#sub_6E0F0F20
		gadget = "8B44240483C04089411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 40h
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_sub_6E0F2B60(self):
		#sub_6E0F2B60
		gadget = "8B44240483C010894118C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 10h
		#mov     [ecx+18h], eax
		#retn    4


  def test_gadget_unknown_libname_4(self):
		#unknown_libname_4
		gadget = "33C03941340F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+34h], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E0F6E00(self):
		#sub_6E0F6E00
		gadget = "8B4424048B0485206FA66EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, dword_6EA66F20[eax*4]
		#retn


  def test_gadget_sub_6E0F6E10(self):
		#sub_6E0F6E10
		gadget = "8B4424048B0481C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [ecx+eax*4]
		#retn    4


  def test_gadget_sub_6E0F6FA0(self):
		#sub_6E0F6FA0
		gadget = "8B44240483C02C89411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 2Ch
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_sub_6E0F73C0(self):
		#sub_6E0F73C0
		gadget = "518B44240833C98908894804894808890C2489480C89481089481489481888481C59C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6E0FD7E0(self):
		#sub_6E0FD7E0
		gadget = "8B4424088B108B44240C3B100F94C28891E8000000C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     edx, [eax]
		#mov     eax, [esp+arg_8]
		#cmp     edx, [eax]
		#setz    dl
		#mov     [ecx+0E8h], dl
		#retn    0Ch


  def test_gadget_sub_6E0FFC80(self):
		#sub_6E0FFC80
		gadget = "518B44240833C9890C24890889480489480889480C89481059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E109730(self):
		#sub_6E109730
		gadget = "8D41F08B49F489413CC3"
		self.do(gadget)

		#lea     eax, [ecx-10h]
		#mov     ecx, [ecx-0Ch]
		#mov     [ecx+3Ch], eax
		#retn


  def test_gadget_sub_6E109740(self):
		#sub_6E109740
		gadget = "C6412401C3"
		self.do(gadget)

		#mov     byte ptr [ecx+24h], 1
		#retn


  def test_gadget_sub_6E109750(self):
		#sub_6E109750
		gadget = "C6412400C3"
		self.do(gadget)

		#mov     byte ptr [ecx+24h], 0
		#retn


  def test_gadget_sub_6E109760(self):
		#sub_6E109760
		gadget = "8B511C33C089426489411CC3"
		self.do(gadget)

		#mov     edx, [ecx+1Ch]
		#xor     eax, eax
		#mov     [edx+64h], eax
		#mov     [ecx+1Ch], eax
		#retn


  def test_gadget_sub_6E10E7D0(self):
		#sub_6E10E7D0
		gadget = "8B5424088BC18B4C2404C70001000000894804895008C7400C00000000C20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], edx
		#mov     dword ptr [eax+0Ch], 0
		#retn    8


  def test_gadget_sub_6E10F610(self):
		#sub_6E10F610
		gadget = "8B44240483C038894118C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 38h
		#mov     [ecx+18h], eax
		#retn    4


  def test_gadget_sub_6E111150(self):
		#sub_6E111150
		gadget = "8BC133C9C7002058896E89480489480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E895820
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_2YAPAXIPAXZ(self):
		#2YAPAXIPAXZ
		gadget = "8B442408C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#retn


  def test_gadget_sub_6E114200(self):
		#sub_6E114200
		gadget = "8B44240483C048894114C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 48h
		#mov     [ecx+14h], eax
		#retn    4


  def test_gadget_sub_6E1172C0(self):
		#sub_6E1172C0
		gadget = "8B44240483C004894114C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 4
		#mov     [ecx+14h], eax
		#retn    4


  def test_gadget_sub_6E1172D0(self):
		#sub_6E1172D0
		gadget = "C7411400000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+14h], 0
		#retn


  def test_gadget_sub_6E1174B0(self):
		#sub_6E1174B0
		gadget = "8B442404D94004D95C2404D900D801D919D9442404D84104D95904D94004D95C2404D94108D800D95908D9410CD8442404D9590CD94004D95C2404D900D84110D95910D94114D8442404D95914D94004D95C2404D94118D800D95918D9411CD8442404D9591CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     dword ptr [eax+4]
		#fstp    [esp+arg_0]
		#fld     dword ptr [eax]
		#fadd    dword ptr [ecx]
		#fstp    dword ptr [ecx]
		#fld     [esp+arg_0]
		#fadd    dword ptr [ecx+4]
		#fstp    dword ptr [ecx+4]
		#fld     dword ptr [eax+4]
		#fstp    [esp+arg_0]
		#fld     dword ptr [ecx+8]
		#fadd    dword ptr [eax]
		#fstp    dword ptr [ecx+8]
		#fld     dword ptr [ecx+0Ch]
		#fadd    [esp+arg_0]
		#fstp    dword ptr [ecx+0Ch]
		#fld     dword ptr [eax+4]
		#fstp    [esp+arg_0]
		#fld     dword ptr [eax]
		#fadd    dword ptr [ecx+10h]
		#fstp    dword ptr [ecx+10h]
		#fld     dword ptr [ecx+14h]
		#fadd    [esp+arg_0]
		#fstp    dword ptr [ecx+14h]
		#fld     dword ptr [eax+4]
		#fstp    [esp+arg_0]
		#fld     dword ptr [ecx+18h]
		#fadd    dword ptr [eax]
		#fstp    dword ptr [ecx+18h]
		#fld     dword ptr [ecx+1Ch]
		#fadd    [esp+arg_0]
		#fstp    dword ptr [ecx+1Ch]
		#retn    4


  def test_gadget_sub_6E117520(self):
		#sub_6E117520
		gadget = "518B44240CD900D9E0D95C240CD940048B442408D9E0D91C24D900D944240CD9C0DEC2D9C9D918D94004D90424D9C0DEC2D9C9D95804D9C1D84008D95808D9C0D8400CD9580CD94010D8C2D95810D9C0D84014D95814D94018DEC2D9C9D95818D8401CD9581C59C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_4]
		#fld     dword ptr [eax]
		#fchs
		#fstp    [esp+4+arg_4]
		#fld     dword ptr [eax+4]
		#mov     eax, [esp+4+arg_0]
		#fchs
		#fstp    [esp+4+var_4]
		#fld     dword ptr [eax]
		#fld     [esp+4+arg_4]
		#fld     st
		#faddp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [eax]
		#fld     dword ptr [eax+4]
		#fld     [esp+4+var_4]
		#fld     st
		#faddp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [eax+4]
		#fld     st(1)
		#fadd    dword ptr [eax+8]
		#fstp    dword ptr [eax+8]
		#fld     st
		#fadd    dword ptr [eax+0Ch]
		#fstp    dword ptr [eax+0Ch]
		#fld     dword ptr [eax+10h]
		#fadd    st, st(2)
		#fstp    dword ptr [eax+10h]
		#fld     st
		#fadd    dword ptr [eax+14h]
		#fstp    dword ptr [eax+14h]
		#fld     dword ptr [eax+18h]
		#faddp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [eax+18h]
		#fadd    dword ptr [eax+1Ch]
		#fstp    dword ptr [eax+1Ch]
		#pop     ecx
		#retn


  def test_gadget_sub_6E117590(self):
		#sub_6E117590
		gadget = "8B4424048B1089118B50048951048B50088951088B500C89510C8B50108951108B50148951148B50188951188B501C89511C8B50208951208B50248951248A50298851388A402A884139C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx], edx
		#mov     edx, [eax+4]
		#mov     [ecx+4], edx
		#mov     edx, [eax+8]
		#mov     [ecx+8], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+0Ch], edx
		#mov     edx, [eax+10h]
		#mov     [ecx+10h], edx
		#mov     edx, [eax+14h]
		#mov     [ecx+14h], edx
		#mov     edx, [eax+18h]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+1Ch]
		#mov     [ecx+1Ch], edx
		#mov     edx, [eax+20h]
		#mov     [ecx+20h], edx
		#mov     edx, [eax+24h]
		#mov     [ecx+24h], edx
		#mov     dl, [eax+29h]
		#mov     [ecx+38h], dl
		#mov     al, [eax+2Ah]
		#mov     [ecx+39h], al
		#retn    4


  def test_gadget_do_narrowctypeDstdMBEDDDZ(self):
		#do_narrowctypeDstdMBEDDDZ
		gadget = "8A442404C20800"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#retn    8


  def test_gadget_do_widenctypeDstdMBEDDZ(self):
		#do_widenctypeDstdMBEDDZ
		gadget = "8A442404C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#retn    4


  def test_gadget_sub_6E1176E0(self):
		#sub_6E1176E0
		gadget = "8A442404C20C00"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#retn    0Ch


  def test_gadget_nullsub_3(self):
		#nullsub_3
		gadget = "C21800"
		self.do(gadget)

		#retn    18h


  def test_gadget_nullsub_4(self):
		#nullsub_4
		gadget = "C20800"
		self.do(gadget)

		#retn    8


  def test_gadget_sub_6E117FF0(self):
		#sub_6E117FF0
		gadget = "8BC18B4C24048B542408890833C989500489480889480C89481088481489481888481C89482088482489482888482C89483088483489483C89484089484488484889484C88485089485488485889485C884860894864884868894870894874C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], cl
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cl
		#mov     [eax+20h], ecx
		#mov     [eax+24h], cl
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], cl
		#mov     [eax+30h], ecx
		#mov     [eax+34h], cl
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], cl
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], cl
		#mov     [eax+54h], ecx
		#mov     [eax+58h], cl
		#mov     [eax+5Ch], ecx
		#mov     [eax+60h], cl
		#mov     [eax+64h], ecx
		#mov     [eax+68h], cl
		#mov     [eax+70h], ecx
		#mov     [eax+74h], ecx
		#retn    8


  def test_gadget_sub_6E11B4E0(self):
		#sub_6E11B4E0
		gadget = "8B5424048B012BC289018B41088D04508941088B41042BC28941048B410C8D145089510CC20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, [ecx]
		#sub     eax, edx
		#mov     [ecx], eax
		#mov     eax, [ecx+8]
		#lea     eax, [eax+edx*2]
		#mov     [ecx+8], eax
		#mov     eax, [ecx+4]
		#sub     eax, edx
		#mov     [ecx+4], eax
		#mov     eax, [ecx+0Ch]
		#lea     edx, [eax+edx*2]
		#mov     [ecx+0Ch], edx
		#retn    4


  def test_gadget_sub_6E11B730(self):
		#sub_6E11B730
		gadget = "8B44240483C008894124C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 8
		#mov     [ecx+24h], eax
		#retn    4


  def test_gadget_sub_6E11B8E0(self):
		#sub_6E11B8E0
		gadget = "8B41148B403CC3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+3Ch]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_43(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_43
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E1243C0(self):
		#sub_6E1243C0
		gadget = "8B442408C60001C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     byte ptr [eax], 1
		#retn    8


  def test_gadget_sub_6E1243D0(self):
		#sub_6E1243D0
		gadget = "8B442408C60000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     byte ptr [eax], 0
		#retn    8


  def test_gadget_sub_6E1243E0(self):
		#sub_6E1243E0
		gadget = "8B44240483C03489411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 34h
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_sub_6E126F70(self):
		#sub_6E126F70
		gadget = "8B44240483C01489411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 14h
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_MarkRootRemovedVirtualProcessorRootdetailsConcurrencyQAEXXZ(self):
		#MarkRootRemovedVirtualProcessorRootdetailsConcurrencyQAEXXZ
		gadget = "C6414401C3"
		self.do(gadget)

		#mov     byte ptr [ecx+44h], 1
		#retn


  def test_gadget_sub_6E12C640(self):
		#sub_6E12C640
		gadget = "C6410401C20400"
		self.do(gadget)

		#mov     byte ptr [ecx+4], 1
		#retn    4


  def test_gadget_sub_6E12C650(self):
		#sub_6E12C650
		gadget = "C6410400C20400"
		self.do(gadget)

		#mov     byte ptr [ecx+4], 0
		#retn    4


  def test_gadget_sub_6E12D180(self):
		#sub_6E12D180
		gadget = "C6410C01C3"
		self.do(gadget)

		#mov     byte ptr [ecx+0Ch], 1
		#retn


  def test_gadget_ResetOverflowTaskStackdetailsConcurrencyQAEXXZ(self):
		#ResetOverflowTaskStackdetailsConcurrencyQAEXXZ
		gadget = "C6410C00C3"
		self.do(gadget)

		#mov     byte ptr [ecx+0Ch], 0
		#retn


  def test_gadget_sub_6E12DB40(self):
		#sub_6E12DB40
		gadget = "8B41488B48148B4108C3"
		self.do(gadget)

		#mov     eax, [ecx+48h]
		#mov     ecx, [eax+14h]
		#mov     eax, [ecx+8]
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_28(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_28
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E139B80(self):
		#sub_6E139B80
		gadget = "8B44240483C028894130C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 28h
		#mov     [ecx+30h], eax
		#retn    4


  def test_gadget_sub_6E13A0E0(self):
		#sub_6E13A0E0
		gadget = "518B4424088B4C240CC7042400000000890859C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     ecx, [esp+4+arg_4]
		#mov     [esp+4+var_4], 0
		#mov     [eax], ecx
		#pop     ecx
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_32(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_32
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_34(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_34
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E1401B0(self):
		#sub_6E1401B0
		gadget = "8BC1C740040100000033C9C7400804000000C70050BD896E89480C89481089481489481889481C894820894824894828C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], 1
		#xor     ecx, ecx
		#mov     dword ptr [eax+8], 4
		#mov     dword ptr [eax], offset off_6E89BD50
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#retn


  def test_gadget_sub_6E140330(self):
		#sub_6E140330
		gadget = "8BC1C740040100000033C9C7400805000000C7008CBD896E89480C894810894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], 1
		#xor     ecx, ecx
		#mov     dword ptr [eax+8], 5
		#mov     dword ptr [eax], offset off_6E89BD8C
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_6E141140(self):
		#sub_6E141140
		gadget = "8B442404894114C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+14h], eax
		#retn    4


  def test_gadget_sub_6E142120(self):
		#sub_6E142120
		gadget = "33C089410489410889410C89411089411489411889411C89412089412489412889412C89413089413489413889413C89414089414889414CC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [ecx+4], eax
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#mov     [ecx+18h], eax
		#mov     [ecx+1Ch], eax
		#mov     [ecx+20h], eax
		#mov     [ecx+24h], eax
		#mov     [ecx+28h], eax
		#mov     [ecx+2Ch], eax
		#mov     [ecx+30h], eax
		#mov     [ecx+34h], eax
		#mov     [ecx+38h], eax
		#mov     [ecx+3Ch], eax
		#mov     [ecx+40h], eax
		#mov     [ecx+48h], eax
		#mov     [ecx+4Ch], eax
		#retn


  def test_gadget_sub_6E1421A0(self):
		#sub_6E1421A0
		gadget = "8BC133C9C7000100000089480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483C89484089484889484CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#retn


  def test_gadget_sub_6E142D40(self):
		#sub_6E142D40
		gadget = "8B153C26A56E8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482C8948308948348948388B0D3826A56E89483C895040C3"
		self.do(gadget)

		#mov     edx, dword_6EA5263C
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     ecx, dword_6EA52638
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], edx
		#retn


  def test_gadget_sub_6E144930(self):
		#sub_6E144930
		gadget = "8B44240483C00C894128C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 0Ch
		#mov     [ecx+28h], eax
		#retn    4


  def test_gadget_sub_6E1496C0(self):
		#sub_6E1496C0
		gadget = "518B44240833C98908890C2489480489480889480C59C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E14BAE0(self):
		#sub_6E14BAE0
		gadget = "8D818C000000C20400"
		self.do(gadget)

		#lea     eax, [ecx+8Ch]
		#retn    4


  def test_gadget_sub_6E14C890(self):
		#sub_6E14C890
		gadget = "C6411400C20400"
		self.do(gadget)

		#mov     byte ptr [ecx+14h], 0
		#retn    4


  def test_gadget_sub_6E14DB20(self):
		#sub_6E14DB20
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C894820894824C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#retn


  def test_gadget_sub_6E1501D0(self):
		#sub_6E1501D0
		gadget = "D9EE8BC133C9DD581066C700000188480289480889481889481CBA0000800089500489500CC74024200000008988280100008D502889502089882C01000089883001000089883401000089883801000089883C010000898840010000898844010000C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#fstp    qword ptr [eax+10h]
		#mov     word ptr [eax], 100h
		#mov     [eax+2], cl
		#mov     [eax+8], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     edx, 800000h
		#mov     [eax+4], edx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax+24h], 20h
		#mov     [eax+128h], ecx
		#lea     edx, [eax+28h]
		#mov     [eax+20h], edx
		#mov     [eax+12Ch], ecx
		#mov     [eax+130h], ecx
		#mov     [eax+134h], ecx
		#mov     [eax+138h], ecx
		#mov     [eax+13Ch], ecx
		#mov     [eax+140h], ecx
		#mov     [eax+144h], ecx
		#retn


  def test_gadget_sub_6E1514F0(self):
		#sub_6E1514F0
		gadget = "80893002000002C20800"
		self.do(gadget)

		#or      byte ptr [ecx+230h], 2
		#retn    8


  def test_gadget_sub_6E151910(self):
		#sub_6E151910
		gadget = "8B442408808930020000088B108991D80000008B50048991DC0000008B50088991E00000008B500C8991E40000008B50108991E80000008B40148981EC000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#or      byte ptr [ecx+230h], 8
		#mov     edx, [eax]
		#mov     [ecx+0D8h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+0DCh], edx
		#mov     edx, [eax+8]
		#mov     [ecx+0E0h], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+0E4h], edx
		#mov     edx, [eax+10h]
		#mov     [ecx+0E8h], edx
		#mov     eax, [eax+14h]
		#mov     [ecx+0ECh], eax
		#retn    8


  def test_gadget_sub_6E1519E0(self):
		#sub_6E1519E0
		gadget = "33C038816D0200000F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+26Dh], al
		#setz    al
		#retn


  def test_gadget_sub_6E151AA0(self):
		#sub_6E151AA0
		gadget = "33C038816C0200000F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+26Ch], al
		#setz    al
		#retn


  def test_gadget_sub_6E153CF0(self):
		#sub_6E153CF0
		gadget = "8B4424048981E0000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+0E0h], eax
		#retn    4


  def test_gadget_sub_6E155400(self):
		#sub_6E155400
		gadget = "8B44240489885002000089814C020000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [eax+250h], ecx
		#mov     [ecx+24Ch], eax
		#retn    4


  def test_gadget_sub_6E15FF20(self):
		#sub_6E15FF20
		gadget = "D9EE8BC1DD1033C9DD500866894838DD501066894860DD5018DD5020DD5028DD5030DD5040DD5048DD5050DD5858C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fst     qword ptr [eax]
		#xor     ecx, ecx
		#fst     qword ptr [eax+8]
		#mov     [eax+38h], cx
		#fst     qword ptr [eax+10h]
		#mov     [eax+60h], cx
		#fst     qword ptr [eax+18h]
		#fst     qword ptr [eax+20h]
		#fst     qword ptr [eax+28h]
		#fst     qword ptr [eax+30h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+48h]
		#fst     qword ptr [eax+50h]
		#fstp    qword ptr [eax+58h]
		#retn


  def test_gadget_sub_6E1600C0(self):
		#sub_6E1600C0
		gadget = "8D8188010000C3"
		self.do(gadget)

		#lea     eax, [ecx+188h]
		#retn


  def test_gadget_sub_6E1600D0(self):
		#sub_6E1600D0
		gadget = "8D8128020000C3"
		self.do(gadget)

		#lea     eax, [ecx+228h]
		#retn


  def test_gadget_sub_6E160170(self):
		#sub_6E160170
		gadget = "8D8124010000C3"
		self.do(gadget)

		#lea     eax, [ecx+124h]
		#retn


  def test_gadget_sub_6E167320(self):
		#sub_6E167320
		gadget = "8B4118C6400C01C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     byte ptr [eax+0Ch], 1
		#retn


  def test_gadget_sub_6E167570(self):
		#sub_6E167570
		gadget = "8BC18B4C2404890833C988480489480888480C89481089481489481889481CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], cl
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cl
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn    4


  def test_gadget_sub_6E167E50(self):
		#sub_6E167E50
		gadget = "D9053CD3896E8B442404D910D95804C20400"
		self.do(gadget)

		#fld     ds:flt_6E89D33C
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fstp    dword ptr [eax+4]
		#retn    4


  def test_gadget_nullsub_7(self):
		#nullsub_7
		gadget = "C21400"
		self.do(gadget)

		#retn    14h


  def test_gadget_sub_6E167FF0(self):
		#sub_6E167FF0
		gadget = "D9EE8B442404D910D95004D95008D9580CC20400"
		self.do(gadget)

		#fldz
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fst     dword ptr [eax+4]
		#fst     dword ptr [eax+8]
		#fstp    dword ptr [eax+0Ch]
		#retn    4


  def test_gadget__Java_com_sun_webkit_BackForwardList_bflItemGetIcon16(self):
		#_Java_com_sun_webkit_BackForwardList_bflItemGetIcon16
		gadget = "33C0C21000"
		self.do(gadget)

		#xor     eax, eax
		#retn    10h


  def test_gadget_sub_6E168020(self):
		#sub_6E168020
		gadget = "8B4C24088B118B4424048B49048910894804C20800"
		self.do(gadget)

		#mov     ecx, [esp+arg_4]
		#mov     edx, [ecx]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+4]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    8


  def test_gadget_sub_6E168040(self):
		#sub_6E168040
		gadget = "8B4C24088B4424048B1189108B51048950048B51088B490C89500889480CC20800"
		self.do(gadget)

		#mov     ecx, [esp+arg_4]
		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    8


  def test_gadget_sub_6E168090(self):
		#sub_6E168090
		gadget = "83C8FFC3"
		self.do(gadget)

		#or      eax, 0FFFFFFFFh
		#retn


  def test_gadget_sub_6E168620(self):
		#sub_6E168620
		gadget = "518B442408C7042400000000C7000000000059C22000"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    20h


  def test_gadget_sub_6E16A2C0(self):
		#sub_6E16A2C0
		gadget = "8A414CC3"
		self.do(gadget)

		#mov     al, [ecx+4Ch]
		#retn


  def test_gadget_sub_6E16A350(self):
		#sub_6E16A350
		gadget = "33C083792C080F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx+2Ch], 8
		#setz    al
		#retn


  def test_gadget_sub_6E16A360(self):
		#sub_6E16A360
		gadget = "C7412C08000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+2Ch], 8
		#retn


  def test_gadget_sub_6E176270(self):
		#sub_6E176270
		gadget = "33C08339020F9DC0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx], 2
		#setnl   al
		#retn


  def test_gadget_unknown_libname_5(self):
		#unknown_libname_5
		gadget = "33C039010F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx], eax
		#setz    al
		#retn


  def test_gadget_sub_6E1762B0(self):
		#sub_6E1762B0
		gadget = "33C08339040F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx], 4
		#setz    al
		#retn


  def test_gadget_sub_6E176C60(self):
		#sub_6E176C60
		gadget = "8BC18B4C2404890833C989480489480889480C66C740100100894814C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     word ptr [eax+10h], 1
		#mov     [eax+14h], ecx
		#retn    4


  def test_gadget_sub_6E17D560(self):
		#sub_6E17D560
		gadget = "8A4140C20400"
		self.do(gadget)

		#mov     al, [ecx+40h]
		#retn    4


  def test_gadget_sub_6E17F2D0(self):
		#sub_6E17F2D0
		gadget = "DD4138C3"
		self.do(gadget)

		#fld     qword ptr [ecx+38h]
		#retn


  def test_gadget_sub_6E17F2E0(self):
		#sub_6E17F2E0
		gadget = "A14870A66E40A34870A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67048
		#inc     eax
		#mov     dword_6EA67048, eax
		#retn


  def test_gadget_sub_6E181900(self):
		#sub_6E181900
		gadget = "8B4108837820000F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#cmp     dword ptr [eax+20h], 0
		#setnz   al
		#retn


  def test_gadget_sub_6E1819E0(self):
		#sub_6E1819E0
		gadget = "8BC18B4C2404C7400401000000C70074DF896E894808C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     dword ptr [eax], offset off_6E89DF74
		#mov     [eax+8], ecx
		#retn    4


  def test_gadget_sub_6E183D00(self):
		#sub_6E183D00
		gadget = "FF4158C3"
		self.do(gadget)

		#inc     dword ptr [ecx+58h]
		#retn


  def test_gadget_sub_6E183E90(self):
		#sub_6E183E90
		gadget = "8A44240488415CC20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+5Ch], al
		#retn    4


  def test_gadget_sub_6E184E40(self):
		#sub_6E184E40
		gadget = "8BC18B4C2404C60000894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     byte ptr [eax], 0
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E184E50(self):
		#sub_6E184E50
		gadget = "C60100C3"
		self.do(gadget)

		#mov     byte ptr [ecx], 0
		#retn


  def test_gadget_sub_6E186AA0(self):
		#sub_6E186AA0
		gadget = "8B81D0020000C3"
		self.do(gadget)

		#mov     eax, [ecx+2D0h]
		#retn


  def test_gadget_sub_6E189290(self):
		#sub_6E189290
		gadget = "8BC1BA0100000033C9891089500489480889500CC740100200000089501489481889481C894820C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     edx, 1
		#xor     ecx, ecx
		#mov     [eax], edx
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax+10h], 2
		#mov     [eax+14h], edx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn


  def test_gadget_sub_6E189560(self):
		#sub_6E189560
		gadget = "8B4144DD4020C3"
		self.do(gadget)

		#mov     eax, [ecx+44h]
		#fld     qword ptr [eax+20h]
		#retn


  def test_gadget_sub_6E189570(self):
		#sub_6E189570
		gadget = "8B4144F6402C30B8000000000F94C0C3"
		self.do(gadget)

		#mov     eax, [ecx+44h]
		#test    byte ptr [eax+2Ch], 30h
		#mov     eax, 0
		#setz    al
		#retn


  def test_gadget_sub_6E18A540(self):
		#sub_6E18A540
		gadget = "8B018A80D9000000C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     al, [eax+0D9h]
		#retn


  def test_gadget_sub_6E18D650(self):
		#sub_6E18D650
		gadget = "8B5424048BC133C9C7000100000089500489480889480C89481089481489481889481C89482089482489482889482C8948308948348948388A8AD900000088483CC20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     cl, [edx+0D9h]
		#mov     [eax+3Ch], cl
		#retn    4


  def test_gadget_sub_6E1986B0(self):
		#sub_6E1986B0
		gadget = "8B495433C03B4C24040F94C0C20400"
		self.do(gadget)

		#mov     ecx, [ecx+54h]
		#xor     eax, eax
		#cmp     ecx, [esp+arg_0]
		#setz    al
		#retn    4


  def test_gadget_sub_6E19A4B0(self):
		#sub_6E19A4B0
		gadget = "8B4138C3"
		self.do(gadget)

		#mov     eax, [ecx+38h]
		#retn


  def test_gadget_sub_6E19A4C0(self):
		#sub_6E19A4C0
		gadget = "33C083793C020F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx+3Ch], 2
		#setz    al
		#retn


  def test_gadget_sub_6E19B130(self):
		#sub_6E19B130
		gadget = "D9EE8B442404D910D95004D95008D9580CC21000"
		self.do(gadget)

		#fldz
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fst     dword ptr [eax+4]
		#fst     dword ptr [eax+8]
		#fstp    dword ptr [eax+0Ch]
		#retn    10h


  def test_gadget_sub_6E19DC00(self):
		#sub_6E19DC00
		gadget = "8A442404884104C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+4], al
		#retn    4


  def test_gadget_sub_6E1A8E00(self):
		#sub_6E1A8E00
		gadget = "8BC18B4C2404890833C988480489480889480C894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], cl
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E1ADEA0(self):
		#sub_6E1ADEA0
		gadget = "8BC1C70000000000C7400401000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 1
		#retn


  def test_gadget_sub_6E1B0A70(self):
		#sub_6E1B0A70
		gadget = "8BC1C3"
		self.do(gadget)

		#mov     eax, ecx
		#retn


  def test_gadget_unknown_libname_6(self):
		#unknown_libname_6
		gadget = "33C03941100F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+10h], eax
		#setz    al
		#retn


  def test_gadget_sub_6E1BB7F0(self):
		#sub_6E1BB7F0
		gadget = "8B91200100008B4424048B89240100008910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+120h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+124h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E1BB990(self):
		#sub_6E1BB990
		gadget = "C781DC00000000000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+0DCh], 0
		#retn


  def test_gadget_sub_6E1C3A80(self):
		#sub_6E1C3A80
		gadget = "8A4148C3"
		self.do(gadget)

		#mov     al, [ecx+48h]
		#retn


  def test_gadget_sub_6E1C3A90(self):
		#sub_6E1C3A90
		gadget = "668B414AC3"
		self.do(gadget)

		#mov     ax, [ecx+4Ah]
		#retn


  def test_gadget_sub_6E1C3AA0(self):
		#sub_6E1C3AA0
		gadget = "8D81CC000000C3"
		self.do(gadget)

		#lea     eax, [ecx+0CCh]
		#retn


  def test_gadget_sub_6E1CA440(self):
		#sub_6E1CA440
		gadget = "FF01C3"
		self.do(gadget)

		#inc     dword ptr [ecx]
		#retn


  def test_gadget_sub_6E1CB4C0(self):
		#sub_6E1CB4C0
		gadget = "8B442404DB00DC0D10E1846ED95C2404D9442404D8642408D95C2404D9442404C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#fsub    [esp+arg_4]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn


  def test_gadget_sub_6E1CB5D0(self):
		#sub_6E1CB5D0
		gadget = "8B4424048B108951688B500489516C8B50088951708B400C894174C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+68h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+6Ch], edx
		#mov     edx, [eax+8]
		#mov     [ecx+70h], edx
		#mov     eax, [eax+0Ch]
		#mov     [ecx+74h], eax
		#retn    4


  def test_gadget_sub_6E1CB7D0(self):
		#sub_6E1CB7D0
		gadget = "33C03881790100000F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+179h], al
		#setz    al
		#retn


  def test_gadget_sub_6E1CB7E0(self):
		#sub_6E1CB7E0
		gadget = "8B4424048981BC000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+0BCh], eax
		#retn    4


  def test_gadget_sub_6E1CB7F0(self):
		#sub_6E1CB7F0
		gadget = "8B4424048981C0000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+0C0h], eax
		#retn    4


  def test_gadget_sub_6E1CB9E0(self):
		#sub_6E1CB9E0
		gadget = "8A817A010000C3"
		self.do(gadget)

		#mov     al, [ecx+17Ah]
		#retn


  def test_gadget_sub_6E1CB9F0(self):
		#sub_6E1CB9F0
		gadget = "8A44240488817A010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+17Ah], al
		#retn    4


  def test_gadget_sub_6E1CBA00(self):
		#sub_6E1CBA00
		gadget = "8B917C0100008B4424048B89800100008910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+17Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+180h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E1CBAD0(self):
		#sub_6E1CBAD0
		gadget = "8A81B4010000C3"
		self.do(gadget)

		#mov     al, [ecx+1B4h]
		#retn


  def test_gadget_sub_6E1CBAE0(self):
		#sub_6E1CBAE0
		gadget = "8B442404898144020000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+244h], eax
		#retn    4


  def test_gadget_sub_6E1CBAF0(self):
		#sub_6E1CBAF0
		gadget = "8B8144020000C3"
		self.do(gadget)

		#mov     eax, [ecx+244h]
		#retn


  def test_gadget_sub_6E1CBB00(self):
		#sub_6E1CBB00
		gadget = "8A8148020000C3"
		self.do(gadget)

		#mov     al, [ecx+248h]
		#retn


  def test_gadget_sub_6E1CBB70(self):
		#sub_6E1CBB70
		gadget = "8B442404098184020000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#or      [ecx+284h], eax
		#retn    4


  def test_gadget_sub_6E1CD400(self):
		#sub_6E1CD400
		gadget = "8B81A000000033C9837868020F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx+0A0h]
		#xor     ecx, ecx
		#cmp     dword ptr [eax+68h], 2
		#setnz   al
		#retn


  def test_gadget_sub_6E1D1150(self):
		#sub_6E1D1150
		gadget = "8B8154020000C3"
		self.do(gadget)

		#mov     eax, [ecx+254h]
		#retn


  def test_gadget_sub_6E1D1160(self):
		#sub_6E1D1160
		gadget = "8B8158020000C3"
		self.do(gadget)

		#mov     eax, [ecx+258h]
		#retn


  def test_gadget_sub_6E1D5060(self):
		#sub_6E1D5060
		gadget = "8B4424048901C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx], eax
		#retn    4


  def test_gadget_sub_6E1D5070(self):
		#sub_6E1D5070
		gadget = "8B4424048B54240889410889510CC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], edx
		#retn    8


  def test_gadget_sub_6E1D5090(self):
		#sub_6E1D5090
		gadget = "8BC133C9C70000005000894804C740080000500089480CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 500000h
		#mov     [eax+4], ecx
		#mov     dword ptr [eax+8], 500000h
		#mov     [eax+0Ch], ecx
		#retn


  def test_gadget_sub_6E1D7830(self):
		#sub_6E1D7830
		gadget = "C7011C048A6EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E8A041C
		#retn


  def test_gadget_sub_6E1D7CC0(self):
		#sub_6E1D7CC0
		gadget = "8A4160C3"
		self.do(gadget)

		#mov     al, [ecx+60h]
		#retn


  def test_gadget_sub_6E1D7CD0(self):
		#sub_6E1D7CD0
		gadget = "C6416001C3"
		self.do(gadget)

		#mov     byte ptr [ecx+60h], 1
		#retn


  def test_gadget_sub_6E1D7CE0(self):
		#sub_6E1D7CE0
		gadget = "8A4168C3"
		self.do(gadget)

		#mov     al, [ecx+68h]
		#retn


  def test_gadget_GetCompletionListEventUMSSchedulerProxydetailsConcurrencyQBEPAXXZ(self):
		#GetCompletionListEventUMSSchedulerProxydetailsConcurrencyQBEPAXXZ
		gadget = "8B81DC000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0DCh]
		#retn


  def test_gadget_sub_6E1D7DE0(self):
		#sub_6E1D7DE0
		gadget = "8B41388B4004C3"
		self.do(gadget)

		#mov     eax, [ecx+38h]
		#mov     eax, [eax+4]
		#retn


  def test_gadget_sub_6E1D8150(self):
		#sub_6E1D8150
		gadget = "33C03981980400000F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+498h], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E1D8160(self):
		#sub_6E1D8160
		gadget = "33C03981AC0400000F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+4ACh], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E1D8730(self):
		#sub_6E1D8730
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C894820C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn


  def test_gadget_0facetlocalestdIAEIZ_1(self):
		#0facetlocalestdIAEIZ_1
		gadget = "8BC18B4C2404C700FC048A6E894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8A04FC
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E1DC390(self):
		#sub_6E1DC390
		gadget = "FF056C77A66EC3"
		self.do(gadget)

		#inc     dword_6EA6776C
		#retn


  def test_gadget_sub_6E1DC3A0(self):
		#sub_6E1DC3A0
		gadget = "FF0D6C77A66EC3"
		self.do(gadget)

		#dec     dword_6EA6776C
		#retn


  def test_gadget_sub_6E1DC3B0(self):
		#sub_6E1DC3B0
		gadget = "A07077A66EC3"
		self.do(gadget)

		#mov     al, byte_6EA67770
		#retn


  def test_gadget_sub_6E1DDE80(self):
		#sub_6E1DDE80
		gadget = "8D410CC3"
		self.do(gadget)

		#lea     eax, [ecx+0Ch]
		#retn


  def test_gadget_sub_6E1DE050(self):
		#sub_6E1DE050
		gadget = "FF4108C3"
		self.do(gadget)

		#inc     dword ptr [ecx+8]
		#retn


  def test_gadget_sub_6E1DEE20(self):
		#sub_6E1DEE20
		gadget = "8BC18B4C2404890833C989480489480889480C884810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], cl
		#retn    4


  def test_gadget_sub_6E1E2480(self):
		#sub_6E1E2480
		gadget = "8B4424088B54240CC21400"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     edx, [esp+arg_8]
		#retn    14h


  def test_gadget_sub_6E1E2490(self):
		#sub_6E1E2490
		gadget = "C7410C00000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+0Ch], 0
		#retn


  def test_gadget_sub_6E1E24B0(self):
		#sub_6E1E24B0
		gadget = "8B0D884DA56E568B358C4DA56E8BC183C1018BD683D60089358C4DA56E890D884DA56E5EC3"
		self.do(gadget)

		#mov     ecx, dword_6EA54D88
		#push    esi
		#mov     esi, dword_6EA54D8C
		#mov     eax, ecx
		#add     ecx, 1
		#mov     edx, esi
		#adc     esi, 0
		#mov     dword_6EA54D8C, esi
		#mov     dword_6EA54D88, ecx
		#pop     esi
		#retn


  def test_gadget_sub_6E1E3220(self):
		#sub_6E1E3220
		gadget = "C6411901C3"
		self.do(gadget)

		#mov     byte ptr [ecx+19h], 1
		#retn


  def test_gadget_sub_6E1E3230(self):
		#sub_6E1E3230
		gadget = "C6411701C3"
		self.do(gadget)

		#mov     byte ptr [ecx+17h], 1
		#retn


  def test_gadget_sub_6E1E3240(self):
		#sub_6E1E3240
		gadget = "C6412001C3"
		self.do(gadget)

		#mov     byte ptr [ecx+20h], 1
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_37(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_37
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E1E4350(self):
		#sub_6E1E4350
		gadget = "51C7042400000000C7000000000059C3"
		self.do(gadget)

		#push    ecx
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn


  def test_gadget_sub_6E1E5020(self):
		#sub_6E1E5020
		gadget = "8B442404A3D04DA56EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword_6EA54DD0, eax
		#retn


  def test_gadget___uncaught_exceptionYA_NXZ(self):
		#__uncaught_exceptionYA_NXZ
		gadget = "33C03905D04DA56E0F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword_6EA54DD0, eax
		#setnz   al
		#retn


  def test_gadget_sub_6E1E5040(self):
		#sub_6E1E5040
		gadget = "33C0833DD04DA56E020F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword_6EA54DD0, 2
		#setnz   al
		#retn


  def test_gadget_sub_6E1E58C0(self):
		#sub_6E1E58C0
		gadget = "8A442404C0E0043281420100002410308142010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 4
		#xor     al, [ecx+142h]
		#and     al, 10h
		#xor     [ecx+142h], al
		#retn    4


  def test_gadget_sub_6E1E58E0(self):
		#sub_6E1E58E0
		gadget = "DD05D84DA56EC3"
		self.do(gadget)

		#fld     dbl_6EA54DD8
		#retn


  def test_gadget_sub_6E1E5920(self):
		#sub_6E1E5920
		gadget = "DD05A877A66EC3"
		self.do(gadget)

		#fld     dbl_6EA677A8
		#retn


  def test_gadget_sub_6E1E5940(self):
		#sub_6E1E5940
		gadget = "8B814401000083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+144h]
		#and     eax, 1
		#retn


  def test_gadget_sub_6E1E5970(self):
		#sub_6E1E5970
		gadget = "8A442404A2B077A66EC3"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     byte_6EA677B0, al
		#retn


  def test_gadget_sub_6E1E5980(self):
		#sub_6E1E5980
		gadget = "A0B077A66EC3"
		self.do(gadget)

		#mov     al, byte_6EA677B0
		#retn


  def test_gadget_sub_6E1E5990(self):
		#sub_6E1E5990
		gadget = "8A442404A2B177A66EC3"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     byte_6EA677B1, al
		#retn


  def test_gadget_sub_6E1E59A0(self):
		#sub_6E1E59A0
		gadget = "A0B277A66EC3"
		self.do(gadget)

		#mov     al, byte_6EA677B2
		#retn


  def test_gadget_sub_6E1E6740(self):
		#sub_6E1E6740
		gadget = "8B442408DB00DC0D10E1846ED95C2408D9442408D8442404D95C2408D9442408C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_4]
		#fld     [esp+arg_4]
		#fadd    [esp+arg_0]
		#fstp    [esp+arg_4]
		#fld     [esp+arg_4]
		#retn


  def test_gadget_sub_6E1E9E10(self):
		#sub_6E1E9E10
		gadget = "A0BC77A66EC3"
		self.do(gadget)

		#mov     al, byte_6EA677BC
		#retn


  def test_gadget_sub_6E1E9E80(self):
		#sub_6E1E9E80
		gadget = "32C0C20800"
		self.do(gadget)

		#xor     al, al
		#retn    8


  def test_gadget_sub_6E1E9E90(self):
		#sub_6E1E9E90
		gadget = "B800000010C3"
		self.do(gadget)

		#mov     eax, 10000000h
		#retn


  def test_gadget_sub_6E1E9EA0(self):
		#sub_6E1E9EA0
		gadget = "8B44240433C9890889480489480889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E1E9F50(self):
		#sub_6E1E9F50
		gadget = "518B442408C7042400000000C7000000000059C20C00"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    0Ch


  def test_gadget_sub_6E1EC3E0(self):
		#sub_6E1EC3E0
		gadget = "8A442404A25078A66EC3"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     byte_6EA67850, al
		#retn


  def test_gadget_sub_6E1EC420(self):
		#sub_6E1EC420
		gadget = "A05078A66EC20400"
		self.do(gadget)

		#mov     al, byte_6EA67850
		#retn    4


  def test_gadget_sub_6E1F1E90(self):
		#sub_6E1F1E90
		gadget = "DD4110C3"
		self.do(gadget)

		#fld     qword ptr [ecx+10h]
		#retn


  def test_gadget_sub_6E1F1EA0(self):
		#sub_6E1F1EA0
		gadget = "8A4108C3"
		self.do(gadget)

		#mov     al, [ecx+8]
		#retn


  def test_gadget_sub_6E1F29D0(self):
		#sub_6E1F29D0
		gadget = "518B41188B49148D8440EAE8FFFF8D1481891424DB042459C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [ecx+18h]
		#mov     ecx, [ecx+14h]
		#lea     eax, [eax+eax*2-1716h]
		#lea     edx, [ecx+eax*4]
		#mov     [esp+4+var_4], edx
		#fild    [esp+4+var_4]
		#pop     ecx
		#retn


  def test_gadget_sub_6E1F42E0(self):
		#sub_6E1F42E0
		gadget = "8BC18B4C24048B1189108B51048950048B51088950088B510C89500C8B51108950108B4914894814C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+10h]
		#mov     [eax+10h], edx
		#mov     ecx, [ecx+14h]
		#mov     [eax+14h], ecx
		#retn    4


  def test_gadget_sub_6E1F4390(self):
		#sub_6E1F4390
		gadget = "8B4424048B1189108B51048950048B51088950088B510C8B491489500C894814C7401000000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     ecx, [ecx+14h]
		#mov     [eax+0Ch], edx
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+10h], 0
		#retn    4


  def test_gadget_sub_6E1F43C0(self):
		#sub_6E1F43C0
		gadget = "83EC1833C033C966894424088B44241C89088B4C24085633D28950048B542418578B7C242833F689480889700C8978105F8950145E83C418C3"
		self.do(gadget)

		#sub     esp, 18h
		#xor     eax, eax
		#xor     ecx, ecx
		#mov     word ptr [esp+18h+var_10], ax
		#mov     eax, [esp+18h+arg_0]
		#mov     [eax], ecx
		#mov     ecx, [esp+18h+var_10]
		#push    esi
		#xor     edx, edx
		#mov     [eax+4], edx
		#mov     edx, [esp+1Ch+var_4]
		#push    edi
		#mov     edi, [esp+20h+arg_4]
		#xor     esi, esi
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], esi
		#mov     [eax+10h], edi
		#pop     edi
		#mov     [eax+14h], edx
		#pop     esi
		#add     esp, 18h
		#retn


  def test_gadget_sub_6E1F4400(self):
		#sub_6E1F4400
		gadget = "83EC1833C033C956668944240C8B442420890833D28D71028B4C240C8950048B5424185789480833FF89700C8978105F8950145E83C418C3"
		self.do(gadget)

		#sub     esp, 18h
		#xor     eax, eax
		#xor     ecx, ecx
		#push    esi
		#mov     word ptr [esp+1Ch+var_10], ax
		#mov     eax, [esp+1Ch+arg_0]
		#mov     [eax], ecx
		#xor     edx, edx
		#lea     esi, [ecx+2]
		#mov     ecx, [esp+1Ch+var_10]
		#mov     [eax+4], edx
		#mov     edx, [esp+1Ch+var_4]
		#push    edi
		#mov     [eax+8], ecx
		#xor     edi, edi
		#mov     [eax+0Ch], esi
		#mov     [eax+10h], edi
		#pop     edi
		#mov     [eax+14h], edx
		#pop     esi
		#add     esp, 18h
		#retn


  def test_gadget_sub_6E1F61B0(self):
		#sub_6E1F61B0
		gadget = "8BC18B4C24088B1189108B49048948048B4C240C8B118950088B49048B54240489480C8B4C24108950108B542414894814895018C21400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx]
		#mov     [eax+8], edx
		#mov     ecx, [ecx+4]
		#mov     edx, [esp+arg_0]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+10h], edx
		#mov     edx, [esp+arg_10]
		#mov     [eax+14h], ecx
		#mov     [eax+18h], edx
		#retn    14h


  def test_gadget_sub_6E1F6390(self):
		#sub_6E1F6390
		gadget = "C7410400000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+4], 0
		#retn


  def test_gadget_sub_6E1F69D0(self):
		#sub_6E1F69D0
		gadget = "8B511C8BCAC1E907B810000000D3E0F6C220B9000000000F95C18D0C8D040000000BC1F6C210BA000000000F95C2420BC2C3"
		self.do(gadget)

		#mov     edx, [ecx+1Ch]
		#mov     ecx, edx
		#shr     ecx, 7
		#mov     eax, 10h
		#shl     eax, cl
		#test    dl, 20h
		#mov     ecx, 0
		#setnz   cl
		#lea     ecx, ds:4[ecx*4]
		#or      eax, ecx
		#test    dl, 10h
		#mov     edx, 0
		#setnz   dl
		#inc     edx
		#or      eax, edx
		#retn


  def test_gadget_sub_6E1F7920(self):
		#sub_6E1F7920
		gadget = "8BC133C9C7000100000089480489480889480CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn


  def test_gadget_GetPhysicalContextExternalContextBasedetailsConcurrencyQAEPAXXZ(self):
		#GetPhysicalContextExternalContextBasedetailsConcurrencyQAEPAXXZ
		gadget = "8B8188000000C3"
		self.do(gadget)

		#mov     eax, [ecx+88h]
		#retn


  def test_gadget_sub_6E1F7C40(self):
		#sub_6E1F7C40
		gadget = "8B91800000008B4424048B89840000008910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+80h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+84h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E1F8E30(self):
		#sub_6E1F8E30
		gadget = "8B4424040FB64802568B74240C0FB656022BCA0FB650010FAFC98B00570FB67E018B3625FF00000081E6FF0000002BC62BD70FAFC00FAFD203C25F03C15EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#movzx   ecx, byte ptr [eax+2]
		#push    esi
		#mov     esi, [esp+4+arg_4]
		#movzx   edx, byte ptr [esi+2]
		#sub     ecx, edx
		#movzx   edx, byte ptr [eax+1]
		#imul    ecx, ecx
		#mov     eax, [eax]
		#push    edi
		#movzx   edi, byte ptr [esi+1]
		#mov     esi, [esi]
		#and     eax, 0FFh
		#and     esi, 0FFh
		#sub     eax, esi
		#sub     edx, edi
		#imul    eax, eax
		#imul    edx, edx
		#add     eax, edx
		#pop     edi
		#add     eax, ecx
		#pop     esi
		#retn


  def test_gadget_sub_6E1F8E70(self):
		#sub_6E1F8E70
		gadget = "510FB641028904248B542408DB0424DD056070806EDCF9D9C9D91A0FB64101894424088B54240CDB442408D8F1D91A8B0125FF00000089442408DB4424088B542410D8F1D91A0FB64103894424088B4C2414DB442408DEF1D91959C21000"
		self.do(gadget)

		#push    ecx
		#movzx   eax, byte ptr [ecx+2]
		#mov     [esp+4+var_4], eax
		#mov     edx, [esp+4+arg_0]
		#fild    [esp+4+var_4]
		#fld     ds:dbl_6E807060
		#fdiv    st(1), st
		#fxch    st(1)
		#fstp    dword ptr [edx]
		#movzx   eax, byte ptr [ecx+1]
		#mov     [esp+4+arg_0], eax
		#mov     edx, [esp+4+arg_4]
		#fild    [esp+4+arg_0]
		#fdiv    st, st(1)
		#fstp    dword ptr [edx]
		#mov     eax, [ecx]
		#and     eax, 0FFh
		#mov     [esp+4+arg_0], eax
		#fild    [esp+4+arg_0]
		#mov     edx, [esp+4+arg_8]
		#fdiv    st, st(1)
		#fstp    dword ptr [edx]
		#movzx   eax, byte ptr [ecx+3]
		#mov     [esp+4+arg_0], eax
		#mov     ecx, [esp+4+arg_C]
		#fild    [esp+4+arg_0]
		#fdivrp  st(1), st
		#fstp    dword ptr [ecx]
		#pop     ecx
		#retn    10h


  def test_gadget_sub_6E1FA3D0(self):
		#sub_6E1FA3D0
		gadget = "8B51248B4424048B49288910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+24h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+28h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E1FA880(self):
		#sub_6E1FA880
		gadget = "8BC18B4C24048B1189542404DB442404DD0510E1846EDCC9D9C9D9188B4904894C2404DA4C2404D95804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [esp+arg_0], edx
		#fild    [esp+arg_0]
		#fld     ds:dbl_6E84E110
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    dword ptr [eax]
		#mov     ecx, [ecx+4]
		#mov     [esp+arg_0], ecx
		#fimul   [esp+arg_0]
		#fstp    dword ptr [eax+4]
		#retn    4


  def test_gadget_sub_6E1FA8D0(self):
		#sub_6E1FA8D0
		gadget = "8B4424048B1089542404DB442404DD0510E1846EDCC9D9C9D95C2404D9442404D801D9198B400489442404DA4C2404D95C2404D9442404D84104D95904C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [esp+arg_0], edx
		#fild    [esp+arg_0]
		#fld     ds:dbl_6E84E110
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#fadd    dword ptr [ecx]
		#fstp    dword ptr [ecx]
		#mov     eax, [eax+4]
		#mov     [esp+arg_0], eax
		#fimul   [esp+arg_0]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#fadd    dword ptr [ecx+4]
		#fstp    dword ptr [ecx+4]
		#retn    4


  def test_gadget_sub_6E1FA910(self):
		#sub_6E1FA910
		gadget = "8B442404DD442408D918DD442410D95804C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     [esp+arg_4]
		#fstp    dword ptr [eax]
		#fld     [esp+arg_C]
		#fstp    dword ptr [eax+4]
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_27(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_27
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E1FD370(self):
		#sub_6E1FD370
		gadget = "D901D9442404D9C0DECAD9C9D919D94104D9442408D9C0DECAD9C9D95904D94108DECAD9C9D95908D8490CD9590CC20800"
		self.do(gadget)

		#fld     dword ptr [ecx]
		#fld     [esp+arg_0]
		#fld     st
		#fmulp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [ecx]
		#fld     dword ptr [ecx+4]
		#fld     [esp+arg_4]
		#fld     st
		#fmulp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [ecx+4]
		#fld     dword ptr [ecx+8]
		#fmulp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [ecx+8]
		#fmul    dword ptr [ecx+0Ch]
		#fstp    dword ptr [ecx+0Ch]
		#retn    8


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_44(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_44
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E1FDC20(self):
		#sub_6E1FDC20
		gadget = "8BC18B4C2404DB01D918DB4104D95804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#fild    dword ptr [ecx]
		#fstp    dword ptr [eax]
		#fild    dword ptr [ecx+4]
		#fstp    dword ptr [eax+4]
		#retn    4


  def test_gadget_sub_6E1FDD10(self):
		#sub_6E1FDD10
		gadget = "C7016C11856EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E85116C
		#retn


  def test_gadget_sub_6E1FEC40(self):
		#sub_6E1FEC40
		gadget = "8B442404C70000000000C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#retn    10h


  def test_gadget_sub_6E200290(self):
		#sub_6E200290
		gadget = "66A1AC78A66EC3"
		self.do(gadget)

		#mov     ax, word_6EA678AC
		#retn


  def test_gadget_sub_6E2008D0(self):
		#sub_6E2008D0
		gadget = "6AFF68297B796E64A1000000005051A1F44AA66E33C4508D44240864A30000000033C9894C24048B44241889088948048948086689480C8948108948148948188B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E797B29
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#xor     ecx, ecx
		#mov     [esp+14h+var_10], ecx
		#mov     eax, [esp+14h+arg_0]
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E203FD0(self):
		#sub_6E203FD0
		gadget = "D9EE8BC18D4808890856BA0008000089500433C98988082000008DB01420000089B00C2000008990102000008988144000008DB02040000089B01840000089901C400000898820800000D99024800000D998288000005EC3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#lea     ecx, [eax+8]
		#mov     [eax], ecx
		#push    esi
		#mov     edx, 800h
		#mov     [eax+4], edx
		#xor     ecx, ecx
		#mov     [eax+2008h], ecx
		#lea     esi, [eax+2014h]
		#mov     [eax+200Ch], esi
		#mov     [eax+2010h], edx
		#mov     [eax+4014h], ecx
		#lea     esi, [eax+4020h]
		#mov     [eax+4018h], esi
		#mov     [eax+401Ch], edx
		#mov     [eax+8020h], ecx
		#fst     dword ptr [eax+8024h]
		#fstp    dword ptr [eax+8028h]
		#pop     esi
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_45(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_45
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E2088B0(self):
		#sub_6E2088B0
		gadget = "D94120C3"
		self.do(gadget)

		#fld     dword ptr [ecx+20h]
		#retn


  def test_gadget_sub_6E2088C0(self):
		#sub_6E2088C0
		gadget = "8B512C8B4424048B49308910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+2Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+30h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E2088E0(self):
		#sub_6E2088E0
		gadget = "8B414CC3"
		self.do(gadget)

		#mov     eax, [ecx+4Ch]
		#retn


  def test_gadget_sub_6E2088F0(self):
		#sub_6E2088F0
		gadget = "8B4148C3"
		self.do(gadget)

		#mov     eax, [ecx+48h]
		#retn


  def test_gadget_sub_6E208900(self):
		#sub_6E208900
		gadget = "8B51348B4424048B49388910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+34h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+38h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E208920(self):
		#sub_6E208920
		gadget = "8B4150C3"
		self.do(gadget)

		#mov     eax, [ecx+50h]
		#retn


  def test_gadget_sub_6E208950(self):
		#sub_6E208950
		gadget = "8A41602401C3"
		self.do(gadget)

		#mov     al, [ecx+60h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E208960(self):
		#sub_6E208960
		gadget = "8A44240402C002C03241602404304160C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#xor     al, [ecx+60h]
		#and     al, 4
		#xor     [ecx+60h], al
		#retn    4


  def test_gadget_sub_6E208980(self):
		#sub_6E208980
		gadget = "8A4160C0E8022401C3"
		self.do(gadget)

		#mov     al, [ecx+60h]
		#shr     al, 2
		#and     al, 1
		#retn


  def test_gadget_sub_6E208990(self):
		#sub_6E208990
		gadget = "8A442404C0E0043241602410304160C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 4
		#xor     al, [ecx+60h]
		#and     al, 10h
		#xor     [ecx+60h], al
		#retn    4


  def test_gadget_sub_6E2089B0(self):
		#sub_6E2089B0
		gadget = "8A4160C0E8042401C3"
		self.do(gadget)

		#mov     al, [ecx+60h]
		#shr     al, 4
		#and     al, 1
		#retn


  def test_gadget_sub_6E2089F0(self):
		#sub_6E2089F0
		gadget = "8A81AC000000C3"
		self.do(gadget)

		#mov     al, [ecx+0ACh]
		#retn


  def test_gadget_sub_6E208A00(self):
		#sub_6E208A00
		gadget = "8A4160C0E8032401C3"
		self.do(gadget)

		#mov     al, [ecx+60h]
		#shr     al, 3
		#and     al, 1
		#retn


  def test_gadget_sub_6E208ED0(self):
		#sub_6E208ED0
		gadget = "8B4158C3"
		self.do(gadget)

		#mov     eax, [ecx+58h]
		#retn


  def test_gadget_sub_6E208FF0(self):
		#sub_6E208FF0
		gadget = "8A4424048AD002D202D202D23251608881AC00000080E208305160C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     dl, al
		#add     dl, dl
		#add     dl, dl
		#add     dl, dl
		#xor     dl, [ecx+60h]
		#mov     [ecx+0ACh], al
		#and     dl, 8
		#xor     [ecx+60h], dl
		#retn    4


  def test_gadget_sub_6E20A960(self):
		#sub_6E20A960
		gadget = "8BC133C9890889480489480889480C89481089481489481889481CBA0D00000089502089502489502889482C89503089483489483888483C894840894844C640480189484C89485089485489485889485C89486089486489486889486C88487089487489487889487C8988800000008D908C000000899084000000C78088000000080000008988CC000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     edx, 0Dh
		#mov     [eax+20h], edx
		#mov     [eax+24h], edx
		#mov     [eax+28h], edx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], edx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], cl
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     byte ptr [eax+48h], 1
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], ecx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+68h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], cl
		#mov     [eax+74h], ecx
		#mov     [eax+78h], ecx
		#mov     [eax+7Ch], ecx
		#mov     [eax+80h], ecx
		#lea     edx, [eax+8Ch]
		#mov     [eax+84h], edx
		#mov     dword ptr [eax+88h], 8
		#mov     [eax+0CCh], ecx
		#retn


  def test_gadget_sub_6E20C0D0(self):
		#sub_6E20C0D0
		gadget = "8B4424048B108991400100008B4004898144010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+140h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+144h], eax
		#retn    4


  def test_gadget_sub_6E20C210(self):
		#sub_6E20C210
		gadget = "D9442404D9994C010000C20400"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+14Ch]
		#retn    4


  def test_gadget_sub_6E20D2C0(self):
		#sub_6E20D2C0
		gadget = "8B442404898178010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+178h], eax
		#retn    4


  def test_gadget_sub_6E20D2D0(self):
		#sub_6E20D2D0
		gadget = "8B4424048B108951188B400489411CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+18h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+1Ch], eax
		#retn    4


  def test_gadget_sub_6E20D2F0(self):
		#sub_6E20D2F0
		gadget = "8B4424048B108951208B50048951248B4008894128C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+20h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+24h], edx
		#mov     eax, [eax+8]
		#mov     [ecx+28h], eax
		#retn    4


  def test_gadget_sub_6E20D310(self):
		#sub_6E20D310
		gadget = "8B4424048B108951348B4004894138C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+34h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+38h], eax
		#retn    4


  def test_gadget_sub_6E20D330(self):
		#sub_6E20D330
		gadget = "8A44240402C032815C010000240230815C010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#xor     al, [ecx+15Ch]
		#and     al, 2
		#xor     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D350(self):
		#sub_6E20D350
		gadget = "8A442404C0E00432815C010000241030815C010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 4
		#xor     al, [ecx+15Ch]
		#and     al, 10h
		#xor     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D370(self):
		#sub_6E20D370
		gadget = "8A442404C0E00532815C010000242030815C010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 5
		#xor     al, [ecx+15Ch]
		#and     al, 20h
		#xor     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D390(self):
		#sub_6E20D390
		gadget = "8A442404C0E00632815C010000244030815C010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 6
		#xor     al, [ecx+15Ch]
		#and     al, 40h
		#xor     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D3B0(self):
		#sub_6E20D3B0
		gadget = "8A815C0100008A542404247FC0E2070AC288815C010000C20400"
		self.do(gadget)

		#mov     al, [ecx+15Ch]
		#mov     dl, [esp+arg_0]
		#and     al, 7Fh
		#shl     dl, 7
		#or      al, dl
		#mov     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D3D0(self):
		#sub_6E20D3D0
		gadget = "8A815C01000032442404240130815C010000C20400"
		self.do(gadget)

		#mov     al, [ecx+15Ch]
		#xor     al, [esp+arg_0]
		#and     al, 1
		#xor     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D3F0(self):
		#sub_6E20D3F0
		gadget = "8A44240402C002C032815C010000240430815C010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#xor     al, [ecx+15Ch]
		#and     al, 4
		#xor     [ecx+15Ch], al
		#retn    4


  def test_gadget_sub_6E20D410(self):
		#sub_6E20D410
		gadget = "D9442404D99948010000C20400"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+148h]
		#retn    4


  def test_gadget_sub_6E20D440(self):
		#sub_6E20D440
		gadget = "8B4424048B1089919C0100008B40048981A0010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+19Ch], edx
		#mov     eax, [eax+4]
		#mov     [ecx+1A0h], eax
		#retn    4


  def test_gadget_sub_6E20D460(self):
		#sub_6E20D460
		gadget = "8B4424048B108991A40100008B40048981A8010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+1A4h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+1A8h], eax
		#retn    4


  def test_gadget_sub_6E20D480(self):
		#sub_6E20D480
		gadget = "8B4424048B1089918C0100008B50048991900100008B50088991940100008B400C898198010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+18Ch], edx
		#mov     edx, [eax+4]
		#mov     [ecx+190h], edx
		#mov     edx, [eax+8]
		#mov     [ecx+194h], edx
		#mov     eax, [eax+0Ch]
		#mov     [ecx+198h], eax
		#retn    4


  def test_gadget_sub_6E20D4C0(self):
		#sub_6E20D4C0
		gadget = "8B442404898164010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+164h], eax
		#retn    4


  def test_gadget_sub_6E20D4D0(self):
		#sub_6E20D4D0
		gadget = "8A44240402C002C032815D010000240430815D010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#xor     al, [ecx+15Dh]
		#and     al, 4
		#xor     [ecx+15Dh], al
		#retn    4


  def test_gadget_sub_6E20D4F0(self):
		#sub_6E20D4F0
		gadget = "8A44240402C002C002C032815D010000240830815D010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#add     al, al
		#xor     al, [ecx+15Dh]
		#and     al, 8
		#xor     [ecx+15Dh], al
		#retn    4


  def test_gadget_sub_6E20D510(self):
		#sub_6E20D510
		gadget = "D9814C010000C3"
		self.do(gadget)

		#fld     dword ptr [ecx+14Ch]
		#retn


  def test_gadget_sub_6E20D520(self):
		#sub_6E20D520
		gadget = "8A815D01000032442404240130815D010000C20400"
		self.do(gadget)

		#mov     al, [ecx+15Dh]
		#xor     al, [esp+arg_0]
		#and     al, 1
		#xor     [ecx+15Dh], al
		#retn    4


  def test_gadget_sub_6E20D540(self):
		#sub_6E20D540
		gadget = "8A815D0100002401C3"
		self.do(gadget)

		#mov     al, [ecx+15Dh]
		#and     al, 1
		#retn


  def test_gadget_sub_6E20D550(self):
		#sub_6E20D550
		gadget = "8A44240402C032815D010000240230815D010000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#xor     al, [ecx+15Dh]
		#and     al, 2
		#xor     [ecx+15Dh], al
		#retn    4


  def test_gadget_sub_6E20D570(self):
		#sub_6E20D570
		gadget = "8A815D010000D0E82401C3"
		self.do(gadget)

		#mov     al, [ecx+15Dh]
		#shr     al, 1
		#and     al, 1
		#retn


  def test_gadget_sub_6E20D580(self):
		#sub_6E20D580
		gadget = "8B442404898180010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+180h], eax
		#retn    4


  def test_gadget_sub_6E211290(self):
		#sub_6E211290
		gadget = "8BC18B4C2404C700402A8A6E894804C6400800C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8A2A40
		#mov     [eax+4], ecx
		#mov     byte ptr [eax+8], 0
		#retn    8


  def test_gadget_sub_6E2113F0(self):
		#sub_6E2113F0
		gadget = "8BC1D90558068A6ED91032C9D95804D9EED95008D9500CD95010D95014D9581866C7401C0100D9E888481EDD5020D9EEDD5028DD5030DD5038DD5040DD5050DD5058DD5060DD5068DD5078DD9080000000DD9088000000DD9090000000D9C9DD5048DD5070DD9098000000DD90A0000000D9C9DD90A8000000DD90B0000000DD90B8000000DD90C0000000DD90D0000000DD90D8000000DD90E0000000DD90E8000000DD90F8000000DD9000010000DD9008010000DD9010010000D9C9DD90C8000000DD90F0000000DD9018010000DD9020010000D9C9DD9028010000DD9030010000DD9038010000DD9040010000DD9050010000DD9058010000DD9060010000DD9068010000DD9078010000DD9080010000DD9088010000DD9090010000D9C9DD9048010000DD9070010000DD9098010000DD90A0010000D9C9DD90A8010000DD90B0010000DD90B8010000DD90C0010000DD90D0010000DD90D8010000DD90E0010000DD90E8010000DD90F8010000DD9000020000DD9008020000DD9810020000DD90C8010000DD90F0010000DD9818020000C3"
		self.do(gadget)

		#mov     eax, ecx
		#fld     ds:flt_6E8A0658
		#fst     dword ptr [eax]
		#xor     cl, cl
		#fstp    dword ptr [eax+4]
		#fldz
		#fst     dword ptr [eax+8]
		#fst     dword ptr [eax+0Ch]
		#fst     dword ptr [eax+10h]
		#fst     dword ptr [eax+14h]
		#fstp    dword ptr [eax+18h]
		#mov     word ptr [eax+1Ch], 1
		#fld1
		#mov     [eax+1Eh], cl
		#fst     qword ptr [eax+20h]
		#fldz
		#fst     qword ptr [eax+28h]
		#fst     qword ptr [eax+30h]
		#fst     qword ptr [eax+38h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+50h]
		#fst     qword ptr [eax+58h]
		#fst     qword ptr [eax+60h]
		#fst     qword ptr [eax+68h]
		#fst     qword ptr [eax+78h]
		#fst     qword ptr [eax+80h]
		#fst     qword ptr [eax+88h]
		#fst     qword ptr [eax+90h]
		#fxch    st(1)
		#fst     qword ptr [eax+48h]
		#fst     qword ptr [eax+70h]
		#fst     qword ptr [eax+98h]
		#fst     qword ptr [eax+0A0h]
		#fxch    st(1)
		#fst     qword ptr [eax+0A8h]
		#fst     qword ptr [eax+0B0h]
		#fst     qword ptr [eax+0B8h]
		#fst     qword ptr [eax+0C0h]
		#fst     qword ptr [eax+0D0h]
		#fst     qword ptr [eax+0D8h]
		#fst     qword ptr [eax+0E0h]
		#fst     qword ptr [eax+0E8h]
		#fst     qword ptr [eax+0F8h]
		#fst     qword ptr [eax+100h]
		#fst     qword ptr [eax+108h]
		#fst     qword ptr [eax+110h]
		#fxch    st(1)
		#fst     qword ptr [eax+0C8h]
		#fst     qword ptr [eax+0F0h]
		#fst     qword ptr [eax+118h]
		#fst     qword ptr [eax+120h]
		#fxch    st(1)
		#fst     qword ptr [eax+128h]
		#fst     qword ptr [eax+130h]
		#fst     qword ptr [eax+138h]
		#fst     qword ptr [eax+140h]
		#fst     qword ptr [eax+150h]
		#fst     qword ptr [eax+158h]
		#fst     qword ptr [eax+160h]
		#fst     qword ptr [eax+168h]
		#fst     qword ptr [eax+178h]
		#fst     qword ptr [eax+180h]
		#fst     qword ptr [eax+188h]
		#fst     qword ptr [eax+190h]
		#fxch    st(1)
		#fst     qword ptr [eax+148h]
		#fst     qword ptr [eax+170h]
		#fst     qword ptr [eax+198h]
		#fst     qword ptr [eax+1A0h]
		#fxch    st(1)
		#fst     qword ptr [eax+1A8h]
		#fst     qword ptr [eax+1B0h]
		#fst     qword ptr [eax+1B8h]
		#fst     qword ptr [eax+1C0h]
		#fst     qword ptr [eax+1D0h]
		#fst     qword ptr [eax+1D8h]
		#fst     qword ptr [eax+1E0h]
		#fst     qword ptr [eax+1E8h]
		#fst     qword ptr [eax+1F8h]
		#fst     qword ptr [eax+200h]
		#fst     qword ptr [eax+208h]
		#fstp    qword ptr [eax+210h]
		#fst     qword ptr [eax+1C8h]
		#fst     qword ptr [eax+1F0h]
		#fstp    qword ptr [eax+218h]
		#retn


  def test_gadget_sub_6E2122B0(self):
		#sub_6E2122B0
		gadget = "8BC18B4C2404C7400401000000C700CC2A8A6EC740080000000089480CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     dword ptr [eax], offset off_6E8A2ACC
		#mov     dword ptr [eax+8], 0
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E212BD0(self):
		#sub_6E212BD0
		gadget = "568B7424088B069983E23F03C2C1F806578B7E0489018BC79983E23F03C2C1F8068941048B46088B7E0C9983E23F03C2C1F8068941088BC79983E23F03C2C1F8065F89410C8BC15EC20400"
		self.do(gadget)

		#push    esi
		#mov     esi, [esp+4+arg_0]
		#mov     eax, [esi]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#push    edi
		#mov     edi, [esi+4]
		#mov     [ecx], eax
		#mov     eax, edi
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#mov     [ecx+4], eax
		#mov     eax, [esi+8]
		#mov     edi, [esi+0Ch]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#mov     [ecx+8], eax
		#mov     eax, edi
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#pop     edi
		#mov     [ecx+0Ch], eax
		#mov     eax, ecx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E2136F0(self):
		#sub_6E2136F0
		gadget = "83EC08D9018B44240CD8410856DD0530FD846E57DCC9D9C9D95C24088B542408D94104D8410C895008D8C9D95C240C8B54240C89500CD94110D841088B542418D8C9D95C24088B742408D94114D8410C897208D8C9D95C240C8B74240C89720CD94208D84008D8C9D95C24088B742408D9420CD8400C897010DEC9D95C240C8B7C240C8978148932897A048B3189308B71048970048B41108942108B49145F894A145E83C408C20800"
		self.do(gadget)

		#sub     esp, 8
		#fld     dword ptr [ecx]
		#mov     eax, [esp+8+arg_0]
		#fadd    dword ptr [ecx+8]
		#push    esi
		#fld     ds:dbl_6E84FD30
		#push    edi
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    [esp+10h+var_8]
		#mov     edx, [esp+10h+var_8]
		#fld     dword ptr [ecx+4]
		#fadd    dword ptr [ecx+0Ch]
		#mov     [eax+8], edx
		#fmul    st, st(1)
		#fstp    [esp+10h+var_4]
		#mov     edx, [esp+10h+var_4]
		#mov     [eax+0Ch], edx
		#fld     dword ptr [ecx+10h]
		#fadd    dword ptr [ecx+8]
		#mov     edx, [esp+10h+arg_4]
		#fmul    st, st(1)
		#fstp    [esp+10h+var_8]
		#mov     esi, [esp+10h+var_8]
		#fld     dword ptr [ecx+14h]
		#fadd    dword ptr [ecx+0Ch]
		#mov     [edx+8], esi
		#fmul    st, st(1)
		#fstp    [esp+10h+var_4]
		#mov     esi, [esp+10h+var_4]
		#mov     [edx+0Ch], esi
		#fld     dword ptr [edx+8]
		#fadd    dword ptr [eax+8]
		#fmul    st, st(1)
		#fstp    [esp+10h+var_8]
		#mov     esi, [esp+10h+var_8]
		#fld     dword ptr [edx+0Ch]
		#fadd    dword ptr [eax+0Ch]
		#mov     [eax+10h], esi
		#fmulp   st(1), st
		#fstp    [esp+10h+var_4]
		#mov     edi, [esp+10h+var_4]
		#mov     [eax+14h], edi
		#mov     [edx], esi
		#mov     [edx+4], edi
		#mov     esi, [ecx]
		#mov     [eax], esi
		#mov     esi, [ecx+4]
		#mov     [eax+4], esi
		#mov     eax, [ecx+10h]
		#mov     [edx+10h], eax
		#mov     ecx, [ecx+14h]
		#pop     edi
		#mov     [edx+14h], ecx
		#pop     esi
		#add     esp, 8
		#retn    8


  def test_gadget_sub_6E2137A0(self):
		#sub_6E2137A0
		gadget = "83EC10D941088B11D841108B442414DD0530FD846E56DCC9D9C9D95C240CD94114D8410C89108B5104895004D8C9D95C2410D94108D801D8C9D95C24048B542404D94104D8410C895008D8C9D95C24088B54240889500CD94008D944240CD9C0DEC2D9C9D8CAD95C24048B542404D9400C895010D9442410D9C0DEC2D9C9D8CBD95C24088B542408895014D94118D841108B54241CD8CBD95C240C8B74240CD9411CD84114897210D8CBD95C24108B742410897214D94210DEC2D9C9D8CAD95C240C8B74240CD84214897208D8C9D95C24108B74241089720C8B71188972188B491C894A1CD94208D84010D8C9D95C240CD9420CD840148B4C240CDEC9894818D95C24108B74241089701C897204890A5E83C410C20800"
		self.do(gadget)

		#sub     esp, 10h
		#fld     dword ptr [ecx+8]
		#mov     edx, [ecx]
		#fadd    dword ptr [ecx+10h]
		#mov     eax, [esp+10h+arg_0]
		#fld     ds:dbl_6E84FD30
		#push    esi
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    [esp+14h+var_8]
		#fld     dword ptr [ecx+14h]
		#fadd    dword ptr [ecx+0Ch]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#fmul    st, st(1)
		#fstp    [esp+14h+var_4]
		#fld     dword ptr [ecx+8]
		#fadd    dword ptr [ecx]
		#fmul    st, st(1)
		#fstp    [esp+14h+var_10]
		#mov     edx, [esp+14h+var_10]
		#fld     dword ptr [ecx+4]
		#fadd    dword ptr [ecx+0Ch]
		#mov     [eax+8], edx
		#fmul    st, st(1)
		#fstp    [esp+14h+var_C]
		#mov     edx, [esp+14h+var_C]
		#mov     [eax+0Ch], edx
		#fld     dword ptr [eax+8]
		#fld     [esp+14h+var_8]
		#fld     st
		#faddp   st(2), st
		#fxch    st(1)
		#fmul    st, st(2)
		#fstp    [esp+14h+var_10]
		#mov     edx, [esp+14h+var_10]
		#fld     dword ptr [eax+0Ch]
		#mov     [eax+10h], edx
		#fld     [esp+14h+var_4]
		#fld     st
		#faddp   st(2), st
		#fxch    st(1)
		#fmul    st, st(3)
		#fstp    [esp+14h+var_C]
		#mov     edx, [esp+14h+var_C]
		#mov     [eax+14h], edx
		#fld     dword ptr [ecx+18h]
		#fadd    dword ptr [ecx+10h]
		#mov     edx, [esp+14h+arg_4]
		#fmul    st, st(3)
		#fstp    [esp+14h+var_8]
		#mov     esi, [esp+14h+var_8]
		#fld     dword ptr [ecx+1Ch]
		#fadd    dword ptr [ecx+14h]
		#mov     [edx+10h], esi
		#fmul    st, st(3)
		#fstp    [esp+14h+var_4]
		#mov     esi, [esp+14h+var_4]
		#mov     [edx+14h], esi
		#fld     dword ptr [edx+10h]
		#faddp   st(2), st
		#fxch    st(1)
		#fmul    st, st(2)
		#fstp    [esp+14h+var_8]
		#mov     esi, [esp+14h+var_8]
		#fadd    dword ptr [edx+14h]
		#mov     [edx+8], esi
		#fmul    st, st(1)
		#fstp    [esp+14h+var_4]
		#mov     esi, [esp+14h+var_4]
		#mov     [edx+0Ch], esi
		#mov     esi, [ecx+18h]
		#mov     [edx+18h], esi
		#mov     ecx, [ecx+1Ch]
		#mov     [edx+1Ch], ecx
		#fld     dword ptr [edx+8]
		#fadd    dword ptr [eax+10h]
		#fmul    st, st(1)
		#fstp    [esp+14h+var_8]
		#fld     dword ptr [edx+0Ch]
		#fadd    dword ptr [eax+14h]
		#mov     ecx, [esp+14h+var_8]
		#fmulp   st(1), st
		#mov     [eax+18h], ecx
		#fstp    [esp+14h+var_4]
		#mov     esi, [esp+14h+var_4]
		#mov     [eax+1Ch], esi
		#mov     [edx+4], esi
		#mov     [edx], ecx
		#pop     esi
		#add     esp, 10h
		#retn    8


  def test_gadget_sub_6E2138C0(self):
		#sub_6E2138C0
		gadget = "D9EE8BC18B4C2404890833C9884804D95008D9500CD95010D95014D95018D9501CD95020D9502489482CD95028D95030D95034D95038D9583CC20400"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], cl
		#fst     dword ptr [eax+8]
		#fst     dword ptr [eax+0Ch]
		#fst     dword ptr [eax+10h]
		#fst     dword ptr [eax+14h]
		#fst     dword ptr [eax+18h]
		#fst     dword ptr [eax+1Ch]
		#fst     dword ptr [eax+20h]
		#fst     dword ptr [eax+24h]
		#mov     [eax+2Ch], ecx
		#fst     dword ptr [eax+28h]
		#fst     dword ptr [eax+30h]
		#fst     dword ptr [eax+34h]
		#fst     dword ptr [eax+38h]
		#fstp    dword ptr [eax+3Ch]
		#retn    4


  def test_gadget_sub_6E213900(self):
		#sub_6E213900
		gadget = "8B442404D9EE8B108951208B50048951248B108951188B500489511C8B108951108B50048951148B108951088B400489410CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fldz
		#mov     edx, [eax]
		#mov     [ecx+20h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+24h], edx
		#mov     edx, [eax]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+1Ch], edx
		#mov     edx, [eax]
		#mov     [ecx+10h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+14h], edx
		#mov     edx, [eax]
		#mov     [ecx+8], edx
		#mov     eax, [eax+4]
		#mov     [ecx+0Ch], eax
		#retn    4


  def test_gadget_sub_6E214330(self):
		#sub_6E214330
		gadget = "568B742408578D7918B90C000000F3A55F5EC20400"
		self.do(gadget)

		#push    esi
		#mov     esi, [esp+4+arg_0]
		#push    edi
		#lea     edi, [ecx+18h]
		#mov     ecx, 0Ch
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E214B30(self):
		#sub_6E214B30
		gadget = "8BC133C9890889480489480889480C8D5018895010C74014200000008988980000008D90A400000089909C000000C780A000000010000000898824010000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#lea     edx, [eax+18h]
		#mov     [eax+10h], edx
		#mov     dword ptr [eax+14h], 20h
		#mov     [eax+98h], ecx
		#lea     edx, [eax+0A4h]
		#mov     [eax+9Ch], edx
		#mov     dword ptr [eax+0A0h], 10h
		#mov     [eax+124h], ecx
		#retn


  def test_gadget_sub_6E2165F0(self):
		#sub_6E2165F0
		gadget = "8BC18B4C24048B1189108B51048950048B5108568B74240C8950088B490C5789480C8D7810B908000000F3A55F5EC20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#push    esi
		#mov     esi, [esp+4+arg_4]
		#mov     [eax+8], edx
		#mov     ecx, [ecx+0Ch]
		#push    edi
		#mov     [eax+0Ch], ecx
		#lea     edi, [eax+10h]
		#mov     ecx, 8
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    8


  def test_gadget_sub_6E217BD0(self):
		#sub_6E217BD0
		gadget = "8A814D040000C3"
		self.do(gadget)

		#mov     al, [ecx+44Dh]
		#retn


  def test_gadget_sub_6E217BE0(self):
		#sub_6E217BE0
		gadget = "8BC1C20400"
		self.do(gadget)

		#mov     eax, ecx
		#retn    4


  def test_gadget_sub_6E2181E0(self):
		#sub_6E2181E0
		gadget = "8A814E040000C3"
		self.do(gadget)

		#mov     al, [ecx+44Eh]
		#retn


  def test_gadget_sub_6E219000(self):
		#sub_6E219000
		gadget = "8A442404A2F478A66EC3"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     byte_6EA678F4, al
		#retn


  def test_gadget_sub_6E2192D0(self):
		#sub_6E2192D0
		gadget = "80899400000002C3"
		self.do(gadget)

		#or      byte ptr [ecx+94h], 2
		#retn


  def test_gadget_sub_6E2196C0(self):
		#sub_6E2196C0
		gadget = "518B442408C7042400000000C7000000000059C21800"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    18h


  def test_gadget_sub_6E21D1D0(self):
		#sub_6E21D1D0
		gadget = "8B442404894168C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+68h], eax
		#retn    4


  def test_gadget_sub_6E21D1E0(self):
		#sub_6E21D1E0
		gadget = "8B4168C3"
		self.do(gadget)

		#mov     eax, [ecx+68h]
		#retn


  def test_gadget_sub_6E21D1F0(self):
		#sub_6E21D1F0
		gadget = "8B44240456578D7170B90C0000008BF8F3A55F5EC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#push    esi
		#push    edi
		#lea     esi, [ecx+70h]
		#mov     ecx, 0Ch
		#mov     edi, eax
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    8


  def test_gadget_sub_6E220B50(self):
		#sub_6E220B50
		gadget = "DD442404DD19DD44240CDD5908DD442414DD5910DD44241CDD5918DD442424DD5920DD44242CDD5928C23000"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    qword ptr [ecx]
		#fld     [esp+arg_8]
		#fstp    qword ptr [ecx+8]
		#fld     [esp+arg_10]
		#fstp    qword ptr [ecx+10h]
		#fld     [esp+arg_18]
		#fstp    qword ptr [ecx+18h]
		#fld     [esp+arg_20]
		#fstp    qword ptr [ecx+20h]
		#fld     [esp+arg_28]
		#fstp    qword ptr [ecx+28h]
		#retn    30h


  def test_gadget_sub_6E220C60(self):
		#sub_6E220C60
		gadget = "8BC1DD00DD442404DCC9D9C9DD18DC4808DD5808DD4010DD44240CDCC9D9C9DD5810DC4818DD5818C21000"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax]
		#fld     [esp+arg_0]
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax]
		#fmul    qword ptr [eax+8]
		#fstp    qword ptr [eax+8]
		#fld     qword ptr [eax+10h]
		#fld     [esp+arg_8]
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax+10h]
		#fmul    qword ptr [eax+18h]
		#fstp    qword ptr [eax+18h]
		#retn    10h


  def test_gadget_sub_6E220D20(self):
		#sub_6E220D20
		gadget = "8BC1DD00DD05580B856EDCC9D9C9DD18DC4808DD5808C3"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax]
		#fld     ds:dbl_6E850B58
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax]
		#fmul    qword ptr [eax+8]
		#fstp    qword ptr [eax+8]
		#retn


  def test_gadget_sub_6E220D40(self):
		#sub_6E220D40
		gadget = "8BC1DD4010DD05580B856EDCC9D9C9DD5810DC4818DD5818C3"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax+10h]
		#fld     ds:dbl_6E850B58
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax+10h]
		#fmul    qword ptr [eax+18h]
		#fstp    qword ptr [eax+18h]
		#retn


  def test_gadget_sub_6E220D60(self):
		#sub_6E220D60
		gadget = "DD41108B442414DD44240CDCC9DD01DD442404DCC9D9CBDEC1DC4120DD18DD4108DECADC4918DEC1DC41288B4C2418DD19C21800"
		self.do(gadget)

		#fld     qword ptr [ecx+10h]
		#mov     eax, [esp+arg_10]
		#fld     [esp+arg_8]
		#fmul    st(1), st
		#fld     qword ptr [ecx]
		#fld     [esp+arg_0]
		#fmul    st(1), st
		#fxch    st(3)
		#faddp   st(1), st
		#fadd    qword ptr [ecx+20h]
		#fstp    qword ptr [eax]
		#fld     qword ptr [ecx+8]
		#fmulp   st(2), st
		#fmul    qword ptr [ecx+18h]
		#faddp   st(1), st
		#fadd    qword ptr [ecx+28h]
		#mov     ecx, [esp+arg_14]
		#fstp    qword ptr [ecx]
		#retn    18h


  def test_gadget_sub_6E220DA0(self):
		#sub_6E220DA0
		gadget = "8B442408D900D940048B442404DD4110D8C9DD01D8CBDEC1DC4120D918DD4108DECADC4918DEC1DC4128D95804C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#fld     dword ptr [eax]
		#fld     dword ptr [eax+4]
		#mov     eax, [esp+arg_0]
		#fld     qword ptr [ecx+10h]
		#fmul    st, st(1)
		#fld     qword ptr [ecx]
		#fmul    st, st(3)
		#faddp   st(1), st
		#fadd    qword ptr [ecx+20h]
		#fstp    dword ptr [eax]
		#fld     qword ptr [ecx+8]
		#fmulp   st(2), st
		#fmul    qword ptr [ecx+18h]
		#faddp   st(1), st
		#fadd    qword ptr [ecx+28h]
		#fstp    dword ptr [eax+4]
		#retn    8


  def test_gadget_sub_6E220FF0(self):
		#sub_6E220FF0
		gadget = "D9E88BC1DD10D9EEDD5008DD5010DD5020DD5828DD5818C3"
		self.do(gadget)

		#fld1
		#mov     eax, ecx
		#fst     qword ptr [eax]
		#fldz
		#fst     qword ptr [eax+8]
		#fst     qword ptr [eax+10h]
		#fst     qword ptr [eax+20h]
		#fstp    qword ptr [eax+28h]
		#fstp    qword ptr [eax+18h]
		#retn


  def test_gadget_sub_6E221010(self):
		#sub_6E221010
		gadget = "DD4424048BC1DD18DD44240CDD5808DD442414DD5810DD44241CDD5818DD442424DD5820DD44242CDD5828C23000"
		self.do(gadget)

		#fld     [esp+arg_0]
		#mov     eax, ecx
		#fstp    qword ptr [eax]
		#fld     [esp+arg_8]
		#fstp    qword ptr [eax+8]
		#fld     [esp+arg_10]
		#fstp    qword ptr [eax+10h]
		#fld     [esp+arg_18]
		#fstp    qword ptr [eax+18h]
		#fld     [esp+arg_20]
		#fstp    qword ptr [eax+20h]
		#fld     [esp+arg_28]
		#fstp    qword ptr [eax+28h]
		#retn    30h


  def test_gadget_sub_6E221040(self):
		#sub_6E221040
		gadget = "D9E8DD11D9EEDD5108DD5110DD5120DD5928DD5918C3"
		self.do(gadget)

		#fld1
		#fst     qword ptr [ecx]
		#fldz
		#fst     qword ptr [ecx+8]
		#fst     qword ptr [ecx+10h]
		#fst     qword ptr [ecx+20h]
		#fstp    qword ptr [ecx+28h]
		#fstp    qword ptr [ecx+18h]
		#retn


  def test_gadget_sub_6E221290(self):
		#sub_6E221290
		gadget = "8BC1DD00DD442404DCC9D9C9DD18DD4008D8C9DD5808DD4010D8C9DD5810DC4818DD5818C20800"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax]
		#fld     [esp+arg_0]
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax]
		#fld     qword ptr [eax+8]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+8]
		#fld     qword ptr [eax+10h]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+10h]
		#fmul    qword ptr [eax+18h]
		#fstp    qword ptr [eax+18h]
		#retn    8


  def test_gadget_sub_6E221630(self):
		#sub_6E221630
		gadget = "8B442404DD01DD18DD4108DD5808D9EEDD5010DD5018DD4110DD5820DD4118DD5828DD5030DD5038DD5040DD5048D9E8DD5050D9C9DD5058DD4120DD5860DD4128DD5868DD5870DD5878C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     qword ptr [ecx]
		#fstp    qword ptr [eax]
		#fld     qword ptr [ecx+8]
		#fstp    qword ptr [eax+8]
		#fldz
		#fst     qword ptr [eax+10h]
		#fst     qword ptr [eax+18h]
		#fld     qword ptr [ecx+10h]
		#fstp    qword ptr [eax+20h]
		#fld     qword ptr [ecx+18h]
		#fstp    qword ptr [eax+28h]
		#fst     qword ptr [eax+30h]
		#fst     qword ptr [eax+38h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+48h]
		#fld1
		#fst     qword ptr [eax+50h]
		#fxch    st(1)
		#fst     qword ptr [eax+58h]
		#fld     qword ptr [ecx+20h]
		#fstp    qword ptr [eax+60h]
		#fld     qword ptr [ecx+28h]
		#fstp    qword ptr [eax+68h]
		#fstp    qword ptr [eax+70h]
		#fstp    qword ptr [eax+78h]
		#retn    4


  def test_gadget_sub_6E221A20(self):
		#sub_6E221A20
		gadget = "558BEC83E4F883EC50DD4020DD4028DD4030DD4038DD4040DD4048DD5C2418DD4050DD542428DD4058DD542438DD4060DD5C2410DD4068DD5C2408DD4070DD1C24DD4078DD542420DECADD0424D8C9DEEAD9C9DD5C2440DD442420DC4C2418DD442408DECADEE1DD5C2448DD0424DC4C2418DD442408DC4C2428DEE9DD5C2430DD442420D8C9DD442410DC4C2438DEE9DD5C2420DD0424D8C9DD442410DC4C2428DEE9DD5C2428DC4C2408DD442410DC4C2418DEE9DD5C2438DD442440D9C0D8CCDD442448D9C0D8CDDEEADD442430D8CCDEC2D9C9DC08D9CAD8CEDD442420D8CDDEE9DD442428D8CCDEC1DC4808DEEAD8CDDD442420D8CDDEE9DD442438D9C0DECCD9C9DEC3D9CADC4810DEC1DD442430DECDDD442428DECCD9CCDEE3DEC9DEC1DC4818DEE98BE55DC3"
		self.do(gadget)

		#push    ebp
		#mov     ebp, esp
		#and     esp, 0FFFFFFF8h
		#sub     esp, 50h
		#fld     qword ptr [eax+20h]
		#fld     qword ptr [eax+28h]
		#fld     qword ptr [eax+30h]
		#fld     qword ptr [eax+38h]
		#fld     qword ptr [eax+40h]
		#fld     qword ptr [eax+48h]
		#fstp    [esp+50h+var_38]
		#fld     qword ptr [eax+50h]
		#fst     [esp+50h+var_28]
		#fld     qword ptr [eax+58h]
		#fst     [esp+50h+var_18]
		#fld     qword ptr [eax+60h]
		#fstp    [esp+50h+var_40]
		#fld     qword ptr [eax+68h]
		#fstp    [esp+50h+var_48]
		#fld     qword ptr [eax+70h]
		#fstp    [esp+50h+var_50]
		#fld     qword ptr [eax+78h]
		#fst     [esp+50h+var_30]
		#fmulp   st(2), st
		#fld     [esp+50h+var_50]
		#fmul    st, st(1)
		#fsubp   st(2), st
		#fxch    st(1)
		#fstp    [esp+50h+var_10]
		#fld     [esp+50h+var_30]
		#fmul    [esp+50h+var_38]
		#fld     [esp+50h+var_48]
		#fmulp   st(2), st
		#fsubrp  st(1), st
		#fstp    [esp+50h+var_8]
		#fld     [esp+50h+var_50]
		#fmul    [esp+50h+var_38]
		#fld     [esp+50h+var_48]
		#fmul    [esp+50h+var_28]
		#fsubp   st(1), st
		#fstp    [esp+50h+var_20]
		#fld     [esp+50h+var_30]
		#fmul    st, st(1)
		#fld     [esp+50h+var_40]
		#fmul    [esp+50h+var_18]
		#fsubp   st(1), st
		#fstp    [esp+50h+var_30]
		#fld     [esp+50h+var_50]
		#fmul    st, st(1)
		#fld     [esp+50h+var_40]
		#fmul    [esp+50h+var_28]
		#fsubp   st(1), st
		#fstp    [esp+50h+var_28]
		#fmul    [esp+50h+var_48]
		#fld     [esp+50h+var_40]
		#fmul    [esp+50h+var_38]
		#fsubp   st(1), st
		#fstp    [esp+50h+var_18]
		#fld     [esp+50h+var_10]
		#fld     st
		#fmul    st, st(4)
		#fld     [esp+50h+var_8]
		#fld     st
		#fmul    st, st(5)
		#fsubp   st(2), st
		#fld     [esp+50h+var_20]
		#fmul    st, st(4)
		#faddp   st(2), st
		#fxch    st(1)
		#fmul    qword ptr [eax]
		#fxch    st(2)
		#fmul    st, st(6)
		#fld     [esp+50h+var_30]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fld     [esp+50h+var_28]
		#fmul    st, st(4)
		#faddp   st(1), st
		#fmul    qword ptr [eax+8]
		#fsubp   st(2), st
		#fmul    st, st(5)
		#fld     [esp+50h+var_30]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fld     [esp+50h+var_18]
		#fld     st
		#fmulp   st(4), st
		#fxch    st(1)
		#faddp   st(3), st
		#fxch    st(2)
		#fmul    qword ptr [eax+10h]
		#faddp   st(1), st
		#fld     [esp+50h+var_20]
		#fmulp   st(5), st
		#fld     [esp+50h+var_28]
		#fmulp   st(4), st
		#fxch    st(4)
		#fsubrp  st(3), st
		#fmulp   st(1), st
		#faddp   st(1), st
		#fmul    qword ptr [eax+18h]
		#fsubp   st(1), st
		#mov     esp, ebp
		#pop     ebp
		#retn


  def test_gadget_sub_6E221B50(self):
		#sub_6E221B50
		gadget = "558BEC83E4F881EC88000000DD01DD4108DD4110DD4118DD4120DD4128DD5C2410DD4130DD5C2428DD4138DD5C2438DD4140DD5C2458DD4148DD5C2440DD4150DD542478DD4158DD542430DD4160DD5C2460DD4168DD5C2468DD4170DD5C2448DD4178DD542470DECADD442448D8C9DEEAD9C9DD9C2480000000DD442470DC4C2440DD442468DECADEE1DD5C2450DD442448DC4C2440DD442468DC4C2478DEE9DD5C2418DD842480000000DC4C2410DD442450DC4C2428DEE9DD442418DC4C2438DEC1DD18DD442470DC4C2458DD442460DC4C2430DEE9DD5C2420DD442448DC4C2458DD442460DC4C2478DEE9DD5C2408DD842480000000D8C9DD442420DC4C2428DEE9DD442408DC4C2438DEC1D9E0DD5820DD442468DC4C2458DD442460DC4C2440DEE9DD1C24DD442450D8C9DD442420DC4C2410DEE9DD0424DC4C2438DEC1DD5840DD442418D8C9DD442408DC4C2410DEE9DD0424DD442428DCC9D9CADEC1D9E0DD5860DD842480000000D8CDDD442450D8CDDEE9DD442418D8CCDEC1D9E0DD5808DD842480000000D8CEDD442420D8CDDEE9DD442408D8CCDEC1DD5828DD442450D8CEDD442420D8CEDEE9DD0424D8CCDEC1D9E0DD5848DD442418D8CEDD442408D8CEDEE9DD0424D8CDDEC1DD5868DC4C2470DD442448DD442438DCC9D9CADEE1DD1C24DD442470DC4C2410DD442468DECADEE1DD5C2408DD442448DC4C2410DD442468DC4C2428DEE9DD542420DD0424D8CDDD442408D8CDDEE9D9C9D8CBDEC1DD5810DD442470D8C9DD442460DC4C2438DEE9DD5C2418DD442448D8C9DD442460DC4C2428DEE9DD542450DD0424D8CEDD442418D8CDDEE9D9C9D8CBDEC1D9E0DD5830DD442468D8C9DD442460DC4C2410DEE9DD442408D8CEDD442418D8CEDEE9D9C1D8CCDEC1DD5850DD442420D8CEDD442450D8CEDEE9D9C9D8CCDEC1D9E0DD5870DD442430DC4C2428DD442478DD442438DCC9D9CADEE1DD1C24DD442430DC4C2410DD442440DECADEE1DD5C2408DD442478DC4C2410DD442440DC4C2428DEE9DD542420DD0424D8CDDD442408D8CDDEE9D9C9D8CBDEC1D9E0DD5818DD442430D8C9DD442458DC4C2438DEE9DD5C2418DD442478D8C9DD442458DC4C2428DEE9DD5C2430DD0424D8CDDD442418D9C0D8CDDEEADD442430D8CCDEC2D9C9DD5838DD442440DECADD442458DC4C2410DEEADD442408D8CED9C9D8CDDEE9D9C1DECBDEC2D9C9D9E0DD5858DD442420DECCDD442430DECBD9CBDEE2DECADEC1DD58788BE55DC3"
		self.do(gadget)

		#push    ebp
		#mov     ebp, esp
		#and     esp, 0FFFFFFF8h
		#sub     esp, 88h
		#fld     qword ptr [ecx]
		#fld     qword ptr [ecx+8]
		#fld     qword ptr [ecx+10h]
		#fld     qword ptr [ecx+18h]
		#fld     qword ptr [ecx+20h]
		#fld     qword ptr [ecx+28h]
		#fstp    [esp+88h+var_78]
		#fld     qword ptr [ecx+30h]
		#fstp    [esp+88h+var_60]
		#fld     qword ptr [ecx+38h]
		#fstp    [esp+88h+var_50]
		#fld     qword ptr [ecx+40h]
		#fstp    [esp+88h+var_30]
		#fld     qword ptr [ecx+48h]
		#fstp    [esp+88h+var_48]
		#fld     qword ptr [ecx+50h]
		#fst     [esp+88h+var_10]
		#fld     qword ptr [ecx+58h]
		#fst     [esp+88h+var_58]
		#fld     qword ptr [ecx+60h]
		#fstp    [esp+88h+var_28]
		#fld     qword ptr [ecx+68h]
		#fstp    [esp+88h+var_20]
		#fld     qword ptr [ecx+70h]
		#fstp    [esp+88h+var_40]
		#fld     qword ptr [ecx+78h]
		#fst     [esp+88h+var_18]
		#fmulp   st(2), st
		#fld     [esp+88h+var_40]
		#fmul    st, st(1)
		#fsubp   st(2), st
		#fxch    st(1)
		#fstp    [esp+88h+var_8]
		#fld     [esp+88h+var_18]
		#fmul    [esp+88h+var_48]
		#fld     [esp+88h+var_20]
		#fmulp   st(2), st
		#fsubrp  st(1), st
		#fstp    [esp+88h+var_38]
		#fld     [esp+88h+var_40]
		#fmul    [esp+88h+var_48]
		#fld     [esp+88h+var_20]
		#fmul    [esp+88h+var_10]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_70]
		#fld     [esp+88h+var_8]
		#fmul    [esp+88h+var_78]
		#fld     [esp+88h+var_38]
		#fmul    [esp+88h+var_60]
		#fsubp   st(1), st
		#fld     [esp+88h+var_70]
		#fmul    [esp+88h+var_50]
		#faddp   st(1), st
		#fstp    qword ptr [eax]
		#fld     [esp+88h+var_18]
		#fmul    [esp+88h+var_30]
		#fld     [esp+88h+var_28]
		#fmul    [esp+88h+var_58]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_68]
		#fld     [esp+88h+var_40]
		#fmul    [esp+88h+var_30]
		#fld     [esp+88h+var_28]
		#fmul    [esp+88h+var_10]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_80]
		#fld     [esp+88h+var_8]
		#fmul    st, st(1)
		#fld     [esp+88h+var_68]
		#fmul    [esp+88h+var_60]
		#fsubp   st(1), st
		#fld     [esp+88h+var_80]
		#fmul    [esp+88h+var_50]
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+20h]
		#fld     [esp+88h+var_20]
		#fmul    [esp+88h+var_30]
		#fld     [esp+88h+var_28]
		#fmul    [esp+88h+var_48]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_88]
		#fld     [esp+88h+var_38]
		#fmul    st, st(1)
		#fld     [esp+88h+var_68]
		#fmul    [esp+88h+var_78]
		#fsubp   st(1), st
		#fld     [esp+88h+var_88]
		#fmul    [esp+88h+var_50]
		#faddp   st(1), st
		#fstp    qword ptr [eax+40h]
		#fld     [esp+88h+var_70]
		#fmul    st, st(1)
		#fld     [esp+88h+var_80]
		#fmul    [esp+88h+var_78]
		#fsubp   st(1), st
		#fld     [esp+88h+var_88]
		#fld     [esp+88h+var_60]
		#fmul    st(1), st
		#fxch    st(2)
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+60h]
		#fld     [esp+88h+var_8]
		#fmul    st, st(5)
		#fld     [esp+88h+var_38]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fld     [esp+88h+var_70]
		#fmul    st, st(4)
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+8]
		#fld     [esp+88h+var_8]
		#fmul    st, st(6)
		#fld     [esp+88h+var_68]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fld     [esp+88h+var_80]
		#fmul    st, st(4)
		#faddp   st(1), st
		#fstp    qword ptr [eax+28h]
		#fld     [esp+88h+var_38]
		#fmul    st, st(6)
		#fld     [esp+88h+var_68]
		#fmul    st, st(6)
		#fsubp   st(1), st
		#fld     [esp+88h+var_88]
		#fmul    st, st(4)
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+48h]
		#fld     [esp+88h+var_70]
		#fmul    st, st(6)
		#fld     [esp+88h+var_80]
		#fmul    st, st(6)
		#fsubp   st(1), st
		#fld     [esp+88h+var_88]
		#fmul    st, st(5)
		#faddp   st(1), st
		#fstp    qword ptr [eax+68h]
		#fmul    [esp+88h+var_18]
		#fld     [esp+88h+var_40]
		#fld     [esp+88h+var_50]
		#fmul    st(1), st
		#fxch    st(2)
		#fsubrp  st(1), st
		#fstp    [esp+88h+var_88]
		#fld     [esp+88h+var_18]
		#fmul    [esp+88h+var_78]
		#fld     [esp+88h+var_20]
		#fmulp   st(2), st
		#fsubrp  st(1), st
		#fstp    [esp+88h+var_80]
		#fld     [esp+88h+var_40]
		#fmul    [esp+88h+var_78]
		#fld     [esp+88h+var_20]
		#fmul    [esp+88h+var_60]
		#fsubp   st(1), st
		#fst     [esp+88h+var_68]
		#fld     [esp+88h+var_88]
		#fmul    st, st(5)
		#fld     [esp+88h+var_80]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fxch    st(1)
		#fmul    st, st(3)
		#faddp   st(1), st
		#fstp    qword ptr [eax+10h]
		#fld     [esp+88h+var_18]
		#fmul    st, st(1)
		#fld     [esp+88h+var_28]
		#fmul    [esp+88h+var_50]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_70]
		#fld     [esp+88h+var_40]
		#fmul    st, st(1)
		#fld     [esp+88h+var_28]
		#fmul    [esp+88h+var_60]
		#fsubp   st(1), st
		#fst     [esp+88h+var_38]
		#fld     [esp+88h+var_88]
		#fmul    st, st(6)
		#fld     [esp+88h+var_70]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fxch    st(1)
		#fmul    st, st(3)
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+30h]
		#fld     [esp+88h+var_20]
		#fmul    st, st(1)
		#fld     [esp+88h+var_28]
		#fmul    [esp+88h+var_78]
		#fsubp   st(1), st
		#fld     [esp+88h+var_80]
		#fmul    st, st(6)
		#fld     [esp+88h+var_70]
		#fmul    st, st(6)
		#fsubp   st(1), st
		#fld     st(1)
		#fmul    st, st(4)
		#faddp   st(1), st
		#fstp    qword ptr [eax+50h]
		#fld     [esp+88h+var_68]
		#fmul    st, st(6)
		#fld     [esp+88h+var_38]
		#fmul    st, st(6)
		#fsubp   st(1), st
		#fxch    st(1)
		#fmul    st, st(4)
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+70h]
		#fld     [esp+88h+var_58]
		#fmul    [esp+88h+var_60]
		#fld     [esp+88h+var_10]
		#fld     [esp+88h+var_50]
		#fmul    st(1), st
		#fxch    st(2)
		#fsubrp  st(1), st
		#fstp    [esp+88h+var_88]
		#fld     [esp+88h+var_58]
		#fmul    [esp+88h+var_78]
		#fld     [esp+88h+var_48]
		#fmulp   st(2), st
		#fsubrp  st(1), st
		#fstp    [esp+88h+var_80]
		#fld     [esp+88h+var_10]
		#fmul    [esp+88h+var_78]
		#fld     [esp+88h+var_48]
		#fmul    [esp+88h+var_60]
		#fsubp   st(1), st
		#fst     [esp+88h+var_68]
		#fld     [esp+88h+var_88]
		#fmul    st, st(5)
		#fld     [esp+88h+var_80]
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fxch    st(1)
		#fmul    st, st(3)
		#faddp   st(1), st
		#fchs
		#fstp    qword ptr [eax+18h]
		#fld     [esp+88h+var_58]
		#fmul    st, st(1)
		#fld     [esp+88h+var_30]
		#fmul    [esp+88h+var_50]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_70]
		#fld     [esp+88h+var_10]
		#fmul    st, st(1)
		#fld     [esp+88h+var_30]
		#fmul    [esp+88h+var_60]
		#fsubp   st(1), st
		#fstp    [esp+88h+var_58]
		#fld     [esp+88h+var_88]
		#fmul    st, st(5)
		#fld     [esp+88h+var_70]
		#fld     st
		#fmul    st, st(5)
		#fsubp   st(2), st
		#fld     [esp+88h+var_58]
		#fmul    st, st(4)
		#faddp   st(2), st
		#fxch    st(1)
		#fstp    qword ptr [eax+38h]
		#fld     [esp+88h+var_48]
		#fmulp   st(2), st
		#fld     [esp+88h+var_30]
		#fmul    [esp+88h+var_78]
		#fsubp   st(2), st
		#fld     [esp+88h+var_80]
		#fmul    st, st(6)
		#fxch    st(1)
		#fmul    st, st(5)
		#fsubp   st(1), st
		#fld     st(1)
		#fmulp   st(3), st
		#faddp   st(2), st
		#fxch    st(1)
		#fchs
		#fstp    qword ptr [eax+58h]
		#fld     [esp+88h+var_68]
		#fmulp   st(4), st
		#fld     [esp+88h+var_58]
		#fmulp   st(3), st
		#fxch    st(3)
		#fsubrp  st(2), st
		#fmulp   st(2), st
		#faddp   st(1), st
		#fstp    qword ptr [eax+78h]
		#mov     esp, ebp
		#pop     ebp
		#retn


  def test_gadget_sub_6E222890(self):
		#sub_6E222890
		gadget = "8BC18B4C2404DD4128DD4120DD4118DD4110DD4108DD01DD18DD5808D9EEDD5010DD5018DD5030DD5038DD5040DD5048D9C9DD5820D9C9DD5828D9E8DD5050DD5878DD5058DD5870DD5860DD5868C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#fld     qword ptr [ecx+28h]
		#fld     qword ptr [ecx+20h]
		#fld     qword ptr [ecx+18h]
		#fld     qword ptr [ecx+10h]
		#fld     qword ptr [ecx+8]
		#fld     qword ptr [ecx]
		#fstp    qword ptr [eax]
		#fstp    qword ptr [eax+8]
		#fldz
		#fst     qword ptr [eax+10h]
		#fst     qword ptr [eax+18h]
		#fst     qword ptr [eax+30h]
		#fst     qword ptr [eax+38h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+48h]
		#fxch    st(1)
		#fstp    qword ptr [eax+20h]
		#fxch    st(1)
		#fstp    qword ptr [eax+28h]
		#fld1
		#fst     qword ptr [eax+50h]
		#fstp    qword ptr [eax+78h]
		#fst     qword ptr [eax+58h]
		#fstp    qword ptr [eax+70h]
		#fstp    qword ptr [eax+60h]
		#fstp    qword ptr [eax+68h]
		#retn    4


  def test_gadget_sub_6E2228F0(self):
		#sub_6E2228F0
		gadget = "8BC1DD00DD442404DCC9D9C9DD18DD4008D8C9DD5808DD4010D8C9DD5810DC4818DD5818DD4020DD44240CDCC9D9C9DD5820DD4028D8C9DD5828DD4030D8C9DD5830DC4838DD5838DD4040DD442414DCC9D9C9DD5840DD4048D8C9DD5848DD4050D8C9DD5850DC4858DD5858C21800"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax]
		#fld     [esp+arg_0]
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax]
		#fld     qword ptr [eax+8]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+8]
		#fld     qword ptr [eax+10h]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+10h]
		#fmul    qword ptr [eax+18h]
		#fstp    qword ptr [eax+18h]
		#fld     qword ptr [eax+20h]
		#fld     [esp+arg_8]
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax+20h]
		#fld     qword ptr [eax+28h]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+28h]
		#fld     qword ptr [eax+30h]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+30h]
		#fmul    qword ptr [eax+38h]
		#fstp    qword ptr [eax+38h]
		#fld     qword ptr [eax+40h]
		#fld     [esp+arg_10]
		#fmul    st(1), st
		#fxch    st(1)
		#fstp    qword ptr [eax+40h]
		#fld     qword ptr [eax+48h]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+48h]
		#fld     qword ptr [eax+50h]
		#fmul    st, st(1)
		#fstp    qword ptr [eax+50h]
		#fmul    qword ptr [eax+58h]
		#fstp    qword ptr [eax+58h]
		#retn    18h


  def test_gadget_sub_6E222960(self):
		#sub_6E222960
		gadget = "8BC1DD4020DD44240CDCC9DD00DD442404DCC9D9CBDEC1DC4060DD5860DD4008D8CADD4028D8CADEC1DC4068DD5868DD4010D8CADD4030D8CADEC1DC4070DD5870DD4018DECADC4838DEC1DC4078DD5878C21000"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax+20h]
		#fld     [esp+arg_8]
		#fmul    st(1), st
		#fld     qword ptr [eax]
		#fld     [esp+arg_0]
		#fmul    st(1), st
		#fxch    st(3)
		#faddp   st(1), st
		#fadd    qword ptr [eax+60h]
		#fstp    qword ptr [eax+60h]
		#fld     qword ptr [eax+8]
		#fmul    st, st(2)
		#fld     qword ptr [eax+28h]
		#fmul    st, st(2)
		#faddp   st(1), st
		#fadd    qword ptr [eax+68h]
		#fstp    qword ptr [eax+68h]
		#fld     qword ptr [eax+10h]
		#fmul    st, st(2)
		#fld     qword ptr [eax+30h]
		#fmul    st, st(2)
		#faddp   st(1), st
		#fadd    qword ptr [eax+70h]
		#fstp    qword ptr [eax+70h]
		#fld     qword ptr [eax+18h]
		#fmulp   st(2), st
		#fmul    qword ptr [eax+38h]
		#faddp   st(1), st
		#fadd    qword ptr [eax+78h]
		#fstp    qword ptr [eax+78h]
		#retn    10h


  def test_gadget_sub_6E2229C0(self):
		#sub_6E2229C0
		gadget = "8BC1DD4020DD44240CDCC9DD00DD442404DCC9D9CBDEC1DD4040DD442414DCC9D9CADEC1DC4060DD5860DD4008D8CBDD4028D8CBDEC1DD4048D8CADEC1DC4068DD5868DD4010D8CBDD4030D8CBDEC1DD4050D8CADEC1DC4070DD5870DD4018DECBDD4038DECAD9CADEC1DD4058DECADEC1DC4078DD5878C21800"
		self.do(gadget)

		#mov     eax, ecx
		#fld     qword ptr [eax+20h]
		#fld     [esp+arg_8]
		#fmul    st(1), st
		#fld     qword ptr [eax]
		#fld     [esp+arg_0]
		#fmul    st(1), st
		#fxch    st(3)
		#faddp   st(1), st
		#fld     qword ptr [eax+40h]
		#fld     [esp+arg_10]
		#fmul    st(1), st
		#fxch    st(2)
		#faddp   st(1), st
		#fadd    qword ptr [eax+60h]
		#fstp    qword ptr [eax+60h]
		#fld     qword ptr [eax+8]
		#fmul    st, st(3)
		#fld     qword ptr [eax+28h]
		#fmul    st, st(3)
		#faddp   st(1), st
		#fld     qword ptr [eax+48h]
		#fmul    st, st(2)
		#faddp   st(1), st
		#fadd    qword ptr [eax+68h]
		#fstp    qword ptr [eax+68h]
		#fld     qword ptr [eax+10h]
		#fmul    st, st(3)
		#fld     qword ptr [eax+30h]
		#fmul    st, st(3)
		#faddp   st(1), st
		#fld     qword ptr [eax+50h]
		#fmul    st, st(2)
		#faddp   st(1), st
		#fadd    qword ptr [eax+70h]
		#fstp    qword ptr [eax+70h]
		#fld     qword ptr [eax+18h]
		#fmulp   st(3), st
		#fld     qword ptr [eax+38h]
		#fmulp   st(2), st
		#fxch    st(2)
		#faddp   st(1), st
		#fld     qword ptr [eax+58h]
		#fmulp   st(2), st
		#faddp   st(1), st
		#fadd    qword ptr [eax+78h]
		#fstp    qword ptr [eax+78h]
		#retn    18h


  def test_gadget_sub_6E222EF0(self):
		#sub_6E222EF0
		gadget = "D9EEDD5110DD5118DD5130DD5138DD5140DD5148D9E8DD5150DD5978DD5158DD5970C3"
		self.do(gadget)

		#fldz
		#fst     qword ptr [ecx+10h]
		#fst     qword ptr [ecx+18h]
		#fst     qword ptr [ecx+30h]
		#fst     qword ptr [ecx+38h]
		#fst     qword ptr [ecx+40h]
		#fst     qword ptr [ecx+48h]
		#fld1
		#fst     qword ptr [ecx+50h]
		#fstp    qword ptr [ecx+78h]
		#fst     qword ptr [ecx+58h]
		#fstp    qword ptr [ecx+70h]
		#retn


  def test_gadget_sub_6E223FE0(self):
		#sub_6E223FE0
		gadget = "8B4C240C8B542408D94108D872088B442404DD18D9EEDD5008DD5010DD5018DD5020D9410CD8720CDD5828DD5030DD5038DD5040DD5048D9E8DD5050D9C9DD5058D901D822DD5860D94104D86204DD5868DD5870DD5878C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [esp+arg_4]
		#fld     dword ptr [ecx+8]
		#fdiv    dword ptr [edx+8]
		#mov     eax, [esp+arg_0]
		#fstp    qword ptr [eax]
		#fldz
		#fst     qword ptr [eax+8]
		#fst     qword ptr [eax+10h]
		#fst     qword ptr [eax+18h]
		#fst     qword ptr [eax+20h]
		#fld     dword ptr [ecx+0Ch]
		#fdiv    dword ptr [edx+0Ch]
		#fstp    qword ptr [eax+28h]
		#fst     qword ptr [eax+30h]
		#fst     qword ptr [eax+38h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+48h]
		#fld1
		#fst     qword ptr [eax+50h]
		#fxch    st(1)
		#fst     qword ptr [eax+58h]
		#fld     dword ptr [ecx]
		#fsub    dword ptr [edx]
		#fstp    qword ptr [eax+60h]
		#fld     dword ptr [ecx+4]
		#fsub    dword ptr [edx+4]
		#fstp    qword ptr [eax+68h]
		#fstp    qword ptr [eax+70h]
		#fstp    qword ptr [eax+78h]
		#retn


  def test_gadget_sub_6E224350(self):
		#sub_6E224350
		gadget = "8B442404DD01DD18DD4108DD5808D9EEDD5010DD4118DD5818DD4120DD5820DD4128DD5828DD5030DD4138DD5838DD5040DD5048D9E8DD5850DD5058DD4160DD5860DD4168DD5868DD5870DD4178DD5878C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     qword ptr [ecx]
		#fstp    qword ptr [eax]
		#fld     qword ptr [ecx+8]
		#fstp    qword ptr [eax+8]
		#fldz
		#fst     qword ptr [eax+10h]
		#fld     qword ptr [ecx+18h]
		#fstp    qword ptr [eax+18h]
		#fld     qword ptr [ecx+20h]
		#fstp    qword ptr [eax+20h]
		#fld     qword ptr [ecx+28h]
		#fstp    qword ptr [eax+28h]
		#fst     qword ptr [eax+30h]
		#fld     qword ptr [ecx+38h]
		#fstp    qword ptr [eax+38h]
		#fst     qword ptr [eax+40h]
		#fst     qword ptr [eax+48h]
		#fld1
		#fstp    qword ptr [eax+50h]
		#fst     qword ptr [eax+58h]
		#fld     qword ptr [ecx+60h]
		#fstp    qword ptr [eax+60h]
		#fld     qword ptr [ecx+68h]
		#fstp    qword ptr [eax+68h]
		#fstp    qword ptr [eax+70h]
		#fld     qword ptr [ecx+78h]
		#fstp    qword ptr [eax+78h]
		#retn    4


  def test_gadget_sub_6E225E50(self):
		#sub_6E225E50
		gadget = "B814000000C3"
		self.do(gadget)

		#mov     eax, 14h
		#retn


  def test_gadget_sub_6E229300(self):
		#sub_6E229300
		gadget = "806104FC33C089410889410C89411089411489411889411C89412489412089412889412CC3"
		self.do(gadget)

		#and     byte ptr [ecx+4], 0FCh
		#xor     eax, eax
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#mov     [ecx+18h], eax
		#mov     [ecx+1Ch], eax
		#mov     [ecx+24h], eax
		#mov     [ecx+20h], eax
		#mov     [ecx+28h], eax
		#mov     [ecx+2Ch], eax
		#retn


  def test_gadget_sub_6E229330(self):
		#sub_6E229330
		gadget = "8B412C33D23B41280F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#xor     edx, edx
		#cmp     eax, [ecx+28h]
		#setnz   al
		#retn


  def test_gadget_sub_6E239540(self):
		#sub_6E239540
		gadget = "8BC18B4C24048B1189108B4904894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_ReinitializeStructuredWorkStealingQueueV_UnrealizedChoredetailsConcurrencyV_CriticalNonReentrantLock23detailsConcurrencyQAEXXZ(self):
		#ReinitializeStructuredWorkStealingQueueV_UnrealizedChoredetailsConcurrencyV_CriticalNonReentrantLock23detailsConcurrencyQAEXXZ
		gadget = "C70100000000C7410400000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx], 0
		#mov     dword ptr [ecx+4], 0
		#retn


  def test_gadget_sub_6E23AD00(self):
		#sub_6E23AD00
		gadget = "8B442404C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#retn


  def test_gadget_sub_6E23AD20(self):
		#sub_6E23AD20
		gadget = "33C0C20C00"
		self.do(gadget)

		#xor     eax, eax
		#retn    0Ch


  def test_gadget_sub_6E23B320(self):
		#sub_6E23B320
		gadget = "8B442404C70000000000C6400400C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#mov     byte ptr [eax+4], 0
		#retn    4


  def test_gadget_sub_6E23B340(self):
		#sub_6E23B340
		gadget = "8B41108B4068C3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#mov     eax, [eax+68h]
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_39(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_39
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E23B830(self):
		#sub_6E23B830
		gadget = "8A442408C20800"
		self.do(gadget)

		#mov     al, [esp+arg_4]
		#retn    8


  def test_gadget_sub_6E23BA60(self):
		#sub_6E23BA60
		gadget = "8B411C33D23B41200F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#xor     edx, edx
		#cmp     eax, [ecx+20h]
		#setnz   al
		#retn


  def test_gadget_sub_6E23BA70(self):
		#sub_6E23BA70
		gadget = "8B410C33D23B41100F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#xor     edx, edx
		#cmp     eax, [ecx+10h]
		#setnz   al
		#retn


  def test_gadget_nullsub_6(self):
		#nullsub_6
		gadget = "C20C00"
		self.do(gadget)

		#retn    0Ch


  def test_gadget_sub_6E23DA10(self):
		#sub_6E23DA10
		gadget = "C781C0000000FFFFFFFFC3"
		self.do(gadget)

		#mov     dword ptr [ecx+0C0h], 0FFFFFFFFh
		#retn


  def test_gadget_sub_6E23DA30(self):
		#sub_6E23DA30
		gadget = "33C0394424040F95C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [esp+arg_0], eax
		#setnz   al
		#retn    4


  def test_gadget_sub_6E23DA40(self):
		#sub_6E23DA40
		gadget = "C681C500000001C20400"
		self.do(gadget)

		#mov     byte ptr [ecx+0C5h], 1
		#retn    4


  def test_gadget_sub_6E23EC00(self):
		#sub_6E23EC00
		gadget = "518B442408C7042400000000C7000000000059C20800"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn    8


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_46(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_46
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__JNI_OnLoad8(self):
		#_JNI_OnLoad8
		gadget = "8B442404A3C07EA66EB802000100C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword_6EA67EC0, eax
		#mov     eax, 10002h
		#retn    8


  def test_gadget__JNI_OnUnload8(self):
		#_JNI_OnUnload8
		gadget = "C705C07EA66E00000000C20800"
		self.do(gadget)

		#mov     dword_6EA67EC0, 0
		#retn    8


  def test_gadget_sub_6E2422F0(self):
		#sub_6E2422F0
		gadget = "518B442408C7042400000000C7000000000059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 0
		#pop     ecx
		#retn


  def test_gadget_sub_6E244800(self):
		#sub_6E244800
		gadget = "8BC133C989480489480889480C89481089481489481889481C894820C7402430598A6EC7402850598A6EC7402C58598A6EC7403090598A6EC74034A0598A6EC74038AC598A6EC7403CC0598A6EC700485A8A6EC74024285A8A6EC74028205A8A6EC7402C105A8A6EC74030005A8A6EC74034F4598A6EC74038E0598A6EC7403CD0598A6EC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     dword ptr [eax+24h], offset off_6E8A5930
		#mov     dword ptr [eax+28h], offset off_6E8A5950
		#mov     dword ptr [eax+2Ch], offset off_6E8A5958
		#mov     dword ptr [eax+30h], offset off_6E8A5990
		#mov     dword ptr [eax+34h], offset off_6E8A59A0
		#mov     dword ptr [eax+38h], offset off_6E8A59AC
		#mov     dword ptr [eax+3Ch], offset off_6E8A59C0
		#mov     dword ptr [eax], offset off_6E8A5A48
		#mov     dword ptr [eax+24h], offset off_6E8A5A28
		#mov     dword ptr [eax+28h], offset off_6E8A5A20
		#mov     dword ptr [eax+2Ch], offset off_6E8A5A10
		#mov     dword ptr [eax+30h], offset off_6E8A5A00
		#mov     dword ptr [eax+34h], offset off_6E8A59F4
		#mov     dword ptr [eax+38h], offset off_6E8A59E0
		#mov     dword ptr [eax+3Ch], offset off_6E8A59D0
		#retn


  def test_gadget_sub_6E245430(self):
		#sub_6E245430
		gadget = "8A442404884111C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+11h], al
		#retn    4


  def test_gadget_sub_6E246E90(self):
		#sub_6E246E90
		gadget = "DD05285D8A6EC20400"
		self.do(gadget)

		#fld     ds:dbl_6E8A5D28
		#retn    4


  def test_gadget_sub_6E246EA0(self):
		#sub_6E246EA0
		gadget = "DD0570328A6EC20400"
		self.do(gadget)

		#fld     ds:dbl_6E8A3270
		#retn    4


  def test_gadget_j_nullsub_6(self):
		#j_nullsub_6
		gadget = "E90B6BFFFF"
		self.do(gadget)

		#jmp     nullsub_6


  def test_gadget_sub_6E246F00(self):
		#sub_6E246F00
		gadget = "32C0C20C00"
		self.do(gadget)

		#xor     al, al
		#retn    0Ch


  def test_gadget_sub_6E246F60(self):
		#sub_6E246F60
		gadget = "DD0530FD846EC3"
		self.do(gadget)

		#fld     ds:dbl_6E84FD30
		#retn


  def test_gadget_sub_6E246F70(self):
		#sub_6E246F70
		gadget = "DD05B0FD846EC3"
		self.do(gadget)

		#fld     ds:dbl_6E84FDB0
		#retn


  def test_gadget_sub_6E246F80(self):
		#sub_6E246F80
		gadget = "DD05305F8A6EC3"
		self.do(gadget)

		#fld     ds:dbl_6E8A5F30
		#retn


  def test_gadget_sub_6E246F90(self):
		#sub_6E246F90
		gadget = "B001C20C00"
		self.do(gadget)

		#mov     al, 1
		#retn    0Ch


  def test_gadget_sub_6E2494B0(self):
		#sub_6E2494B0
		gadget = "B8FFFFFF7FC3"
		self.do(gadget)

		#mov     eax, 7FFFFFFFh
		#retn


  def test_gadget_sub_6E2494C0(self):
		#sub_6E2494C0
		gadget = "DD05B8FD846EC3"
		self.do(gadget)

		#fld     ds:dbl_6E84FDB8
		#retn


  def test_gadget_sub_6E2494D0(self):
		#sub_6E2494D0
		gadget = "DD05F8328A6EC3"
		self.do(gadget)

		#fld     ds:dbl_6E8A32F8
		#retn


  def test_gadget_sub_6E24A4E0(self):
		#sub_6E24A4E0
		gadget = "8B442404A3B481A66EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword_6EA681B4, eax
		#retn


  def test_gadget_sub_6E24AE80(self):
		#sub_6E24AE80
		gadget = "D9E8C3"
		self.do(gadget)

		#fld1
		#retn


  def test_gadget_sub_6E24B2E0(self):
		#sub_6E24B2E0
		gadget = "B802000000C20400"
		self.do(gadget)

		#mov     eax, 2
		#retn    4


  def test_gadget_sub_6E24B630(self):
		#sub_6E24B630
		gadget = "8B41048B48308A813E010000C0E8032401C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     ecx, [eax+30h]
		#mov     al, [ecx+13Eh]
		#shr     al, 3
		#and     al, 1
		#retn    4


  def test_gadget_sub_6E24B650(self):
		#sub_6E24B650
		gadget = "8B41048B48308A813E010000C0E8042401C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     ecx, [eax+30h]
		#mov     al, [ecx+13Eh]
		#shr     al, 4
		#and     al, 1
		#retn    4


  def test_gadget_sub_6E2500B0(self):
		#sub_6E2500B0
		gadget = "8B49248B4424048B1189108B51048950048B51088B490C89500889480CC20400"
		self.do(gadget)

		#mov     ecx, [ecx+24h]
		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E251500(self):
		#sub_6E251500
		gadget = "8B4424048B0485985CA56EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, dword_6EA55C98[eax*4]
		#retn    4


  def test_gadget_sub_6E251720(self):
		#sub_6E251720
		gadget = "8B4424048B5110568B70088971108950088B308B510889710889108B70048B510C89710C8950045EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+10h]
		#push    esi
		#mov     esi, [eax+8]
		#mov     [ecx+10h], esi
		#mov     [eax+8], edx
		#mov     esi, [eax]
		#mov     edx, [ecx+8]
		#mov     [ecx+8], esi
		#mov     [eax], edx
		#mov     esi, [eax+4]
		#mov     edx, [ecx+0Ch]
		#mov     [ecx+0Ch], esi
		#mov     [eax+4], edx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E2588D0(self):
		#sub_6E2588D0
		gadget = "8B41088B4004C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     eax, [eax+4]
		#retn


  def test_gadget_sub_6E2588E0(self):
		#sub_6E2588E0
		gadget = "8B41088B4C2404894804C20400"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E2588F0(self):
		#sub_6E2588F0
		gadget = "8B410883C008C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#add     eax, 8
		#retn


  def test_gadget_sub_6E258900(self):
		#sub_6E258900
		gadget = "8B41088B00C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     eax, [eax]
		#retn


  def test_gadget_sub_6E2594B0(self):
		#sub_6E2594B0
		gadget = "8BC1C7003C6B8A6EC3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_6E8A6B3C
		#retn


  def test_gadget_sub_6E2594C0(self):
		#sub_6E2594C0
		gadget = "C7013C6B8A6EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E8A6B3C
		#retn


  def test_gadget_sub_6E2595E0(self):
		#sub_6E2595E0
		gadget = "DB442404DC35A00C856EDC4108C20400"
		self.do(gadget)

		#fild    [esp+arg_0]
		#fdiv    ds:dbl_6E850CA0
		#fadd    qword ptr [ecx+8]
		#retn    4


  def test_gadget_sub_6E25AC70(self):
		#sub_6E25AC70
		gadget = "6AFF68B9007A6E64A1000000005051A1F44AA66E33C4508D44240864A300000000C7442404000000008B4424188B4C241C89088B4C240864890D000000005983C410C20800"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7A00B9
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#mov     [esp+14h+var_10], 0
		#mov     eax, [esp+14h+arg_0]
		#mov     ecx, [esp+14h+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn    8


  def test_gadget_sub_6E25B5B0(self):
		#sub_6E25B5B0
		gadget = "8D4130C3"
		self.do(gadget)

		#lea     eax, [ecx+30h]
		#retn


  def test_gadget_sub_6E25B5C0(self):
		#sub_6E25B5C0
		gadget = "8B41388B513CC3"
		self.do(gadget)

		#mov     eax, [ecx+38h]
		#mov     edx, [ecx+3Ch]
		#retn


  def test_gadget_sub_6E25B5D0(self):
		#sub_6E25B5D0
		gadget = "8B4424048B54240880A180000000FE89413889513CC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#and     byte ptr [ecx+80h], 0FEh
		#mov     [ecx+38h], eax
		#mov     [ecx+3Ch], edx
		#retn    8


  def test_gadget_sub_6E25B5F0(self):
		#sub_6E25B5F0
		gadget = "8B442404894148C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+48h], eax
		#retn    4


  def test_gadget_sub_6E25B600(self):
		#sub_6E25B600
		gadget = "8A41702401C3"
		self.do(gadget)

		#mov     al, [ecx+70h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E25B610(self):
		#sub_6E25B610
		gadget = "8A41782401C3"
		self.do(gadget)

		#mov     al, [ecx+78h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E25B620(self):
		#sub_6E25B620
		gadget = "8B4174C3"
		self.do(gadget)

		#mov     eax, [ecx+74h]
		#retn


  def test_gadget_sub_6E25B630(self):
		#sub_6E25B630
		gadget = "8B417CC3"
		self.do(gadget)

		#mov     eax, [ecx+7Ch]
		#retn


  def test_gadget_sub_6E25DBB0(self):
		#sub_6E25DBB0
		gadget = "6AFF6809087A6E64A1000000005051A1F44AA66E33C4508D44240864A300000000C7442404000000008B4424188B4C241C89088B4C240864890D000000005983C410C20800"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7A0809
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#mov     [esp+14h+var_10], 0
		#mov     eax, [esp+14h+arg_0]
		#mov     ecx, [esp+14h+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn    8


  def test_gadget_sub_6E260B70(self):
		#sub_6E260B70
		gadget = "8B0133C939480C0F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#xor     ecx, ecx
		#cmp     [eax+0Ch], ecx
		#setnz   al
		#retn


  def test_gadget_sub_6E261130(self):
		#sub_6E261130
		gadget = "C70144BC896EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E89BC44
		#retn


  def test_gadget_sub_6E261140(self):
		#sub_6E261140
		gadget = "8B442404A37C83A66EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword_6EA6837C, eax
		#retn


  def test_gadget_sub_6E2624B0(self):
		#sub_6E2624B0
		gadget = "8BC133C9C700BC6E8A6E8948048B500881E215FEFFFF83CA1589500889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8A6EBC
		#mov     [eax+4], ecx
		#mov     edx, [eax+8]
		#and     edx, 0FFFFFE15h
		#or      edx, 15h
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_6E262CF0(self):
		#sub_6E262CF0
		gadget = "8B442404D900D95908D94004D9590CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     dword ptr [eax]
		#fstp    dword ptr [ecx+8]
		#fld     dword ptr [eax+4]
		#fstp    dword ptr [ecx+0Ch]
		#retn    4


  def test_gadget_sub_6E262D10(self):
		#sub_6E262D10
		gadget = "8B442404D94108D918D9410CD95804C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     dword ptr [ecx+8]
		#fstp    dword ptr [eax]
		#fld     dword ptr [ecx+0Ch]
		#fstp    dword ptr [eax+4]
		#retn    4


  def test_gadget_sub_6E263390(self):
		#sub_6E263390
		gadget = "DB44240C8B442404D9E88B542408DEF189414C895150D95954C20C00"
		self.do(gadget)

		#fild    [esp+arg_8]
		#mov     eax, [esp+arg_0]
		#fld1
		#mov     edx, [esp+arg_4]
		#fdivrp  st(1), st
		#mov     [ecx+4Ch], eax
		#mov     [ecx+50h], edx
		#fstp    dword ptr [ecx+54h]
		#retn    0Ch


  def test_gadget_sub_6E263A20(self):
		#sub_6E263A20
		gadget = "8B41E0C3"
		self.do(gadget)

		#mov     eax, [ecx-20h]
		#retn


  def test_gadget_sub_6E263AD0(self):
		#sub_6E263AD0
		gadget = "D9411CC3"
		self.do(gadget)

		#fld     dword ptr [ecx+1Ch]
		#retn


  def test_gadget_sub_6E263AE0(self):
		#sub_6E263AE0
		gadget = "8B41182B4114C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#sub     eax, [ecx+14h]
		#retn


  def test_gadget_sub_6E263AF0(self):
		#sub_6E263AF0
		gadget = "8A8192000000C3"
		self.do(gadget)

		#mov     al, [ecx+92h]
		#retn


  def test_gadget_sub_6E263B00(self):
		#sub_6E263B00
		gadget = "8A442404888192000000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+92h], al
		#retn    4


  def test_gadget_sub_6E264500(self):
		#sub_6E264500
		gadget = "8B4C240C8B4424048B1189108B51048950048B51088B490C89500889480CC20C00"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    0Ch


  def test_gadget_sub_6E264530(self):
		#sub_6E264530
		gadget = "8B44240433C9890889480489480889480CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn    10h


  def test_gadget_sub_6E2655B0(self):
		#sub_6E2655B0
		gadget = "8B91880000008B4424048B898C0000008910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+88h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+8Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E2655D0(self):
		#sub_6E2655D0
		gadget = "8A81AD000000C3"
		self.do(gadget)

		#mov     al, [ecx+0ADh]
		#retn


  def test_gadget_sub_6E2655E0(self):
		#sub_6E2655E0
		gadget = "8B51688B4424048B496C8910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+68h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+6Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E269470(self):
		#sub_6E269470
		gadget = "8B4424048B5108568B70088971088950088B308B11893189108B70048B51048971048950045EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+8]
		#push    esi
		#mov     esi, [eax+8]
		#mov     [ecx+8], esi
		#mov     [eax+8], edx
		#mov     esi, [eax]
		#mov     edx, [ecx]
		#mov     [ecx], esi
		#mov     [eax], edx
		#mov     esi, [eax+4]
		#mov     edx, [ecx+4]
		#mov     [ecx+4], esi
		#mov     [eax+4], edx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E26B3A0(self):
		#sub_6E26B3A0
		gadget = "8A5424088BC18B4C24048908C6400400885005C20800"
		self.do(gadget)

		#mov     dl, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     byte ptr [eax+4], 0
		#mov     [eax+5], dl
		#retn    8


  def test_gadget_sub_6E26B5C0(self):
		#sub_6E26B5C0
		gadget = "C6413401C3"
		self.do(gadget)

		#mov     byte ptr [ecx+34h], 1
		#retn


  def test_gadget_unknown_libname_7(self):
		#unknown_libname_7
		gadget = "8B49208B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+20h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E26B7C0(self):
		#sub_6E26B7C0
		gadget = "8B118B4424048B49048910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+4]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E26C8B0(self):
		#sub_6E26C8B0
		gadget = "C6413600C7413810C7266EC7413CC0C7266EC3"
		self.do(gadget)

		#mov     byte ptr [ecx+36h], 0
		#mov     dword ptr [ecx+38h], offset sub_6E26C710
		#mov     dword ptr [ecx+3Ch], offset sub_6E26C7C0
		#retn


  def test_gadget_sub_6E26CAC0(self):
		#sub_6E26CAC0
		gadget = "8B44240833C985C00F9FC14923C1C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#xor     ecx, ecx
		#test    eax, eax
		#setnle  cl
		#dec     ecx
		#and     eax, ecx
		#retn


  def test_gadget_sub_6E26CAD0(self):
		#sub_6E26CAD0
		gadget = "8B44240833C985C00F9EC14923C1C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#xor     ecx, ecx
		#test    eax, eax
		#setle   cl
		#dec     ecx
		#and     eax, ecx
		#retn


  def test_gadget_sub_6E26CEE0(self):
		#sub_6E26CEE0
		gadget = "C70154758A6EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E8A7554
		#retn


  def test_gadget_sub_6E26F4F0(self):
		#sub_6E26F4F0
		gadget = "83EC088B4C241833C089018B44240489410432C083C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_C]
		#xor     eax, eax
		#mov     [ecx], eax
		#mov     eax, [esp+8+var_4]
		#mov     [ecx+4], eax
		#xor     al, al
		#add     esp, 8
		#retn


  def test_gadget_sub_6E26F570(self):
		#sub_6E26F570
		gadget = "33C038056084A66E0F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     byte_6EA68460, al
		#setz    al
		#retn


  def test_gadget_sub_6E273640(self):
		#sub_6E273640
		gadget = "D9EE8BC1DD5008C700AC7B8A6EDD5010C74020FFFFFFFFDD5818C7402800000000C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fst     qword ptr [eax+8]
		#mov     dword ptr [eax], offset off_6E8A7BAC
		#fst     qword ptr [eax+10h]
		#mov     dword ptr [eax+20h], 0FFFFFFFFh
		#fstp    qword ptr [eax+18h]
		#mov     dword ptr [eax+28h], 0
		#retn


  def test_gadget_sub_6E275260(self):
		#sub_6E275260
		gadget = "A18C84A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6848C
		#retn


  def test_gadget_sub_6E276380(self):
		#sub_6E276380
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483C89484089484489484889484C89485089485489485889485C89486089486489486889486C89487089487489487889487C898880000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], ecx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+68h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], ecx
		#mov     [eax+74h], ecx
		#mov     [eax+78h], ecx
		#mov     [eax+7Ch], ecx
		#mov     [eax+80h], ecx
		#retn


  def test_gadget_sub_6E279C40(self):
		#sub_6E279C40
		gadget = "8BC18B4C2404894804C700C47D8A6E8D501089500833C98988B000000056BA0400000089500C8DB0BC0000008988CC00000089B0B40000008990B80000008A88D000000080E1FE80C9028888D00000005EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#mov     dword ptr [eax], offset off_6E8A7DC4
		#lea     edx, [eax+10h]
		#mov     [eax+8], edx
		#xor     ecx, ecx
		#mov     [eax+0B0h], ecx
		#push    esi
		#mov     edx, 4
		#mov     [eax+0Ch], edx
		#lea     esi, [eax+0BCh]
		#mov     [eax+0CCh], ecx
		#mov     [eax+0B4h], esi
		#mov     [eax+0B8h], edx
		#mov     cl, [eax+0D0h]
		#and     cl, 0FEh
		#or      cl, 2
		#mov     [eax+0D0h], cl
		#pop     esi
		#retn    4


  def test_gadget_sub_6E27C5A0(self):
		#sub_6E27C5A0
		gadget = "8B442404DB00DC0D10E1846ED95C2404D9442404D8442408D95C2404D9442404C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#fadd    [esp+arg_4]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn


  def test_gadget_sub_6E27E760(self):
		#sub_6E27E760
		gadget = "518B54240C8BC18B4C2408C70074828A6ED94104D91C24D94204D95C2408D901D8028B542410D95804D9442408D80424D95808D94104D95C2408D94204D95C240CD901D802D9580CD9442408D844240CD95810C74014FFFFFFFFC740180100000059C20C00"
		self.do(gadget)

		#push    ecx
		#mov     edx, [esp+4+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+4+arg_0]
		#mov     dword ptr [eax], offset off_6E8A8274
		#fld     dword ptr [ecx+4]
		#fstp    [esp+4+var_4]
		#fld     dword ptr [edx+4]
		#fstp    [esp+4+arg_0]
		#fld     dword ptr [ecx]
		#fadd    dword ptr [edx]
		#mov     edx, [esp+4+arg_8]
		#fstp    dword ptr [eax+4]
		#fld     [esp+4+arg_0]
		#fadd    [esp+4+var_4]
		#fstp    dword ptr [eax+8]
		#fld     dword ptr [ecx+4]
		#fstp    [esp+4+arg_0]
		#fld     dword ptr [edx+4]
		#fstp    [esp+4+arg_4]
		#fld     dword ptr [ecx]
		#fadd    dword ptr [edx]
		#fstp    dword ptr [eax+0Ch]
		#fld     [esp+4+arg_0]
		#fadd    [esp+4+arg_4]
		#fstp    dword ptr [eax+10h]
		#mov     dword ptr [eax+14h], 0FFFFFFFFh
		#mov     dword ptr [eax+18h], 1
		#pop     ecx
		#retn    0Ch


  def test_gadget_sub_6E27E7D0(self):
		#sub_6E27E7D0
		gadget = "83EC108BC18B4C2414C70074828A6E8B51088914248B510C895424048B5110895424088B51148954240C8B54241CD9420456D95C2418D902D8442404D95804D9442418D944241CD9C0DEC2D9C9D958088B7108897424048B710C897424088B71108B49148974240CD944240CD8442404894C24105ED91C24D94204D95C2414D902D80424D9580CD8442414D95810C74014FFFFFFFFC740180200000083C410C20C00"
		self.do(gadget)

		#sub     esp, 10h
		#mov     eax, ecx
		#mov     ecx, [esp+10h+arg_0]
		#mov     dword ptr [eax], offset off_6E8A8274
		#mov     edx, [ecx+8]
		#mov     [esp+10h+var_10], edx
		#mov     edx, [ecx+0Ch]
		#mov     [esp+10h+var_C], edx
		#mov     edx, [ecx+10h]
		#mov     [esp+10h+var_8], edx
		#mov     edx, [ecx+14h]
		#mov     [esp+10h+var_4], edx
		#mov     edx, [esp+10h+arg_8]
		#fld     dword ptr [edx+4]
		#push    esi
		#fstp    [esp+14h+arg_0]
		#fld     dword ptr [edx]
		#fadd    [esp+14h+var_10]
		#fstp    dword ptr [eax+4]
		#fld     [esp+14h+arg_0]
		#fld     [esp+14h+arg_4]
		#fld     st
		#faddp   st(2), st
		#fxch    st(1)
		#fstp    dword ptr [eax+8]
		#mov     esi, [ecx+8]
		#mov     [esp+14h+var_10], esi
		#mov     esi, [ecx+0Ch]
		#mov     [esp+14h+var_C], esi
		#mov     esi, [ecx+10h]
		#mov     ecx, [ecx+14h]
		#mov     [esp+14h+var_8], esi
		#fld     [esp+14h+var_8]
		#fadd    [esp+14h+var_10]
		#mov     [esp+14h+var_4], ecx
		#pop     esi
		#fstp    [esp+10h+var_10]
		#fld     dword ptr [edx+4]
		#fstp    [esp+10h+arg_0]
		#fld     dword ptr [edx]
		#fadd    [esp+10h+var_10]
		#fstp    dword ptr [eax+0Ch]
		#fadd    [esp+10h+arg_0]
		#fstp    dword ptr [eax+10h]
		#mov     dword ptr [eax+14h], 0FFFFFFFFh
		#mov     dword ptr [eax+18h], 2
		#add     esp, 10h
		#retn    0Ch


  def test_gadget_sub_6E282E80(self):
		#sub_6E282E80
		gadget = "8BC1D9EE8B4C2404C700A8828A6E8B118950108B51048950148B51088950188B490C89481C8B4C24088B118950208B4904894824D95028D9502CD95030D95034D95038D9503CD95040D95044D95048D9504CD95050D95854806058FCC20800"
		self.do(gadget)

		#mov     eax, ecx
		#fldz
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8A82A8
		#mov     edx, [ecx]
		#mov     [eax+10h], edx
		#mov     edx, [ecx+4]
		#mov     [eax+14h], edx
		#mov     edx, [ecx+8]
		#mov     [eax+18h], edx
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_4]
		#mov     edx, [ecx]
		#mov     [eax+20h], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+24h], ecx
		#fst     dword ptr [eax+28h]
		#fst     dword ptr [eax+2Ch]
		#fst     dword ptr [eax+30h]
		#fst     dword ptr [eax+34h]
		#fst     dword ptr [eax+38h]
		#fst     dword ptr [eax+3Ch]
		#fst     dword ptr [eax+40h]
		#fst     dword ptr [eax+44h]
		#fst     dword ptr [eax+48h]
		#fst     dword ptr [eax+4Ch]
		#fst     dword ptr [eax+50h]
		#fstp    dword ptr [eax+54h]
		#and     byte ptr [eax+58h], 0FCh
		#retn    8


  def test_gadget_sub_6E2834C0(self):
		#sub_6E2834C0
		gadget = "8A4128C3"
		self.do(gadget)

		#mov     al, [ecx+28h]
		#retn


  def test_gadget_sub_6E284A40(self):
		#sub_6E284A40
		gadget = "8BC18B4C24048B5108568B71048B0989088B4C240C8970048950088B71048B51088B0989701089480C8950145EC20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx+8]
		#push    esi
		#mov     esi, [ecx+4]
		#mov     ecx, [ecx]
		#mov     [eax], ecx
		#mov     ecx, [esp+4+arg_4]
		#mov     [eax+4], esi
		#mov     [eax+8], edx
		#mov     esi, [ecx+4]
		#mov     edx, [ecx+8]
		#mov     ecx, [ecx]
		#mov     [eax+10h], esi
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], edx
		#pop     esi
		#retn    8


  def test_gadget_sub_6E284EC0(self):
		#sub_6E284EC0
		gadget = "D9410CD84C2404D95C2404D9442404C20400"
		self.do(gadget)

		#fld     dword ptr [ecx+0Ch]
		#fmul    [esp+arg_0]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn    4


  def test_gadget_sub_6E284EE0(self):
		#sub_6E284EE0
		gadget = "D94110D84C2404D95C2404D9442404C20400"
		self.do(gadget)

		#fld     dword ptr [ecx+10h]
		#fmul    [esp+arg_0]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn    4


  def test_gadget_sub_6E284F00(self):
		#sub_6E284F00
		gadget = "D9EE8B442404D910D95804C20800"
		self.do(gadget)

		#fldz
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fstp    dword ptr [eax+4]
		#retn    8


  def test_gadget_sub_6E285A80(self):
		#sub_6E285A80
		gadget = "8B4424048B511889108B511C8950048B51208B492489500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+18h]
		#mov     [eax], edx
		#mov     edx, [ecx+1Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx+20h]
		#mov     ecx, [ecx+24h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E285AA0(self):
		#sub_6E285AA0
		gadget = "8B4424048B108951288B500489512C8B50088951308B400C894134C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+28h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+2Ch], edx
		#mov     edx, [eax+8]
		#mov     [ecx+30h], edx
		#mov     eax, [eax+0Ch]
		#mov     [ecx+34h], eax
		#retn    4


  def test_gadget_sub_6E285AC0(self):
		#sub_6E285AC0
		gadget = "8B4424048B512889108B512C8950048B51308B493489500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+28h]
		#mov     [eax], edx
		#mov     edx, [ecx+2Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx+30h]
		#mov     ecx, [ecx+34h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E287AC0(self):
		#sub_6E287AC0
		gadget = "D94424048B442408DB00DC0D10E1846ED95C2404D8642404D95C2404D9442404C3"
		self.do(gadget)

		#fld     [esp+arg_0]
		#mov     eax, [esp+arg_4]
		#fild    dword ptr [eax]
		#fmul    ds:dbl_6E84E110
		#fstp    [esp+arg_0]
		#fsub    [esp+arg_0]
		#fstp    [esp+arg_0]
		#fld     [esp+arg_0]
		#retn


  def test_gadget_sub_6E287DB0(self):
		#sub_6E287DB0
		gadget = "8BC18B4C240489480433C9C700F8838A6E89480889480C894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8A83F8
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E2899F0(self):
		#sub_6E2899F0
		gadget = "8B5424048BC18B0A89088B4A048948048B4A088948088B4A0C89480C8B4A108948108B4A148948148B4A188948188B4A1C5689481C578D72208D7820B908000000F3A58B4A408948408A4A448848448A52455F8850455EC20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [edx]
		#mov     [eax], ecx
		#mov     ecx, [edx+4]
		#mov     [eax+4], ecx
		#mov     ecx, [edx+8]
		#mov     [eax+8], ecx
		#mov     ecx, [edx+0Ch]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [edx+10h]
		#mov     [eax+10h], ecx
		#mov     ecx, [edx+14h]
		#mov     [eax+14h], ecx
		#mov     ecx, [edx+18h]
		#mov     [eax+18h], ecx
		#mov     ecx, [edx+1Ch]
		#push    esi
		#mov     [eax+1Ch], ecx
		#push    edi
		#lea     esi, [edx+20h]
		#lea     edi, [eax+20h]
		#mov     ecx, 8
		#rep movsd
		#mov     ecx, [edx+40h]
		#mov     [eax+40h], ecx
		#mov     cl, [edx+44h]
		#mov     [eax+44h], cl
		#mov     dl, [edx+45h]
		#pop     edi
		#mov     [eax+45h], dl
		#pop     esi
		#retn    4


  def test_gadget_sub_6E289B30(self):
		#sub_6E289B30
		gadget = "D9EE8BC133C9890889480489480889480C894810894814D95018D9501CD95020D95024D95028D9502CD95030D95034D95038D9583C89484066C740440001C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#fst     dword ptr [eax+18h]
		#fst     dword ptr [eax+1Ch]
		#fst     dword ptr [eax+20h]
		#fst     dword ptr [eax+24h]
		#fst     dword ptr [eax+28h]
		#fst     dword ptr [eax+2Ch]
		#fst     dword ptr [eax+30h]
		#fst     dword ptr [eax+34h]
		#fst     dword ptr [eax+38h]
		#fstp    dword ptr [eax+3Ch]
		#mov     [eax+40h], ecx
		#mov     word ptr [eax+44h], 100h
		#retn


  def test_gadget_sub_6E28C400(self):
		#sub_6E28C400
		gadget = "D9411C8B442414D800D918D9055021856EC21800"
		self.do(gadget)

		#fld     dword ptr [ecx+1Ch]
		#mov     eax, [esp+arg_10]
		#fadd    dword ptr [eax]
		#fstp    dword ptr [eax]
		#fld     ds:flt_6E852150
		#retn    18h


  def test_gadget_sub_6E28C980(self):
		#sub_6E28C980
		gadget = "8B41100FB6401B83E007C3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#movzx   eax, byte ptr [eax+1Bh]
		#and     eax, 7
		#retn


  def test_gadget_sub_6E28CCF0(self):
		#sub_6E28CCF0
		gadget = "8BC18B4C24048B1189108B51048950048B51088950088B490C89480C8B4C24088B118950108B51048950148B51088950188B490C89481CC7402000000000C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+arg_4]
		#mov     edx, [ecx]
		#mov     [eax+10h], edx
		#mov     edx, [ecx+4]
		#mov     [eax+14h], edx
		#mov     edx, [ecx+8]
		#mov     [eax+18h], edx
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+1Ch], ecx
		#mov     dword ptr [eax+20h], 0
		#retn    8


  def test_gadget_sub_6E28CDC0(self):
		#sub_6E28CDC0
		gadget = "8B411083C028C3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#add     eax, 28h
		#retn


  def test_gadget_sub_6E2931F0(self):
		#sub_6E2931F0
		gadget = "0FB7413003412CC3"
		self.do(gadget)

		#movzx   eax, word ptr [ecx+30h]
		#add     eax, [ecx+2Ch]
		#retn


  def test_gadget_sub_6E293290(self):
		#sub_6E293290
		gadget = "0FB6442404C1E0083341202500010000314120C20400"
		self.do(gadget)

		#movzx   eax, [esp+arg_0]
		#shl     eax, 8
		#xor     eax, [ecx+20h]
		#and     eax, 100h
		#xor     [ecx+20h], eax
		#retn    4


  def test_gadget_sub_6E2988E0(self):
		#sub_6E2988E0
		gadget = "8B410C8B503C89513C8B50408951408B50448951448B4004894104C3"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     edx, [eax+3Ch]
		#mov     [ecx+3Ch], edx
		#mov     edx, [eax+40h]
		#mov     [ecx+40h], edx
		#mov     edx, [eax+44h]
		#mov     [ecx+44h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+4], eax
		#retn


  def test_gadget_sub_6E2992D0(self):
		#sub_6E2992D0
		gadget = "83C8FFC20400"
		self.do(gadget)

		#or      eax, 0FFFFFFFFh
		#retn    4


  def test_gadget_sub_6E2992E0(self):
		#sub_6E2992E0
		gadget = "8B51508B4424048B49548910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+50h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+54h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_GetLocationVirtualProcessordetailsConcurrencyQBEABVlocation3XZ(self):
		#GetLocationVirtualProcessordetailsConcurrencyQBEABVlocation3XZ
		gadget = "8D8188000000C3"
		self.do(gadget)

		#lea     eax, [ecx+88h]
		#retn


  def test_gadget_sub_6E299310(self):
		#sub_6E299310
		gadget = "B888888A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderapplet; "RenderApplet"
		#retn


  def test_gadget_sub_6E2994F0(self):
		#sub_6E2994F0
		gadget = "8B44240429812404000083C003C1E80203C003C0C1E8028B548124568B74240C897481248B412033C289065EC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#sub     [ecx+424h], eax
		#add     eax, 3
		#shr     eax, 2
		#add     eax, eax
		#add     eax, eax
		#shr     eax, 2
		#mov     edx, [ecx+eax*4+24h]
		#push    esi
		#mov     esi, [esp+4+arg_4]
		#mov     [ecx+eax*4+24h], esi
		#mov     eax, [ecx+20h]
		#xor     eax, edx
		#mov     [esi], eax
		#pop     esi
		#retn    8


  def test_gadget_sub_6E2999A0(self):
		#sub_6E2999A0
		gadget = "8BC18B4C240833D28910895004568B318970088B710489700C8B71088970108B490C8950188B501C8948148B4C240883E2F483E1030BD183CA1489501C5EC20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#xor     edx, edx
		#mov     [eax], edx
		#mov     [eax+4], edx
		#push    esi
		#mov     esi, [ecx]
		#mov     [eax+8], esi
		#mov     esi, [ecx+4]
		#mov     [eax+0Ch], esi
		#mov     esi, [ecx+8]
		#mov     [eax+10h], esi
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+18h], edx
		#mov     edx, [eax+1Ch]
		#mov     [eax+14h], ecx
		#mov     ecx, [esp+4+arg_0]
		#and     edx, 0FFFFFFF4h
		#and     ecx, 3
		#or      edx, ecx
		#or      edx, 14h
		#mov     [eax+1Ch], edx
		#pop     esi
		#retn    8


  def test_gadget_sub_6E299AC0(self):
		#sub_6E299AC0
		gadget = "833DB484A66E000F95C0C3"
		self.do(gadget)

		#cmp     dword_6EA684B4, 0
		#setnz   al
		#retn


  def test_gadget_sub_6E299AD0(self):
		#sub_6E299AD0
		gadget = "8B4424048B4010C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+10h]
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_30(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_30
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_47(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_47
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E2B7FD0(self):
		#sub_6E2B7FD0
		gadget = "518B4120D9411C8B542408C1F814890424DA2424C1E214D9591C8B4120DB44240825FFFF0F000BD0895120D8411CD9591C59C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [ecx+20h]
		#fld     dword ptr [ecx+1Ch]
		#mov     edx, [esp+4+arg_0]
		#sar     eax, 14h
		#mov     [esp+4+var_4], eax
		#fisub   [esp+4+var_4]
		#shl     edx, 14h
		#fstp    dword ptr [ecx+1Ch]
		#mov     eax, [ecx+20h]
		#fild    [esp+4+arg_0]
		#and     eax, 0FFFFFh
		#or      edx, eax
		#mov     [ecx+20h], edx
		#fadd    dword ptr [ecx+1Ch]
		#fstp    dword ptr [ecx+1Ch]
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E2B82A0(self):
		#sub_6E2B82A0
		gadget = "83492002C3"
		self.do(gadget)

		#or      dword ptr [ecx+20h], 2
		#retn


  def test_gadget_sub_6E2BCE10(self):
		#sub_6E2BCE10
		gadget = "8BC133C9890889480489480883CAFF89500C89501C89481089481489481889502C89482089482489482889503C89483089483489483856BE0D00000089704089704489704889484C89705089506089485489485889485C88486489507489486889486C894870C640780189487C89888000000089888400000089888800000089888C00000089889000000089889400000089889800000089889C0000008888A00000008988A40000008988A80000008988AC0000008988B00000008D90BC0000008990B4000000C780B8000000080000008988FC0000005EC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#or      edx, 0FFFFFFFFh
		#mov     [eax+0Ch], edx
		#mov     [eax+1Ch], edx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+2Ch], edx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+3Ch], edx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#push    esi
		#mov     esi, 0Dh
		#mov     [eax+40h], esi
		#mov     [eax+44h], esi
		#mov     [eax+48h], esi
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], esi
		#mov     [eax+60h], edx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], ecx
		#mov     [eax+64h], cl
		#mov     [eax+74h], edx
		#mov     [eax+68h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], ecx
		#mov     byte ptr [eax+78h], 1
		#mov     [eax+7Ch], ecx
		#mov     [eax+80h], ecx
		#mov     [eax+84h], ecx
		#mov     [eax+88h], ecx
		#mov     [eax+8Ch], ecx
		#mov     [eax+90h], ecx
		#mov     [eax+94h], ecx
		#mov     [eax+98h], ecx
		#mov     [eax+9Ch], ecx
		#mov     [eax+0A0h], cl
		#mov     [eax+0A4h], ecx
		#mov     [eax+0A8h], ecx
		#mov     [eax+0ACh], ecx
		#mov     [eax+0B0h], ecx
		#lea     edx, [eax+0BCh]
		#mov     [eax+0B4h], edx
		#mov     dword ptr [eax+0B8h], 8
		#mov     [eax+0FCh], ecx
		#pop     esi
		#retn


  def test_gadget_sub_6E2C6770(self):
		#sub_6E2C6770
		gadget = "8B491C8B517C8B4424048B89800000008910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+1Ch]
		#mov     edx, [ecx+7Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+80h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E2C7620(self):
		#sub_6E2C7620
		gadget = "8B491C8B51748B442404C1E20689108B4978C1E106894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+1Ch]
		#mov     edx, [ecx+74h]
		#mov     eax, [esp+arg_0]
		#shl     edx, 6
		#mov     [eax], edx
		#mov     ecx, [ecx+78h]
		#shl     ecx, 6
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E2D7170(self):
		#sub_6E2D7170
		gadget = "8BC18B4C240489088B4C24088B118950048B51048950088B510889500C8B490C8B54240C8948108B4C24108950148B5424148948188B4C241889501C8B54241C8948208B4C24208950248B54242489482889502CC22400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     ecx, [esp+arg_4]
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     edx, [ecx+4]
		#mov     [eax+8], edx
		#mov     edx, [ecx+8]
		#mov     [eax+0Ch], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_8]
		#mov     [eax+10h], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+14h], edx
		#mov     edx, [esp+arg_10]
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_14]
		#mov     [eax+1Ch], edx
		#mov     edx, [esp+arg_18]
		#mov     [eax+20h], ecx
		#mov     ecx, [esp+arg_1C]
		#mov     [eax+24h], edx
		#mov     edx, [esp+arg_20]
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], edx
		#retn    24h


  def test_gadget_sub_6E2D7B50(self):
		#sub_6E2D7B50
		gadget = "8B44240433C9890889480489480889480CC20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn    0Ch


  def test_gadget_sub_6E2D7B70(self):
		#sub_6E2D7B70
		gadget = "8B442404C1E0183341182500000007314118C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#shl     eax, 18h
		#xor     eax, [ecx+18h]
		#and     eax, 7000000h
		#xor     [ecx+18h], eax
		#retn    4


  def test_gadget_sub_6E2E2510(self):
		#sub_6E2E2510
		gadget = "B8AC998A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderbr; "RenderBR"
		#retn


  def test_gadget_sub_6E2E2520(self):
		#sub_6E2E2520
		gadget = "D9EEC21800"
		self.do(gadget)

		#fldz
		#retn    18h


  def test_gadget_sub_6E2E2950(self):
		#sub_6E2E2950
		gadget = "B8149E8A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderbutton; "RenderButton"
		#retn


  def test_gadget_sub_6E2E3380(self):
		#sub_6E2E3380
		gadget = "B8FCA08A6EC3"
		self.do(gadget)

		#mov     eax, offset aRendercombinet; "RenderCombineText"
		#retn


  def test_gadget_sub_6E2E3870(self):
		#sub_6E2E3870
		gadget = "B82CA18A6EC3"
		self.do(gadget)

		#mov     eax, offset aRendercounter; "RenderCounter"
		#retn


  def test_gadget_sub_6E2E62E0(self):
		#sub_6E2E62E0
		gadget = "8A416CC3"
		self.do(gadget)

		#mov     al, [ecx+6Ch]
		#retn


  def test_gadget_sub_6E2EB490(self):
		#sub_6E2EB490
		gadget = "B87CAD8A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderdetailsm; "RenderDetailsMarker"
		#retn


  def test_gadget_sub_6E2EBD60(self):
		#sub_6E2EBD60
		gadget = "8A4179C3"
		self.do(gadget)

		#mov     al, [ecx+79h]
		#retn


  def test_gadget_sub_6E2ED660(self):
		#sub_6E2ED660
		gadget = "B84CB68A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderfieldset; "RenderFieldSet"
		#retn


  def test_gadget_sub_6E2EE060(self):
		#sub_6E2EE060
		gadget = "B8A4BA8A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderfileuplo; "RenderFileUploadControl"
		#retn


  def test_gadget_sub_6E2EE920(self):
		#sub_6E2EE920
		gadget = "518B442408836008F833C980600CFE890C248908894804C740100100000059C20800"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#and     dword ptr [eax+8], 0FFFFFFF8h
		#xor     ecx, ecx
		#and     byte ptr [eax+0Ch], 0FEh
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     dword ptr [eax+10h], 1
		#pop     ecx
		#retn    8


  def test_gadget_sub_6E2EEF40(self):
		#sub_6E2EEF40
		gadget = "B8CCBA8A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderflexible; "RenderFlexibleBox"
		#retn


  def test_gadget_sub_6E2F5860(self):
		#sub_6E2F5860
		gadget = "8B4424048B50148951148B50188951188B501C89511C8B4020894120C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax+14h]
		#mov     [ecx+14h], edx
		#mov     edx, [eax+18h]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+1Ch]
		#mov     [ecx+1Ch], edx
		#mov     eax, [eax+20h]
		#mov     [ecx+20h], eax
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_31(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_31
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E2F8CF0(self):
		#sub_6E2F8CF0
		gadget = "80A110010000DFC3"
		self.do(gadget)

		#and     byte ptr [ecx+110h], 0DFh
		#retn


  def test_gadget_sub_6E2F8D00(self):
		#sub_6E2F8D00
		gadget = "8B442404C70000000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0
		#retn    4


  def test_gadget_sub_6E2F9A70(self):
		#sub_6E2F9A70
		gadget = "B8D8C78A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderframe; "RenderFrame"
		#retn


  def test_gadget_sub_6E2F9D20(self):
		#sub_6E2F9D20
		gadget = "B800CC8A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderpart; "RenderPart"
		#retn


  def test_gadget_sub_6E2FA950(self):
		#sub_6E2FA950
		gadget = "8D4150C3"
		self.do(gadget)

		#lea     eax, [ecx+50h]
		#retn


  def test_gadget_sub_6E2FA960(self):
		#sub_6E2FA960
		gadget = "B8F8CF8A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderframeset; "RenderFrameSet"
		#retn


  def test_gadget_sub_6E2FD210(self):
		#sub_6E2FD210
		gadget = "8BC133C989480489480889480CC700FFFFFFFF8988980200008D5018895010C740142000000089889C0200008988A00200008B4C24048988A4020000C20400"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     dword ptr [eax], 0FFFFFFFFh
		#mov     [eax+298h], ecx
		#lea     edx, [eax+18h]
		#mov     [eax+10h], edx
		#mov     dword ptr [eax+14h], 20h
		#mov     [eax+29Ch], ecx
		#mov     [eax+2A0h], ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+2A4h], ecx
		#retn    4


  def test_gadget_sub_6E2FD4E0(self):
		#sub_6E2FD4E0
		gadget = "8B4424040101C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     [ecx], eax
		#retn    4


  def test_gadget_sub_6E2FD4F0(self):
		#sub_6E2FD4F0
		gadget = "8B098B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E300AE0(self):
		#sub_6E300AE0
		gadget = "B8CCD88A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderhtmlcanv; "RenderHTMLCanvas"
		#retn


  def test_gadget_sub_6E3019F0(self):
		#sub_6E3019F0
		gadget = "B818E18A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderimage; "RenderImage"
		#retn


  def test_gadget_sub_6E3035B0(self):
		#sub_6E3035B0
		gadget = "33C03941080F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+8], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E304450(self):
		#sub_6E304450
		gadget = "8B542404D9EE8BC133C989480489480889480C895010C7006C8E8A6ED95014D9501856D9581CC7402000480000C700D4E48A6E8948248B703889482889482C89483089483481E61CFFFFFF83CE108970388B4A048B513033C980E21F80FA020F94C103C903C933CE83E10433CE8D140933D183E20833D18950385EC20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], edx
		#mov     dword ptr [eax], offset off_6E8A8E6C
		#fst     dword ptr [eax+14h]
		#fst     dword ptr [eax+18h]
		#push    esi
		#fstp    dword ptr [eax+1Ch]
		#mov     dword ptr [eax+20h], 4800h
		#mov     dword ptr [eax], offset off_6E8AE4D4
		#mov     [eax+24h], ecx
		#mov     esi, [eax+38h]
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#and     esi, 0FFFFFF1Ch
		#or      esi, 10h
		#mov     [eax+38h], esi
		#mov     ecx, [edx+4]
		#mov     edx, [ecx+30h]
		#xor     ecx, ecx
		#and     dl, 1Fh
		#cmp     dl, 2
		#setz    cl
		#add     ecx, ecx
		#add     ecx, ecx
		#xor     ecx, esi
		#and     ecx, 4
		#xor     ecx, esi
		#lea     edx, [ecx+ecx]
		#xor     edx, ecx
		#and     edx, 8
		#xor     edx, ecx
		#mov     [eax+38h], edx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E30A8C0(self):
		#sub_6E30A8C0
		gadget = "83EC148B4424188B10558B680C568B7004578B7808891189710489790889690CC644241C008B54241C8951108B108B70048B78088B680C89511489711889791C896920C644241C008B54241C8951248B70048B78088B108B400C806140FE89512889712C8979305F894134C6442418008B4424185E8941385D83C414C20400"
		self.do(gadget)

		#sub     esp, 14h
		#mov     eax, [esp+14h+arg_0]
		#mov     edx, [eax]
		#push    ebp
		#mov     ebp, [eax+0Ch]
		#push    esi
		#mov     esi, [eax+4]
		#push    edi
		#mov     edi, [eax+8]
		#mov     [ecx], edx
		#mov     [ecx+4], esi
		#mov     [ecx+8], edi
		#mov     [ecx+0Ch], ebp
		#mov     byte ptr [esp+20h+var_4], 0
		#mov     edx, [esp+20h+var_4]
		#mov     [ecx+10h], edx
		#mov     edx, [eax]
		#mov     esi, [eax+4]
		#mov     edi, [eax+8]
		#mov     ebp, [eax+0Ch]
		#mov     [ecx+14h], edx
		#mov     [ecx+18h], esi
		#mov     [ecx+1Ch], edi
		#mov     [ecx+20h], ebp
		#mov     byte ptr [esp+20h+var_4], 0
		#mov     edx, [esp+20h+var_4]
		#mov     [ecx+24h], edx
		#mov     esi, [eax+4]
		#mov     edi, [eax+8]
		#mov     edx, [eax]
		#mov     eax, [eax+0Ch]
		#and     byte ptr [ecx+40h], 0FEh
		#mov     [ecx+28h], edx
		#mov     [ecx+2Ch], esi
		#mov     [ecx+30h], edi
		#pop     edi
		#mov     [ecx+34h], eax
		#mov     byte ptr [esp+1Ch+var_4], 0
		#mov     eax, [esp+1Ch+var_4]
		#pop     esi
		#mov     [ecx+38h], eax
		#pop     ebp
		#add     esp, 14h
		#retn    4


  def test_gadget_sub_6E30A9F0(self):
		#sub_6E30A9F0
		gadget = "8BC18B4C24048B1189108B51048950048B51088950088B510C89500C8B51108950108B51148950148B51188950188B511C89501C8B51208950208B51248950248B51288950288B512C89502C8B51308950308B51348950348B51388950388A494032484080E101304840C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+10h]
		#mov     [eax+10h], edx
		#mov     edx, [ecx+14h]
		#mov     [eax+14h], edx
		#mov     edx, [ecx+18h]
		#mov     [eax+18h], edx
		#mov     edx, [ecx+1Ch]
		#mov     [eax+1Ch], edx
		#mov     edx, [ecx+20h]
		#mov     [eax+20h], edx
		#mov     edx, [ecx+24h]
		#mov     [eax+24h], edx
		#mov     edx, [ecx+28h]
		#mov     [eax+28h], edx
		#mov     edx, [ecx+2Ch]
		#mov     [eax+2Ch], edx
		#mov     edx, [ecx+30h]
		#mov     [eax+30h], edx
		#mov     edx, [ecx+34h]
		#mov     [eax+34h], edx
		#mov     edx, [ecx+38h]
		#mov     [eax+38h], edx
		#mov     cl, [ecx+40h]
		#xor     cl, [eax+40h]
		#and     cl, 1
		#xor     [eax+40h], cl
		#retn    4


  def test_gadget_sub_6E30AA60(self):
		#sub_6E30AA60
		gadget = "8BC18B4C24048B1189108B51048950048B51088950088B510C89500C8B51108950108B51148950148B51188950188B511C89501C8B51208950208B51248950248B51288950288B512C89502C8B51308950308B51348950348B51388950388B503C81E20100008083CA0189503C8A494032484080E101304840C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+10h]
		#mov     [eax+10h], edx
		#mov     edx, [ecx+14h]
		#mov     [eax+14h], edx
		#mov     edx, [ecx+18h]
		#mov     [eax+18h], edx
		#mov     edx, [ecx+1Ch]
		#mov     [eax+1Ch], edx
		#mov     edx, [ecx+20h]
		#mov     [eax+20h], edx
		#mov     edx, [ecx+24h]
		#mov     [eax+24h], edx
		#mov     edx, [ecx+28h]
		#mov     [eax+28h], edx
		#mov     edx, [ecx+2Ch]
		#mov     [eax+2Ch], edx
		#mov     edx, [ecx+30h]
		#mov     [eax+30h], edx
		#mov     edx, [ecx+34h]
		#mov     [eax+34h], edx
		#mov     edx, [ecx+38h]
		#mov     [eax+38h], edx
		#mov     edx, [eax+3Ch]
		#and     edx, 80000001h
		#or      edx, 1
		#mov     [eax+3Ch], edx
		#mov     cl, [ecx+40h]
		#xor     cl, [eax+40h]
		#and     cl, 1
		#xor     [eax+40h], cl
		#retn    4


  def test_gadget_sub_6E30AAE0(self):
		#sub_6E30AAE0
		gadget = "8B4424048B108951048B50048951088B500889510C8B400C8941108B4424088B108951148B50048951188B500889511C8B500C8951208B40108941248B44240C8B108951288B500489512C8B50088951308B500C8951348B40108941388B4424108B1089513C8B50048951408B50088951448B500C8951488B401089414CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+4], edx
		#mov     edx, [eax+4]
		#mov     [ecx+8], edx
		#mov     edx, [eax+8]
		#mov     [ecx+0Ch], edx
		#mov     eax, [eax+0Ch]
		#mov     [ecx+10h], eax
		#mov     eax, [esp+arg_4]
		#mov     edx, [eax]
		#mov     [ecx+14h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+8]
		#mov     [ecx+1Ch], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+20h], edx
		#mov     eax, [eax+10h]
		#mov     [ecx+24h], eax
		#mov     eax, [esp+arg_8]
		#mov     edx, [eax]
		#mov     [ecx+28h], edx
		#mov     edx, [eax+4]
		#mov     [ecx+2Ch], edx
		#mov     edx, [eax+8]
		#mov     [ecx+30h], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+34h], edx
		#mov     eax, [eax+10h]
		#mov     [ecx+38h], eax
		#mov     eax, [esp+arg_C]
		#mov     edx, [eax]
		#mov     [ecx+3Ch], edx
		#mov     edx, [eax+4]
		#mov     [ecx+40h], edx
		#mov     edx, [eax+8]
		#mov     [ecx+44h], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+48h], edx
		#mov     eax, [eax+10h]
		#mov     [ecx+4Ch], eax
		#retn    10h


  def test_gadget_sub_6E30ACA0(self):
		#sub_6E30ACA0
		gadget = "8A4115C0E8022401C3"
		self.do(gadget)

		#mov     al, [ecx+15h]
		#shr     al, 2
		#and     al, 1
		#retn


  def test_gadget_sub_6E30ADD0(self):
		#sub_6E30ADD0
		gadget = "8B517C8B4424048B89800000008910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+7Ch]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+80h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E30ADF0(self):
		#sub_6E30ADF0
		gadget = "8B510C8B49108B442404F7DAF7D98910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+0Ch]
		#mov     ecx, [ecx+10h]
		#mov     eax, [esp+arg_0]
		#neg     edx
		#neg     ecx
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E30AED0(self):
		#sub_6E30AED0
		gadget = "8B4178C3"
		self.do(gadget)

		#mov     eax, [ecx+78h]
		#retn


  def test_gadget_sub_6E30B1B0(self):
		#sub_6E30B1B0
		gadget = "8BC1D9E88B4C2404C700010000008B118950048B4904894808568B74240C578D780CB908000000F3A58B7424148D782CB908000000F3A5DD5050D9EEDD5058DD5060DD5068DD5070DD9080000000DD9088000000DD9090000000DD9098000000DD90A8000000DD90B00000005FDD90B80000005EDD98C0000000DD5078DD90A0000000DD98C8000000C680D000000000C20C00"
		self.do(gadget)

		#mov     eax, ecx
		#fld1
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+8], ecx
		#push    esi
		#mov     esi, [esp+4+arg_4]
		#push    edi
		#lea     edi, [eax+0Ch]
		#mov     ecx, 8
		#rep movsd
		#mov     esi, [esp+8+arg_8]
		#lea     edi, [eax+2Ch]
		#mov     ecx, 8
		#rep movsd
		#fst     qword ptr [eax+50h]
		#fldz
		#fst     qword ptr [eax+58h]
		#fst     qword ptr [eax+60h]
		#fst     qword ptr [eax+68h]
		#fst     qword ptr [eax+70h]
		#fst     qword ptr [eax+80h]
		#fst     qword ptr [eax+88h]
		#fst     qword ptr [eax+90h]
		#fst     qword ptr [eax+98h]
		#fst     qword ptr [eax+0A8h]
		#fst     qword ptr [eax+0B0h]
		#pop     edi
		#fst     qword ptr [eax+0B8h]
		#pop     esi
		#fstp    qword ptr [eax+0C0h]
		#fst     qword ptr [eax+78h]
		#fst     qword ptr [eax+0A0h]
		#fstp    qword ptr [eax+0C8h]
		#mov     byte ptr [eax+0D0h], 0
		#retn    0Ch


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_48(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_48
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E314F60(self):
		#sub_6E314F60
		gadget = "8B8190000000C3"
		self.do(gadget)

		#mov     eax, [ecx+90h]
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_49(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_49
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E325150(self):
		#sub_6E325150
		gadget = "8A442404884166C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+66h], al
		#retn    4


  def test_gadget_sub_6E325160(self):
		#sub_6E325160
		gadget = "8A4166C3"
		self.do(gadget)

		#mov     al, [ecx+66h]
		#retn


  def test_gadget_sub_6E32C2A0(self):
		#sub_6E32C2A0
		gadget = "8B411CC20400"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#retn    4


  def test_gadget_sub_6E32C2F0(self):
		#sub_6E32C2F0
		gadget = "8B41C09983E23F03C2C1F806C3"
		self.do(gadget)

		#mov     eax, [ecx-40h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn


  def test_gadget_sub_6E32C300(self):
		#sub_6E32C300
		gadget = "8B41BC9983E23F03C2C1F806C3"
		self.do(gadget)

		#mov     eax, [ecx-44h]
		#cdq
		#and     edx, 3Fh
		#add     eax, edx
		#sar     eax, 6
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_50(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_50
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E32D470(self):
		#sub_6E32D470
		gadget = "B8B0F08A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderlistbox; "RenderListBox"
		#retn


  def test_gadget_sub_6E32D490(self):
		#sub_6E32D490
		gadget = "8B4120C3"
		self.do(gadget)

		#mov     eax, [ecx+20h]
		#retn


  def test_gadget_sub_6E32F550(self):
		#sub_6E32F550
		gadget = "B80CF58A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderlistitem; "RenderListItem"
		#retn


  def test_gadget_sub_6E32F560(self):
		#sub_6E32F560
		gadget = "B001C3"
		self.do(gadget)

		#mov     al, 1
		#retn


  def test_gadget_sub_6E32F590(self):
		#sub_6E32F590
		gadget = "8B415C33D23B41700F94C0C3"
		self.do(gadget)

		#mov     eax, [ecx+5Ch]
		#xor     edx, edx
		#cmp     eax, [ecx+70h]
		#setz    al
		#retn


  def test_gadget_unknown_libname_10(self):
		#unknown_libname_10
		gadget = "568BF1E848CC00008BCE5EE910FFFFFF5153568BF18BC6E844F0FFFF8BD885DB0F84C00000008B430CC1E80257C644240F00A80174378B432C8B0DC05DA66E3BC174108B500C3B510C75228B40103B4110751A804B3C048A433CD0E824018844240F74098BC6E8E5F1FFFFEB078BC6E8ACF0FFFF8BF885FF746B8D9B000000008A4778A802745EA801753F8B777024FD88477885F674338A4618834E18012401751D6A006A018BCEE853D100008B4E18C1E90EF6C10174078BCEE8C1AF00006A016A018BCEE8F6F50000807C240F008BC77407E878F1FFFFEB05E841F0FFFF8BF885FF759B5F5E5B59C3"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E33D310
		#mov     ecx, esi
		#pop     esi
		#jmp     loc_6E3305E0
		#push    ecx
		#push    ebx
		#push    esi
		#mov     esi, ecx
		#mov     eax, esi
		#call    sub_6E32F630
		#mov     ebx, eax
		#test    ebx, ebx
		#jz      loc_6E3306B6
		#mov     eax, [ebx+0Ch]
		#shr     eax, 2
		#push    edi
		#mov     [esp+10h+var_1], 0
		#test    al, 1
		#jz      short loc_6E33063D
		#mov     eax, [ebx+2Ch]
		#mov     ecx, dword_6EA65DC0
		#cmp     eax, ecx
		#jz      short loc_6E330623
		#mov     edx, [eax+0Ch]
		#cmp     edx, [ecx+0Ch]
		#jnz     short loc_6E33063D
		#mov     eax, [eax+10h]
		#cmp     eax, [ecx+10h]
		#jnz     short loc_6E33063D
		#or      byte ptr [ebx+3Ch], 4
		#mov     al, [ebx+3Ch]
		#shr     al, 1
		#and     al, 1
		#mov     [esp+10h+var_1], al
		#jz      short loc_6E33063D
		#mov     eax, esi
		#call    sub_6E32F820
		#jmp     short loc_6E330644
		#mov     eax, esi
		#call    sub_6E32F6F0
		#mov     edi, eax
		#test    edi, edi
		#jz      short loc_6E3306B5
		#lea     ebx, [ebx+0]
		#mov     al, [edi+78h]
		#test    al, 2
		#jz      short loc_6E3306B5
		#test    al, 1
		#jnz     short loc_6E33069A
		#mov     esi, [edi+70h]
		#and     al, 0FDh
		#mov     [edi+78h], al
		#test    esi, esi
		#jz      short loc_6E33069A
		#mov     al, [esi+18h]
		#or      dword ptr [esi+18h], 1
		#and     al, 1
		#jnz     short loc_6E33068F
		#push    0
		#push    1
		#mov     ecx, esi
		#call    sub_6E33D7D0
		#mov     ecx, [esi+18h]
		#shr     ecx, 0Eh
		#test    cl, 1
		#jz      short loc_6E33068F
		#mov     ecx, esi
		#call    sub_6E33B650
		#push    1
		#push    1
		#mov     ecx, esi
		#call    sub_6E33FC90
		#cmp     [esp+10h+var_1], 0
		#mov     eax, edi
		#jz      short loc_6E3306AA
		#call    sub_6E32F820
		#jmp     short loc_6E3306AF
		#call    sub_6E32F6F0
		#mov     edi, eax
		#test    edi, edi
		#jnz     short loc_6E330650
		#pop     edi
		#pop     esi
		#pop     ebx
		#pop     ecx
		#retn


  def test_gadget_unknown_libname_11(self):
		#unknown_libname_11
		gadget = "568BF1E8A81501008BCE5EE900FFFFFF"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E341C80
		#mov     ecx, esi
		#pop     esi
		#jmp     loc_6E3305E0


  def test_gadget_sub_6E331DC0(self):
		#sub_6E331DC0
		gadget = "B890F98A6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderlistmark; "RenderListMarker"
		#retn


  def test_gadget_unknown_libname_12(self):
		#unknown_libname_12
		gadget = "568BF1E8A8FAFFFF8BCE5EE970D6FFFF"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E333AF0
		#mov     ecx, esi
		#pop     esi
		#jmp     sub_6E3316C0


  def test_gadget_sub_6E3350C0(self):
		#sub_6E3350C0
		gadget = "33C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget_sub_6E335120(self):
		#sub_6E335120
		gadget = "C6412000C3"
		self.do(gadget)

		#mov     byte ptr [ecx+20h], 0
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_51(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_51
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_52(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_52
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_53(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_53
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E3370C0(self):
		#sub_6E3370C0
		gadget = "B854068B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermenulist; "RenderMenuList"
		#retn


  def test_gadget_sub_6E3376B0(self):
		#sub_6E3376B0
		gadget = "B8AC0A8B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermeter; "RenderMeter"
		#retn


  def test_gadget_sub_6E337D50(self):
		#sub_6E337D50
		gadget = "B8E00F8B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermultic_5; "RenderMultiColumnFlowThread"
		#retn


  def test_gadget_sub_6E337D60(self):
		#sub_6E337D60
		gadget = "8B44240C8B4C24048B5424088908895004C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#retn    0Ch


  def test_gadget_sub_6E337D80(self):
		#sub_6E337D80
		gadget = "8B410C8B48748B4424048908C20400"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+74h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E337E90(self):
		#sub_6E337E90
		gadget = "8B410C8B48788B54240C890AC20C00"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#mov     ecx, [eax+78h]
		#mov     edx, [esp+arg_8]
		#mov     [edx], ecx
		#retn    0Ch


  def test_gadget_sub_6E337EA0(self):
		#sub_6E337EA0
		gadget = "B85C148B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermultic_6; "RenderMultiColumnSet"
		#retn


  def test_gadget_sub_6E339410(self):
		#sub_6E339410
		gadget = "8B89B80000008B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+0B8h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E339420(self):
		#sub_6E339420
		gadget = "8B89BC0000008B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+0BCh]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E3394F0(self):
		#sub_6E3394F0
		gadget = "B8E8188B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendernamedflo; "RenderNamedFlowThread"
		#retn


  def test_gadget_sub_6E339580(self):
		#sub_6E339580
		gadget = "8B819C01000033C93948100F94C0C3"
		self.do(gadget)

		#mov     eax, [ecx+19Ch]
		#xor     ecx, ecx
		#cmp     [eax+10h], ecx
		#setz    al
		#retn


  def test_gadget_sub_6E33B4C0(self):
		#sub_6E33B4C0
		gadget = "8B4424088B4C24048901C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [esp+arg_0]
		#mov     [ecx], eax
		#retn


  def test_gadget_sub_6E33B650(self):
		#sub_6E33B650
		gadget = "8B411C8B481883E1FD83C901894818C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#mov     ecx, [eax+18h]
		#and     ecx, 0FFFFFFFDh
		#or      ecx, 1
		#mov     [eax+18h], ecx
		#retn


  def test_gadget_sub_6E33B730(self):
		#sub_6E33B730
		gadget = "8B44240448C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#dec     eax
		#retn    4


  def test_gadget_sub_6E33B740(self):
		#sub_6E33B740
		gadget = "8B44240440C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#inc     eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_55(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_55
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E33C6A0(self):
		#sub_6E33C6A0
		gadget = "8B41088B48148B51088B82500100008B80C4010000C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     ecx, [eax+14h]
		#mov     edx, [ecx+8]
		#mov     eax, [edx+150h]
		#mov     eax, [eax+1C4h]
		#retn


  def test_gadget_sub_6E342740(self):
		#sub_6E342740
		gadget = "8BC18B4C240433D25633F63BCE0F94C2C700741D8B6E89700489480889700C8970108970148B481883E20183CA28C1E20781E1001400800BD18950185EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#xor     edx, edx
		#push    esi
		#xor     esi, esi
		#cmp     ecx, esi
		#setz    dl
		#mov     dword ptr [eax], offset off_6E8B1D74
		#mov     [eax+4], esi
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], esi
		#mov     [eax+10h], esi
		#mov     [eax+14h], esi
		#mov     ecx, [eax+18h]
		#and     edx, 1
		#or      edx, 28h
		#shl     edx, 7
		#and     ecx, 80001400h
		#or      edx, ecx
		#mov     [eax+18h], edx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E3445D0(self):
		#sub_6E3445D0
		gadget = "B85C288B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderprogress; "RenderProgress"
		#retn


  def test_gadget_sub_6E344BC0(self):
		#sub_6E344BC0
		gadget = "B884338B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderquote; "RenderQuote"
		#retn


  def test_gadget_unknown_libname_13(self):
		#unknown_libname_13
		gadget = "568BF1E828FEFFFF8BCE5EE920120200"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E344CE0
		#mov     ecx, esi
		#pop     esi
		#jmp     sub_6E3660E0


  def test_gadget_unknown_libname_14(self):
		#unknown_libname_14
		gadget = "568BF1E8B8CDFFFF8BCE5EE910FEFFFF"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E341C80
		#mov     ecx, esi
		#pop     esi
		#jmp     sub_6E344CE0


  def test_gadget_unknown_libname_15(self):
		#unknown_libname_15
		gadget = "568BF1E8287CFFFF8BCE5EE970FFFFFF568BF18B46088B48148B510883BA000500000074658B068B906404000080A6AC000000FE8BCEFFD28B4E6C85C9744B8B018B904004000056FFD28BCEE80FFFFFFFF686AC0000000174308B068B90600400008BCEFFD202C002C03286AC00000024043086AC000000F686AC0000000474098B4E6C5EE93607FBFF5EC3"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E33D310
		#mov     ecx, esi
		#pop     esi
		#jmp     loc_6E345660
		#push    esi
		#mov     esi, ecx
		#mov     eax, [esi+8]
		#mov     ecx, [eax+14h]
		#mov     edx, [ecx+8]
		#cmp     dword ptr [edx+500h], 0
		#jz      short loc_6E3456DA
		#mov     eax, [esi]
		#mov     edx, [eax+464h]
		#and     byte ptr [esi+0ACh], 0FEh
		#mov     ecx, esi
		#call    edx
		#mov     ecx, [esi+6Ch]
		#test    ecx, ecx
		#jz      short loc_6E3456DA
		#mov     eax, [ecx]
		#mov     edx, [eax+440h]
		#push    esi
		#call    edx
		#mov     ecx, esi
		#call    sub_6E3455B0
		#test    byte ptr [esi+0ACh], 1
		#jz      short loc_6E3456DA
		#mov     eax, [esi]
		#mov     edx, [eax+460h]
		#mov     ecx, esi
		#call    edx
		#add     al, al
		#add     al, al
		#xor     al, [esi+0ACh]
		#and     al, 4
		#xor     [esi+0ACh], al
		#test    byte ptr [esi+0ACh], 4
		#jz      short loc_6E3456DA
		#mov     ecx, [esi+6Ch]
		#pop     esi
		#jmp     loc_6E2F5E10
		#pop     esi
		#retn


  def test_gadget_sub_6E346960(self):
		#sub_6E346960
		gadget = "B804388B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderregion; "RenderRegion"
		#retn


  def test_gadget_sub_6E347640(self):
		#sub_6E347640
		gadget = "B884408B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderreplaced; "RenderReplaced"
		#retn


  def test_gadget_sub_6E3498D0(self):
		#sub_6E3498D0
		gadget = "B890448B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderreplica; "RenderReplica"
		#retn


  def test_gadget_sub_6E349B70(self):
		#sub_6E349B70
		gadget = "B8D0478B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderrubyInli; "RenderRuby (inline)"
		#retn


  def test_gadget_sub_6E349C60(self):
		#sub_6E349C60
		gadget = "B82C4C8B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderrubyBloc; "RenderRuby (block)"
		#retn


  def test_gadget_sub_6E34A340(self):
		#sub_6E34A340
		gadget = "B88C508B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderrubybase; "RenderRubyBase (anonymous)"
		#retn


  def test_gadget_sub_6E34A350(self):
		#sub_6E34A350
		gadget = "B803000000C20400"
		self.do(gadget)

		#mov     eax, 3
		#retn    4


  def test_gadget_sub_6E34A600(self):
		#sub_6E34A600
		gadget = "B8F4548B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderrubyrunA; "RenderRubyRun (anonymous)"
		#retn


  def test_gadget_sub_6E34B280(self):
		#sub_6E34B280
		gadget = "B85C598B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderrubytext; "RenderRubyText"
		#retn


  def test_gadget_sub_6E34C930(self):
		#sub_6E34C930
		gadget = "B8C45E8B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderscrollba; "RenderScrollbarPart"
		#retn


  def test_gadget_sub_6E34C940(self):
		#sub_6E34C940
		gadget = "8B49308B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+30h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E34C950(self):
		#sub_6E34C950
		gadget = "8B49348B4424048908C20400"
		self.do(gadget)

		#mov     ecx, [ecx+34h]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_36(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_36
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E34DA50(self):
		#sub_6E34DA50
		gadget = "C6410400C3"
		self.do(gadget)

		#mov     byte ptr [ecx+4], 0
		#retn


  def test_gadget_sub_6E34DA80(self):
		#sub_6E34DA80
		gadget = "33C0394424040F94C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [esp+arg_0], eax
		#setz    al
		#retn    4


  def test_gadget_sub_6E34E170(self):
		#sub_6E34E170
		gadget = "B870648B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendertextcont; "RenderTextControl"
		#retn


  def test_gadget_sub_6E34EC50(self):
		#sub_6E34EC50
		gadget = "B8D4688B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderslider; "RenderSlider"
		#retn


  def test_gadget_sub_6E34EF30(self):
		#sub_6E34EF30
		gadget = "B8106D8B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersnapshot; "RenderSnapshottedPlugIn"
		#retn


  def test_gadget_GetNumNestedThreadSubscriptionsSchedulerProxydetailsConcurrencyQAEIXZ(self):
		#GetNumNestedThreadSubscriptionsSchedulerProxydetailsConcurrencyQAEIXZ
		gadget = "8B81C4000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0C4h]
		#retn


  def test_gadget_IdSchedulerBasedetailsConcurrencyUBEIXZ(self):
		#IdSchedulerBasedetailsConcurrencyUBEIXZ
		gadget = "8B81C8000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0C8h]
		#retn


  def test_gadget_sub_6E350AB0(self):
		#sub_6E350AB0
		gadget = "B874718B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendertable; "RenderTable"
		#retn


  def test_gadget_sub_6E3513A0(self):
		#sub_6E3513A0
		gadget = "80A1BC000000EFC7819800000000000000C20400"
		self.do(gadget)

		#and     byte ptr [ecx+0BCh], 0EFh
		#mov     dword ptr [ecx+98h], 0
		#retn    4


  def test_gadget_sub_6E355270(self):
		#sub_6E355270
		gadget = "8BC133C9890889480489482489482889484889484C89486C894870898890000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], ecx
		#mov     [eax+90h], ecx
		#retn


  def test_gadget_sub_6E358D60(self):
		#sub_6E358D60
		gadget = "8B41048B483083E11F33C080F90C0F94C0C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     ecx, [eax+30h]
		#and     ecx, 1Fh
		#xor     eax, eax
		#cmp     cl, 0Ch
		#setz    al
		#retn


  def test_gadget_sub_6E359020(self):
		#sub_6E359020
		gadget = "B8387E8B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendertablecol; "RenderTableCol"
		#retn


  def test_gadget_sub_6E359C80(self):
		#sub_6E359C80
		gadget = "8B4424048B480C8B4424088B51588B480C8B415825FFFFFF7F81E2FFFFFF7F3BD01BC0F7D8C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+0Ch]
		#mov     eax, [esp+arg_4]
		#mov     edx, [ecx+58h]
		#mov     ecx, [eax+0Ch]
		#mov     eax, [ecx+58h]
		#and     eax, 7FFFFFFFh
		#and     edx, 7FFFFFFFh
		#cmp     edx, eax
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_6E3601F0(self):
		#sub_6E3601F0
		gadget = "B8A0868B6EC3"
		self.do(gadget)

		#mov     eax, offset aRendertext; "RenderText"
		#retn


  def test_gadget_sub_6E360320(self):
		#sub_6E360320
		gadget = "B8FFFF000066894132C3"
		self.do(gadget)

		#mov     eax, 0FFFFh
		#mov     [ecx+32h], ax
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_57(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_57
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E367C20(self):
		#sub_6E367C20
		gadget = "8B4C2408034C240C8B4424048908C20C00"
		self.do(gadget)

		#mov     ecx, [esp+arg_4]
		#add     ecx, [esp+arg_8]
		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#retn    0Ch


  def test_gadget_sub_6E36A050(self):
		#sub_6E36A050
		gadget = "8B442404C700FFFFFFFFC6400401C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0FFFFFFFFh
		#mov     byte ptr [eax+4], 1
		#retn    4


  def test_gadget_sub_6E36A0A0(self):
		#sub_6E36A0A0
		gadget = "8B442404C700000000FFC6400401C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 0FF000000h
		#mov     byte ptr [eax+4], 1
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_58(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_58
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E36A160(self):
		#sub_6E36A160
		gadget = "8B4C240C8B51088B4424048B490C8910894804C20C00"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     edx, [ecx+8]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    0Ch


  def test_gadget_sub_6E36A180(self):
		#sub_6E36A180
		gadget = "D9EEC20400"
		self.do(gadget)

		#fldz
		#retn    4


  def test_gadget_sub_6E36A5D0(self):
		#sub_6E36A5D0
		gadget = "8BC1C740040100000033C9C700345D8A6E89480888480C89481088481489481888481C89482088482489482888482C89483088483489483888483C894840884844C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], 1
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8A5D34
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cl
		#mov     [eax+10h], ecx
		#mov     [eax+14h], cl
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cl
		#mov     [eax+20h], ecx
		#mov     [eax+24h], cl
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], cl
		#mov     [eax+30h], ecx
		#mov     [eax+34h], cl
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], cl
		#mov     [eax+40h], ecx
		#mov     [eax+44h], cl
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_37(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_37
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_38(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_38
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_44(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_44
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_60(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_60
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_39(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_39
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_61(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_61
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_40(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_40
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_41(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_41
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_62(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_62
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E36F8C0(self):
		#sub_6E36F8C0
		gadget = "8B4424048B4018C1E80983E001C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+18h]
		#shr     eax, 9
		#and     eax, 1
		#retn    8


  def test_gadget_sub_6E36FC10(self):
		#sub_6E36FC10
		gadget = "8B41088B48148B51088A82A0020000C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     ecx, [eax+14h]
		#mov     edx, [ecx+8]
		#mov     al, [edx+2A0h]
		#retn


  def test_gadget_sub_6E370540(self):
		#sub_6E370540
		gadget = "B8FCA38B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderview; "RenderView"
		#retn


  def test_gadget_sub_6E374B50(self):
		#sub_6E374B50
		gadget = "B838A88B6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderwordbrea; "RenderWordBreak"
		#retn


  def test_gadget_sub_6E374E00(self):
		#sub_6E374E00
		gadget = "8B411083C060C3"
		self.do(gadget)

		#mov     eax, [ecx+10h]
		#add     eax, 60h
		#retn


  def test_gadget_sub_6E3755D0(self):
		#sub_6E3755D0
		gadget = "8B4128C3"
		self.do(gadget)

		#mov     eax, [ecx+28h]
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_45(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_45
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E37C230(self):
		#sub_6E37C230
		gadget = "33C03B0D9869A66E0F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     ecx, dword_6EA66998
		#setnz   al
		#retn


  def test_gadget_sub_6E37C240(self):
		#sub_6E37C240
		gadget = "F7413400E007000F95C0C3"
		self.do(gadget)

		#test    dword ptr [ecx+34h], 7E000h
		#setnz   al
		#retn


  def test_gadget_sub_6E37C250(self):
		#sub_6E37C250
		gadget = "8B41348B4C240449BA01000000D3E2C1E80C23D0F6C27F0F95C0C20400"
		self.do(gadget)

		#mov     eax, [ecx+34h]
		#mov     ecx, [esp+arg_0]
		#dec     ecx
		#mov     edx, 1
		#shl     edx, cl
		#shr     eax, 0Ch
		#and     edx, eax
		#test    dl, 7Fh
		#setnz   al
		#retn    4


  def test_gadget_sub_6E37C270(self):
		#sub_6E37C270
		gadget = "568BD18B4C24088B423449BE01000000D3E6C1E60C0BF033F081E600F0070033F08972345EC20400"
		self.do(gadget)

		#push    esi
		#mov     edx, ecx
		#mov     ecx, [esp+4+arg_0]
		#mov     eax, [edx+34h]
		#dec     ecx
		#mov     esi, 1
		#shl     esi, cl
		#shl     esi, 0Ch
		#or      esi, eax
		#xor     esi, eax
		#and     esi, 7F000h
		#xor     esi, eax
		#mov     [edx+34h], esi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E37DA70(self):
		#sub_6E37DA70
		gadget = "8B41188B4004C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     eax, [eax+4]
		#retn


  def test_gadget_sub_6E37DA80(self):
		#sub_6E37DA80
		gadget = "8B491C8B51448B4424048B49488910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+1Ch]
		#mov     edx, [ecx+44h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+48h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E37DAC0(self):
		#sub_6E37DAC0
		gadget = "8B411C668B4004C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#mov     ax, [eax+4]
		#retn


  def test_gadget_sub_6E37DAD0(self):
		#sub_6E37DAD0
		gadget = "8B411C668B4006C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#mov     ax, [eax+6]
		#retn


  def test_gadget_sub_6E37DAE0(self):
		#sub_6E37DAE0
		gadget = "8B41148B4050C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+50h]
		#retn


  def test_gadget_sub_6E37DAF0(self):
		#sub_6E37DAF0
		gadget = "8B411C83C010C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#add     eax, 10h
		#retn


  def test_gadget_sub_6E37DB30(self):
		#sub_6E37DB30
		gadget = "8B411CD94028C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#fld     dword ptr [eax+28h]
		#retn


  def test_gadget_sub_6E37DB60(self):
		#sub_6E37DB60
		gadget = "8B411C0FBF403AC3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#movsx   eax, word ptr [eax+3Ah]
		#retn


  def test_gadget_sub_6E37DB70(self):
		#sub_6E37DB70
		gadget = "8B411C0FBF4038C3"
		self.do(gadget)

		#mov     eax, [ecx+1Ch]
		#movsx   eax, word ptr [eax+38h]
		#retn


  def test_gadget_sub_6E3850A0(self):
		#sub_6E3850A0
		gadget = "D94114C3"
		self.do(gadget)

		#fld     dword ptr [ecx+14h]
		#retn


  def test_gadget_sub_6E385310(self):
		#sub_6E385310
		gadget = "D9EE8BC183601080D95804B901000000890889480889480CC3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#and     dword ptr [eax+10h], 0FFFFFF80h
		#fstp    dword ptr [eax+4]
		#mov     ecx, 1
		#mov     [eax], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn


  def test_gadget_sub_6E385330(self):
		#sub_6E385330
		gadget = "8BC1C70001000000568B742408D94604D958048B4E088948088B560C8B481089500C334E1083E1073148108B50108B4E1033CA83E11833CA8948108B561033D183E22033D18950108B4E1033CA83E14033CA8948105EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#push    esi
		#mov     esi, [esp+4+arg_0]
		#fld     dword ptr [esi+4]
		#fstp    dword ptr [eax+4]
		#mov     ecx, [esi+8]
		#mov     [eax+8], ecx
		#mov     edx, [esi+0Ch]
		#mov     ecx, [eax+10h]
		#mov     [eax+0Ch], edx
		#xor     ecx, [esi+10h]
		#and     ecx, 7
		#xor     [eax+10h], ecx
		#mov     edx, [eax+10h]
		#mov     ecx, [esi+10h]
		#xor     ecx, edx
		#and     ecx, 18h
		#xor     ecx, edx
		#mov     [eax+10h], ecx
		#mov     edx, [esi+10h]
		#xor     edx, ecx
		#and     edx, 20h
		#xor     edx, ecx
		#mov     [eax+10h], edx
		#mov     ecx, [esi+10h]
		#xor     ecx, edx
		#and     ecx, 40h
		#xor     ecx, edx
		#mov     [eax+10h], ecx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E385820(self):
		#sub_6E385820
		gadget = "33C03841180F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+18h], al
		#setz    al
		#retn


  def test_gadget_sub_6E385830(self):
		#sub_6E385830
		gadget = "8B4424088B108951108B4004894114C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     edx, [eax]
		#mov     [ecx+10h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+14h], eax
		#retn    0Ch


  def test_gadget_sub_6E385900(self):
		#sub_6E385900
		gadget = "518B44240833C989088948046689480888480A890C2489480C6689481088481259C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], cx
		#mov     [eax+0Ah], cl
		#mov     [esp+4+var_4], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], cx
		#mov     [eax+12h], cl
		#pop     ecx
		#retn


  def test_gadget_sub_6E385A80(self):
		#sub_6E385A80
		gadget = "8BC133C9C7000100000089480489480889480C89481089481489481889481C894820C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn


  def test_gadget_sub_6E385AB0(self):
		#sub_6E385AB0
		gadget = "8BC18B4C2404C700010000008B51048950048B51088950088B510C89500C8B51108950108B51148950148B51188950188B511C89501C8B4920894820C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#mov     edx, [ecx+4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+10h]
		#mov     [eax+10h], edx
		#mov     edx, [ecx+14h]
		#mov     [eax+14h], edx
		#mov     edx, [ecx+18h]
		#mov     [eax+18h], edx
		#mov     edx, [ecx+1Ch]
		#mov     [eax+1Ch], edx
		#mov     ecx, [ecx+20h]
		#mov     [eax+20h], ecx
		#retn    4


  def test_gadget_sub_6E385EF0(self):
		#sub_6E385EF0
		gadget = "D9EE8BC1D95004B90100000066894808D9580CC7000100000033C9894810C740140600000089481888481C8B50248048200781E200F9FFFF81CA00010000895024C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fst     dword ptr [eax+4]
		#mov     ecx, 1
		#mov     [eax+8], cx
		#fstp    dword ptr [eax+0Ch]
		#mov     dword ptr [eax], 1
		#xor     ecx, ecx
		#mov     [eax+10h], ecx
		#mov     dword ptr [eax+14h], 6
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], cl
		#mov     edx, [eax+24h]
		#or      byte ptr [eax+20h], 7
		#and     edx, 0FFFFF900h
		#or      edx, 100h
		#mov     [eax+24h], edx
		#retn


  def test_gadget_sub_6E385F40(self):
		#sub_6E385F40
		gadget = "8BC1C70001000000568B742408D94604D95804668B4E0866894808D9460CD9580C8B56108950108B4E148948148B56188950188B4E1C0FB6502089481C32562080E2013050208A4E208A502032CA80E10232CA8848200FB6562032D180E20432D18B4824885020334E2483E1013148248B50248B4E2433CA83E10633CA8948248B562433D183E21833D18950248B4E2433CA83E16033CA8948248B562433D181E28001000033D18950248B4E2433CA81E10006000033CA8948245EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#push    esi
		#mov     esi, [esp+4+arg_0]
		#fld     dword ptr [esi+4]
		#fstp    dword ptr [eax+4]
		#mov     cx, [esi+8]
		#mov     [eax+8], cx
		#fld     dword ptr [esi+0Ch]
		#fstp    dword ptr [eax+0Ch]
		#mov     edx, [esi+10h]
		#mov     [eax+10h], edx
		#mov     ecx, [esi+14h]
		#mov     [eax+14h], ecx
		#mov     edx, [esi+18h]
		#mov     [eax+18h], edx
		#mov     ecx, [esi+1Ch]
		#movzx   edx, byte ptr [eax+20h]
		#mov     [eax+1Ch], ecx
		#xor     dl, [esi+20h]
		#and     dl, 1
		#xor     [eax+20h], dl
		#mov     cl, [esi+20h]
		#mov     dl, [eax+20h]
		#xor     cl, dl
		#and     cl, 2
		#xor     cl, dl
		#mov     [eax+20h], cl
		#movzx   edx, byte ptr [esi+20h]
		#xor     dl, cl
		#and     dl, 4
		#xor     dl, cl
		#mov     ecx, [eax+24h]
		#mov     [eax+20h], dl
		#xor     ecx, [esi+24h]
		#and     ecx, 1
		#xor     [eax+24h], ecx
		#mov     edx, [eax+24h]
		#mov     ecx, [esi+24h]
		#xor     ecx, edx
		#and     ecx, 6
		#xor     ecx, edx
		#mov     [eax+24h], ecx
		#mov     edx, [esi+24h]
		#xor     edx, ecx
		#and     edx, 18h
		#xor     edx, ecx
		#mov     [eax+24h], edx
		#mov     ecx, [esi+24h]
		#xor     ecx, edx
		#and     ecx, 60h
		#xor     ecx, edx
		#mov     [eax+24h], ecx
		#mov     edx, [esi+24h]
		#xor     edx, ecx
		#and     edx, 180h
		#xor     edx, ecx
		#mov     [eax+24h], edx
		#mov     ecx, [esi+24h]
		#xor     ecx, edx
		#and     ecx, 600h
		#xor     ecx, edx
		#mov     [eax+24h], ecx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E3882C0(self):
		#sub_6E3882C0
		gadget = "D9E88BC133C9C700010000008948046689480888480A89480C668948108848128948146689481888481A89481C66894820884822D9582C806024FE836028F0C3"
		self.do(gadget)

		#fld1
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], cx
		#mov     [eax+0Ah], cl
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], cx
		#mov     [eax+12h], cl
		#mov     [eax+14h], ecx
		#mov     [eax+18h], cx
		#mov     [eax+1Ah], cl
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], cx
		#mov     [eax+22h], cl
		#fstp    dword ptr [eax+2Ch]
		#and     byte ptr [eax+24h], 0FEh
		#and     dword ptr [eax+28h], 0FFFFFFF0h
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_63(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_63
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E38EF30(self):
		#sub_6E38EF30
		gadget = "8A8100010000C3"
		self.do(gadget)

		#mov     al, [ecx+100h]
		#retn


  def test_gadget_sub_6E396810(self):
		#sub_6E396810
		gadget = "8A442404A23E9AA46EC20800"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     byte_6EA49A3E, al
		#retn    8


  def test_gadget_sub_6E396820(self):
		#sub_6E396820
		gadget = "8A442404A21664A66EC20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     byte_6EA66416, al
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_44(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_44
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E397770(self):
		#sub_6E397770
		gadget = "8BC18B4C2404C7400401000000C70000B78B6E894808C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     dword ptr [eax], offset off_6E8BB700
		#mov     [eax+8], ecx
		#retn    4


  def test_gadget_sub_6E3978B0(self):
		#sub_6E3978B0
		gadget = "8D8184010000C3"
		self.do(gadget)

		#lea     eax, [ecx+184h]
		#retn


  def test_gadget_sub_6E397AC0(self):
		#sub_6E397AC0
		gadget = "33C03941740F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+74h], eax
		#setz    al
		#retn


  def test_gadget_sub_6E398E60(self):
		#sub_6E398E60
		gadget = "FF4118C3"
		self.do(gadget)

		#inc     dword ptr [ecx+18h]
		#retn


  def test_gadget_sub_6E39E8A0(self):
		#sub_6E39E8A0
		gadget = "8B4104FF4018C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#inc     dword ptr [eax+18h]
		#retn


  def test_gadget_sub_6E39EAF0(self):
		#sub_6E39EAF0
		gadget = "8BC18B4C2404890833C989480483CAFF89500889500C894810894814894818C6401C01894820894824C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#or      edx, 0FFFFFFFFh
		#mov     [eax+8], edx
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     byte ptr [eax+1Ch], 1
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#retn    4


  def test_gadget_sub_6E39FD70(self):
		#sub_6E39FD70
		gadget = "FF4114C3"
		self.do(gadget)

		#inc     dword ptr [ecx+14h]
		#retn


  def test_gadget_sub_6E3A00E0(self):
		#sub_6E3A00E0
		gadget = "8B410433D23B48540F95C0C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#xor     edx, edx
		#cmp     ecx, [eax+54h]
		#setnz   al
		#retn


  def test_gadget_sub_6E3A11A0(self):
		#sub_6E3A11A0
		gadget = "8B5424048BC133C98908895004C640080189480C89481089481489481889481C894820C20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     byte ptr [eax+8], 1
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn    4


  def test_gadget_sub_6E3A23D0(self):
		#sub_6E3A23D0
		gadget = "8B4424040981F8000000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#or      [ecx+0F8h], eax
		#retn    4


  def test_gadget_sub_6E3A4670(self):
		#sub_6E3A4670
		gadget = "8BC133C9C700D8BF8B6E89480489480889480C66894810884812C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8BBFD8
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], cx
		#mov     [eax+12h], cl
		#retn


  def test_gadget_sub_6E3A4C00(self):
		#sub_6E3A4C00
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget_sub_6E3A89F0(self):
		#sub_6E3A89F0
		gadget = "518B442408D9EE33C9DD5808C70001000000C6400401890C2489481059C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#fldz
		#xor     ecx, ecx
		#fstp    qword ptr [eax+8]
		#mov     dword ptr [eax], 1
		#mov     byte ptr [eax+4], 1
		#mov     [esp+4+var_4], ecx
		#mov     [eax+10h], ecx
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E3A8C90(self):
		#sub_6E3A8C90
		gadget = "518B442408D9EE33C9DD5808C70001000000884804890C2489481059C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#fldz
		#xor     ecx, ecx
		#fstp    qword ptr [eax+8]
		#mov     dword ptr [eax], 1
		#mov     [eax+4], cl
		#mov     [esp+4+var_4], ecx
		#mov     [eax+10h], ecx
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E3AA080(self):
		#sub_6E3AA080
		gadget = "C701FCE4846EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E84E4FC
		#retn


  def test_gadget_sub_6E3AA2F0(self):
		#sub_6E3AA2F0
		gadget = "518B44241433D20141088B4424088B4C240C89088950048914248B54241089500C59C21000"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_C]
		#xor     edx, edx
		#add     [ecx+8], eax
		#mov     eax, [esp+4+arg_0]
		#mov     ecx, [esp+4+arg_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     [esp+4+var_4], edx
		#mov     edx, [esp+4+arg_8]
		#mov     [eax+0Ch], edx
		#pop     ecx
		#retn    10h


  def test_gadget_sub_6E3AA320(self):
		#sub_6E3AA320
		gadget = "518B44241433D20141088B4424088B4C240C89088950048914248B54241089501059C21000"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_C]
		#xor     edx, edx
		#add     [ecx+8], eax
		#mov     eax, [esp+4+arg_0]
		#mov     ecx, [esp+4+arg_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     [esp+4+var_4], edx
		#mov     edx, [esp+4+arg_8]
		#mov     [eax+10h], edx
		#pop     ecx
		#retn    10h


  def test_gadget_sub_6E3AA350(self):
		#sub_6E3AA350
		gadget = "518B44241033D20141088B4424088B4C240C890889142489500459C20C00"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_8]
		#xor     edx, edx
		#add     [ecx+8], eax
		#mov     eax, [esp+4+arg_0]
		#mov     ecx, [esp+4+arg_4]
		#mov     [eax], ecx
		#mov     [esp+4+var_4], edx
		#mov     [eax+4], edx
		#pop     ecx
		#retn    0Ch


  def test_gadget_unknown_libname_16(self):
		#unknown_libname_16
		gadget = "8BC18B4C24048908C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#retn    4


  def test_gadget_sub_6E3AEBF0(self):
		#sub_6E3AEBF0
		gadget = "668B4134C3"
		self.do(gadget)

		#mov     ax, [ecx+34h]
		#retn


  def test_gadget_sub_6E3AF7B0(self):
		#sub_6E3AF7B0
		gadget = "8B4424088B4C24048B5108568B70088971088950088B308B11893189108B70048B51048971048950045EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx+8]
		#push    esi
		#mov     esi, [eax+8]
		#mov     [ecx+8], esi
		#mov     [eax+8], edx
		#mov     esi, [eax]
		#mov     edx, [ecx]
		#mov     [ecx], esi
		#mov     [eax], edx
		#mov     esi, [eax+4]
		#mov     edx, [ecx+4]
		#mov     [ecx+4], esi
		#mov     [eax+4], edx
		#pop     esi
		#retn


  def test_gadget_sub_6E3B1070(self):
		#sub_6E3B1070
		gadget = "B802000000C3"
		self.do(gadget)

		#mov     eax, 2
		#retn


  def test_gadget_sub_6E3B11B0(self):
		#sub_6E3B11B0
		gadget = "33C03981C40000000F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+0C4h], eax
		#setnz   al
		#retn


  def test_gadget_unknown_libname_17(self):
		#unknown_libname_17
		gadget = "568BF1E848FDFFFF8BCE5EE9E020BBFF"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E3B1580
		#mov     ecx, esi
		#pop     esi
		#jmp     sub_6DF63920


  def test_gadget_sub_6E3B2520(self):
		#sub_6E3B2520
		gadget = "8B442404D94424088B108991D40100008B4004D999DC0100008189C4010000000000018981D8010000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#fld     [esp+arg_4]
		#mov     edx, [eax]
		#mov     [ecx+1D4h], edx
		#mov     eax, [eax+4]
		#fstp    dword ptr [ecx+1DCh]
		#or      dword ptr [ecx+1C4h], 1000000h
		#mov     [ecx+1D8h], eax
		#retn    8


  def test_gadget_sub_6E3B3850(self):
		#sub_6E3B3850
		gadget = "8B81E0010000C3"
		self.do(gadget)

		#mov     eax, [ecx+1E0h]
		#retn


  def test_gadget_sub_6E3B4AE0(self):
		#sub_6E3B4AE0
		gadget = "B820000000C3"
		self.do(gadget)

		#mov     eax, 20h
		#retn


  def test_gadget_sub_6E3B4BA0(self):
		#sub_6E3B4BA0
		gadget = "8B49148B51088B4424048B490C8910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+14h]
		#mov     edx, [ecx+8]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget__IsAbnormalExit_TaskCollectionBasedetailsConcurrencyIBE_NXZ(self):
		#_IsAbnormalExit_TaskCollectionBasedetailsConcurrencyIBE_NXZ
		gadget = "33C03941140F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+14h], eax
		#setnz   al
		#retn


  def test_gadget_sub_6E3B4FB0(self):
		#sub_6E3B4FB0
		gadget = "8B442404C70000080000C7400400080000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 800h
		#mov     dword ptr [eax+4], 800h
		#retn    4


  def test_gadget_sub_6E3B5350(self):
		#sub_6E3B5350
		gadget = "83EC08D9EE8B44240CD914248B1424D95C240489108B5424048950048B916C0200008B897002000089500889480C83C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#fldz
		#mov     eax, [esp+8+arg_0]
		#fst     [esp+8+var_8]
		#mov     edx, [esp+8+var_8]
		#fstp    [esp+8+var_4]
		#mov     [eax], edx
		#mov     edx, [esp+8+var_4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+26Ch]
		#mov     ecx, [ecx+270h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6E3B5430(self):
		#sub_6E3B5430
		gadget = "D9442404D99940020000C20400"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+240h]
		#retn    4


  def test_gadget_sub_6E3B5620(self):
		#sub_6E3B5620
		gadget = "8A44240402C03281C803000024023081C8030000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#xor     al, [ecx+3C8h]
		#and     al, 2
		#xor     [ecx+3C8h], al
		#retn    4


  def test_gadget_sub_6E3B5640(self):
		#sub_6E3B5640
		gadget = "8A44240402C002C03281C803000024043081C8030000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#xor     al, [ecx+3C8h]
		#and     al, 4
		#xor     [ecx+3C8h], al
		#retn    4


  def test_gadget_sub_6E3B5660(self):
		#sub_6E3B5660
		gadget = "8A44240402C002C002C03281C803000024083081C8030000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#add     al, al
		#xor     al, [ecx+3C8h]
		#and     al, 8
		#xor     [ecx+3C8h], al
		#retn    4


  def test_gadget_sub_6E3B5680(self):
		#sub_6E3B5680
		gadget = "8A442404C0E0043281C803000024103081C8030000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 4
		#xor     al, [ecx+3C8h]
		#and     al, 10h
		#xor     [ecx+3C8h], al
		#retn    4


  def test_gadget_sub_6E3B56A0(self):
		#sub_6E3B56A0
		gadget = "8A442404C0E0053281C803000024203081C8030000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#shl     al, 5
		#xor     al, [ecx+3C8h]
		#and     al, 20h
		#xor     [ecx+3C8h], al
		#retn    4


  def test_gadget_sub_6E3B56C0(self):
		#sub_6E3B56C0
		gadget = "D9442404D99978030000C20400"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+378h]
		#retn    4


  def test_gadget_sub_6E3B56D0(self):
		#sub_6E3B56D0
		gadget = "8B4424048B108991A40300008B40048981A8030000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+3A4h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+3A8h], eax
		#retn    4


  def test_gadget_sub_6E3B5700(self):
		#sub_6E3B5700
		gadget = "8A81C8030000D944240C8A542404C0E207247F0AC28881C80300008B4424088B108991B80300000FB691C9030000325424108B400480E2013091C9030000D999C00300008981BC030000C21000"
		self.do(gadget)

		#mov     al, [ecx+3C8h]
		#fld     [esp+arg_8]
		#mov     dl, [esp+arg_0]
		#shl     dl, 7
		#and     al, 7Fh
		#or      al, dl
		#mov     [ecx+3C8h], al
		#mov     eax, [esp+arg_4]
		#mov     edx, [eax]
		#mov     [ecx+3B8h], edx
		#movzx   edx, byte ptr [ecx+3C9h]
		#xor     dl, [esp+arg_C]
		#mov     eax, [eax+4]
		#and     dl, 1
		#xor     [ecx+3C9h], dl
		#fstp    dword ptr [ecx+3C0h]
		#mov     [ecx+3BCh], eax
		#retn    10h


  def test_gadget_sub_6E3B5750(self):
		#sub_6E3B5750
		gadget = "8B4424048981C4030000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+3C4h], eax
		#retn    4


  def test_gadget_sub_6E3B5760(self):
		#sub_6E3B5760
		gadget = "8A4424048881E8030000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+3E8h], al
		#retn    4


  def test_gadget_sub_6E3B8C70(self):
		#sub_6E3B8C70
		gadget = "D9EE8BC133C9894804C7400801000000C70044C68B6E89480C894810894814D95018D9581C894820C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     dword ptr [eax+8], 1
		#mov     dword ptr [eax], offset off_6E8BC644
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#fst     dword ptr [eax+18h]
		#fstp    dword ptr [eax+1Ch]
		#mov     [eax+20h], ecx
		#retn


  def test_gadget_sub_6E3BBB40(self):
		#sub_6E3BBB40
		gadget = "8B51108B4424048B49148910894804C20800"
		self.do(gadget)

		#mov     edx, [ecx+10h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+14h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    8


  def test_gadget_sub_6E3BBB60(self):
		#sub_6E3BBB60
		gadget = "8B442404C70001000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#retn    8


  def test_gadget_sub_6E3BC7D0(self):
		#sub_6E3BC7D0
		gadget = "51D9057047A66E8B442408D91C24D90424D910D9580459C20400"
		self.do(gadget)

		#push    ecx
		#fld     flt_6EA64770
		#mov     eax, [esp+4+arg_0]
		#fstp    [esp+4+var_4]
		#fld     [esp+4+var_4]
		#fst     dword ptr [eax]
		#fstp    dword ptr [eax+4]
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E3BF140(self):
		#sub_6E3BF140
		gadget = "8B51108B4424048B49148910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+10h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+14h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E3BF250(self):
		#sub_6E3BF250
		gadget = "A0568DA56EC3"
		self.do(gadget)

		#mov     al, byte_6EA58D56
		#retn


  def test_gadget_sub_6E3BF260(self):
		#sub_6E3BF260
		gadget = "B8C4F6846EC3"
		self.do(gadget)

		#mov     eax, offset word_6E84F6C4
		#retn


  def test_gadget_sub_6E3BF2A0(self):
		#sub_6E3BF2A0
		gadget = "C7410C02000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+0Ch], 2
		#retn


  def test_gadget_unknown_libname_18(self):
		#unknown_libname_18
		gadget = "33C03941140F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+14h], eax
		#setz    al
		#retn


  def test_gadget_sub_6E3C1C50(self):
		#sub_6E3C1C50
		gadget = "C6416401C3"
		self.do(gadget)

		#mov     byte ptr [ecx+64h], 1
		#retn


  def test_gadget_sub_6E3C1D10(self):
		#sub_6E3C1D10
		gadget = "8B41148B4038C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#mov     eax, [eax+38h]
		#retn


  def test_gadget_sub_6E3C4E60(self):
		#sub_6E3C4E60
		gadget = "8BC1C60000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     byte ptr [eax], 0
		#retn


  def test_gadget_sub_6E3C5DE0(self):
		#sub_6E3C5DE0
		gadget = "8B013B41041BC040C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#cmp     eax, [ecx+4]
		#sbb     eax, eax
		#inc     eax
		#retn


  def test_gadget_sub_6E3C5DF0(self):
		#sub_6E3C5DF0
		gadget = "8B0133D23B41040F94C0C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#xor     edx, edx
		#cmp     eax, [ecx+4]
		#setz    al
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_45(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_45
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E3C62C0(self):
		#sub_6E3C62C0
		gadget = "B87D0000003B4424041BC0F7D8C3"
		self.do(gadget)

		#mov     eax, 7Dh
		#cmp     eax, [esp+arg_0]
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_6E3C62D0(self):
		#sub_6E3C62D0
		gadget = "8A5424088BC18B4C240489088A4C240C8850048A5424108848058B4C24148850088B54241866C74006000089480C895010C21800"
		self.do(gadget)

		#mov     dl, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     cl, [esp+arg_8]
		#mov     [eax+4], dl
		#mov     dl, [esp+arg_C]
		#mov     [eax+5], cl
		#mov     ecx, [esp+arg_10]
		#mov     [eax+8], dl
		#mov     edx, [esp+arg_14]
		#mov     word ptr [eax+6], 0
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], edx
		#retn    18h


  def test_gadget_sub_6E3C6A00(self):
		#sub_6E3C6A00
		gadget = "C7413800000000C3"
		self.do(gadget)

		#mov     dword ptr [ecx+38h], 0
		#retn


  def test_gadget_sub_6E3C6A10(self):
		#sub_6E3C6A10
		gadget = "8B413CC3"
		self.do(gadget)

		#mov     eax, [ecx+3Ch]
		#retn


  def test_gadget_sub_6E3C6A20(self):
		#sub_6E3C6A20
		gadget = "8D4140C3"
		self.do(gadget)

		#lea     eax, [ecx+40h]
		#retn


  def test_gadget_sub_6E3C9A90(self):
		#sub_6E3C9A90
		gadget = "6AFF68D9627B6E64A1000000005051A1F44AA66E33C4508D44240864A300000000C7442404000000008B4424188B4C241C89088B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7B62D9
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#mov     [esp+14h+var_10], 0
		#mov     eax, [esp+14h+arg_0]
		#mov     ecx, [esp+14h+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E3CA8E0(self):
		#sub_6E3CA8E0
		gadget = "6AFF68A9647B6E64A1000000005051A1F44AA66E33C4508D44240864A300000000C7442404000000008B4424188B4C241C89088B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7B64A9
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#mov     [esp+14h+var_10], 0
		#mov     eax, [esp+14h+arg_0]
		#mov     ecx, [esp+14h+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E3CDD70(self):
		#sub_6E3CDD70
		gadget = "C6411100C3"
		self.do(gadget)

		#mov     byte ptr [ecx+11h], 0
		#retn


  def test_gadget_sub_6E3CDD80(self):
		#sub_6E3CDD80
		gadget = "8A4111C3"
		self.do(gadget)

		#mov     al, [ecx+11h]
		#retn


  def test_gadget_sub_6E3CDD90(self):
		#sub_6E3CDD90
		gadget = "8B44240489410CC6411101C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+0Ch], eax
		#mov     byte ptr [ecx+11h], 1
		#retn    4


  def test_gadget_sub_6E3CDDA0(self):
		#sub_6E3CDDA0
		gadget = "8A4110C3"
		self.do(gadget)

		#mov     al, [ecx+10h]
		#retn


  def test_gadget_sub_6E3CDDB0(self):
		#sub_6E3CDDB0
		gadget = "C6411001C3"
		self.do(gadget)

		#mov     byte ptr [ecx+10h], 1
		#retn


  def test_gadget_sub_6E3CDDC0(self):
		#sub_6E3CDDC0
		gadget = "8B44240489412CC6411101C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+2Ch], eax
		#mov     byte ptr [ecx+11h], 1
		#retn    4


  def test_gadget_sub_6E3CDDD0(self):
		#sub_6E3CDDD0
		gadget = "8B4130C3"
		self.do(gadget)

		#mov     eax, [ecx+30h]
		#retn


  def test_gadget_sub_6E3CDDE0(self):
		#sub_6E3CDDE0
		gadget = "8B442404894130C6411101C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+30h], eax
		#mov     byte ptr [ecx+11h], 1
		#retn    4


  def test_gadget_GetTransferListEventUMSSchedulerProxydetailsConcurrencyQBEPAXXZ(self):
		#GetTransferListEventUMSSchedulerProxydetailsConcurrencyQBEPAXXZ
		gadget = "8B81E0000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0E0h]
		#retn


  def test_gadget_sub_6E3D48D0(self):
		#sub_6E3D48D0
		gadget = "8B8124010000C3"
		self.do(gadget)

		#mov     eax, [ecx+124h]
		#retn


  def test_gadget_sub_6E3D48E0(self):
		#sub_6E3D48E0
		gadget = "FF8198000000C3"
		self.do(gadget)

		#inc     dword ptr [ecx+98h]
		#retn


  def test_gadget_sub_6E3D58A0(self):
		#sub_6E3D58A0
		gadget = "8D816CFFFFFFC3"
		self.do(gadget)

		#lea     eax, [ecx-94h]
		#retn


  def test_gadget_sub_6E3D58B0(self):
		#sub_6E3D58B0
		gadget = "8D819C000000C3"
		self.do(gadget)

		#lea     eax, [ecx+9Ch]
		#retn


  def test_gadget_sub_6E3D5920(self):
		#sub_6E3D5920
		gadget = "8D4158C3"
		self.do(gadget)

		#lea     eax, [ecx+58h]
		#retn


  def test_gadget_sub_6E3D5950(self):
		#sub_6E3D5950
		gadget = "8B8120010000C3"
		self.do(gadget)

		#mov     eax, [ecx+120h]
		#retn


  def test_gadget_sub_6E3DA730(self):
		#sub_6E3DA730
		gadget = "8B442404894104C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+4], eax
		#retn    4


  def test_gadget_sub_6E3DA760(self):
		#sub_6E3DA760
		gadget = "D9EEDD5908C3"
		self.do(gadget)

		#fldz
		#fstp    qword ptr [ecx+8]
		#retn


  def test_gadget_sub_6E3DA7E0(self):
		#sub_6E3DA7E0
		gadget = "8B44240489088B4904894804C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [eax], ecx
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E3E0750(self):
		#sub_6E3E0750
		gadget = "8B4424048981B8010000C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+1B8h], eax
		#retn    4


  def test_gadget_sub_6E3E0BA0(self):
		#sub_6E3E0BA0
		gadget = "8B812C010000C3"
		self.do(gadget)

		#mov     eax, [ecx+12Ch]
		#retn


  def test_gadget_GetNumberOfBoundContextsSchedulerBasedetailsConcurrencyIBEKXZ(self):
		#GetNumberOfBoundContextsSchedulerBasedetailsConcurrencyIBEKXZ
		gadget = "8B81E4000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0E4h]
		#retn


  def test_gadget_sub_6E3E0C00(self):
		#sub_6E3E0C00
		gadget = "8A81ED0100002401C3"
		self.do(gadget)

		#mov     al, [ecx+1EDh]
		#and     al, 1
		#retn


  def test_gadget_sub_6E3E0C40(self):
		#sub_6E3E0C40
		gadget = "8A81A0010000C0E807C3"
		self.do(gadget)

		#mov     al, [ecx+1A0h]
		#shr     al, 7
		#retn


  def test_gadget_sub_6E3E0C50(self):
		#sub_6E3E0C50
		gadget = "DD81D4000000C3"
		self.do(gadget)

		#fld     qword ptr [ecx+0D4h]
		#retn


  def test_gadget_sub_6E3E0C60(self):
		#sub_6E3E0C60
		gadget = "DD81CC000000C3"
		self.do(gadget)

		#fld     qword ptr [ecx+0CCh]
		#retn


  def test_gadget_sub_6E3E0C70(self):
		#sub_6E3E0C70
		gadget = "8A8128010000C3"
		self.do(gadget)

		#mov     al, [ecx+128h]
		#retn


  def test_gadget_sub_6E3E0CC0(self):
		#sub_6E3E0CC0
		gadget = "DD8124010000C3"
		self.do(gadget)

		#fld     qword ptr [ecx+124h]
		#retn


  def test_gadget_sub_6E3E0CD0(self):
		#sub_6E3E0CD0
		gadget = "8A81A0010000C0E8062401C3"
		self.do(gadget)

		#mov     al, [ecx+1A0h]
		#shr     al, 6
		#and     al, 1
		#retn


  def test_gadget_sub_6E3E0DA0(self):
		#sub_6E3E0DA0
		gadget = "8A81A1010000C0E8062401C3"
		self.do(gadget)

		#mov     al, [ecx+1A1h]
		#shr     al, 6
		#and     al, 1
		#retn


  def test_gadget_sub_6E3E0DC0(self):
		#sub_6E3E0DC0
		gadget = "8A81ED010000C0E8062401C3"
		self.do(gadget)

		#mov     al, [ecx+1EDh]
		#shr     al, 6
		#and     al, 1
		#retn


  def test_gadget_sub_6E3E0DE0(self):
		#sub_6E3E0DE0
		gadget = "83B930010000020F9EC0C3"
		self.do(gadget)

		#cmp     dword ptr [ecx+130h], 2
		#setle   al
		#retn


  def test_gadget_sub_6E3E1680(self):
		#sub_6E3E1680
		gadget = "8B81F4010000C3"
		self.do(gadget)

		#mov     eax, [ecx+1F4h]
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_47(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_47
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E3EAAC0(self):
		#sub_6E3EAAC0
		gadget = "8A4138C3"
		self.do(gadget)

		#mov     al, [ecx+38h]
		#retn


  def test_gadget_sub_6E3EAAD0(self):
		#sub_6E3EAAD0
		gadget = "DD4148C3"
		self.do(gadget)

		#fld     qword ptr [ecx+48h]
		#retn


  def test_gadget_sub_6E3EAAE0(self):
		#sub_6E3EAAE0
		gadget = "8A4158C3"
		self.do(gadget)

		#mov     al, [ecx+58h]
		#retn


  def test_gadget_sub_6E3EAAF0(self):
		#sub_6E3EAAF0
		gadget = "8B415CC3"
		self.do(gadget)

		#mov     eax, [ecx+5Ch]
		#retn


  def test_gadget_sub_6E3EAB00(self):
		#sub_6E3EAB00
		gadget = "8A81F4000000C3"
		self.do(gadget)

		#mov     al, [ecx+0F4h]
		#retn


  def test_gadget_GetNumberOfActiveVirtualProcessorsSchedulerBasedetailsConcurrencyIBEIXZ(self):
		#GetNumberOfActiveVirtualProcessorsSchedulerBasedetailsConcurrencyIBEIXZ
		gadget = "8B81F8000000C3"
		self.do(gadget)

		#mov     eax, [ecx+0F8h]
		#retn


  def test_gadget_sub_6E3EAB30(self):
		#sub_6E3EAB30
		gadget = "FF4104C3"
		self.do(gadget)

		#inc     dword ptr [ecx+4]
		#retn


  def test_gadget_unknown_libname_19(self):
		#unknown_libname_19
		gadget = "568BF1E818FBFFFF8BCE5EE970FCFFFF"
		self.do(gadget)

		#push    esi
		#mov     esi, ecx
		#call    sub_6E3EB690
		#mov     ecx, esi
		#pop     esi
		#jmp     sub_6E3EB7F0


  def test_gadget_sub_6E3EBDC0(self):
		#sub_6E3EBDC0
		gadget = "DD05580B856EC3"
		self.do(gadget)

		#fld     ds:dbl_6E850B58
		#retn


  def test_gadget_sub_6E3ECBF0(self):
		#sub_6E3ECBF0
		gadget = "DD442404DD5948C20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    qword ptr [ecx+48h]
		#retn    8


  def test_gadget_sub_6E3ED7F0(self):
		#sub_6E3ED7F0
		gadget = "8A442404884146C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+46h], al
		#retn    4


  def test_gadget_sub_6E3F2A00(self):
		#sub_6E3F2A00
		gadget = "32C0C21C00"
		self.do(gadget)

		#xor     al, al
		#retn    1Ch


  def test_gadget_sub_6E3F2A30(self):
		#sub_6E3F2A30
		gadget = "D9442404C20400"
		self.do(gadget)

		#fld     [esp+arg_0]
		#retn    4


  def test_gadget_sub_6E3F2A60(self):
		#sub_6E3F2A60
		gadget = "8B4424048B0D9C578C6E8B15A0578C6E8908895004C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, ds:dword_6E8C579C
		#mov     edx, ds:dword_6E8C57A0
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#retn    4


  def test_gadget_sub_6E3F2A80(self):
		#sub_6E3F2A80
		gadget = "D9EEC3"
		self.do(gadget)

		#fldz
		#retn


  def test_gadget_sub_6E3F2A90(self):
		#sub_6E3F2A90
		gadget = "DD81A8000000C3"
		self.do(gadget)

		#fld     qword ptr [ecx+0A8h]
		#retn


  def test_gadget_sub_6E3F2AA0(self):
		#sub_6E3F2AA0
		gadget = "8A81B0000000C3"
		self.do(gadget)

		#mov     al, [ecx+0B0h]
		#retn


  def test_gadget_sub_6E3F2AB0(self):
		#sub_6E3F2AB0
		gadget = "DD81A0000000C3"
		self.do(gadget)

		#fld     qword ptr [ecx+0A0h]
		#retn


  def test_gadget_sub_6E3F45E0(self):
		#sub_6E3F45E0
		gadget = "B8EC5D8C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendervideo; "RenderVideo"
		#retn


  def test_gadget_sub_6E3F5010(self):
		#sub_6E3F5010
		gadget = "B800628C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermedia; "RenderMedia"
		#retn


  def test_gadget_sub_6E3F5520(self):
		#sub_6E3F5520
		gadget = "8B51148B4424048B49188910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+14h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+18h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E3F5540(self):
		#sub_6E3F5540
		gadget = "8A4112C3"
		self.do(gadget)

		#mov     al, [ecx+12h]
		#retn


  def test_gadget_sub_6E3F5560(self):
		#sub_6E3F5560
		gadget = "8A411DC3"
		self.do(gadget)

		#mov     al, [ecx+1Dh]
		#retn


  def test_gadget_sub_6E3F5570(self):
		#sub_6E3F5570
		gadget = "8A411CC3"
		self.do(gadget)

		#mov     al, [ecx+1Ch]
		#retn


  def test_gadget_sub_6E3F5580(self):
		#sub_6E3F5580
		gadget = "D94124C3"
		self.do(gadget)

		#fld     dword ptr [ecx+24h]
		#retn


  def test_gadget_sub_6E3F5590(self):
		#sub_6E3F5590
		gadget = "8A4130C6413000C3"
		self.do(gadget)

		#mov     al, [ecx+30h]
		#mov     byte ptr [ecx+30h], 0
		#retn


  def test_gadget_sub_6E3F55A0(self):
		#sub_6E3F55A0
		gadget = "8B412CC3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#retn


  def test_gadget__Java_com_sun_webkit_graphics_WCMediaPlayer_notifySizeChanged24(self):
		#_Java_com_sun_webkit_graphics_WCMediaPlayer_notifySizeChanged24
		gadget = "8B54240C8B4424148B4C2418894214894A18C21800"
		self.do(gadget)

		#mov     edx, [esp+arg_8]
		#mov     eax, [esp+arg_10]
		#mov     ecx, [esp+arg_14]
		#mov     [edx+14h], eax
		#mov     [edx+18h], ecx
		#retn    18h


  def test_gadget_sub_6E3F6FD0(self):
		#sub_6E3F6FD0
		gadget = "B87C758C6EC3"
		self.do(gadget)

		#mov     eax, offset aRenderfullscre; "RenderFullScreen"
		#retn


  def test_gadget_0facetlocalestdIAEIZ_2(self):
		#0facetlocalestdIAEIZ_2
		gadget = "8BC18B4C2404C7009CB58C6E894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8CB59C
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E3FA090(self):
		#sub_6E3FA090
		gadget = "8BC18B4C24048B118910C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#retn    4


  def test_gadget_sub_6E3FA100(self):
		#sub_6E3FA100
		gadget = "8B44240489415CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+5Ch], eax
		#retn    4


  def test_gadget_sub_6E3FA520(self):
		#sub_6E3FA520
		gadget = "8A4140C3"
		self.do(gadget)

		#mov     al, [ecx+40h]
		#retn


  def test_gadget_sub_6E3FA530(self):
		#sub_6E3FA530
		gadget = "8A442404884140C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+40h], al
		#retn    4


  def test_gadget_sub_6E3FA540(self):
		#sub_6E3FA540
		gadget = "8B4108C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#retn


  def test_gadget_sub_6E3FF0B0(self):
		#sub_6E3FF0B0
		gadget = "33C03881940000000F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [ecx+94h], al
		#setz    al
		#retn


  def test_gadget_sub_6E401380(self):
		#sub_6E401380
		gadget = "8B442404894170C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+70h], eax
		#retn    4


  def test_gadget_sub_6E401390(self):
		#sub_6E401390
		gadget = "8B442404894174C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     [ecx+74h], eax
		#retn    4


  def test_gadget_sub_6E402020(self):
		#sub_6E402020
		gadget = "D94424088B442404DD05C0BC8C6ED8C9DD05B8BC8C6EDCC1D9C9D918D9C1DD05B0BC8C6EDCC9D9C0DEE2D9C9D95C2408D9442408D95004D9C3DD05A8BC8C6EDCC9D9C0DEE2D9C9D95C2408D9442408D95008D9C5D8CDDEEDD9CCD95C2408D9442408D9500CD9C5DC0DA0BC8C6EDEC4D9CBD95810D9CBD95814D9C9D95818D9581CD9C9DC0D98BC8C6EDEC1D95820C3"
		self.do(gadget)

		#fld     [esp+arg_4]
		#mov     eax, [esp+arg_0]
		#fld     ds:dbl_6E8CBCC0
		#fmul    st, st(1)
		#fld     ds:dbl_6E8CBCB8
		#fadd    st(1), st
		#fxch    st(1)
		#fstp    dword ptr [eax]
		#fld     st(1)
		#fld     ds:dbl_6E8CBCB0
		#fmul    st(1), st
		#fld     st
		#fsubrp  st(2), st
		#fxch    st(1)
		#fstp    [esp+arg_4]
		#fld     [esp+arg_4]
		#fst     dword ptr [eax+4]
		#fld     st(3)
		#fld     ds:dbl_6E8CBCA8
		#fmul    st(1), st
		#fld     st
		#fsubrp  st(2), st
		#fxch    st(1)
		#fstp    [esp+arg_4]
		#fld     [esp+arg_4]
		#fst     dword ptr [eax+8]
		#fld     st(5)
		#fmul    st, st(5)
		#fsubp   st(5), st
		#fxch    st(4)
		#fstp    [esp+arg_4]
		#fld     [esp+arg_4]
		#fst     dword ptr [eax+0Ch]
		#fld     st(5)
		#fmul    ds:dbl_6E8CBCA0
		#faddp   st(4), st
		#fxch    st(3)
		#fstp    dword ptr [eax+10h]
		#fxch    st(3)
		#fstp    dword ptr [eax+14h]
		#fxch    st(1)
		#fstp    dword ptr [eax+18h]
		#fstp    dword ptr [eax+1Ch]
		#fxch    st(1)
		#fmul    ds:dbl_6E8CBC98
		#faddp   st(1), st
		#fstp    dword ptr [eax+20h]
		#retn


  def test_gadget_sub_6E4041D0(self):
		#sub_6E4041D0
		gadget = "33C0837978060F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx+78h], 6
		#setnz   al
		#retn


  def test_gadget_sub_6E408B10(self):
		#sub_6E408B10
		gadget = "C7417400000000C20400"
		self.do(gadget)

		#mov     dword ptr [ecx+74h], 0
		#retn    4


  def test_gadget_sub_6E409FA0(self):
		#sub_6E409FA0
		gadget = "5355568BF18B068B50088B4424100FB66C02078A4C0203570FB67C02FF0346080FB6C90FB67402FF8A5C02030FB6440207885C24148D143F8D5C2D002BDA8B5424182BDE03D8891A0FB65C241403DB03C92BD92BDD2BDF03D85F03DE5E5D895A045BC20800"
		self.do(gadget)

		#push    ebx
		#push    ebp
		#push    esi
		#mov     esi, ecx
		#mov     eax, [esi]
		#mov     edx, [eax+8]
		#mov     eax, [esp+0Ch+arg_0]
		#movzx   ebp, byte ptr [edx+eax+7]
		#mov     cl, [edx+eax+3]
		#push    edi
		#movzx   edi, byte ptr [edx+eax-1]
		#add     eax, [esi+8]
		#movzx   ecx, cl
		#movzx   esi, byte ptr [edx+eax-1]
		#mov     bl, [edx+eax+3]
		#movzx   eax, byte ptr [edx+eax+7]
		#mov     byte ptr [esp+10h+arg_0], bl
		#lea     edx, [edi+edi]
		#lea     ebx, [ebp+ebp+0]
		#sub     ebx, edx
		#mov     edx, [esp+10h+arg_4]
		#sub     ebx, esi
		#add     ebx, eax
		#mov     [edx], ebx
		#movzx   ebx, byte ptr [esp+10h+arg_0]
		#add     ebx, ebx
		#add     ecx, ecx
		#sub     ebx, ecx
		#sub     ebx, ebp
		#sub     ebx, edi
		#add     ebx, eax
		#pop     edi
		#add     ebx, esi
		#pop     esi
		#pop     ebp
		#mov     [edx+4], ebx
		#pop     ebx
		#retn    8


  def test_gadget_unknown_libname_21(self):
		#unknown_libname_21
		gadget = "8BC133C98908894804894808C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#retn


  def test_gadget_sub_6E40EE20(self):
		#sub_6E40EE20
		gadget = "8B5424088B442404568B322B7124578B7A042B79288B4A088B520C8978045F893089480889500C5EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, [esp+arg_0]
		#push    esi
		#mov     esi, [edx]
		#sub     esi, [ecx+24h]
		#push    edi
		#mov     edi, [edx+4]
		#sub     edi, [ecx+28h]
		#mov     ecx, [edx+8]
		#mov     edx, [edx+0Ch]
		#mov     [eax+4], edi
		#pop     edi
		#mov     [eax], esi
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#pop     esi
		#retn    8


  def test_gadget_sub_6E40EE50(self):
		#sub_6E40EE50
		gadget = "8B442404C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#retn    8


  def test_gadget_sub_6E40EE60(self):
		#sub_6E40EE60
		gadget = "8B4424088B5124568B7128578B388B40042BF08B44240C2BD789108B512C8B49305F89700489500889480C5EC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     edx, [ecx+24h]
		#push    esi
		#mov     esi, [ecx+28h]
		#push    edi
		#mov     edi, [eax]
		#mov     eax, [eax+4]
		#sub     esi, eax
		#mov     eax, [esp+8+arg_0]
		#sub     edx, edi
		#mov     [eax], edx
		#mov     edx, [ecx+2Ch]
		#mov     ecx, [ecx+30h]
		#pop     edi
		#mov     [eax+4], esi
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#pop     esi
		#retn    8


  def test_gadget_sub_6E40F560(self):
		#sub_6E40F560
		gadget = "D9EE8BC133C9BA01000000895004C700D8C48C6E89480889480C89481089481489481889481C88482089482489482889482C894830D95034D95038568B742408D9503CD95040897044D950485ED9504CD95050D95054D95058D9505CD95060D9586489486888506CC7407002000000894874C20400"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     edx, 1
		#mov     [eax+4], edx
		#mov     dword ptr [eax], offset off_6E8CC4D8
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], cl
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#fst     dword ptr [eax+34h]
		#fst     dword ptr [eax+38h]
		#push    esi
		#mov     esi, [esp+4+arg_0]
		#fst     dword ptr [eax+3Ch]
		#fst     dword ptr [eax+40h]
		#mov     [eax+44h], esi
		#fst     dword ptr [eax+48h]
		#pop     esi
		#fst     dword ptr [eax+4Ch]
		#fst     dword ptr [eax+50h]
		#fst     dword ptr [eax+54h]
		#fst     dword ptr [eax+58h]
		#fst     dword ptr [eax+5Ch]
		#fst     dword ptr [eax+60h]
		#fstp    dword ptr [eax+64h]
		#mov     [eax+68h], ecx
		#mov     [eax+6Ch], dl
		#mov     dword ptr [eax+70h], 2
		#mov     [eax+74h], ecx
		#retn    4


  def test_gadget_sub_6E4106A0(self):
		#sub_6E4106A0
		gadget = "B803000000C3"
		self.do(gadget)

		#mov     eax, 3
		#retn


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_73(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_73
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E410CE0(self):
		#sub_6E410CE0
		gadget = "B8DCCC8C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlta; "RenderMathMLTable"
		#retn


  def test_gadget_sub_6E4118B0(self):
		#sub_6E4118B0
		gadget = "B884DD8C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlfe; "RenderMathMLFenced"
		#retn


  def test_gadget_sub_6E4120A0(self):
		#sub_6E4120A0
		gadget = "B81CE28C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlfr; "RenderMathMLFraction"
		#retn


  def test_gadget_sub_6E412670(self):
		#sub_6E412670
		gadget = "B8B4E68C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlma; "RenderMathMLMath"
		#retn


  def test_gadget_sub_6E413480(self):
		#sub_6E413480
		gadget = "B814F08C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlro; "RenderMathMLRoot"
		#retn


  def test_gadget_sub_6E414330(self):
		#sub_6E414330
		gadget = "B85CF98C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlsq; "RenderMathMLSquareRoot"
		#retn


  def test_gadget_sub_6E414390(self):
		#sub_6E414390
		gadget = "B8E4FD8C6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlsu; "RenderMathMLSubSup"
		#retn


  def test_gadget_sub_6E4149E0(self):
		#sub_6E4149E0
		gadget = "B86C028D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendermathmlun; "RenderMathMLUnderOver"
		#retn


  def test_gadget_sub_6E41A070(self):
		#sub_6E41A070
		gadget = "518B44240833C9890C24890889480489480859C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#pop     ecx
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_65(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_65
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_66(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_66
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_67(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_67
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_68(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_68
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E41DC90(self):
		#sub_6E41DC90
		gadget = "8BC18B4C2404C70001000000D94104D958048B51088950088B490C89480CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#fld     dword ptr [ecx+4]
		#fstp    dword ptr [eax+4]
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     ecx, [ecx+0Ch]
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_0DNameNodeIAEXZ(self):
		#0DNameNodeIAEXZ
		gadget = "8BC1C70001000000C7400400000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_6E41E370(self):
		#sub_6E41E370
		gadget = "8089A000000001C3"
		self.do(gadget)

		#or      byte ptr [ecx+0A0h], 1
		#retn


  def test_gadget_sub_6E41E380(self):
		#sub_6E41E380
		gadget = "8B4424048B514089108B51448950048B51488B494C89500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+40h]
		#mov     [eax], edx
		#mov     edx, [ecx+44h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+48h]
		#mov     ecx, [ecx+4Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E41E3A0(self):
		#sub_6E41E3A0
		gadget = "8B4424048B515089108B51548950048B51588B495C89500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+50h]
		#mov     [eax], edx
		#mov     edx, [ecx+54h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+58h]
		#mov     ecx, [ecx+5Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E41E3C0(self):
		#sub_6E41E3C0
		gadget = "8D4160C3"
		self.do(gadget)

		#lea     eax, [ecx+60h]
		#retn


  def test_gadget_sub_6E41E3D0(self):
		#sub_6E41E3D0
		gadget = "8B44240456578D7160B90C0000008BF8F3A55F5EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#push    esi
		#push    edi
		#lea     esi, [ecx+60h]
		#mov     ecx, 0Ch
		#mov     edi, eax
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E41E3F0(self):
		#sub_6E41E3F0
		gadget = "8B4424048B512089108B51248950048B51288B492C89500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+20h]
		#mov     [eax], edx
		#mov     edx, [ecx+24h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+28h]
		#mov     ecx, [ecx+2Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E41E410(self):
		#sub_6E41E410
		gadget = "8B4424048B513089108B51348950048B51388B493C89500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+30h]
		#mov     [eax], edx
		#mov     edx, [ecx+34h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+38h]
		#mov     ecx, [ecx+3Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E41E430(self):
		#sub_6E41E430
		gadget = "B864058D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgellip; "RenderSVGEllipse"
		#retn


  def test_gadget_sub_6E41F160(self):
		#sub_6E41F160
		gadget = "B81C088D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgpath; "RenderSVGPath"
		#retn


  def test_gadget_sub_6E41F780(self):
		#sub_6E41F780
		gadget = "B8D40A8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgrect; "RenderSVGRect"
		#retn


  def test_gadget_sub_6E420DA0(self):
		#sub_6E420DA0
		gadget = "B8940D8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgshape; "RenderSVGShape"
		#retn


  def test_gadget_sub_6E421B00(self):
		#sub_6E421B00
		gadget = "80495C01C3"
		self.do(gadget)

		#or      byte ptr [ecx+5Ch], 1
		#retn


  def test_gadget_sub_6E421B10(self):
		#sub_6E421B10
		gadget = "8A415C2401C3"
		self.do(gadget)

		#mov     al, [ecx+5Ch]
		#and     al, 1
		#retn


  def test_gadget_sub_6E421B20(self):
		#sub_6E421B20
		gadget = "B8A0148D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgconta; "RenderSVGContainer"
		#retn


  def test_gadget_sub_6E421B30(self):
		#sub_6E421B30
		gadget = "8B4424048B513C89108B51408950048B51448B494889500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+3Ch]
		#mov     [eax], edx
		#mov     edx, [ecx+40h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+44h]
		#mov     ecx, [ecx+48h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E421B50(self):
		#sub_6E421B50
		gadget = "8B4424048B514C89108B51508950048B51548B495889500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+4Ch]
		#mov     [eax], edx
		#mov     edx, [ecx+50h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+54h]
		#mov     ecx, [ecx+58h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E422290(self):
		#sub_6E422290
		gadget = "32C0C3"
		self.do(gadget)

		#xor     al, al
		#retn


  def test_gadget_sub_6E4222A0(self):
		#sub_6E4222A0
		gadget = "83EC08D9EE8B44240CD914248B1424D95C240489108B5424048950048B51788B497C89500889480C83C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#fldz
		#mov     eax, [esp+8+arg_0]
		#fst     [esp+8+var_8]
		#mov     edx, [esp+8+var_8]
		#fstp    [esp+8+var_4]
		#mov     [eax], edx
		#mov     edx, [esp+8+var_4]
		#mov     [eax+4], edx
		#mov     edx, [ecx+78h]
		#mov     ecx, [ecx+7Ch]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6E4222D0(self):
		#sub_6E4222D0
		gadget = "80496C01C3"
		self.do(gadget)

		#or      byte ptr [ecx+6Ch], 1
		#retn


  def test_gadget_sub_6E4222E0(self):
		#sub_6E4222E0
		gadget = "8B44240456578DB180000000B90C0000008BF8F3A55F5EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#push    esi
		#push    edi
		#lea     esi, [ecx+80h]
		#mov     ecx, 0Ch
		#mov     edi, eax
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E422BD0(self):
		#sub_6E422BD0
		gadget = "B8A81B8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvggradi; "RenderSVGGradientStop"
		#retn


  def test_gadget_sub_6E422D10(self):
		#sub_6E422D10
		gadget = "B8681E8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvghidde; "RenderSVGHiddenContainer"
		#retn


  def test_gadget_sub_6E422FA0(self):
		#sub_6E422FA0
		gadget = "80492001C3"
		self.do(gadget)

		#or      byte ptr [ecx+20h], 1
		#retn


  def test_gadget_sub_6E422FB0(self):
		#sub_6E422FB0
		gadget = "8A41202401C3"
		self.do(gadget)

		#mov     al, [ecx+20h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E422FC0(self):
		#sub_6E422FC0
		gadget = "80492002C3"
		self.do(gadget)

		#or      byte ptr [ecx+20h], 2
		#retn


  def test_gadget_sub_6E422FD0(self):
		#sub_6E422FD0
		gadget = "B818218D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgimage; "RenderSVGImage"
		#retn


  def test_gadget_sub_6E422FE0(self):
		#sub_6E422FE0
		gadget = "8D4128C3"
		self.do(gadget)

		#lea     eax, [ecx+28h]
		#retn


  def test_gadget_sub_6E422FF0(self):
		#sub_6E422FF0
		gadget = "8B4424048B515889108B515C8950048B51608B496489500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+58h]
		#mov     [eax], edx
		#mov     edx, [ecx+5Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx+60h]
		#mov     ecx, [ecx+64h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E423010(self):
		#sub_6E423010
		gadget = "8B4424048B517889108B517C8950048B91800000008B898400000089500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+78h]
		#mov     [eax], edx
		#mov     edx, [ecx+7Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx+80h]
		#mov     ecx, [ecx+84h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E423040(self):
		#sub_6E423040
		gadget = "8B44240456578D7128B90C0000008BF8F3A55F5EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#push    esi
		#push    edi
		#lea     esi, [ecx+28h]
		#mov     ecx, 0Ch
		#mov     edi, eax
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E423B80(self):
		#sub_6E423B80
		gadget = "B854248D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvginlin; "RenderSVGInline"
		#retn


  def test_gadget_sub_6E423C10(self):
		#sub_6E423C10
		gadget = "D9413CC3"
		self.do(gadget)

		#fld     dword ptr [ecx+3Ch]
		#retn


  def test_gadget_sub_6E424BF0(self):
		#sub_6E424BF0
		gadget = "B8C0278D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvginl_0; "RenderSVGInlineText"
		#retn


  def test_gadget_sub_6E426000(self):
		#sub_6E426000
		gadget = "B8382D8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgresou; "RenderSVGResourceClipper"
		#retn


  def test_gadget_sub_6E4278E0(self):
		#sub_6E4278E0
		gadget = "B818338D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_0; "RenderSVGResourceFilter"
		#retn


  def test_gadget_sub_6E4278F0(self):
		#sub_6E4278F0
		gadget = "A198C2A56EC3"
		self.do(gadget)

		#mov     eax, dword_6EA5C298
		#retn


  def test_gadget_sub_6E42A5B0(self):
		#sub_6E42A5B0
		gadget = "B8E8388D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_1; "RenderSVGResourceLinearGradient"
		#retn


  def test_gadget_sub_6E42A5C0(self):
		#sub_6E42A5C0
		gadget = "A1FCC2A56EC3"
		self.do(gadget)

		#mov     eax, dword_6EA5C2FC
		#retn


  def test_gadget_sub_6E42A750(self):
		#sub_6E42A750
		gadget = "B8D03B8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_2; "RenderSVGResourceMarker"
		#retn


  def test_gadget_sub_6E42A760(self):
		#sub_6E42A760
		gadget = "D9EE8B442404D910D95004D95008D9580CC20800"
		self.do(gadget)

		#fldz
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fst     dword ptr [eax+4]
		#fst     dword ptr [eax+8]
		#fstp    dword ptr [eax+0Ch]
		#retn    8


  def test_gadget_sub_6E42A780(self):
		#sub_6E42A780
		gadget = "A138C3A56EC3"
		self.do(gadget)

		#mov     eax, dword_6EA5C338
		#retn


  def test_gadget_sub_6E42B180(self):
		#sub_6E42B180
		gadget = "B8B03E8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_3; "RenderSVGResourceMasker"
		#retn


  def test_gadget_sub_6E42B190(self):
		#sub_6E42B190
		gadget = "A1EC8CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CEC
		#retn


  def test_gadget_sub_6E42C730(self):
		#sub_6E42C730
		gadget = "B890418D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_4; "RenderSVGResourcePattern"
		#retn


  def test_gadget_sub_6E42C740(self):
		#sub_6E42C740
		gadget = "A19CC3A56EC3"
		self.do(gadget)

		#mov     eax, dword_6EA5C39C
		#retn


  def test_gadget_sub_6E42D710(self):
		#sub_6E42D710
		gadget = "B888448D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_5; "RenderSVGResourceRadialGradient"
		#retn


  def test_gadget_sub_6E42D720(self):
		#sub_6E42D720
		gadget = "A1D0C3A56EC3"
		self.do(gadget)

		#mov     eax, dword_6EA5C3D0
		#retn


  def test_gadget_sub_6E42D730(self):
		#sub_6E42D730
		gadget = "8B81EC000000C1E80283E003C3"
		self.do(gadget)

		#mov     eax, [ecx+0ECh]
		#shr     eax, 2
		#and     eax, 3
		#retn


  def test_gadget_sub_6E42D740(self):
		#sub_6E42D740
		gadget = "83EC3056578DB1B0000000B90C0000008D7C2408F3A58B7C243CB90C0000008D742408F3A55F5E83C430C20400"
		self.do(gadget)

		#sub     esp, 30h
		#push    esi
		#push    edi
		#lea     esi, [ecx+0B0h]
		#mov     ecx, 0Ch
		#lea     edi, [esp+38h+var_30]
		#rep movsd
		#mov     edi, [esp+38h+arg_0]
		#mov     ecx, 0Ch
		#lea     esi, [esp+38h+var_30]
		#rep movsd
		#pop     edi
		#pop     esi
		#add     esp, 30h
		#retn    4


  def test_gadget_sub_6E42D820(self):
		#sub_6E42D820
		gadget = "8BC133C9C700B4448D6E894804884808C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8D44B4
		#mov     [eax+4], ecx
		#mov     [eax+8], cl
		#retn


  def test_gadget_sub_6E42D840(self):
		#sub_6E42D840
		gadget = "A10CC4A56EC3"
		self.do(gadget)

		#mov     eax, dword_6EA5C40C
		#retn


  def test_gadget_sub_6E42E100(self):
		#sub_6E42E100
		gadget = "8A8124010000D0E82401C3"
		self.do(gadget)

		#mov     al, [ecx+124h]
		#shr     al, 1
		#and     al, 1
		#retn


  def test_gadget_sub_6E42E110(self):
		#sub_6E42E110
		gadget = "80892401000002C3"
		self.do(gadget)

		#or      byte ptr [ecx+124h], 2
		#retn


  def test_gadget_sub_6E42E120(self):
		#sub_6E42E120
		gadget = "B8D8488D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgroot; "RenderSVGRoot"
		#retn


  def test_gadget_sub_6E42E130(self):
		#sub_6E42E130
		gadget = "8B4424048B516889108B516C8950048B51708B497489500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+68h]
		#mov     [eax], edx
		#mov     edx, [ecx+6Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx+70h]
		#mov     ecx, [ecx+74h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E42E150(self):
		#sub_6E42E150
		gadget = "8B4424048B517C89108B91800000008950048B91840000008B898800000089500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+7Ch]
		#mov     [eax], edx
		#mov     edx, [ecx+80h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+84h]
		#mov     ecx, [ecx+88h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E42E180(self):
		#sub_6E42E180
		gadget = "8B4424048B918C00000089108B91900000008950048B91940000008B899800000089500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+8Ch]
		#mov     [eax], edx
		#mov     edx, [ecx+90h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+94h]
		#mov     ecx, [ecx+98h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E42E1B0(self):
		#sub_6E42E1B0
		gadget = "8B4424048B919C00000089108B91A00000008950048B91A40000008B89A800000089500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+9Ch]
		#mov     [eax], edx
		#mov     edx, [ecx+0A0h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+0A4h]
		#mov     ecx, [ecx+0A8h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E42F3D0(self):
		#sub_6E42F3D0
		gadget = "B8144C8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgtspan; "RenderSVGTSpan"
		#retn


  def test_gadget_sub_6E42F5A0(self):
		#sub_6E42F5A0
		gadget = "32C0C21400"
		self.do(gadget)

		#xor     al, al
		#retn    14h


  def test_gadget_sub_6E42F5B0(self):
		#sub_6E42F5B0
		gadget = "8B4424048B4018C1E80A83E001C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+18h]
		#shr     eax, 0Ah
		#and     eax, 1
		#retn    8


  def test_gadget_sub_6E4302C0(self):
		#sub_6E4302C0
		gadget = "D94160C3"
		self.do(gadget)

		#fld     dword ptr [ecx+60h]
		#retn


  def test_gadget_sub_6E430560(self):
		#sub_6E430560
		gadget = "80496C04C3"
		self.do(gadget)

		#or      byte ptr [ecx+6Ch], 4
		#retn


  def test_gadget_sub_6E430570(self):
		#sub_6E430570
		gadget = "B80C518D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgtext; "RenderSVGText"
		#retn


  def test_gadget_sub_6E4305C0(self):
		#sub_6E4305C0
		gadget = "8B44240456578D7170B90C0000008BF8F3A55F5EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#push    esi
		#push    edi
		#lea     esi, [ecx+70h]
		#mov     ecx, 0Ch
		#mov     edi, eax
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E430960(self):
		#sub_6E430960
		gadget = "B844548D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgtextp; "RenderSVGTextPath"
		#retn


  def test_gadget_sub_6E430C20(self):
		#sub_6E430C20
		gadget = "80496001C3"
		self.do(gadget)

		#or      byte ptr [ecx+60h], 1
		#retn


  def test_gadget_sub_6E430C30(self):
		#sub_6E430C30
		gadget = "8A4160D0E82401C3"
		self.do(gadget)

		#mov     al, [ecx+60h]
		#shr     al, 1
		#and     al, 1
		#retn


  def test_gadget_sub_6E430C40(self):
		#sub_6E430C40
		gadget = "8B44240456578D7168B90C0000008BF8F3A55F5EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#push    esi
		#push    edi
		#lea     esi, [ecx+68h]
		#mov     ecx, 0Ch
		#mov     edi, eax
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E430FD0(self):
		#sub_6E430FD0
		gadget = "8A81A00000002401C3"
		self.do(gadget)

		#mov     al, [ecx+0A0h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E430FE0(self):
		#sub_6E430FE0
		gadget = "8089A000000004C3"
		self.do(gadget)

		#or      byte ptr [ecx+0A0h], 4
		#retn


  def test_gadget_sub_6E430FF0(self):
		#sub_6E430FF0
		gadget = "B8A8598D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgviewp; "RenderSVGViewportContainer"
		#retn


  def test_gadget_sub_6E431000(self):
		#sub_6E431000
		gadget = "8D4170C3"
		self.do(gadget)

		#lea     eax, [ecx+70h]
		#retn


  def test_gadget_sub_6E432930(self):
		#sub_6E432930
		gadget = "D9EE8B5424048BC133C9895010C7006C8E8A6E89480489480889480CD95014D9501833D2D9501CC740200048000066895030D95834BAFFFF0000668950328B503883E2E189482489482889482CC700E4598D6E83CA0189503889483C894840894844894848C20400"
		self.do(gadget)

		#fldz
		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+10h], edx
		#mov     dword ptr [eax], offset off_6E8A8E6C
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#fst     dword ptr [eax+14h]
		#fst     dword ptr [eax+18h]
		#xor     edx, edx
		#fst     dword ptr [eax+1Ch]
		#mov     dword ptr [eax+20h], 4800h
		#mov     [eax+30h], dx
		#fstp    dword ptr [eax+34h]
		#mov     edx, 0FFFFh
		#mov     [eax+32h], dx
		#mov     edx, [eax+38h]
		#and     edx, 0FFFFFFE1h
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     dword ptr [eax], offset off_6E8D59E4
		#or      edx, 1
		#mov     [eax+38h], edx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#retn    4


  def test_gadget_sub_6E4329A0(self):
		#sub_6E4329A0
		gadget = "D94134C3"
		self.do(gadget)

		#fld     dword ptr [ecx+34h]
		#retn


  def test_gadget_sub_6E434B00(self):
		#sub_6E434B00
		gadget = "8B4424048B48048B513081E2001C000033C081FA000400000F94C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+4]
		#mov     edx, [ecx+30h]
		#and     edx, 1C00h
		#xor     eax, eax
		#cmp     edx, 400h
		#setz    al
		#retn


  def test_gadget_1_Scoped_lock_NonReentrantLockdetailsConcurrencyQAEXZ(self):
		#1_Scoped_lock_NonReentrantLockdetailsConcurrencyQAEXZ
		gadget = "8B01C70000000000C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     dword ptr [eax], 0
		#retn


  def test_gadget_sub_6E4399F0(self):
		#sub_6E4399F0
		gadget = "8B01C7400400000000C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_6E439A00(self):
		#sub_6E439A00
		gadget = "8B4104C70000000000C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     dword ptr [eax], 0
		#retn


  def test_gadget_sub_6E439A10(self):
		#sub_6E439A10
		gadget = "8B4104C7400400000000C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_6E439A20(self):
		#sub_6E439A20
		gadget = "8B4104C7400800000000C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     dword ptr [eax+8], 0
		#retn


  def test_gadget_sub_6E439A30(self):
		#sub_6E439A30
		gadget = "8B01C7400800000000C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     dword ptr [eax+8], 0
		#retn


  def test_gadget_sub_6E439A40(self):
		#sub_6E439A40
		gadget = "8B4108C70000000000C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     dword ptr [eax], 0
		#retn


  def test_gadget_sub_6E439A50(self):
		#sub_6E439A50
		gadget = "8B4108C7400400000000C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_6E43C2B0(self):
		#sub_6E43C2B0
		gadget = "8B5424088BC18B4C2404890833C989500489480889480C894810894814894818C20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#retn    8


  def test_gadget_sub_6E43D8E0(self):
		#sub_6E43D8E0
		gadget = "D94424088BC133C9D9581089088948048948088B4C240489480CC20800"
		self.do(gadget)

		#fld     [esp+arg_4]
		#mov     eax, ecx
		#xor     ecx, ecx
		#fstp    dword ptr [eax+10h]
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+0Ch], ecx
		#retn    8


  def test_gadget_sub_6E43EA80(self):
		#sub_6E43EA80
		gadget = "8BC18B4C2404890833C989480489480889480C89481089481489481889481C894820C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn    4


  def test_gadget_sub_6E441410(self):
		#sub_6E441410
		gadget = "8BC18B4C2404890833C989480488480889480C894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], cl
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E441630(self):
		#sub_6E441630
		gadget = "D9EE8BC133C9D910D9580489480888480C894810894814C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#fst     dword ptr [eax]
		#fstp    dword ptr [eax+4]
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cl
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_6E441650(self):
		#sub_6E441650
		gadget = "D9EE8BC1D91033C9D95804C740080100000088480C894810894814C20400"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fst     dword ptr [eax]
		#xor     ecx, ecx
		#fstp    dword ptr [eax+4]
		#mov     dword ptr [eax+8], 1
		#mov     [eax+0Ch], cl
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn    4


  def test_gadget_sub_6E444F20(self):
		#sub_6E444F20
		gadget = "518B44240C8B088B4424088B54241089088B0A894804FF01C704240000000059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_4]
		#mov     ecx, [eax]
		#mov     eax, [esp+4+arg_0]
		#mov     edx, [esp+4+arg_8]
		#mov     [eax], ecx
		#mov     ecx, [edx]
		#mov     [eax+4], ecx
		#inc     dword ptr [ecx]
		#mov     [esp+4+var_4], 0
		#pop     ecx
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_69(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_69
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_72(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_72
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E4463A0(self):
		#sub_6E4463A0
		gadget = "8B493433C03B0D0064A66E0F95C0C3"
		self.do(gadget)

		#mov     ecx, [ecx+34h]
		#xor     eax, eax
		#cmp     ecx, dword_6EA66400
		#setnz   al
		#retn


  def test_gadget_sub_6E4463B0(self):
		#sub_6E4463B0
		gadget = "33C083B990000000020F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword ptr [ecx+90h], 2
		#setz    al
		#retn


  def test_gadget_sub_6E4463D0(self):
		#sub_6E4463D0
		gadget = "DD81A00000008B442404DD18C20400"
		self.do(gadget)

		#fld     qword ptr [ecx+0A0h]
		#mov     eax, [esp+arg_0]
		#fstp    qword ptr [eax]
		#retn    4


  def test_gadget_sub_6E446530(self):
		#sub_6E446530
		gadget = "83EC0856578B442414DD0033C9DD5C24088B4424088BD0F7D103C18B4C240CF7D213CA8BD08BF10FACF216C1EE1633CE33C28BD08BF10FA4D60DF7D6C1E20DF7D203C213CE8BF08BF90FACFE0833F0C1EF0833F98BD68BCF0FA4F70303F603F603F603D613CF8BF18BC20FACF00FC1EE0F33D033CE8BF18BC20FA4C61BC1E01BF7D003D0F7D613CE8BC20FACC81F5FC1E91F33C25E83C408C3"
		self.do(gadget)

		#sub     esp, 8
		#push    esi
		#push    edi
		#mov     eax, [esp+10h+arg_0]
		#fld     qword ptr [eax]
		#xor     ecx, ecx
		#fstp    [esp+10h+var_8]
		#mov     eax, dword ptr [esp+10h+var_8]
		#mov     edx, eax
		#not     ecx
		#add     eax, ecx
		#mov     ecx, dword ptr [esp+10h+var_8+4]
		#not     edx
		#adc     ecx, edx
		#mov     edx, eax
		#mov     esi, ecx
		#shrd    edx, esi, 16h
		#shr     esi, 16h
		#xor     ecx, esi
		#xor     eax, edx
		#mov     edx, eax
		#mov     esi, ecx
		#shld    esi, edx, 0Dh
		#not     esi
		#shl     edx, 0Dh
		#not     edx
		#add     eax, edx
		#adc     ecx, esi
		#mov     esi, eax
		#mov     edi, ecx
		#shrd    esi, edi, 8
		#xor     esi, eax
		#shr     edi, 8
		#xor     edi, ecx
		#mov     edx, esi
		#mov     ecx, edi
		#shld    edi, esi, 3
		#add     esi, esi
		#add     esi, esi
		#add     esi, esi
		#add     edx, esi
		#adc     ecx, edi
		#mov     esi, ecx
		#mov     eax, edx
		#shrd    eax, esi, 0Fh
		#shr     esi, 0Fh
		#xor     edx, eax
		#xor     ecx, esi
		#mov     esi, ecx
		#mov     eax, edx
		#shld    esi, eax, 1Bh
		#shl     eax, 1Bh
		#not     eax
		#add     edx, eax
		#not     esi
		#adc     ecx, esi
		#mov     eax, edx
		#shrd    eax, ecx, 1Fh
		#pop     edi
		#shr     ecx, 1Fh
		#xor     eax, edx
		#pop     esi
		#add     esp, 8
		#retn


  def test_gadget_sub_6E44C8F0(self):
		#sub_6E44C8F0
		gadget = "8B4424048B514889108B514C8950048B51508B495489500889480CC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx+48h]
		#mov     [eax], edx
		#mov     edx, [ecx+4Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx+50h]
		#mov     ecx, [ecx+54h]
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E44E570(self):
		#sub_6E44E570
		gadget = "8B51188B4424048B491C8910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+18h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+1Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E44F0E0(self):
		#sub_6E44F0E0
		gadget = "8BC18B4C2404890833C989480489480889480C894810894814C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_73(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_73
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E452C20(self):
		#sub_6E452C20
		gadget = "8B5424088BC18B4C2404560FB67102570FB67A022BFE89380FB671010FB67A012BFE8978048B128B0981E1FF00000081E2FF0000002BD15F8950085EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#push    esi
		#movzx   esi, byte ptr [ecx+2]
		#push    edi
		#movzx   edi, byte ptr [edx+2]
		#sub     edi, esi
		#mov     [eax], edi
		#movzx   esi, byte ptr [ecx+1]
		#movzx   edi, byte ptr [edx+1]
		#sub     edi, esi
		#mov     [eax+4], edi
		#mov     edx, [edx]
		#mov     ecx, [ecx]
		#and     ecx, 0FFh
		#and     edx, 0FFh
		#sub     edx, ecx
		#pop     edi
		#mov     [eax+8], edx
		#pop     esi
		#retn    8


  def test_gadget_sub_6E452FD0(self):
		#sub_6E452FD0
		gadget = "8B4424048B088B510C8B0D4460A66E33C03B510C0F94C0C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax]
		#mov     edx, [ecx+0Ch]
		#mov     ecx, dword_6EA66044
		#xor     eax, eax
		#cmp     edx, [ecx+0Ch]
		#setz    al
		#retn    4


  def test_gadget_sub_6E453B60(self):
		#sub_6E453B60
		gadget = "8B4424048A108A44240802C03241598851582402304159C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+59h]
		#mov     [ecx+58h], dl
		#and     al, 2
		#xor     [ecx+59h], al
		#retn    8


  def test_gadget_sub_6E4545A0(self):
		#sub_6E4545A0
		gadget = "8B4424048B088A410C2401C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax]
		#mov     al, [ecx+0Ch]
		#and     al, 1
		#retn    4


  def test_gadget_sub_6E454D90(self):
		#sub_6E454D90
		gadget = "8D4164C3"
		self.do(gadget)

		#lea     eax, [ecx+64h]
		#retn


  def test_gadget_sub_6E455120(self):
		#sub_6E455120
		gadget = "D9EE8BC1D95804C70001000000C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fstp    dword ptr [eax+4]
		#mov     dword ptr [eax], 1
		#retn


  def test_gadget_sub_6E4558E0(self):
		#sub_6E4558E0
		gadget = "8D414CC3"
		self.do(gadget)

		#lea     eax, [ecx+4Ch]
		#retn


  def test_gadget_sub_6E4558F0(self):
		#sub_6E4558F0
		gadget = "8B4424048A108A44240802C032414D88514C240230414DC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+4Dh]
		#mov     [ecx+4Ch], dl
		#and     al, 2
		#xor     [ecx+4Dh], al
		#retn    8


  def test_gadget_sub_6E455BB0(self):
		#sub_6E455BB0
		gadget = "8B5424088BC18B4C2404C740040000000089480889500CC70030738D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D7330
		#retn    8


  def test_gadget_sub_6E456360(self):
		#sub_6E456360
		gadget = "8B5424088BC18B4C2404C740040100000089480889500CC7005C738D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D735C
		#retn    8


  def test_gadget_sub_6E456570(self):
		#sub_6E456570
		gadget = "8B5424088BC18B4C2404C740040200000089480889500CC7008C738D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 2
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D738C
		#retn    8


  def test_gadget_sub_6E456AA0(self):
		#sub_6E456AA0
		gadget = "8B5424088BC18B4C2404C740040300000089480889500CC700C0738D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 3
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D73C0
		#retn    8


  def test_gadget_sub_6E4573C0(self):
		#sub_6E4573C0
		gadget = "8B5424088BC18B4C2404C740040400000089480889500CC700A4748D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 4
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D74A4
		#retn    8


  def test_gadget_sub_6E4573E0(self):
		#sub_6E4573E0
		gadget = "8B4C24048B51088B4424088B40088B0A0108C20800"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx+8]
		#mov     eax, [esp+arg_4]
		#mov     eax, [eax+8]
		#mov     ecx, [edx]
		#add     [eax], ecx
		#retn    8


  def test_gadget_sub_6E457710(self):
		#sub_6E457710
		gadget = "8B5424088BC18B4C2404C740040500000089480889500CC700D0748D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 5
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D74D0
		#retn    8


  def test_gadget_sub_6E457730(self):
		#sub_6E457730
		gadget = "8B4424048B48088B5424088B42088B1101108B4904014804C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+8]
		#mov     edx, [esp+arg_4]
		#mov     eax, [edx+8]
		#mov     edx, [ecx]
		#add     [eax], edx
		#mov     ecx, [ecx+4]
		#add     [eax+4], ecx
		#retn    8


  def test_gadget_sub_6E458E80(self):
		#sub_6E458E80
		gadget = "8B5424088BC18B4C2404C740040800000089480889500CC70054758D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 8
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D7554
		#retn    8


  def test_gadget_sub_6E458EA0(self):
		#sub_6E458EA0
		gadget = "8B4C24048B4424088B51088B4008D902D800D918C20800"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     eax, [esp+arg_4]
		#mov     edx, [ecx+8]
		#mov     eax, [eax+8]
		#fld     dword ptr [edx]
		#fadd    dword ptr [eax]
		#fstp    dword ptr [eax]
		#retn    8


  def test_gadget_sub_6E459220(self):
		#sub_6E459220
		gadget = "8B5424088BC18B4C2404C740040900000089480889500CC70080758D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 9
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D7580
		#retn    8


  def test_gadget_sub_6E4598C0(self):
		#sub_6E4598C0
		gadget = "8B5424088BC18B4C2404C740040A00000089480889500CC700AC758D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0Ah
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D75AC
		#retn    8


  def test_gadget_sub_6E4598E0(self):
		#sub_6E4598E0
		gadget = "8B4424048B48088B5424088B4208D900D801D918D94104D84004D95804C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+8]
		#mov     edx, [esp+arg_4]
		#mov     eax, [edx+8]
		#fld     dword ptr [eax]
		#fadd    dword ptr [ecx]
		#fstp    dword ptr [eax]
		#fld     dword ptr [ecx+4]
		#fadd    dword ptr [eax+4]
		#fstp    dword ptr [eax+4]
		#retn    8


  def test_gadget_sub_6E459D80(self):
		#sub_6E459D80
		gadget = "8B5424088BC18B4C2404C740040B00000089480889500CC700D8758D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0Bh
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D75D8
		#retn    8


  def test_gadget_sub_6E45ABD0(self):
		#sub_6E45ABD0
		gadget = "8B5424088BC18B4C2404C740040C00000089480889500CC70004768D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0Ch
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D7604
		#retn    8


  def test_gadget_sub_6E45B400(self):
		#sub_6E45B400
		gadget = "8B5424088BC18B4C2404C740040D00000089480889500CC70030768D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0Dh
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D7630
		#retn    8


  def test_gadget_sub_6E45B840(self):
		#sub_6E45B840
		gadget = "8B5424088BC18B4C2404C740040E00000089480889500CC7005C768D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0Eh
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D765C
		#retn    8


  def test_gadget_sub_6E45B860(self):
		#sub_6E45B860
		gadget = "8B4424048B4808D941048B5424088B4208D95C2404D900D801D918D94004D8442404D95804D94108D84008D95808D9410CD8400CD9580CC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+8]
		#fld     dword ptr [ecx+4]
		#mov     edx, [esp+arg_4]
		#mov     eax, [edx+8]
		#fstp    [esp+arg_0]
		#fld     dword ptr [eax]
		#fadd    dword ptr [ecx]
		#fstp    dword ptr [eax]
		#fld     dword ptr [eax+4]
		#fadd    [esp+arg_0]
		#fstp    dword ptr [eax+4]
		#fld     dword ptr [ecx+8]
		#fadd    dword ptr [eax+8]
		#fstp    dword ptr [eax+8]
		#fld     dword ptr [ecx+0Ch]
		#fadd    dword ptr [eax+0Ch]
		#fstp    dword ptr [eax+0Ch]
		#retn    8


  def test_gadget_sub_6E45BA10(self):
		#sub_6E45BA10
		gadget = "D9055021856EC20800"
		self.do(gadget)

		#fld     ds:flt_6E852150
		#retn    8


  def test_gadget_sub_6E45BD40(self):
		#sub_6E45BD40
		gadget = "8B5424088BC18B4C2404C740040F00000089480889500CC70088768D6EC20800"
		self.do(gadget)

		#mov     edx, [esp+arg_4]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 0Fh
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], edx
		#mov     dword ptr [eax], offset off_6E8D7688
		#retn    8


  def test_gadget_sub_6E462DF0(self):
		#sub_6E462DF0
		gadget = "33C0888126010000898190000000C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [ecx+126h], al
		#mov     [ecx+90h], eax
		#retn


  def test_gadget_sub_6E462E00(self):
		#sub_6E462E00
		gadget = "51DD4178D91C24D9042459C3"
		self.do(gadget)

		#push    ecx
		#fld     qword ptr [ecx+78h]
		#fstp    [esp+4+var_4]
		#fld     [esp+4+var_4]
		#pop     ecx
		#retn


  def test_gadget_sub_6E4666C0(self):
		#sub_6E4666C0
		gadget = "8D416CC3"
		self.do(gadget)

		#lea     eax, [ecx+6Ch]
		#retn


  def test_gadget_sub_6E4666D0(self):
		#sub_6E4666D0
		gadget = "8B4424048A108A44240802C032416D88516C240230416DC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+6Dh]
		#mov     [ecx+6Ch], dl
		#and     al, 2
		#xor     [ecx+6Dh], al
		#retn    8


  def test_gadget_sub_6E4671A0(self):
		#sub_6E4671A0
		gadget = "8B4424048A108A44240802C03241518851502402304151C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+51h]
		#mov     [ecx+50h], dl
		#and     al, 2
		#xor     [ecx+51h], al
		#retn    8


  def test_gadget_sub_6E467360(self):
		#sub_6E467360
		gadget = "8B44240CC70007000000C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     dword ptr [eax], 7
		#retn    0Ch


  def test_gadget_sub_6E4673A0(self):
		#sub_6E4673A0
		gadget = "8B5424048BC18B480481E100E0FAFF81C900E0020089480433C9C7000100000089480888480C8B0A894810C20400"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#mov     ecx, [eax+4]
		#and     ecx, 0FFFAE000h
		#or      ecx, 2E000h
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cl
		#mov     ecx, [edx]
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E4673D0(self):
		#sub_6E4673D0
		gadget = "8BC18B50048B4C240483E13FC1E10D81E20000F8FF0BCA89480433C9C7000100000089480888480C8B4C24088B11895010C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     edx, [eax+4]
		#mov     ecx, [esp+arg_0]
		#and     ecx, 3Fh
		#shl     ecx, 0Dh
		#and     edx, 0FFF80000h
		#or      ecx, edx
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], cl
		#mov     ecx, [esp+arg_4]
		#mov     edx, [ecx]
		#mov     [eax+10h], edx
		#retn    8


  def test_gadget_sub_6E467530(self):
		#sub_6E467530
		gadget = "8BC18B4C24048B500483E13FC1E10D81E20100F8FF0BCA83C9018948048B4C2408C700010000008B51088950088B510C89500C8B4910894810C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [eax+4]
		#and     ecx, 3Fh
		#shl     ecx, 0Dh
		#and     edx, 0FFF80001h
		#or      ecx, edx
		#or      ecx, 1
		#mov     [eax+4], ecx
		#mov     ecx, [esp+arg_4]
		#mov     dword ptr [eax], 1
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+0Ch], edx
		#mov     ecx, [ecx+10h]
		#mov     [eax+10h], ecx
		#retn    8


  def test_gadget_sub_6E469FE0(self):
		#sub_6E469FE0
		gadget = "8B4424048A108A44240802C03241498851482402304149C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+49h]
		#mov     [ecx+48h], dl
		#and     al, 2
		#xor     [ecx+49h], al
		#retn    8


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_74(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_74
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_70(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_70
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_76(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_76
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E46D9F0(self):
		#sub_6E46D9F0
		gadget = "8BC18B4C2404C7400401000000C70014998D6E894808C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax+4], 1
		#mov     dword ptr [eax], offset off_6E8D9914
		#mov     [eax+8], ecx
		#retn    4


  def test_gadget_sub_6E46EC90(self):
		#sub_6E46EC90
		gadget = "8B4C24048B1133C03B152C4EA66E0F94C0C20400"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#xor     eax, eax
		#cmp     edx, dword_6EA64E2C
		#setz    al
		#retn    4


  def test_gadget_sub_6E47BC80(self):
		#sub_6E47BC80
		gadget = "8D4124C3"
		self.do(gadget)

		#lea     eax, [ecx+24h]
		#retn


  def test_gadget_sub_6E47BC90(self):
		#sub_6E47BC90
		gadget = "8B4424048A108A44240802C03241258851242402304125C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+25h]
		#mov     [ecx+24h], dl
		#and     al, 2
		#xor     [ecx+25h], al
		#retn    8


  def test_gadget_sub_6E484B30(self):
		#sub_6E484B30
		gadget = "8B4424048B1089517C8A5424088B400402D232918400000089818000000080E202309184000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+7Ch], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+84h]
		#mov     [ecx+80h], eax
		#and     dl, 2
		#xor     [ecx+84h], dl
		#retn    8


  def test_gadget_sub_6E484B60(self):
		#sub_6E484B60
		gadget = "8B4424048B108991880000008A5424088B400402D232919000000089818C00000080E202309190000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+88h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+90h]
		#mov     [ecx+8Ch], eax
		#and     dl, 2
		#xor     [ecx+90h], dl
		#retn    8


  def test_gadget_sub_6E486A70(self):
		#sub_6E486A70
		gadget = "8B4424048A108A44240802C03241658851642402304165C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+65h]
		#mov     [ecx+64h], dl
		#and     al, 2
		#xor     [ecx+65h], al
		#retn    8


  def test_gadget_sub_6E486E00(self):
		#sub_6E486E00
		gadget = "B8B8EA8D6EC3"
		self.do(gadget)

		#mov     eax, offset aRendersvgres_6; "RenderSVGResourceFilterPrimitive"
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_74(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_74
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E48BCE0(self):
		#sub_6E48BCE0
		gadget = "8B4424048A108A44240802C03241058851042402304105C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+5]
		#mov     [ecx+4], dl
		#and     al, 2
		#xor     [ecx+5], al
		#retn    8


  def test_gadget_sub_6E48F7D0(self):
		#sub_6E48F7D0
		gadget = "8D8180000000C3"
		self.do(gadget)

		#lea     eax, [ecx+80h]
		#retn


  def test_gadget_sub_6E48F7E0(self):
		#sub_6E48F7E0
		gadget = "8B4424048A108A44240802C03281810000008891800000002402308181000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+81h]
		#mov     [ecx+80h], dl
		#and     al, 2
		#xor     [ecx+81h], al
		#retn    8


  def test_gadget_sub_6E4908B0(self):
		#sub_6E4908B0
		gadget = "D9442404D9595CC20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+5Ch]
		#retn    8


  def test_gadget_sub_6E4908C0(self):
		#sub_6E4908C0
		gadget = "D9442404D95960C20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+60h]
		#retn    8


  def test_gadget_sub_6E4908D0(self):
		#sub_6E4908D0
		gadget = "D9442404D95964C20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+64h]
		#retn    8


  def test_gadget_sub_6E4908E0(self):
		#sub_6E4908E0
		gadget = "D9442404D95968C20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#fstp    dword ptr [ecx+68h]
		#retn    8


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_77(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_77
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_75(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_75
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E491E90(self):
		#sub_6E491E90
		gadget = "8D412CC3"
		self.do(gadget)

		#lea     eax, [ecx+2Ch]
		#retn


  def test_gadget_sub_6E491EA0(self):
		#sub_6E491EA0
		gadget = "8B4424048A108A44240802C032412D88512C240230412DC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+2Dh]
		#mov     [ecx+2Ch], dl
		#and     al, 2
		#xor     [ecx+2Dh], al
		#retn    8


  def test_gadget_sub_6E4924A0(self):
		#sub_6E4924A0
		gadget = "8B4424048B108991D40000008A5424088B400402D23291DC0000008981D800000080E2023091DC000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0D4h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0DCh]
		#mov     [ecx+0D8h], eax
		#and     dl, 2
		#xor     [ecx+0DCh], dl
		#retn    8


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_78(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_78
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_71(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_71
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E494560(self):
		#sub_6E494560
		gadget = "8BC18B4C2404D901D9188B4904894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#fld     dword ptr [ecx]
		#fstp    dword ptr [eax]
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E4945F0(self):
		#sub_6E4945F0
		gadget = "8B410483E00FC3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#and     eax, 0Fh
		#retn


  def test_gadget_sub_6E494600(self):
		#sub_6E494600
		gadget = "8B4104C1E804C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#shr     eax, 4
		#retn


  def test_gadget_sub_6E4956D0(self):
		#sub_6E4956D0
		gadget = "D9EE8BC18B4C2404D95004D950088908D9500CD95810C20400"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#fst     dword ptr [eax+4]
		#fst     dword ptr [eax+8]
		#mov     [eax], ecx
		#fst     dword ptr [eax+0Ch]
		#fstp    dword ptr [eax+10h]
		#retn    4


  def test_gadget_sub_6E496480(self):
		#sub_6E496480
		gadget = "8B4424048B108991A80000008A5424088B400402D23291B00000008981AC00000080E2023091B0000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0A8h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0B0h]
		#mov     [ecx+0ACh], eax
		#and     dl, 2
		#xor     [ecx+0B0h], dl
		#retn    8


  def test_gadget_sub_6E498940(self):
		#sub_6E498940
		gadget = "8D4178C3"
		self.do(gadget)

		#lea     eax, [ecx+78h]
		#retn


  def test_gadget_sub_6E498950(self):
		#sub_6E498950
		gadget = "8B4424048A108A44240802C03241798851782402304179C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+79h]
		#mov     [ecx+78h], dl
		#and     al, 2
		#xor     [ecx+79h], al
		#retn    8


  def test_gadget_sub_6E498F30(self):
		#sub_6E498F30
		gadget = "8B4424048B108991800000008A5424088B400402D232918800000089818400000080E202309188000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+80h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+88h]
		#mov     [ecx+84h], eax
		#and     dl, 2
		#xor     [ecx+88h], dl
		#retn    8


  def test_gadget_sub_6E498F60(self):
		#sub_6E498F60
		gadget = "8B4424048B108991940000008A5424088B400402D232919C00000089819800000080E20230919C000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+94h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+9Ch]
		#mov     [ecx+98h], eax
		#and     dl, 2
		#xor     [ecx+9Ch], dl
		#retn    8


  def test_gadget_sub_6E49B5A0(self):
		#sub_6E49B5A0
		gadget = "8B4424048B108991CC0000008A5424088B400402D23291D40000008981D000000080E2023091D4000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0CCh], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0D4h]
		#mov     [ecx+0D0h], eax
		#and     dl, 2
		#xor     [ecx+0D4h], dl
		#retn    8


  def test_gadget_sub_6E49DBA0(self):
		#sub_6E49DBA0
		gadget = "8B442414C70007000000C21400"
		self.do(gadget)

		#mov     eax, [esp+arg_10]
		#mov     dword ptr [eax], 7
		#retn    14h


  def test_gadget_sub_6E4A0110(self):
		#sub_6E4A0110
		gadget = "D9EE8BC133C98908894804894808D9500CD95010D95014D95018894828D9582488482CC3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#fst     dword ptr [eax+0Ch]
		#fst     dword ptr [eax+10h]
		#fst     dword ptr [eax+14h]
		#fst     dword ptr [eax+18h]
		#mov     [eax+28h], ecx
		#fstp    dword ptr [eax+24h]
		#mov     [eax+2Ch], cl
		#retn


  def test_gadget_sub_6E4A1300(self):
		#sub_6E4A1300
		gadget = "D9EE8BC1D95008C700D0258E6ED9580CC7400400000000C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fst     dword ptr [eax+8]
		#mov     dword ptr [eax], offset off_6E8E25D0
		#fstp    dword ptr [eax+0Ch]
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_0DNameNodeIAEXZ_0(self):
		#0DNameNodeIAEXZ_0
		gadget = "8BC1C7000C268E6EC7400400000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_6E8E260C
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_6E4A19F0(self):
		#sub_6E4A19F0
		gadget = "8B41043B41081BC0F7D8C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#cmp     eax, [ecx+8]
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_6E4A1A00(self):
		#sub_6E4A1A00
		gadget = "83EC088B41040FB610408941048814240FB61040894104885424010FB61040894104885424020FB61040894104885424030FB610D9042440894104885424040FB61040894104885424050FB61040894104885424060FB610408941048B44240C88542407D918D9442404D9580483C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx+4]
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_8], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_8+1], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_8+2], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_8+3], dl
		#movzx   edx, byte ptr [eax]
		#fld     [esp+8+var_8]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_4], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_4+1], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+8+var_4+2], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     eax, [esp+8+arg_0]
		#mov     byte ptr [esp+8+var_4+3], dl
		#fstp    dword ptr [eax]
		#fld     [esp+8+var_4]
		#fstp    dword ptr [eax+4]
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6E4A1A80(self):
		#sub_6E4A1A80
		gadget = "518B41040FB610408941048814240FB610408941048B4C2408885424010FB704248901B00159C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [ecx+4]
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+4+var_4], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     ecx, [esp+4+arg_0]
		#mov     byte ptr [esp+4+var_4+1], dl
		#movzx   eax, [esp+4+var_4]
		#mov     [ecx], eax
		#mov     al, 1
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E4A1AB0(self):
		#sub_6E4A1AB0
		gadget = "518B41040FB610408941048814240FB61040885424018941040FB7042459C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [ecx+4]
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+4+var_4], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     byte ptr [esp+4+var_4+1], dl
		#mov     [ecx+4], eax
		#movzx   eax, [esp+4+var_4]
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E4A1B10(self):
		#sub_6E4A1B10
		gadget = "518B41040FB610408941048814240FB61040894104885424010FB61040894104885424020FB610408941048B44240888542403D90424D918B00159C20400"
		self.do(gadget)

		#push    ecx
		#mov     eax, [ecx+4]
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+4+var_4], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+4+var_4+1], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     byte ptr [esp+4+var_4+2], dl
		#movzx   edx, byte ptr [eax]
		#inc     eax
		#mov     [ecx+4], eax
		#mov     eax, [esp+4+arg_0]
		#mov     byte ptr [esp+4+var_4+3], dl
		#fld     [esp+4+var_4]
		#fstp    dword ptr [eax]
		#mov     al, 1
		#pop     ecx
		#retn    4


  def test_gadget_sub_6E4A1CF0(self):
		#sub_6E4A1CF0
		gadget = "8BC18B4C2404C70084268E6E8B118950048B51080311895008C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E8E2684
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#add     edx, [ecx]
		#mov     [eax+8], edx
		#retn    4


  def test_gadget_sub_6E4A20D0(self):
		#sub_6E4A20D0
		gadget = "B806000000C3"
		self.do(gadget)

		#mov     eax, 6
		#retn


  def test_gadget_sub_6E4A2170(self):
		#sub_6E4A2170
		gadget = "B811000000C3"
		self.do(gadget)

		#mov     eax, 11h
		#retn


  def test_gadget_sub_6E4A2210(self):
		#sub_6E4A2210
		gadget = "B812000000C3"
		self.do(gadget)

		#mov     eax, 12h
		#retn


  def test_gadget___RTC_NumErrors_22(self):
		#__RTC_NumErrors_22
		gadget = "B805000000C3"
		self.do(gadget)

		#mov     eax, 5
		#retn


  def test_gadget_sub_6E4A22F0(self):
		#sub_6E4A22F0
		gadget = "B80C000000C3"
		self.do(gadget)

		#mov     eax, 0Ch
		#retn


  def test_gadget_sub_6E4A2330(self):
		#sub_6E4A2330
		gadget = "B80D000000C3"
		self.do(gadget)

		#mov     eax, 0Dh
		#retn


  def test_gadget_sub_6E4A2370(self):
		#sub_6E4A2370
		gadget = "B80E000000C3"
		self.do(gadget)

		#mov     eax, 0Eh
		#retn


  def test_gadget_sub_6E4A23B0(self):
		#sub_6E4A23B0
		gadget = "B80F000000C3"
		self.do(gadget)

		#mov     eax, 0Fh
		#retn


  def test_gadget_sub_6E4A54A0(self):
		#sub_6E4A54A0
		gadget = "D9EE8BC1D95018C7400400000000D9501CD95020D95024D95028D9582CC3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fst     dword ptr [eax+18h]
		#mov     dword ptr [eax+4], 0
		#fst     dword ptr [eax+1Ch]
		#fst     dword ptr [eax+20h]
		#fst     dword ptr [eax+24h]
		#fst     dword ptr [eax+28h]
		#fstp    dword ptr [eax+2Ch]
		#retn


  def test_gadget_sub_6E4A6790(self):
		#sub_6E4A6790
		gadget = "8BC133C9C700442C8E6E894804894808C7400C02000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8E2C44
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     dword ptr [eax+0Ch], 2
		#retn


  def test_gadget_sub_6E4A67B0(self):
		#sub_6E4A67B0
		gadget = "33C0894104894108C7410C02000000C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [ecx+4], eax
		#mov     [ecx+8], eax
		#mov     dword ptr [ecx+0Ch], 2
		#retn


  def test_gadget_sub_6E4A76A0(self):
		#sub_6E4A76A0
		gadget = "8B410C33D23B41100F9CC0C3"
		self.do(gadget)

		#mov     eax, [ecx+0Ch]
		#xor     edx, edx
		#cmp     eax, [ecx+10h]
		#setl    al
		#retn


  def test_gadget_sub_6E4A76B0(self):
		#sub_6E4A76B0
		gadget = "83EC088B4108D94010D91C248B0C24D940148B44240CD95C24048B5424048908895004B00183C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx+8]
		#fld     dword ptr [eax+10h]
		#fstp    [esp+8+var_8]
		#mov     ecx, [esp+8+var_8]
		#fld     dword ptr [eax+14h]
		#mov     eax, [esp+8+arg_0]
		#fstp    [esp+8+var_4]
		#mov     edx, [esp+8+var_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     al, 1
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6E4A76E0(self):
		#sub_6E4A76E0
		gadget = "8B4108D940108B4C2404D919B001C20400"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#fld     dword ptr [eax+10h]
		#mov     ecx, [esp+arg_0]
		#fstp    dword ptr [ecx]
		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E4A7700(self):
		#sub_6E4A7700
		gadget = "83EC088B4108D940188B4C240CD91C248B1424D9401C8911D95C24048B542404895104D940208B4C2410D91C24D940248B14248911D95C24048B542404895104D94010D91C248B0C24D940148B442414D95C24048B5424048908895004B00183C408C20C00"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx+8]
		#fld     dword ptr [eax+18h]
		#mov     ecx, [esp+8+arg_0]
		#fstp    [esp+8+var_8]
		#mov     edx, [esp+8+var_8]
		#fld     dword ptr [eax+1Ch]
		#mov     [ecx], edx
		#fstp    [esp+8+var_4]
		#mov     edx, [esp+8+var_4]
		#mov     [ecx+4], edx
		#fld     dword ptr [eax+20h]
		#mov     ecx, [esp+8+arg_4]
		#fstp    [esp+8+var_8]
		#fld     dword ptr [eax+24h]
		#mov     edx, [esp+8+var_8]
		#mov     [ecx], edx
		#fstp    [esp+8+var_4]
		#mov     edx, [esp+8+var_4]
		#mov     [ecx+4], edx
		#fld     dword ptr [eax+10h]
		#fstp    [esp+8+var_8]
		#mov     ecx, [esp+8+var_8]
		#fld     dword ptr [eax+14h]
		#mov     eax, [esp+8+arg_8]
		#fstp    [esp+8+var_4]
		#mov     edx, [esp+8+var_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     al, 1
		#add     esp, 8
		#retn    0Ch


  def test_gadget_sub_6E4A7770(self):
		#sub_6E4A7770
		gadget = "83EC088B4108D940188B4C240CD91C248B1424D9401C8911D95C24048B542404895104D94010D91C248B0C24D940148B442410D95C24048B5424048908895004B00183C408C20800"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx+8]
		#fld     dword ptr [eax+18h]
		#mov     ecx, [esp+8+arg_0]
		#fstp    [esp+8+var_8]
		#mov     edx, [esp+8+var_8]
		#fld     dword ptr [eax+1Ch]
		#mov     [ecx], edx
		#fstp    [esp+8+var_4]
		#mov     edx, [esp+8+var_4]
		#mov     [ecx+4], edx
		#fld     dword ptr [eax+10h]
		#fstp    [esp+8+var_8]
		#mov     ecx, [esp+8+var_8]
		#fld     dword ptr [eax+14h]
		#mov     eax, [esp+8+arg_4]
		#fstp    [esp+8+var_4]
		#mov     edx, [esp+8+var_4]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     al, 1
		#add     esp, 8
		#retn    8


  def test_gadget_sub_6E4A77C0(self):
		#sub_6E4A77C0
		gadget = "83EC088B4108D940188B4C240C8B542410D919D9401C8B4C2414D91AD94020D9190FB650248B4C241880E20188110FB650248B4C241CD0EA80E2018811D94010D91C248B1424D940148B442420D95C24048B4C24048910894804B00183C408C21800"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx+8]
		#fld     dword ptr [eax+18h]
		#mov     ecx, [esp+8+arg_0]
		#mov     edx, [esp+8+arg_4]
		#fstp    dword ptr [ecx]
		#fld     dword ptr [eax+1Ch]
		#mov     ecx, [esp+8+arg_8]
		#fstp    dword ptr [edx]
		#fld     dword ptr [eax+20h]
		#fstp    dword ptr [ecx]
		#movzx   edx, byte ptr [eax+24h]
		#mov     ecx, [esp+8+arg_C]
		#and     dl, 1
		#mov     [ecx], dl
		#movzx   edx, byte ptr [eax+24h]
		#mov     ecx, [esp+8+arg_10]
		#shr     dl, 1
		#and     dl, 1
		#mov     [ecx], dl
		#fld     dword ptr [eax+10h]
		#fstp    [esp+8+var_8]
		#mov     edx, [esp+8+var_8]
		#fld     dword ptr [eax+14h]
		#mov     eax, [esp+8+arg_14]
		#fstp    [esp+8+var_4]
		#mov     ecx, [esp+8+var_4]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#mov     al, 1
		#add     esp, 8
		#retn    18h


  def test_gadget_sub_6E4A7830(self):
		#sub_6E4A7830
		gadget = "8BC18B4C240489480433C9C700802C8E6E8948088B500489480C8B4A08894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_6E8E2C80
		#mov     [eax+8], ecx
		#mov     edx, [eax+4]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [edx+8]
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_0DNameNodeIAEXZ_1(self):
		#0DNameNodeIAEXZ_1
		gadget = "8BC1C700442D8E6EC7400400000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_6E8E2D44
		#mov     dword ptr [eax+4], 0
		#retn


  def test_gadget_nullsub_8(self):
		#nullsub_8
		gadget = "C21C00"
		self.do(gadget)

		#retn    1Ch


  def test_gadget_sub_6E4AE3C0(self):
		#sub_6E4AE3C0
		gadget = "8B4104D9442404D95830C20400"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#fld     [esp+arg_0]
		#fstp    dword ptr [eax+30h]
		#retn    4


  def test_gadget_sub_6E4AE3F0(self):
		#sub_6E4AE3F0
		gadget = "8B4104FF402CC3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#inc     dword ptr [eax+2Ch]
		#retn


  def test_gadget_sub_6E4AE400(self):
		#sub_6E4AE400
		gadget = "8B41048B402CC3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     eax, [eax+2Ch]
		#retn


  def test_gadget_sub_6E4AE410(self):
		#sub_6E4AE410
		gadget = "8B4104D94028C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#fld     dword ptr [eax+28h]
		#retn


  def test_gadget_sub_6E4AE420(self):
		#sub_6E4AE420
		gadget = "8B49048B51088B4424048B490C8910894804C20400"
		self.do(gadget)

		#mov     ecx, [ecx+4]
		#mov     edx, [ecx+8]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E4AFB30(self):
		#sub_6E4AFB30
		gadget = "8B4424048B1089919C0000008A5424088B400402D23291A40000008981A000000080E2023091A4000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+9Ch], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0A4h]
		#mov     [ecx+0A0h], eax
		#and     dl, 2
		#xor     [ecx+0A4h], dl
		#retn    8


  def test_gadget_sub_6E4AFB60(self):
		#sub_6E4AFB60
		gadget = "8B4424048B108991B40000008A5424088B400402D23291BC0000008981B800000080E2023091BC000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0B4h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0BCh]
		#mov     [ecx+0B8h], eax
		#and     dl, 2
		#xor     [ecx+0BCh], dl
		#retn    8


  def test_gadget_sub_6E4B17B0(self):
		#sub_6E4B17B0
		gadget = "8D81A0000000C3"
		self.do(gadget)

		#lea     eax, [ecx+0A0h]
		#retn


  def test_gadget_sub_6E4B17C0(self):
		#sub_6E4B17C0
		gadget = "8B4424048A108A44240802C03281A10000008891A000000024023081A1000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+0A1h]
		#mov     [ecx+0A0h], dl
		#and     al, 2
		#xor     [ecx+0A1h], al
		#retn    8


  def test_gadget_sub_6E4B3F70(self):
		#sub_6E4B3F70
		gadget = "8BC1C70006000000C7400401000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 6
		#mov     dword ptr [eax+4], 1
		#retn


  def test_gadget_sub_6E4B4B00(self):
		#sub_6E4B4B00
		gadget = "8B4424048B108991C00000008A5424088B400402D23291C80000008981C400000080E2023091C8000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0C0h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0C8h]
		#mov     [ecx+0C4h], eax
		#and     dl, 2
		#xor     [ecx+0C8h], dl
		#retn    8


  def test_gadget_sub_6E4B6700(self):
		#sub_6E4B6700
		gadget = "8B4424048B108991D00000008A5424088B400402D23291D80000008981D400000080E2023091D8000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0D0h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0D8h]
		#mov     [ecx+0D4h], eax
		#and     dl, 2
		#xor     [ecx+0D8h], dl
		#retn    8


  def test_gadget_sub_6E4B6730(self):
		#sub_6E4B6730
		gadget = "8B4424048B108991DC0000008A5424088B400402D23291E40000008981E000000080E2023091E4000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0DCh], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0E4h]
		#mov     [ecx+0E0h], eax
		#and     dl, 2
		#xor     [ecx+0E4h], dl
		#retn    8


  def test_gadget_sub_6E4B6760(self):
		#sub_6E4B6760
		gadget = "8B4424048B108991F40000008A5424088B400402D23291FC0000008981F800000080E2023091FC000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0F4h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0FCh]
		#mov     [ecx+0F8h], eax
		#and     dl, 2
		#xor     [ecx+0FCh], dl
		#retn    8


  def test_gadget_sub_6E4B7C60(self):
		#sub_6E4B7C60
		gadget = "8D8190000000C3"
		self.do(gadget)

		#lea     eax, [ecx+90h]
		#retn


  def test_gadget_sub_6E4B7C70(self):
		#sub_6E4B7C70
		gadget = "8B4424048A108A44240802C03281910000008891900000002402308191000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+91h]
		#mov     [ecx+90h], dl
		#and     al, 2
		#xor     [ecx+91h], al
		#retn    8


  def test_gadget_sub_6E4B7F80(self):
		#sub_6E4B7F80
		gadget = "8B4424048B108991C80000008A5424088B400402D23291D00000008981CC00000080E2023091D0000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0C8h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0D0h]
		#mov     [ecx+0CCh], eax
		#and     dl, 2
		#xor     [ecx+0D0h], dl
		#retn    8


  def test_gadget_sub_6E4B7FB0(self):
		#sub_6E4B7FB0
		gadget = "8B4424048B108991E00000008A5424088B400402D23291E80000008981E400000080E2023091E8000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0E0h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0E8h]
		#mov     [ecx+0E4h], eax
		#and     dl, 2
		#xor     [ecx+0E8h], dl
		#retn    8


  def test_gadget_sub_6E4B8020(self):
		#sub_6E4B8020
		gadget = "D90528408E6EC3"
		self.do(gadget)

		#fld     ds:flt_6E8E4028
		#retn


  def test_gadget_sub_6E4B8040(self):
		#sub_6E4B8040
		gadget = "D9EE8B442404D910D95804C3"
		self.do(gadget)

		#fldz
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fstp    dword ptr [eax+4]
		#retn


  def test_gadget_sub_6E4B8060(self):
		#sub_6E4B8060
		gadget = "D9EE8B442404D910D95004D95008D9580CC3"
		self.do(gadget)

		#fldz
		#mov     eax, [esp+arg_0]
		#fst     dword ptr [eax]
		#fst     dword ptr [eax+4]
		#fst     dword ptr [eax+8]
		#fstp    dword ptr [eax+0Ch]
		#retn


  def test_gadget_sub_6E4B9B20(self):
		#sub_6E4B9B20
		gadget = "8D417CC3"
		self.do(gadget)

		#lea     eax, [ecx+7Ch]
		#retn


  def test_gadget_sub_6E4B9B30(self):
		#sub_6E4B9B30
		gadget = "8B4424048A108A44240802C032417D88517C240230417DC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+7Dh]
		#mov     [ecx+7Ch], dl
		#and     al, 2
		#xor     [ecx+7Dh], al
		#retn    8


  def test_gadget_sub_6E4BC0A0(self):
		#sub_6E4BC0A0
		gadget = "8A44240402C002C002C03241142408304114C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#add     al, al
		#add     al, al
		#add     al, al
		#xor     al, [ecx+14h]
		#and     al, 8
		#xor     [ecx+14h], al
		#retn    4


  def test_gadget_sub_6E4BC0C0(self):
		#sub_6E4BC0C0
		gadget = "8A41142401C3"
		self.do(gadget)

		#mov     al, [ecx+14h]
		#and     al, 1
		#retn


  def test_gadget_sub_6E4BC0D0(self):
		#sub_6E4BC0D0
		gadget = "8A4114C0E8032401C3"
		self.do(gadget)

		#mov     al, [ecx+14h]
		#shr     al, 3
		#and     al, 1
		#retn


  def test_gadget_sub_6E4BC0E0(self):
		#sub_6E4BC0E0
		gadget = "8D4168C3"
		self.do(gadget)

		#lea     eax, [ecx+68h]
		#retn


  def test_gadget_sub_6E4BC0F0(self):
		#sub_6E4BC0F0
		gadget = "8B4424048A108A44240802C03241298851282402304129C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+29h]
		#mov     [ecx+28h], dl
		#and     al, 2
		#xor     [ecx+29h], al
		#retn    8


  def test_gadget_sub_6E4C1350(self):
		#sub_6E4C1350
		gadget = "8B4424048A108A44240802C032410D88510C240230410DC20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+0Dh]
		#mov     [ecx+0Ch], dl
		#and     al, 2
		#xor     [ecx+0Dh], al
		#retn    8


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_76(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_76
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_sub_6E4C1460(self):
		#sub_6E4C1460
		gadget = "8B4424048B088B410CC1E81A2401C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax]
		#mov     eax, [ecx+0Ch]
		#shr     eax, 1Ah
		#and     al, 1
		#retn    4


  def test_gadget_sub_6E4C2820(self):
		#sub_6E4C2820
		gadget = "8BC180481001C3"
		self.do(gadget)

		#mov     eax, ecx
		#or      byte ptr [eax+10h], 1
		#retn


  def test_gadget_sub_6E4C2830(self):
		#sub_6E4C2830
		gadget = "804924018D4114C3"
		self.do(gadget)

		#or      byte ptr [ecx+24h], 1
		#lea     eax, [ecx+14h]
		#retn


  def test_gadget_sub_6E4C2840(self):
		#sub_6E4C2840
		gadget = "804938018D4128C3"
		self.do(gadget)

		#or      byte ptr [ecx+38h], 1
		#lea     eax, [ecx+28h]
		#retn


  def test_gadget_sub_6E4C2F30(self):
		#sub_6E4C2F30
		gadget = "8BC133C98908894804894808C7400CF04FA66EB2FC20501020502489481489481889481CC74020EC4FA66E20503889482889482C894830C740347450A66EC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     dword ptr [eax+0Ch], offset dword_6EA64FF0
		#mov     dl, 0FCh
		#and     [eax+10h], dl
		#and     [eax+24h], dl
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     dword ptr [eax+20h], offset dword_6EA64FEC
		#and     [eax+38h], dl
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     dword ptr [eax+34h], offset dword_6EA65074
		#retn


  def test_gadget_sub_6E4C7EC0(self):
		#sub_6E4C7EC0
		gadget = "D9EE8BC156D950048B74240857C70001000000D950088D7810D9580CB90C000000F3A55F5EC20400"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#push    esi
		#fst     dword ptr [eax+4]
		#mov     esi, [esp+4+arg_0]
		#push    edi
		#mov     dword ptr [eax], 1
		#fst     dword ptr [eax+8]
		#lea     edi, [eax+10h]
		#fstp    dword ptr [eax+0Ch]
		#mov     ecx, 0Ch
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E4C7EF0(self):
		#sub_6E4C7EF0
		gadget = "D9EE568B742408D9590457C701010000008D7910B90C000000F3A55F5EC20400"
		self.do(gadget)

		#fldz
		#push    esi
		#mov     esi, [esp+4+arg_0]
		#fstp    dword ptr [ecx+4]
		#push    edi
		#mov     dword ptr [ecx], 1
		#lea     edi, [ecx+10h]
		#mov     ecx, 0Ch
		#rep movsd
		#pop     edi
		#pop     esi
		#retn    4


  def test_gadget_sub_6E4C7F10(self):
		#sub_6E4C7F10
		gadget = "D9EEC70101000000D95904C3"
		self.do(gadget)

		#fldz
		#mov     dword ptr [ecx], 1
		#fstp    dword ptr [ecx+4]
		#retn


  def test_gadget_sub_6E4CD880(self):
		#sub_6E4CD880
		gadget = "8B41F8C741F43C548E6E8B5004C7440AF81C548E6E8B41F88B40048D50F8895408F4C3"
		self.do(gadget)

		#mov     eax, [ecx-8]
		#mov     dword ptr [ecx-0Ch], offset off_6E8E543C
		#mov     edx, [eax+4]
		#mov     dword ptr [edx+ecx-8], offset off_6E8E541C
		#mov     eax, [ecx-8]
		#mov     eax, [eax+4]
		#lea     edx, [eax-8]
		#mov     [eax+ecx-0Ch], edx
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_72(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_72
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E4CE960(self):
		#sub_6E4CE960
		gadget = "8B4424048B108991E40000008A5424088B400402D23291EC0000008981E800000080E2023091EC000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx+0E4h], edx
		#mov     dl, [esp+arg_4]
		#mov     eax, [eax+4]
		#add     dl, dl
		#xor     dl, [ecx+0ECh]
		#mov     [ecx+0E8h], eax
		#and     dl, 2
		#xor     [ecx+0ECh], dl
		#retn    8


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_81(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_81
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E4CF740(self):
		#sub_6E4CF740
		gadget = "8B4424048A108A44240802C03281890000008891880000002402308189000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+89h]
		#mov     [ecx+88h], dl
		#and     al, 2
		#xor     [ecx+89h], al
		#retn    8


  def test_gadget_sub_6E4CF7A0(self):
		#sub_6E4CF7A0
		gadget = "8A44240488818B000000C20400"
		self.do(gadget)

		#mov     al, [esp+arg_0]
		#mov     [ecx+8Bh], al
		#retn    4


  def test_gadget_sub_6E4CF7B0(self):
		#sub_6E4CF7B0
		gadget = "8A818A000000C3"
		self.do(gadget)

		#mov     al, [ecx+8Ah]
		#retn


  def test_gadget_sub_6E4CF7C0(self):
		#sub_6E4CF7C0
		gadget = "8A818B000000C3"
		self.do(gadget)

		#mov     al, [ecx+8Bh]
		#retn


  def test_gadget_sub_6E4CF7D0(self):
		#sub_6E4CF7D0
		gadget = "8D8108010000C3"
		self.do(gadget)

		#lea     eax, [ecx+108h]
		#retn


  def test_gadget_sub_6E4D3010(self):
		#sub_6E4D3010
		gadget = "8D4105C3"
		self.do(gadget)

		#lea     eax, [ecx+5]
		#retn


  def test_gadget_sub_6E4D3020(self):
		#sub_6E4D3020
		gadget = "8B4424048A108A44240802C03241068851052402304106C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dl, [eax]
		#mov     al, [esp+arg_4]
		#add     al, al
		#xor     al, [ecx+6]
		#mov     [ecx+5], dl
		#and     al, 2
		#xor     [ecx+6], al
		#retn    8


  def test_gadget_sub_6E4D31D0(self):
		#sub_6E4D31D0
		gadget = "8B442408C70007000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], 7
		#retn    8


  def test_gadget_sub_6E4D4180(self):
		#sub_6E4D4180
		gadget = "8B4C24048B1133C03B153851A66E0F94C0C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#xor     eax, eax
		#cmp     edx, dword_6EA65138
		#setz    al
		#retn


  def test_gadget_sub_6E4D4260(self):
		#sub_6E4D4260
		gadget = "D94144C3"
		self.do(gadget)

		#fld     dword ptr [ecx+44h]
		#retn


  def test_gadget_sub_6E4D4270(self):
		#sub_6E4D4270
		gadget = "8B51608B4424048B49648910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+60h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+64h]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E4D4290(self):
		#sub_6E4D4290
		gadget = "D94140C3"
		self.do(gadget)

		#fld     dword ptr [ecx+40h]
		#retn


  def test_gadget_sub_6E4D42A0(self):
		#sub_6E4D42A0
		gadget = "8B51588B4424048B495C8910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+58h]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+5Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E4D4340(self):
		#sub_6E4D4340
		gadget = "8B442404C74004FEFFFFFFC70000000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFEh
		#mov     dword ptr [eax], 0
		#retn    8


  def test_gadget_sub_6E4D49B0(self):
		#sub_6E4D49B0
		gadget = "518B44240833C9894804890C24C70060E6846E89480859C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [esp+4+var_4], ecx
		#mov     dword ptr [eax], offset off_6E84E660
		#mov     [eax+8], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E4D4DC0(self):
		#sub_6E4D4DC0
		gadget = "8BC18B4C2404C700010000008B118950088B510489500C8B51088950108B490C8B5424088948148B4C240C89501889481C8B4C24108B118950208B4904894824C6402801C21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], 1
		#mov     edx, [ecx]
		#mov     [eax+8], edx
		#mov     edx, [ecx+4]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+8]
		#mov     [eax+10h], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+14h], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+18h], edx
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_C]
		#mov     edx, [ecx]
		#mov     [eax+20h], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+24h], ecx
		#mov     byte ptr [eax+28h], 1
		#retn    10h


  def test_gadget_sub_6E4D56A0(self):
		#sub_6E4D56A0
		gadget = "8B44240483C00783E0F8C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     eax, 7
		#and     eax, 0FFFFFFF8h
		#retn


  def test_gadget_sub_6E4D6830(self):
		#sub_6E4D6830
		gadget = "0FB6010FB65101C1E0080BC20FB651020FB64903C1E0080BC2C1E0080BC1C3"
		self.do(gadget)

		#movzx   eax, byte ptr [ecx]
		#movzx   edx, byte ptr [ecx+1]
		#shl     eax, 8
		#or      eax, edx
		#movzx   edx, byte ptr [ecx+2]
		#movzx   ecx, byte ptr [ecx+3]
		#shl     eax, 8
		#or      eax, edx
		#shl     eax, 8
		#or      eax, ecx
		#retn


  def test_gadget_sub_6E4D82C0(self):
		#sub_6E4D82C0
		gadget = "8B4424048B4024C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+24h]
		#retn


  def test_gadget_sub_6E4D91F0(self):
		#sub_6E4D91F0
		gadget = "518B4E100FB641640FB65165C1E0080BC20FB651660FB64967C1E0080BC2C1E0080BC18B4E0440538BD8C1EB10885919895C24048BD0C1EA1888511888411B8BD8C1EB0888591A8B4E0488515C8A54240488595E88515D88415F8B4604C74060002DE2285B59C3"
		self.do(gadget)

		#push    ecx
		#mov     ecx, [esi+10h]
		#movzx   eax, byte ptr [ecx+64h]
		#movzx   edx, byte ptr [ecx+65h]
		#shl     eax, 8
		#or      eax, edx
		#movzx   edx, byte ptr [ecx+66h]
		#movzx   ecx, byte ptr [ecx+67h]
		#shl     eax, 8
		#or      eax, edx
		#shl     eax, 8
		#or      eax, ecx
		#mov     ecx, [esi+4]
		#inc     eax
		#push    ebx
		#mov     ebx, eax
		#shr     ebx, 10h
		#mov     [ecx+19h], bl
		#mov     [esp+8+var_4], ebx
		#mov     edx, eax
		#shr     edx, 18h
		#mov     [ecx+18h], dl
		#mov     [ecx+1Bh], al
		#mov     ebx, eax
		#shr     ebx, 8
		#mov     [ecx+1Ah], bl
		#mov     ecx, [esi+4]
		#mov     [ecx+5Ch], dl
		#mov     dl, byte ptr [esp+8+var_4]
		#mov     [ecx+5Eh], bl
		#mov     [ecx+5Dh], dl
		#mov     [ecx+5Fh], al
		#mov     eax, [esi+4]
		#mov     dword ptr [eax+60h], 28E22D00h
		#pop     ebx
		#pop     ecx
		#retn


  def test_gadget_sub_6E4DA780(self):
		#sub_6E4DA780
		gadget = "8B41048B098948048B500C8B42388B4C24040FB65488248D4488240FB64801C1E2080BD10FB648020FB64003C1E2080BD18B4C2408C1E2080BD08911C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     ecx, [ecx]
		#mov     [eax+4], ecx
		#mov     edx, [eax+0Ch]
		#mov     eax, [edx+38h]
		#mov     ecx, [esp+arg_0]
		#movzx   edx, byte ptr [eax+ecx*4+24h]
		#lea     eax, [eax+ecx*4+24h]
		#movzx   ecx, byte ptr [eax+1]
		#shl     edx, 8
		#or      edx, ecx
		#movzx   ecx, byte ptr [eax+2]
		#movzx   eax, byte ptr [eax+3]
		#shl     edx, 8
		#or      edx, ecx
		#mov     ecx, [esp+arg_4]
		#shl     edx, 8
		#or      edx, eax
		#mov     [ecx], edx
		#retn


  def test_gadget_sub_6E4DB720(self):
		#sub_6E4DB720
		gadget = "8B4424048B50088B4C240889118B400C89410433C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax+8]
		#mov     ecx, [esp+arg_4]
		#mov     [ecx], edx
		#mov     eax, [eax+0Ch]
		#mov     [ecx+4], eax
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4DF170(self):
		#sub_6E4DF170
		gadget = "8B4424048B404CC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+4Ch]
		#retn


  def test_gadget_sub_6E4DF4A0(self):
		#sub_6E4DF4A0
		gadget = "8B4424088B4C2404F7D81BC02500FFFFFF05FF00000089413033C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [esp+arg_0]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 0FFFFFF00h
		#add     eax, 0FFh
		#mov     [ecx+30h], eax
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4E0750(self):
		#sub_6E4E0750
		gadget = "8B4424040FB64006C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#movzx   eax, byte ptr [eax+6]
		#retn


  def test_gadget_sub_6E4E0760(self):
		#sub_6E4E0760
		gadget = "8B4424048B50208B4C240889118B402489410433C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax+20h]
		#mov     ecx, [esp+arg_4]
		#mov     [ecx], edx
		#mov     eax, [eax+24h]
		#mov     [ecx+4], eax
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4E0780(self):
		#sub_6E4E0780
		gadget = "8B442404C740300000000033C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+30h], 0
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4E0CD0(self):
		#sub_6E4E0CD0
		gadget = "8B4424048B4054C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+54h]
		#retn


  def test_gadget_sub_6E4E2EE0(self):
		#sub_6E4E2EE0
		gadget = "8B4424048B48148B44240CFF40048B493001480833C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+14h]
		#mov     eax, [esp+arg_8]
		#inc     dword ptr [eax+4]
		#mov     ecx, [ecx+30h]
		#add     [eax+8], ecx
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4E2FB0(self):
		#sub_6E4E2FB0
		gadget = "8B44240CFF0033C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#inc     dword ptr [eax]
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4E3530(self):
		#sub_6E4E3530
		gadget = "8B4424088B4C240C8B54240403C08914C133C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [esp+arg_8]
		#mov     edx, [esp+arg_0]
		#add     eax, eax
		#mov     [ecx+eax*8], edx
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E4E3550(self):
		#sub_6E4E3550
		gadget = "0FB601990FA4C208C1E008568BF00FB64101578BFA9903F013FA0FB641020FA4F708C1E6089903F00FB6410313FA0FA4F708C1E6089903F00FB6410413FA0FA4F708C1E6089903F00FB6410513FA0FA4F708C1E6089903F00FB6410613FA0FA4F70899C1E60803F00FB6410713FA0FA4F70899C1E60803C613D75F5EC3"
		self.do(gadget)

		#movzx   eax, byte ptr [ecx]
		#cdq
		#shld    edx, eax, 8
		#shl     eax, 8
		#push    esi
		#mov     esi, eax
		#movzx   eax, byte ptr [ecx+1]
		#push    edi
		#mov     edi, edx
		#cdq
		#add     esi, eax
		#adc     edi, edx
		#movzx   eax, byte ptr [ecx+2]
		#shld    edi, esi, 8
		#shl     esi, 8
		#cdq
		#add     esi, eax
		#movzx   eax, byte ptr [ecx+3]
		#adc     edi, edx
		#shld    edi, esi, 8
		#shl     esi, 8
		#cdq
		#add     esi, eax
		#movzx   eax, byte ptr [ecx+4]
		#adc     edi, edx
		#shld    edi, esi, 8
		#shl     esi, 8
		#cdq
		#add     esi, eax
		#movzx   eax, byte ptr [ecx+5]
		#adc     edi, edx
		#shld    edi, esi, 8
		#shl     esi, 8
		#cdq
		#add     esi, eax
		#movzx   eax, byte ptr [ecx+6]
		#adc     edi, edx
		#shld    edi, esi, 8
		#cdq
		#shl     esi, 8
		#add     esi, eax
		#movzx   eax, byte ptr [ecx+7]
		#adc     edi, edx
		#shld    edi, esi, 8
		#cdq
		#shl     esi, 8
		#add     eax, esi
		#adc     edx, edi
		#pop     edi
		#pop     esi
		#retn


  def test_gadget_sub_6E4E35D0(self):
		#sub_6E4E35D0
		gadget = "8B44240853568BD0C1FA1888118BD0C1FA108BF0C1FE1F8851018BD08BF0C1FE1FC1FA088BF0C1FE1F8851028BD08BF0C1FE1F8851038B54240C8BF08BDA0FACF318885904C1FE188BF08BDA0FACF3108859058BDA0FACC308C1FE105EC1F808885906885107B8080000005BC3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#push    ebx
		#push    esi
		#mov     edx, eax
		#sar     edx, 18h
		#mov     [ecx], dl
		#mov     edx, eax
		#sar     edx, 10h
		#mov     esi, eax
		#sar     esi, 1Fh
		#mov     [ecx+1], dl
		#mov     edx, eax
		#mov     esi, eax
		#sar     esi, 1Fh
		#sar     edx, 8
		#mov     esi, eax
		#sar     esi, 1Fh
		#mov     [ecx+2], dl
		#mov     edx, eax
		#mov     esi, eax
		#sar     esi, 1Fh
		#mov     [ecx+3], dl
		#mov     edx, [esp+8+arg_0]
		#mov     esi, eax
		#mov     ebx, edx
		#shrd    ebx, esi, 18h
		#mov     [ecx+4], bl
		#sar     esi, 18h
		#mov     esi, eax
		#mov     ebx, edx
		#shrd    ebx, esi, 10h
		#mov     [ecx+5], bl
		#mov     ebx, edx
		#shrd    ebx, eax, 8
		#sar     esi, 10h
		#pop     esi
		#sar     eax, 8
		#mov     [ecx+6], bl
		#mov     [ecx+7], dl
		#mov     eax, 8
		#pop     ebx
		#retn


  def test_gadget_sub_6E4E38E0(self):
		#sub_6E4E38E0
		gadget = "8B4C240433C03941040F94C0C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#xor     eax, eax        ; Microsoft VisualC 2-11/net runtime
		#cmp     [ecx+4], eax
		#setz    al
		#retn


  def test_gadget_sub_6E4E9570(self):
		#sub_6E4E9570
		gadget = "33C989480489480889480C89481089481489481889481C894820894824C70068958E6EC3"
		self.do(gadget)

		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     dword ptr [eax], offset unk_6E8E9568
		#retn


  def test_gadget_2YAPAXIPAXZ_0(self):
		#2YAPAXIPAXZ_0
		gadget = "8B442408C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#retn


  def test_gadget_sub_6E5989F0(self):
		#sub_6E5989F0
		gadget = "8B4424088B4C24048981A4000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [esp+arg_0]
		#mov     [ecx+0A4h], eax
		#retn


  def test_gadget_sub_6E598F60(self):
		#sub_6E598F60
		gadget = "8B442404010544FEA56EC3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#add     dword_6EA5FE44, eax
		#retn


  def test_gadget_sub_6E599CF0(self):
		#sub_6E599CF0
		gadget = "8B4C24048B81B00000008D50018991B0000000C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     eax, [ecx+0B0h]
		#lea     edx, [eax+1]
		#mov     [ecx+0B0h], edx
		#retn


  def test_gadget_sub_6E59C850(self):
		#sub_6E59C850
		gadget = "A19CA6A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6A69C
		#retn


  def test_gadget_sub_6E5AF9F0(self):
		#sub_6E5AF9F0
		gadget = "8B44240433C98908894804894808C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#retn


  def test_gadget_sub_6E5B8370(self):
		#sub_6E5B8370
		gadget = "C70130A67E6EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E7EA630
		#retn


  def test_gadget_sub_6E5B9270(self):
		#sub_6E5B9270
		gadget = "8B4C24048B0183480803C70100000000C3"
		self.do(gadget)

		#mov     ecx, [esp+arg_0]
		#mov     eax, [ecx]
		#or      dword ptr [eax+8], 3
		#mov     dword ptr [ecx], 0
		#retn


  def test_gadget_sub_6E5BB1B0(self):
		#sub_6E5BB1B0
		gadget = "8BC133C98908894804894808BAFDFFFFFF89500C89481089481489481889481CC7402010FFA56EC7402401000000894828C7402C05000000C74030FFFFFFFFC740340780000083603CFC806040F08160440000FCFF884838894848C20400"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     edx, 0FFFFFFFDh
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     dword ptr [eax+20h], offset s_infoStructureJSC2UClassInfo2B; JSC::ClassInfo const JSC::Structure::s_info
		#mov     dword ptr [eax+24h], 1
		#mov     [eax+28h], ecx
		#mov     dword ptr [eax+2Ch], 5
		#mov     dword ptr [eax+30h], 0FFFFFFFFh
		#mov     dword ptr [eax+34h], 8007h
		#and     dword ptr [eax+3Ch], 0FFFFFFFCh
		#and     byte ptr [eax+40h], 0F0h
		#and     dword ptr [eax+44h], 0FFFC0000h
		#mov     [eax+38h], cl
		#mov     [eax+48h], ecx
		#retn    4


  def test_gadget_sub_6E5BCA20(self):
		#sub_6E5BCA20
		gadget = "8BD1C1EA0C80E20F80CAE0568B308816FF008B308BD1C1EA0680E23F80CA808816FF008B1080E13F80C980880AFF005EC3"
		self.do(gadget)

		#mov     edx, ecx
		#shr     edx, 0Ch
		#and     dl, 0Fh
		#or      dl, 0E0h
		#push    esi
		#mov     esi, [eax]
		#mov     [esi], dl
		#inc     dword ptr [eax]
		#mov     esi, [eax]
		#mov     edx, ecx
		#shr     edx, 6
		#and     dl, 3Fh
		#or      dl, 80h
		#mov     [esi], dl
		#inc     dword ptr [eax]
		#mov     edx, [eax]
		#and     cl, 3Fh
		#or      cl, 80h
		#mov     [edx], cl
		#inc     dword ptr [eax]
		#pop     esi
		#retn


  def test_gadget_sub_6E5C0EC0(self):
		#sub_6E5C0EC0
		gadget = "8B442408C700900E5C6EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E5C0E90
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E5C1980(self):
		#sub_6E5C1980
		gadget = "8B815C480000C3"
		self.do(gadget)

		#mov     eax, [ecx+485Ch]
		#retn


  def test_gadget_sub_6E5C1FC0(self):
		#sub_6E5C1FC0
		gadget = "8B4424048BD081E20000FFFF2BC2C1E803568BF08BCE83E11FB801000000D3E0C1EE052344B2145EF7D81BC0F7D8C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, eax
		#and     edx, 0FFFF0000h
		#sub     eax, edx
		#shr     eax, 3
		#push    esi
		#mov     esi, eax
		#mov     ecx, esi
		#and     ecx, 1Fh
		#mov     eax, 1
		#shl     eax, cl
		#shr     esi, 5
		#and     eax, [edx+esi*4+14h]
		#pop     esi
		#neg     eax
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_6E5C3D40(self):
		#sub_6E5C3D40
		gadget = "8BD133C057890289420489420889420C89421089421489421889421C8942208942248982280400008D7A28B900010000F3AB8BC25FC3"
		self.do(gadget)

		#mov     edx, ecx
		#xor     eax, eax
		#push    edi
		#mov     [edx], eax
		#mov     [edx+4], eax
		#mov     [edx+8], eax
		#mov     [edx+0Ch], eax
		#mov     [edx+10h], eax
		#mov     [edx+14h], eax
		#mov     [edx+18h], eax
		#mov     [edx+1Ch], eax
		#mov     [edx+20h], eax
		#mov     [edx+24h], eax
		#mov     [edx+428h], eax
		#lea     edi, [edx+28h]
		#mov     ecx, 100h
		#rep stosd
		#mov     eax, edx
		#pop     edi
		#retn


  def test_gadget_sub_6E5C4540(self):
		#sub_6E5C4540
		gadget = "B848A7A66EC3"
		self.do(gadget)

		#mov     eax, offset dword_6EA6A748
		#retn


  def test_gadget_sub_6E5C4550(self):
		#sub_6E5C4550
		gadget = "B850A7A66EC3"
		self.do(gadget)

		#mov     eax, offset dword_6EA6A750
		#retn


  def test_gadget__Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_73(self):
		#_Get_deleter_Ref_count_basestdUBEPAXABVtype_infoZ_73
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_6E5C8020(self):
		#sub_6E5C8020
		gadget = "83EC088B41E88B49EC250000FFFF8B90340400008B824C4800008B8078490000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+4978h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E5CD680(self):
		#sub_6E5CD680
		gadget = "837908000F95C0C3"
		self.do(gadget)

		#cmp     dword ptr [ecx+8], 0
		#setnz   al
		#retn


  def test_gadget_sub_6E5CD690(self):
		#sub_6E5CD690
		gadget = "8B44240433D285C90F95C2890883C2FA895004C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     edx, edx
		#test    ecx, ecx
		#setnz   dl
		#mov     [eax], ecx
		#add     edx, 0FFFFFFFAh
		#mov     [eax+4], edx
		#retn    0Ch


  def test_gadget_sub_6E5CE900(self):
		#sub_6E5CE900
		gadget = "DD44240433D253DD5C24088B44240856578BF0F7D203C28B542414F7D613D68BF08BFA0FACFE16C1EF1633D733C68BF08BFA0FA4F70DF7D7C1E60DF7D603C613D78BF88BDA0FACDF0833F88BF7C1EB0833DA8BD30FA4FB0303FF03FF03FF03F713D38BC68BFA0FACF80F33F0C1EF0F33D78BC68BFA0FA4C71BC1E01BF7D003F0F7D713D78BC60FACD01F33C683E03F5FC1E0045EC1EA1F03C15BC20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#xor     edx, edx
		#push    ebx
		#fstp    [esp+4+arg_0]
		#mov     eax, dword ptr [esp+4+arg_0]
		#push    esi
		#push    edi
		#mov     esi, eax
		#not     edx
		#add     eax, edx
		#mov     edx, dword ptr [esp+0Ch+arg_0+4]
		#not     esi
		#adc     edx, esi
		#mov     esi, eax
		#mov     edi, edx
		#shrd    esi, edi, 16h
		#shr     edi, 16h
		#xor     edx, edi
		#xor     eax, esi
		#mov     esi, eax
		#mov     edi, edx
		#shld    edi, esi, 0Dh
		#not     edi
		#shl     esi, 0Dh
		#not     esi
		#add     eax, esi
		#adc     edx, edi
		#mov     edi, eax
		#mov     ebx, edx
		#shrd    edi, ebx, 8
		#xor     edi, eax
		#mov     esi, edi
		#shr     ebx, 8
		#xor     ebx, edx
		#mov     edx, ebx
		#shld    ebx, edi, 3
		#add     edi, edi
		#add     edi, edi
		#add     edi, edi
		#add     esi, edi
		#adc     edx, ebx
		#mov     eax, esi
		#mov     edi, edx
		#shrd    eax, edi, 0Fh
		#xor     esi, eax
		#shr     edi, 0Fh
		#xor     edx, edi
		#mov     eax, esi
		#mov     edi, edx
		#shld    edi, eax, 1Bh
		#shl     eax, 1Bh
		#not     eax
		#add     esi, eax
		#not     edi
		#adc     edx, edi
		#mov     eax, esi
		#shrd    eax, edx, 1Fh
		#xor     eax, esi
		#and     eax, 3Fh
		#pop     edi
		#shl     eax, 4
		#pop     esi
		#shr     edx, 1Fh
		#add     eax, ecx
		#pop     ebx
		#retn    8


  def test_gadget_sub_6E5CFD40(self):
		#sub_6E5CFD40
		gadget = "8BC18B4C24088908C74004000000008B4920894808C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#retn    8


  def test_gadget_sub_6E5CFE00(self):
		#sub_6E5CFE00
		gadget = "8B44240C8B480C8B51548B4A1C8B44240433D285C90F95C2890883C2FA895004C3"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     ecx, [eax+0Ch]
		#mov     edx, [ecx+54h]
		#mov     ecx, [edx+1Ch]
		#mov     eax, [esp+arg_0]
		#xor     edx, edx
		#test    ecx, ecx
		#setnz   dl
		#mov     [eax], ecx
		#add     edx, 0FFFFFFFAh
		#mov     [eax+4], edx
		#retn


  def test_gadget_sub_6E5D1180(self):
		#sub_6E5D1180
		gadget = "8BC18B4C240C890833D28950048B49208948088B4C240889500C894810895014895018C7401C01000000C20C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax], ecx
		#xor     edx, edx
		#mov     [eax+4], edx
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], edx
		#mov     [eax+18h], edx
		#mov     dword ptr [eax+1Ch], 1
		#retn    0Ch


  def test_gadget_sub_6E5D22C0(self):
		#sub_6E5D22C0
		gadget = "8B4118D1E8F7D083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#shr     eax, 1
		#not     eax
		#and     eax, 1
		#retn


  def test_gadget_sub_6E5D22D0(self):
		#sub_6E5D22D0
		gadget = "8B4118C1E802F7D083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#shr     eax, 2
		#not     eax
		#and     eax, 1
		#retn


  def test_gadget_sub_6E5D22E0(self):
		#sub_6E5D22E0
		gadget = "8B4118C1E803F7D083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#shr     eax, 3
		#not     eax
		#and     eax, 1
		#retn


  def test_gadget_sub_6E5D22F0(self):
		#sub_6E5D22F0
		gadget = "8B51088B4424048B490C8910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx+8]
		#mov     eax, [esp+arg_0]
		#mov     ecx, [ecx+0Ch]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E5D2370(self):
		#sub_6E5D2370
		gadget = "8B4424048B5424088941108B411883E0FD83C820895114894118C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [ecx+10h], eax
		#mov     eax, [ecx+18h]
		#and     eax, 0FFFFFFFDh
		#or      eax, 20h
		#mov     [ecx+14h], edx
		#mov     [ecx+18h], eax
		#retn    8


  def test_gadget_sub_6E5D2390(self):
		#sub_6E5D2390
		gadget = "8B4424048B5424088941088B411883E0FD83C82089510C894118C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [ecx+8], eax
		#mov     eax, [ecx+18h]
		#and     eax, 0FFFFFFFDh
		#or      eax, 20h
		#mov     [ecx+0Ch], edx
		#mov     [ecx+18h], eax
		#retn    8


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_82(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_82
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E5D2430(self):
		#sub_6E5D2430
		gadget = "B8FCFFFFFF33D28911894104C741180E000000C3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFCh
		#xor     edx, edx
		#mov     [ecx], edx
		#mov     [ecx+4], eax
		#mov     dword ptr [ecx+18h], 0Eh
		#retn


  def test_gadget_sub_6E5D2850(self):
		#sub_6E5D2850
		gadget = "8B442408C7400400000000C7000000000033C0C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax+4], 0
		#mov     dword ptr [eax], 0
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E5D2A00(self):
		#sub_6E5D2A00
		gadget = "8B01807834111BC0F7D023C1C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#cmp     byte ptr [eax+34h], 11h
		#sbb     eax, eax
		#not     eax
		#and     eax, ecx
		#retn


  def test_gadget_sub_6E5D3420(self):
		#sub_6E5D3420
		gadget = "C7413000000000C20400"
		self.do(gadget)

		#mov     dword ptr [ecx+30h], 0
		#retn    4


  def test_gadget_sub_6E5D3AD0(self):
		#sub_6E5D3AD0
		gadget = "8D8168010000C3"
		self.do(gadget)

		#lea     eax, [ecx+168h]
		#retn


  def test_gadget_sub_6E5D3B80(self):
		#sub_6E5D3B80
		gadget = "518B442408C7042400000000C7000100000059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     [esp+4+var_4], 0
		#mov     dword ptr [eax], 1
		#pop     ecx
		#retn


  def test_gadget_sub_6E5D3BA0(self):
		#sub_6E5D3BA0
		gadget = "8B118B49488B44240403D203D203D22BCA8B51088B490CC74004FAFFFFFFC700000000008910894804C20400"
		self.do(gadget)

		#mov     edx, [ecx]
		#mov     ecx, [ecx+48h]
		#mov     eax, [esp+arg_0]
		#add     edx, edx
		#add     edx, edx
		#add     edx, edx
		#sub     ecx, edx
		#mov     edx, [ecx+8]
		#mov     ecx, [ecx+0Ch]
		#mov     dword ptr [eax+4], 0FFFFFFFAh
		#mov     dword ptr [eax], 0
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E5D3BD0(self):
		#sub_6E5D3BD0
		gadget = "8B4424048B8068010000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+168h]
		#retn


  def test_gadget_sub_6E5D5210(self):
		#sub_6E5D5210
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80E0480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48E0h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E5DB0C0(self):
		#sub_6E5DB0C0
		gadget = "8B4424048B088B5424088B123BD11BC0F7D83BCA1BC9F7D92BC1C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax]
		#mov     edx, [esp+arg_4]
		#mov     edx, [edx]
		#cmp     edx, ecx
		#sbb     eax, eax
		#neg     eax
		#cmp     ecx, edx
		#sbb     ecx, ecx
		#neg     ecx
		#sub     eax, ecx
		#retn


  def test_gadget_sub_6E5DB1A0(self):
		#sub_6E5DB1A0
		gadget = "8B4424048B008B4C24082B01C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax]
		#mov     ecx, [esp+arg_4]
		#sub     eax, [ecx]
		#retn


  def test_gadget_sub_6E5DB8E0(self):
		#sub_6E5DB8E0
		gadget = "8B118B44240403C08164C20C000000808B098D54C20C8B5424080954C10C8D44C10CC20800"
		self.do(gadget)

		#mov     edx, [ecx]
		#mov     eax, [esp+arg_0]
		#add     eax, eax
		#and     dword ptr [edx+eax*8+0Ch], 80000000h
		#mov     ecx, [ecx]
		#lea     edx, [edx+eax*8+0Ch]
		#mov     edx, [esp+arg_4]
		#or      [ecx+eax*8+0Ch], edx
		#lea     eax, [ecx+eax*8+0Ch]
		#retn    8


  def test_gadget_sub_6E5DB910(self):
		#sub_6E5DB910
		gadget = "8B118B44240403C08164C208000000808B098D54C2088B5424080954C1088D44C108C20800"
		self.do(gadget)

		#mov     edx, [ecx]
		#mov     eax, [esp+arg_0]
		#add     eax, eax
		#and     dword ptr [edx+eax*8+8], 80000000h
		#mov     ecx, [ecx]
		#lea     edx, [edx+eax*8+8]
		#mov     edx, [esp+arg_4]
		#or      [ecx+eax*8+8], edx
		#lea     eax, [ecx+eax*8+8]
		#retn    8


  def test_gadget_sub_6E5E2800(self):
		#sub_6E5E2800
		gadget = "837C2404008BC18D4804C700010000008D5108C70200000000C74204000000008911C741040000000089490CC702000000000F94C1884814C6401500C20400"
		self.do(gadget)

		#cmp     [esp+arg_0], 0
		#mov     eax, ecx
		#lea     ecx, [eax+4]
		#mov     dword ptr [eax], 1
		#lea     edx, [ecx+8]
		#mov     dword ptr [edx], 0
		#mov     dword ptr [edx+4], 0
		#mov     [ecx], edx
		#mov     dword ptr [ecx+4], 0
		#mov     [ecx+0Ch], ecx
		#mov     dword ptr [edx], 0
		#setz    cl
		#mov     [eax+14h], cl
		#mov     byte ptr [eax+15h], 0
		#retn    4


  def test_gadget_sub_6E5E4BB0(self):
		#sub_6E5E4BB0
		gadget = "C7019CE5846EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E84E59C
		#retn


  def test_gadget_sub_6E5EAF50(self):
		#sub_6E5EAF50
		gadget = "8BC1C70001000000DD050847A66EDD580833C989481089481489481889481C89482089482489482889482C894830894834DD050847A66EDD583889484089484489484889484C89485089485489485889485C894860894864C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], 1
		#fld     dbl_6EA64708
		#fstp    qword ptr [eax+8]
		#xor     ecx, ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#fld     dbl_6EA64708
		#fstp    qword ptr [eax+38h]
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+5Ch], ecx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#retn


  def test_gadget_sub_6E5EAFB0(self):
		#sub_6E5EAFB0
		gadget = "DD44240433D253DD5C24088B44240856578BF0F7D203C28B542414F7D613D68BF08BFA0FACFE16C1EF1633D733C68BF08BFA0FA4F70DF7D7C1E60DF7D603C613D78BF88BDA0FACDF0833F88BF7C1EB0833DA8BD30FA4FB0303FF03FF03FF03F713D38BC68BFA0FACF80F33F0C1EF0F33D78BC68BFA0FA4C71BC1E01BF7D003F0F7D713D78BC60FACD01F33C683E00F5FC1E0045EC1EA1F03C15BC20800"
		self.do(gadget)

		#fld     [esp+arg_0]
		#xor     edx, edx
		#push    ebx
		#fstp    [esp+4+arg_0]
		#mov     eax, dword ptr [esp+4+arg_0]
		#push    esi
		#push    edi
		#mov     esi, eax
		#not     edx
		#add     eax, edx
		#mov     edx, dword ptr [esp+0Ch+arg_0+4]
		#not     esi
		#adc     edx, esi
		#mov     esi, eax
		#mov     edi, edx
		#shrd    esi, edi, 16h
		#shr     edi, 16h
		#xor     edx, edi
		#xor     eax, esi
		#mov     esi, eax
		#mov     edi, edx
		#shld    edi, esi, 0Dh
		#not     edi
		#shl     esi, 0Dh
		#not     esi
		#add     eax, esi
		#adc     edx, edi
		#mov     edi, eax
		#mov     ebx, edx
		#shrd    edi, ebx, 8
		#xor     edi, eax
		#mov     esi, edi
		#shr     ebx, 8
		#xor     ebx, edx
		#mov     edx, ebx
		#shld    ebx, edi, 3
		#add     edi, edi
		#add     edi, edi
		#add     edi, edi
		#add     esi, edi
		#adc     edx, ebx
		#mov     eax, esi
		#mov     edi, edx
		#shrd    eax, edi, 0Fh
		#xor     esi, eax
		#shr     edi, 0Fh
		#xor     edx, edi
		#mov     eax, esi
		#mov     edi, edx
		#shld    edi, eax, 1Bh
		#shl     eax, 1Bh
		#not     eax
		#add     esi, eax
		#not     edi
		#adc     edx, edi
		#mov     eax, esi
		#shrd    eax, edx, 1Fh
		#xor     eax, esi
		#and     eax, 0Fh
		#pop     edi
		#shl     eax, 4
		#pop     esi
		#shr     edx, 1Fh
		#add     eax, ecx
		#pop     ebx
		#retn    8


  def test_gadget_sub_6E5EB1C0(self):
		#sub_6E5EB1C0
		gadget = "8BC18B4C2408890833D28950048B4920894808B9FAFFFFFF895010894814895018C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#xor     edx, edx
		#mov     [eax+4], edx
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#mov     ecx, 0FFFFFFFAh
		#mov     [eax+10h], edx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], edx
		#retn    8


  def test_gadget_sub_6E5EBA60(self):
		#sub_6E5EBA60
		gadget = "6AFF68090F7D6E64A1000000005051A1F44AA66E33C4508D44240864A30000000033C9894C24048B44241889088948048B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7D0F09
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#xor     ecx, ecx
		#mov     [esp+14h+var_10], ecx
		#mov     eax, [esp+14h+arg_0]
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E5EFE30(self):
		#sub_6E5EFE30
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482C89483089483489483889483C89484089484489484889484C894850894854894858C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#retn


  def test_gadget_sub_6E5F3150(self):
		#sub_6E5F3150
		gadget = "8B018B400483C014C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#mov     eax, [eax+4]
		#add     eax, 14h
		#retn


  def test_gadget_sub_6E5F4550(self):
		#sub_6E5F4550
		gadget = "8B4424048B5424088941088B44240C89510C8B542410C74128FFFFFFFFC7412C00000000C7010000000089411889511CC21000"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [ecx+8], eax
		#mov     eax, [esp+arg_8]
		#mov     [ecx+0Ch], edx
		#mov     edx, [esp+arg_C]
		#mov     dword ptr [ecx+28h], 0FFFFFFFFh
		#mov     dword ptr [ecx+2Ch], 0
		#mov     dword ptr [ecx], 0
		#mov     [ecx+18h], eax
		#mov     [ecx+1Ch], edx
		#retn    10h


  def test_gadget_sub_6E5F4C30(self):
		#sub_6E5F4C30
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80FC480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48FCh]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E5F5970(self):
		#sub_6E5F5970
		gadget = "8BC18B4C240889088B4C240C33D289500489480883C9FFC6401801895010894814C20C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [esp+arg_8]
		#xor     edx, edx
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#or      ecx, 0FFFFFFFFh
		#mov     byte ptr [eax+18h], 1
		#mov     [eax+10h], edx
		#mov     [eax+14h], ecx
		#retn    0Ch


  def test_gadget_sub_6E5F5C10(self):
		#sub_6E5F5C10
		gadget = "8BC18B4C24048B1189108B51088950088B510C89500C8B51108950108B51148950148B51188950188B491C89481CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     [eax], edx
		#mov     edx, [ecx+8]
		#mov     [eax+8], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+10h]
		#mov     [eax+10h], edx
		#mov     edx, [ecx+14h]
		#mov     [eax+14h], edx
		#mov     edx, [ecx+18h]
		#mov     [eax+18h], edx
		#mov     ecx, [ecx+1Ch]
		#mov     [eax+1Ch], ecx
		#retn    4


  def test_gadget_sub_6E5F7BC0(self):
		#sub_6E5F7BC0
		gadget = "8B442408C700707B5F6EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E5F7B70
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E5FC0D0(self):
		#sub_6E5FC0D0
		gadget = "8BC18B4C2408890833D28950048B4920894808B9FAFFFFFF895010894814C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#xor     edx, edx
		#mov     [eax+4], edx
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#mov     ecx, 0FFFFFFFAh
		#mov     [eax+10h], edx
		#mov     [eax+14h], ecx
		#retn    8


  def test_gadget_sub_6E5FD150(self):
		#sub_6E5FD150
		gadget = "8B44240833D285C00F95C289411083C2FA895114C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#xor     edx, edx
		#test    eax, eax
		#setnz   dl
		#mov     [ecx+10h], eax
		#add     edx, 0FFFFFFFAh
		#mov     [ecx+14h], edx
		#retn    8


  def test_gadget_sub_6E6092E0(self):
		#sub_6E6092E0
		gadget = "8BC1806004FC8A4C2408C70009000000C7401C000000000FB6500880E10180E2FC02C90ACA8A54240480E2010ACA884808C7401800000000C7401C01000000C20800"
		self.do(gadget)

		#mov     eax, ecx
		#and     byte ptr [eax+4], 0FCh
		#mov     cl, [esp+arg_4]
		#mov     dword ptr [eax], 9
		#mov     dword ptr [eax+1Ch], 0
		#movzx   edx, byte ptr [eax+8]
		#and     cl, 1
		#and     dl, 0FCh
		#add     cl, cl
		#or      cl, dl
		#mov     dl, [esp+arg_0]
		#and     dl, 1
		#or      cl, dl
		#mov     [eax+8], cl
		#mov     dword ptr [eax+18h], 0
		#mov     dword ptr [eax+1Ch], 1
		#retn    8


  def test_gadget_sub_6E60FDD0(self):
		#sub_6E60FDD0
		gadget = "51FE010FB60153568D7408028A060041010FB651018A540A0288160FB6710188440E020FB6D20FB6C003D081E2FF0000008A5C0A02FE010FB6118A440A020041018D740A020FB651018A540A0288160FB6710188440E020FB6C00FB6D203D081E2FF0000000FB6540A02FE010FB6018D7408028A06004101885424090FB651018A540A0288160FB6710188440E020FB6C00FB6D203D081E2FF0000000FB6540A02FE010FB6018D7408028854240A8A160051010FB641018A44080288060FB67424098844240B0FB64101885408020FB6C3C1E0080BC60FB674240AC1E0080BC60FB674240B0FB6D203F281E6FF0000000FB64C0E02C1E0085E0BC15B59C3"
		self.do(gadget)

		#push    ecx
		#inc     byte ptr [ecx]
		#movzx   eax, byte ptr [ecx]
		#push    ebx
		#push    esi
		#lea     esi, [eax+ecx+2]
		#mov     al, [esi]
		#add     [ecx+1], al
		#movzx   edx, byte ptr [ecx+1]
		#mov     dl, [edx+ecx+2]
		#mov     [esi], dl
		#movzx   esi, byte ptr [ecx+1]
		#mov     [esi+ecx+2], al
		#movzx   edx, dl
		#movzx   eax, al
		#add     edx, eax
		#and     edx, 0FFh
		#mov     bl, [edx+ecx+2]
		#inc     byte ptr [ecx]
		#movzx   edx, byte ptr [ecx]
		#mov     al, [edx+ecx+2]
		#add     [ecx+1], al
		#lea     esi, [edx+ecx+2]
		#movzx   edx, byte ptr [ecx+1]
		#mov     dl, [edx+ecx+2]
		#mov     [esi], dl
		#movzx   esi, byte ptr [ecx+1]
		#mov     [esi+ecx+2], al
		#movzx   eax, al
		#movzx   edx, dl
		#add     edx, eax
		#and     edx, 0FFh
		#movzx   edx, byte ptr [edx+ecx+2]
		#inc     byte ptr [ecx]
		#movzx   eax, byte ptr [ecx]
		#lea     esi, [eax+ecx+2]
		#mov     al, [esi]
		#add     [ecx+1], al
		#mov     [esp+0Ch+var_3], dl
		#movzx   edx, byte ptr [ecx+1]
		#mov     dl, [edx+ecx+2]
		#mov     [esi], dl
		#movzx   esi, byte ptr [ecx+1]
		#mov     [esi+ecx+2], al
		#movzx   eax, al
		#movzx   edx, dl
		#add     edx, eax
		#and     edx, 0FFh
		#movzx   edx, byte ptr [edx+ecx+2]
		#inc     byte ptr [ecx]
		#movzx   eax, byte ptr [ecx]
		#lea     esi, [eax+ecx+2]
		#mov     [esp+0Ch+var_2], dl
		#mov     dl, [esi]
		#add     [ecx+1], dl
		#movzx   eax, byte ptr [ecx+1]
		#mov     al, [eax+ecx+2]
		#mov     [esi], al
		#movzx   esi, [esp+0Ch+var_3]
		#mov     [esp+0Ch+var_1], al
		#movzx   eax, byte ptr [ecx+1]
		#mov     [eax+ecx+2], dl
		#movzx   eax, bl
		#shl     eax, 8
		#or      eax, esi
		#movzx   esi, [esp+0Ch+var_2]
		#shl     eax, 8
		#or      eax, esi
		#movzx   esi, [esp+0Ch+var_1]
		#movzx   edx, dl
		#add     esi, edx
		#and     esi, 0FFh
		#movzx   ecx, byte ptr [esi+ecx+2]
		#shl     eax, 8
		#pop     esi
		#or      eax, ecx
		#pop     ebx
		#pop     ecx
		#retn


  def test_gadget_JSPropertyNameArrayRetain(self):
		#JSPropertyNameArrayRetain
		gadget = "8B442404FF00C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#inc     dword ptr [eax]
		#retn


  def test_gadget_JSPropertyNameArrayGetCount(self):
		#JSPropertyNameArrayGetCount
		gadget = "8B4424048B4010C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     eax, [eax+10h]
		#retn


  def test_gadget_sub_6E611480(self):
		#sub_6E611480
		gadget = "6AFF68090F7D6E64A1000000005051A1F44AA66E33C4508D44240864A30000000033D2895424048B442418B9FAFFFFFF891089500889480C8B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7D0F09
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#xor     edx, edx
		#mov     [esp+14h+var_10], edx
		#mov     eax, [esp+14h+arg_0]
		#mov     ecx, 0FFFFFFFAh
		#mov     [eax], edx
		#mov     [eax+8], edx
		#mov     [eax+0Ch], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E6173C0(self):
		#sub_6E6173C0
		gadget = "C6410101C3"
		self.do(gadget)

		#mov     byte ptr [ecx+1], 1
		#retn


  def test_gadget_reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_78(self):
		#reserve_message_Order_node_baseW4agent_statusConcurrencyConcurrencyUAE_NHZ_78
		gadget = "32C0C20400"
		self.do(gadget)

		#xor     al, al
		#retn    4


  def test_gadget_8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_83(self):
		#8_ContextCallbackdetailsConcurrencyQBE_NABV012Z_83
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_6E620620(self):
		#sub_6E620620
		gadget = "8BC18B4C2408890833C9894804884808C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], cl
		#retn    8


  def test_gadget_sub_6E621DF0(self):
		#sub_6E621DF0
		gadget = "8B41308B1083BAB4580000640F97C28850088B41308A5008885134C3"
		self.do(gadget)

		#mov     eax, [ecx+30h]
		#mov     edx, [eax]
		#cmp     dword ptr [edx+58B4h], 64h
		#setnbe  dl
		#mov     [eax+8], dl
		#mov     eax, [ecx+30h]
		#mov     dl, [eax+8]
		#mov     [ecx+34h], dl
		#retn


  def test_gadget_sub_6E622800(self):
		#sub_6E622800
		gadget = "8BC18B4C2404890833C989480489480889480CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#retn    4


  def test_gadget_sub_6E626AB0(self):
		#sub_6E626AB0
		gadget = "8B5424048BC18D481489088B4C2408C7400400000000C740088000000089500C894810C20800"
		self.do(gadget)

		#mov     edx, [esp+arg_0]
		#mov     eax, ecx
		#lea     ecx, [eax+14h]
		#mov     [eax], ecx
		#mov     ecx, [esp+arg_4]
		#mov     dword ptr [eax+4], 0
		#mov     dword ptr [eax+8], 80h
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], ecx
		#retn    8


  def test_gadget_sub_6E626F90(self):
		#sub_6E626F90
		gadget = "8B4114034110894108C3"
		self.do(gadget)

		#mov     eax, [ecx+14h]
		#add     eax, [ecx+10h]
		#mov     [ecx+8], eax
		#retn


  def test_gadget_sub_6E627740(self):
		#sub_6E627740
		gadget = "6AFF6889397D6E64A1000000005083EC08A1F44AA66E33C4508D44240C64A30000000033C9894C24048B44241C8B54240489088950048948088B4C240C64890D000000005983C414C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7D3989
		#mov     eax, large fs:0
		#push    eax
		#sub     esp, 8
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+18h+var_C]
		#mov     large fs:0, eax
		#xor     ecx, ecx
		#mov     [esp+18h+var_14], ecx
		#mov     eax, [esp+18h+arg_0]
		#mov     edx, [esp+18h+var_14]
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     [eax+8], ecx
		#mov     ecx, [esp+18h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 14h
		#retn


  def test_gadget_sub_6E627C40(self):
		#sub_6E627C40
		gadget = "8B412C8B4058C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#mov     eax, [eax+58h]
		#retn


  def test_gadget_sub_6E627C50(self):
		#sub_6E627C50
		gadget = "8B412C8B4054C3"
		self.do(gadget)

		#mov     eax, [ecx+2Ch]
		#mov     eax, [eax+54h]
		#retn


  def test_gadget_sub_6E633060(self):
		#sub_6E633060
		gadget = "83EC108B4424140305A40EA66E5699F73DA80EA66E57C1E0040305D0B1A66E8B48088B108B70048B400C894424148B4424200FBFF989108B542414897004897808C1E91089500C0FBFC18B4C24245F89015E83C410C3"
		self.do(gadget)

		#sub     esp, 10h
		#mov     eax, [esp+10h+arg_0]
		#add     eax, dword_6EA60EA4
		#push    esi
		#cdq
		#idiv    dword_6EA60EA8
		#push    edi
		#shl     eax, 4
		#add     eax, dword_6EA6B1D0
		#mov     ecx, [eax+8]
		#mov     edx, [eax]
		#mov     esi, [eax+4]
		#mov     eax, [eax+0Ch]
		#mov     [esp+18h+var_4], eax
		#mov     eax, [esp+18h+arg_4]
		#movsx   edi, cx
		#mov     [eax], edx
		#mov     edx, [esp+18h+var_4]
		#mov     [eax+4], esi
		#mov     [eax+8], edi
		#shr     ecx, 10h
		#mov     [eax+0Ch], edx
		#movsx   eax, cx
		#mov     ecx, [esp+18h+arg_8]
		#pop     edi
		#mov     [ecx], eax
		#pop     esi
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E633170(self):
		#sub_6E633170
		gadget = "8B4424048B118B4904C74004FAFFFFFFC700000000008910894804C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#mov     ecx, [ecx+4]
		#mov     dword ptr [eax+4], 0FFFFFFFAh
		#mov     dword ptr [eax], 0
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E637E00(self):
		#sub_6E637E00
		gadget = "8BC1C7001469926EC3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_6E926914
		#retn


  def test_gadget_sub_6E637E10(self):
		#sub_6E637E10
		gadget = "C7011469926EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E926914
		#retn


  def test_gadget_sub_6E6382B0(self):
		#sub_6E6382B0
		gadget = "8B442408C7008082636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E638280
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E638370(self):
		#sub_6E638370
		gadget = "8B442408C700C082636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset loc_6E6382C0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E638380(self):
		#sub_6E638380
		gadget = "8B41288B4004C3"
		self.do(gadget)

		#mov     eax, [ecx+28h]
		#mov     eax, [eax+4]
		#retn


  def test_gadget_sub_6E639950(self):
		#sub_6E639950
		gadget = "8BC18B4C240889088B54240483C9FF5633F689700489700C8970108948208948280FB6482C895018897014578B7C2418320F80E10130482C8A57018A482C80E1F980E20102D20AD188502C8A4F0202C902C902C932CA80E10832CA88482C0FB6570389703089703489703880E20180E1CFC0E2040AD18B4C241488502C89483C89704089704489704889704C89705089705489705889705C89706089706489706889706C89707089707489707889707C89B08000000089B08400000089B08800000089B08C00000089B09000000089B09400000089B09800000089B0A000000089B0A400000089B0A800000089B0AC00000089B0B0000000C7809C0000000100000089B0B40000005F89B0B800000089B0BC00000089B0C00000005EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#mov     edx, [esp+arg_0]
		#or      ecx, 0FFFFFFFFh
		#push    esi
		#xor     esi, esi
		#mov     [eax+4], esi
		#mov     [eax+0Ch], esi
		#mov     [eax+10h], esi
		#mov     [eax+20h], ecx
		#mov     [eax+28h], ecx
		#movzx   ecx, byte ptr [eax+2Ch]
		#mov     [eax+18h], edx
		#mov     [eax+14h], esi
		#push    edi
		#mov     edi, [esp+8+arg_C]
		#xor     cl, [edi]
		#and     cl, 1
		#xor     [eax+2Ch], cl
		#mov     dl, [edi+1]
		#mov     cl, [eax+2Ch]
		#and     cl, 0F9h
		#and     dl, 1
		#add     dl, dl
		#or      dl, cl
		#mov     [eax+2Ch], dl
		#mov     cl, [edi+2]
		#add     cl, cl
		#add     cl, cl
		#add     cl, cl
		#xor     cl, dl
		#and     cl, 8
		#xor     cl, dl
		#mov     [eax+2Ch], cl
		#movzx   edx, byte ptr [edi+3]
		#mov     [eax+30h], esi
		#mov     [eax+34h], esi
		#mov     [eax+38h], esi
		#and     dl, 1
		#and     cl, 0CFh
		#shl     dl, 4
		#or      dl, cl
		#mov     ecx, [esp+8+arg_8]
		#mov     [eax+2Ch], dl
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], esi
		#mov     [eax+44h], esi
		#mov     [eax+48h], esi
		#mov     [eax+4Ch], esi
		#mov     [eax+50h], esi
		#mov     [eax+54h], esi
		#mov     [eax+58h], esi
		#mov     [eax+5Ch], esi
		#mov     [eax+60h], esi
		#mov     [eax+64h], esi
		#mov     [eax+68h], esi
		#mov     [eax+6Ch], esi
		#mov     [eax+70h], esi
		#mov     [eax+74h], esi
		#mov     [eax+78h], esi
		#mov     [eax+7Ch], esi
		#mov     [eax+80h], esi
		#mov     [eax+84h], esi
		#mov     [eax+88h], esi
		#mov     [eax+8Ch], esi
		#mov     [eax+90h], esi
		#mov     [eax+94h], esi
		#mov     [eax+98h], esi
		#mov     [eax+0A0h], esi
		#mov     [eax+0A4h], esi
		#mov     [eax+0A8h], esi
		#mov     [eax+0ACh], esi
		#mov     [eax+0B0h], esi
		#mov     dword ptr [eax+9Ch], 1
		#mov     [eax+0B4h], esi
		#pop     edi
		#mov     [eax+0B8h], esi
		#mov     [eax+0BCh], esi
		#mov     [eax+0C0h], esi
		#pop     esi
		#retn    10h


  def test_gadget_sub_6E63ADF0(self):
		#sub_6E63ADF0
		gadget = "518B44240833C9890889480489480889480C890C2489481059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+10h], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E63DF50(self):
		#sub_6E63DF50
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80E8480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48E8h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E63E620(self):
		#sub_6E63E620
		gadget = "8BC18B4C24088908C7400400000000C20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#retn    8


  def test_gadget_sub_6E63E7A0(self):
		#sub_6E63E7A0
		gadget = "8B442408C70030E7636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E63E730
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E63E8A0(self):
		#sub_6E63E8A0
		gadget = "8B442408C700B0E7636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E63E7B0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E63E8B0(self):
		#sub_6E63E8B0
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80EC480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48ECh]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E63ECB0(self):
		#sub_6E63ECB0
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B8008490000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+4908h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E63F1B0(self):
		#sub_6E63F1B0
		gadget = "8B442408C70000F1636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E63F100
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E63F240(self):
		#sub_6E63F240
		gadget = "8B442408C700C0F1636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset loc_6E63F1C0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E63F320(self):
		#sub_6E63F320
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80C8480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48C8h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E63F6B0(self):
		#sub_6E63F6B0
		gadget = "8B442408C70030F6636EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E63F630
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E63FBF0(self):
		#sub_6E63FBF0
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80D8480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48D8h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E6403F0(self):
		#sub_6E6403F0
		gadget = "8B442408C700A003646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E6403A0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E640510(self):
		#sub_6E640510
		gadget = "8B442408C7000004646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset loc_6E640400
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E640E90(self):
		#sub_6E640E90
		gadget = "8B54240C8BC18B4C24088908C74004000000008B49208948088B4C241089500C894810C21000"
		self.do(gadget)

		#mov     edx, [esp+arg_8]
		#mov     eax, ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#mov     ecx, [ecx+20h]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], ecx
		#retn    10h


  def test_gadget_sub_6E641290(self):
		#sub_6E641290
		gadget = "8B442408C700C00E646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E640EC0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E6417C0(self):
		#sub_6E6417C0
		gadget = "8B442408C7004013646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E641340
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E641DD0(self):
		#sub_6E641DD0
		gadget = "8B442408C700001D646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E641D00
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E641E40(self):
		#sub_6E641E40
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80F8480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48F8h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E642040(self):
		#sub_6E642040
		gadget = "8B442408C700D01F646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E641FD0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E642200(self):
		#sub_6E642200
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B8000490000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+4900h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E642D30(self):
		#sub_6E642D30
		gadget = "8B442408C700E02C646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E642CE0
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E642D90(self):
		#sub_6E642D90
		gadget = "8B442408C700402D646EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E642D40
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E643B10(self):
		#sub_6E643B10
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B8004490000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+4904h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E644760(self):
		#sub_6E644760
		gadget = "83EC088B4424108B48E88B40EC8B098B5104894424048B826801000083C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [esp+8+arg_4]
		#mov     ecx, [eax-18h]
		#mov     eax, [eax-14h]
		#mov     ecx, [ecx]
		#mov     edx, [ecx+4]
		#mov     [esp+8+var_4], eax
		#mov     eax, [edx+168h]
		#add     esp, 8
		#retn


  def test_gadget_sub_6E644780(self):
		#sub_6E644780
		gadget = "83EC088B54240C8BC18B4AE88B52EC568BF18B0989542408895424088B51048B8AC40100008908C74004000000008970085E83C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#mov     edx, [esp+8+arg_0]
		#mov     eax, ecx
		#mov     ecx, [edx-18h]
		#mov     edx, [edx-14h]
		#push    esi
		#mov     esi, ecx
		#mov     ecx, [ecx]
		#mov     [esp+0Ch+var_4], edx
		#mov     [esp+0Ch+var_4], edx
		#mov     edx, [ecx+4]
		#mov     ecx, [edx+1C4h]
		#mov     [eax], ecx
		#mov     dword ptr [eax+4], 0
		#mov     [eax+8], esi
		#pop     esi
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6E645230(self):
		#sub_6E645230
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80F0480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48F0h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E650DF0(self):
		#sub_6E650DF0
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80F4480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48F4h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E651160(self):
		#sub_6E651160
		gadget = "8B442408C7005010656EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E651050
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E6565E0(self):
		#sub_6E6565E0
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80CC480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48CCh]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E65E820(self):
		#sub_6E65E820
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80D0480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48D0h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E65E8F0(self):
		#sub_6E65E8F0
		gadget = "8B4424048B1089118B50048951048B50088951088B500C89510C8B50108951108B50148951148B50188951188B501C89511C8B50208951208B4024894124C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx], edx
		#mov     edx, [eax+4]
		#mov     [ecx+4], edx
		#mov     edx, [eax+8]
		#mov     [ecx+8], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+0Ch], edx
		#mov     edx, [eax+10h]
		#mov     [ecx+10h], edx
		#mov     edx, [eax+14h]
		#mov     [ecx+14h], edx
		#mov     edx, [eax+18h]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+1Ch]
		#mov     [ecx+1Ch], edx
		#mov     edx, [eax+20h]
		#mov     [ecx+20h], edx
		#mov     eax, [eax+24h]
		#mov     [ecx+24h], eax
		#retn    4


  def test_gadget_sub_6E660320(self):
		#sub_6E660320
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80D4480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48D4h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E6614C0(self):
		#sub_6E6614C0
		gadget = "8B442408C7004014666EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E661440
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E661510(self):
		#sub_6E661510
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80DC480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48DCh]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E661F10(self):
		#sub_6E661F10
		gadget = "BAFCFFFFFF33C0C3"
		self.do(gadget)

		#mov     edx, 0FFFFFFFCh
		#xor     eax, eax
		#retn


  def test_gadget_sub_6E661F20(self):
		#sub_6E661F20
		gadget = "8B442408C700101F666EB801000000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     dword ptr [eax], offset sub_6E661F10
		#mov     eax, 1
		#retn


  def test_gadget_sub_6E663DF0(self):
		#sub_6E663DF0
		gadget = "83EC088B4C240C8B41E88B49EC250000FFFF8B90340400008B824C4800008B80E4480000894C240483C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [esp+8+arg_0]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     eax, [eax+48E4h]
		#mov     [esp+8+var_4], ecx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E66F780(self):
		#sub_6E66F780
		gadget = "518B4424088B54240C33C98910890C2489480459C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#mov     edx, [esp+4+arg_4]
		#xor     ecx, ecx
		#mov     [eax], edx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+4], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E6762E0(self):
		#sub_6E6762E0
		gadget = "8BC133C9890889480489480889480C89481089481489481889481C89482089482489482889482CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#retn


  def test_gadget_sub_6E6799E0(self):
		#sub_6E6799E0
		gadget = "8B4104C7410800000000C60000C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#mov     dword ptr [ecx+8], 0
		#mov     byte ptr [eax], 0
		#retn


  def test_gadget_sub_6E679BA0(self):
		#sub_6E679BA0
		gadget = "83C43C5B5F5E5DC3"
		self.do(gadget)

		#add     esp, 3Ch
		#pop     ebx
		#pop     edi
		#pop     esi
		#pop     ebp
		#retn


  def test_gadget_sub_6E67A270(self):
		#sub_6E67A270
		gadget = "8B44240C8B542410C641040289412C8951308B41348A5138334424143254241825FFFFFF7F31413480E201305138C21800"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     edx, [esp+arg_C]
		#mov     byte ptr [ecx+4], 2
		#mov     [ecx+2Ch], eax
		#mov     [ecx+30h], edx
		#mov     eax, [ecx+34h]
		#mov     dl, [ecx+38h]
		#xor     eax, [esp+arg_10]
		#xor     dl, [esp+arg_14]
		#and     eax, 7FFFFFFFh
		#xor     [ecx+34h], eax
		#and     dl, 1
		#xor     [ecx+38h], dl
		#retn    18h


  def test_gadget_sub_6E67CAD0(self):
		#sub_6E67CAD0
		gadget = "83EC088B41588B50EC8B48E88B49088954240433D285C90F95C28948E883C2FA8950EC83C408C3"
		self.do(gadget)

		#sub     esp, 8
		#mov     eax, [ecx+58h]
		#mov     edx, [eax-14h]
		#mov     ecx, [eax-18h]
		#mov     ecx, [ecx+8]
		#mov     [esp+8+var_4], edx
		#xor     edx, edx
		#test    ecx, ecx
		#setnz   dl
		#mov     [eax-18h], ecx
		#add     edx, 0FFFFFFFAh
		#mov     [eax-14h], edx
		#add     esp, 8
		#retn


  def test_gadget_sub_6E682020(self):
		#sub_6E682020
		gadget = "518B44240833C98908890C2489480459C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [esp+4+var_4], ecx
		#mov     [eax+4], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E682FE0(self):
		#sub_6E682FE0
		gadget = "8BC18B4C240489088B157C28A66E8950048B0D8028A66E8948088B158428A66E89500C8B0D8828A66E894810C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax], ecx
		#mov     edx, dword_6EA6287C
		#mov     [eax+4], edx
		#mov     ecx, dword_6EA62880
		#mov     [eax+8], ecx
		#mov     edx, off_6EA62884
		#mov     [eax+0Ch], edx
		#mov     ecx, dword_6EA62888
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E683CD0(self):
		#sub_6E683CD0
		gadget = "8BC133C989480889480C89481089481489481889481C88483C8948408B4C240489484CC20400"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+3Ch], cl
		#mov     [eax+40h], ecx
		#mov     ecx, [esp+arg_0]
		#mov     [eax+4Ch], ecx
		#retn    4


  def test_gadget_sub_6E692610(self):
		#sub_6E692610
		gadget = "8B41F88B50188D04D1C3"
		self.do(gadget)

		#mov     eax, [ecx-8]
		#mov     edx, [eax+18h]
		#lea     eax, [ecx+edx*8]
		#retn


  def test_gadget_sub_6E692620(self):
		#sub_6E692620
		gadget = "8B51F88B41D42B4234C1F802C3"
		self.do(gadget)

		#mov     edx, [ecx-8]
		#mov     eax, [ecx-2Ch]
		#sub     eax, [edx+34h]
		#sar     eax, 2
		#retn


  def test_gadget_sub_6E69DDA0(self):
		#sub_6E69DDA0
		gadget = "5164A1180000008904248B04248B400489010500C0FBFF89410459C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, large fs:18h
		#mov     [esp+4+var_4], eax
		#mov     eax, [esp+4+var_4]
		#mov     eax, [eax+4]
		#mov     [ecx], eax
		#add     eax, 0FFFBC000h
		#mov     [ecx+4], eax
		#pop     ecx
		#retn


  def test_gadget_sub_6E69E300(self):
		#sub_6E69E300
		gadget = "8B4424048B5424088941048B44240C89510C894108C20C00"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [ecx+4], eax
		#mov     eax, [esp+arg_8]
		#mov     [ecx+0Ch], edx
		#mov     [ecx+8], eax
		#retn    0Ch


  def test_gadget_sub_6E69E3F0(self):
		#sub_6E69E3F0
		gadget = "8B4424048B11568B30893189108B70048B51048971048950048B70088B51088971088950088B70148B51148971148950148B700C8B510C89710C89500C8B70108B51108971108950108B70208B51208971208950208B70188B51188971188950188B701C8B511C89711C89501C8B702C8B512C89712C89502C8B70248B51248971248950248B70288B51288971288950285EC20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [ecx]
		#push    esi
		#mov     esi, [eax]
		#mov     [ecx], esi
		#mov     [eax], edx
		#mov     esi, [eax+4]
		#mov     edx, [ecx+4]
		#mov     [ecx+4], esi
		#mov     [eax+4], edx
		#mov     esi, [eax+8]
		#mov     edx, [ecx+8]
		#mov     [ecx+8], esi
		#mov     [eax+8], edx
		#mov     esi, [eax+14h]
		#mov     edx, [ecx+14h]
		#mov     [ecx+14h], esi
		#mov     [eax+14h], edx
		#mov     esi, [eax+0Ch]
		#mov     edx, [ecx+0Ch]
		#mov     [ecx+0Ch], esi
		#mov     [eax+0Ch], edx
		#mov     esi, [eax+10h]
		#mov     edx, [ecx+10h]
		#mov     [ecx+10h], esi
		#mov     [eax+10h], edx
		#mov     esi, [eax+20h]
		#mov     edx, [ecx+20h]
		#mov     [ecx+20h], esi
		#mov     [eax+20h], edx
		#mov     esi, [eax+18h]
		#mov     edx, [ecx+18h]
		#mov     [ecx+18h], esi
		#mov     [eax+18h], edx
		#mov     esi, [eax+1Ch]
		#mov     edx, [ecx+1Ch]
		#mov     [ecx+1Ch], esi
		#mov     [eax+1Ch], edx
		#mov     esi, [eax+2Ch]
		#mov     edx, [ecx+2Ch]
		#mov     [ecx+2Ch], esi
		#mov     [eax+2Ch], edx
		#mov     esi, [eax+24h]
		#mov     edx, [ecx+24h]
		#mov     [ecx+24h], esi
		#mov     [eax+24h], edx
		#mov     esi, [eax+28h]
		#mov     edx, [ecx+28h]
		#mov     [ecx+28h], esi
		#mov     [eax+28h], edx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E69F680(self):
		#sub_6E69F680
		gadget = "8B44240433D289501089501CC700010000008B511081E2FFFFFF7F8950088B511081E2FFFFFF7F8950148B511081E2FFFFFF7F428950188B490881E1FFFFFF7F894810C20400"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     edx, edx
		#mov     [eax+10h], edx
		#mov     [eax+1Ch], edx
		#mov     dword ptr [eax], 1
		#mov     edx, [ecx+10h]
		#and     edx, 7FFFFFFFh
		#mov     [eax+8], edx
		#mov     edx, [ecx+10h]
		#and     edx, 7FFFFFFFh
		#mov     [eax+14h], edx
		#mov     edx, [ecx+10h]
		#and     edx, 7FFFFFFFh
		#inc     edx
		#mov     [eax+18h], edx
		#mov     ecx, [ecx+8]
		#and     ecx, 7FFFFFFFh
		#mov     [eax+10h], ecx
		#retn    4


  def test_gadget_sub_6E69F6D0(self):
		#sub_6E69F6D0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B54240C894808668B4C2410C6400C7C895010668B542414668948148B4C240866895016C700DC9B926E894818C21400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_8]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_10]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     dword ptr [eax], offset off_6E929BDC
		#mov     [eax+18h], ecx
		#retn    14h


  def test_gadget_sub_6E69F720(self):
		#sub_6E69F720
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542410894808668B4C2414C6400C7C895010668B542418668948148B4C2408668950168B54240CC7007C9C926E89481889501CC21800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_C]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_10]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_14]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     dword ptr [eax], offset off_6E929C7C
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], edx
		#retn    18h


  def test_gadget_sub_6E69F770(self):
		#sub_6E69F770
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542414894808668B4C2418C6400C7C66894814895010668B54241C33C98948188B4C2408668950168B54240C89481C8B4C2410C700CC9C926E895020894824C21C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_10]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_14]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+14h], cx
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_18]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_C]
		#mov     dword ptr [eax], offset off_6E929CCC
		#mov     [eax+20h], edx
		#mov     [eax+24h], ecx
		#retn    1Ch


  def test_gadget_sub_6E69F7D0(self):
		#sub_6E69F7D0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542414894808668B4C2418C6400C7C66894814895010668B54241C33C98948188B4C2408668950168B54240C89481C8B4C2410C7001C9D926E895020894824C21C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_10]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_14]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+14h], cx
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_18]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_C]
		#mov     dword ptr [eax], offset off_6E929D1C
		#mov     [eax+20h], edx
		#mov     [eax+24h], ecx
		#retn    1Ch


  def test_gadget_sub_6E69F830(self):
		#sub_6E69F830
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542414894808668B4C2418C6400C7C66894814895010668B54241C33C98948188B4C2408668950168B54240C89481C8B4C2410895020894824C7006C9D926EC21C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_10]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_14]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+14h], cx
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_18]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+20h], edx
		#mov     [eax+24h], ecx
		#mov     dword ptr [eax], offset off_6E929D6C
		#retn    1Ch


  def test_gadget_sub_6E69F890(self):
		#sub_6E69F890
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542414894808668B4C2418C6400C7C66894814895010668B54241C33C98948188B4C2408668950168B54240C89481C8B4C2410895020894824C700BC9D926EC21C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_10]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_14]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+14h], cx
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_18]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+20h], edx
		#mov     [eax+24h], ecx
		#mov     dword ptr [eax], offset off_6E929DBC
		#retn    1Ch


  def test_gadget_sub_6E69F8F0(self):
		#sub_6E69F8F0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B54240C894808668B4C2410C6400C7C895010668B542414668948148B4C240866895016C7000C9E926E894818C21400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_8]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_10]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     dword ptr [eax], offset off_6E929E0C
		#mov     [eax+18h], ecx
		#retn    14h


  def test_gadget_sub_6E69F940(self):
		#sub_6E69F940
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542410894808668B4C2414C6400C7C895010668B542418668948148B4C2408668950168B54240CC7005C9E926E89481889501CC21800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_C]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_10]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_14]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     dword ptr [eax], offset off_6E929E5C
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], edx
		#retn    18h


  def test_gadget_sub_6E69F990(self):
		#sub_6E69F990
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542410894808668B4C2414C6400C7C895010668B542418668948148B4C2408668950168B54240CC700AC9E926E89481889501CC21800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_C]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_10]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_14]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     dword ptr [eax], offset off_6E929EAC
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], edx
		#retn    18h


  def test_gadget_sub_6E69F9E0(self):
		#sub_6E69F9E0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542408894808C6400C04895010C740141A000000C7009CA0926EC20800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     byte ptr [eax+0Ch], 4
		#mov     [eax+10h], edx
		#mov     dword ptr [eax+14h], 1Ah
		#mov     dword ptr [eax], offset off_6E92A09C
		#retn    8


  def test_gadget_sub_6E69FAA0(self):
		#sub_6E69FAA0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740181600000088501CC700FCA4926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 16h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A4FC
		#retn    10h


  def test_gadget_sub_6E69FAE0(self):
		#sub_6E69FAE0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740181500000088501CC7004CA5926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 15h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A54C
		#retn    10h


  def test_gadget_sub_6E69FB20(self):
		#sub_6E69FB20
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740181700000088501CC7009CA5926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 17h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A59C
		#retn    10h


  def test_gadget_sub_6E69FB60(self):
		#sub_6E69FB60
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740182800000088501CC74020FFFFFFFFC74024FFFFFFFFC700ECA5926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 28h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax+20h], 0FFFFFFFFh
		#mov     dword ptr [eax+24h], 0FFFFFFFFh
		#mov     dword ptr [eax], offset off_6E92A5EC
		#retn    10h


  def test_gadget_sub_6E69FBB0(self):
		#sub_6E69FBB0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C7C894814C740183000000088501CC74020FFFFFFFFC74024FFFFFFFFC7003CA6926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 30h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax+20h], 0FFFFFFFFh
		#mov     dword ptr [eax+24h], 0FFFFFFFFh
		#mov     dword ptr [eax], offset off_6E92A63C
		#retn    10h


  def test_gadget_sub_6E69FC00(self):
		#sub_6E69FC00
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740180E00000088501CC7008CA6926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 0Eh
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A68C
		#retn    10h


  def test_gadget_sub_6E69FC40(self):
		#sub_6E69FC40
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740181000000088501CC700DCA6926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 10h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A6DC
		#retn    10h


  def test_gadget_sub_6E69FC80(self):
		#sub_6E69FC80
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740181200000088501CC7002CA7926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 12h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A72C
		#retn    10h


  def test_gadget_sub_6E69FCC0(self):
		#sub_6E69FCC0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108A542410C6400C20894814C740181300000088501CC7007CA7926EC21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     dl, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 13h
		#mov     [eax+1Ch], dl
		#mov     dword ptr [eax], offset off_6E92A77C
		#retn    10h


  def test_gadget_sub_6E69FD00(self):
		#sub_6E69FD00
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240C8950108B542410C6400C20C700BCA8926E894814895018C21000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+10h], edx
		#mov     edx, [esp+arg_C]
		#mov     byte ptr [eax+0Ch], 20h
		#mov     dword ptr [eax], offset off_6E92A8BC
		#mov     [eax+14h], ecx
		#mov     [eax+18h], edx
		#retn    10h


  def test_gadget_sub_6E69FD40(self):
		#sub_6E69FD40
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542418894808668B4C241CC6400C7C895010668B542420668948148B4C2408668950168B5424108948188B4C240C89501C8A542414C7005CA9926E894820885024C22000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_14]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_18]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_1C]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_C]
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_8]
		#mov     [eax+1Ch], edx
		#mov     dl, [esp+arg_10]
		#mov     dword ptr [eax], offset off_6E92A95C
		#mov     [eax+20h], ecx
		#mov     [eax+24h], dl
		#retn    20h


  def test_gadget_sub_6E69FDA0(self):
		#sub_6E69FDA0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B5424088948088B4C240CC6400C7CC74010FFFFFFFFC74014FFFFFFFFC700ACA9926E89501889481CC20C00"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_4]
		#mov     [eax+8], ecx
		#mov     ecx, [esp+arg_8]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     dword ptr [eax+10h], 0FFFFFFFFh
		#mov     dword ptr [eax+14h], 0FFFFFFFFh
		#mov     dword ptr [eax], offset off_6E92A9AC
		#mov     [eax+18h], edx
		#mov     [eax+1Ch], ecx
		#retn    0Ch


  def test_gadget_sub_6E69FDE0(self):
		#sub_6E69FDE0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542420894808668B4C2424C6400C7C895010668B54242866894814668950168B54240C33C98948188B4C24088950208B50283354241089481C8B4C241481E2FFFFFF3F3150280FB6502C8948248A4C241C80E10180E2FC02C90ACA8A54241880E2010ACAC700FCA9926E88482CC22800"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_1C]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_20]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_24]
		#mov     [eax+14h], cx
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+20h], edx
		#mov     edx, [eax+28h]
		#xor     edx, [esp+arg_C]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_10]
		#and     edx, 3FFFFFFFh
		#xor     [eax+28h], edx
		#movzx   edx, byte ptr [eax+2Ch]
		#mov     [eax+24h], ecx
		#mov     cl, [esp+arg_18]
		#and     cl, 1
		#and     dl, 0FCh
		#add     cl, cl
		#or      cl, dl
		#mov     dl, [esp+arg_14]
		#and     dl, 1
		#or      cl, dl
		#mov     dword ptr [eax], offset off_6E92A9FC
		#mov     [eax+2Ch], cl
		#retn    28h


  def test_gadget_sub_6E69FE70(self):
		#sub_6E69FE70
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B54241C894808668B4C2420C6400C7C895010668B542424668948148B4C2408668950168B54240C8948188B4C241089501C8A5424188948200FB6482480E20180E1FC02D20AD18A4C241480E1010AD1C7004CAA926E885024C22400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_18]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_1C]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_20]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+1Ch], edx
		#mov     dl, [esp+arg_14]
		#mov     [eax+20h], ecx
		#movzx   ecx, byte ptr [eax+24h]
		#and     dl, 1
		#and     cl, 0FCh
		#add     dl, dl
		#or      dl, cl
		#mov     cl, [esp+arg_10]
		#and     cl, 1
		#or      dl, cl
		#mov     dword ptr [eax], offset off_6E92AA4C
		#mov     [eax+24h], dl
		#retn    24h


  def test_gadget_sub_6E69FEE0(self):
		#sub_6E69FEE0
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B542418894808668B4C241CC6400C7C895010668B542420668948148B4C2408668950168B54240C8948188B4C241089501C8A542414C7009CAA926E894820885024C22000"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_14]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_18]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_1C]
		#mov     [eax+14h], cx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_C]
		#mov     [eax+1Ch], edx
		#mov     dl, [esp+arg_10]
		#mov     dword ptr [eax], offset off_6E92AA9C
		#mov     [eax+20h], ecx
		#mov     [eax+24h], dl
		#retn    20h


  def test_gadget_sub_6E69FF40(self):
		#sub_6E69FF40
		gadget = "8BC18B4C2404C7006C96926E8B118950048B490C8B54241C894808668B4C2420C6400C7C66894814895010668B542424668950168B54240C33C98948188B4C240889481C8B4C24148950208B5028335424108948248A482C324C241881E2FFFFFF7F31502880E10130482CC700ECAA926EC22400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92966C
		#mov     edx, [ecx]
		#mov     [eax+4], edx
		#mov     ecx, [ecx+0Ch]
		#mov     edx, [esp+arg_18]
		#mov     [eax+8], ecx
		#mov     cx, [esp+arg_1C]
		#mov     byte ptr [eax+0Ch], 7Ch
		#mov     [eax+14h], cx
		#mov     [eax+10h], edx
		#mov     dx, [esp+arg_20]
		#mov     [eax+16h], dx
		#mov     edx, [esp+arg_8]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     ecx, [esp+arg_4]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [esp+arg_10]
		#mov     [eax+20h], edx
		#mov     edx, [eax+28h]
		#xor     edx, [esp+arg_C]
		#mov     [eax+24h], ecx
		#mov     cl, [eax+2Ch]
		#xor     cl, [esp+arg_14]
		#and     edx, 7FFFFFFFh
		#xor     [eax+28h], edx
		#and     cl, 1
		#xor     [eax+2Ch], cl
		#mov     dword ptr [eax], offset off_6E92AAEC
		#retn    24h


  def test_gadget_sub_6E6A0120(self):
		#sub_6E6A0120
		gadget = "8B442404C74004FDFFFFFFC70000000000C20800"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     dword ptr [eax+4], 0FFFFFFFDh
		#mov     dword ptr [eax], 0
		#retn    8


  def test_gadget_sub_6E6A3130(self):
		#sub_6E6A3130
		gadget = "8B4424048B5424088981600400008B44240C8981680400008B44241C8991640400008B916C040000568B3089B16C0400008B700489108B917004000089B1700400008B70088950048B917404000089B1740400008B700C8950088B917804000089B1780400008B701089500C8B917C04000089B17C0400008950108B5424148B4424188991800400008B54241C89813C0400008991840400005EC21C00"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     edx, [esp+arg_4]
		#mov     [ecx+460h], eax
		#mov     eax, [esp+arg_8]
		#mov     [ecx+468h], eax
		#mov     eax, [esp+arg_18]
		#mov     [ecx+464h], edx
		#mov     edx, [ecx+46Ch]
		#push    esi
		#mov     esi, [eax]
		#mov     [ecx+46Ch], esi
		#mov     esi, [eax+4]
		#mov     [eax], edx
		#mov     edx, [ecx+470h]
		#mov     [ecx+470h], esi
		#mov     esi, [eax+8]
		#mov     [eax+4], edx
		#mov     edx, [ecx+474h]
		#mov     [ecx+474h], esi
		#mov     esi, [eax+0Ch]
		#mov     [eax+8], edx
		#mov     edx, [ecx+478h]
		#mov     [ecx+478h], esi
		#mov     esi, [eax+10h]
		#mov     [eax+0Ch], edx
		#mov     edx, [ecx+47Ch]
		#mov     [ecx+47Ch], esi
		#mov     [eax+10h], edx
		#mov     edx, [esp+4+arg_C]
		#mov     eax, [esp+4+arg_10]
		#mov     [ecx+480h], edx
		#mov     edx, [esp+4+arg_14]
		#mov     [ecx+43Ch], eax
		#mov     [ecx+484h], edx
		#pop     esi
		#retn    1Ch


  def test_gadget_sub_6E6D3430(self):
		#sub_6E6D3430
		gadget = "8BC10FB65004568B7424088B0E890832560480E2013050040FB656048A480432D180E20232D1885004668B4E08668948088B56088950088B4E088948088B56088950088B4E0C89480C8B56108950108B4E148948140FB656088850088B4E188948188B4E1C89481C8B56208950208B4E248948245EC20400"
		self.do(gadget)

		#mov     eax, ecx
		#movzx   edx, byte ptr [eax+4]
		#push    esi
		#mov     esi, [esp+4+arg_0]
		#mov     ecx, [esi]
		#mov     [eax], ecx
		#xor     dl, [esi+4]
		#and     dl, 1
		#xor     [eax+4], dl
		#movzx   edx, byte ptr [esi+4]
		#mov     cl, [eax+4]
		#xor     dl, cl
		#and     dl, 2
		#xor     dl, cl
		#mov     [eax+4], dl
		#mov     cx, [esi+8]
		#mov     [eax+8], cx
		#mov     edx, [esi+8]
		#mov     [eax+8], edx
		#mov     ecx, [esi+8]
		#mov     [eax+8], ecx
		#mov     edx, [esi+8]
		#mov     [eax+8], edx
		#mov     ecx, [esi+0Ch]
		#mov     [eax+0Ch], ecx
		#mov     edx, [esi+10h]
		#mov     [eax+10h], edx
		#mov     ecx, [esi+14h]
		#mov     [eax+14h], ecx
		#movzx   edx, byte ptr [esi+8]
		#mov     [eax+8], dl
		#mov     ecx, [esi+18h]
		#mov     [eax+18h], ecx
		#mov     ecx, [esi+1Ch]
		#mov     [eax+1Ch], ecx
		#mov     edx, [esi+20h]
		#mov     [eax+20h], edx
		#mov     ecx, [esi+24h]
		#mov     [eax+24h], ecx
		#pop     esi
		#retn    4


  def test_gadget_sub_6E6D3770(self):
		#sub_6E6D3770
		gadget = "8B81A40000008B91A0000000568BF0C1EE10C1E01003F203C68981A400000003C2F681A40000003F8981A0000000B8000000000F94C05EC3"
		self.do(gadget)

		#mov     eax, [ecx+0A4h]
		#mov     edx, [ecx+0A0h]
		#push    esi
		#mov     esi, eax
		#shr     esi, 10h
		#shl     eax, 10h
		#add     esi, edx
		#add     eax, esi
		#mov     [ecx+0A4h], eax
		#add     eax, edx
		#test    byte ptr [ecx+0A4h], 3Fh
		#mov     [ecx+0A0h], eax
		#mov     eax, 0
		#setz    al
		#pop     esi
		#retn


  def test_gadget__Java_com_sun_webkit_WatchdogTimer_twkFire16(self):
		#_Java_com_sun_webkit_WatchdogTimer_twkFire16
		gadget = "8B44240CC60001C21000"
		self.do(gadget)

		#mov     eax, [esp+arg_8]
		#mov     byte ptr [eax], 1
		#retn    10h


  def test_gadget_sub_6E6DE690(self):
		#sub_6E6DE690
		gadget = "8B410483C008C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#add     eax, 8
		#retn


  def test_gadget_0facetlocalestdIAEIZ_3(self):
		#0facetlocalestdIAEIZ_3
		gadget = "8BC18B4C2404C700FCB6926E894804C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, [esp+arg_0]
		#mov     dword ptr [eax], offset off_6E92B6FC
		#mov     [eax+4], ecx
		#retn    4


  def test_gadget_sub_6E6E1EE0(self):
		#sub_6E6E1EE0
		gadget = "C701FCB6926EC3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_6E92B6FC
		#retn


  def test_gadget_sub_6E6E3840(self):
		#sub_6E6E3840
		gadget = "518B44240833C98D5008890C248910C740040100000089481059C3"
		self.do(gadget)

		#push    ecx
		#mov     eax, [esp+4+arg_0]
		#xor     ecx, ecx
		#lea     edx, [eax+8]
		#mov     [esp+4+var_4], ecx
		#mov     [eax], edx
		#mov     dword ptr [eax+4], 1
		#mov     [eax+10h], ecx
		#pop     ecx
		#retn


  def test_gadget_sub_6E6E5900(self):
		#sub_6E6E5900
		gadget = "8B4C240C8B4424082BC88948FCC3"
		self.do(gadget)

		#mov     ecx, [esp+arg_8]
		#mov     eax, [esp+arg_4]
		#sub     ecx, eax
		#mov     [eax-4], ecx
		#retn


  def test_gadget_sub_6E6E9A10(self):
		#sub_6E6E9A10
		gadget = "D9EE8BC1D95804C70000000000C7400800000000C3"
		self.do(gadget)

		#fldz
		#mov     eax, ecx
		#fstp    dword ptr [eax+4]
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+8], 0
		#retn


  def test_gadget_sub_6E6E9C50(self):
		#sub_6E6E9C50
		gadget = "8B44240433C9C74004FAFFFFFF890889480889480C66894810C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#xor     ecx, ecx
		#mov     dword ptr [eax+4], 0FFFFFFFAh
		#mov     [eax], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], cx
		#retn


  def test_gadget_sub_6E6EAAF0(self):
		#sub_6E6EAAF0
		gadget = "8B4424088B4840BAD01E686E2BD18951FC0FBF48088B5044C74411FCEFBEE7D10FBF500E32C9568B7044884C32FF0FBF50108B7044884C32FF0FBF50148B48402BCA0FBF500A0350445E2BCA894AFCC3"
		self.do(gadget)

		#mov     eax, [esp+arg_4]
		#mov     ecx, [eax+40h]
		#mov     edx, offset sub_6E681ED0
		#sub     edx, ecx
		#mov     [ecx-4], edx
		#movsx   ecx, word ptr [eax+8]
		#mov     edx, [eax+44h]
		#mov     dword ptr [ecx+edx-4], 0D1E7BEEFh
		#movsx   edx, word ptr [eax+0Eh]
		#xor     cl, cl
		#push    esi
		#mov     esi, [eax+44h]
		#mov     [edx+esi-1], cl
		#movsx   edx, word ptr [eax+10h]
		#mov     esi, [eax+44h]
		#mov     [edx+esi-1], cl
		#movsx   edx, word ptr [eax+14h]
		#mov     ecx, [eax+40h]
		#sub     ecx, edx
		#movsx   edx, word ptr [eax+0Ah]
		#add     edx, [eax+44h]
		#pop     esi
		#sub     ecx, edx
		#mov     [edx-4], ecx
		#retn


  def test_gadget_sub_6E6F3EE0(self):
		#sub_6E6F3EE0
		gadget = "6AFF68090F7D6E64A1000000005051A1F44AA66E33C4508D44240864A300000000C7442404000000008B442418C70000000000C74004FFFFFF7F8B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7D0F09
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#mov     [esp+14h+var_10], 0
		#mov     eax, [esp+14h+arg_0]
		#mov     dword ptr [eax], 0
		#mov     dword ptr [eax+4], 7FFFFFFFh
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E6F4CC0(self):
		#sub_6E6F4CC0
		gadget = "83C8FF018138130000018124130000C3"
		self.do(gadget)

		#or      eax, 0FFFFFFFFh
		#add     [ecx+1338h], eax
		#add     [ecx+1324h], eax
		#retn


  def test_gadget_sub_6E6FAF10(self):
		#sub_6E6FAF10
		gadget = "6AFF6879CB7D6E64A1000000005051A1F44AA66E33C4508D44240864A30000000033C9894C24048B442418C700FFFFFF7F8948048B4C240864890D000000005983C410C3"
		self.do(gadget)

		#push    0FFFFFFFFh
		#push    offset sub_6E7DCB79
		#mov     eax, large fs:0
		#push    eax
		#push    ecx
		#mov     eax, ___security_cookie
		#xor     eax, esp
		#push    eax
		#lea     eax, [esp+14h+var_C]
		#mov     large fs:0, eax
		#xor     ecx, ecx
		#mov     [esp+14h+var_10], ecx
		#mov     eax, [esp+14h+arg_0]
		#mov     dword ptr [eax], 7FFFFFFFh
		#mov     [eax+4], ecx
		#mov     ecx, [esp+14h+var_C]
		#mov     large fs:0, ecx
		#pop     ecx
		#add     esp, 10h
		#retn


  def test_gadget_sub_6E707100(self):
		#sub_6E707100
		gadget = "83EC088B098B41E88B49EC250000FFFF8B90340400008B824C480000894C24048B887C4900008B44240C33D285C90F95C2890883C2FA89500483C408C20400"
		self.do(gadget)

		#sub     esp, 8
		#mov     ecx, [ecx]
		#mov     eax, [ecx-18h]
		#mov     ecx, [ecx-14h]
		#and     eax, 0FFFF0000h
		#mov     edx, [eax+434h]
		#mov     eax, [edx+484Ch]
		#mov     [esp+8+var_4], ecx
		#mov     ecx, [eax+497Ch]
		#mov     eax, [esp+8+arg_0]
		#xor     edx, edx
		#test    ecx, ecx
		#setnz   dl
		#mov     [eax], ecx
		#add     edx, 0FFFFFFFAh
		#mov     [eax+4], edx
		#add     esp, 8
		#retn    4


  def test_gadget_sub_6E72D580(self):
		#sub_6E72D580
		gadget = "8B4424048B48108B5424088B849198020000C3"
		self.do(gadget)

		#mov     eax, [esp+arg_0]
		#mov     ecx, [eax+10h]
		#mov     edx, [esp+arg_4]
		#mov     eax, [ecx+edx*4+298h]
		#retn


  def test_gadget_sub_6E72E6F4(self):
		#sub_6E72E6F4
		gadget = "A1D8B2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B2D8
		#retn


  def test_gadget_unknown_libname_26(self):
		#unknown_libname_26
		gadget = "8BFF558BEC8B45088B550C89108948045DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [ebp+arg_4]
		#mov     [eax], edx
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_6E72EA5B(self):
		#sub_6E72EA5B
		gadget = "8B4104C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#retn


  def test_gadget_sub_6E72EA5F(self):
		#sub_6E72EA5F
		gadget = "8B4108C3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#retn


  def test_gadget_sub_6E72EA63(self):
		#sub_6E72EA63
		gadget = "B87C48A66EC3"
		self.do(gadget)

		#mov     eax, offset off_6EA6487C
		#retn


  def test_gadget_do_widenctypeDstdMBEDDZ_0(self):
		#do_widenctypeDstdMBEDDZ_0
		gadget = "8BFF558BEC8A45085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     al, [ebp+arg_0]
		#pop     ebp
		#retn    4


  def test_gadget_do_narrowctypeDstdMBEDDDZ_0(self):
		#do_narrowctypeDstdMBEDDDZ_0
		gadget = "8BFF558BEC8A45085DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     al, [ebp+arg_0]
		#pop     ebp
		#retn    8


  def test_gadget_sub_6E72EE56(self):
		#sub_6E72EE56
		gadget = "83C8FFC20400"
		self.do(gadget)

		#or      eax, 0FFFFFFFFh
		#retn    4


  def test_gadget_sub_6E72EE5C(self):
		#sub_6E72EE5C
		gadget = "33C033D2C3"
		self.do(gadget)

		#xor     eax, eax
		#xor     edx, edx
		#retn


  def test_gadget_sub_6E72EE61(self):
		#sub_6E72EE61
		gadget = "83C8FFC3"
		self.do(gadget)

		#or      eax, 0FFFFFFFFh
		#retn


  def test_gadget_sub_6E72EE65(self):
		#sub_6E72EE65
		gadget = "8BC1C20C00"
		self.do(gadget)

		#mov     eax, ecx
		#retn    0Ch


  def test_gadget_sub_6E72EE6A(self):
		#sub_6E72EE6A
		gadget = "33C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget_nullsub_9(self):
		#nullsub_9
		gadget = "C20400"
		self.do(gadget)

		#retn    4


  def test_gadget_unknown_libname_29(self):
		#unknown_libname_29
		gadget = "8BFF558BEC8B45088B0DC0CE926E89088B0DC4CE926E89480433C989480889480C8948105DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, ds:dword_6E92CEC0
		#mov     [eax], ecx
		#mov     ecx, ds:dword_6E92CEC4
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#pop     ebp
		#retn    14h


  def test_gadget_unknown_libname_30(self):
		#unknown_libname_30
		gadget = "8BFF558BEC8B45088B0DC0CE926E89088B0DC4CE926E89480433C989480889480C8948105DC22000"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, ds:dword_6E92CEC0
		#mov     [eax], ecx
		#mov     ecx, ds:dword_6E92CEC4
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#pop     ebp
		#retn    20h


  def test_gadget_unknown_libname_31(self):
		#unknown_libname_31
		gadget = "8D51188951208D511C8951248D51288951308D41088941108D512C89513433D28D410C89411489108B412489108B413489108B411089108B412089108B41308910C3"
		self.do(gadget)

		#lea     edx, [ecx+18h]
		#mov     [ecx+20h], edx
		#lea     edx, [ecx+1Ch]
		#mov     [ecx+24h], edx
		#lea     edx, [ecx+28h]
		#mov     [ecx+30h], edx
		#lea     eax, [ecx+8]
		#mov     [ecx+10h], eax
		#lea     edx, [ecx+2Ch]
		#mov     [ecx+34h], edx
		#xor     edx, edx
		#lea     eax, [ecx+0Ch]
		#mov     [ecx+14h], eax
		#mov     [eax], edx
		#mov     eax, [ecx+24h]
		#mov     [eax], edx
		#mov     eax, [ecx+34h]
		#mov     [eax], edx
		#mov     eax, [ecx+10h]
		#mov     [eax], edx
		#mov     eax, [ecx+20h]
		#mov     [eax], edx
		#mov     eax, [ecx+30h]
		#mov     [eax], edx
		#retn


  def test_gadget_sub_6E72F2D4(self):
		#sub_6E72F2D4
		gadget = "B001C3"
		self.do(gadget)

		#mov     al, 1
		#retn


  def test_gadget_sub_6E72F2D7(self):
		#sub_6E72F2D7
		gadget = "33C040C3"
		self.do(gadget)

		#xor     eax, eax
		#inc     eax
		#retn


  def test_gadget_unknown_libname_34(self):
		#unknown_libname_34
		gadget = "8BFF558BEC8B45148B4D0C89088B45208B4D186A038908585DC21C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_C]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax], ecx
		#mov     eax, [ebp+arg_18]
		#mov     ecx, [ebp+arg_10]
		#push    3
		#mov     [eax], ecx
		#pop     eax
		#pop     ebp
		#retn    1Ch


  def test_gadget_do_unshiftcodecvtDDHstdMBEHAAHPAD1AAPADZ(self):
		#do_unshiftcodecvtDDHstdMBEHAAHPAD1AAPADZ
		gadget = "8BFF558BEC8B45148B4D0C6A038908585DC21000"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_C]
		#mov     ecx, [ebp+arg_4]
		#push    3
		#mov     [eax], ecx
		#pop     eax
		#pop     ebp
		#retn    10h


  def test_gadget___catch2YAPAXIABUnothrow_tstdZ0(self):
		#__catch2YAPAXIABUnothrow_tstdZ0
		gadget = "8365EC00B8BC06736EC3"
		self.do(gadget)

		#and     dword ptr [ebp-14h], 0
		#mov     eax, offset loc_6E7306BC
		#retn


  def test_gadget___EH_prolog3(self):
		#__EH_prolog3
		gadget = "5064FF35000000008D44240C2B64240C53565789288BE8A1F44AA66E33C550FF75FCC745FCFFFFFFFF8D45F464A300000000C3"
		self.do(gadget)

		#push    eax
		#push    large dword ptr fs:0
		#lea     eax, [esp+8+arg_0]
		#sub     esp, [esp+0Ch]
		#push    ebx
		#push    esi
		#push    edi
		#mov     [eax], ebp
		#mov     ebp, eax
		#mov     eax, ___security_cookie
		#xor     eax, ebp
		#push    eax
		#push    dword ptr [ebp-4]
		#mov     dword ptr [ebp-4], 0FFFFFFFFh
		#lea     eax, [ebp-0Ch]
		#mov     large fs:0, eax
		#retn


  def test_gadget___EH_prolog3_catch(self):
		#__EH_prolog3_catch
		gadget = "5064FF35000000008D44240C2B64240C53565789288BE8A1F44AA66E33C5508965F0FF75FCC745FCFFFFFFFF8D45F464A300000000C3"
		self.do(gadget)

		#push    eax
		#push    large dword ptr fs:0
		#lea     eax, [esp+8+arg_0]
		#sub     esp, [esp+0Ch]
		#push    ebx
		#push    esi
		#push    edi
		#mov     [eax], ebp
		#mov     ebp, eax
		#mov     eax, ___security_cookie
		#xor     eax, ebp
		#push    eax
		#mov     [ebp-10h], esp
		#push    dword ptr [ebp-4]
		#mov     dword ptr [ebp-4], 0FFFFFFFFh
		#lea     eax, [ebp-0Ch]
		#mov     large fs:0, eax
		#retn


  def test_gadget___EH_prolog3_GS(self):
		#__EH_prolog3_GS
		gadget = "5064FF35000000008D44240C2B64240C53565789288BE8A1F44AA66E33C5508945F0FF75FCC745FCFFFFFFFF8D45F464A300000000C3"
		self.do(gadget)

		#push    eax
		#push    large dword ptr fs:0
		#lea     eax, [esp+8+arg_0]
		#sub     esp, [esp+0Ch]
		#push    ebx
		#push    esi
		#push    edi
		#mov     [eax], ebp
		#mov     ebp, eax
		#mov     eax, ___security_cookie
		#xor     eax, ebp
		#push    eax
		#mov     [ebp-10h], eax
		#push    dword ptr [ebp-4]
		#mov     dword ptr [ebp-4], 0FFFFFFFFh
		#lea     eax, [ebp-0Ch]
		#mov     large fs:0, eax
		#retn


  def test_gadget___EH_epilog3(self):
		#__EH_epilog3
		gadget = "8B4DF464890D00000000595F5F5E5B8BE55D51C3"
		self.do(gadget)

		#mov     ecx, [ebp-0Ch]
		#mov     large fs:0, ecx
		#pop     ecx
		#pop     edi
		#pop     edi
		#pop     esi
		#pop     ebx
		#mov     esp, ebp
		#pop     ebp
		#push    ecx
		#retn


  def test_gadget___EH_epilog3_GS(self):
		#__EH_epilog3_GS
		gadget = "8B4DF033CDE8A7F2FFFFE9DDFFFFFF"
		self.do(gadget)

		#mov     ecx, [ebp-10h]
		#xor     ecx, ebp
		#call    __security_check_cookie4; __security_check_cookie(x)
		#jmp     __EH_epilog3


  def test_gadget___SEH_prolog4(self):
		#__SEH_prolog4
		gadget = "68840E736E64FF35000000008B442410896C24108D6C24102BE0535657A1F44AA66E3145FC33C5508965E8FF75F88B45FCC745FCFEFFFFFF8945F88D45F064A300000000C3"
		self.do(gadget)

		#push    offset __except_handler4
		#push    large dword ptr fs:0
		#mov     eax, [esp+8+arg_4]
		#mov     [esp+8+arg_4], ebp
		#lea     ebp, [esp+8+arg_4]
		#sub     esp, eax
		#push    ebx
		#push    esi
		#push    edi
		#mov     eax, ___security_cookie
		#xor     [ebp-4], eax
		#xor     eax, ebp
		#push    eax
		#mov     [ebp-18h], esp
		#push    dword ptr [ebp-8]
		#mov     eax, [ebp-4]
		#mov     dword ptr [ebp-4], 0FFFFFFFEh
		#mov     [ebp-8], eax
		#lea     eax, [ebp-10h]
		#mov     large fs:0, eax
		#retn


  def test_gadget___SEH_epilog4(self):
		#__SEH_epilog4
		gadget = "8B4DF064890D00000000595F5F5E5B8BE55D51C3"
		self.do(gadget)

		#mov     ecx, [ebp-10h]
		#mov     large fs:0, ecx
		#pop     ecx
		#pop     edi
		#pop     edi
		#pop     esi
		#pop     ebx
		#mov     esp, ebp
		#pop     ebp
		#push    ecx
		#retn


  def test_gadget_sub_6E731610(self):
		#sub_6E731610
		gadget = "A1084CA66E83E0FEA3084CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA64C08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA64C08, eax
		#retn


  def test_gadget_sub_6E731678(self):
		#sub_6E731678
		gadget = "A1104CA66E83E0FEA3104CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA64C10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA64C10, eax
		#retn


  def test_gadget_sub_6E7316B0(self):
		#sub_6E7316B0
		gadget = "A16451A66E83E0FEA36451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65164
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65164, eax
		#retn


  def test_gadget_sub_6E731730(self):
		#sub_6E731730
		gadget = "A16C51A66E83E0FEA36C51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6516C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6516C, eax
		#retn


  def test_gadget_sub_6E731960(self):
		#sub_6E731960
		gadget = "A17451A66E83E0FEA37451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65174
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65174, eax
		#retn


  def test_gadget_sub_6E731C20(self):
		#sub_6E731C20
		gadget = "A17C51A66E83E0FEA37C51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6517C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6517C, eax
		#retn


  def test_gadget_sub_6E731E50(self):
		#sub_6E731E50
		gadget = "A18451A66E83E0FEA38451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65184
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65184, eax
		#retn


  def test_gadget_sub_6E731F20(self):
		#sub_6E731F20
		gadget = "A18C51A66E83E0FEA38C51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6518C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6518C, eax
		#retn


  def test_gadget_sub_6E731FB0(self):
		#sub_6E731FB0
		gadget = "A19451A66E83E0FEA39451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65194
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65194, eax
		#retn


  def test_gadget_sub_6E731FF0(self):
		#sub_6E731FF0
		gadget = "A19C51A66E83E0FEA39C51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6519C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6519C, eax
		#retn


  def test_gadget_sub_6E7321C0(self):
		#sub_6E7321C0
		gadget = "A1A451A66E83E0FEA3A451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651A4, eax
		#retn


  def test_gadget_sub_6E732280(self):
		#sub_6E732280
		gadget = "A1AC51A66E83E0FEA3AC51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651AC, eax
		#retn


  def test_gadget_sub_6E732380(self):
		#sub_6E732380
		gadget = "A1B451A66E83E0FEA3B451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651B4, eax
		#retn


  def test_gadget_sub_6E732410(self):
		#sub_6E732410
		gadget = "A1BC51A66E83E0FEA3BC51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651BC, eax
		#retn


  def test_gadget_sub_6E732440(self):
		#sub_6E732440
		gadget = "A1C451A66E83E0FEA3C451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651C4, eax
		#retn


  def test_gadget_sub_6E732470(self):
		#sub_6E732470
		gadget = "A1CC51A66E83E0FEA3CC51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651CC, eax
		#retn


  def test_gadget_sub_6E732570(self):
		#sub_6E732570
		gadget = "A1D451A66E83E0FEA3D451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651D4, eax
		#retn


  def test_gadget_sub_6E7327B0(self):
		#sub_6E7327B0
		gadget = "A1DC51A66E83E0FEA3DC51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651DC, eax
		#retn


  def test_gadget_sub_6E732810(self):
		#sub_6E732810
		gadget = "A1E451A66E83E0FEA3E451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651E4, eax
		#retn


  def test_gadget_sub_6E7328A0(self):
		#sub_6E7328A0
		gadget = "A1EC51A66E83E0FEA3EC51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651EC, eax
		#retn


  def test_gadget_sub_6E732FC0(self):
		#sub_6E732FC0
		gadget = "A1F451A66E83E0FEA3F451A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651F4, eax
		#retn


  def test_gadget_sub_6E733020(self):
		#sub_6E733020
		gadget = "A1FC51A66E83E0FEA3FC51A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA651FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA651FC, eax
		#retn


  def test_gadget_sub_6E7331A0(self):
		#sub_6E7331A0
		gadget = "A10452A66E83E0FEA30452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65204
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65204, eax
		#retn


  def test_gadget_sub_6E733230(self):
		#sub_6E733230
		gadget = "A10C52A66E83E0FEA30C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6520C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6520C, eax
		#retn


  def test_gadget_sub_6E733810(self):
		#sub_6E733810
		gadget = "A11452A66E83E0FEA31452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65214
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65214, eax
		#retn


  def test_gadget_sub_6E733A40(self):
		#sub_6E733A40
		gadget = "A11C52A66E83E0FEA31C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6521C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6521C, eax
		#retn


  def test_gadget_sub_6E733CF0(self):
		#sub_6E733CF0
		gadget = "A12452A66E83E0FEA32452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65224
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65224, eax
		#retn


  def test_gadget_sub_6E733E20(self):
		#sub_6E733E20
		gadget = "A12C52A66E83E0FEA32C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6522C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6522C, eax
		#retn


  def test_gadget_sub_6E733F10(self):
		#sub_6E733F10
		gadget = "A13452A66E83E0FEA33452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65234
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65234, eax
		#retn


  def test_gadget_sub_6E733F40(self):
		#sub_6E733F40
		gadget = "A13C52A66E83E0FEA33C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6523C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6523C, eax
		#retn


  def test_gadget_sub_6E7341B0(self):
		#sub_6E7341B0
		gadget = "A14452A66E83E0FEA34452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65244
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65244, eax
		#retn


  def test_gadget_sub_6E734240(self):
		#sub_6E734240
		gadget = "A14C52A66E83E0FEA34C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6524C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6524C, eax
		#retn


  def test_gadget_sub_6E7342D0(self):
		#sub_6E7342D0
		gadget = "A15452A66E83E0FEA35452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65254
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65254, eax
		#retn


  def test_gadget_sub_6E734400(self):
		#sub_6E734400
		gadget = "A15C52A66E83E0FEA35C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6525C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6525C, eax
		#retn


  def test_gadget_sub_6E734430(self):
		#sub_6E734430
		gadget = "A16452A66E83E0FEA36452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65264
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65264, eax
		#retn


  def test_gadget_sub_6E734640(self):
		#sub_6E734640
		gadget = "A16C52A66E83E0FEA36C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6526C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6526C, eax
		#retn


  def test_gadget_sub_6E734770(self):
		#sub_6E734770
		gadget = "A17452A66E83E0FEA37452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65274
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65274, eax
		#retn


  def test_gadget_sub_6E734890(self):
		#sub_6E734890
		gadget = "A17C52A66E83E0FEA37C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6527C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6527C, eax
		#retn


  def test_gadget_sub_6E734A20(self):
		#sub_6E734A20
		gadget = "A18452A66E83E0FEA38452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65284
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65284, eax
		#retn


  def test_gadget_sub_6E734A50(self):
		#sub_6E734A50
		gadget = "A18C52A66E83E0FEA38C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6528C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6528C, eax
		#retn


  def test_gadget_sub_6E734B10(self):
		#sub_6E734B10
		gadget = "A19452A66E83E0FEA39452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65294
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65294, eax
		#retn


  def test_gadget_sub_6E734C20(self):
		#sub_6E734C20
		gadget = "A19C52A66E83E0FEA39C52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6529C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6529C, eax
		#retn


  def test_gadget_sub_6E734E70(self):
		#sub_6E734E70
		gadget = "A1A452A66E83E0FEA3A452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652A4, eax
		#retn


  def test_gadget_sub_6E734F70(self):
		#sub_6E734F70
		gadget = "A1AC52A66E83E0FEA3AC52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652AC, eax
		#retn


  def test_gadget_sub_6E735330(self):
		#sub_6E735330
		gadget = "A1B452A66E83E0FEA3B452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652B4, eax
		#retn


  def test_gadget_sub_6E7355E0(self):
		#sub_6E7355E0
		gadget = "A1BC52A66E83E0FEA3BC52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652BC, eax
		#retn


  def test_gadget_sub_6E7356A0(self):
		#sub_6E7356A0
		gadget = "A1C452A66E83E0FEA3C452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652C4, eax
		#retn


  def test_gadget_sub_6E7358A0(self):
		#sub_6E7358A0
		gadget = "A1CC52A66E83E0FEA3CC52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652CC, eax
		#retn


  def test_gadget_sub_6E735C00(self):
		#sub_6E735C00
		gadget = "A1D452A66E83E0FEA3D452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652D4, eax
		#retn


  def test_gadget_sub_6E735DB0(self):
		#sub_6E735DB0
		gadget = "A1DC52A66E83E0FEA3DC52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652DC, eax
		#retn


  def test_gadget_sub_6E735E40(self):
		#sub_6E735E40
		gadget = "A1E452A66E83E0FEA3E452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652E4, eax
		#retn


  def test_gadget_sub_6E735EB0(self):
		#sub_6E735EB0
		gadget = "A1EC52A66E83E0FEA3EC52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652EC, eax
		#retn


  def test_gadget_sub_6E735EE0(self):
		#sub_6E735EE0
		gadget = "A1F452A66E83E0FEA3F452A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652F4, eax
		#retn


  def test_gadget_sub_6E735F70(self):
		#sub_6E735F70
		gadget = "A1FC52A66E83E0FEA3FC52A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA652FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA652FC, eax
		#retn


  def test_gadget_sub_6E7360C0(self):
		#sub_6E7360C0
		gadget = "A10453A66E83E0FEA30453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65304
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65304, eax
		#retn


  def test_gadget_sub_6E736150(self):
		#sub_6E736150
		gadget = "A10C53A66E83E0FEA30C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6530C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6530C, eax
		#retn


  def test_gadget_sub_6E7362A0(self):
		#sub_6E7362A0
		gadget = "A11453A66E83E0FEA31453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65314
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65314, eax
		#retn


  def test_gadget_sub_6E736330(self):
		#sub_6E736330
		gadget = "A11C53A66E83E0FEA31C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6531C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6531C, eax
		#retn


  def test_gadget_sub_6E736360(self):
		#sub_6E736360
		gadget = "A12453A66E83E0FEA32453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65324
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65324, eax
		#retn


  def test_gadget_sub_6E7364B0(self):
		#sub_6E7364B0
		gadget = "A12C53A66E83E0FEA32C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6532C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6532C, eax
		#retn


  def test_gadget_sub_6E736510(self):
		#sub_6E736510
		gadget = "A13453A66E83E0FEA33453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65334
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65334, eax
		#retn


  def test_gadget_sub_6E736570(self):
		#sub_6E736570
		gadget = "A13C53A66E83E0FEA33C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6533C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6533C, eax
		#retn


  def test_gadget_sub_6E736600(self):
		#sub_6E736600
		gadget = "A14453A66E83E0FEA34453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65344
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65344, eax
		#retn


  def test_gadget_sub_6E736660(self):
		#sub_6E736660
		gadget = "A14C53A66E83E0FEA34C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6534C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6534C, eax
		#retn


  def test_gadget_sub_6E736A00(self):
		#sub_6E736A00
		gadget = "A15453A66E83E0FEA35453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65354
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65354, eax
		#retn


  def test_gadget_sub_6E736A90(self):
		#sub_6E736A90
		gadget = "A15C53A66E83E0FEA35C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6535C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6535C, eax
		#retn


  def test_gadget_sub_6E736AC0(self):
		#sub_6E736AC0
		gadget = "A16453A66E83E0FEA36453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65364
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65364, eax
		#retn


  def test_gadget_sub_6E736B20(self):
		#sub_6E736B20
		gadget = "A16C53A66E83E0FEA36C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6536C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6536C, eax
		#retn


  def test_gadget_sub_6E736B80(self):
		#sub_6E736B80
		gadget = "A17453A66E83E0FEA37453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65374
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65374, eax
		#retn


  def test_gadget_sub_6E736C10(self):
		#sub_6E736C10
		gadget = "A17C53A66E83E0FEA37C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6537C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6537C, eax
		#retn


  def test_gadget_sub_6E736CA0(self):
		#sub_6E736CA0
		gadget = "A18453A66E83E0FEA38453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65384
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65384, eax
		#retn


  def test_gadget_sub_6E736CD0(self):
		#sub_6E736CD0
		gadget = "A18C53A66E83E0FEA38C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6538C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6538C, eax
		#retn


  def test_gadget_sub_6E736D30(self):
		#sub_6E736D30
		gadget = "A19453A66E83E0FEA39453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65394
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65394, eax
		#retn


  def test_gadget_sub_6E736D60(self):
		#sub_6E736D60
		gadget = "A19C53A66E83E0FEA39C53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6539C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6539C, eax
		#retn


  def test_gadget_sub_6E736D90(self):
		#sub_6E736D90
		gadget = "A1A453A66E83E0FEA3A453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653A4, eax
		#retn


  def test_gadget_sub_6E736DF0(self):
		#sub_6E736DF0
		gadget = "A1AC53A66E83E0FEA3AC53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653AC, eax
		#retn


  def test_gadget_sub_6E736EB0(self):
		#sub_6E736EB0
		gadget = "A1B453A66E83E0FEA3B453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653B4, eax
		#retn


  def test_gadget_sub_6E736FA0(self):
		#sub_6E736FA0
		gadget = "A1BC53A66E83E0FEA3BC53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653BC, eax
		#retn


  def test_gadget_sub_6E737050(self):
		#sub_6E737050
		gadget = "A1C453A66E83E0FEA3C453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653C4, eax
		#retn


  def test_gadget_sub_6E7370D0(self):
		#sub_6E7370D0
		gadget = "A1CC53A66E83E0FEA3CC53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653CC, eax
		#retn


  def test_gadget_sub_6E737950(self):
		#sub_6E737950
		gadget = "A1D453A66E83E0FEA3D453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653D4, eax
		#retn


  def test_gadget_sub_6E737980(self):
		#sub_6E737980
		gadget = "A1DC53A66E83E0FEA3DC53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653DC, eax
		#retn


  def test_gadget_sub_6E7379B0(self):
		#sub_6E7379B0
		gadget = "A1E453A66E83E0FEA3E453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653E4, eax
		#retn


  def test_gadget_sub_6E737A10(self):
		#sub_6E737A10
		gadget = "A1EC53A66E83E0FEA3EC53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653EC, eax
		#retn


  def test_gadget_sub_6E737A40(self):
		#sub_6E737A40
		gadget = "A1F453A66E83E0FEA3F453A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653F4, eax
		#retn


  def test_gadget_sub_6E737B60(self):
		#sub_6E737B60
		gadget = "A1FC53A66E83E0FEA3FC53A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA653FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA653FC, eax
		#retn


  def test_gadget_sub_6E737BF0(self):
		#sub_6E737BF0
		gadget = "A10454A66E83E0FEA30454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65404
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65404, eax
		#retn


  def test_gadget_sub_6E737C90(self):
		#sub_6E737C90
		gadget = "A10C54A66E83E0FEA30C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6540C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6540C, eax
		#retn


  def test_gadget_sub_6E737E80(self):
		#sub_6E737E80
		gadget = "A11454A66E83E0FEA31454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65414
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65414, eax
		#retn


  def test_gadget_sub_6E737EB0(self):
		#sub_6E737EB0
		gadget = "A11C54A66E83E0FEA31C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6541C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6541C, eax
		#retn


  def test_gadget_sub_6E737F70(self):
		#sub_6E737F70
		gadget = "A12454A66E83E0FEA32454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65424
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65424, eax
		#retn


  def test_gadget_sub_6E738000(self):
		#sub_6E738000
		gadget = "A12C54A66E83E0FEA32C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6542C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6542C, eax
		#retn


  def test_gadget_sub_6E738030(self):
		#sub_6E738030
		gadget = "A13454A66E83E0FEA33454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65434
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65434, eax
		#retn


  def test_gadget_sub_6E738060(self):
		#sub_6E738060
		gadget = "A13C54A66E83E0FEA33C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6543C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6543C, eax
		#retn


  def test_gadget_sub_6E738120(self):
		#sub_6E738120
		gadget = "A14454A66E83E0FEA34454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65444
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65444, eax
		#retn


  def test_gadget_sub_6E7381B0(self):
		#sub_6E7381B0
		gadget = "A14C54A66E83E0FEA34C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6544C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6544C, eax
		#retn


  def test_gadget_sub_6E7382A0(self):
		#sub_6E7382A0
		gadget = "A15454A66E83E0FEA35454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65454
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65454, eax
		#retn


  def test_gadget_sub_6E7383D0(self):
		#sub_6E7383D0
		gadget = "A15C54A66E83E0FEA35C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6545C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6545C, eax
		#retn


  def test_gadget_sub_6E738520(self):
		#sub_6E738520
		gadget = "A16454A66E83E0FEA36454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65464
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65464, eax
		#retn


  def test_gadget_sub_6E738550(self):
		#sub_6E738550
		gadget = "A16C54A66E83E0FEA36C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6546C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6546C, eax
		#retn


  def test_gadget_sub_6E738580(self):
		#sub_6E738580
		gadget = "A17454A66E83E0FEA37454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65474
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65474, eax
		#retn


  def test_gadget_sub_6E7385B0(self):
		#sub_6E7385B0
		gadget = "A17C54A66E83E0FEA37C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6547C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6547C, eax
		#retn


  def test_gadget_sub_6E738610(self):
		#sub_6E738610
		gadget = "A18454A66E83E0FEA38454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65484
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65484, eax
		#retn


  def test_gadget_sub_6E738640(self):
		#sub_6E738640
		gadget = "A18C54A66E83E0FEA38C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6548C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6548C, eax
		#retn


  def test_gadget_sub_6E7386A0(self):
		#sub_6E7386A0
		gadget = "A19454A66E83E0FEA39454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65494
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65494, eax
		#retn


  def test_gadget_sub_6E7386D0(self):
		#sub_6E7386D0
		gadget = "A19C54A66E83E0FEA39C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6549C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6549C, eax
		#retn


  def test_gadget_sub_6E738700(self):
		#sub_6E738700
		gadget = "A1A454A66E83E0FEA3A454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654A4, eax
		#retn


  def test_gadget_sub_6E738730(self):
		#sub_6E738730
		gadget = "A1AC54A66E83E0FEA3AC54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654AC, eax
		#retn


  def test_gadget_sub_6E738760(self):
		#sub_6E738760
		gadget = "A1B454A66E83E0FEA3B454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654B4, eax
		#retn


  def test_gadget_sub_6E7387F0(self):
		#sub_6E7387F0
		gadget = "A1BC54A66E83E0FEA3BC54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654BC, eax
		#retn


  def test_gadget_sub_6E738820(self):
		#sub_6E738820
		gadget = "A1C454A66E83E0FEA3C454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654C4, eax
		#retn


  def test_gadget_sub_6E738A30(self):
		#sub_6E738A30
		gadget = "A1CC54A66E83E0FEA3CC54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654CC, eax
		#retn


  def test_gadget_sub_6E738B20(self):
		#sub_6E738B20
		gadget = "A1D454A66E83E0FEA3D454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654D4, eax
		#retn


  def test_gadget_sub_6E738B50(self):
		#sub_6E738B50
		gadget = "A1DC54A66E83E0FEA3DC54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654DC, eax
		#retn


  def test_gadget_sub_6E738CB0(self):
		#sub_6E738CB0
		gadget = "A1E454A66E83E0FEA3E454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654E4, eax
		#retn


  def test_gadget_sub_6E738CE0(self):
		#sub_6E738CE0
		gadget = "A1EC54A66E83E0FEA3EC54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654EC, eax
		#retn


  def test_gadget_sub_6E738E70(self):
		#sub_6E738E70
		gadget = "A1F454A66E83E0FEA3F454A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654F4, eax
		#retn


  def test_gadget_sub_6E738FA0(self):
		#sub_6E738FA0
		gadget = "A1FC54A66E83E0FEA3FC54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA654FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA654FC, eax
		#retn


  def test_gadget_sub_6E738FD0(self):
		#sub_6E738FD0
		gadget = "A10455A66E83E0FEA30455A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65504
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65504, eax
		#retn


  def test_gadget_sub_6E739260(self):
		#sub_6E739260
		gadget = "A10C55A66E83E0FEA30C55A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6550C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6550C, eax
		#retn


  def test_gadget_sub_6E739310(self):
		#sub_6E739310
		gadget = "A11455A66E83E0FEA31455A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65514
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65514, eax
		#retn


  def test_gadget_sub_6E739370(self):
		#sub_6E739370
		gadget = "A11C55A66E83E0FEA31C55A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6551C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6551C, eax
		#retn


  def test_gadget_sub_6E739460(self):
		#sub_6E739460
		gadget = "A12455A66E83E0FEA32455A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65524
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65524, eax
		#retn


  def test_gadget_sub_6E739490(self):
		#sub_6E739490
		gadget = "A12C55A66E83E0FEA32C55A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6552C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6552C, eax
		#retn


  def test_gadget_sub_6E7394C0(self):
		#sub_6E7394C0
		gadget = "A13455A66E83E0FEA33455A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65534
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65534, eax
		#retn


  def test_gadget_sub_6E739A00(self):
		#sub_6E739A00
		gadget = "A13C55A66E83E0FEA33C55A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6553C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6553C, eax
		#retn


  def test_gadget_sub_6E739A70(self):
		#sub_6E739A70
		gadget = "A14455A66E83E0FEA34455A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65544
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65544, eax
		#retn


  def test_gadget_sub_6E739B80(self):
		#sub_6E739B80
		gadget = "A14C55A66E83E0FEA34C55A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6554C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6554C, eax
		#retn


  def test_gadget_sub_6E739BE0(self):
		#sub_6E739BE0
		gadget = "A16855A66E83E0EFA36855A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65568
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA65568, eax
		#retn


  def test_gadget_sub_6E739BEE(self):
		#sub_6E739BEE
		gadget = "A16855A66E83E0DFA36855A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65568
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA65568, eax
		#retn


  def test_gadget_sub_6E739BFC(self):
		#sub_6E739BFC
		gadget = "A16855A66E83E0FBA36855A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65568
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA65568, eax
		#retn


  def test_gadget_sub_6E739C0A(self):
		#sub_6E739C0A
		gadget = "A16855A66E83E0F7A36855A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65568
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA65568, eax
		#retn


  def test_gadget_sub_6E739C18(self):
		#sub_6E739C18
		gadget = "A16855A66E83E0FEA36855A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65568
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65568, eax
		#retn


  def test_gadget_sub_6E739C26(self):
		#sub_6E739C26
		gadget = "A16855A66E83E0FDA36855A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65568
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA65568, eax
		#retn


  def test_gadget_sub_6E73A938(self):
		#sub_6E73A938
		gadget = "A17055A66E83E0FEA37055A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65570
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65570, eax
		#retn


  def test_gadget_sub_6E73CE18(self):
		#sub_6E73CE18
		gadget = "A12C5CA66E83E0FEA32C5CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65C2C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65C2C, eax
		#retn


  def test_gadget_sub_6E73D2F0(self):
		#sub_6E73D2F0
		gadget = "A1385CA66E83E0FEA3385CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65C38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65C38, eax
		#retn


  def test_gadget_sub_6E73D3F0(self):
		#sub_6E73D3F0
		gadget = "A1405CA66E83E0FEA3405CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65C40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65C40, eax
		#retn


  def test_gadget_sub_6E73D420(self):
		#sub_6E73D420
		gadget = "A1485CA66E83E0FEA3485CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65C48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65C48, eax
		#retn


  def test_gadget_sub_6E73D488(self):
		#sub_6E73D488
		gadget = "A1505CA66E83E0FEA3505CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA65C50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA65C50, eax
		#retn


  def test_gadget_sub_6E73DA80(self):
		#sub_6E73DA80
		gadget = "A10C64A66E83E0FEA30C64A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6640C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6640C, eax
		#retn


  def test_gadget_sub_6E73DFBB(self):
		#sub_6E73DFBB
		gadget = "A13464A66E83E0FEA33464A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66434
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66434, eax
		#retn


  def test_gadget_sub_6E73DFF0(self):
		#sub_6E73DFF0
		gadget = "A13C64A66E83E0FEA33C64A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6643C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6643C, eax
		#retn


  def test_gadget_sub_6E73E030(self):
		#sub_6E73E030
		gadget = "A15064A66E83E0FEA35064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66450
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66450, eax
		#retn


  def test_gadget_sub_6E73E1C0(self):
		#sub_6E73E1C0
		gadget = "A15864A66E83E0FEA35864A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66458
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66458, eax
		#retn


  def test_gadget_sub_6E73E3F8(self):
		#sub_6E73E3F8
		gadget = "A16464A66E83E0FEA36464A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66464
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66464, eax
		#retn


  def test_gadget_sub_6E73E510(self):
		#sub_6E73E510
		gadget = "A16C64A66E83E0FEA36C64A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6646C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6646C, eax
		#retn


  def test_gadget_sub_6E73E690(self):
		#sub_6E73E690
		gadget = "A17464A66E83E0FEA37464A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66474
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66474, eax
		#retn


  def test_gadget_sub_6E73F180(self):
		#sub_6E73F180
		gadget = "A18064A66E83E0FEA38064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66480
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66480, eax
		#retn


  def test_gadget_sub_6E73F4B0(self):
		#sub_6E73F4B0
		gadget = "A18864A66E83E0FEA38864A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66488
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66488, eax
		#retn


  def test_gadget_sub_6E73F4E0(self):
		#sub_6E73F4E0
		gadget = "A19064A66E83E0FEA39064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66490
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66490, eax
		#retn


  def test_gadget_sub_6E73F840(self):
		#sub_6E73F840
		gadget = "A19864A66E83E0FEA39864A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66498
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66498, eax
		#retn


  def test_gadget_sub_6E73FD20(self):
		#sub_6E73FD20
		gadget = "A1A064A66E83E0FEA3A064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664A0, eax
		#retn


  def test_gadget_sub_6E73FD60(self):
		#sub_6E73FD60
		gadget = "A1A864A66E83E0FEA3A864A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664A8, eax
		#retn


  def test_gadget_sub_6E740330(self):
		#sub_6E740330
		gadget = "A1B464A66E83E0FEA3B464A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664B4, eax
		#retn


  def test_gadget_sub_6E740430(self):
		#sub_6E740430
		gadget = "A1BC64A66E83E0FEA3BC64A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664BC, eax
		#retn


  def test_gadget_sub_6E741120(self):
		#sub_6E741120
		gadget = "A1C864A66E83E0FEA3C864A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664C8, eax
		#retn


  def test_gadget_sub_6E741139(self):
		#sub_6E741139
		gadget = "A1C864A66E83E0FDA3C864A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664C8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA664C8, eax
		#retn


  def test_gadget_sub_6E742590(self):
		#sub_6E742590
		gadget = "A1D064A66E83E0FEA3D064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664D0, eax
		#retn


  def test_gadget_sub_6E7425D8(self):
		#sub_6E7425D8
		gadget = "A1F064A66E83E0FEA3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E7425E6(self):
		#sub_6E7425E6
		gadget = "A1F064A66E83E0FDA3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E7425F4(self):
		#sub_6E7425F4
		gadget = "A1F064A66E83E0FBA3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E742602(self):
		#sub_6E742602
		gadget = "A1F064A66E83E0F7A3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E742618(self):
		#sub_6E742618
		gadget = "A1F064A66E83E0EFA3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E742626(self):
		#sub_6E742626
		gadget = "A1F064A66E83E0DFA3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E742634(self):
		#sub_6E742634
		gadget = "A1F064A66E83E0BFA3F064A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA664F0
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA664F0, eax
		#retn


  def test_gadget_sub_6E742670(self):
		#sub_6E742670
		gadget = "A11465A66E83E0FEA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E74267E(self):
		#sub_6E74267E
		gadget = "A11465A66E83E0FDA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E74268C(self):
		#sub_6E74268C
		gadget = "A11465A66E83E0FBA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E74269A(self):
		#sub_6E74269A
		gadget = "A11465A66E83E0F7A31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E7426A8(self):
		#sub_6E7426A8
		gadget = "A11465A66E83E0EFA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E7426B6(self):
		#sub_6E7426B6
		gadget = "A11465A66E83E0DFA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E7426C4(self):
		#sub_6E7426C4
		gadget = "A11465A66E83E0BFA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E7426D2(self):
		#sub_6E7426D2
		gadget = "A11465A66E257FFFFFFFA31465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66514
		#and     eax, 0FFFFFF7Fh
		#mov     dword_6EA66514, eax
		#retn


  def test_gadget_sub_6E742880(self):
		#sub_6E742880
		gadget = "A11C65A66E83E0FEA31C65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6651C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6651C, eax
		#retn


  def test_gadget_sub_6E742930(self):
		#sub_6E742930
		gadget = "A11C65A66E83E0FEA31C65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6651C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6651C, eax
		#retn


  def test_gadget_sub_6E744300(self):
		#sub_6E744300
		gadget = "A12465A66E83E0FEA32465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66524
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66524, eax
		#retn


  def test_gadget_sub_6E744330(self):
		#sub_6E744330
		gadget = "A12C65A66E83E0FEA32C65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6652C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6652C, eax
		#retn


  def test_gadget_sub_6E745D60(self):
		#sub_6E745D60
		gadget = "A13465A66E83E0FEA33465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66534
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66534, eax
		#retn


  def test_gadget_sub_6E746820(self):
		#sub_6E746820
		gadget = "A16C65A66E83E0FEA36C65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6656C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6656C, eax
		#retn


  def test_gadget_sub_6E746860(self):
		#sub_6E746860
		gadget = "A17465A66E83E0FEA37465A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66574
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66574, eax
		#retn


  def test_gadget_sub_6E748200(self):
		#sub_6E748200
		gadget = "A18065A66E83E0FEA38065A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66580
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66580, eax
		#retn


  def test_gadget_sub_6E74B780(self):
		#sub_6E74B780
		gadget = "A18865A66E83E0FEA38865A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66588
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66588, eax
		#retn


  def test_gadget_sub_6E74BAB0(self):
		#sub_6E74BAB0
		gadget = "A19065A66E83E0FEA39065A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66590
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66590, eax
		#retn


  def test_gadget_sub_6E74C000(self):
		#sub_6E74C000
		gadget = "A19865A66E83E0FEA39865A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66598
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66598, eax
		#retn


  def test_gadget_sub_6E74C410(self):
		#sub_6E74C410
		gadget = "A1C466A66E83E0FEA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C429(self):
		#sub_6E74C429
		gadget = "A1C466A66E83E0FDA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C442(self):
		#sub_6E74C442
		gadget = "A1C466A66E83E0FBA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C45B(self):
		#sub_6E74C45B
		gadget = "A1C466A66E83E0F7A3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C474(self):
		#sub_6E74C474
		gadget = "A1C466A66E83E0EFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C48D(self):
		#sub_6E74C48D
		gadget = "A1C466A66E83E0DFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C4A6(self):
		#sub_6E74C4A6
		gadget = "A1C466A66E83E0BFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C4BF(self):
		#sub_6E74C4BF
		gadget = "A1C466A66E257FFFFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFF7Fh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C4DA(self):
		#sub_6E74C4DA
		gadget = "A1C466A66E25FFFEFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFEFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C4F5(self):
		#sub_6E74C4F5
		gadget = "A1C466A66E25FFFDFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFDFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C510(self):
		#sub_6E74C510
		gadget = "A1C466A66E25FFFBFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFFBFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C52B(self):
		#sub_6E74C52B
		gadget = "A1C466A66E25FFF7FFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFF7FFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C546(self):
		#sub_6E74C546
		gadget = "A1C466A66E25FFEFFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFEFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C561(self):
		#sub_6E74C561
		gadget = "A1C466A66E25FFDFFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFDFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C57C(self):
		#sub_6E74C57C
		gadget = "A1C466A66E25FFBFFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFFBFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C597(self):
		#sub_6E74C597
		gadget = "A1C466A66E25FF7FFFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFF7FFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C5B2(self):
		#sub_6E74C5B2
		gadget = "A1C466A66E25FFFFFEFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFEFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C5CD(self):
		#sub_6E74C5CD
		gadget = "A1C466A66E25FFFFFDFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFDFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C5E8(self):
		#sub_6E74C5E8
		gadget = "A1C466A66E25FFFFFBFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFFBFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C603(self):
		#sub_6E74C603
		gadget = "A1C466A66E25FFFFF7FFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFF7FFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C61E(self):
		#sub_6E74C61E
		gadget = "A1C466A66E25FFFFEFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFEFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C639(self):
		#sub_6E74C639
		gadget = "A1C466A66E25FFFFDFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFDFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C654(self):
		#sub_6E74C654
		gadget = "A1C466A66E25FFFFBFFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FFBFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C66F(self):
		#sub_6E74C66F
		gadget = "A1C466A66E25FFFF7FFFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FF7FFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C68A(self):
		#sub_6E74C68A
		gadget = "A1C466A66E25FFFFFFFEA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FEFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C6A5(self):
		#sub_6E74C6A5
		gadget = "A1C466A66E25FFFFFFFDA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FDFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C6C0(self):
		#sub_6E74C6C0
		gadget = "A1C466A66E25FFFFFFFBA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0FBFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C6DB(self):
		#sub_6E74C6DB
		gadget = "A1C466A66E25FFFFFFF7A3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0F7FFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C6F6(self):
		#sub_6E74C6F6
		gadget = "A1C466A66E25FFFFFFEFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0EFFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C711(self):
		#sub_6E74C711
		gadget = "A1C466A66E25FFFFFFDFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0DFFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C72C(self):
		#sub_6E74C72C
		gadget = "A1C466A66E25FFFFFFBFA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 0BFFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C747(self):
		#sub_6E74C747
		gadget = "A1C466A66E25FFFFFF7FA3C466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666C4
		#and     eax, 7FFFFFFFh
		#mov     dword_6EA666C4, eax
		#retn


  def test_gadget_sub_6E74C762(self):
		#sub_6E74C762
		gadget = "A14066A66E83E0FEA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C77B(self):
		#sub_6E74C77B
		gadget = "A14066A66E83E0FDA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C794(self):
		#sub_6E74C794
		gadget = "A14066A66E83E0FBA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C7AD(self):
		#sub_6E74C7AD
		gadget = "A14066A66E83E0F7A34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C7C6(self):
		#sub_6E74C7C6
		gadget = "A14066A66E83E0EFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C7DF(self):
		#sub_6E74C7DF
		gadget = "A14066A66E83E0DFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C7F8(self):
		#sub_6E74C7F8
		gadget = "A14066A66E83E0BFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C811(self):
		#sub_6E74C811
		gadget = "A14066A66E257FFFFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFF7Fh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C82C(self):
		#sub_6E74C82C
		gadget = "A14066A66E25FFFEFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFEFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C847(self):
		#sub_6E74C847
		gadget = "A14066A66E25FFFDFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFDFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C862(self):
		#sub_6E74C862
		gadget = "A14066A66E25FFFBFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFFBFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C87D(self):
		#sub_6E74C87D
		gadget = "A14066A66E25FFF7FFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFF7FFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C898(self):
		#sub_6E74C898
		gadget = "A14066A66E25FFEFFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFEFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C8B3(self):
		#sub_6E74C8B3
		gadget = "A14066A66E25FFDFFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFDFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C8CE(self):
		#sub_6E74C8CE
		gadget = "A14066A66E25FFBFFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFFBFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C8E9(self):
		#sub_6E74C8E9
		gadget = "A14066A66E25FF7FFFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFF7FFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C904(self):
		#sub_6E74C904
		gadget = "A14066A66E25FFFFFEFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFEFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C91F(self):
		#sub_6E74C91F
		gadget = "A14066A66E25FFFFFDFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFDFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C93A(self):
		#sub_6E74C93A
		gadget = "A14066A66E25FFFFFBFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFFBFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C955(self):
		#sub_6E74C955
		gadget = "A14066A66E25FFFFF7FFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFF7FFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C970(self):
		#sub_6E74C970
		gadget = "A14066A66E25FFFFEFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFEFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C98B(self):
		#sub_6E74C98B
		gadget = "A14066A66E25FFFFDFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFDFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C9A6(self):
		#sub_6E74C9A6
		gadget = "A14066A66E25FFFFBFFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FFBFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C9C1(self):
		#sub_6E74C9C1
		gadget = "A14066A66E25FFFF7FFFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FF7FFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C9DC(self):
		#sub_6E74C9DC
		gadget = "A14066A66E25FFFFFFFEA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FEFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74C9F7(self):
		#sub_6E74C9F7
		gadget = "A14066A66E25FFFFFFFDA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FDFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CA12(self):
		#sub_6E74CA12
		gadget = "A14066A66E25FFFFFFFBA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0FBFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CA2D(self):
		#sub_6E74CA2D
		gadget = "A14066A66E25FFFFFFF7A34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0F7FFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CA48(self):
		#sub_6E74CA48
		gadget = "A14066A66E25FFFFFFEFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0EFFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CA63(self):
		#sub_6E74CA63
		gadget = "A14066A66E25FFFFFFDFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0DFFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CA7E(self):
		#sub_6E74CA7E
		gadget = "A14066A66E25FFFFFFBFA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 0BFFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CA99(self):
		#sub_6E74CA99
		gadget = "A14066A66E25FFFFFF7FA34066A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66640
		#and     eax, 7FFFFFFFh
		#mov     dword_6EA66640, eax
		#retn


  def test_gadget_sub_6E74CAB4(self):
		#sub_6E74CAB4
		gadget = "A1BC65A66E83E0FEA3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CACD(self):
		#sub_6E74CACD
		gadget = "A1BC65A66E83E0FDA3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CAE6(self):
		#sub_6E74CAE6
		gadget = "A1BC65A66E83E0FBA3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CAFF(self):
		#sub_6E74CAFF
		gadget = "A1BC65A66E83E0F7A3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CB18(self):
		#sub_6E74CB18
		gadget = "A1BC65A66E83E0EFA3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CB31(self):
		#sub_6E74CB31
		gadget = "A1BC65A66E83E0DFA3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CB4A(self):
		#sub_6E74CB4A
		gadget = "A1BC65A66E83E0BFA3BC65A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA665BC
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA665BC, eax
		#retn


  def test_gadget_sub_6E74CE50(self):
		#sub_6E74CE50
		gadget = "A1CC66A66E83E0FEA3CC66A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA666CC, eax
		#retn


  def test_gadget_sub_6E74DD10(self):
		#sub_6E74DD10
		gadget = "A1D466A66E83E0FEA3D466A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA666D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA666D4, eax
		#retn


  def test_gadget_sub_6E74E130(self):
		#sub_6E74E130
		gadget = "A12467A66E83E0FEA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E149(self):
		#sub_6E74E149
		gadget = "A12467A66E83E0FDA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E162(self):
		#sub_6E74E162
		gadget = "A12467A66E83E0FBA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E17B(self):
		#sub_6E74E17B
		gadget = "A12467A66E83E0F7A32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E194(self):
		#sub_6E74E194
		gadget = "A12467A66E83E0EFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E1AD(self):
		#sub_6E74E1AD
		gadget = "A12467A66E83E0DFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E1C6(self):
		#sub_6E74E1C6
		gadget = "A12467A66E83E0BFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E1DF(self):
		#sub_6E74E1DF
		gadget = "A12467A66E257FFFFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFF7Fh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E1FA(self):
		#sub_6E74E1FA
		gadget = "A12467A66E25FFFEFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFEFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E215(self):
		#sub_6E74E215
		gadget = "A12467A66E25FFFDFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFDFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E230(self):
		#sub_6E74E230
		gadget = "A12467A66E25FFFBFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFFBFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E24B(self):
		#sub_6E74E24B
		gadget = "A12467A66E25FFF7FFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFF7FFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E266(self):
		#sub_6E74E266
		gadget = "A12467A66E25FFEFFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFEFFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E281(self):
		#sub_6E74E281
		gadget = "A12467A66E25FFDFFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFDFFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E29C(self):
		#sub_6E74E29C
		gadget = "A12467A66E25FFBFFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFFBFFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74E2B7(self):
		#sub_6E74E2B7
		gadget = "A12467A66E25FF7FFFFFA32467A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66724
		#and     eax, 0FFFF7FFFh
		#mov     dword_6EA66724, eax
		#retn


  def test_gadget_sub_6E74F2C0(self):
		#sub_6E74F2C0
		gadget = "A12C67A66E83E0FEA32C67A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6672C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6672C, eax
		#retn


  def test_gadget_sub_6E74F410(self):
		#sub_6E74F410
		gadget = "A13867A66E83E0FEA33867A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66738
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66738, eax
		#retn


  def test_gadget_sub_6E74F450(self):
		#sub_6E74F450
		gadget = "A14067A66E83E0FEA34067A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66740
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66740, eax
		#retn


  def test_gadget_sub_6E74F5D0(self):
		#sub_6E74F5D0
		gadget = "A10468A66E83E0FEA30468A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66804
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66804, eax
		#retn


  def test_gadget_sub_6E74F5E9(self):
		#sub_6E74F5E9
		gadget = "A10468A66E83E0FDA30468A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66804
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66804, eax
		#retn


  def test_gadget_sub_6E74F602(self):
		#sub_6E74F602
		gadget = "A10468A66E83E0FBA30468A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66804
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66804, eax
		#retn


  def test_gadget_sub_6E74F61B(self):
		#sub_6E74F61B
		gadget = "A10468A66E83E0F7A30468A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66804
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66804, eax
		#retn


  def test_gadget_sub_6E74F634(self):
		#sub_6E74F634
		gadget = "A10468A66E83E0EFA30468A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66804
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA66804, eax
		#retn


  def test_gadget_sub_6E750570(self):
		#sub_6E750570
		gadget = "A12068A66E83E0FEA32068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66820
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66820, eax
		#retn


  def test_gadget_sub_6E750589(self):
		#sub_6E750589
		gadget = "A12068A66E83E0FDA32068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66820
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66820, eax
		#retn


  def test_gadget_sub_6E7508B0(self):
		#sub_6E7508B0
		gadget = "A12868A66E83E0FEA32868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66828
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66828, eax
		#retn


  def test_gadget_sub_6E750E60(self):
		#sub_6E750E60
		gadget = "A13068A66E83E0FEA33068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66830
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66830, eax
		#retn


  def test_gadget_sub_6E750E90(self):
		#sub_6E750E90
		gadget = "A13868A66E83E0FEA33868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66838
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66838, eax
		#retn


  def test_gadget_sub_6E750EC0(self):
		#sub_6E750EC0
		gadget = "A14068A66E83E0FEA34068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66840
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66840, eax
		#retn


  def test_gadget_sub_6E750EF0(self):
		#sub_6E750EF0
		gadget = "A14868A66E83E0FEA34868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66848
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66848, eax
		#retn


  def test_gadget_sub_6E750F20(self):
		#sub_6E750F20
		gadget = "A15068A66E83E0FEA35068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66850
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66850, eax
		#retn


  def test_gadget_sub_6E750F50(self):
		#sub_6E750F50
		gadget = "A15868A66E83E0FEA35868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66858
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66858, eax
		#retn


  def test_gadget_sub_6E750F80(self):
		#sub_6E750F80
		gadget = "A16068A66E83E0FEA36068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66860
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66860, eax
		#retn


  def test_gadget_sub_6E750FB0(self):
		#sub_6E750FB0
		gadget = "A16868A66E83E0FEA36868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66868
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66868, eax
		#retn


  def test_gadget_sub_6E750FF0(self):
		#sub_6E750FF0
		gadget = "A17068A66E83E0FEA37068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66870
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66870, eax
		#retn


  def test_gadget_sub_6E751020(self):
		#sub_6E751020
		gadget = "A17868A66E83E0FEA37868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66878
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66878, eax
		#retn


  def test_gadget_sub_6E751050(self):
		#sub_6E751050
		gadget = "A18068A66E83E0FEA38068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66880
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66880, eax
		#retn


  def test_gadget_sub_6E751080(self):
		#sub_6E751080
		gadget = "A18868A66E83E0FEA38868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66888
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66888, eax
		#retn


  def test_gadget_sub_6E7510B0(self):
		#sub_6E7510B0
		gadget = "A19068A66E83E0FEA39068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66890
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66890, eax
		#retn


  def test_gadget_sub_6E7510E0(self):
		#sub_6E7510E0
		gadget = "A19868A66E83E0FEA39868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66898
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66898, eax
		#retn


  def test_gadget_sub_6E751110(self):
		#sub_6E751110
		gadget = "A1A068A66E83E0FEA3A068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668A0, eax
		#retn


  def test_gadget_sub_6E751140(self):
		#sub_6E751140
		gadget = "A1A868A66E83E0FEA3A868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668A8, eax
		#retn


  def test_gadget_sub_6E751170(self):
		#sub_6E751170
		gadget = "A1B068A66E83E0FEA3B068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668B0, eax
		#retn


  def test_gadget_sub_6E7511A0(self):
		#sub_6E7511A0
		gadget = "A1B868A66E83E0FEA3B868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668B8, eax
		#retn


  def test_gadget_sub_6E7511D0(self):
		#sub_6E7511D0
		gadget = "A1C068A66E83E0FEA3C068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668C0, eax
		#retn


  def test_gadget_sub_6E751200(self):
		#sub_6E751200
		gadget = "A1C868A66E83E0FEA3C868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668C8, eax
		#retn


  def test_gadget_sub_6E751230(self):
		#sub_6E751230
		gadget = "A1D068A66E83E0FEA3D068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668D0, eax
		#retn


  def test_gadget_sub_6E751260(self):
		#sub_6E751260
		gadget = "A1D868A66E83E0FEA3D868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668D8, eax
		#retn


  def test_gadget_sub_6E751290(self):
		#sub_6E751290
		gadget = "A1E068A66E83E0FEA3E068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668E0, eax
		#retn


  def test_gadget_sub_6E7512C0(self):
		#sub_6E7512C0
		gadget = "A1E868A66E83E0FEA3E868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668E8, eax
		#retn


  def test_gadget_sub_6E7512F0(self):
		#sub_6E7512F0
		gadget = "A1F068A66E83E0FEA3F068A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668F0, eax
		#retn


  def test_gadget_sub_6E751320(self):
		#sub_6E751320
		gadget = "A1F868A66E83E0FEA3F868A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA668F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA668F8, eax
		#retn


  def test_gadget_sub_6E751350(self):
		#sub_6E751350
		gadget = "A10069A66E83E0FEA30069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66900
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66900, eax
		#retn


  def test_gadget_sub_6E751380(self):
		#sub_6E751380
		gadget = "A10869A66E83E0FEA30869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66908
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66908, eax
		#retn


  def test_gadget_sub_6E7513B0(self):
		#sub_6E7513B0
		gadget = "A11069A66E83E0FEA31069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66910
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66910, eax
		#retn


  def test_gadget_sub_6E7513E0(self):
		#sub_6E7513E0
		gadget = "A11869A66E83E0FEA31869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66918
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66918, eax
		#retn


  def test_gadget_sub_6E751410(self):
		#sub_6E751410
		gadget = "A12069A66E83E0FEA32069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66920
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66920, eax
		#retn


  def test_gadget_sub_6E751440(self):
		#sub_6E751440
		gadget = "A12869A66E83E0FEA32869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66928
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66928, eax
		#retn


  def test_gadget_sub_6E751470(self):
		#sub_6E751470
		gadget = "A13069A66E83E0FEA33069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66930
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66930, eax
		#retn


  def test_gadget_sub_6E7514A0(self):
		#sub_6E7514A0
		gadget = "A13869A66E83E0FEA33869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66938
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66938, eax
		#retn


  def test_gadget_sub_6E7514D0(self):
		#sub_6E7514D0
		gadget = "A14069A66E83E0FEA34069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66940
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66940, eax
		#retn


  def test_gadget_sub_6E751500(self):
		#sub_6E751500
		gadget = "A14869A66E83E0FEA34869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66948
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66948, eax
		#retn


  def test_gadget_sub_6E751530(self):
		#sub_6E751530
		gadget = "A15069A66E83E0FEA35069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66950
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66950, eax
		#retn


  def test_gadget_sub_6E751560(self):
		#sub_6E751560
		gadget = "A15869A66E83E0FEA35869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66958
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66958, eax
		#retn


  def test_gadget_sub_6E751590(self):
		#sub_6E751590
		gadget = "A16069A66E83E0FEA36069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66960
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66960, eax
		#retn


  def test_gadget_sub_6E7515C0(self):
		#sub_6E7515C0
		gadget = "A16869A66E83E0FEA36869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66968
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66968, eax
		#retn


  def test_gadget_sub_6E7515F0(self):
		#sub_6E7515F0
		gadget = "A17069A66E83E0FEA37069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66970
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66970, eax
		#retn


  def test_gadget_sub_6E751620(self):
		#sub_6E751620
		gadget = "A17869A66E83E0FEA37869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66978
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66978, eax
		#retn


  def test_gadget_sub_6E751650(self):
		#sub_6E751650
		gadget = "A18069A66E83E0FEA38069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66980
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66980, eax
		#retn


  def test_gadget_sub_6E751680(self):
		#sub_6E751680
		gadget = "A19469A66E83E0FEA39469A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66994
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66994, eax
		#retn


  def test_gadget_sub_6E75168E(self):
		#sub_6E75168E
		gadget = "A19469A66E83E0FDA39469A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66994
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66994, eax
		#retn


  def test_gadget_sub_6E7516C0(self):
		#sub_6E7516C0
		gadget = "A1A069A66E83E0FEA3A069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669A0, eax
		#retn


  def test_gadget_sub_6E751700(self):
		#sub_6E751700
		gadget = "A1A869A66E83E0FEA3A869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669A8, eax
		#retn


  def test_gadget_sub_6E7531C6(self):
		#sub_6E7531C6
		gadget = "A1B869A66E83E0FEA3B869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669B8, eax
		#retn


  def test_gadget_sub_6E753CF0(self):
		#sub_6E753CF0
		gadget = "A1C069A66E83E0FEA3C069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669C0, eax
		#retn


  def test_gadget_sub_6E7541C0(self):
		#sub_6E7541C0
		gadget = "A1D869A66E83E0FEA3D869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669D8, eax
		#retn


  def test_gadget_sub_6E754548(self):
		#sub_6E754548
		gadget = "A1D869A66E83E0FEA3D869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669D8, eax
		#retn


  def test_gadget_sub_6E7548D0(self):
		#sub_6E7548D0
		gadget = "A1E069A66E83E0FEA3E069A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669E0, eax
		#retn


  def test_gadget_sub_6E754900(self):
		#sub_6E754900
		gadget = "A1E869A66E83E0FEA3E869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669E8, eax
		#retn


  def test_gadget_sub_6E7549D0(self):
		#sub_6E7549D0
		gadget = "A10C6AA66E83E0FEA30C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A0C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A0C, eax
		#retn


  def test_gadget_sub_6E7549E9(self):
		#sub_6E7549E9
		gadget = "A10C6AA66E83E0FDA30C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A0C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66A0C, eax
		#retn


  def test_gadget_sub_6E754A02(self):
		#sub_6E754A02
		gadget = "A10C6AA66E83E0FBA30C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A0C
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66A0C, eax
		#retn


  def test_gadget_sub_6E7575B0(self):
		#sub_6E7575B0
		gadget = "A1306AA66E83E0FEA3306AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A30, eax
		#retn


  def test_gadget_sub_6E7575C9(self):
		#sub_6E7575C9
		gadget = "A1306AA66E83E0FDA3306AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A30
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66A30, eax
		#retn


  def test_gadget_sub_6E757DF0(self):
		#sub_6E757DF0
		gadget = "A13C6AA66E83E0FEA33C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A3C, eax
		#retn


  def test_gadget_sub_6E757E40(self):
		#sub_6E757E40
		gadget = "A1486AA66E83E0FEA3486AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A48, eax
		#retn


  def test_gadget_sub_6E757E90(self):
		#sub_6E757E90
		gadget = "A1546AA66E83E0FEA3546AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A54, eax
		#retn


  def test_gadget_sub_6E757EC0(self):
		#sub_6E757EC0
		gadget = "A1606AA66E83E0FEA3606AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A60, eax
		#retn


  def test_gadget_sub_6E758330(self):
		#sub_6E758330
		gadget = "A1746AA66E83E0FEA3746AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A74
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A74, eax
		#retn


  def test_gadget_sub_6E758349(self):
		#sub_6E758349
		gadget = "A1746AA66E83E0FDA3746AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A74
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66A74, eax
		#retn


  def test_gadget_sub_6E758362(self):
		#sub_6E758362
		gadget = "A1746AA66E83E0FBA3746AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A74
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66A74, eax
		#retn


  def test_gadget_sub_6E75837B(self):
		#sub_6E75837B
		gadget = "A1746AA66E83E0F7A3746AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A74
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66A74, eax
		#retn


  def test_gadget_sub_6E758960(self):
		#sub_6E758960
		gadget = "A17C6AA66E83E0FEA37C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A7C, eax
		#retn


  def test_gadget_sub_6E758A88(self):
		#sub_6E758A88
		gadget = "A17C6AA66E83E0FEA37C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A7C, eax
		#retn


  def test_gadget_sub_6E759490(self):
		#sub_6E759490
		gadget = "A1846AA66E83E0FEA3846AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A84, eax
		#retn


  def test_gadget_sub_6E75A500(self):
		#sub_6E75A500
		gadget = "A18C6AA66E83E0FEA38C6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A8C, eax
		#retn


  def test_gadget_sub_6E75B740(self):
		#sub_6E75B740
		gadget = "A1986AA66E83E0FEA3986AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A98, eax
		#retn


  def test_gadget_sub_6E75B7A0(self):
		#sub_6E75B7A0
		gadget = "A1A06AA66E83E0FEA3A06AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AA0, eax
		#retn


  def test_gadget_sub_6E75B840(self):
		#sub_6E75B840
		gadget = "A1A06AA66E83E0FEA3A06AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AA0, eax
		#retn


  def test_gadget_sub_6E75B856(self):
		#sub_6E75B856
		gadget = "A1A06AA66E83E0FEA3A06AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AA0, eax
		#retn


  def test_gadget_sub_6E75B864(self):
		#sub_6E75B864
		gadget = "A1A06AA66E83E0FEA3A06AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AA0, eax
		#retn


  def test_gadget_sub_6E75B872(self):
		#sub_6E75B872
		gadget = "A1986AA66E83E0FEA3986AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66A98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66A98, eax
		#retn


  def test_gadget_sub_6E75BAB0(self):
		#sub_6E75BAB0
		gadget = "A1AC6AA66E83E0FEA3AC6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AAC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AAC, eax
		#retn


  def test_gadget_sub_6E75BAF0(self):
		#sub_6E75BAF0
		gadget = "A1B46AA66E83E0FEA3B46AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AB4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AB4, eax
		#retn


  def test_gadget_sub_6E75BB30(self):
		#sub_6E75BB30
		gadget = "A1BC6AA66E83E0FEA3BC6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66ABC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66ABC, eax
		#retn


  def test_gadget_sub_6E75C730(self):
		#sub_6E75C730
		gadget = "A1C46AA66E83E0FEA3C46AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AC4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AC4, eax
		#retn


  def test_gadget_sub_6E75D5A0(self):
		#sub_6E75D5A0
		gadget = "A1D06AA66E83E0FEA3D06AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AD0, eax
		#retn


  def test_gadget_sub_6E75D5B9(self):
		#sub_6E75D5B9
		gadget = "A1D06AA66E83E0FDA3D06AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AD0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66AD0, eax
		#retn


  def test_gadget_sub_6E75D5F0(self):
		#sub_6E75D5F0
		gadget = "A1D86AA66E83E0FEA3D86AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AD8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AD8, eax
		#retn


  def test_gadget_sub_6E75E130(self):
		#sub_6E75E130
		gadget = "A1E46AA66E83E0FEA3E46AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AE4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AE4, eax
		#retn


  def test_gadget_sub_6E75E200(self):
		#sub_6E75E200
		gadget = "A1EC6AA66E83E0FEA3EC6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AEC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AEC, eax
		#retn


  def test_gadget_sub_6E75EB90(self):
		#sub_6E75EB90
		gadget = "A1F46AA66E83E0FEA3F46AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AF4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AF4, eax
		#retn


  def test_gadget_sub_6E75EFA0(self):
		#sub_6E75EFA0
		gadget = "A1FC6AA66E83E0FEA3FC6AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66AFC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66AFC, eax
		#retn


  def test_gadget_sub_6E75EFD0(self):
		#sub_6E75EFD0
		gadget = "A1046BA66E83E0FEA3046BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B04
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B04, eax
		#retn


  def test_gadget_sub_6E75FA10(self):
		#sub_6E75FA10
		gadget = "A1146BA66E83E0FEA3146BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B14
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B14, eax
		#retn


  def test_gadget_sub_6E760450(self):
		#sub_6E760450
		gadget = "A11C6BA66E83E0FEA31C6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B1C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B1C, eax
		#retn


  def test_gadget_sub_6E763998(self):
		#sub_6E763998
		gadget = "A12C6BA66E83E0FEA32C6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B2C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B2C, eax
		#retn


  def test_gadget_sub_6E7639B1(self):
		#sub_6E7639B1
		gadget = "A12C6BA66E83E0FDA32C6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B2C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66B2C, eax
		#retn


  def test_gadget_sub_6E763D30(self):
		#sub_6E763D30
		gadget = "A1346BA66E83E0FEA3346BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B34
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B34, eax
		#retn


  def test_gadget_sub_6E763DB0(self):
		#sub_6E763DB0
		gadget = "A13C6BA66E83E0FEA33C6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B3C, eax
		#retn


  def test_gadget_sub_6E763E10(self):
		#sub_6E763E10
		gadget = "A1486BA66E83E0FEA3486BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B48, eax
		#retn


  def test_gadget_sub_6E763E29(self):
		#sub_6E763E29
		gadget = "A1486BA66E83E0FDA3486BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B48
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66B48, eax
		#retn


  def test_gadget_sub_6E766080(self):
		#sub_6E766080
		gadget = "A1546BA66E83E0FEA3546BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B54, eax
		#retn


  def test_gadget_sub_6E7660F0(self):
		#sub_6E7660F0
		gadget = "A15C6BA66E83E0FEA35C6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B5C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B5C, eax
		#retn


  def test_gadget_sub_6E7673C0(self):
		#sub_6E7673C0
		gadget = "A1646BA66E83E0FEA3646BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B64, eax
		#retn


  def test_gadget_sub_6E768C50(self):
		#sub_6E768C50
		gadget = "A1706BA66E83E0FEA3706BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B70, eax
		#retn


  def test_gadget_sub_6E768C69(self):
		#sub_6E768C69
		gadget = "A1706BA66E83E0FDA3706BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B70
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66B70, eax
		#retn


  def test_gadget_sub_6E769530(self):
		#sub_6E769530
		gadget = "A1786BA66E83E0FEA3786BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66B78
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66B78, eax
		#retn


  def test_gadget_sub_6E769750(self):
		#sub_6E769750
		gadget = "A1CC6BA66E83E0FEA3CC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BCC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66BCC, eax
		#retn


  def test_gadget_sub_6E769769(self):
		#sub_6E769769
		gadget = "A1CC6BA66E83E0FDA3CC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BCC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66BCC, eax
		#retn


  def test_gadget_sub_6E769782(self):
		#sub_6E769782
		gadget = "A1CC6BA66E83E0FBA3CC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BCC
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66BCC, eax
		#retn


  def test_gadget_sub_6E76979B(self):
		#sub_6E76979B
		gadget = "A1CC6BA66E83E0F7A3CC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BCC
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66BCC, eax
		#retn


  def test_gadget_sub_6E7697B4(self):
		#sub_6E7697B4
		gadget = "A1CC6BA66E83E0EFA3CC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BCC
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA66BCC, eax
		#retn


  def test_gadget_sub_6E7698F0(self):
		#sub_6E7698F0
		gadget = "A1D46BA66E83E0FEA3D46BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BD4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66BD4, eax
		#retn


  def test_gadget_sub_6E769B10(self):
		#sub_6E769B10
		gadget = "A1DC6BA66E83E0FEA3DC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BDC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66BDC, eax
		#retn


  def test_gadget_sub_6E769C60(self):
		#sub_6E769C60
		gadget = "A1E46BA66E83E0FEA3E46BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BE4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66BE4, eax
		#retn


  def test_gadget_sub_6E769CA0(self):
		#sub_6E769CA0
		gadget = "A1EC6BA66E83E0FEA3EC6BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BEC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66BEC, eax
		#retn


  def test_gadget_sub_6E76A900(self):
		#sub_6E76A900
		gadget = "A1F46BA66E83E0FEA3F46BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66BF4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66BF4, eax
		#retn


  def test_gadget_sub_6E76E9F4(self):
		#sub_6E76E9F4
		gadget = "A1006CA66E83E0FEA3006CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C00, eax
		#retn


  def test_gadget_sub_6E76EA02(self):
		#sub_6E76EA02
		gadget = "A1006CA66E83E0FEA3006CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C00, eax
		#retn


  def test_gadget_sub_6E76EBA8(self):
		#sub_6E76EBA8
		gadget = "A1006CA66E83E0FEA3006CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C00, eax
		#retn


  def test_gadget_sub_6E76EBB6(self):
		#sub_6E76EBB6
		gadget = "A1006CA66E83E0FEA3006CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C00, eax
		#retn


  def test_gadget_sub_6E76EC50(self):
		#sub_6E76EC50
		gadget = "A1086CA66E83E0FEA3086CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C08, eax
		#retn


  def test_gadget_sub_6E76ED90(self):
		#sub_6E76ED90
		gadget = "A1106CA66E83E0FEA3106CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C10, eax
		#retn


  def test_gadget_sub_6E76F350(self):
		#sub_6E76F350
		gadget = "A1186CA66E83E0FEA3186CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C18, eax
		#retn


  def test_gadget_sub_6E76F380(self):
		#sub_6E76F380
		gadget = "A1206CA66E83E0FEA3206CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C20, eax
		#retn


  def test_gadget_sub_6E76F3B0(self):
		#sub_6E76F3B0
		gadget = "A1286CA66E83E0FEA3286CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C28, eax
		#retn


  def test_gadget_sub_6E76F3E0(self):
		#sub_6E76F3E0
		gadget = "A1306CA66E83E0FEA3306CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C30, eax
		#retn


  def test_gadget_sub_6E76F700(self):
		#sub_6E76F700
		gadget = "A1386CA66E83E0FEA3386CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C38, eax
		#retn


  def test_gadget_sub_6E76F9F0(self):
		#sub_6E76F9F0
		gadget = "A1406CA66E83E0FEA3406CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C40, eax
		#retn


  def test_gadget_sub_6E770010(self):
		#sub_6E770010
		gadget = "A1486CA66E83E0FEA3486CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C48, eax
		#retn


  def test_gadget_sub_6E7702C0(self):
		#sub_6E7702C0
		gadget = "A1506CA66E83E0FEA3506CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C50, eax
		#retn


  def test_gadget_sub_6E770DB0(self):
		#sub_6E770DB0
		gadget = "A1586CA66E83E0FEA3586CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C58, eax
		#retn


  def test_gadget_sub_6E771290(self):
		#sub_6E771290
		gadget = "A1686CA66E83E0FDA3686CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C68
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66C68, eax
		#retn


  def test_gadget_sub_6E7712A9(self):
		#sub_6E7712A9
		gadget = "A1686CA66E83E0FBA3686CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C68
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66C68, eax
		#retn


  def test_gadget_sub_6E7712C2(self):
		#sub_6E7712C2
		gadget = "A1686CA66E83E0FEA3686CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C68
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C68, eax
		#retn


  def test_gadget_sub_6E771530(self):
		#sub_6E771530
		gadget = "A1706CA66E83E0FEA3706CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C70, eax
		#retn


  def test_gadget_sub_6E7716C0(self):
		#sub_6E7716C0
		gadget = "A1786CA66E83E0FEA3786CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C78
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C78, eax
		#retn


  def test_gadget_sub_6E771A50(self):
		#sub_6E771A50
		gadget = "A1806CA66E83E0FEA3806CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C80, eax
		#retn


  def test_gadget_sub_6E771B50(self):
		#sub_6E771B50
		gadget = "A1886CA66E83E0FEA3886CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C88
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C88, eax
		#retn


  def test_gadget_sub_6E772210(self):
		#sub_6E772210
		gadget = "A1D869A66E83E0FEA3D869A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA669D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA669D8, eax
		#retn


  def test_gadget_sub_6E772B10(self):
		#sub_6E772B10
		gadget = "A1906CA66E83E0FEA3906CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C90, eax
		#retn


  def test_gadget_sub_6E772B58(self):
		#sub_6E772B58
		gadget = "A1986CA66E83E0FEA3986CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66C98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66C98, eax
		#retn


  def test_gadget_sub_6E772D80(self):
		#sub_6E772D80
		gadget = "A1A46CA66E83E0FEA3A46CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CA4, eax
		#retn


  def test_gadget_sub_6E7730A8(self):
		#sub_6E7730A8
		gadget = "A1AC6CA66E83E0FEA3AC6CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CAC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CAC, eax
		#retn


  def test_gadget_sub_6E7733A0(self):
		#sub_6E7733A0
		gadget = "A1B46CA66E83E0FEA3B46CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CB4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CB4, eax
		#retn


  def test_gadget_sub_6E7734F0(self):
		#sub_6E7734F0
		gadget = "A1BC6CA66E83E0FEA3BC6CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CBC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CBC, eax
		#retn


  def test_gadget_sub_6E773750(self):
		#sub_6E773750
		gadget = "A1C46CA66E83E0FEA3C46CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CC4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CC4, eax
		#retn


  def test_gadget_sub_6E773940(self):
		#sub_6E773940
		gadget = "A1CC6CA66E83E0FEA3CC6CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CCC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CCC, eax
		#retn


  def test_gadget_sub_6E773B18(self):
		#sub_6E773B18
		gadget = "A1D46CA66E83E0FEA3D46CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CD4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CD4, eax
		#retn


  def test_gadget_sub_6E773B88(self):
		#sub_6E773B88
		gadget = "A1DC6CA66E83E0FEA3DC6CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CDC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CDC, eax
		#retn


  def test_gadget_sub_6E773BFB(self):
		#sub_6E773BFB
		gadget = "A1E46CA66E83E0FEA3E46CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CE4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CE4, eax
		#retn


  def test_gadget_sub_6E773DD8(self):
		#sub_6E773DD8
		gadget = "A1EC6CA66E83E0FEA3EC6CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CEC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CEC, eax
		#retn


  def test_gadget_sub_6E773E18(self):
		#sub_6E773E18
		gadget = "A1F46CA66E83E0FEA3F46CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66CF4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66CF4, eax
		#retn


  def test_gadget_sub_6E774050(self):
		#sub_6E774050
		gadget = "A1006DA66E83E0FEA3006DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D00, eax
		#retn


  def test_gadget_sub_6E774069(self):
		#sub_6E774069
		gadget = "A1006DA66E83E0FDA3006DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D00
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66D00, eax
		#retn


  def test_gadget_sub_6E7742F0(self):
		#sub_6E7742F0
		gadget = "A1086DA66E83E0FEA3086DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D08, eax
		#retn


  def test_gadget_sub_6E7745B0(self):
		#sub_6E7745B0
		gadget = "A1186DA66E83E0FEA3186DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D18, eax
		#retn


  def test_gadget_sub_6E7745BE(self):
		#sub_6E7745BE
		gadget = "A1186DA66E83E0FDA3186DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D18
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66D18, eax
		#retn


  def test_gadget_sub_6E7745CC(self):
		#sub_6E7745CC
		gadget = "A1186DA66E83E0FBA3186DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D18
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66D18, eax
		#retn


  def test_gadget_sub_6E7746C0(self):
		#sub_6E7746C0
		gadget = "A1246DA66E83E0FEA3246DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D24
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D24, eax
		#retn


  def test_gadget_sub_6E7746CE(self):
		#sub_6E7746CE
		gadget = "A1246DA66E83E0FDA3246DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D24
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66D24, eax
		#retn


  def test_gadget_sub_6E7748A0(self):
		#sub_6E7748A0
		gadget = "A12C6DA66E83E0FEA32C6DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D2C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D2C, eax
		#retn


  def test_gadget_sub_6E774C80(self):
		#sub_6E774C80
		gadget = "A13C6DA66E83E0FEA33C6DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D3C, eax
		#retn


  def test_gadget_sub_6E774C99(self):
		#sub_6E774C99
		gadget = "A13C6DA66E83E0FDA33C6DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D3C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66D3C, eax
		#retn


  def test_gadget_sub_6E774CB2(self):
		#sub_6E774CB2
		gadget = "A13C6DA66E83E0FBA33C6DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D3C
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66D3C, eax
		#retn


  def test_gadget_sub_6E7753E0(self):
		#sub_6E7753E0
		gadget = "A1486DA66E83E0FEA3486DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D48, eax
		#retn


  def test_gadget_sub_6E7753F9(self):
		#sub_6E7753F9
		gadget = "A1486DA66E83E0FDA3486DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D48
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66D48, eax
		#retn


  def test_gadget_sub_6E775640(self):
		#sub_6E775640
		gadget = "A1506DA66E83E0FEA3506DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D50, eax
		#retn


  def test_gadget_sub_6E7756D0(self):
		#sub_6E7756D0
		gadget = "A1586DA66E83E0FEA3586DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D58, eax
		#retn


  def test_gadget_sub_6E775710(self):
		#sub_6E775710
		gadget = "A1606DA66E83E0FEA3606DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D60, eax
		#retn


  def test_gadget_sub_6E775750(self):
		#sub_6E775750
		gadget = "A1686DA66E83E0FEA3686DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D68
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D68, eax
		#retn


  def test_gadget_sub_6E775790(self):
		#sub_6E775790
		gadget = "A1706DA66E83E0FEA3706DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D70, eax
		#retn


  def test_gadget_sub_6E7757D0(self):
		#sub_6E7757D0
		gadget = "A1786DA66E83E0FEA3786DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D78
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D78, eax
		#retn


  def test_gadget_sub_6E775810(self):
		#sub_6E775810
		gadget = "A1806DA66E83E0FEA3806DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D80, eax
		#retn


  def test_gadget_sub_6E775850(self):
		#sub_6E775850
		gadget = "A1886DA66E83E0FEA3886DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D88
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D88, eax
		#retn


  def test_gadget_sub_6E775890(self):
		#sub_6E775890
		gadget = "A1906DA66E83E0FEA3906DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D90, eax
		#retn


  def test_gadget_sub_6E7758D0(self):
		#sub_6E7758D0
		gadget = "A1986DA66E83E0FEA3986DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66D98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66D98, eax
		#retn


  def test_gadget_sub_6E775910(self):
		#sub_6E775910
		gadget = "A1A06DA66E83E0FEA3A06DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DA0, eax
		#retn


  def test_gadget_sub_6E775950(self):
		#sub_6E775950
		gadget = "A1A86DA66E83E0FEA3A86DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DA8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DA8, eax
		#retn


  def test_gadget_sub_6E775990(self):
		#sub_6E775990
		gadget = "A1B06DA66E83E0FEA3B06DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DB0, eax
		#retn


  def test_gadget_sub_6E7759D0(self):
		#sub_6E7759D0
		gadget = "A1B86DA66E83E0FEA3B86DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DB8, eax
		#retn


  def test_gadget_sub_6E775A10(self):
		#sub_6E775A10
		gadget = "A1C06DA66E83E0FEA3C06DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DC0, eax
		#retn


  def test_gadget_sub_6E775A50(self):
		#sub_6E775A50
		gadget = "A1C86DA66E83E0FEA3C86DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DC8, eax
		#retn


  def test_gadget_sub_6E775A90(self):
		#sub_6E775A90
		gadget = "A1D06DA66E83E0FEA3D06DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DD0, eax
		#retn


  def test_gadget_sub_6E775AD0(self):
		#sub_6E775AD0
		gadget = "A1D86DA66E83E0FEA3D86DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DD8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DD8, eax
		#retn


  def test_gadget_sub_6E775B10(self):
		#sub_6E775B10
		gadget = "A1E06DA66E83E0FEA3E06DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DE0, eax
		#retn


  def test_gadget_sub_6E775B50(self):
		#sub_6E775B50
		gadget = "A1E86DA66E83E0FEA3E86DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DE8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DE8, eax
		#retn


  def test_gadget_sub_6E775B90(self):
		#sub_6E775B90
		gadget = "A1F06DA66E83E0FEA3F06DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DF0, eax
		#retn


  def test_gadget_sub_6E775BD0(self):
		#sub_6E775BD0
		gadget = "A1F86DA66E83E0FEA3F86DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66DF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66DF8, eax
		#retn


  def test_gadget_sub_6E775C10(self):
		#sub_6E775C10
		gadget = "A1006EA66E83E0FEA3006EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E00, eax
		#retn


  def test_gadget_sub_6E775C50(self):
		#sub_6E775C50
		gadget = "A1086EA66E83E0FEA3086EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E08, eax
		#retn


  def test_gadget_sub_6E775EC0(self):
		#sub_6E775EC0
		gadget = "A1106EA66E83E0FEA3106EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E10, eax
		#retn


  def test_gadget_sub_6E775F50(self):
		#sub_6E775F50
		gadget = "A1186EA66E83E0FEA3186EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E18, eax
		#retn


  def test_gadget_sub_6E776180(self):
		#sub_6E776180
		gadget = "A1206EA66E83E0FEA3206EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E20, eax
		#retn


  def test_gadget_sub_6E7763D0(self):
		#sub_6E7763D0
		gadget = "A1286EA66E83E0FEA3286EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E28, eax
		#retn


  def test_gadget_sub_6E776410(self):
		#sub_6E776410
		gadget = "A1306EA66E83E0FEA3306EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E30, eax
		#retn


  def test_gadget_sub_6E776450(self):
		#sub_6E776450
		gadget = "A1386EA66E83E0FEA3386EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E38, eax
		#retn


  def test_gadget_sub_6E7766F0(self):
		#sub_6E7766F0
		gadget = "A1406EA66E83E0FEA3406EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E40, eax
		#retn


  def test_gadget_sub_6E776990(self):
		#sub_6E776990
		gadget = "A1486EA66E83E0FEA3486EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E48, eax
		#retn


  def test_gadget_sub_6E776EB0(self):
		#sub_6E776EB0
		gadget = "A1586EA66E83E0FEA3586EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E58, eax
		#retn


  def test_gadget_sub_6E779048(self):
		#sub_6E779048
		gadget = "A1706EA66E83E0FEA3706EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E70, eax
		#retn


  def test_gadget_sub_6E779061(self):
		#sub_6E779061
		gadget = "A1706EA66E83E0FDA3706EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E70
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66E70, eax
		#retn


  def test_gadget_sub_6E77907A(self):
		#sub_6E77907A
		gadget = "A1706EA66E83E0FBA3706EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E70
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66E70, eax
		#retn


  def test_gadget_sub_6E779093(self):
		#sub_6E779093
		gadget = "A1706EA66E83E0F7A3706EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E70
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66E70, eax
		#retn


  def test_gadget_sub_6E7790AC(self):
		#sub_6E7790AC
		gadget = "A1706EA66E83E0EFA3706EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E70
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA66E70, eax
		#retn


  def test_gadget_sub_6E779E00(self):
		#sub_6E779E00
		gadget = "A1886EA66E83E0FEA3886EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E88
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E88, eax
		#retn


  def test_gadget_sub_6E77A0DC(self):
		#sub_6E77A0DC
		gadget = "A1906EA66E83E0FEA3906EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E90, eax
		#retn


  def test_gadget_sub_6E77A3D0(self):
		#sub_6E77A3D0
		gadget = "A1986EA66E83E0FEA3986EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66E98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66E98, eax
		#retn


  def test_gadget_sub_6E77A410(self):
		#sub_6E77A410
		gadget = "A1A06EA66E83E0FEA3A06EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EA0, eax
		#retn


  def test_gadget_sub_6E77A778(self):
		#sub_6E77A778
		gadget = "A1A86EA66E83E0FEA3A86EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EA8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EA8, eax
		#retn


  def test_gadget_sub_6E77A7B0(self):
		#sub_6E77A7B0
		gadget = "A1B86EA66E83E0FEA3B86EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EB8, eax
		#retn


  def test_gadget_sub_6E77A7C9(self):
		#sub_6E77A7C9
		gadget = "A1B86EA66E83E0FDA3B86EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EB8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66EB8, eax
		#retn


  def test_gadget_sub_6E77A7E2(self):
		#sub_6E77A7E2
		gadget = "A1B86EA66E83E0FBA3B86EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EB8
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66EB8, eax
		#retn


  def test_gadget_sub_6E77A828(self):
		#sub_6E77A828
		gadget = "A1C06EA66E83E0FEA3C06EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EC0, eax
		#retn


  def test_gadget_sub_6E77A890(self):
		#sub_6E77A890
		gadget = "A1C86EA66E83E0FEA3C86EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EC8, eax
		#retn


  def test_gadget_sub_6E77A8D0(self):
		#sub_6E77A8D0
		gadget = "A1D06EA66E83E0FEA3D06EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66ED0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66ED0, eax
		#retn


  def test_gadget_sub_6E77A910(self):
		#sub_6E77A910
		gadget = "A1DC6EA66E83E0FEA3DC6EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EDC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EDC, eax
		#retn


  def test_gadget_sub_6E77A929(self):
		#sub_6E77A929
		gadget = "A1DC6EA66E83E0FDA3DC6EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EDC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66EDC, eax
		#retn


  def test_gadget_sub_6E77AA10(self):
		#sub_6E77AA10
		gadget = "A1E46EA66E83E0FEA3E46EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EE4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EE4, eax
		#retn


  def test_gadget_sub_6E77AA80(self):
		#sub_6E77AA80
		gadget = "A1F46EA66E83E0FEA3F46EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EF4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EF4, eax
		#retn


  def test_gadget_sub_6E77AA99(self):
		#sub_6E77AA99
		gadget = "A1F46EA66E83E0FDA3F46EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EF4
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66EF4, eax
		#retn


  def test_gadget_sub_6E77AAB2(self):
		#sub_6E77AAB2
		gadget = "A1F46EA66E83E0FBA3F46EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EF4
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66EF4, eax
		#retn


  def test_gadget_sub_6E77AAF0(self):
		#sub_6E77AAF0
		gadget = "A1FC6EA66E83E0FEA3FC6EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66EFC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66EFC, eax
		#retn


  def test_gadget_sub_6E77CE80(self):
		#sub_6E77CE80
		gadget = "A1186FA66E83E0FEA3186FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F18, eax
		#retn


  def test_gadget_sub_6E77CE99(self):
		#sub_6E77CE99
		gadget = "A1186FA66E83E0FDA3186FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F18
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66F18, eax
		#retn


  def test_gadget_sub_6E77CEB2(self):
		#sub_6E77CEB2
		gadget = "A1186FA66E83E0FBA3186FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F18
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA66F18, eax
		#retn


  def test_gadget_sub_6E77CECB(self):
		#sub_6E77CECB
		gadget = "A1186FA66E83E0F7A3186FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F18
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA66F18, eax
		#retn


  def test_gadget_sub_6E77EBB0(self):
		#sub_6E77EBB0
		gadget = "A1346FA66E83E0FEA3346FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F34
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F34, eax
		#retn


  def test_gadget_sub_6E77EBC9(self):
		#sub_6E77EBC9
		gadget = "A1346FA66E83E0FDA3346FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F34
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66F34, eax
		#retn


  def test_gadget_sub_6E781840(self):
		#sub_6E781840
		gadget = "A1446FA66E83E0FEA3446FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F44
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F44, eax
		#retn


  def test_gadget_sub_6E7820F0(self):
		#sub_6E7820F0
		gadget = "A1546FA66E83E0FEA3546FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F54, eax
		#retn


  def test_gadget_sub_6E782109(self):
		#sub_6E782109
		gadget = "A1546FA66E83E0FDA3546FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F54
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66F54, eax
		#retn


  def test_gadget_sub_6E783C00(self):
		#sub_6E783C00
		gadget = "A15C6FA66E83E0FEA35C6FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F5C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F5C, eax
		#retn


  def test_gadget_sub_6E784640(self):
		#sub_6E784640
		gadget = "A1646FA66E83E0FEA3646FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F64, eax
		#retn


  def test_gadget_sub_6E784810(self):
		#sub_6E784810
		gadget = "A16C6FA66E83E0FEA36C6FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F6C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F6C, eax
		#retn


  def test_gadget_sub_6E786350(self):
		#sub_6E786350
		gadget = "A1746FA66E83E0FEA3746FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F74
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F74, eax
		#retn


  def test_gadget_sub_6E786440(self):
		#sub_6E786440
		gadget = "A17C6FA66E83E0FEA37C6FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F7C, eax
		#retn


  def test_gadget_sub_6E7864F0(self):
		#sub_6E7864F0
		gadget = "A1846FA66E83E0FEA3846FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F84, eax
		#retn


  def test_gadget_sub_6E7867B0(self):
		#sub_6E7867B0
		gadget = "A1906FA66E83E0FEA3906FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F90, eax
		#retn


  def test_gadget_sub_6E786E80(self):
		#sub_6E786E80
		gadget = "A1986FA66E83E0FEA3986FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66F98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66F98, eax
		#retn


  def test_gadget_sub_6E7872B0(self):
		#sub_6E7872B0
		gadget = "A1A46FA66E83E0FEA3A46FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FA4, eax
		#retn


  def test_gadget_sub_6E7872C9(self):
		#sub_6E7872C9
		gadget = "A1A46FA66E83E0FDA3A46FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FA4
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66FA4, eax
		#retn


  def test_gadget_sub_6E787518(self):
		#sub_6E787518
		gadget = "A1AC6FA66E83E0FEA3AC6FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FAC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FAC, eax
		#retn


  def test_gadget_sub_6E787E80(self):
		#sub_6E787E80
		gadget = "A1B86FA66E83E0FEA3B86FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FB8, eax
		#retn


  def test_gadget_sub_6E787E99(self):
		#sub_6E787E99
		gadget = "A1B86FA66E83E0FDA3B86FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FB8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA66FB8, eax
		#retn


  def test_gadget_sub_6E787FB0(self):
		#sub_6E787FB0
		gadget = "A1C06FA66E83E0FEA3C06FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FC0, eax
		#retn


  def test_gadget_sub_6E788340(self):
		#sub_6E788340
		gadget = "A1C86FA66E83E0FEA3C86FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FC8, eax
		#retn


  def test_gadget_unknown_libname_40(self):
		#unknown_libname_40
		gadget = "8B45F050E8D020A0FF59C3"
		self.do(gadget)

		#mov     eax, [ebp-10h]
		#push    eax             ; void *
		#call    j_free
		#pop     ecx
		#retn


  def test_gadget_sub_6E78946C(self):
		#sub_6E78946C
		gadget = "A1EC6FA66E83E0FEA3EC6FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FEC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FEC, eax
		#retn


  def test_gadget_sub_6E7894E8(self):
		#sub_6E7894E8
		gadget = "A1F46FA66E83E0FEA3F46FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA66FF4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA66FF4, eax
		#retn


  def test_gadget_sub_6E789A40(self):
		#sub_6E789A40
		gadget = "A10C70A66E83E0FEA30C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6700C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6700C, eax
		#retn


  def test_gadget_sub_6E789A4E(self):
		#sub_6E789A4E
		gadget = "A10C70A66E83E0FDA30C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6700C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6700C, eax
		#retn


  def test_gadget_sub_6E789A5C(self):
		#sub_6E789A5C
		gadget = "A10C70A66E83E0FBA30C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6700C
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA6700C, eax
		#retn


  def test_gadget_sub_6E789A6A(self):
		#sub_6E789A6A
		gadget = "A10C70A66E83E0F7A30C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6700C
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA6700C, eax
		#retn


  def test_gadget_sub_6E789A78(self):
		#sub_6E789A78
		gadget = "A10C70A66E83E0EFA30C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6700C
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA6700C, eax
		#retn


  def test_gadget_sub_6E789D33(self):
		#sub_6E789D33
		gadget = "A11870A66E83E0FEA31870A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67018
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67018, eax
		#retn


  def test_gadget_sub_6E78B9A0(self):
		#sub_6E78B9A0
		gadget = "A12C70A66E83E0FEA32C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6702C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6702C, eax
		#retn


  def test_gadget_sub_6E78B9E0(self):
		#sub_6E78B9E0
		gadget = "A13470A66E83E0FEA33470A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67034
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67034, eax
		#retn


  def test_gadget_sub_6E78BA20(self):
		#sub_6E78BA20
		gadget = "A13C70A66E83E0FEA33C70A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6703C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6703C, eax
		#retn


  def test_gadget_sub_6E78BAF0(self):
		#sub_6E78BAF0
		gadget = "A14470A66E83E0FEA34470A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67044
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67044, eax
		#retn


  def test_gadget_sub_6E78DA60(self):
		#sub_6E78DA60
		gadget = "A16070A66E83E0FEA36070A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67060
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67060, eax
		#retn


  def test_gadget_sub_6E78E0B0(self):
		#sub_6E78E0B0
		gadget = "A1AC76A66E83E0FEA3AC76A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676AC, eax
		#retn


  def test_gadget_sub_6E78E0BE(self):
		#sub_6E78E0BE
		gadget = "A1AC76A66E83E0FDA3AC76A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676AC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA676AC, eax
		#retn


  def test_gadget_sub_6E78E0CC(self):
		#sub_6E78E0CC
		gadget = "A1AC76A66E83E0FBA3AC76A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676AC
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA676AC, eax
		#retn


  def test_gadget_sub_6E78E0DA(self):
		#sub_6E78E0DA
		gadget = "A1AC76A66E83E0F7A3AC76A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676AC
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA676AC, eax
		#retn


  def test_gadget_unknown_libname_41(self):
		#unknown_libname_41
		gadget = "8B45F050E809C09FFF59C3"
		self.do(gadget)

		#mov     eax, [ebp-10h]
		#push    eax             ; void *
		#call    j_free
		#pop     ecx
		#retn


  def test_gadget_sub_6E78F120(self):
		#sub_6E78F120
		gadget = "A1C876A66E83E0FEA3C876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676C8, eax
		#retn


  def test_gadget_sub_6E78F139(self):
		#sub_6E78F139
		gadget = "A1C876A66E83E0FDA3C876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676C8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA676C8, eax
		#retn


  def test_gadget_sub_6E78F152(self):
		#sub_6E78F152
		gadget = "A1C876A66E83E0FBA3C876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676C8
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA676C8, eax
		#retn


  def test_gadget_sub_6E78F16B(self):
		#sub_6E78F16B
		gadget = "A1C876A66E83E0F7A3C876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676C8
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA676C8, eax
		#retn


  def test_gadget_sub_6E78F184(self):
		#sub_6E78F184
		gadget = "A1C876A66E83E0EFA3C876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676C8
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA676C8, eax
		#retn


  def test_gadget_sub_6E78F19D(self):
		#sub_6E78F19D
		gadget = "A1C876A66E83E0DFA3C876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676C8
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA676C8, eax
		#retn


  def test_gadget_sub_6E78FE20(self):
		#sub_6E78FE20
		gadget = "A1D076A66E83E0FEA3D076A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676D0, eax
		#retn


  def test_gadget_sub_6E78FE90(self):
		#sub_6E78FE90
		gadget = "A1D876A66E83E0FEA3D876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676D8, eax
		#retn


  def test_gadget_sub_6E78FF00(self):
		#sub_6E78FF00
		gadget = "A1E076A66E83E0FEA3E076A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676E0, eax
		#retn


  def test_gadget_sub_6E78FF40(self):
		#sub_6E78FF40
		gadget = "A1E876A66E83E0FEA3E876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676E8, eax
		#retn


  def test_gadget_sub_6E78FF80(self):
		#sub_6E78FF80
		gadget = "A1F076A66E83E0FEA3F076A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676F0, eax
		#retn


  def test_gadget_sub_6E78FFD0(self):
		#sub_6E78FFD0
		gadget = "A1F876A66E83E0FEA3F876A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA676F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA676F8, eax
		#retn


  def test_gadget_sub_6E791580(self):
		#sub_6E791580
		gadget = "A10477A66E83E0FEA30477A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67704
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67704, eax
		#retn


  def test_gadget_sub_6E7915B0(self):
		#sub_6E7915B0
		gadget = "A10C77A66E83E0FEA30C77A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6770C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6770C, eax
		#retn


  def test_gadget_sub_6E792780(self):
		#sub_6E792780
		gadget = "A12077A66E83E0FEA32077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67720
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67720, eax
		#retn


  def test_gadget_sub_6E792799(self):
		#sub_6E792799
		gadget = "A12077A66E83E0FDA32077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67720
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67720, eax
		#retn


  def test_gadget_sub_6E7927B2(self):
		#sub_6E7927B2
		gadget = "A12077A66E83E0FBA32077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67720
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA67720, eax
		#retn


  def test_gadget_sub_6E7927CB(self):
		#sub_6E7927CB
		gadget = "A12077A66E83E0F7A32077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67720
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA67720, eax
		#retn


  def test_gadget_sub_6E792830(self):
		#sub_6E792830
		gadget = "A12877A66E83E0FEA32877A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67728
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67728, eax
		#retn


  def test_gadget_sub_6E794720(self):
		#sub_6E794720
		gadget = "A15C77A66E83E0FEA35C77A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6775C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6775C, eax
		#retn


  def test_gadget_sub_6E794750(self):
		#sub_6E794750
		gadget = "A16477A66E83E0FEA36477A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67764
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67764, eax
		#retn


  def test_gadget_sub_6E795480(self):
		#sub_6E795480
		gadget = "A19077A66E83E0FEA39077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67790
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67790, eax
		#retn


  def test_gadget_sub_6E795499(self):
		#sub_6E795499
		gadget = "A19077A66E83E0FDA39077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67790
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67790, eax
		#retn


  def test_gadget_sub_6E7954B2(self):
		#sub_6E7954B2
		gadget = "A19077A66E83E0FBA39077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67790
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA67790, eax
		#retn


  def test_gadget_sub_6E7954CB(self):
		#sub_6E7954CB
		gadget = "A19077A66E83E0F7A39077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67790
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA67790, eax
		#retn


  def test_gadget_sub_6E795C70(self):
		#sub_6E795C70
		gadget = "A19877A66E83E0FEA39877A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67798
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67798, eax
		#retn


  def test_gadget_sub_6E796090(self):
		#sub_6E796090
		gadget = "A1A077A66E83E0FEA3A077A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA677A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA677A0, eax
		#retn


  def test_gadget_sub_6E7962C0(self):
		#sub_6E7962C0
		gadget = "A1B877A66E83E0FEA3B877A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA677B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA677B8, eax
		#retn


  def test_gadget_sub_6E796570(self):
		#sub_6E796570
		gadget = "A13478A66E83E0FEA33478A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67834
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67834, eax
		#retn


  def test_gadget_sub_6E7965A0(self):
		#sub_6E7965A0
		gadget = "A13C78A66E83E0FEA33C78A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6783C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6783C, eax
		#retn


  def test_gadget_sub_6E7965D0(self):
		#sub_6E7965D0
		gadget = "A14478A66E83E0FEA34478A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67844
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67844, eax
		#retn


  def test_gadget_sub_6E796760(self):
		#sub_6E796760
		gadget = "A14C78A66E83E0FEA34C78A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6784C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6784C, eax
		#retn


  def test_gadget_sub_6E796CC0(self):
		#sub_6E796CC0
		gadget = "A16478A66E83E0FEA36478A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67864
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67864, eax
		#retn


  def test_gadget_sub_6E796D70(self):
		#sub_6E796D70
		gadget = "A17878A66E83E0FEA37878A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67878
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67878, eax
		#retn


  def test_gadget_sub_6E796D7E(self):
		#sub_6E796D7E
		gadget = "A17878A66E83E0FDA37878A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67878
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67878, eax
		#retn


  def test_gadget_sub_6E796D8C(self):
		#sub_6E796D8C
		gadget = "A17878A66E83E0FBA37878A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67878
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA67878, eax
		#retn


  def test_gadget_sub_6E796D9A(self):
		#sub_6E796D9A
		gadget = "A17878A66E83E0F7A37878A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67878
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA67878, eax
		#retn


  def test_gadget_sub_6E796F50(self):
		#sub_6E796F50
		gadget = "A18078A66E83E0FEA38078A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67880
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67880, eax
		#retn


  def test_gadget_sub_6E796F90(self):
		#sub_6E796F90
		gadget = "A18878A66E83E0FEA38878A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67888
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67888, eax
		#retn


  def test_gadget_sub_6E7979E0(self):
		#sub_6E7979E0
		gadget = "A19878A66E83E0FEA39878A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67898
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67898, eax
		#retn


  def test_gadget_sub_6E797A70(self):
		#sub_6E797A70
		gadget = "A1B478A66E83E0FEA3B478A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678B4, eax
		#retn


  def test_gadget_sub_6E797AD0(self):
		#sub_6E797AD0
		gadget = "A1BC78A66E83E0FEA3BC78A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678BC, eax
		#retn


  def test_gadget_sub_6E798910(self):
		#sub_6E798910
		gadget = "A1D478A66E83E0FEA3D478A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678D4, eax
		#retn


  def test_gadget_sub_6E798A60(self):
		#sub_6E798A60
		gadget = "A1DC78A66E83E0FEA3DC78A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678DC, eax
		#retn


  def test_gadget_sub_6E798DD0(self):
		#sub_6E798DD0
		gadget = "A1E478A66E83E0FEA3E478A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678E4, eax
		#retn


  def test_gadget_sub_6E798E70(self):
		#sub_6E798E70
		gadget = "A1F078A66E83E0FEA3F078A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678F0, eax
		#retn


  def test_gadget_sub_6E798E7E(self):
		#sub_6E798E7E
		gadget = "A1F078A66E83E0FDA3F078A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678F0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA678F0, eax
		#retn


  def test_gadget_sub_6E7994F0(self):
		#sub_6E7994F0
		gadget = "A1FC78A66E83E0FEA3FC78A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA678FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA678FC, eax
		#retn


  def test_gadget_sub_6E799530(self):
		#sub_6E799530
		gadget = "A10479A66E83E0FEA30479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67904
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67904, eax
		#retn


  def test_gadget_sub_6E799591(self):
		#sub_6E799591
		gadget = "A10C79A66E83E0FEA30C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6790C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6790C, eax
		#retn


  def test_gadget_sub_6E799620(self):
		#sub_6E799620
		gadget = "A11479A66E83E0FEA31479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67914
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67914, eax
		#retn


  def test_gadget_sub_6E799650(self):
		#sub_6E799650
		gadget = "A11C79A66E83E0FEA31C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6791C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6791C, eax
		#retn


  def test_gadget_sub_6E799710(self):
		#sub_6E799710
		gadget = "A12479A66E83E0FEA32479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67924
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67924, eax
		#retn


  def test_gadget_sub_6E799800(self):
		#sub_6E799800
		gadget = "A12C79A66E83E0FEA32C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6792C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6792C, eax
		#retn


  def test_gadget_sub_6E799938(self):
		#sub_6E799938
		gadget = "A13479A66E83E0FEA33479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67934
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67934, eax
		#retn


  def test_gadget_sub_6E799978(self):
		#sub_6E799978
		gadget = "A13C79A66E83E0FEA33C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6793C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6793C, eax
		#retn


  def test_gadget_sub_6E7999C8(self):
		#sub_6E7999C8
		gadget = "A14479A66E83E0FEA34479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67944
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67944, eax
		#retn


  def test_gadget_sub_6E799A30(self):
		#sub_6E799A30
		gadget = "A14C79A66E83E0FEA34C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6794C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6794C, eax
		#retn


  def test_gadget_sub_6E799A88(self):
		#sub_6E799A88
		gadget = "A15879A66E83E0FEA35879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67958
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67958, eax
		#retn


  def test_gadget_sub_6E799AA6(self):
		#sub_6E799AA6
		gadget = "A15879A66E83E0FDA35879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67958
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67958, eax
		#retn


  def test_gadget_sub_6E799AE0(self):
		#sub_6E799AE0
		gadget = "A16079A66E83E0FEA36079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67960
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67960, eax
		#retn


  def test_gadget_sub_6E799B20(self):
		#sub_6E799B20
		gadget = "A16879A66E83E0FEA36879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67968
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67968, eax
		#retn


  def test_gadget_sub_6E799B60(self):
		#sub_6E799B60
		gadget = "A17079A66E83E0FEA37079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67970
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67970, eax
		#retn


  def test_gadget_sub_6E799BB8(self):
		#sub_6E799BB8
		gadget = "A17879A66E83E0FEA37879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67978
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67978, eax
		#retn


  def test_gadget_sub_6E799D73(self):
		#sub_6E799D73
		gadget = "A18079A66E83E0FEA38079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67980
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67980, eax
		#retn


  def test_gadget_sub_6E799E2B(self):
		#sub_6E799E2B
		gadget = "A18879A66E83E0FEA38879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67988
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67988, eax
		#retn


  def test_gadget_sub_6E799ED0(self):
		#sub_6E799ED0
		gadget = "A19C79A66E83E0FDA39C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6799C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6799C, eax
		#retn


  def test_gadget_sub_6E799EDE(self):
		#sub_6E799EDE
		gadget = "A19C79A66E83E0FEA39C79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6799C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6799C, eax
		#retn


  def test_gadget_sub_6E79A090(self):
		#sub_6E79A090
		gadget = "A1A479A66E83E0FEA3A479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679A4, eax
		#retn


  def test_gadget_sub_6E79A170(self):
		#sub_6E79A170
		gadget = "A1AC79A66E83E0FEA3AC79A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679AC, eax
		#retn


  def test_gadget_sub_6E79A1D0(self):
		#sub_6E79A1D0
		gadget = "A1B479A66E83E0FEA3B479A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679B4, eax
		#retn


  def test_gadget_sub_6E79A240(self):
		#sub_6E79A240
		gadget = "A1C079A66E83E0FEA3C079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679C0, eax
		#retn


  def test_gadget_sub_6E79A24E(self):
		#sub_6E79A24E
		gadget = "A1C079A66E83E0FDA3C079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679C0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA679C0, eax
		#retn


  def test_gadget_sub_6E79A28B(self):
		#sub_6E79A28B
		gadget = "A1C879A66E83E0FEA3C879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679C8, eax
		#retn


  def test_gadget_sub_6E79A73B(self):
		#sub_6E79A73B
		gadget = "A1D079A66E83E0FEA3D079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679D0, eax
		#retn


  def test_gadget_sub_6E79A78B(self):
		#sub_6E79A78B
		gadget = "A1D879A66E83E0FEA3D879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679D8, eax
		#retn


  def test_gadget_sub_6E79ADD0(self):
		#sub_6E79ADD0
		gadget = "A1E079A66E83E0FEA3E079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679E0, eax
		#retn


  def test_gadget_sub_6E79B280(self):
		#sub_6E79B280
		gadget = "A1E879A66E83E0FEA3E879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679E8, eax
		#retn


  def test_gadget_sub_6E79B2D0(self):
		#sub_6E79B2D0
		gadget = "A1F079A66E83E0FEA3F079A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679F0, eax
		#retn


  def test_gadget_sub_6E79B380(self):
		#sub_6E79B380
		gadget = "A1F879A66E83E0FEA3F879A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA679F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA679F8, eax
		#retn


  def test_gadget_sub_6E79B7C0(self):
		#sub_6E79B7C0
		gadget = "A1007AA66E83E0FEA3007AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A00, eax
		#retn


  def test_gadget_sub_6E79B900(self):
		#sub_6E79B900
		gadget = "A1287AA66E83E0FEA3287AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A28, eax
		#retn


  def test_gadget_sub_6E79B9A0(self):
		#sub_6E79B9A0
		gadget = "A1387AA66E83E0FEA3387AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A38, eax
		#retn


  def test_gadget_sub_6E79B9D0(self):
		#sub_6E79B9D0
		gadget = "A1407AA66E83E0FEA3407AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A40, eax
		#retn


  def test_gadget_sub_6E79BA00(self):
		#sub_6E79BA00
		gadget = "A1487AA66E83E0FEA3487AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A48, eax
		#retn


  def test_gadget_sub_6E79BA30(self):
		#sub_6E79BA30
		gadget = "A1507AA66E83E0FEA3507AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A50, eax
		#retn


  def test_gadget_sub_6E79BA60(self):
		#sub_6E79BA60
		gadget = "A1587AA66E83E0FEA3587AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A58, eax
		#retn


  def test_gadget_sub_6E79BA90(self):
		#sub_6E79BA90
		gadget = "A1307AA66E83E0FEA3307AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A30, eax
		#retn


  def test_gadget_sub_6E79BA9E(self):
		#sub_6E79BA9E
		gadget = "A1607AA66E83E0FEA3607AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A60, eax
		#retn


  def test_gadget_sub_6E79BAD0(self):
		#sub_6E79BAD0
		gadget = "A1307AA66E83E0FEA3307AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A30, eax
		#retn


  def test_gadget_sub_6E79BADE(self):
		#sub_6E79BADE
		gadget = "A17C7AA66E83E0FEA37C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A7C, eax
		#retn


  def test_gadget_sub_6E79BAEC(self):
		#sub_6E79BAEC
		gadget = "A17C7AA66E83E0FDA37C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A7C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67A7C, eax
		#retn


  def test_gadget_sub_6E79BAFA(self):
		#sub_6E79BAFA
		gadget = "A17C7AA66E83E0FBA37C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A7C
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA67A7C, eax
		#retn


  def test_gadget_sub_6E79BB08(self):
		#sub_6E79BB08
		gadget = "A17C7AA66E83E0F7A37C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A7C
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA67A7C, eax
		#retn


  def test_gadget_sub_6E79BB16(self):
		#sub_6E79BB16
		gadget = "A17C7AA66E83E0EFA37C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A7C
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA67A7C, eax
		#retn


  def test_gadget_sub_6E79BB24(self):
		#sub_6E79BB24
		gadget = "A17C7AA66E83E0DFA37C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A7C
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA67A7C, eax
		#retn


  def test_gadget_sub_6E79BB70(self):
		#sub_6E79BB70
		gadget = "A18C7AA66E83E0FEA38C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A8C, eax
		#retn


  def test_gadget_sub_6E79BBA0(self):
		#sub_6E79BBA0
		gadget = "A19C7AA66E83E0FEA39C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A9C, eax
		#retn


  def test_gadget_sub_6E79BBD0(self):
		#sub_6E79BBD0
		gadget = "A1A47AA66E83E0FEA3A47AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67AA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67AA4, eax
		#retn


  def test_gadget_sub_6E79BC10(self):
		#sub_6E79BC10
		gadget = "A18C7AA66E83E0FEA38C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A8C, eax
		#retn


  def test_gadget_sub_6E79BCE0(self):
		#sub_6E79BCE0
		gadget = "A1D87AA66E83E0FEA3D87AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67AD8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67AD8, eax
		#retn


  def test_gadget_sub_6E79BD20(self):
		#sub_6E79BD20
		gadget = "A19C7AA66E83E0FEA39C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A9C, eax
		#retn


  def test_gadget_sub_6E79BD50(self):
		#sub_6E79BD50
		gadget = "A1947AA66E83E0FEA3947AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A94, eax
		#retn


  def test_gadget_sub_6E79BDA1(self):
		#sub_6E79BDA1
		gadget = "A19C7AA66E83E0FEA39C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A9C, eax
		#retn


  def test_gadget_sub_6E79BDB7(self):
		#sub_6E79BDB7
		gadget = "A1947AA66E83E0FEA3947AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A94, eax
		#retn


  def test_gadget_sub_6E79BDF0(self):
		#sub_6E79BDF0
		gadget = "A19C7AA66E83E0FEA39C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A9C, eax
		#retn


  def test_gadget_sub_6E79BDFE(self):
		#sub_6E79BDFE
		gadget = "A1A47AA66E83E0FEA3A47AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67AA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67AA4, eax
		#retn


  def test_gadget_sub_6E79BE30(self):
		#sub_6E79BE30
		gadget = "A18C7AA66E83E0FEA38C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A8C, eax
		#retn


  def test_gadget_sub_6E79BE60(self):
		#sub_6E79BE60
		gadget = "A1947AA66E83E0FEA3947AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A94, eax
		#retn


  def test_gadget_sub_6E79BE98(self):
		#sub_6E79BE98
		gadget = "A19C7AA66E83E0FEA39C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A9C, eax
		#retn


  def test_gadget_sub_6E79BEAE(self):
		#sub_6E79BEAE
		gadget = "A1947AA66E83E0FEA3947AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A94, eax
		#retn


  def test_gadget_sub_6E79C1D0(self):
		#sub_6E79C1D0
		gadget = "A11C7BA66E83E0FEA31C7BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B1C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B1C, eax
		#retn


  def test_gadget_sub_6E79C200(self):
		#sub_6E79C200
		gadget = "A1247BA66E83E0FEA3247BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B24
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B24, eax
		#retn


  def test_gadget_sub_6E79C280(self):
		#sub_6E79C280
		gadget = "A12C7BA66E83E0FEA32C7BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B2C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B2C, eax
		#retn


  def test_gadget_sub_6E79C2C0(self):
		#sub_6E79C2C0
		gadget = "A1347BA66E83E0FEA3347BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B34
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B34, eax
		#retn


  def test_gadget_sub_6E79C2F0(self):
		#sub_6E79C2F0
		gadget = "A13C7BA66E83E0FEA33C7BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B3C, eax
		#retn


  def test_gadget_sub_6E79C3B0(self):
		#sub_6E79C3B0
		gadget = "A1447BA66E83E0FEA3447BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B44
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B44, eax
		#retn


  def test_gadget_sub_6E79C3E0(self):
		#sub_6E79C3E0
		gadget = "A14C7BA66E83E0FEA34C7BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B4C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B4C, eax
		#retn


  def test_gadget_sub_6E79C451(self):
		#sub_6E79C451
		gadget = "A1547BA66E83E0FEA3547BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B54, eax
		#retn


  def test_gadget_sub_6E79C480(self):
		#sub_6E79C480
		gadget = "A1607BA66E83E0FEA3607BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B60, eax
		#retn


  def test_gadget_sub_6E79C4B0(self):
		#sub_6E79C4B0
		gadget = "A1707BA66E83E0FEA3707BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B70, eax
		#retn


  def test_gadget_sub_6E79C4E0(self):
		#sub_6E79C4E0
		gadget = "A1807BA66E83E0FEA3807BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B80, eax
		#retn


  def test_gadget_sub_6E79C510(self):
		#sub_6E79C510
		gadget = "A1907BA66E83E0FEA3907BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67B90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67B90, eax
		#retn


  def test_gadget_sub_6E79C540(self):
		#sub_6E79C540
		gadget = "A1A07BA66E83E0FEA3A07BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67BA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67BA0, eax
		#retn


  def test_gadget_sub_6E79C570(self):
		#sub_6E79C570
		gadget = "A1B07BA66E83E0FEA3B07BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67BB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67BB0, eax
		#retn


  def test_gadget_sub_6E79C5A0(self):
		#sub_6E79C5A0
		gadget = "A1C07BA66E83E0FEA3C07BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67BC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67BC0, eax
		#retn


  def test_gadget_sub_6E79C5D0(self):
		#sub_6E79C5D0
		gadget = "A1D07BA66E83E0FEA3D07BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67BD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67BD0, eax
		#retn


  def test_gadget_sub_6E79C600(self):
		#sub_6E79C600
		gadget = "A1E07BA66E83E0FEA3E07BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67BE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67BE0, eax
		#retn


  def test_gadget_sub_6E79C630(self):
		#sub_6E79C630
		gadget = "A1F07BA66E83E0FEA3F07BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67BF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67BF0, eax
		#retn


  def test_gadget_sub_6E79C660(self):
		#sub_6E79C660
		gadget = "A1007CA66E83E0FEA3007CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C00, eax
		#retn


  def test_gadget_sub_6E79C690(self):
		#sub_6E79C690
		gadget = "A1107CA66E83E0FEA3107CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C10, eax
		#retn


  def test_gadget_sub_6E79C6C0(self):
		#sub_6E79C6C0
		gadget = "A1207CA66E83E0FEA3207CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C20, eax
		#retn


  def test_gadget_sub_6E79C6F0(self):
		#sub_6E79C6F0
		gadget = "A1307CA66E83E0FEA3307CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C30, eax
		#retn


  def test_gadget_sub_6E79C720(self):
		#sub_6E79C720
		gadget = "A1407CA66E83E0FEA3407CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C40, eax
		#retn


  def test_gadget_sub_6E79C750(self):
		#sub_6E79C750
		gadget = "A1507CA66E83E0FEA3507CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C50, eax
		#retn


  def test_gadget_sub_6E79C780(self):
		#sub_6E79C780
		gadget = "A1607CA66E83E0FEA3607CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C60, eax
		#retn


  def test_gadget_sub_6E79C7B0(self):
		#sub_6E79C7B0
		gadget = "A1707CA66E83E0FEA3707CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C70, eax
		#retn


  def test_gadget_sub_6E79C7E0(self):
		#sub_6E79C7E0
		gadget = "A1807CA66E83E0FEA3807CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C80, eax
		#retn


  def test_gadget_sub_6E79C810(self):
		#sub_6E79C810
		gadget = "A1907CA66E83E0FEA3907CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67C90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67C90, eax
		#retn


  def test_gadget_sub_6E79C840(self):
		#sub_6E79C840
		gadget = "A1A07CA66E83E0FEA3A07CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67CA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67CA0, eax
		#retn


  def test_gadget_sub_6E79C870(self):
		#sub_6E79C870
		gadget = "A1B07CA66E83E0FEA3B07CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67CB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67CB0, eax
		#retn


  def test_gadget_sub_6E79C8A0(self):
		#sub_6E79C8A0
		gadget = "A1C07CA66E83E0FEA3C07CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67CC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67CC0, eax
		#retn


  def test_gadget_sub_6E79C8D0(self):
		#sub_6E79C8D0
		gadget = "A1D07CA66E83E0FEA3D07CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67CD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67CD0, eax
		#retn


  def test_gadget_sub_6E79C900(self):
		#sub_6E79C900
		gadget = "A1E07CA66E83E0FEA3E07CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67CE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67CE0, eax
		#retn


  def test_gadget_sub_6E79C930(self):
		#sub_6E79C930
		gadget = "A1F07CA66E83E0FEA3F07CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67CF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67CF0, eax
		#retn


  def test_gadget_sub_6E79C960(self):
		#sub_6E79C960
		gadget = "A1007DA66E83E0FEA3007DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D00, eax
		#retn


  def test_gadget_sub_6E79C990(self):
		#sub_6E79C990
		gadget = "A1107DA66E83E0FEA3107DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D10, eax
		#retn


  def test_gadget_sub_6E79C9C0(self):
		#sub_6E79C9C0
		gadget = "A1207DA66E83E0FEA3207DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D20, eax
		#retn


  def test_gadget_sub_6E79C9F0(self):
		#sub_6E79C9F0
		gadget = "A1307DA66E83E0FEA3307DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D30, eax
		#retn


  def test_gadget_sub_6E79CA20(self):
		#sub_6E79CA20
		gadget = "A1407DA66E83E0FEA3407DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D40, eax
		#retn


  def test_gadget_sub_6E79CA50(self):
		#sub_6E79CA50
		gadget = "A1507DA66E83E0FEA3507DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D50, eax
		#retn


  def test_gadget_sub_6E79CA80(self):
		#sub_6E79CA80
		gadget = "A1607DA66E83E0FEA3607DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D60, eax
		#retn


  def test_gadget_sub_6E79CAB0(self):
		#sub_6E79CAB0
		gadget = "A1707DA66E83E0FEA3707DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D70, eax
		#retn


  def test_gadget_sub_6E79CAE0(self):
		#sub_6E79CAE0
		gadget = "A1807DA66E83E0FEA3807DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D80, eax
		#retn


  def test_gadget_sub_6E79CB10(self):
		#sub_6E79CB10
		gadget = "A1907DA66E83E0FEA3907DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67D90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67D90, eax
		#retn


  def test_gadget_sub_6E79CB40(self):
		#sub_6E79CB40
		gadget = "A1A07DA66E83E0FEA3A07DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67DA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67DA0, eax
		#retn


  def test_gadget_sub_6E79CB70(self):
		#sub_6E79CB70
		gadget = "A1B07DA66E83E0FEA3B07DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67DB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67DB0, eax
		#retn


  def test_gadget_sub_6E79CBA0(self):
		#sub_6E79CBA0
		gadget = "A1C07DA66E83E0FEA3C07DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67DC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67DC0, eax
		#retn


  def test_gadget_sub_6E79CBD0(self):
		#sub_6E79CBD0
		gadget = "A1D07DA66E83E0FEA3D07DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67DD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67DD0, eax
		#retn


  def test_gadget_sub_6E79CC00(self):
		#sub_6E79CC00
		gadget = "A1E07DA66E83E0FEA3E07DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67DE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67DE0, eax
		#retn


  def test_gadget_sub_6E79CC30(self):
		#sub_6E79CC30
		gadget = "A1F07DA66E83E0FEA3F07DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67DF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67DF0, eax
		#retn


  def test_gadget_sub_6E79CC60(self):
		#sub_6E79CC60
		gadget = "A1007EA66E83E0FEA3007EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E00, eax
		#retn


  def test_gadget_sub_6E79CC98(self):
		#sub_6E79CC98
		gadget = "A1087EA66E83E0FEA3087EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E08, eax
		#retn


  def test_gadget_sub_6E79CD00(self):
		#sub_6E79CD00
		gadget = "A1187EA66E83E0FEA3187EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E18, eax
		#retn


  def test_gadget_sub_6E79CD0E(self):
		#sub_6E79CD0E
		gadget = "A1187EA66E83E0FDA3187EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E18
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67E18, eax
		#retn


  def test_gadget_sub_6E79CD1C(self):
		#sub_6E79CD1C
		gadget = "A1187EA66E83E0FBA3187EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E18
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA67E18, eax
		#retn


  def test_gadget_sub_6E79CDA0(self):
		#sub_6E79CDA0
		gadget = "A18C7AA66E83E0FEA38C7AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67A8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67A8C, eax
		#retn


  def test_gadget_sub_6E79CE30(self):
		#sub_6E79CE30
		gadget = "A1207EA66E83E0FEA3207EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E20, eax
		#retn


  def test_gadget_sub_6E79D060(self):
		#sub_6E79D060
		gadget = "A1487EA66E83E0FEA3487EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E48, eax
		#retn


  def test_gadget_sub_6E79D06E(self):
		#sub_6E79D06E
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D084(self):
		#sub_6E79D084
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D0B0(self):
		#sub_6E79D0B0
		gadget = "A1507EA66E83E0FEA3507EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E50, eax
		#retn


  def test_gadget_sub_6E79D0BE(self):
		#sub_6E79D0BE
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D0D4(self):
		#sub_6E79D0D4
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D100(self):
		#sub_6E79D100
		gadget = "A1587EA66E83E0FEA3587EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E58, eax
		#retn


  def test_gadget_sub_6E79D10E(self):
		#sub_6E79D10E
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D12C(self):
		#sub_6E79D12C
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D180(self):
		#sub_6E79D180
		gadget = "A1607EA66E83E0FEA3607EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E60, eax
		#retn


  def test_gadget_sub_6E79D18E(self):
		#sub_6E79D18E
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D1A4(self):
		#sub_6E79D1A4
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D1D0(self):
		#sub_6E79D1D0
		gadget = "A1687EA66E83E0FEA3687EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E68
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E68, eax
		#retn


  def test_gadget_sub_6E79D1DE(self):
		#sub_6E79D1DE
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D1F4(self):
		#sub_6E79D1F4
		gadget = "A1407EA66E83E0FEA3407EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67E40, eax
		#retn


  def test_gadget_sub_6E79D7E0(self):
		#sub_6E79D7E0
		gadget = "A1C87EA66E83E0FEA3C87EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67EC8, eax
		#retn


  def test_gadget_sub_6E79D810(self):
		#sub_6E79D810
		gadget = "A1D07EA66E83E0FEA3D07EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67ED0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67ED0, eax
		#retn


  def test_gadget_sub_6E79D840(self):
		#sub_6E79D840
		gadget = "A1D87EA66E83E0FEA3D87EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67ED8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67ED8, eax
		#retn


  def test_gadget_sub_6E79D870(self):
		#sub_6E79D870
		gadget = "A1E07EA66E83E0FEA3E07EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67EE0, eax
		#retn


  def test_gadget_sub_6E79D8A0(self):
		#sub_6E79D8A0
		gadget = "A1E87EA66E83E0FEA3E87EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EE8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67EE8, eax
		#retn


  def test_gadget_sub_6E79D8D0(self):
		#sub_6E79D8D0
		gadget = "A1F07EA66E83E0FEA3F07EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67EF0, eax
		#retn


  def test_gadget_sub_6E79D900(self):
		#sub_6E79D900
		gadget = "A1F87EA66E83E0FEA3F87EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67EF8, eax
		#retn


  def test_gadget_sub_6E79D930(self):
		#sub_6E79D930
		gadget = "A1007FA66E83E0FEA3007FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F00, eax
		#retn


  def test_gadget_sub_6E79D93E(self):
		#sub_6E79D93E
		gadget = "A1C87EA66E83E0FEA3C87EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67EC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67EC8, eax
		#retn


  def test_gadget_sub_6E79D980(self):
		#sub_6E79D980
		gadget = "A1087FA66E83E0FEA3087FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F08, eax
		#retn


  def test_gadget_sub_6E79D9B0(self):
		#sub_6E79D9B0
		gadget = "A1107FA66E83E0FEA3107FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F10, eax
		#retn


  def test_gadget_sub_6E79D9E0(self):
		#sub_6E79D9E0
		gadget = "A1187FA66E83E0FEA3187FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F18, eax
		#retn


  def test_gadget_sub_6E79DA10(self):
		#sub_6E79DA10
		gadget = "A1207FA66E83E0FEA3207FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F20, eax
		#retn


  def test_gadget_sub_6E79DA40(self):
		#sub_6E79DA40
		gadget = "A1287FA66E83E0FEA3287FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F28, eax
		#retn


  def test_gadget_sub_6E79DA70(self):
		#sub_6E79DA70
		gadget = "A1307FA66E83E0FEA3307FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F30, eax
		#retn


  def test_gadget_sub_6E79DAA0(self):
		#sub_6E79DAA0
		gadget = "A1387FA66E83E0FEA3387FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F38, eax
		#retn


  def test_gadget_sub_6E79DAD0(self):
		#sub_6E79DAD0
		gadget = "A1407FA66E83E0FEA3407FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F40, eax
		#retn


  def test_gadget_sub_6E79DAE6(self):
		#sub_6E79DAE6
		gadget = "A1387FA66E83E0FEA3387FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F38, eax
		#retn


  def test_gadget_sub_6E79DB30(self):
		#sub_6E79DB30
		gadget = "A1487FA66E83E0FEA3487FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F48, eax
		#retn


  def test_gadget_sub_6E79DB70(self):
		#sub_6E79DB70
		gadget = "A1507FA66E83E0FEA3507FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F50, eax
		#retn


  def test_gadget_sub_6E79DC90(self):
		#sub_6E79DC90
		gadget = "A1587FA66E83E0FEA3587FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F58, eax
		#retn


  def test_gadget_sub_6E79DD18(self):
		#sub_6E79DD18
		gadget = "A1647FA66E83E0FEA3647FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F64, eax
		#retn


  def test_gadget_sub_6E79DD26(self):
		#sub_6E79DD26
		gadget = "A1647FA66E83E0FDA3647FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F64
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67F64, eax
		#retn


  def test_gadget_sub_6E79DE00(self):
		#sub_6E79DE00
		gadget = "A1707FA66E83E0FEA3707FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F70, eax
		#retn


  def test_gadget_sub_6E79DE0E(self):
		#sub_6E79DE0E
		gadget = "A1707FA66E83E0FDA3707FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F70
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA67F70, eax
		#retn


  def test_gadget_sub_6E79DFA0(self):
		#sub_6E79DFA0
		gadget = "A1907FA66E83E0FEA3907FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67F90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67F90, eax
		#retn


  def test_gadget_sub_6E79E0B0(self):
		#sub_6E79E0B0
		gadget = "A1B87FA66E83E0FEA3B87FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67FB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67FB8, eax
		#retn


  def test_gadget_sub_6E79E350(self):
		#sub_6E79E350
		gadget = "A1F07FA66E83E0FEA3F07FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67FF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67FF0, eax
		#retn


  def test_gadget_sub_6E79E380(self):
		#sub_6E79E380
		gadget = "A1F87FA66E83E0FEA3F87FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA67FF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA67FF8, eax
		#retn


  def test_gadget_sub_6E79E3F3(self):
		#sub_6E79E3F3
		gadget = "A10080A66E83E0FEA30080A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68000
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68000, eax
		#retn


  def test_gadget_sub_6E79E420(self):
		#sub_6E79E420
		gadget = "A10880A66E83E0FEA30880A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68008
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68008, eax
		#retn


  def test_gadget_sub_6E79E460(self):
		#sub_6E79E460
		gadget = "A11080A66E83E0FEA31080A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68010
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68010, eax
		#retn


  def test_gadget_sub_6E79E4C0(self):
		#sub_6E79E4C0
		gadget = "A11880A66E83E0FEA31880A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68018
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68018, eax
		#retn


  def test_gadget_sub_6E79E550(self):
		#sub_6E79E550
		gadget = "A12080A66E83E0FEA32080A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68020
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68020, eax
		#retn


  def test_gadget_sub_6E79E590(self):
		#sub_6E79E590
		gadget = "A12C80A66E83E0FEA32C80A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6802C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6802C, eax
		#retn


  def test_gadget_sub_6E79E5BF(self):
		#sub_6E79E5BF
		gadget = "A12C80A66E83E0FDA32C80A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6802C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6802C, eax
		#retn


  def test_gadget_sub_6E79E630(self):
		#sub_6E79E630
		gadget = "A13480A66E83E0FEA33480A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68034
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68034, eax
		#retn


  def test_gadget_sub_6E79E660(self):
		#sub_6E79E660
		gadget = "A13C80A66E83E0FEA33C80A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6803C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6803C, eax
		#retn


  def test_gadget_sub_6E79E7C8(self):
		#sub_6E79E7C8
		gadget = "A14480A66E83E0FEA34480A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68044
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68044, eax
		#retn


  def test_gadget_sub_6E79E839(self):
		#sub_6E79E839
		gadget = "A14C80A66E83E0FEA34C80A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6804C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6804C, eax
		#retn


  def test_gadget_sub_6E79E8E0(self):
		#sub_6E79E8E0
		gadget = "A15C81A66E83E0FEA35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E8EE(self):
		#sub_6E79E8EE
		gadget = "A15C81A66E83E0FDA35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E8FC(self):
		#sub_6E79E8FC
		gadget = "A15C81A66E83E0FBA35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E90A(self):
		#sub_6E79E90A
		gadget = "A15C81A66E83E0F7A35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E918(self):
		#sub_6E79E918
		gadget = "A15C81A66E83E0EFA35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E926(self):
		#sub_6E79E926
		gadget = "A15C81A66E83E0DFA35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E934(self):
		#sub_6E79E934
		gadget = "A15C81A66E83E0BFA35C81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6815C
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA6815C, eax
		#retn


  def test_gadget_sub_6E79E970(self):
		#sub_6E79E970
		gadget = "A16881A66E83E0FEA36881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68168
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68168, eax
		#retn


  def test_gadget_sub_6E79E9C1(self):
		#sub_6E79E9C1
		gadget = "A17081A66E83E0FEA37081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68170
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68170, eax
		#retn


  def test_gadget_sub_6E79EA00(self):
		#sub_6E79EA00
		gadget = "A17881A66E83E0FEA37881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68178
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68178, eax
		#retn


  def test_gadget_sub_6E79EA38(self):
		#sub_6E79EA38
		gadget = "A18081A66E83E0FEA38081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68180
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68180, eax
		#retn


  def test_gadget_sub_6E79EA78(self):
		#sub_6E79EA78
		gadget = "A18881A66E83E0FEA38881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68188
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68188, eax
		#retn


  def test_gadget_sub_6E79EAB8(self):
		#sub_6E79EAB8
		gadget = "A19081A66E83E0FEA39081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68190
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68190, eax
		#retn


  def test_gadget_sub_6E79EAF8(self):
		#sub_6E79EAF8
		gadget = "A19881A66E83E0FEA39881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68198
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68198, eax
		#retn


  def test_gadget_sub_6E79EB38(self):
		#sub_6E79EB38
		gadget = "A1A081A66E83E0FEA3A081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681A0, eax
		#retn


  def test_gadget_sub_6E79EB70(self):
		#sub_6E79EB70
		gadget = "A1A881A66E83E0FEA3A881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681A8, eax
		#retn


  def test_gadget_sub_6E79EBA8(self):
		#sub_6E79EBA8
		gadget = "A1B081A66E83E0FEA3B081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681B0, eax
		#retn


  def test_gadget_sub_6E79EC00(self):
		#sub_6E79EC00
		gadget = "A1BC81A66E83E0FEA3BC81A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681BC, eax
		#retn


  def test_gadget_sub_6E79EC30(self):
		#sub_6E79EC30
		gadget = "A1C481A66E83E0FEA3C481A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681C4, eax
		#retn


  def test_gadget_sub_6E79EC68(self):
		#sub_6E79EC68
		gadget = "A1D081A66E83E0FEA3D081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681D0, eax
		#retn


  def test_gadget_sub_6E79EC7E(self):
		#sub_6E79EC7E
		gadget = "A1D081A66E83E0FDA3D081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681D0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA681D0, eax
		#retn


  def test_gadget_sub_6E79ED30(self):
		#sub_6E79ED30
		gadget = "A1D881A66E83E0FEA3D881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681D8, eax
		#retn


  def test_gadget_sub_6E79EDD0(self):
		#sub_6E79EDD0
		gadget = "A1E881A66E83E0FEA3E881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681E8, eax
		#retn


  def test_gadget_sub_6E79EE40(self):
		#sub_6E79EE40
		gadget = "A1F081A66E83E0FEA3F081A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681F0, eax
		#retn


  def test_gadget_sub_6E79EF60(self):
		#sub_6E79EF60
		gadget = "A1F881A66E83E0FEA3F881A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA681F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA681F8, eax
		#retn


  def test_gadget_sub_6E79F740(self):
		#sub_6E79F740
		gadget = "A1C882A66E83E0FEA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F759(self):
		#sub_6E79F759
		gadget = "A1C882A66E83E0FDA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F772(self):
		#sub_6E79F772
		gadget = "A1C882A66E83E0FBA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F78B(self):
		#sub_6E79F78B
		gadget = "A1C882A66E83E0F7A3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F7A4(self):
		#sub_6E79F7A4
		gadget = "A1C882A66E83E0EFA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F7BD(self):
		#sub_6E79F7BD
		gadget = "A1C882A66E83E0DFA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F7D6(self):
		#sub_6E79F7D6
		gadget = "A1C882A66E83E0BFA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79F7EF(self):
		#sub_6E79F7EF
		gadget = "A1C882A66E257FFFFFFFA3C882A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682C8
		#and     eax, 0FFFFFF7Fh
		#mov     dword_6EA682C8, eax
		#retn


  def test_gadget_sub_6E79FBE0(self):
		#sub_6E79FBE0
		gadget = "A1D082A66E83E0FEA3D082A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA682D0, eax
		#retn


  def test_gadget_sub_6E79FDC0(self):
		#sub_6E79FDC0
		gadget = "A1DC82A66E83E0FEA3DC82A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA682DC, eax
		#retn


  def test_gadget_sub_6E79FDF0(self):
		#sub_6E79FDF0
		gadget = "A1E482A66E83E0FEA3E482A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA682E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA682E4, eax
		#retn


  def test_gadget_sub_6E7A0250(self):
		#sub_6E7A0250
		gadget = "A10083A66E83E0FEA30083A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68300
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68300, eax
		#retn


  def test_gadget_sub_6E7A0269(self):
		#sub_6E7A0269
		gadget = "A10083A66E83E0FDA30083A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68300
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68300, eax
		#retn


  def test_gadget_sub_6E7A0282(self):
		#sub_6E7A0282
		gadget = "A10083A66E83E0FBA30083A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68300
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68300, eax
		#retn


  def test_gadget_sub_6E7A029B(self):
		#sub_6E7A029B
		gadget = "A10083A66E83E0F7A30083A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68300
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA68300, eax
		#retn


  def test_gadget_sub_6E7A02B4(self):
		#sub_6E7A02B4
		gadget = "A10083A66E83E0EFA30083A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68300
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA68300, eax
		#retn


  def test_gadget_sub_6E7A02CD(self):
		#sub_6E7A02CD
		gadget = "A10083A66E83E0DFA30083A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68300
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA68300, eax
		#retn


  def test_gadget_sub_6E7A0310(self):
		#sub_6E7A0310
		gadget = "A10C83A66E83E0FEA30C83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6830C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6830C, eax
		#retn


  def test_gadget_sub_6E7A0329(self):
		#sub_6E7A0329
		gadget = "A10C83A66E83E0FDA30C83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6830C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6830C, eax
		#retn


  def test_gadget_sub_6E7A0380(self):
		#sub_6E7A0380
		gadget = "A11483A66E83E0FEA31483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68314
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68314, eax
		#retn


  def test_gadget_sub_6E7A03C0(self):
		#sub_6E7A03C0
		gadget = "A11C83A66E83E0FEA31C83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6831C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6831C, eax
		#retn


  def test_gadget_sub_6E7A0400(self):
		#sub_6E7A0400
		gadget = "A12483A66E83E0FEA32483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68324
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68324, eax
		#retn


  def test_gadget_sub_6E7A0440(self):
		#sub_6E7A0440
		gadget = "A12C83A66E83E0FEA32C83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6832C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6832C, eax
		#retn


  def test_gadget_sub_6E7A0710(self):
		#sub_6E7A0710
		gadget = "A14883A66E83E0FEA34883A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68348
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68348, eax
		#retn


  def test_gadget_sub_6E7A0729(self):
		#sub_6E7A0729
		gadget = "A14883A66E83E0FDA34883A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68348
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68348, eax
		#retn


  def test_gadget_sub_6E7A0742(self):
		#sub_6E7A0742
		gadget = "A14883A66E83E0FBA34883A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68348
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68348, eax
		#retn


  def test_gadget_sub_6E7A075B(self):
		#sub_6E7A075B
		gadget = "A14883A66E83E0F7A34883A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68348
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA68348, eax
		#retn


  def test_gadget_sub_6E7A0774(self):
		#sub_6E7A0774
		gadget = "A14883A66E83E0EFA34883A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68348
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA68348, eax
		#retn


  def test_gadget_sub_6E7A07A5(self):
		#sub_6E7A07A5
		gadget = "A14883A66E83E0DFA34883A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68348
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA68348, eax
		#retn


  def test_gadget_sub_6E7A0EF0(self):
		#sub_6E7A0EF0
		gadget = "A18483A66E83E0FEA38483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68384
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68384, eax
		#retn


  def test_gadget_sub_6E7A0F20(self):
		#sub_6E7A0F20
		gadget = "A18C83A66E83E0FEA38C83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6838C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6838C, eax
		#retn


  def test_gadget_sub_6E7A0F50(self):
		#sub_6E7A0F50
		gadget = "A19483A66E83E0FEA39483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68394
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68394, eax
		#retn


  def test_gadget_sub_6E7A0F80(self):
		#sub_6E7A0F80
		gadget = "A19C83A66E83E0FEA39C83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6839C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6839C, eax
		#retn


  def test_gadget_sub_6E7A0FB0(self):
		#sub_6E7A0FB0
		gadget = "A1A483A66E83E0FEA3A483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683A4, eax
		#retn


  def test_gadget_sub_6E7A0FE0(self):
		#sub_6E7A0FE0
		gadget = "A1AC83A66E83E0FEA3AC83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683AC, eax
		#retn


  def test_gadget_sub_6E7A1020(self):
		#sub_6E7A1020
		gadget = "A1B483A66E83E0FEA3B483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683B4, eax
		#retn


  def test_gadget_sub_6E7A1070(self):
		#sub_6E7A1070
		gadget = "A1BC83A66E83E0FEA3BC83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683BC, eax
		#retn


  def test_gadget_sub_6E7A10C0(self):
		#sub_6E7A10C0
		gadget = "A1C483A66E83E0FEA3C483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683C4, eax
		#retn


  def test_gadget_sub_6E7A1100(self):
		#sub_6E7A1100
		gadget = "A1CC83A66E83E0FEA3CC83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683CC, eax
		#retn


  def test_gadget_sub_6E7A1170(self):
		#sub_6E7A1170
		gadget = "A1D483A66E83E0FEA3D483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683D4, eax
		#retn


  def test_gadget_sub_6E7A1230(self):
		#sub_6E7A1230
		gadget = "A1DC83A66E83E0FEA3DC83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683DC, eax
		#retn


  def test_gadget_sub_6E7A1260(self):
		#sub_6E7A1260
		gadget = "A1E483A66E83E0FEA3E483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683E4, eax
		#retn


  def test_gadget_sub_6E7A1A00(self):
		#sub_6E7A1A00
		gadget = "A1EC83A66E83E0FEA3EC83A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683EC, eax
		#retn


  def test_gadget_sub_6E7A1A30(self):
		#sub_6E7A1A30
		gadget = "A1F483A66E83E0FEA3F483A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA683F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA683F4, eax
		#retn


  def test_gadget_sub_6E7A1A60(self):
		#sub_6E7A1A60
		gadget = "A10084A66E83E0FEA30084A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68400
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68400, eax
		#retn


  def test_gadget_sub_6E7A1A90(self):
		#sub_6E7A1A90
		gadget = "A10C84A66E83E0FEA30C84A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6840C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6840C, eax
		#retn


  def test_gadget_sub_6E7A1AC0(self):
		#sub_6E7A1AC0
		gadget = "A11884A66E83E0FEA31884A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68418
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68418, eax
		#retn


  def test_gadget_sub_6E7A1AF0(self):
		#sub_6E7A1AF0
		gadget = "A12484A66E83E0FEA32484A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68424
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68424, eax
		#retn


  def test_gadget_sub_6E7A1B20(self):
		#sub_6E7A1B20
		gadget = "A13084A66E83E0FEA33084A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68430
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68430, eax
		#retn


  def test_gadget_sub_6E7A1B50(self):
		#sub_6E7A1B50
		gadget = "A13C84A66E83E0FEA33C84A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6843C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6843C, eax
		#retn


  def test_gadget_sub_6E7A1B80(self):
		#sub_6E7A1B80
		gadget = "A14884A66E83E0FEA34884A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68448
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68448, eax
		#retn


  def test_gadget_sub_6E7A1BB0(self):
		#sub_6E7A1BB0
		gadget = "A15484A66E83E0FEA35484A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68454
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68454, eax
		#retn


  def test_gadget_sub_6E7A1BE0(self):
		#sub_6E7A1BE0
		gadget = "A13C84A66E83E0FEA33C84A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6843C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6843C, eax
		#retn


  def test_gadget_sub_6E7A1CA0(self):
		#sub_6E7A1CA0
		gadget = "A17084A66E83E0FEA37084A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68470
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68470, eax
		#retn


  def test_gadget_sub_6E7A2AE0(self):
		#sub_6E7A2AE0
		gadget = "A17C84A66E83E0FEA37C84A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6847C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6847C, eax
		#retn


  def test_gadget_sub_6E7A2BC0(self):
		#sub_6E7A2BC0
		gadget = "A18884A66E83E0FEA38884A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68488
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68488, eax
		#retn


  def test_gadget_sub_6E7A44A2(self):
		#sub_6E7A44A2
		gadget = "A1A084A66E83E0FEA3A084A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA684A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA684A0, eax
		#retn


  def test_gadget_sub_6E7A44BB(self):
		#sub_6E7A44BB
		gadget = "A1A084A66E83E0FDA3A084A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA684A0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA684A0, eax
		#retn


  def test_gadget_sub_6E7A4C30(self):
		#sub_6E7A4C30
		gadget = "A1C884A66E83E0FEA3C884A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA684C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA684C8, eax
		#retn


  def test_gadget_sub_6E7A4E60(self):
		#sub_6E7A4E60
		gadget = "A1D084A66E83E0FEA3D084A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA684D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA684D0, eax
		#retn


  def test_gadget_sub_6E7A5460(self):
		#sub_6E7A5460
		gadget = "A1D884A66E83E0FEA3D884A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA684D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA684D8, eax
		#retn


  def test_gadget_sub_6E7A6C80(self):
		#sub_6E7A6C80
		gadget = "A10085A66E83E0FEA30085A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68500
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68500, eax
		#retn


  def test_gadget_sub_6E7A6D96(self):
		#sub_6E7A6D96
		gadget = "A10885A66E83E0FEA30885A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68508
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68508, eax
		#retn


  def test_gadget_sub_6E7A6FD0(self):
		#sub_6E7A6FD0
		gadget = "A11085A66E83E0FEA31085A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68510
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68510, eax
		#retn


  def test_gadget_sub_6E7A73DE(self):
		#sub_6E7A73DE
		gadget = "A11C85A66E83E0FEA31C85A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6851C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6851C, eax
		#retn


  def test_gadget_sub_6E7A73FA(self):
		#sub_6E7A73FA
		gadget = "A11C85A66E83E0FDA31C85A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6851C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6851C, eax
		#retn


  def test_gadget_sub_6E7A7640(self):
		#sub_6E7A7640
		gadget = "A12885A66E83E0FEA32885A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68528
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68528, eax
		#retn


  def test_gadget_sub_6E7A8AD8(self):
		#sub_6E7A8AD8
		gadget = "A13485A66E83E0FEA33485A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68534
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68534, eax
		#retn


  def test_gadget_sub_6E7A8AF1(self):
		#sub_6E7A8AF1
		gadget = "A13485A66E83E0FDA33485A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68534
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68534, eax
		#retn


  def test_gadget_sub_6E7AAD80(self):
		#sub_6E7AAD80
		gadget = "A19885A66E83E0FEA39885A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68598
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68598, eax
		#retn


  def test_gadget_sub_6E7AADB0(self):
		#sub_6E7AADB0
		gadget = "A1D085A66E83E0FEA3D085A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA685D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA685D0, eax
		#retn


  def test_gadget_sub_6E7AB310(self):
		#sub_6E7AB310
		gadget = "A15C86A66E83E0FEA35C86A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6865C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6865C, eax
		#retn


  def test_gadget_sub_6E7AB340(self):
		#sub_6E7AB340
		gadget = "A16486A66E83E0FEA36486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68664
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68664, eax
		#retn


  def test_gadget_sub_6E7AB950(self):
		#sub_6E7AB950
		gadget = "A16C86A66E83E0FEA36C86A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6866C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6866C, eax
		#retn


  def test_gadget_sub_6E7AC730(self):
		#sub_6E7AC730
		gadget = "A17C86A66E83E0FEA37C86A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6867C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6867C, eax
		#retn


  def test_gadget_sub_6E7ACF10(self):
		#sub_6E7ACF10
		gadget = "A18886A66E83E0FEA38886A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68688
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68688, eax
		#retn


  def test_gadget_sub_6E7ACF40(self):
		#sub_6E7ACF40
		gadget = "A19086A66E83E0FEA39086A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68690
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68690, eax
		#retn


  def test_gadget_sub_6E7AD690(self):
		#sub_6E7AD690
		gadget = "A19C86A66E83E0FEA39C86A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6869C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6869C, eax
		#retn


  def test_gadget_sub_6E7AD9F0(self):
		#sub_6E7AD9F0
		gadget = "A1A886A66E83E0FEA3A886A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA686A8, eax
		#retn


  def test_gadget_sub_6E7ADA09(self):
		#sub_6E7ADA09
		gadget = "A1A886A66E83E0FDA3A886A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686A8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA686A8, eax
		#retn


  def test_gadget_sub_6E7ADA40(self):
		#sub_6E7ADA40
		gadget = "A1D486A66E83E0FEA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADA59(self):
		#sub_6E7ADA59
		gadget = "A1D486A66E83E0FDA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADA72(self):
		#sub_6E7ADA72
		gadget = "A1D486A66E83E0FBA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADA8B(self):
		#sub_6E7ADA8B
		gadget = "A1D486A66E83E0F7A3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADAA4(self):
		#sub_6E7ADAA4
		gadget = "A1D486A66E83E0EFA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADABD(self):
		#sub_6E7ADABD
		gadget = "A1D486A66E83E0DFA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADAD6(self):
		#sub_6E7ADAD6
		gadget = "A1D486A66E83E0BFA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFFBFh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADAEF(self):
		#sub_6E7ADAEF
		gadget = "A1D486A66E257FFFFFFFA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFF7Fh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADB0A(self):
		#sub_6E7ADB0A
		gadget = "A1D486A66E25FFFEFFFFA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFEFFh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADB25(self):
		#sub_6E7ADB25
		gadget = "A1D486A66E25FFFDFFFFA3D486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686D4
		#and     eax, 0FFFFFDFFh
		#mov     dword_6EA686D4, eax
		#retn


  def test_gadget_sub_6E7ADDF0(self):
		#sub_6E7ADDF0
		gadget = "A1DC86A66E83E0FEA3DC86A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA686DC, eax
		#retn


  def test_gadget_sub_6E7AE320(self):
		#sub_6E7AE320
		gadget = "A1E486A66E83E0FEA3E486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA686E4, eax
		#retn


  def test_gadget_sub_6E7AF600(self):
		#sub_6E7AF600
		gadget = "A1EC86A66E83E0FEA3EC86A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA686EC, eax
		#retn


  def test_gadget_sub_6E7AF930(self):
		#sub_6E7AF930
		gadget = "A1F486A66E83E0FEA3F486A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA686F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA686F4, eax
		#retn


  def test_gadget_sub_6E7B12C0(self):
		#sub_6E7B12C0
		gadget = "A10487A66E83E0FEA30487A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68704
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68704, eax
		#retn


  def test_gadget_sub_6E7B2310(self):
		#sub_6E7B2310
		gadget = "A10C87A66E83E0FEA30C87A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6870C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6870C, eax
		#retn


  def test_gadget_sub_6E7B2E10(self):
		#sub_6E7B2E10
		gadget = "A1D488A66E83E0FEA3D488A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA688D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA688D4, eax
		#retn


  def test_gadget_sub_6E7B2E40(self):
		#sub_6E7B2E40
		gadget = "A1DC88A66E83E0FEA3DC88A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA688DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA688DC, eax
		#retn


  def test_gadget_sub_6E7B3610(self):
		#sub_6E7B3610
		gadget = "A1E488A66E83E0FEA3E488A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA688E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA688E4, eax
		#retn


  def test_gadget_sub_6E7B4320(self):
		#sub_6E7B4320
		gadget = "A12889A66E83E0FEA32889A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68928
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68928, eax
		#retn


  def test_gadget_sub_6E7B4350(self):
		#sub_6E7B4350
		gadget = "A13489A66E83E0FEA33489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68934
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68934, eax
		#retn


  def test_gadget_sub_6E7B436E(self):
		#sub_6E7B436E
		gadget = "A13489A66E83E0FDA33489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68934
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68934, eax
		#retn


  def test_gadget_sub_6E7B43B0(self):
		#sub_6E7B43B0
		gadget = "A13C89A66E83E0FEA33C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6893C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6893C, eax
		#retn


  def test_gadget_sub_6E7B4430(self):
		#sub_6E7B4430
		gadget = "A14C89A66E83E0FEA34C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6894C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6894C, eax
		#retn


  def test_gadget_sub_6E7B4460(self):
		#sub_6E7B4460
		gadget = "A15489A66E83E0FEA35489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68954
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68954, eax
		#retn


  def test_gadget_sub_6E7B44A0(self):
		#sub_6E7B44A0
		gadget = "A15C89A66E83E0FEA35C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6895C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6895C, eax
		#retn


  def test_gadget_sub_6E7B44E0(self):
		#sub_6E7B44E0
		gadget = "A16489A66E83E0FEA36489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68964
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68964, eax
		#retn


  def test_gadget_sub_6E7B454B(self):
		#sub_6E7B454B
		gadget = "A16C89A66E83E0FEA36C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6896C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6896C, eax
		#retn


  def test_gadget_sub_6E7B45A3(self):
		#sub_6E7B45A3
		gadget = "A17489A66E83E0FEA37489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68974
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68974, eax
		#retn


  def test_gadget_sub_6E7B45D0(self):
		#sub_6E7B45D0
		gadget = "A17C89A66E83E0FEA37C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6897C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6897C, eax
		#retn


  def test_gadget_sub_6E7B4630(self):
		#sub_6E7B4630
		gadget = "A18489A66E83E0FEA38489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68984
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68984, eax
		#retn


  def test_gadget_sub_6E7B4660(self):
		#sub_6E7B4660
		gadget = "A18C89A66E83E0FEA38C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6898C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6898C, eax
		#retn


  def test_gadget_sub_6E7B4690(self):
		#sub_6E7B4690
		gadget = "A19489A66E83E0FEA39489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68994
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68994, eax
		#retn


  def test_gadget_sub_6E7B46C0(self):
		#sub_6E7B46C0
		gadget = "A19C89A66E83E0FEA39C89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6899C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6899C, eax
		#retn


  def test_gadget_sub_6E7B46F0(self):
		#sub_6E7B46F0
		gadget = "A1A489A66E83E0FEA3A489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689A4, eax
		#retn


  def test_gadget_sub_6E7B4720(self):
		#sub_6E7B4720
		gadget = "A1AC89A66E83E0FEA3AC89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689AC, eax
		#retn


  def test_gadget_sub_6E7B4750(self):
		#sub_6E7B4750
		gadget = "A1B489A66E83E0FEA3B489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689B4, eax
		#retn


  def test_gadget_sub_6E7B4780(self):
		#sub_6E7B4780
		gadget = "A1BC89A66E83E0FEA3BC89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689BC, eax
		#retn


  def test_gadget_sub_6E7B47B0(self):
		#sub_6E7B47B0
		gadget = "A1C489A66E83E0FEA3C489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689C4, eax
		#retn


  def test_gadget_sub_6E7B47E0(self):
		#sub_6E7B47E0
		gadget = "A1CC89A66E83E0FEA3CC89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689CC, eax
		#retn


  def test_gadget_sub_6E7B4810(self):
		#sub_6E7B4810
		gadget = "A1D489A66E83E0FEA3D489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689D4, eax
		#retn


  def test_gadget_sub_6E7B4840(self):
		#sub_6E7B4840
		gadget = "A1DC89A66E83E0FEA3DC89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689DC, eax
		#retn


  def test_gadget_sub_6E7B4870(self):
		#sub_6E7B4870
		gadget = "A1E489A66E83E0FEA3E489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689E4, eax
		#retn


  def test_gadget_sub_6E7B48A0(self):
		#sub_6E7B48A0
		gadget = "A1EC89A66E83E0FEA3EC89A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689EC, eax
		#retn


  def test_gadget_sub_6E7B48D0(self):
		#sub_6E7B48D0
		gadget = "A1F489A66E83E0FEA3F489A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA689F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA689F4, eax
		#retn


  def test_gadget_sub_6E7B4900(self):
		#sub_6E7B4900
		gadget = "A1088AA66E83E0FEA3088AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A08, eax
		#retn


  def test_gadget_sub_6E7B4916(self):
		#sub_6E7B4916
		gadget = "A1088AA66E83E0FDA3088AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A08
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68A08, eax
		#retn


  def test_gadget_sub_6E7B4924(self):
		#sub_6E7B4924
		gadget = "A1088AA66E83E0FBA3088AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A08
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68A08, eax
		#retn


  def test_gadget_sub_6E7B4932(self):
		#sub_6E7B4932
		gadget = "A1088AA66E83E0F7A3088AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A08
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA68A08, eax
		#retn


  def test_gadget_sub_6E7B4980(self):
		#sub_6E7B4980
		gadget = "A1148AA66E83E0FEA3148AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A14
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A14, eax
		#retn


  def test_gadget_sub_6E7B498E(self):
		#sub_6E7B498E
		gadget = "A1148AA66E83E0FDA3148AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A14
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68A14, eax
		#retn


  def test_gadget_sub_6E7B49C0(self):
		#sub_6E7B49C0
		gadget = "A11C8AA66E83E0FEA31C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A1C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A1C, eax
		#retn


  def test_gadget_sub_6E7B4A41(self):
		#sub_6E7B4A41
		gadget = "A1248AA66E83E0FEA3248AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A24
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A24, eax
		#retn


  def test_gadget_sub_6E7B4B10(self):
		#sub_6E7B4B10
		gadget = "A13C8AA66E83E0FEA33C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A3C, eax
		#retn


  def test_gadget_sub_6E7B4B26(self):
		#sub_6E7B4B26
		gadget = "A13C8AA66E83E0FDA33C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A3C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68A3C, eax
		#retn


  def test_gadget_sub_6E7B4B34(self):
		#sub_6E7B4B34
		gadget = "A13C8AA66E83E0FBA33C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A3C
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68A3C, eax
		#retn


  def test_gadget_sub_6E7B4B42(self):
		#sub_6E7B4B42
		gadget = "A13C8AA66E83E0F7A33C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A3C
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA68A3C, eax
		#retn


  def test_gadget_sub_6E7B4B50(self):
		#sub_6E7B4B50
		gadget = "A13C8AA66E83E0EFA33C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A3C
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA68A3C, eax
		#retn


  def test_gadget_sub_6E7B4B88(self):
		#sub_6E7B4B88
		gadget = "A1548AA66E83E0FEA3548AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A54, eax
		#retn


  def test_gadget_sub_6E7B4B96(self):
		#sub_6E7B4B96
		gadget = "A1548AA66E83E0FDA3548AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A54
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68A54, eax
		#retn


  def test_gadget_sub_6E7B4BA4(self):
		#sub_6E7B4BA4
		gadget = "A1548AA66E83E0FBA3548AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A54
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68A54, eax
		#retn


  def test_gadget_sub_6E7B4BB2(self):
		#sub_6E7B4BB2
		gadget = "A1548AA66E83E0F7A3548AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A54
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA68A54, eax
		#retn


  def test_gadget_sub_6E7B4BC0(self):
		#sub_6E7B4BC0
		gadget = "A1548AA66E83E0EFA3548AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A54
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA68A54, eax
		#retn


  def test_gadget_sub_6E7B4BF8(self):
		#sub_6E7B4BF8
		gadget = "A15C8AA66E83E0FEA35C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A5C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A5C, eax
		#retn


  def test_gadget_sub_6E7B4C38(self):
		#sub_6E7B4C38
		gadget = "A1648AA66E83E0FEA3648AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A64, eax
		#retn


  def test_gadget_sub_6E7B4CB0(self):
		#sub_6E7B4CB0
		gadget = "A1748AA66E83E0FEA3748AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A74
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A74, eax
		#retn


  def test_gadget_sub_6E7B4CBE(self):
		#sub_6E7B4CBE
		gadget = "A1748AA66E83E0FDA3748AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A74
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68A74, eax
		#retn


  def test_gadget_sub_6E7B4CD4(self):
		#sub_6E7B4CD4
		gadget = "A1748AA66E83E0FBA3748AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A74
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68A74, eax
		#retn


  def test_gadget_sub_6E7B4D20(self):
		#sub_6E7B4D20
		gadget = "A17C8AA66E83E0FEA37C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A7C, eax
		#retn


  def test_gadget_sub_6E7B6EE8(self):
		#sub_6E7B6EE8
		gadget = "A18C8AA66E83E0FEA38C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A8C, eax
		#retn


  def test_gadget_sub_6E7B6EF6(self):
		#sub_6E7B6EF6
		gadget = "A1848AA66E83E0FEA3848AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A84, eax
		#retn


  def test_gadget_sub_6E7B6F20(self):
		#sub_6E7B6F20
		gadget = "A1948AA66E83E0FEA3948AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A94, eax
		#retn


  def test_gadget_sub_6E7B6F2E(self):
		#sub_6E7B6F2E
		gadget = "A1848AA66E83E0FEA3848AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A84, eax
		#retn


  def test_gadget_sub_6E7B6FB3(self):
		#sub_6E7B6FB3
		gadget = "A19C8AA66E83E0FEA39C8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A9C, eax
		#retn


  def test_gadget_sub_6E7B6FC1(self):
		#sub_6E7B6FC1
		gadget = "A1848AA66E83E0FEA3848AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A84, eax
		#retn


  def test_gadget_sub_6E7B6FDF(self):
		#sub_6E7B6FDF
		gadget = "A1848AA66E83E0FEA3848AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A84, eax
		#retn


  def test_gadget_sub_6E7B7023(self):
		#sub_6E7B7023
		gadget = "A1A48AA66E83E0FEA3A48AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AA4, eax
		#retn


  def test_gadget_sub_6E7B7031(self):
		#sub_6E7B7031
		gadget = "A1848AA66E83E0FEA3848AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68A84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68A84, eax
		#retn


  def test_gadget_sub_6E7B8B60(self):
		#sub_6E7B8B60
		gadget = "A1AC8AA66E83E0FEA3AC8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AAC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AAC, eax
		#retn


  def test_gadget_sub_6E7B8BD0(self):
		#sub_6E7B8BD0
		gadget = "A1B48AA66E83E0FEA3B48AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AB4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AB4, eax
		#retn


  def test_gadget_sub_6E7B92A0(self):
		#sub_6E7B92A0
		gadget = "A1BC8AA66E83E0FEA3BC8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68ABC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68ABC, eax
		#retn


  def test_gadget_sub_6E7B9CA0(self):
		#sub_6E7B9CA0
		gadget = "A1C48AA66E83E0FEA3C48AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AC4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AC4, eax
		#retn


  def test_gadget_sub_6E7BA5F0(self):
		#sub_6E7BA5F0
		gadget = "A1CC8AA66E83E0FEA3CC8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68ACC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68ACC, eax
		#retn


  def test_gadget_sub_6E7BA630(self):
		#sub_6E7BA630
		gadget = "A1D48AA66E83E0FEA3D48AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AD4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AD4, eax
		#retn


  def test_gadget_sub_6E7BA670(self):
		#sub_6E7BA670
		gadget = "A1DC8AA66E83E0FEA3DC8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68ADC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68ADC, eax
		#retn


  def test_gadget_sub_6E7BAB50(self):
		#sub_6E7BAB50
		gadget = "A1E48AA66E83E0FEA3E48AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AE4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AE4, eax
		#retn


  def test_gadget_sub_6E7BAB90(self):
		#sub_6E7BAB90
		gadget = "A1EC8AA66E83E0FEA3EC8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AEC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AEC, eax
		#retn


  def test_gadget_sub_6E7BABD0(self):
		#sub_6E7BABD0
		gadget = "A1F48AA66E83E0FEA3F48AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AF4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AF4, eax
		#retn


  def test_gadget_sub_6E7BAC10(self):
		#sub_6E7BAC10
		gadget = "A1FC8AA66E83E0FEA3FC8AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68AFC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68AFC, eax
		#retn


  def test_gadget_sub_6E7BAC50(self):
		#sub_6E7BAC50
		gadget = "A1048BA66E83E0FEA3048BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B04
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B04, eax
		#retn


  def test_gadget_sub_6E7BAC90(self):
		#sub_6E7BAC90
		gadget = "A10C8BA66E83E0FEA30C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B0C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B0C, eax
		#retn


  def test_gadget_sub_6E7BACD0(self):
		#sub_6E7BACD0
		gadget = "A1148BA66E83E0FEA3148BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B14
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B14, eax
		#retn


  def test_gadget_sub_6E7BAD10(self):
		#sub_6E7BAD10
		gadget = "A11C8BA66E83E0FEA31C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B1C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B1C, eax
		#retn


  def test_gadget_sub_6E7BAD50(self):
		#sub_6E7BAD50
		gadget = "A1248BA66E83E0FEA3248BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B24
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B24, eax
		#retn


  def test_gadget_sub_6E7BAD90(self):
		#sub_6E7BAD90
		gadget = "A12C8BA66E83E0FEA32C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B2C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B2C, eax
		#retn


  def test_gadget_sub_6E7BADD0(self):
		#sub_6E7BADD0
		gadget = "A1348BA66E83E0FEA3348BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B34
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B34, eax
		#retn


  def test_gadget_sub_6E7BAE10(self):
		#sub_6E7BAE10
		gadget = "A13C8BA66E83E0FEA33C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B3C, eax
		#retn


  def test_gadget_sub_6E7BAE50(self):
		#sub_6E7BAE50
		gadget = "A1448BA66E83E0FEA3448BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B44
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B44, eax
		#retn


  def test_gadget_sub_6E7BAE90(self):
		#sub_6E7BAE90
		gadget = "A14C8BA66E83E0FEA34C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B4C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B4C, eax
		#retn


  def test_gadget_sub_6E7BAED0(self):
		#sub_6E7BAED0
		gadget = "A1548BA66E83E0FEA3548BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B54, eax
		#retn


  def test_gadget_sub_6E7BAF10(self):
		#sub_6E7BAF10
		gadget = "A15C8BA66E83E0FEA35C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B5C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B5C, eax
		#retn


  def test_gadget_sub_6E7BAF50(self):
		#sub_6E7BAF50
		gadget = "A1648BA66E83E0FEA3648BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B64, eax
		#retn


  def test_gadget_sub_6E7BAF90(self):
		#sub_6E7BAF90
		gadget = "A16C8BA66E83E0FEA36C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B6C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B6C, eax
		#retn


  def test_gadget_sub_6E7BAFD0(self):
		#sub_6E7BAFD0
		gadget = "A1748BA66E83E0FEA3748BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B74
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B74, eax
		#retn


  def test_gadget_sub_6E7BB010(self):
		#sub_6E7BB010
		gadget = "A17C8BA66E83E0FEA37C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B7C, eax
		#retn


  def test_gadget_sub_6E7BB050(self):
		#sub_6E7BB050
		gadget = "A1848BA66E83E0FEA3848BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B84, eax
		#retn


  def test_gadget_sub_6E7BB090(self):
		#sub_6E7BB090
		gadget = "A18C8BA66E83E0FEA38C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B8C, eax
		#retn


  def test_gadget_sub_6E7BB420(self):
		#sub_6E7BB420
		gadget = "A1948BA66E83E0FEA3948BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B94, eax
		#retn


  def test_gadget_sub_6E7BB460(self):
		#sub_6E7BB460
		gadget = "A19C8BA66E83E0FEA39C8BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68B9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68B9C, eax
		#retn


  def test_gadget_sub_6E7BB4A0(self):
		#sub_6E7BB4A0
		gadget = "A1A48BA66E83E0FEA3A48BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BA4, eax
		#retn


  def test_gadget_sub_6E7BB4E0(self):
		#sub_6E7BB4E0
		gadget = "A1B08BA66E83E0FEA3B08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BB0, eax
		#retn


  def test_gadget_sub_6E7BB510(self):
		#sub_6E7BB510
		gadget = "A1B08BA66E83E0FEA3B08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BB0, eax
		#retn


  def test_gadget_sub_6E7BB5B0(self):
		#sub_6E7BB5B0
		gadget = "A1B08BA66E83E0FEA3B08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BB0, eax
		#retn


  def test_gadget_sub_6E7BB5E0(self):
		#sub_6E7BB5E0
		gadget = "A1B08BA66E83E0FEA3B08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BB0, eax
		#retn


  def test_gadget_sub_6E7BB7A0(self):
		#sub_6E7BB7A0
		gadget = "A1B88BA66E83E0FEA3B88BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BB8, eax
		#retn


  def test_gadget_sub_6E7BB7D0(self):
		#sub_6E7BB7D0
		gadget = "A1C08BA66E83E0FEA3C08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BC0, eax
		#retn


  def test_gadget_sub_6E7BB800(self):
		#sub_6E7BB800
		gadget = "A1C88BA66E83E0FEA3C88BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BC8, eax
		#retn


  def test_gadget_sub_6E7BB830(self):
		#sub_6E7BB830
		gadget = "A1D08BA66E83E0FEA3D08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BD0, eax
		#retn


  def test_gadget_sub_6E7BB860(self):
		#sub_6E7BB860
		gadget = "A1D88BA66E83E0FEA3D88BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BD8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BD8, eax
		#retn


  def test_gadget_sub_6E7BB890(self):
		#sub_6E7BB890
		gadget = "A1E08BA66E83E0FEA3E08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BE0, eax
		#retn


  def test_gadget_sub_6E7BB8C0(self):
		#sub_6E7BB8C0
		gadget = "A1E88BA66E83E0FEA3E88BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BE8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BE8, eax
		#retn


  def test_gadget_sub_6E7BB8F0(self):
		#sub_6E7BB8F0
		gadget = "A1F08BA66E83E0FEA3F08BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BF0, eax
		#retn


  def test_gadget_sub_6E7BB920(self):
		#sub_6E7BB920
		gadget = "A1F88BA66E83E0FEA3F88BA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68BF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68BF8, eax
		#retn


  def test_gadget_sub_6E7BB950(self):
		#sub_6E7BB950
		gadget = "A1008CA66E83E0FEA3008CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68C00, eax
		#retn


  def test_gadget_sub_6E7BB980(self):
		#sub_6E7BB980
		gadget = "A1088CA66E83E0FEA3088CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68C08, eax
		#retn


  def test_gadget_sub_6E7BB9B0(self):
		#sub_6E7BB9B0
		gadget = "A1108CA66E83E0FEA3108CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68C10, eax
		#retn


  def test_gadget_sub_6E7BB9F0(self):
		#sub_6E7BB9F0
		gadget = "A1188CA66E83E0FEA3188CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68C18, eax
		#retn


  def test_gadget_sub_6E7BBA8E(self):
		#sub_6E7BBA8E
		gadget = "A1208CA66E83E0FEA3208CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68C20, eax
		#retn


  def test_gadget_sub_6E7BBAFE(self):
		#sub_6E7BBAFE
		gadget = "A1288CA66E83E0FEA3288CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68C28, eax
		#retn


  def test_gadget_sub_6E7BBB60(self):
		#sub_6E7BBB60
		gadget = "A1448CA66E83E0FDA3448CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68C44
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68C44, eax
		#retn


  def test_gadget_sub_6E7BD750(self):
		#sub_6E7BD750
		gadget = "A1BC8CA66E83E0FEA3BC8CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CBC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CBC, eax
		#retn


  def test_gadget_sub_6E7BD790(self):
		#sub_6E7BD790
		gadget = "A1C48CA66E83E0FEA3C48CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CC4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CC4, eax
		#retn


  def test_gadget_sub_6E7BDA50(self):
		#sub_6E7BDA50
		gadget = "A1CC8CA66E83E0FEA3CC8CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CCC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CCC, eax
		#retn


  def test_gadget_sub_6E7BE2F8(self):
		#sub_6E7BE2F8
		gadget = "A1D48CA66E83E0FEA3D48CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CD4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CD4, eax
		#retn


  def test_gadget_sub_6E7BE380(self):
		#sub_6E7BE380
		gadget = "A1DC8CA66E83E0FEA3DC8CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CDC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CDC, eax
		#retn


  def test_gadget_sub_6E7BE420(self):
		#sub_6E7BE420
		gadget = "A1E48CA66E83E0FEA3E48CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CE4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CE4, eax
		#retn


  def test_gadget_sub_6E7BFA30(self):
		#sub_6E7BFA30
		gadget = "A1F88CA66E83E0FEA3F88CA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68CF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68CF8, eax
		#retn


  def test_gadget_sub_6E7BFB80(self):
		#sub_6E7BFB80
		gadget = "A1008DA66E83E0FEA3008DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D00, eax
		#retn


  def test_gadget_sub_6E7BFBB0(self):
		#sub_6E7BFBB0
		gadget = "A1088DA66E83E0FEA3088DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D08, eax
		#retn


  def test_gadget_sub_6E7BFBE0(self):
		#sub_6E7BFBE0
		gadget = "A1108DA66E83E0FEA3108DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D10, eax
		#retn


  def test_gadget_sub_6E7BFC10(self):
		#sub_6E7BFC10
		gadget = "A1188DA66E83E0FEA3188DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D18, eax
		#retn


  def test_gadget_sub_6E7C0090(self):
		#sub_6E7C0090
		gadget = "A1208DA66E83E0FEA3208DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D20, eax
		#retn


  def test_gadget_sub_6E7C0180(self):
		#sub_6E7C0180
		gadget = "A15C54A66E83E0FEA35C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6545C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6545C, eax
		#retn


  def test_gadget_sub_6E7C09A8(self):
		#sub_6E7C09A8
		gadget = "A1308DA66E83E0FEA3308DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D30, eax
		#retn


  def test_gadget_sub_6E7C0A90(self):
		#sub_6E7C0A90
		gadget = "A13C8DA66E83E0FEA33C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D3C, eax
		#retn


  def test_gadget_sub_6E7C0AA9(self):
		#sub_6E7C0AA9
		gadget = "A13C8DA66E83E0FDA33C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D3C
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68D3C, eax
		#retn


  def test_gadget_sub_6E7C0AE0(self):
		#sub_6E7C0AE0
		gadget = "A1448DA66E83E0FEA3448DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D44
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D44, eax
		#retn


  def test_gadget_sub_6E7C0B20(self):
		#sub_6E7C0B20
		gadget = "A14C8DA66E83E0FEA34C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D4C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D4C, eax
		#retn


  def test_gadget_sub_6E7C0C30(self):
		#sub_6E7C0C30
		gadget = "A1548DA66E83E0FEA3548DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D54, eax
		#retn


  def test_gadget_sub_6E7C0C60(self):
		#sub_6E7C0C60
		gadget = "A15C8DA66E83E0FEA35C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D5C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D5C, eax
		#retn


  def test_gadget_sub_6E7C1170(self):
		#sub_6E7C1170
		gadget = "A1648DA66E83E0FEA3648DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D64, eax
		#retn


  def test_gadget_sub_6E7C1710(self):
		#sub_6E7C1710
		gadget = "A16C8DA66E83E0FEA36C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D6C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D6C, eax
		#retn


  def test_gadget_sub_6E7C1740(self):
		#sub_6E7C1740
		gadget = "A1748DA66E83E0FEA3748DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D74
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D74, eax
		#retn


  def test_gadget_sub_6E7C1770(self):
		#sub_6E7C1770
		gadget = "A17C8DA66E83E0FEA37C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D7C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D7C, eax
		#retn


  def test_gadget_sub_6E7C17A0(self):
		#sub_6E7C17A0
		gadget = "A1848DA66E83E0FEA3848DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D84, eax
		#retn


  def test_gadget_sub_6E7C17D0(self):
		#sub_6E7C17D0
		gadget = "A18C8DA66E83E0FEA38C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D8C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D8C, eax
		#retn


  def test_gadget_sub_6E7C1A40(self):
		#sub_6E7C1A40
		gadget = "A1948DA66E83E0FEA3948DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D94
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D94, eax
		#retn


  def test_gadget_sub_6E7C1A70(self):
		#sub_6E7C1A70
		gadget = "A19C8DA66E83E0FEA39C8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68D9C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68D9C, eax
		#retn


  def test_gadget_sub_6E7C1B20(self):
		#sub_6E7C1B20
		gadget = "A1AC8DA66E83E0FEA3AC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DAC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DAC, eax
		#retn


  def test_gadget_sub_6E7C1B51(self):
		#sub_6E7C1B51
		gadget = "A1AC8DA66E83E0FDA3AC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DAC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68DAC, eax
		#retn


  def test_gadget_sub_6E7C1B82(self):
		#sub_6E7C1B82
		gadget = "A1AC8DA66E83E0FBA3AC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DAC
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68DAC, eax
		#retn


  def test_gadget_sub_6E7C1BD0(self):
		#sub_6E7C1BD0
		gadget = "A1B48DA66E83E0FEA3B48DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DB4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DB4, eax
		#retn


  def test_gadget_sub_6E7C1D50(self):
		#sub_6E7C1D50
		gadget = "A1BC8DA66E83E0FEA3BC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DBC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DBC, eax
		#retn


  def test_gadget_unknown_libname_42(self):
		#unknown_libname_42
		gadget = "8B45F050E8B77D9CFF59C3"
		self.do(gadget)

		#mov     eax, [ebp-10h]
		#push    eax             ; void *
		#call    j_free
		#pop     ecx
		#retn


  def test_gadget_unknown_libname_43(self):
		#unknown_libname_43
		gadget = "8B45F050E8807D9CFF59C3"
		self.do(gadget)

		#mov     eax, [ebp-10h]
		#push    eax             ; void *
		#call    j_free
		#pop     ecx
		#retn


  def test_gadget_unknown_libname_44(self):
		#unknown_libname_44
		gadget = "8B45F050E8497D9CFF59C3"
		self.do(gadget)

		#mov     eax, [ebp-10h]
		#push    eax             ; void *
		#call    j_free
		#pop     ecx
		#retn


  def test_gadget_sub_6E7C2AF0(self):
		#sub_6E7C2AF0
		gadget = "A1C88DA66E83E0FEA3C88DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DC8, eax
		#retn


  def test_gadget_sub_6E7C2B09(self):
		#sub_6E7C2B09
		gadget = "A1C88DA66E83E0FDA3C88DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DC8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68DC8, eax
		#retn


  def test_gadget_sub_6E7C2BB0(self):
		#sub_6E7C2BB0
		gadget = "A1D08DA66E83E0FEA3D08DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DD0, eax
		#retn


  def test_gadget_sub_6E7C2BE0(self):
		#sub_6E7C2BE0
		gadget = "A1D88DA66E83E0FEA3D88DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DD8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DD8, eax
		#retn


  def test_gadget_sub_6E7C2C10(self):
		#sub_6E7C2C10
		gadget = "A1EC8DA66E83E0FEA3EC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DEC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DEC, eax
		#retn


  def test_gadget_sub_6E7C2C29(self):
		#sub_6E7C2C29
		gadget = "A1EC8DA66E83E0FDA3EC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DEC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68DEC, eax
		#retn


  def test_gadget_sub_6E7C2C42(self):
		#sub_6E7C2C42
		gadget = "A1EC8DA66E83E0FBA3EC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DEC
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA68DEC, eax
		#retn


  def test_gadget_sub_6E7C2C5B(self):
		#sub_6E7C2C5B
		gadget = "A1EC8DA66E83E0F7A3EC8DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DEC
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA68DEC, eax
		#retn


  def test_gadget_sub_6E7C2C90(self):
		#sub_6E7C2C90
		gadget = "A1F88DA66E83E0FEA3F88DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68DF8, eax
		#retn


  def test_gadget_sub_6E7C2CA9(self):
		#sub_6E7C2CA9
		gadget = "A1F88DA66E83E0FDA3F88DA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68DF8
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA68DF8, eax
		#retn


  def test_gadget_sub_6E7C2D50(self):
		#sub_6E7C2D50
		gadget = "A1008EA66E83E0FEA3008EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E00, eax
		#retn


  def test_gadget_sub_6E7C2D90(self):
		#sub_6E7C2D90
		gadget = "A1088EA66E83E0FEA3088EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E08, eax
		#retn


  def test_gadget_sub_6E7C2DD0(self):
		#sub_6E7C2DD0
		gadget = "A1108EA66E83E0FEA3108EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E10, eax
		#retn


  def test_gadget_sub_6E7C2E90(self):
		#sub_6E7C2E90
		gadget = "A1188EA66E83E0FEA3188EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E18, eax
		#retn


  def test_gadget_sub_6E7C2EC0(self):
		#sub_6E7C2EC0
		gadget = "A1208EA66E83E0FEA3208EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E20, eax
		#retn


  def test_gadget_sub_6E7C2EF0(self):
		#sub_6E7C2EF0
		gadget = "A1288EA66E83E0FEA3288EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E28, eax
		#retn


  def test_gadget_sub_6E7C2FD0(self):
		#sub_6E7C2FD0
		gadget = "A1308EA66E83E0FEA3308EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E30, eax
		#retn


  def test_gadget_sub_6E7C3000(self):
		#sub_6E7C3000
		gadget = "A1388EA66E83E0FEA3388EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E38, eax
		#retn


  def test_gadget_sub_6E7C3030(self):
		#sub_6E7C3030
		gadget = "A1408EA66E83E0FEA3408EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E40, eax
		#retn


  def test_gadget_sub_6E7C3060(self):
		#sub_6E7C3060
		gadget = "A1488EA66E83E0FEA3488EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E48, eax
		#retn


  def test_gadget_sub_6E7C3090(self):
		#sub_6E7C3090
		gadget = "A1508EA66E83E0FEA3508EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E50, eax
		#retn


  def test_gadget_sub_6E7C30C0(self):
		#sub_6E7C30C0
		gadget = "A1588EA66E83E0FEA3588EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E58, eax
		#retn


  def test_gadget_sub_6E7C3170(self):
		#sub_6E7C3170
		gadget = "A1608EA66E83E0FEA3608EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E60, eax
		#retn


  def test_gadget_sub_6E7C31A0(self):
		#sub_6E7C31A0
		gadget = "A1688EA66E83E0FEA3688EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E68
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E68, eax
		#retn


  def test_gadget_sub_6E7C31D0(self):
		#sub_6E7C31D0
		gadget = "A1708EA66E83E0FEA3708EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E70, eax
		#retn


  def test_gadget_sub_6E7C3200(self):
		#sub_6E7C3200
		gadget = "A1788EA66E83E0FEA3788EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E78
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E78, eax
		#retn


  def test_gadget_sub_6E7C32A0(self):
		#sub_6E7C32A0
		gadget = "A1808EA66E83E0FEA3808EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E80, eax
		#retn


  def test_gadget_sub_6E7C3300(self):
		#sub_6E7C3300
		gadget = "A1888EA66E83E0FEA3888EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E88
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E88, eax
		#retn


  def test_gadget_sub_6E7C3330(self):
		#sub_6E7C3330
		gadget = "A1908EA66E83E0FEA3908EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E90, eax
		#retn


  def test_gadget_sub_6E7C3360(self):
		#sub_6E7C3360
		gadget = "A1988EA66E83E0FEA3988EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68E98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68E98, eax
		#retn


  def test_gadget_sub_6E7C3390(self):
		#sub_6E7C3390
		gadget = "A1A08EA66E83E0FEA3A08EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EA0, eax
		#retn


  def test_gadget_sub_6E7C33C0(self):
		#sub_6E7C33C0
		gadget = "A1A88EA66E83E0FEA3A88EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EA8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EA8, eax
		#retn


  def test_gadget_sub_6E7C33F0(self):
		#sub_6E7C33F0
		gadget = "A1B08EA66E83E0FEA3B08EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EB0, eax
		#retn


  def test_gadget_sub_6E7C3420(self):
		#sub_6E7C3420
		gadget = "A1B88EA66E83E0FEA3B88EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EB8, eax
		#retn


  def test_gadget_sub_6E7C3450(self):
		#sub_6E7C3450
		gadget = "A1C08EA66E83E0FEA3C08EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EC0, eax
		#retn


  def test_gadget_sub_6E7C3550(self):
		#sub_6E7C3550
		gadget = "A1C88EA66E83E0FEA3C88EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EC8, eax
		#retn


  def test_gadget_sub_6E7C35B0(self):
		#sub_6E7C35B0
		gadget = "A1D08EA66E83E0FEA3D08EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68ED0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68ED0, eax
		#retn


  def test_gadget_sub_6E7C35E0(self):
		#sub_6E7C35E0
		gadget = "A1D88EA66E83E0FEA3D88EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68ED8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68ED8, eax
		#retn


  def test_gadget_sub_6E7C3610(self):
		#sub_6E7C3610
		gadget = "A1E08EA66E83E0FEA3E08EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EE0, eax
		#retn


  def test_gadget_sub_6E7C3640(self):
		#sub_6E7C3640
		gadget = "A1E88EA66E83E0FEA3E88EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EE8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EE8, eax
		#retn


  def test_gadget_sub_6E7C3670(self):
		#sub_6E7C3670
		gadget = "A1F08EA66E83E0FEA3F08EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EF0, eax
		#retn


  def test_gadget_sub_6E7C3710(self):
		#sub_6E7C3710
		gadget = "A1F88EA66E83E0FEA3F88EA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68EF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68EF8, eax
		#retn


  def test_gadget_sub_6E7C3740(self):
		#sub_6E7C3740
		gadget = "A1008FA66E83E0FEA3008FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F00
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F00, eax
		#retn


  def test_gadget_sub_6E7C37E0(self):
		#sub_6E7C37E0
		gadget = "A1088FA66E83E0FEA3088FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F08
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F08, eax
		#retn


  def test_gadget_sub_6E7C39A0(self):
		#sub_6E7C39A0
		gadget = "A1108FA66E83E0FEA3108FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F10
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F10, eax
		#retn


  def test_gadget_sub_6E7C3A40(self):
		#sub_6E7C3A40
		gadget = "A1188FA66E83E0FEA3188FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F18
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F18, eax
		#retn


  def test_gadget_sub_6E7C3B40(self):
		#sub_6E7C3B40
		gadget = "A1208FA66E83E0FEA3208FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F20
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F20, eax
		#retn


  def test_gadget_sub_6E7C3CB0(self):
		#sub_6E7C3CB0
		gadget = "A1288FA66E83E0FEA3288FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F28
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F28, eax
		#retn


  def test_gadget_sub_6E7C3CE0(self):
		#sub_6E7C3CE0
		gadget = "A1308FA66E83E0FEA3308FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F30, eax
		#retn


  def test_gadget_sub_6E7C3D10(self):
		#sub_6E7C3D10
		gadget = "A1388FA66E83E0FEA3388FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F38
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F38, eax
		#retn


  def test_gadget_sub_6E7C3D40(self):
		#sub_6E7C3D40
		gadget = "A1408FA66E83E0FEA3408FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F40
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F40, eax
		#retn


  def test_gadget_sub_6E7C3D70(self):
		#sub_6E7C3D70
		gadget = "A1488FA66E83E0FEA3488FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F48
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F48, eax
		#retn


  def test_gadget_sub_6E7C3DA0(self):
		#sub_6E7C3DA0
		gadget = "A1508FA66E83E0FEA3508FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F50
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F50, eax
		#retn


  def test_gadget_sub_6E7C3DD0(self):
		#sub_6E7C3DD0
		gadget = "A1588FA66E83E0FEA3588FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F58
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F58, eax
		#retn


  def test_gadget_sub_6E7C3ED0(self):
		#sub_6E7C3ED0
		gadget = "A1608FA66E83E0FEA3608FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F60
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F60, eax
		#retn


  def test_gadget_sub_6E7C3F00(self):
		#sub_6E7C3F00
		gadget = "A1688FA66E83E0FEA3688FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F68
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F68, eax
		#retn


  def test_gadget_sub_6E7C3F30(self):
		#sub_6E7C3F30
		gadget = "A1708FA66E83E0FEA3708FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F70
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F70, eax
		#retn


  def test_gadget_sub_6E7C3F60(self):
		#sub_6E7C3F60
		gadget = "A1788FA66E83E0FEA3788FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F78
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F78, eax
		#retn


  def test_gadget_sub_6E7C3F90(self):
		#sub_6E7C3F90
		gadget = "A1808FA66E83E0FEA3808FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F80
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F80, eax
		#retn


  def test_gadget_sub_6E7C4050(self):
		#sub_6E7C4050
		gadget = "A1888FA66E83E0FEA3888FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F88
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F88, eax
		#retn


  def test_gadget_sub_6E7C4080(self):
		#sub_6E7C4080
		gadget = "A1908FA66E83E0FEA3908FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F90
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F90, eax
		#retn


  def test_gadget_sub_6E7C40B0(self):
		#sub_6E7C40B0
		gadget = "A1988FA66E83E0FEA3988FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68F98
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68F98, eax
		#retn


  def test_gadget_sub_6E7C40E0(self):
		#sub_6E7C40E0
		gadget = "A1A08FA66E83E0FEA3A08FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FA0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FA0, eax
		#retn


  def test_gadget_sub_6E7C4110(self):
		#sub_6E7C4110
		gadget = "A1A88FA66E83E0FEA3A88FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FA8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FA8, eax
		#retn


  def test_gadget_sub_6E7C41D0(self):
		#sub_6E7C41D0
		gadget = "A1B08FA66E83E0FEA3B08FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FB0, eax
		#retn


  def test_gadget_sub_6E7C4200(self):
		#sub_6E7C4200
		gadget = "A1B88FA66E83E0FEA3B88FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FB8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FB8, eax
		#retn


  def test_gadget_sub_6E7C4230(self):
		#sub_6E7C4230
		gadget = "A1C08FA66E83E0FEA3C08FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FC0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FC0, eax
		#retn


  def test_gadget_sub_6E7C4300(self):
		#sub_6E7C4300
		gadget = "A1C88FA66E83E0FEA3C88FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FC8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FC8, eax
		#retn


  def test_gadget_sub_6E7C4330(self):
		#sub_6E7C4330
		gadget = "A1D08FA66E83E0FEA3D08FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FD0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FD0, eax
		#retn


  def test_gadget_sub_6E7C4360(self):
		#sub_6E7C4360
		gadget = "A1D88FA66E83E0FEA3D88FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FD8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FD8, eax
		#retn


  def test_gadget_sub_6E7C4390(self):
		#sub_6E7C4390
		gadget = "A1E08FA66E83E0FEA3E08FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FE0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FE0, eax
		#retn


  def test_gadget_sub_6E7C43C0(self):
		#sub_6E7C43C0
		gadget = "A1E88FA66E83E0FEA3E88FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FE8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FE8, eax
		#retn


  def test_gadget_sub_6E7C43F0(self):
		#sub_6E7C43F0
		gadget = "A1F08FA66E83E0FEA3F08FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FF0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FF0, eax
		#retn


  def test_gadget_sub_6E7C4420(self):
		#sub_6E7C4420
		gadget = "A1F88FA66E83E0FEA3F88FA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA68FF8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA68FF8, eax
		#retn


  def test_gadget_sub_6E7C4450(self):
		#sub_6E7C4450
		gadget = "A10090A66E83E0FEA30090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69000
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69000, eax
		#retn


  def test_gadget_sub_6E7C4480(self):
		#sub_6E7C4480
		gadget = "A10890A66E83E0FEA30890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69008
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69008, eax
		#retn


  def test_gadget_sub_6E7C4540(self):
		#sub_6E7C4540
		gadget = "A11090A66E83E0FEA31090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69010
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69010, eax
		#retn


  def test_gadget_sub_6E7C4580(self):
		#sub_6E7C4580
		gadget = "A11890A66E83E0FEA31890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69018
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69018, eax
		#retn


  def test_gadget_sub_6E7C45C0(self):
		#sub_6E7C45C0
		gadget = "A12090A66E83E0FEA32090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69020
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69020, eax
		#retn


  def test_gadget_sub_6E7C4600(self):
		#sub_6E7C4600
		gadget = "A12890A66E83E0FEA32890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69028
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69028, eax
		#retn


  def test_gadget_sub_6E7C4640(self):
		#sub_6E7C4640
		gadget = "A13090A66E83E0FEA33090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69030
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69030, eax
		#retn


  def test_gadget_sub_6E7C4670(self):
		#sub_6E7C4670
		gadget = "A13890A66E83E0FEA33890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69038
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69038, eax
		#retn


  def test_gadget_sub_6E7C46A0(self):
		#sub_6E7C46A0
		gadget = "A14090A66E83E0FEA34090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69040
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69040, eax
		#retn


  def test_gadget_sub_6E7C46D0(self):
		#sub_6E7C46D0
		gadget = "A14890A66E83E0FEA34890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69048
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69048, eax
		#retn


  def test_gadget_sub_6E7C4710(self):
		#sub_6E7C4710
		gadget = "A15090A66E83E0FEA35090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69050
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69050, eax
		#retn


  def test_gadget_sub_6E7C4750(self):
		#sub_6E7C4750
		gadget = "A15890A66E83E0FEA35890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69058
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69058, eax
		#retn


  def test_gadget_sub_6E7C4780(self):
		#sub_6E7C4780
		gadget = "A16090A66E83E0FEA36090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69060
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69060, eax
		#retn


  def test_gadget_sub_6E7C47B0(self):
		#sub_6E7C47B0
		gadget = "A16890A66E83E0FEA36890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69068
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69068, eax
		#retn


  def test_gadget_sub_6E7C47E0(self):
		#sub_6E7C47E0
		gadget = "A17090A66E83E0FEA37090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69070
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69070, eax
		#retn


  def test_gadget_sub_6E7C4810(self):
		#sub_6E7C4810
		gadget = "A17890A66E83E0FEA37890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69078
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69078, eax
		#retn


  def test_gadget_sub_6E7C4840(self):
		#sub_6E7C4840
		gadget = "A18090A66E83E0FEA38090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69080
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69080, eax
		#retn


  def test_gadget_sub_6E7C4880(self):
		#sub_6E7C4880
		gadget = "A18890A66E83E0FEA38890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69088
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69088, eax
		#retn


  def test_gadget_sub_6E7C48C0(self):
		#sub_6E7C48C0
		gadget = "A19090A66E83E0FEA39090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69090
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69090, eax
		#retn


  def test_gadget_sub_6E7C48F0(self):
		#sub_6E7C48F0
		gadget = "A19890A66E83E0FEA39890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69098
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69098, eax
		#retn


  def test_gadget_sub_6E7C4A50(self):
		#sub_6E7C4A50
		gadget = "A1A090A66E83E0FEA3A090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690A0, eax
		#retn


  def test_gadget_sub_6E7C4A90(self):
		#sub_6E7C4A90
		gadget = "A1A890A66E83E0FEA3A890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690A8, eax
		#retn


  def test_gadget_sub_6E7C4AD0(self):
		#sub_6E7C4AD0
		gadget = "A1B090A66E83E0FEA3B090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690B0, eax
		#retn


  def test_gadget_sub_6E7C4B00(self):
		#sub_6E7C4B00
		gadget = "A1B890A66E83E0FEA3B890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690B8, eax
		#retn


  def test_gadget_sub_6E7C4B30(self):
		#sub_6E7C4B30
		gadget = "A1C090A66E83E0FEA3C090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690C0, eax
		#retn


  def test_gadget_sub_6E7C4B60(self):
		#sub_6E7C4B60
		gadget = "A1C890A66E83E0FEA3C890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690C8, eax
		#retn


  def test_gadget_sub_6E7C4B90(self):
		#sub_6E7C4B90
		gadget = "A1D090A66E83E0FEA3D090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690D0, eax
		#retn


  def test_gadget_sub_6E7C4BC0(self):
		#sub_6E7C4BC0
		gadget = "A1D890A66E83E0FEA3D890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690D8, eax
		#retn


  def test_gadget_sub_6E7C4C00(self):
		#sub_6E7C4C00
		gadget = "A1E090A66E83E0FEA3E090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690E0, eax
		#retn


  def test_gadget_sub_6E7C4CA0(self):
		#sub_6E7C4CA0
		gadget = "A1E890A66E83E0FEA3E890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690E8, eax
		#retn


  def test_gadget_sub_6E7C4CD0(self):
		#sub_6E7C4CD0
		gadget = "A1F090A66E83E0FEA3F090A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690F0, eax
		#retn


  def test_gadget_sub_6E7C4D00(self):
		#sub_6E7C4D00
		gadget = "A1F890A66E83E0FEA3F890A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA690F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA690F8, eax
		#retn


  def test_gadget_sub_6E7C4D30(self):
		#sub_6E7C4D30
		gadget = "A10091A66E83E0FEA30091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69100
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69100, eax
		#retn


  def test_gadget_sub_6E7C4D60(self):
		#sub_6E7C4D60
		gadget = "A10891A66E83E0FEA30891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69108
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69108, eax
		#retn


  def test_gadget_sub_6E7C4D90(self):
		#sub_6E7C4D90
		gadget = "A11091A66E83E0FEA31091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69110
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69110, eax
		#retn


  def test_gadget_sub_6E7C4DC0(self):
		#sub_6E7C4DC0
		gadget = "A11891A66E83E0FEA31891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69118
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69118, eax
		#retn


  def test_gadget_sub_6E7C4E30(self):
		#sub_6E7C4E30
		gadget = "A12091A66E83E0FEA32091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69120
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69120, eax
		#retn


  def test_gadget_sub_6E7C4E70(self):
		#sub_6E7C4E70
		gadget = "A12891A66E83E0FEA32891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69128
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69128, eax
		#retn


  def test_gadget_sub_6E7C4EB0(self):
		#sub_6E7C4EB0
		gadget = "A13091A66E83E0FEA33091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69130
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69130, eax
		#retn


  def test_gadget_sub_6E7C4EE0(self):
		#sub_6E7C4EE0
		gadget = "A13891A66E83E0FEA33891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69138
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69138, eax
		#retn


  def test_gadget_sub_6E7C4F10(self):
		#sub_6E7C4F10
		gadget = "A14091A66E83E0FEA34091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69140
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69140, eax
		#retn


  def test_gadget_sub_6E7C4F40(self):
		#sub_6E7C4F40
		gadget = "A14891A66E83E0FEA34891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69148
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69148, eax
		#retn


  def test_gadget_sub_6E7C4F70(self):
		#sub_6E7C4F70
		gadget = "A15091A66E83E0FEA35091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69150
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69150, eax
		#retn


  def test_gadget_sub_6E7C4FA0(self):
		#sub_6E7C4FA0
		gadget = "A15891A66E83E0FEA35891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69158
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69158, eax
		#retn


  def test_gadget_sub_6E7C4FE0(self):
		#sub_6E7C4FE0
		gadget = "A16091A66E83E0FEA36091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69160
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69160, eax
		#retn


  def test_gadget_sub_6E7C5070(self):
		#sub_6E7C5070
		gadget = "A16891A66E83E0FEA36891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69168
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69168, eax
		#retn


  def test_gadget_sub_6E7C50B0(self):
		#sub_6E7C50B0
		gadget = "A17091A66E83E0FEA37091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69170
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69170, eax
		#retn


  def test_gadget_sub_6E7C50F0(self):
		#sub_6E7C50F0
		gadget = "A17891A66E83E0FEA37891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69178
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69178, eax
		#retn


  def test_gadget_sub_6E7C5120(self):
		#sub_6E7C5120
		gadget = "A18091A66E83E0FEA38091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69180
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69180, eax
		#retn


  def test_gadget_sub_6E7C5150(self):
		#sub_6E7C5150
		gadget = "A18891A66E83E0FEA38891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69188
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69188, eax
		#retn


  def test_gadget_sub_6E7C5180(self):
		#sub_6E7C5180
		gadget = "A19091A66E83E0FEA39091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69190
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69190, eax
		#retn


  def test_gadget_sub_6E7C51C0(self):
		#sub_6E7C51C0
		gadget = "A19891A66E83E0FEA39891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69198
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69198, eax
		#retn


  def test_gadget_sub_6E7C5250(self):
		#sub_6E7C5250
		gadget = "A1A091A66E83E0FEA3A091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691A0, eax
		#retn


  def test_gadget_sub_6E7C5280(self):
		#sub_6E7C5280
		gadget = "A1A891A66E83E0FEA3A891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691A8, eax
		#retn


  def test_gadget_sub_6E7C52B0(self):
		#sub_6E7C52B0
		gadget = "A1B091A66E83E0FEA3B091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691B0, eax
		#retn


  def test_gadget_sub_6E7C52E0(self):
		#sub_6E7C52E0
		gadget = "A1B891A66E83E0FEA3B891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691B8, eax
		#retn


  def test_gadget_sub_6E7C5310(self):
		#sub_6E7C5310
		gadget = "A1C091A66E83E0FEA3C091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691C0, eax
		#retn


  def test_gadget_sub_6E7C5490(self):
		#sub_6E7C5490
		gadget = "A1C891A66E83E0FEA3C891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691C8, eax
		#retn


  def test_gadget_sub_6E7C54C0(self):
		#sub_6E7C54C0
		gadget = "A1D091A66E83E0FEA3D091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691D0, eax
		#retn


  def test_gadget_sub_6E7C54F0(self):
		#sub_6E7C54F0
		gadget = "A1D891A66E83E0FEA3D891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691D8, eax
		#retn


  def test_gadget_sub_6E7C5520(self):
		#sub_6E7C5520
		gadget = "A1E091A66E83E0FEA3E091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691E0, eax
		#retn


  def test_gadget_sub_6E7C5550(self):
		#sub_6E7C5550
		gadget = "A1E891A66E83E0FEA3E891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691E8, eax
		#retn


  def test_gadget_sub_6E7C5580(self):
		#sub_6E7C5580
		gadget = "A1F091A66E83E0FEA3F091A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691F0, eax
		#retn


  def test_gadget_sub_6E7C55B0(self):
		#sub_6E7C55B0
		gadget = "A1F891A66E83E0FEA3F891A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA691F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA691F8, eax
		#retn


  def test_gadget_sub_6E7C55E0(self):
		#sub_6E7C55E0
		gadget = "A10092A66E83E0FEA30092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69200
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69200, eax
		#retn


  def test_gadget_sub_6E7C5610(self):
		#sub_6E7C5610
		gadget = "A10892A66E83E0FEA30892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69208
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69208, eax
		#retn


  def test_gadget_sub_6E7C5640(self):
		#sub_6E7C5640
		gadget = "A11092A66E83E0FEA31092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69210
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69210, eax
		#retn


  def test_gadget_sub_6E7C5670(self):
		#sub_6E7C5670
		gadget = "A11892A66E83E0FEA31892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69218
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69218, eax
		#retn


  def test_gadget_sub_6E7C56A0(self):
		#sub_6E7C56A0
		gadget = "A12092A66E83E0FEA32092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69220
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69220, eax
		#retn


  def test_gadget_sub_6E7C5750(self):
		#sub_6E7C5750
		gadget = "A12892A66E83E0FEA32892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69228
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69228, eax
		#retn


  def test_gadget_sub_6E7C5780(self):
		#sub_6E7C5780
		gadget = "A13092A66E83E0FEA33092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69230
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69230, eax
		#retn


  def test_gadget_sub_6E7C57B0(self):
		#sub_6E7C57B0
		gadget = "A13892A66E83E0FEA33892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69238
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69238, eax
		#retn


  def test_gadget_sub_6E7C5810(self):
		#sub_6E7C5810
		gadget = "A14092A66E83E0FEA34092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69240
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69240, eax
		#retn


  def test_gadget_sub_6E7C5850(self):
		#sub_6E7C5850
		gadget = "A14892A66E83E0FEA34892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69248
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69248, eax
		#retn


  def test_gadget_sub_6E7C5890(self):
		#sub_6E7C5890
		gadget = "A15092A66E83E0FEA35092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69250
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69250, eax
		#retn


  def test_gadget_sub_6E7C58C0(self):
		#sub_6E7C58C0
		gadget = "A15892A66E83E0FEA35892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69258
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69258, eax
		#retn


  def test_gadget_sub_6E7C58F0(self):
		#sub_6E7C58F0
		gadget = "A16092A66E83E0FEA36092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69260
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69260, eax
		#retn


  def test_gadget_sub_6E7C5920(self):
		#sub_6E7C5920
		gadget = "A16892A66E83E0FEA36892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69268
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69268, eax
		#retn


  def test_gadget_sub_6E7C5960(self):
		#sub_6E7C5960
		gadget = "A17092A66E83E0FEA37092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69270
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69270, eax
		#retn


  def test_gadget_sub_6E7C59A0(self):
		#sub_6E7C59A0
		gadget = "A17892A66E83E0FEA37892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69278
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69278, eax
		#retn


  def test_gadget_sub_6E7C5A20(self):
		#sub_6E7C5A20
		gadget = "A18092A66E83E0FEA38092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69280
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69280, eax
		#retn


  def test_gadget_sub_6E7C5A50(self):
		#sub_6E7C5A50
		gadget = "A18892A66E83E0FEA38892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69288
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69288, eax
		#retn


  def test_gadget_sub_6E7C5A80(self):
		#sub_6E7C5A80
		gadget = "A19092A66E83E0FEA39092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69290
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69290, eax
		#retn


  def test_gadget_sub_6E7C5AB0(self):
		#sub_6E7C5AB0
		gadget = "A19892A66E83E0FEA39892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69298
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69298, eax
		#retn


  def test_gadget_sub_6E7C5AE0(self):
		#sub_6E7C5AE0
		gadget = "A1A092A66E83E0FEA3A092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692A0, eax
		#retn


  def test_gadget_sub_6E7C5BE0(self):
		#sub_6E7C5BE0
		gadget = "A1A892A66E83E0FEA3A892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692A8, eax
		#retn


  def test_gadget_sub_6E7C5C20(self):
		#sub_6E7C5C20
		gadget = "A1B092A66E83E0FEA3B092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692B0, eax
		#retn


  def test_gadget_sub_6E7C5C60(self):
		#sub_6E7C5C60
		gadget = "A1B892A66E83E0FEA3B892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692B8, eax
		#retn


  def test_gadget_sub_6E7C5CC0(self):
		#sub_6E7C5CC0
		gadget = "A1C092A66E83E0FEA3C092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692C0, eax
		#retn


  def test_gadget_sub_6E7C5CF0(self):
		#sub_6E7C5CF0
		gadget = "A1C892A66E83E0FEA3C892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692C8, eax
		#retn


  def test_gadget_sub_6E7C5D20(self):
		#sub_6E7C5D20
		gadget = "A1D092A66E83E0FEA3D092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692D0, eax
		#retn


  def test_gadget_sub_6E7C5D50(self):
		#sub_6E7C5D50
		gadget = "A1D892A66E83E0FEA3D892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692D8, eax
		#retn


  def test_gadget_sub_6E7C5D80(self):
		#sub_6E7C5D80
		gadget = "A1E092A66E83E0FEA3E092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692E0, eax
		#retn


  def test_gadget_sub_6E7C5DB0(self):
		#sub_6E7C5DB0
		gadget = "A1E892A66E83E0FEA3E892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692E8, eax
		#retn


  def test_gadget_sub_6E7C5DF0(self):
		#sub_6E7C5DF0
		gadget = "A1F092A66E83E0FEA3F092A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692F0, eax
		#retn


  def test_gadget_sub_6E7C5ED0(self):
		#sub_6E7C5ED0
		gadget = "A1F892A66E83E0FEA3F892A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA692F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA692F8, eax
		#retn


  def test_gadget_sub_6E7C5F00(self):
		#sub_6E7C5F00
		gadget = "A10093A66E83E0FEA30093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69300
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69300, eax
		#retn


  def test_gadget_sub_6E7C5F30(self):
		#sub_6E7C5F30
		gadget = "A10893A66E83E0FEA30893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69308
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69308, eax
		#retn


  def test_gadget_sub_6E7C6010(self):
		#sub_6E7C6010
		gadget = "A11093A66E83E0FEA31093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69310
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69310, eax
		#retn


  def test_gadget_sub_6E7C6050(self):
		#sub_6E7C6050
		gadget = "A11893A66E83E0FEA31893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69318
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69318, eax
		#retn


  def test_gadget_sub_6E7C6090(self):
		#sub_6E7C6090
		gadget = "A12093A66E83E0FEA32093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69320
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69320, eax
		#retn


  def test_gadget_sub_6E7C60C0(self):
		#sub_6E7C60C0
		gadget = "A12893A66E83E0FEA32893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69328
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69328, eax
		#retn


  def test_gadget_sub_6E7C60F0(self):
		#sub_6E7C60F0
		gadget = "A13093A66E83E0FEA33093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69330
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69330, eax
		#retn


  def test_gadget_sub_6E7C6130(self):
		#sub_6E7C6130
		gadget = "A13893A66E83E0FEA33893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69338
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69338, eax
		#retn


  def test_gadget_sub_6E7C6170(self):
		#sub_6E7C6170
		gadget = "A14093A66E83E0FEA34093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69340
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69340, eax
		#retn


  def test_gadget_sub_6E7C61A0(self):
		#sub_6E7C61A0
		gadget = "A14893A66E83E0FEA34893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69348
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69348, eax
		#retn


  def test_gadget_sub_6E7C61D0(self):
		#sub_6E7C61D0
		gadget = "A15093A66E83E0FEA35093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69350
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69350, eax
		#retn


  def test_gadget_sub_6E7C6200(self):
		#sub_6E7C6200
		gadget = "A15893A66E83E0FEA35893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69358
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69358, eax
		#retn


  def test_gadget_sub_6E7C6270(self):
		#sub_6E7C6270
		gadget = "A16093A66E83E0FEA36093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69360
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69360, eax
		#retn


  def test_gadget_sub_6E7C62B0(self):
		#sub_6E7C62B0
		gadget = "A16893A66E83E0FEA36893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69368
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69368, eax
		#retn


  def test_gadget_sub_6E7C62F0(self):
		#sub_6E7C62F0
		gadget = "A17093A66E83E0FEA37093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69370
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69370, eax
		#retn


  def test_gadget_sub_6E7C6320(self):
		#sub_6E7C6320
		gadget = "A17893A66E83E0FEA37893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69378
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69378, eax
		#retn


  def test_gadget_sub_6E7C6350(self):
		#sub_6E7C6350
		gadget = "A18093A66E83E0FEA38093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69380
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69380, eax
		#retn


  def test_gadget_sub_6E7C6380(self):
		#sub_6E7C6380
		gadget = "A18893A66E83E0FEA38893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69388
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69388, eax
		#retn


  def test_gadget_sub_6E7C63B0(self):
		#sub_6E7C63B0
		gadget = "A19093A66E83E0FEA39093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69390
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69390, eax
		#retn


  def test_gadget_sub_6E7C63E0(self):
		#sub_6E7C63E0
		gadget = "A19893A66E83E0FEA39893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69398
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69398, eax
		#retn


  def test_gadget_sub_6E7C6410(self):
		#sub_6E7C6410
		gadget = "A1A093A66E83E0FEA3A093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693A0, eax
		#retn


  def test_gadget_sub_6E7C6440(self):
		#sub_6E7C6440
		gadget = "A1A893A66E83E0FEA3A893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693A8, eax
		#retn


  def test_gadget_sub_6E7C6480(self):
		#sub_6E7C6480
		gadget = "A1B093A66E83E0FEA3B093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693B0, eax
		#retn


  def test_gadget_sub_6E7C64C0(self):
		#sub_6E7C64C0
		gadget = "A1B893A66E83E0FEA3B893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693B8, eax
		#retn


  def test_gadget_sub_6E7C64F0(self):
		#sub_6E7C64F0
		gadget = "A1C093A66E83E0FEA3C093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693C0, eax
		#retn


  def test_gadget_sub_6E7C6520(self):
		#sub_6E7C6520
		gadget = "A1C893A66E83E0FEA3C893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693C8, eax
		#retn


  def test_gadget_sub_6E7C6550(self):
		#sub_6E7C6550
		gadget = "A1D093A66E83E0FEA3D093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693D0, eax
		#retn


  def test_gadget_sub_6E7C6660(self):
		#sub_6E7C6660
		gadget = "A1D893A66E83E0FEA3D893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693D8, eax
		#retn


  def test_gadget_sub_6E7C6690(self):
		#sub_6E7C6690
		gadget = "A1E093A66E83E0FEA3E093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693E0, eax
		#retn


  def test_gadget_sub_6E7C66C0(self):
		#sub_6E7C66C0
		gadget = "A1E893A66E83E0FEA3E893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693E8, eax
		#retn


  def test_gadget_sub_6E7C66F0(self):
		#sub_6E7C66F0
		gadget = "A1F093A66E83E0FEA3F093A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693F0, eax
		#retn


  def test_gadget_sub_6E7C6720(self):
		#sub_6E7C6720
		gadget = "A1F893A66E83E0FEA3F893A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA693F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA693F8, eax
		#retn


  def test_gadget_sub_6E7C6750(self):
		#sub_6E7C6750
		gadget = "A10094A66E83E0FEA30094A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69400
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69400, eax
		#retn


  def test_gadget_sub_6E7C6780(self):
		#sub_6E7C6780
		gadget = "A10894A66E83E0FEA30894A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69408
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69408, eax
		#retn


  def test_gadget_sub_6E7C6A40(self):
		#sub_6E7C6A40
		gadget = "A11094A66E83E0FEA31094A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69410
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69410, eax
		#retn


  def test_gadget_sub_6E7C6C40(self):
		#sub_6E7C6C40
		gadget = "A11894A66E83E0FEA31894A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69418
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69418, eax
		#retn


  def test_gadget_sub_6E7C6D30(self):
		#sub_6E7C6D30
		gadget = "A12094A66E83E0FEA32094A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69420
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69420, eax
		#retn


  def test_gadget_sub_6E7C71D0(self):
		#sub_6E7C71D0
		gadget = "A12C94A66E83E0FEA32C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6942C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6942C, eax
		#retn


  def test_gadget_sub_6E7C7200(self):
		#sub_6E7C7200
		gadget = "A13494A66E83E0FEA33494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69434
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69434, eax
		#retn


  def test_gadget_sub_6E7C7230(self):
		#sub_6E7C7230
		gadget = "A13C94A66E83E0FEA33C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6943C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6943C, eax
		#retn


  def test_gadget_sub_6E7C7260(self):
		#sub_6E7C7260
		gadget = "A14494A66E83E0FEA34494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69444
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69444, eax
		#retn


  def test_gadget_sub_6E7C7290(self):
		#sub_6E7C7290
		gadget = "A14C94A66E83E0FEA34C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6944C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6944C, eax
		#retn


  def test_gadget_sub_6E7C72C0(self):
		#sub_6E7C72C0
		gadget = "A15494A66E83E0FEA35494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69454
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69454, eax
		#retn


  def test_gadget_sub_6E7C72F0(self):
		#sub_6E7C72F0
		gadget = "A15C94A66E83E0FEA35C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6945C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6945C, eax
		#retn


  def test_gadget_sub_6E7C7320(self):
		#sub_6E7C7320
		gadget = "A16494A66E83E0FEA36494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69464
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69464, eax
		#retn


  def test_gadget_sub_6E7C7440(self):
		#sub_6E7C7440
		gadget = "A16C94A66E83E0FEA36C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6946C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6946C, eax
		#retn


  def test_gadget_sub_6E7C7470(self):
		#sub_6E7C7470
		gadget = "A17494A66E83E0FEA37494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69474
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69474, eax
		#retn


  def test_gadget_sub_6E7C74A0(self):
		#sub_6E7C74A0
		gadget = "A17C94A66E83E0FEA37C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6947C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6947C, eax
		#retn


  def test_gadget_sub_6E7C7560(self):
		#sub_6E7C7560
		gadget = "A18C94A66E83E0FEA38C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6948C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6948C, eax
		#retn


  def test_gadget_sub_6E7C7590(self):
		#sub_6E7C7590
		gadget = "A19494A66E83E0FEA39494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69494
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69494, eax
		#retn


  def test_gadget_sub_6E7C7690(self):
		#sub_6E7C7690
		gadget = "A19C94A66E83E0FEA39C94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6949C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6949C, eax
		#retn


  def test_gadget_sub_6E7C76C0(self):
		#sub_6E7C76C0
		gadget = "A1A494A66E83E0FEA3A494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694A4, eax
		#retn


  def test_gadget_sub_6E7C76F0(self):
		#sub_6E7C76F0
		gadget = "A1AC94A66E83E0FEA3AC94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694AC, eax
		#retn


  def test_gadget_sub_6E7C7720(self):
		#sub_6E7C7720
		gadget = "A1B494A66E83E0FEA3B494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694B4, eax
		#retn


  def test_gadget_sub_6E7C7750(self):
		#sub_6E7C7750
		gadget = "A1BC94A66E83E0FEA3BC94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694BC, eax
		#retn


  def test_gadget_sub_6E7C7780(self):
		#sub_6E7C7780
		gadget = "A1C494A66E83E0FEA3C494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694C4, eax
		#retn


  def test_gadget_sub_6E7C77B0(self):
		#sub_6E7C77B0
		gadget = "A1CC94A66E83E0FEA3CC94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694CC, eax
		#retn


  def test_gadget_sub_6E7C7890(self):
		#sub_6E7C7890
		gadget = "A1D494A66E83E0FEA3D494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694D4, eax
		#retn


  def test_gadget_sub_6E7C78C0(self):
		#sub_6E7C78C0
		gadget = "A1DC94A66E83E0FEA3DC94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694DC, eax
		#retn


  def test_gadget_sub_6E7C78F0(self):
		#sub_6E7C78F0
		gadget = "A1E494A66E83E0FEA3E494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694E4, eax
		#retn


  def test_gadget_sub_6E7C7920(self):
		#sub_6E7C7920
		gadget = "A1EC94A66E83E0FEA3EC94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694EC, eax
		#retn


  def test_gadget_sub_6E7C7950(self):
		#sub_6E7C7950
		gadget = "A1F494A66E83E0FEA3F494A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694F4, eax
		#retn


  def test_gadget_sub_6E7C7980(self):
		#sub_6E7C7980
		gadget = "A1FC94A66E83E0FEA3FC94A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA694FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA694FC, eax
		#retn


  def test_gadget_sub_6E7C79B0(self):
		#sub_6E7C79B0
		gadget = "A10495A66E83E0FEA30495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69504
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69504, eax
		#retn


  def test_gadget_sub_6E7C79E0(self):
		#sub_6E7C79E0
		gadget = "A10C95A66E83E0FEA30C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6950C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6950C, eax
		#retn


  def test_gadget_sub_6E7C7A10(self):
		#sub_6E7C7A10
		gadget = "A11495A66E83E0FEA31495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69514
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69514, eax
		#retn


  def test_gadget_sub_6E7C7BA0(self):
		#sub_6E7C7BA0
		gadget = "A11C95A66E83E0FEA31C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6951C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6951C, eax
		#retn


  def test_gadget_sub_6E7C7BE0(self):
		#sub_6E7C7BE0
		gadget = "A12495A66E83E0FEA32495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69524
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69524, eax
		#retn


  def test_gadget_sub_6E7C7C80(self):
		#sub_6E7C7C80
		gadget = "A12C95A66E83E0FEA32C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6952C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6952C, eax
		#retn


  def test_gadget_sub_6E7C7D30(self):
		#sub_6E7C7D30
		gadget = "A13495A66E83E0FEA33495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69534
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69534, eax
		#retn


  def test_gadget_sub_6E7C7D60(self):
		#sub_6E7C7D60
		gadget = "A13C95A66E83E0FEA33C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6953C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6953C, eax
		#retn


  def test_gadget_sub_6E7C7D90(self):
		#sub_6E7C7D90
		gadget = "A14495A66E83E0FEA34495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69544
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69544, eax
		#retn


  def test_gadget_sub_6E7C7DC0(self):
		#sub_6E7C7DC0
		gadget = "A14C95A66E83E0FEA34C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6954C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6954C, eax
		#retn


  def test_gadget_sub_6E7C7DF0(self):
		#sub_6E7C7DF0
		gadget = "A15495A66E83E0FEA35495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69554
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69554, eax
		#retn


  def test_gadget_sub_6E7C7E20(self):
		#sub_6E7C7E20
		gadget = "A15C95A66E83E0FEA35C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6955C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6955C, eax
		#retn


  def test_gadget_sub_6E7C7EB6(self):
		#sub_6E7C7EB6
		gadget = "A15C54A66E83E0FEA35C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6545C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6545C, eax
		#retn


  def test_gadget_sub_6E7C7F00(self):
		#sub_6E7C7F00
		gadget = "A16495A66E83E0FEA36495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69564
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69564, eax
		#retn


  def test_gadget_sub_6E7C7F30(self):
		#sub_6E7C7F30
		gadget = "A16C95A66E83E0FEA36C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6956C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6956C, eax
		#retn


  def test_gadget_sub_6E7C7F60(self):
		#sub_6E7C7F60
		gadget = "A17495A66E83E0FEA37495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69574
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69574, eax
		#retn


  def test_gadget_sub_6E7C7F90(self):
		#sub_6E7C7F90
		gadget = "A17C95A66E83E0FEA37C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6957C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6957C, eax
		#retn


  def test_gadget_sub_6E7C7FC0(self):
		#sub_6E7C7FC0
		gadget = "A18495A66E83E0FEA38495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69584
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69584, eax
		#retn


  def test_gadget_sub_6E7C7FF0(self):
		#sub_6E7C7FF0
		gadget = "A18C95A66E83E0FEA38C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6958C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6958C, eax
		#retn


  def test_gadget_sub_6E7C8020(self):
		#sub_6E7C8020
		gadget = "A19495A66E83E0FEA39495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69594
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69594, eax
		#retn


  def test_gadget_sub_6E7C80C0(self):
		#sub_6E7C80C0
		gadget = "A19C95A66E83E0FEA39C95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6959C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6959C, eax
		#retn


  def test_gadget_sub_6E7C8100(self):
		#sub_6E7C8100
		gadget = "A1A495A66E83E0FEA3A495A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695A4, eax
		#retn


  def test_gadget_sub_6E7C8140(self):
		#sub_6E7C8140
		gadget = "A1AC95A66E83E0FEA3AC95A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695AC, eax
		#retn


  def test_gadget_sub_6E7C8180(self):
		#sub_6E7C8180
		gadget = "A1B895A66E83E0FEA3B895A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695B8, eax
		#retn


  def test_gadget_sub_6E7C81B0(self):
		#sub_6E7C81B0
		gadget = "A1C095A66E83E0FEA3C095A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695C0, eax
		#retn


  def test_gadget_sub_6E7C81E0(self):
		#sub_6E7C81E0
		gadget = "A1C895A66E83E0FEA3C895A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695C8, eax
		#retn


  def test_gadget_sub_6E7C8210(self):
		#sub_6E7C8210
		gadget = "A1D095A66E83E0FEA3D095A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695D0, eax
		#retn


  def test_gadget_sub_6E7C8240(self):
		#sub_6E7C8240
		gadget = "A1D895A66E83E0FEA3D895A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695D8, eax
		#retn


  def test_gadget_sub_6E7C8270(self):
		#sub_6E7C8270
		gadget = "A1E095A66E83E0FEA3E095A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695E0, eax
		#retn


  def test_gadget_sub_6E7C82A0(self):
		#sub_6E7C82A0
		gadget = "A1E895A66E83E0FEA3E895A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695E8, eax
		#retn


  def test_gadget_sub_6E7C82E0(self):
		#sub_6E7C82E0
		gadget = "A1F095A66E83E0FEA3F095A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695F0, eax
		#retn


  def test_gadget_sub_6E7C8310(self):
		#sub_6E7C8310
		gadget = "A1F895A66E83E0FEA3F895A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA695F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA695F8, eax
		#retn


  def test_gadget_sub_6E7C8340(self):
		#sub_6E7C8340
		gadget = "A10096A66E83E0FEA30096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69600
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69600, eax
		#retn


  def test_gadget_sub_6E7C8370(self):
		#sub_6E7C8370
		gadget = "A10896A66E83E0FEA30896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69608
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69608, eax
		#retn


  def test_gadget_sub_6E7C8400(self):
		#sub_6E7C8400
		gadget = "A11096A66E83E0FEA31096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69610
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69610, eax
		#retn


  def test_gadget_sub_6E7C8430(self):
		#sub_6E7C8430
		gadget = "A11896A66E83E0FEA31896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69618
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69618, eax
		#retn


  def test_gadget_sub_6E7C8460(self):
		#sub_6E7C8460
		gadget = "A12096A66E83E0FEA32096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69620
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69620, eax
		#retn


  def test_gadget_sub_6E7C8490(self):
		#sub_6E7C8490
		gadget = "A12896A66E83E0FEA32896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69628
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69628, eax
		#retn


  def test_gadget_sub_6E7C84C0(self):
		#sub_6E7C84C0
		gadget = "A13096A66E83E0FEA33096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69630
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69630, eax
		#retn


  def test_gadget_sub_6E7C84F0(self):
		#sub_6E7C84F0
		gadget = "A13896A66E83E0FEA33896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69638
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69638, eax
		#retn


  def test_gadget_sub_6E7C8520(self):
		#sub_6E7C8520
		gadget = "A14096A66E83E0FEA34096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69640
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69640, eax
		#retn


  def test_gadget_sub_6E7C8550(self):
		#sub_6E7C8550
		gadget = "A14896A66E83E0FEA34896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69648
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69648, eax
		#retn


  def test_gadget_sub_6E7C8580(self):
		#sub_6E7C8580
		gadget = "A15096A66E83E0FEA35096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69650
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69650, eax
		#retn


  def test_gadget_sub_6E7C86A0(self):
		#sub_6E7C86A0
		gadget = "A15896A66E83E0FEA35896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69658
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69658, eax
		#retn


  def test_gadget_sub_6E7C86D0(self):
		#sub_6E7C86D0
		gadget = "A16096A66E83E0FEA36096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69660
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69660, eax
		#retn


  def test_gadget_sub_6E7C8700(self):
		#sub_6E7C8700
		gadget = "A16896A66E83E0FEA36896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69668
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69668, eax
		#retn


  def test_gadget_sub_6E7C8730(self):
		#sub_6E7C8730
		gadget = "A17096A66E83E0FEA37096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69670
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69670, eax
		#retn


  def test_gadget_sub_6E7C8910(self):
		#sub_6E7C8910
		gadget = "A19496A66E83E0FEA39496A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69694
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69694, eax
		#retn


  def test_gadget_sub_6E7C89B0(self):
		#sub_6E7C89B0
		gadget = "A19C96A66E83E0FEA39C96A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6969C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6969C, eax
		#retn


  def test_gadget_sub_6E7C8AA0(self):
		#sub_6E7C8AA0
		gadget = "A1A496A66E83E0FEA3A496A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696A4, eax
		#retn


  def test_gadget_sub_6E7C8AD0(self):
		#sub_6E7C8AD0
		gadget = "A1AC96A66E83E0FEA3AC96A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696AC, eax
		#retn


  def test_gadget_sub_6E7C9ED0(self):
		#sub_6E7C9ED0
		gadget = "A1D096A66E83E0FEA3D096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696D0, eax
		#retn


  def test_gadget_sub_6E7C9F00(self):
		#sub_6E7C9F00
		gadget = "A1D896A66E83E0FEA3D896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696D8, eax
		#retn


  def test_gadget_sub_6E7C9F30(self):
		#sub_6E7C9F30
		gadget = "A1E096A66E83E0FEA3E096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696E0, eax
		#retn


  def test_gadget_sub_6E7C9F60(self):
		#sub_6E7C9F60
		gadget = "A1E896A66E83E0FEA3E896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696E8, eax
		#retn


  def test_gadget_sub_6E7C9F90(self):
		#sub_6E7C9F90
		gadget = "A1F096A66E83E0FEA3F096A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696F0, eax
		#retn


  def test_gadget_sub_6E7C9FC0(self):
		#sub_6E7C9FC0
		gadget = "A1F896A66E83E0FEA3F896A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA696F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA696F8, eax
		#retn


  def test_gadget_sub_6E7C9FF0(self):
		#sub_6E7C9FF0
		gadget = "A10097A66E83E0FEA30097A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69700
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69700, eax
		#retn


  def test_gadget_sub_6E7CA020(self):
		#sub_6E7CA020
		gadget = "A10897A66E83E0FEA30897A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69708
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69708, eax
		#retn


  def test_gadget_sub_6E7CA050(self):
		#sub_6E7CA050
		gadget = "A11097A66E83E0FEA31097A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69710
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69710, eax
		#retn


  def test_gadget_sub_6E7CA080(self):
		#sub_6E7CA080
		gadget = "A11897A66E83E0FEA31897A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69718
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69718, eax
		#retn


  def test_gadget_sub_6E7CA0B0(self):
		#sub_6E7CA0B0
		gadget = "A12097A66E83E0FEA32097A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69720
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69720, eax
		#retn


  def test_gadget_sub_6E7CA0E0(self):
		#sub_6E7CA0E0
		gadget = "A12897A66E83E0FEA32897A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69728
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69728, eax
		#retn


  def test_gadget_sub_6E7CA110(self):
		#sub_6E7CA110
		gadget = "A13097A66E83E0FEA33097A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69730
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69730, eax
		#retn


  def test_gadget_sub_6E7CA28B(self):
		#sub_6E7CA28B
		gadget = "A15C54A66E83E0FEA35C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6545C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6545C, eax
		#retn


  def test_gadget_sub_6E7CA350(self):
		#sub_6E7CA350
		gadget = "A13C97A66E83E0FEA33C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6973C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6973C, eax
		#retn


  def test_gadget_sub_6E7CA3F0(self):
		#sub_6E7CA3F0
		gadget = "A14497A66E83E0FEA34497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69744
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69744, eax
		#retn


  def test_gadget_sub_6E7CA4B0(self):
		#sub_6E7CA4B0
		gadget = "A14C97A66E83E0FEA34C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6974C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6974C, eax
		#retn


  def test_gadget_sub_6E7CA6E0(self):
		#sub_6E7CA6E0
		gadget = "A15497A66E83E0FEA35497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69754
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69754, eax
		#retn


  def test_gadget_sub_6E7CA710(self):
		#sub_6E7CA710
		gadget = "A15C97A66E83E0FEA35C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6975C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6975C, eax
		#retn


  def test_gadget_sub_6E7CA740(self):
		#sub_6E7CA740
		gadget = "A16497A66E83E0FEA36497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69764
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69764, eax
		#retn


  def test_gadget_sub_6E7CA770(self):
		#sub_6E7CA770
		gadget = "A16C97A66E83E0FEA36C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6976C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6976C, eax
		#retn


  def test_gadget_sub_6E7CA7A0(self):
		#sub_6E7CA7A0
		gadget = "A17497A66E83E0FEA37497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69774
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69774, eax
		#retn


  def test_gadget_sub_6E7CA7D0(self):
		#sub_6E7CA7D0
		gadget = "A17C97A66E83E0FEA37C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6977C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6977C, eax
		#retn


  def test_gadget_sub_6E7CA800(self):
		#sub_6E7CA800
		gadget = "A18497A66E83E0FEA38497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69784
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69784, eax
		#retn


  def test_gadget_sub_6E7CA830(self):
		#sub_6E7CA830
		gadget = "A18C97A66E83E0FEA38C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6978C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6978C, eax
		#retn


  def test_gadget_sub_6E7CA8D6(self):
		#sub_6E7CA8D6
		gadget = "A15C54A66E83E0FEA35C54A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6545C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6545C, eax
		#retn


  def test_gadget_sub_6E7CA920(self):
		#sub_6E7CA920
		gadget = "A19497A66E83E0FEA39497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69794
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69794, eax
		#retn


  def test_gadget_sub_6E7CA950(self):
		#sub_6E7CA950
		gadget = "A19C97A66E83E0FEA39C97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6979C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6979C, eax
		#retn


  def test_gadget_sub_6E7CA980(self):
		#sub_6E7CA980
		gadget = "A1A497A66E83E0FEA3A497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697A4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697A4, eax
		#retn


  def test_gadget_sub_6E7CA9B0(self):
		#sub_6E7CA9B0
		gadget = "A1AC97A66E83E0FEA3AC97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697AC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697AC, eax
		#retn


  def test_gadget_sub_6E7CA9E0(self):
		#sub_6E7CA9E0
		gadget = "A1B497A66E83E0FEA3B497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697B4, eax
		#retn


  def test_gadget_sub_6E7CAA10(self):
		#sub_6E7CAA10
		gadget = "A1BC97A66E83E0FEA3BC97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697BC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697BC, eax
		#retn


  def test_gadget_sub_6E7CAA40(self):
		#sub_6E7CAA40
		gadget = "A1C497A66E83E0FEA3C497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697C4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697C4, eax
		#retn


  def test_gadget_sub_6E7CAA70(self):
		#sub_6E7CAA70
		gadget = "A1CC97A66E83E0FEA3CC97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697CC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697CC, eax
		#retn


  def test_gadget_sub_6E7CAAA0(self):
		#sub_6E7CAAA0
		gadget = "A1D497A66E83E0FEA3D497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697D4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697D4, eax
		#retn


  def test_gadget_sub_6E7CABA0(self):
		#sub_6E7CABA0
		gadget = "A1DC97A66E83E0FEA3DC97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697DC, eax
		#retn


  def test_gadget_sub_6E7CABE0(self):
		#sub_6E7CABE0
		gadget = "A1E497A66E83E0FEA3E497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697E4, eax
		#retn


  def test_gadget_sub_6E7CAD60(self):
		#sub_6E7CAD60
		gadget = "A1EC97A66E83E0FEA3EC97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697EC, eax
		#retn


  def test_gadget_sub_6E7CADC0(self):
		#sub_6E7CADC0
		gadget = "A1F497A66E83E0FEA3F497A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697F4, eax
		#retn


  def test_gadget_sub_6E7CADF0(self):
		#sub_6E7CADF0
		gadget = "A1FC97A66E83E0FEA3FC97A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA697FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA697FC, eax
		#retn


  def test_gadget_sub_6E7CAE20(self):
		#sub_6E7CAE20
		gadget = "A10498A66E83E0FEA30498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69804
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69804, eax
		#retn


  def test_gadget_sub_6E7CAE50(self):
		#sub_6E7CAE50
		gadget = "A10C98A66E83E0FEA30C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6980C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6980C, eax
		#retn


  def test_gadget_sub_6E7CAE80(self):
		#sub_6E7CAE80
		gadget = "A11498A66E83E0FEA31498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69814
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69814, eax
		#retn


  def test_gadget_sub_6E7CAEB0(self):
		#sub_6E7CAEB0
		gadget = "A11C98A66E83E0FEA31C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6981C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6981C, eax
		#retn


  def test_gadget_sub_6E7CAEE0(self):
		#sub_6E7CAEE0
		gadget = "A12498A66E83E0FEA32498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69824
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69824, eax
		#retn


  def test_gadget_sub_6E7CB060(self):
		#sub_6E7CB060
		gadget = "A12C98A66E83E0FEA32C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6982C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6982C, eax
		#retn


  def test_gadget_sub_6E7CB0C0(self):
		#sub_6E7CB0C0
		gadget = "A13498A66E83E0FEA33498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69834
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69834, eax
		#retn


  def test_gadget_sub_6E7CB0F0(self):
		#sub_6E7CB0F0
		gadget = "A13C98A66E83E0FEA33C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6983C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6983C, eax
		#retn


  def test_gadget_sub_6E7CB120(self):
		#sub_6E7CB120
		gadget = "A14498A66E83E0FEA34498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69844
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69844, eax
		#retn


  def test_gadget_sub_6E7CB250(self):
		#sub_6E7CB250
		gadget = "A14C98A66E83E0FEA34C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6984C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6984C, eax
		#retn


  def test_gadget_sub_6E7CB280(self):
		#sub_6E7CB280
		gadget = "A15498A66E83E0FEA35498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69854
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69854, eax
		#retn


  def test_gadget_sub_6E7CB2B0(self):
		#sub_6E7CB2B0
		gadget = "A15C98A66E83E0FEA35C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6985C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6985C, eax
		#retn


  def test_gadget_sub_6E7CB3F0(self):
		#sub_6E7CB3F0
		gadget = "A16498A66E83E0FEA36498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69864
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69864, eax
		#retn


  def test_gadget_sub_6E7CB430(self):
		#sub_6E7CB430
		gadget = "A16C98A66E83E0FEA36C98A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6986C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6986C, eax
		#retn


  def test_gadget_sub_6E7CB470(self):
		#sub_6E7CB470
		gadget = "A17498A66E83E0FEA37498A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69874
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69874, eax
		#retn


  def test_gadget_sub_6E7CB550(self):
		#sub_6E7CB550
		gadget = "A18098A66E83E0FEA38098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69880
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69880, eax
		#retn


  def test_gadget_sub_6E7CB580(self):
		#sub_6E7CB580
		gadget = "A18898A66E83E0FEA38898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69888
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69888, eax
		#retn


  def test_gadget_sub_6E7CB5B0(self):
		#sub_6E7CB5B0
		gadget = "A19098A66E83E0FEA39098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69890
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69890, eax
		#retn


  def test_gadget_sub_6E7CB710(self):
		#sub_6E7CB710
		gadget = "A19898A66E83E0FEA39898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69898
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69898, eax
		#retn


  def test_gadget_sub_6E7CB740(self):
		#sub_6E7CB740
		gadget = "A1A098A66E83E0FEA3A098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698A0, eax
		#retn


  def test_gadget_sub_6E7CB770(self):
		#sub_6E7CB770
		gadget = "A1A898A66E83E0FEA3A898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698A8, eax
		#retn


  def test_gadget_sub_6E7CB800(self):
		#sub_6E7CB800
		gadget = "A1B098A66E83E0FEA3B098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698B0, eax
		#retn


  def test_gadget_sub_6E7CB830(self):
		#sub_6E7CB830
		gadget = "A1B898A66E83E0FEA3B898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698B8, eax
		#retn


  def test_gadget_sub_6E7CB860(self):
		#sub_6E7CB860
		gadget = "A1C098A66E83E0FEA3C098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698C0, eax
		#retn


  def test_gadget_sub_6E7CB8C0(self):
		#sub_6E7CB8C0
		gadget = "A1C898A66E83E0FEA3C898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698C8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698C8, eax
		#retn


  def test_gadget_sub_6E7CB8F0(self):
		#sub_6E7CB8F0
		gadget = "A1D098A66E83E0FEA3D098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698D0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698D0, eax
		#retn


  def test_gadget_sub_6E7CB920(self):
		#sub_6E7CB920
		gadget = "A1D898A66E83E0FEA3D898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698D8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698D8, eax
		#retn


  def test_gadget_sub_6E7CB950(self):
		#sub_6E7CB950
		gadget = "A1E098A66E83E0FEA3E098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698E0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698E0, eax
		#retn


  def test_gadget_sub_6E7CBA80(self):
		#sub_6E7CBA80
		gadget = "A1E898A66E83E0FEA3E898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698E8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698E8, eax
		#retn


  def test_gadget_sub_6E7CBB00(self):
		#sub_6E7CBB00
		gadget = "A1F098A66E83E0FEA3F098A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698F0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698F0, eax
		#retn


  def test_gadget_sub_6E7CBB30(self):
		#sub_6E7CBB30
		gadget = "A1F898A66E83E0FEA3F898A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA698F8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA698F8, eax
		#retn


  def test_gadget_sub_6E7CBC90(self):
		#sub_6E7CBC90
		gadget = "A10C99A66E83E0FEA30C99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6990C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6990C, eax
		#retn


  def test_gadget_sub_6E7CBD50(self):
		#sub_6E7CBD50
		gadget = "A11899A66E83E0FEA31899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69918
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69918, eax
		#retn


  def test_gadget_sub_6E7CBD80(self):
		#sub_6E7CBD80
		gadget = "A12099A66E83E0FEA32099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69920
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69920, eax
		#retn


  def test_gadget_sub_6E7CBDC0(self):
		#sub_6E7CBDC0
		gadget = "A12899A66E83E0FEA32899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69928
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69928, eax
		#retn


  def test_gadget_sub_6E7CBDF0(self):
		#sub_6E7CBDF0
		gadget = "A13099A66E83E0FEA33099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69930
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69930, eax
		#retn


  def test_gadget_sub_6E7CBE20(self):
		#sub_6E7CBE20
		gadget = "A13899A66E83E0FEA33899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69938
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69938, eax
		#retn


  def test_gadget_sub_6E7CBE90(self):
		#sub_6E7CBE90
		gadget = "A14099A66E83E0FEA34099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69940
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69940, eax
		#retn


  def test_gadget_sub_6E7CBF20(self):
		#sub_6E7CBF20
		gadget = "A14899A66E83E0FEA34899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69948
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69948, eax
		#retn


  def test_gadget_sub_6E7CBF50(self):
		#sub_6E7CBF50
		gadget = "A15099A66E83E0FEA35099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69950
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69950, eax
		#retn


  def test_gadget_sub_6E7CBF80(self):
		#sub_6E7CBF80
		gadget = "A15899A66E83E0FEA35899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69958
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69958, eax
		#retn


  def test_gadget_sub_6E7CC0A0(self):
		#sub_6E7CC0A0
		gadget = "A16099A66E83E0FEA36099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69960
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69960, eax
		#retn


  def test_gadget_sub_6E7CC0D0(self):
		#sub_6E7CC0D0
		gadget = "A16899A66E83E0FEA36899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69968
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69968, eax
		#retn


  def test_gadget_sub_6E7CC100(self):
		#sub_6E7CC100
		gadget = "A17099A66E83E0FEA37099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69970
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69970, eax
		#retn


  def test_gadget_sub_6E7CC130(self):
		#sub_6E7CC130
		gadget = "A17899A66E83E0FEA37899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69978
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69978, eax
		#retn


  def test_gadget_sub_6E7CC160(self):
		#sub_6E7CC160
		gadget = "A18099A66E83E0FEA38099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69980
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69980, eax
		#retn


  def test_gadget_sub_6E7CC190(self):
		#sub_6E7CC190
		gadget = "A18899A66E83E0FEA38899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69988
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69988, eax
		#retn


  def test_gadget_sub_6E7CC210(self):
		#sub_6E7CC210
		gadget = "A19099A66E83E0FEA39099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69990
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69990, eax
		#retn


  def test_gadget_sub_6E7CC240(self):
		#sub_6E7CC240
		gadget = "A19899A66E83E0FEA39899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69998
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69998, eax
		#retn


  def test_gadget_sub_6E7CC270(self):
		#sub_6E7CC270
		gadget = "A1A099A66E83E0FEA3A099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699A0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699A0, eax
		#retn


  def test_gadget_sub_6E7CC2A0(self):
		#sub_6E7CC2A0
		gadget = "A1A899A66E83E0FEA3A899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699A8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699A8, eax
		#retn


  def test_gadget_sub_6E7CC2D0(self):
		#sub_6E7CC2D0
		gadget = "A1B099A66E83E0FEA3B099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699B0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699B0, eax
		#retn


  def test_gadget_sub_6E7CC300(self):
		#sub_6E7CC300
		gadget = "A1B899A66E83E0FEA3B899A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699B8
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699B8, eax
		#retn


  def test_gadget_sub_6E7CC330(self):
		#sub_6E7CC330
		gadget = "A1C099A66E83E0FEA3C099A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699C0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699C0, eax
		#retn


  def test_gadget_sub_6E7CC480(self):
		#sub_6E7CC480
		gadget = "A1DC99A66E83E0FEA3DC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699DC, eax
		#retn


  def test_gadget_sub_6E7CC499(self):
		#sub_6E7CC499
		gadget = "A1DC99A66E83E0FDA3DC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699DC
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA699DC, eax
		#retn


  def test_gadget_sub_6E7CC4B2(self):
		#sub_6E7CC4B2
		gadget = "A1DC99A66E83E0FBA3DC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699DC
		#and     eax, 0FFFFFFFBh
		#mov     dword_6EA699DC, eax
		#retn


  def test_gadget_sub_6E7CC4CB(self):
		#sub_6E7CC4CB
		gadget = "A1DC99A66E83E0F7A3DC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699DC
		#and     eax, 0FFFFFFF7h
		#mov     dword_6EA699DC, eax
		#retn


  def test_gadget_sub_6E7CC4E4(self):
		#sub_6E7CC4E4
		gadget = "A1DC99A66E83E0EFA3DC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699DC
		#and     eax, 0FFFFFFEFh
		#mov     dword_6EA699DC, eax
		#retn


  def test_gadget_sub_6E7CC4FD(self):
		#sub_6E7CC4FD
		gadget = "A1DC99A66E83E0DFA3DC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699DC
		#and     eax, 0FFFFFFDFh
		#mov     dword_6EA699DC, eax
		#retn


  def test_gadget_sub_6E7CD2F0(self):
		#sub_6E7CD2F0
		gadget = "A1E499A66E83E0FEA3E499A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699E4, eax
		#retn


  def test_gadget_sub_6E7CD320(self):
		#sub_6E7CD320
		gadget = "A1EC99A66E83E0FEA3EC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699EC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699EC, eax
		#retn


  def test_gadget_sub_6E7CD390(self):
		#sub_6E7CD390
		gadget = "A1F499A66E83E0FEA3F499A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699F4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699F4, eax
		#retn


  def test_gadget_sub_6E7CD3C0(self):
		#sub_6E7CD3C0
		gadget = "A1FC99A66E83E0FEA3FC99A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA699FC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA699FC, eax
		#retn


  def test_gadget_sub_6E7CD3F0(self):
		#sub_6E7CD3F0
		gadget = "A1049AA66E83E0FEA3049AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A04
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A04, eax
		#retn


  def test_gadget_sub_6E7CD420(self):
		#sub_6E7CD420
		gadget = "A10C9AA66E83E0FEA30C9AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A0C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A0C, eax
		#retn


  def test_gadget_sub_6E7CD450(self):
		#sub_6E7CD450
		gadget = "A1149AA66E83E0FEA3149AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A14
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A14, eax
		#retn


  def test_gadget_sub_6E7CD480(self):
		#sub_6E7CD480
		gadget = "A11C9AA66E83E0FEA31C9AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A1C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A1C, eax
		#retn


  def test_gadget_sub_6E7CD4B0(self):
		#sub_6E7CD4B0
		gadget = "A1249AA66E83E0FEA3249AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A24
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A24, eax
		#retn


  def test_gadget_sub_6E7CD860(self):
		#sub_6E7CD860
		gadget = "A12C9AA66E83E0FEA32C9AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A2C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A2C, eax
		#retn


  def test_gadget_sub_6E7CD890(self):
		#sub_6E7CD890
		gadget = "A1349AA66E83E0FEA3349AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A34
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A34, eax
		#retn


  def test_gadget_sub_6E7CD8C0(self):
		#sub_6E7CD8C0
		gadget = "A13C9AA66E83E0FEA33C9AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A3C, eax
		#retn


  def test_gadget_sub_6E7CD8F0(self):
		#sub_6E7CD8F0
		gadget = "A1449AA66E83E0FEA3449AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A44
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A44, eax
		#retn


  def test_gadget_sub_6E7CD920(self):
		#sub_6E7CD920
		gadget = "A14C9AA66E83E0FEA34C9AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A4C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A4C, eax
		#retn


  def test_gadget_sub_6E7CD9E0(self):
		#sub_6E7CD9E0
		gadget = "A1549AA66E83E0FEA3549AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A54
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A54, eax
		#retn


  def test_gadget_sub_6E7CDA20(self):
		#sub_6E7CDA20
		gadget = "A15C9AA66E83E0FEA35C9AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A5C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A5C, eax
		#retn


  def test_gadget_sub_6E7CDA60(self):
		#sub_6E7CDA60
		gadget = "A1649AA66E83E0FEA3649AA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA69A64
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA69A64, eax
		#retn


  def test_gadget_sub_6E7CE120(self):
		#sub_6E7CE120
		gadget = "A1DCA6A66E83E0FEA3DCA6A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6A6DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6A6DC, eax
		#retn


  def test_gadget_sub_6E7CE540(self):
		#sub_6E7CE540
		gadget = "A140A7A66E83E0FEA340A7A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6A740
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6A740, eax
		#retn


  def test_gadget_sub_6E7CE5E9(self):
		#sub_6E7CE5E9
		gadget = "A140A7A66E83E0FEA340A7A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6A740
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6A740, eax
		#retn


  def test_gadget_sub_6E7CEBA0(self):
		#sub_6E7CEBA0
		gadget = "A184ABA66E83E0FEA384ABA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6AB84
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6AB84, eax
		#retn


  def test_gadget_sub_6E7CEC10(self):
		#sub_6E7CEC10
		gadget = "A1B0ABA66E83E0FEA3B0ABA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6ABB0
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6ABB0, eax
		#retn


  def test_gadget_sub_6E7CEC1E(self):
		#sub_6E7CEC1E
		gadget = "A1B0ABA66E83E0FDA3B0ABA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6ABB0
		#and     eax, 0FFFFFFFDh
		#mov     dword_6EA6ABB0, eax
		#retn


  def test_gadget_sub_6E7D1A30(self):
		#sub_6E7D1A30
		gadget = "A130ACA66E83E0FEA330ACA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6AC30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6AC30, eax
		#retn


  def test_gadget_sub_6E7D1A70(self):
		#sub_6E7D1A70
		gadget = "A13CACA66E83E0FEA33CACA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6AC3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6AC3C, eax
		#retn


  def test_gadget_sub_6E7D1AA0(self):
		#sub_6E7D1AA0
		gadget = "A130ACA66E83E0FEA330ACA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6AC30
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6AC30, eax
		#retn


  def test_gadget_sub_6E7D1AC1(self):
		#sub_6E7D1AC1
		gadget = "A13CACA66E83E0FEA33CACA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6AC3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6AC3C, eax
		#retn


  def test_gadget_sub_6E7D1ACF(self):
		#sub_6E7D1ACF
		gadget = "A13CACA66E83E0FEA33CACA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6AC3C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6AC3C, eax
		#retn


  def test_gadget_sub_6E7D23B0(self):
		#sub_6E7D23B0
		gadget = "A1A4ACA66E83E0FEA3A4ACA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6ACA4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6ACA4, eax
		#retn


  def test_gadget_sub_6E7D2850(self):
		#sub_6E7D2850
		gadget = "A1CCADA66E83E0FEA3CCADA66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6ADCC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6ADCC, eax
		#retn


  def test_gadget_sub_6E7D3930(self):
		#sub_6E7D3930
		gadget = "A1B4B1A66E83E0FEA3B4B1A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B1B4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B1B4, eax
		#retn


  def test_gadget_sub_6E7D4E00(self):
		#sub_6E7D4E00
		gadget = "A1DCB1A66E83E0FEA3DCB1A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B1DC
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B1DC, eax
		#retn


  def test_gadget_sub_6E7D4E40(self):
		#sub_6E7D4E40
		gadget = "A1E4B1A66E83E0FEA3E4B1A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B1E4
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B1E4, eax
		#retn


  def test_gadget_sub_6E7DB6D0(self):
		#sub_6E7DB6D0
		gadget = "A124B2A66E83E0FEA324B2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B224
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B224, eax
		#retn


  def test_gadget_sub_6E7DB6DE(self):
		#sub_6E7DB6DE
		gadget = "A11CB2A66E83E0FEA31CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B21C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B21C, eax
		#retn


  def test_gadget_sub_6E7DB6EC(self):
		#sub_6E7DB6EC
		gadget = "A11CB2A66E83E0FEA31CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B21C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B21C, eax
		#retn


  def test_gadget_sub_6E7DB720(self):
		#sub_6E7DB720
		gadget = "A12CB2A66E83E0FEA32CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B22C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B22C, eax
		#retn


  def test_gadget_sub_6E7DB72E(self):
		#sub_6E7DB72E
		gadget = "A11CB2A66E83E0FEA31CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B21C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B21C, eax
		#retn


  def test_gadget_sub_6E7DB760(self):
		#sub_6E7DB760
		gadget = "A134B2A66E83E0FEA334B2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B234
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B234, eax
		#retn


  def test_gadget_sub_6E7DB76E(self):
		#sub_6E7DB76E
		gadget = "A11CB2A66E83E0FEA31CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B21C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B21C, eax
		#retn


  def test_gadget_sub_6E7DB7A0(self):
		#sub_6E7DB7A0
		gadget = "A13CB2A66E83E0FEA33CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B23C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B23C, eax
		#retn


  def test_gadget_sub_6E7DB7AE(self):
		#sub_6E7DB7AE
		gadget = "A11CB2A66E83E0FEA31CB2A66EC3"
		self.do(gadget)

		#mov     eax, dword_6EA6B21C
		#and     eax, 0FFFFFFFEh
		#mov     dword_6EA6B21C, eax
		#retn


  def test_gadget_sub_6E7E7E80(self):
		#sub_6E7E7E80
		gadget = "33C0A3587BA66EA35C7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67B58, eax
		#mov     dword_6EA67B5C, eax
		#retn


  def test_gadget_sub_6E7E7E90(self):
		#sub_6E7E7E90
		gadget = "33C0A3687BA66EA36C7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67B68, eax
		#mov     dword_6EA67B6C, eax
		#retn


  def test_gadget_sub_6E7E7EA0(self):
		#sub_6E7E7EA0
		gadget = "33C0A3787BA66EA37C7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67B78, eax
		#mov     dword_6EA67B7C, eax
		#retn


  def test_gadget_sub_6E7E7EB0(self):
		#sub_6E7E7EB0
		gadget = "33C0A3887BA66EA38C7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67B88, eax
		#mov     dword_6EA67B8C, eax
		#retn


  def test_gadget_sub_6E7E7EC0(self):
		#sub_6E7E7EC0
		gadget = "33C0A3987BA66EA39C7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67B98, eax
		#mov     dword_6EA67B9C, eax
		#retn


  def test_gadget_sub_6E7E7ED0(self):
		#sub_6E7E7ED0
		gadget = "33C0A3A87BA66EA3AC7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67BA8, eax
		#mov     dword_6EA67BAC, eax
		#retn


  def test_gadget_sub_6E7E7EE0(self):
		#sub_6E7E7EE0
		gadget = "33C0A3B87BA66EA3BC7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67BB8, eax
		#mov     dword_6EA67BBC, eax
		#retn


  def test_gadget_sub_6E7E7EF0(self):
		#sub_6E7E7EF0
		gadget = "33C0A3C87BA66EA3CC7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67BC8, eax
		#mov     dword_6EA67BCC, eax
		#retn


  def test_gadget_sub_6E7E7F00(self):
		#sub_6E7E7F00
		gadget = "33C0A3D87BA66EA3DC7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67BD8, eax
		#mov     dword_6EA67BDC, eax
		#retn


  def test_gadget_sub_6E7E7F10(self):
		#sub_6E7E7F10
		gadget = "33C0A3E87BA66EA3EC7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67BE8, eax
		#mov     dword_6EA67BEC, eax
		#retn


  def test_gadget_sub_6E7E7F20(self):
		#sub_6E7E7F20
		gadget = "33C0A3F87BA66EA3FC7BA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67BF8, eax
		#mov     dword_6EA67BFC, eax
		#retn


  def test_gadget_sub_6E7E7F30(self):
		#sub_6E7E7F30
		gadget = "33C0A3087CA66EA30C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C08, eax
		#mov     dword_6EA67C0C, eax
		#retn


  def test_gadget_sub_6E7E7F40(self):
		#sub_6E7E7F40
		gadget = "33C0A3187CA66EA31C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C18, eax
		#mov     dword_6EA67C1C, eax
		#retn


  def test_gadget_sub_6E7E7F50(self):
		#sub_6E7E7F50
		gadget = "33C0A3287CA66EA32C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C28, eax
		#mov     dword_6EA67C2C, eax
		#retn


  def test_gadget_sub_6E7E7F60(self):
		#sub_6E7E7F60
		gadget = "33C0A3387CA66EA33C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C38, eax
		#mov     dword_6EA67C3C, eax
		#retn


  def test_gadget_sub_6E7E7F70(self):
		#sub_6E7E7F70
		gadget = "33C0A3487CA66EA34C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C48, eax
		#mov     dword_6EA67C4C, eax
		#retn


  def test_gadget_sub_6E7E7F80(self):
		#sub_6E7E7F80
		gadget = "33C0A3587CA66EA35C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C58, eax
		#mov     dword_6EA67C5C, eax
		#retn


  def test_gadget_sub_6E7E7F90(self):
		#sub_6E7E7F90
		gadget = "33C0A3687CA66EA36C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C68, eax
		#mov     dword_6EA67C6C, eax
		#retn


  def test_gadget_sub_6E7E7FA0(self):
		#sub_6E7E7FA0
		gadget = "33C0A3787CA66EA37C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C78, eax
		#mov     dword_6EA67C7C, eax
		#retn


  def test_gadget_sub_6E7E7FB0(self):
		#sub_6E7E7FB0
		gadget = "33C0A3887CA66EA38C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C88, eax
		#mov     dword_6EA67C8C, eax
		#retn


  def test_gadget_sub_6E7E7FC0(self):
		#sub_6E7E7FC0
		gadget = "33C0A3987CA66EA39C7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67C98, eax
		#mov     dword_6EA67C9C, eax
		#retn


  def test_gadget_sub_6E7E7FD0(self):
		#sub_6E7E7FD0
		gadget = "33C0A3A87CA66EA3AC7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67CA8, eax
		#mov     dword_6EA67CAC, eax
		#retn


  def test_gadget_sub_6E7E7FE0(self):
		#sub_6E7E7FE0
		gadget = "33C0A3B87CA66EA3BC7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67CB8, eax
		#mov     dword_6EA67CBC, eax
		#retn


  def test_gadget_sub_6E7E7FF0(self):
		#sub_6E7E7FF0
		gadget = "33C0A3C87CA66EA3CC7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67CC8, eax
		#mov     dword_6EA67CCC, eax
		#retn


  def test_gadget_sub_6E7E8000(self):
		#sub_6E7E8000
		gadget = "33C0A3D87CA66EA3DC7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67CD8, eax
		#mov     dword_6EA67CDC, eax
		#retn


  def test_gadget_sub_6E7E8010(self):
		#sub_6E7E8010
		gadget = "33C0A3E87CA66EA3EC7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67CE8, eax
		#mov     dword_6EA67CEC, eax
		#retn


  def test_gadget_sub_6E7E8020(self):
		#sub_6E7E8020
		gadget = "33C0A3F87CA66EA3FC7CA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67CF8, eax
		#mov     dword_6EA67CFC, eax
		#retn


  def test_gadget_sub_6E7E8030(self):
		#sub_6E7E8030
		gadget = "33C0A3087DA66EA30C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D08, eax
		#mov     dword_6EA67D0C, eax
		#retn


  def test_gadget_sub_6E7E8040(self):
		#sub_6E7E8040
		gadget = "33C0A3187DA66EA31C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D18, eax
		#mov     dword_6EA67D1C, eax
		#retn


  def test_gadget_sub_6E7E8050(self):
		#sub_6E7E8050
		gadget = "33C0A3287DA66EA32C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D28, eax
		#mov     dword_6EA67D2C, eax
		#retn


  def test_gadget_sub_6E7E8060(self):
		#sub_6E7E8060
		gadget = "33C0A3387DA66EA33C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D38, eax
		#mov     dword_6EA67D3C, eax
		#retn


  def test_gadget_sub_6E7E8070(self):
		#sub_6E7E8070
		gadget = "33C0A3487DA66EA34C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D48, eax
		#mov     dword_6EA67D4C, eax
		#retn


  def test_gadget_sub_6E7E8080(self):
		#sub_6E7E8080
		gadget = "33C0A3587DA66EA35C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D58, eax
		#mov     dword_6EA67D5C, eax
		#retn


  def test_gadget_sub_6E7E8090(self):
		#sub_6E7E8090
		gadget = "33C0A3687DA66EA36C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D68, eax
		#mov     dword_6EA67D6C, eax
		#retn


  def test_gadget_sub_6E7E80A0(self):
		#sub_6E7E80A0
		gadget = "33C0A3787DA66EA37C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D78, eax
		#mov     dword_6EA67D7C, eax
		#retn


  def test_gadget_sub_6E7E80B0(self):
		#sub_6E7E80B0
		gadget = "33C0A3887DA66EA38C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D88, eax
		#mov     dword_6EA67D8C, eax
		#retn


  def test_gadget_sub_6E7E80C0(self):
		#sub_6E7E80C0
		gadget = "33C0A3987DA66EA39C7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67D98, eax
		#mov     dword_6EA67D9C, eax
		#retn


  def test_gadget_sub_6E7E80D0(self):
		#sub_6E7E80D0
		gadget = "33C0A3A87DA66EA3AC7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67DA8, eax
		#mov     dword_6EA67DAC, eax
		#retn


  def test_gadget_sub_6E7E80E0(self):
		#sub_6E7E80E0
		gadget = "33C0A3B87DA66EA3BC7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67DB8, eax
		#mov     dword_6EA67DBC, eax
		#retn


  def test_gadget_sub_6E7E80F0(self):
		#sub_6E7E80F0
		gadget = "33C0A3C87DA66EA3CC7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67DC8, eax
		#mov     dword_6EA67DCC, eax
		#retn


  def test_gadget_sub_6E7E8100(self):
		#sub_6E7E8100
		gadget = "33C0A3D87DA66EA3DC7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67DD8, eax
		#mov     dword_6EA67DDC, eax
		#retn


  def test_gadget_sub_6E7E8110(self):
		#sub_6E7E8110
		gadget = "33C0A3E87DA66EA3EC7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67DE8, eax
		#mov     dword_6EA67DEC, eax
		#retn


  def test_gadget_sub_6E7E8120(self):
		#sub_6E7E8120
		gadget = "33C0A3F87DA66EA3FC7DA66EC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword_6EA67DF8, eax
		#mov     dword_6EA67DFC, eax
		#retn


  def test_gadget_sub_6E7E8B80(self):
		#sub_6E7E8B80
		gadget = "C705DC81A66E9C658A6EC3"
		self.do(gadget)

		#mov     dword_6EA681DC, offset off_6E8A659C
		#retn


  def test_gadget_sub_6E7E9270(self):
		#sub_6E7E9270
		gadget = "C7057448A66E1CCD926EC3"
		self.do(gadget)

		#mov     off_6EA64874, offset off_6E92CD1C
		#retn


  def test_gadget_sub_6E7E927B(self):
		#sub_6E7E927B
		gadget = "C7057C48A66E1CCD926EC3"
		self.do(gadget)

		#mov     off_6EA6487C, offset off_6E92CD1C
		#retn


  def test_gadget_sub_6E7E9286(self):
		#sub_6E7E9286
		gadget = "C7058448A66E1CCD926EC3"
		self.do(gadget)

		#mov     off_6EA64884, offset off_6E92CD1C
		#retn


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()