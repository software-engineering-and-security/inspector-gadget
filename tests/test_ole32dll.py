import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetsqmapidll(unittest.TestCase):
    
  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x86")


  def test_gadget_sub_7254375B(self):
		#sub_7254375B
		gadget = "8BFF558BEC56578B7D20BE58575672A5A5A5A55F33C05E5DC21C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_18]
		#mov     esi, offset dword_72565758
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    1Ch


  def test_gadget_sub_72543F77(self):
		#sub_72543F77
		gadget = "8BFF558BEC8B45088B401C8B4D0C83C01C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 1Ch
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72543F95(self):
		#sub_72543F95
		gadget = "8BFF558BEC8B4510C7000100000033C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#mov     dword ptr [eax], 1
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72544068(self):
		#sub_72544068
		gadget = "8BFF558BEC8B45088B40188B4D0C83C02C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+18h]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 2Ch
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72544086(self):
		#sub_72544086
		gadget = "8BFF558BEC8B4508FF4010FF401433C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+10h]
		#inc     dword ptr [eax+14h]
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7254499E(self):
		#sub_7254499E
		gadget = "8B4104C3"
		self.do(gadget)

		#mov     eax, [ecx+4]
		#retn


  def test_gadget_sub_72544C14(self):
		#sub_72544C14
		gadget = "8BFF558BEC578B7D086A065933C0F3AB5F5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    edi
		#mov     edi, [ebp+arg_0]
		#push    6
		#pop     ecx
		#xor     eax, eax
		#rep stosd
		#pop     edi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72545E41(self):
		#sub_72545E41
		gadget = "64A1180000008B40308B80D801000083E020C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+30h]
		#mov     eax, [eax+1D8h]
		#and     eax, 20h
		#retn


  def test_gadget_sub_72546541(self):
		#sub_72546541
		gadget = "64A1180000008B40308B80D801000083E040C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+30h]
		#mov     eax, [eax+1D8h]
		#and     eax, 40h
		#retn


  def test_gadget_sub_72546F51(self):
		#sub_72546F51
		gadget = "8BFF56578BC1834804FF83600800C70074695472C7400C010000008D7810BEA49A5872A5A5A5A55F5EC3"
		self.do(gadget)

		#mov     edi, edi
		#push    esi
		#push    edi
		#mov     eax, ecx
		#or      dword ptr [eax+4], 0FFFFFFFFh
		#and     dword ptr [eax+8], 0
		#mov     dword ptr [eax], offset off_72546974
		#mov     dword ptr [eax+0Ch], 1
		#lea     edi, [eax+10h]
		#mov     esi, offset stru_72589AA4
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#retn


  def test_gadget_sub_725473C1(self):
		#sub_725473C1
		gadget = "8BFF558BEC8BC18B4D08568B751C89088B4D0C578D7814A5A5A5A58360280083602C008948048B4D108948088B4D148948108B4D1889480C8B4D208948248B4D248948308B4D285F8948345E5DC22400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#push    esi
		#mov     esi, [ebp+arg_14]
		#mov     [eax], ecx
		#mov     ecx, [ebp+arg_4]
		#push    edi
		#lea     edi, [eax+14h]
		#movsd
		#movsd
		#movsd
		#movsd
		#and     dword ptr [eax+28h], 0
		#and     dword ptr [eax+2Ch], 0
		#mov     [eax+4], ecx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_C]
		#mov     [eax+10h], ecx
		#mov     ecx, [ebp+arg_10]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [ebp+arg_18]
		#mov     [eax+24h], ecx
		#mov     ecx, [ebp+arg_1C]
		#mov     [eax+30h], ecx
		#mov     ecx, [ebp+arg_20]
		#pop     edi
		#mov     [eax+34h], ecx
		#pop     esi
		#pop     ebp
		#retn    24h


  def test_gadget_sub_725475B6(self):
		#sub_725475B6
		gadget = "8BFF558BEC8BC18B4D088360080083601000C70024545872C74004AC655872C7400C010000008948145DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+8], 0
		#and     dword ptr [eax+10h], 0
		#mov     dword ptr [eax], offset off_72585424
		#mov     dword ptr [eax+4], offset off_725865AC
		#mov     dword ptr [eax+0Ch], 1
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_nullsub_1(self):
		#nullsub_1
		gadget = "CA0100"
		self.do(gadget)

		#retf    1


  def test_gadget_sub_7254A371(self):
		#sub_7254A371
		gadget = "8BFF558BEC8B45088B5004568B3089328956048B5104890289500489088941045E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [eax+4]
		#push    esi
		#mov     esi, [eax]
		#mov     [edx], esi
		#mov     [esi+4], edx
		#mov     edx, [ecx+4]
		#mov     [edx], eax
		#mov     [eax+4], edx
		#mov     [eax], ecx
		#mov     [ecx+4], eax
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_7254A3BF(self):
		#sub_7254A3BF
		gadget = "8BFF558BEC568B75088BC18360080083600C008B4D0C5789400489008D7810A5A5A5A58B095F8948205E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#mov     eax, ecx
		#and     dword ptr [eax+8], 0
		#and     dword ptr [eax+0Ch], 0
		#mov     ecx, [ebp+arg_4]
		#push    edi
		#mov     [eax+4], eax
		#mov     [eax], eax
		#lea     edi, [eax+10h]
		#movsd
		#movsd
		#movsd
		#movsd
		#mov     ecx, [ecx]
		#pop     edi
		#mov     [eax+20h], ecx
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7254AE17(self):
		#sub_7254AE17
		gadget = "8BFF558BEC8B45088B4D0C8948185DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+18h], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7254C328(self):
		#sub_7254C328
		gadget = "855DFB833923D211B89D00C04FB9618A9090909090"
		self.do(gadget)

		#test    [ebp-5], ebx
		#cmp     dword ptr [ecx], 23h
		#rcl     byte ptr [ecx], cl
		#mov     eax, 4FC0009Dh
		#mov     ecx, 90908A61h
		#nop
		#nop
		#nop


  def test_gadget_sub_7254C684(self):
		#sub_7254C684
		gadget = "8BFF558BEC8B45088B4D0C89481033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+10h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7254C748(self):
		#sub_7254C748
		gadget = "8BFF558BEC8B450889413C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+3Ch], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7254ED66(self):
		#sub_7254ED66
		gadget = "8BFF558BEC568B750C578B7D0883C714A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_4]
		#push    edi
		#mov     edi, [ebp+arg_0]
		#add     edi, 14h
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7254EF9F(self):
		#sub_7254EF9F
		gadget = "8BC133C9C70054E6577289480489480889480C894810894814C7401801000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7257E654
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 1
		#retn


  def test_gadget_sub_7254FDC6(self):
		#sub_7254FDC6
		gadget = "8BFF558BEC8B45088B4D0C89482033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+20h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72550A70(self):
		#sub_72550A70
		gadget = "8BFF558BEC8BC18B4D088D5110C700E80855728948048950088948185DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#lea     edx, [ecx+10h]
		#mov     dword ptr [eax], offset off_725508E8
		#mov     [eax+4], ecx
		#mov     [eax+8], edx
		#mov     [eax+18h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7255215D(self):
		#sub_7255215D
		gadget = "8BFF558BEC8B550C8BC133C983482CFF89480C8950208B55148948288948348948388948408B4D108950248B55188948108B4D08894004894008C700D4BA557289401889401C8950308948145DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_4]
		#mov     eax, ecx
		#xor     ecx, ecx
		#or      dword ptr [eax+2Ch], 0FFFFFFFFh
		#mov     [eax+0Ch], ecx
		#mov     [eax+20h], edx
		#mov     edx, [ebp+arg_C]
		#mov     [eax+28h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+40h], ecx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+24h], edx
		#mov     edx, [ebp+arg_10]
		#mov     [eax+10h], ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+4], eax
		#mov     [eax+8], eax
		#mov     dword ptr [eax], offset off_7255BAD4
		#mov     [eax+18h], eax
		#mov     [eax+1Ch], eax
		#mov     [eax+30h], edx
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    14h


  def test_gadget_sub_72552C1E(self):
		#sub_72552C1E
		gadget = "8BC1565733C9C700602E5572C74004802E5572C7400874325572C7400C0100000089482889482C8948308948108948148D7818BEA49A5872A5A5A5A55F5EC3"
		self.do(gadget)

		#mov     eax, ecx
		#push    esi
		#push    edi
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_72552E60
		#mov     dword ptr [eax+4], offset off_72552E80
		#mov     dword ptr [eax+8], offset off_72553274
		#mov     dword ptr [eax+0Ch], 1
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#lea     edi, [eax+18h]
		#mov     esi, offset stru_72589AA4
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#retn


  def test_gadget_sub_725532AD(self):
		#sub_725532AD
		gadget = "C701100D5872C7410498325572C3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_72580D10
		#mov     dword ptr [ecx+4], offset off_72553298
		#retn


  def test_gadget_sub_725532EB(self):
		#sub_725532EB
		gadget = "8BFF558BEC8BC18B4D08C700043355728948045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_72553304
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_72554241(self):
		#sub_72554241
		gadget = "8B410883C01033D256428950048B71108360080083EE1089302B41088B710889068B41088950088B4108836004008B4108C7400C0400000033C05EC3"
		self.do(gadget)

		#mov     eax, [ecx+8]
		#add     eax, 10h
		#xor     edx, edx
		#push    esi
		#inc     edx
		#mov     [eax+4], edx
		#mov     esi, [ecx+10h]
		#and     dword ptr [eax+8], 0
		#sub     esi, 10h
		#mov     [eax], esi
		#sub     eax, [ecx+8]
		#mov     esi, [ecx+8]
		#mov     [esi], eax
		#mov     eax, [ecx+8]
		#mov     [eax+8], edx
		#mov     eax, [ecx+8]
		#and     dword ptr [eax+4], 0
		#mov     eax, [ecx+8]
		#mov     dword ptr [eax+0Ch], 4
		#xor     eax, eax
		#pop     esi
		#retn


  def test_gadget_sub_72554C50(self):
		#sub_72554C50
		gadget = "8BFF558BEC8B41048B550889028B41088B550C89028B41148B4D1089015DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ecx+4]
		#mov     edx, [ebp+arg_0]
		#mov     [edx], eax
		#mov     eax, [ecx+8]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], eax
		#mov     eax, [ecx+14h]
		#mov     ecx, [ebp+arg_8]
		#mov     [ecx], eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72554EA6(self):
		#sub_72554EA6
		gadget = "8BFF558BEC8B55088BC133C9894814834820FF834824FFC70004265872C740043C485572C7400890485572C7400C7C485572895030C7402C01000000894818C74028464C535489483489483889483C89481C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+14h], ecx
		#or      dword ptr [eax+20h], 0FFFFFFFFh
		#or      dword ptr [eax+24h], 0FFFFFFFFh
		#mov     dword ptr [eax], offset off_72582604
		#mov     dword ptr [eax+4], offset off_7255483C
		#mov     dword ptr [eax+8], offset off_72554890
		#mov     dword ptr [eax+0Ch], offset off_7255487C
		#mov     [eax+30h], edx
		#mov     dword ptr [eax+2Ch], 1
		#mov     [eax+18h], ecx
		#mov     dword ptr [eax+28h], 54534C46h
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+1Ch], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_72555481(self):
		#sub_72555481
		gadget = "8BFF558BEC8B4508FF40188B40185DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+18h]
		#mov     eax, [eax+18h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_725555BA(self):
		#sub_725555BA
		gadget = "64A1180000008B40308B80D80100002500000100C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+30h]
		#mov     eax, [eax+1D8h]
		#and     eax, 10000h
		#retn


  def test_gadget_sub_725558E8(self):
		#sub_725558E8
		gadget = "8BFF558BEC568B7508576A0233C059BF10595572F3A70F94C05F5E4825FB0003805DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#push    edi
		#push    2
		#xor     eax, eax
		#pop     ecx
		#mov     edi, offset dword_72555910
		#repe cmpsd
		#setz    al
		#pop     edi
		#pop     esi
		#dec     eax
		#and     eax, 800300FBh
		#pop     ebp
		#retn    4


  def test_gadget_sub_72556E05(self):
		#sub_72556E05
		gadget = "8BC1C70070E35572C74004986D5572C7400801000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_7255E370
		#mov     dword ptr [eax+4], offset off_72556D98
		#mov     dword ptr [eax+8], 1
		#retn


  def test_gadget_sub_725570D7(self):
		#sub_725570D7
		gadget = "8B818C000000C3"
		self.do(gadget)

		#mov     eax, [ecx+8Ch]
		#retn


  def test_gadget_sub_7255712D(self):
		#sub_7255712D
		gadget = "8BFF558BEC8BC18B4D0889480C33C9C70088A35572C7401001000000894814C74018FEFFFFFF89481C89482089482489482889482C8948308948348948385DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+0Ch], ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7255A388
		#mov     dword ptr [eax+10h], 1
		#mov     [eax+14h], ecx
		#mov     dword ptr [eax+18h], 0FFFFFFFEh
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+38h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_72557174(self):
		#sub_72557174
		gadget = "8BFF558BEC8B45088941208D5070568B328D413489513889308BCE89410489025E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+20h], eax
		#lea     edx, [eax+70h]
		#push    esi
		#mov     esi, [edx]
		#lea     eax, [ecx+34h]
		#mov     [ecx+38h], edx
		#mov     [eax], esi
		#mov     ecx, esi
		#mov     [ecx+4], eax
		#mov     [edx], eax
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72557352(self):
		#sub_72557352
		gadget = "8BFF558BEC8B450889411C8D5068568B328D412C89513089308BCE89410489025E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+1Ch], eax
		#lea     edx, [eax+68h]
		#push    esi
		#mov     esi, [edx]
		#lea     eax, [ecx+2Ch]
		#mov     [ecx+30h], edx
		#mov     [eax], esi
		#mov     ecx, esi
		#mov     [ecx+4], eax
		#mov     [edx], eax
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72558C11(self):
		#sub_72558C11
		gadget = "8BFF558BEC568B750857BF78636872A5A5A5A58B75088D7904A5A5A5A55F5E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#push    edi
		#mov     edi, offset rguid
		#movsd
		#movsd
		#movsd
		#movsd
		#mov     esi, [ebp+arg_0]
		#lea     edi, [ecx+4]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72558E52(self):
		#sub_72558E52
		gadget = "8BFF558BEC8B450C83200033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72558EB6(self):
		#sub_72558EB6
		gadget = "8BFF558BEC8B45088B48288B550C890A8B4028F7D81BC025FBBFFF7F05054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+28h]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+28h]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 7FFFBFFBh
		#add     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_72558EE0(self):
		#sub_72558EE0
		gadget = "8BFF558BEC8B45088B4D0C83C01089018B4510C7001000000033C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 10h
		#mov     [ecx], eax
		#mov     eax, [ebp+arg_8]
		#mov     dword ptr [eax], 10h
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72558F04(self):
		#sub_72558F04
		gadget = "8BFF558BEC8B45088B40488B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+48h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72558F1F(self):
		#sub_72558F1F
		gadget = "8BFF558BEC8B450C8B0D14896872890833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     ecx, dword_72688914
		#mov     [eax], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72558F3A(self):
		#sub_72558F3A
		gadget = "8BFF558BEC8B450CC7000800000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword ptr [eax], 8
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72558F62(self):
		#sub_72558F62
		gadget = "8BC183485CFF33C9C70090535872C74004CC655872C74008BC65587289480C89482089482889482C89483489483C89484089485489485889486889487489486C894870894878894860894864C3"
		self.do(gadget)

		#mov     eax, ecx
		#or      dword ptr [eax+5Ch], 0FFFFFFFFh
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_72585390
		#mov     dword ptr [eax+4], offset off_725865CC
		#mov     dword ptr [eax+8], offset off_725865BC
		#mov     [eax+0Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+68h], ecx
		#mov     [eax+74h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+70h], ecx
		#mov     [eax+78h], ecx
		#mov     [eax+60h], ecx
		#mov     [eax+64h], ecx
		#retn


  def test_gadget_sub_725590A5(self):
		#sub_725590A5
		gadget = "B801400080C20800"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    8


  def test_gadget_sub_7255B4F8(self):
		#sub_7255B4F8
		gadget = "8BFF558BEC8B4D0C8B550833C03B51080F94C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_4]
		#mov     edx, [ebp+arg_0]
		#xor     eax, eax
		#cmp     edx, [ecx+8]
		#setz    al
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7255C21E(self):
		#sub_7255C21E
		gadget = "8BFF558BEC56578B7D0CBE28255772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_72572528
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7255C7CD(self):
		#sub_7255C7CD
		gadget = "8BFF558BEC8B45088B40048B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7255C8E1(self):
		#sub_7255C8E1
		gadget = "8BFF558BEC8B45088B40108B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+10h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7255D1C1(self):
		#sub_7255D1C1
		gadget = "8B81CC00000083E002C3"
		self.do(gadget)

		#mov     eax, [ecx+0CCh]
		#and     eax, 2
		#retn


  def test_gadget_sub_72560055(self):
		#sub_72560055
		gadget = "8BC156B9FFFF00008BD16A075E6689500433D26689701089500889501C89500C895014668948185EC3"
		self.do(gadget)

		#mov     eax, ecx
		#push    esi
		#mov     ecx, 0FFFFh
		#mov     edx, ecx
		#push    7
		#pop     esi
		#mov     [eax+4], dx
		#xor     edx, edx
		#mov     [eax+10h], si
		#mov     [eax+8], edx
		#mov     [eax+1Ch], edx
		#mov     [eax+0Ch], edx
		#mov     [eax+14h], edx
		#mov     [eax+18h], cx
		#pop     esi
		#retn


  def test_gadget_sub_72560DFF(self):
		#sub_72560DFF
		gadget = "0FB748040FB7D1568B3083C10266893C326689480433C05EC3"
		self.do(gadget)

		#movzx   ecx, word ptr [eax+4]
		#movzx   edx, cx
		#push    esi
		#mov     esi, [eax]
		#add     ecx, 2
		#mov     [edx+esi], di
		#mov     [eax+4], cx
		#xor     eax, eax
		#pop     esi
		#retn


  def test_gadget_sub_72561C2E(self):
		#sub_72561C2E
		gadget = "8BFF558BEC8B4D088BC1C1E80A33C1C1E109C1E80533C18B4D0C8BD1C1EA0A33D1C1EA05C1E10933D103C25DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     eax, ecx
		#shr     eax, 0Ah
		#xor     eax, ecx
		#shl     ecx, 9
		#shr     eax, 5
		#xor     eax, ecx
		#mov     ecx, [ebp+arg_4]
		#mov     edx, ecx
		#shr     edx, 0Ah
		#xor     edx, ecx
		#shr     edx, 5
		#shl     ecx, 9
		#xor     edx, ecx
		#add     eax, edx
		#pop     ebp
		#retn    8


  def test_gadget_sub_72561C69(self):
		#sub_72561C69
		gadget = "8BC183601800C3"
		self.do(gadget)

		#mov     eax, ecx
		#and     dword ptr [eax+18h], 0
		#retn


  def test_gadget_sub_72562722(self):
		#sub_72562722
		gadget = "8B81CC0000002500000800C3"
		self.do(gadget)

		#mov     eax, [ecx+0CCh]
		#and     eax, 80000h
		#retn


  def test_gadget_sub_72562733(self):
		#sub_72562733
		gadget = "8B81CC000000C1E814F7D083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+0CCh]
		#shr     eax, 14h
		#not     eax
		#and     eax, 1
		#retn


  def test_gadget_sub_725627A7(self):
		#sub_725627A7
		gadget = "8BC1648B0D1800000083480CFF33D2895004895008895018C7401CE0030000C74020E80300008B89800F0000568B717089416889308951705EC3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     ecx, large fs:18h
		#or      dword ptr [eax+0Ch], 0FFFFFFFFh
		#xor     edx, edx
		#mov     [eax+4], edx
		#mov     [eax+8], edx
		#mov     [eax+18h], edx
		#mov     dword ptr [eax+1Ch], 3E0h
		#mov     dword ptr [eax+20h], 3E8h
		#mov     ecx, [ecx+0F80h]
		#push    esi
		#mov     esi, [ecx+70h]
		#mov     [ecx+68h], eax
		#mov     [eax], esi
		#mov     [ecx+70h], edx
		#pop     esi
		#retn


  def test_gadget_sub_725627E6(self):
		#sub_725627E6
		gadget = "8BFF558BEC8B450889410C8B450C8941108B45108941145DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+0Ch], eax
		#mov     eax, [ebp+arg_4]
		#mov     [ecx+10h], eax
		#mov     eax, [ebp+arg_8]
		#mov     [ecx+14h], eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72562AC4(self):
		#sub_72562AC4
		gadget = "8BFF558BEC8B45088B401425000100005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+14h]
		#and     eax, 100h
		#pop     ebp
		#retn    4


  def test_gadget_sub_725635EC(self):
		#sub_725635EC
		gadget = "8BC133C9C700A00E587289481089481489480C894808894818C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_72580EA0
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+8], ecx
		#mov     [eax+18h], ecx
		#retn


  def test_gadget_nullsub_15(self):
		#nullsub_15
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_sub_725677D5(self):
		#sub_725677D5
		gadget = "8BFF558BEC8BC18B4D088320008948045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax], 0
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_72568164(self):
		#sub_72568164
		gadget = "8BFF558BEC8B4508A344896872C70508896872010000005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     dword_72688944, eax
		#mov     dword_72688908, 1
		#pop     ebp
		#retn    4


  def test_gadget_sub_72568740(self):
		#sub_72568740
		gadget = "8BFF558BEC8B45088B4D0C89888C00000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+8Ch], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72568B14(self):
		#sub_72568B14
		gadget = "83A1AC01000000565733C0408941288D7910BEFC105872A5A5A5A55F89819C0000005EC3"
		self.do(gadget)

		#and     dword ptr [ecx+1ACh], 0
		#push    esi
		#push    edi
		#xor     eax, eax
		#inc     eax
		#mov     [ecx+28h], eax
		#lea     edi, [ecx+10h]
		#mov     esi, offset dword_725810FC
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#mov     [ecx+9Ch], eax
		#pop     esi
		#retn


  def test_gadget_sub_725691C6(self):
		#sub_725691C6
		gadget = "8BFF558BEC8B45088D51448950088B51488950048B514889420889414889480C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#lea     edx, [ecx+44h]
		#mov     [eax+8], edx
		#mov     edx, [ecx+48h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+48h]
		#mov     [edx+8], eax
		#mov     [ecx+48h], eax
		#mov     [eax+0Ch], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725691EF(self):
		#sub_725691EF
		gadget = "8BC133C989400489400889480C894810C7001092567289481889481C894820C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], eax
		#mov     [eax+8], eax
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     dword ptr [eax], offset off_72569210
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn


  def test_gadget_sub_7256928C(self):
		#sub_7256928C
		gadget = "8BFF558BEC8B45088B4D0C83C018890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 18h
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_725692B9(self):
		#sub_725692B9
		gadget = "8BC18388AC000000FF33C9C70020A15872C74004AC905772C74008FC905772C7400CD4905772C7401074A258728948148948188988A80000008988A00000008988A40000008988B80000008988BC0000008988C00000008988C40000008988C80000008988CC0000008988D00000008988D40000008988DC0000008988E00000008988E80000008988E40000008988D8000000C7403C010000008948408988EC0000008988F0000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#or      dword ptr [eax+0ACh], 0FFFFFFFFh
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7258A120
		#mov     dword ptr [eax+4], offset off_725790AC
		#mov     dword ptr [eax+8], offset off_725790FC
		#mov     dword ptr [eax+0Ch], offset off_725790D4
		#mov     dword ptr [eax+10h], offset off_7258A274
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+0A8h], ecx
		#mov     [eax+0A0h], ecx
		#mov     [eax+0A4h], ecx
		#mov     [eax+0B8h], ecx
		#mov     [eax+0BCh], ecx
		#mov     [eax+0C0h], ecx
		#mov     [eax+0C4h], ecx
		#mov     [eax+0C8h], ecx
		#mov     [eax+0CCh], ecx
		#mov     [eax+0D0h], ecx
		#mov     [eax+0D4h], ecx
		#mov     [eax+0DCh], ecx
		#mov     [eax+0E0h], ecx
		#mov     [eax+0E8h], ecx
		#mov     [eax+0E4h], ecx
		#mov     [eax+0D8h], ecx
		#mov     dword ptr [eax+3Ch], 1
		#mov     [eax+40h], ecx
		#mov     [eax+0ECh], ecx
		#mov     [eax+0F0h], ecx
		#retn


  def test_gadget_sub_72569947(self):
		#sub_72569947
		gadget = "8BD133C9C702A0995672A1009268728942048D424457890889424889424C8D420C89008942106A08894A08894A3C894A40894A50894A54894A588D7A1C5933C0897A18C7020C915772C7421402000000F3AB8BC25FC3"
		self.do(gadget)

		#mov     edx, ecx
		#xor     ecx, ecx
		#mov     dword ptr [edx], offset off_725699A0
		#mov     eax, dword_72689200
		#mov     [edx+4], eax
		#lea     eax, [edx+44h]
		#push    edi
		#mov     [eax], ecx
		#mov     [edx+48h], eax
		#mov     [edx+4Ch], eax
		#lea     eax, [edx+0Ch]
		#mov     [eax], eax
		#mov     [edx+10h], eax
		#push    8
		#mov     [edx+8], ecx
		#mov     [edx+3Ch], ecx
		#mov     [edx+40h], ecx
		#mov     [edx+50h], ecx
		#mov     [edx+54h], ecx
		#mov     [edx+58h], ecx
		#lea     edi, [edx+1Ch]
		#pop     ecx
		#xor     eax, eax
		#mov     [edx+18h], edi
		#mov     dword ptr [edx], offset off_7257910C
		#mov     dword ptr [edx+14h], 2
		#rep stosd
		#mov     eax, edx
		#pop     edi
		#retn


  def test_gadget_sub_72569EF0(self):
		#sub_72569EF0
		gadget = "8BFF558BEC8B45088B80A80000008B4D100D3240000023450C890133C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0A8h]
		#mov     ecx, [ebp+arg_8]
		#or      eax, 4032h
		#and     eax, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72569F16(self):
		#sub_72569F16
		gadget = "8BFF558BEC8B45088B40188B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+18h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7256A15A(self):
		#sub_7256A15A
		gadget = "8BFF558BEC8B45088B401C8B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7256BAC8(self):
		#sub_7256BAC8
		gadget = "8BFF558BEC8B45088B005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax]
		#pop     ebp
		#retn    4


  def test_gadget_sub_7256BADB(self):
		#sub_7256BADB
		gadget = "8BFF558BEC8B4D088B118B451089108B49048948048B4D0C8B118950088B490489480C5DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     edx, [ecx]
		#mov     eax, [ebp+arg_8]
		#mov     [eax], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     edx, [ecx]
		#mov     [eax+8], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+0Ch], ecx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7256BB07(self):
		#sub_7256BB07
		gadget = "8BFF558BEC8B45088B0D406D6872894848C7404CF86C687289414CA3406D68725DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, dword_72686D40
		#mov     [eax+48h], ecx
		#mov     dword ptr [eax+4Ch], offset unk_72686CF8
		#mov     [ecx+4Ch], eax
		#mov     dword_72686D40, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7256BB30(self):
		#sub_7256BB30
		gadget = "8BC133D28D486CC7008091577289500489501489505C8909894870895074895078C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     edx, edx
		#lea     ecx, [eax+6Ch]
		#mov     dword ptr [eax], offset off_72579180
		#mov     [eax+4], edx
		#mov     [eax+14h], edx
		#mov     [eax+5Ch], edx
		#mov     [ecx], ecx
		#mov     [eax+70h], ecx
		#mov     [eax+74h], edx
		#mov     [eax+78h], edx
		#retn


  def test_gadget_sub_7256BB57(self):
		#sub_7256BB57
		gadget = "8BFF558BEC8BC18B4D088948048B4D0CC70074BB56728948085DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+4], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     dword ptr [eax], offset off_7256BB74
		#mov     [eax+8], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7256D79D(self):
		#sub_7256D79D
		gadget = "8BFF558BEC568B7508578D7928A5A5A5A55F5E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#push    edi
		#lea     edi, [ecx+28h]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_7256DCA7(self):
		#sub_7256DCA7
		gadget = "8BFF558BEC8B450883611C00C74118010000008B108951108B40048941145DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [ecx+1Ch], 0
		#mov     dword ptr [ecx+18h], 1
		#mov     edx, [eax]
		#mov     [ecx+10h], edx
		#mov     eax, [eax+4]
		#mov     [ecx+14h], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7256F48C(self):
		#sub_7256F48C
		gadget = "8BFF558BEC8BC18B4D08836010008948088B4D0CC700B4F4567289480CC74004010000005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+10h], 0
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     dword ptr [eax], offset off_7256F4B4
		#mov     [eax+0Ch], ecx
		#mov     dword ptr [eax+4], 1
		#pop     ebp
		#retn    8


  def test_gadget_sub_7256F837(self):
		#sub_7256F837
		gadget = "8BC1C74004F8F1577233C9C70008815972C74004F8F15772C74038206E5972834830FF894844894848894818894850894854C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax+4], offset off_7257F1F8
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_72598108
		#mov     dword ptr [eax+4], offset off_7257F1F8
		#mov     dword ptr [eax+38h], offset off_72596E20
		#or      dword ptr [eax+30h], 0FFFFFFFFh
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#retn


  def test_gadget_sub_7256F90C(self):
		#sub_7256F90C
		gadget = "606BF5D53B591A10B56908002B2DBF7A9090909090"
		self.do(gadget)

		#pusha
		#imul    esi, ebp, -2Bh
		#cmp     ebx, [ecx+1Ah]
		#adc     [ebp+2B000869h], dh
		#sub     eax, 90907ABFh
		#nop
		#nop
		#nop


  def test_gadget_sub_72570860(self):
		#sub_72570860
		gadget = "8BC133C989481489481889480C89481089482889482C890889480489480889481CC7402001000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+1Ch], ecx
		#mov     dword ptr [eax+20h], 1
		#retn


  def test_gadget_sub_72570EF5(self):
		#sub_72570EF5
		gadget = "8BFF558BEC56578B7D0CBEFC105872A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_725810FC
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72571923(self):
		#sub_72571923
		gadget = "8BFF558BEC8B45088360180033C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [eax+18h], 0
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_72571F4A(self):
		#sub_72571F4A
		gadget = "8BFF558BEC8BC18B4D105657C700E43D5872C74018010000008D7824BEA49A5872A5A5A5A533D281C9003000008948148B4D0C8948348B4D0889481C8D48485F89504089504489503889503C895054895020890989484C8950505E5DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_8]
		#push    esi
		#push    edi
		#mov     dword ptr [eax], offset off_72583DE4
		#mov     dword ptr [eax+18h], 1
		#lea     edi, [eax+24h]
		#mov     esi, offset stru_72589AA4
		#movsd
		#movsd
		#movsd
		#movsd
		#xor     edx, edx
		#or      ecx, 3000h
		#mov     [eax+14h], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+34h], ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+1Ch], ecx
		#lea     ecx, [eax+48h]
		#pop     edi
		#mov     [eax+40h], edx
		#mov     [eax+44h], edx
		#mov     [eax+38h], edx
		#mov     [eax+3Ch], edx
		#mov     [eax+54h], edx
		#mov     [eax+20h], edx
		#mov     [ecx], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], edx
		#pop     esi
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72573ECF(self):
		#sub_72573ECF
		gadget = "8BFF558BEC56578B7D0CBE543F5772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_72573F54
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72574354(self):
		#sub_72574354
		gadget = "8BFF558BEC56578B7D0CBE08255772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_72572508
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72574374(self):
		#sub_72574374
		gadget = "8BFF558BEC56578B7D0CBEC8245772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_725724C8
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_725747EE(self):
		#sub_725747EE
		gadget = "8BFF558BEC56578B7D0CBEB8245772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_725724B8
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7257480E(self):
		#sub_7257480E
		gadget = "8BFF558BEC56578B7D20BE7C055772A5A5A5A55F33C05E5DC21C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_18]
		#mov     esi, offset dword_7257057C
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    1Ch


  def test_gadget_sub_725749FF(self):
		#sub_725749FF
		gadget = "8BFF558BEC8B45088B4D0C8348440289482833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#or      dword ptr [eax+44h], 2
		#mov     [eax+28h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72574B1D(self):
		#sub_72574B1D
		gadget = "8BFF558BEC56578B7D0CBED8245772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_725724D8
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72574B77(self):
		#sub_72574B77
		gadget = "8BFF558BEC56578B7D0CBEF8245772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_725724F8
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72574BAF(self):
		#sub_72574BAF
		gadget = "8BFF558BEC56578B7D0CBE58255772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_72572558
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72575B43(self):
		#sub_72575B43
		gadget = "8BC133C98D5018C7000100000089480489480889480C8948108948145633F6668972186689721A895230895234894A385EC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#lea     edx, [eax+18h]
		#mov     dword ptr [eax], 1
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#push    esi
		#xor     esi, esi
		#mov     [edx+18h], si
		#mov     [edx+1Ah], si
		#mov     [edx+30h], edx
		#mov     [edx+34h], edx
		#mov     [edx+38h], ecx
		#pop     esi
		#retn


  def test_gadget_sub_725760E5(self):
		#sub_725760E5
		gadget = "8BFF558BEC668B550833C0890189410489411C894114894110668951088D41280FB7D28941208D44900383E0FC8941245DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     dx, [ebp+arg_0]
		#xor     eax, eax
		#mov     [ecx], eax
		#mov     [ecx+4], eax
		#mov     [ecx+1Ch], eax
		#mov     [ecx+14h], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+8], dx
		#lea     eax, [ecx+28h]
		#movzx   edx, dx
		#mov     [ecx+20h], eax
		#lea     eax, [eax+edx*4+3]
		#and     eax, 0FFFFFFFCh
		#mov     [ecx+24h], eax
		#pop     ebp
		#retn    4


  def test_gadget_nullsub_2(self):
		#nullsub_2
		gadget = "CB"
		self.do(gadget)

		#retf


  def test_gadget_sub_72579312(self):
		#sub_72579312
		gadget = "8B01C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#retn


  def test_gadget___SEH_prolog4_GS(self):
		#__SEH_prolog4_GS
		gadget = "68F9665A7264FF35000000008B442410896C24108D6C24102BE0535657A12C6668723145FC33C58945E4508965E8FF75F88B45FCC745FCFEFFFFFF8945F88D45F064A300000000C3"
		self.do(gadget)

		#push    offset sub_725A66F9
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
		#mov     [ebp-1Ch], eax
		#push    eax
		#mov     [ebp-18h], esp
		#push    dword ptr [ebp-8]
		#mov     eax, [ebp-4]
		#mov     dword ptr [ebp-4], 0FFFFFFFEh
		#mov     [ebp-8], eax
		#lea     eax, [ebp-10h]
		#mov     large fs:0, eax
		#retn


  def test_gadget___SEH_epilog4_GS(self):
		#__SEH_epilog4_GS
		gadget = "8B4DE433CDE8DA510100E9B1510100"
		self.do(gadget)

		#mov     ecx, [ebp-1Ch]
		#xor     ecx, ebp
		#call    @__security_check_cookie@4; __security_check_cookie(x)
		#jmp     __SEH_epilog4


  def test_gadget_sub_725798D7(self):
		#sub_725798D7
		gadget = "8BFF558BEC8B45148320005DC21000"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_C]
		#and     dword ptr [eax], 0
		#pop     ebp
		#retn    10h


  def test_gadget_sub_72579ED8(self):
		#sub_72579ED8
		gadget = "8BFF558BEC8B45088B80DC0000005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0DCh]
		#pop     ebp
		#retn    4


  def test_gadget_sub_7257AB72(self):
		#sub_7257AB72
		gadget = "8BFF558BEC8B45088B401483E0025DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+14h]
		#and     eax, 2
		#pop     ebp
		#retn    4


  def test_gadget_sub_7257B489(self):
		#sub_7257B489
		gadget = "8BFF558BEC8B45088B48308B50348951348B48348B50308951308940308940345DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+30h]
		#mov     edx, [eax+34h]
		#mov     [ecx+34h], edx
		#mov     ecx, [eax+34h]
		#mov     edx, [eax+30h]
		#mov     [ecx+30h], edx
		#mov     [eax+30h], eax
		#mov     [eax+34h], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7257BA65(self):
		#sub_7257BA65
		gadget = "A13C7C687283E010C3"
		self.do(gadget)

		#mov     eax, dword_72687C3C
		#and     eax, 10h
		#retn


  def test_gadget_sub_7257BDAB(self):
		#sub_7257BDAB
		gadget = "33C040C3"
		self.do(gadget)

		#xor     eax, eax
		#inc     eax
		#retn


  def test_gadget_sub_7257C1E7(self):
		#sub_7257C1E7
		gadget = "8BC1C70074C15772C20400"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_7257C174
		#retn    4


  def test_gadget_sub_7257D768(self):
		#sub_7257D768
		gadget = "046840BFFA6AE7468A486C357E1D6D619090909090"
		self.do(gadget)

		#add     al, 68h
		#inc     eax
		#mov     edi, 46E76AFAh
		#mov     cl, [eax+6Ch]
		#xor     eax, 616D1D7Eh
		#nop
		#nop
		#nop
		#nop
		#nop


  def test_gadget_CoFreeAllLibraries(self):
		#CoFreeAllLibraries
		gadget = "8BC0C3"
		self.do(gadget)

		#mov     eax, eax
		#retn


  def test_gadget_sub_7257F028(self):
		#sub_7257F028
		gadget = "8BFF558BEC8D412C8B108B4D0889410489118B10894A04890833C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#lea     eax, [ecx+2Ch]
		#mov     edx, [eax]
		#mov     ecx, [ebp+arg_0]
		#mov     [ecx+4], eax
		#mov     [ecx], edx
		#mov     edx, [eax]
		#mov     [edx+4], ecx
		#mov     [eax], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7257F118(self):
		#sub_7257F118
		gadget = "8BFF558BEC8B55088BC133C98950088B550C89088948048950108948145DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+8], edx
		#mov     edx, [ebp+arg_4]
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+10h], edx
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7257F515(self):
		#sub_7257F515
		gadget = "8BFF558BEC8B450833C933D28948108908C64018018848196689501A89481C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#xor     ecx, ecx
		#xor     edx, edx
		#mov     [eax+10h], ecx
		#mov     [eax], ecx
		#mov     byte ptr [eax+18h], 1
		#mov     [eax+19h], cl
		#mov     [eax+1Ah], dx
		#mov     [eax+1Ch], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7257F62B(self):
		#sub_7257F62B
		gadget = "33C0C20C00"
		self.do(gadget)

		#xor     eax, eax
		#retn    0Ch


  def test_gadget_sub_7257FC8D(self):
		#sub_7257FC8D
		gadget = "8BFF558BEC8BC18A4D0833D2884806B9C0E9587289500889500C8948108948148850045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     cl, [ebp+arg_0]
		#xor     edx, edx
		#mov     [eax+6], cl
		#mov     ecx, offset byte_7258E9C0
		#mov     [eax+8], edx
		#mov     [eax+0Ch], edx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+4], dl
		#pop     ebp
		#retn    4


  def test_gadget_sub_725804ED(self):
		#sub_725804ED
		gadget = "8BC133C989482889482C894830C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#retn


  def test_gadget_sub_72580CA4(self):
		#sub_72580CA4
		gadget = "64A1180000008B40308B80D80100002580000000C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+30h]
		#mov     eax, [eax+1D8h]
		#and     eax, 80h
		#retn


  def test_gadget_sub_7258155C(self):
		#sub_7258155C
		gadget = "8BFF558BEC8B45088B551489411C668B450C6689412033C089018941188941048941088941108941148B451089510C8941245DC21000"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [ebp+arg_C]
		#mov     [ecx+1Ch], eax
		#mov     ax, [ebp+arg_4]
		#mov     [ecx+20h], ax
		#xor     eax, eax
		#mov     [ecx], eax
		#mov     [ecx+18h], eax
		#mov     [ecx+4], eax
		#mov     [ecx+8], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#mov     eax, [ebp+arg_8]
		#mov     [ecx+0Ch], edx
		#mov     [ecx+24h], eax
		#pop     ebp
		#retn    10h


  def test_gadget_sub_725815EB(self):
		#sub_725815EB
		gadget = "8BFF558BEC8B4D088B410C0341086A1703410433D2030159F7F18BC25DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     eax, [ecx+0Ch]
		#add     eax, [ecx+8]
		#push    17h
		#add     eax, [ecx+4]
		#xor     edx, edx
		#add     eax, [ecx]
		#pop     ecx
		#div     ecx
		#mov     eax, edx
		#pop     ebp
		#retn    4


  def test_gadget_sub_72581610(self):
		#sub_72581610
		gadget = "8BC133C989480C894814894818890889482489481089481C894828894820894804894808C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#retn


  def test_gadget_sub_72581B7F(self):
		#sub_72581B7F
		gadget = "8BFF558BEC8B450C8B550889410433C089410889510C8941108941145DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     edx, [ebp+arg_0]
		#mov     [ecx+4], eax
		#xor     eax, eax
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], edx
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#pop     ebp
		#retn    8


  def test_gadget_IsValidIid(self):
		#IsValidIid
		gadget = "33C040C20400"
		self.do(gadget)

		#xor     eax, eax        ; ComPs_NdrDllCanUnloadNow
		#inc     eax
		#retn    4


  def test_gadget_CoSetState(self):
		#CoSetState
		gadget = "33C0C20400"
		self.do(gadget)

		#xor     eax, eax
		#retn    4


  def test_gadget_sub_72582CD5(self):
		#sub_72582CD5
		gadget = "8BFF558BEC8B45088B4D0C89480433C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+4], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7258314E(self):
		#sub_7258314E
		gadget = "8BFF558BEC8B451083200033C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72583FD5(self):
		#sub_72583FD5
		gadget = "8BFF558BEC33D25733C089510CC7010C2A58728D7910ABABABAB8B45088981D00000008951248951088951208951048991D40000008BC15F5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#xor     edx, edx
		#push    edi
		#xor     eax, eax
		#mov     [ecx+0Ch], edx
		#mov     dword ptr [ecx], offset off_72582A0C
		#lea     edi, [ecx+10h]
		#stosd
		#stosd
		#stosd
		#stosd
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+0D0h], eax
		#mov     [ecx+24h], edx
		#mov     [ecx+8], edx
		#mov     [ecx+20h], edx
		#mov     [ecx+4], edx
		#mov     [ecx+0D4h], edx
		#mov     eax, ecx
		#pop     edi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72584121(self):
		#sub_72584121
		gadget = "33C05789410889410C894110C74104D4265872C701E4285872C74104C02858728D7914ABAB8BC15FC3"
		self.do(gadget)

		#xor     eax, eax
		#push    edi
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     dword ptr [ecx+4], offset off_725826D4
		#mov     dword ptr [ecx], offset off_725828E4
		#mov     dword ptr [ecx+4], offset off_725828C0
		#lea     edi, [ecx+14h]
		#stosd
		#stosd
		#mov     eax, ecx
		#pop     edi
		#retn


  def test_gadget_sub_72584199(self):
		#sub_72584199
		gadget = "8BFF57C74108D426587233D289510C89511089511433C0C70118285872C7410400285872C74108DC2758728D7918ABABAB33C08D7924ABABAB8951308BC15FC3"
		self.do(gadget)

		#mov     edi, edi
		#push    edi
		#mov     dword ptr [ecx+8], offset off_725826D4
		#xor     edx, edx
		#mov     [ecx+0Ch], edx
		#mov     [ecx+10h], edx
		#mov     [ecx+14h], edx
		#xor     eax, eax
		#mov     dword ptr [ecx], offset off_72582818
		#mov     dword ptr [ecx+4], offset off_72582800
		#mov     dword ptr [ecx+8], offset off_725827DC
		#lea     edi, [ecx+18h]
		#stosd
		#stosd
		#stosd
		#xor     eax, eax
		#lea     edi, [ecx+24h]
		#stosd
		#stosd
		#stosd
		#mov     [ecx+30h], edx
		#mov     eax, ecx
		#pop     edi
		#retn


  def test_gadget_sub_725841DE(self):
		#sub_725841DE
		gadget = "33C05789410889410C894110C74104D4265872C70198285872C74104742858728D7914ABAB8BC15FC3"
		self.do(gadget)

		#xor     eax, eax
		#push    edi
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     dword ptr [ecx+4], offset off_725826D4
		#mov     dword ptr [ecx], offset off_72582898
		#mov     dword ptr [ecx+4], offset off_72582874
		#lea     edi, [ecx+14h]
		#stosd
		#stosd
		#mov     eax, ecx
		#pop     edi
		#retn


  def test_gadget_sub_7258420C(self):
		#sub_7258420C
		gadget = "8BFF57C74104D426587233D289510889510C89511033C0C70130295872C741040C2958728D7914ABABABAB8951248BC15FC3"
		self.do(gadget)

		#mov     edi, edi
		#push    edi
		#mov     dword ptr [ecx+4], offset off_725826D4
		#xor     edx, edx
		#mov     [ecx+8], edx
		#mov     [ecx+0Ch], edx
		#mov     [ecx+10h], edx
		#xor     eax, eax
		#mov     dword ptr [ecx], offset off_72582930
		#mov     dword ptr [ecx+4], offset off_7258290C
		#lea     edi, [ecx+14h]
		#stosd
		#stosd
		#stosd
		#stosd
		#mov     [ecx+24h], edx
		#mov     eax, ecx
		#pop     edi
		#retn


  def test_gadget_sub_72584243(self):
		#sub_72584243
		gadget = "8BD15657C74204D426587233C089420889420C8942108942408942448D72188BFE6A06C702642A5872C74204402A5872C74214302A587259F3AB4089068942488D7A30BEA49A5872A5A5A5A55F8BC25EC3"
		self.do(gadget)

		#mov     edx, ecx
		#push    esi
		#push    edi
		#mov     dword ptr [edx+4], offset off_725826D4
		#xor     eax, eax
		#mov     [edx+8], eax
		#mov     [edx+0Ch], eax
		#mov     [edx+10h], eax
		#mov     [edx+40h], eax
		#mov     [edx+44h], eax
		#lea     esi, [edx+18h]
		#mov     edi, esi
		#push    6
		#mov     dword ptr [edx], offset off_72582A64
		#mov     dword ptr [edx+4], offset off_72582A40
		#mov     dword ptr [edx+14h], offset off_72582A30
		#pop     ecx
		#rep stosd
		#inc     eax
		#mov     [esi], eax
		#mov     [edx+48h], eax
		#lea     edi, [edx+30h]
		#mov     esi, offset stru_72589AA4
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#mov     eax, edx
		#pop     esi
		#retn


  def test_gadget_sub_72584336(self):
		#sub_72584336
		gadget = "C74104D42658725733D289510889510C89511033C0C701402C5872C741041C2C58728D7914ABABABAB8951248951288BC15FC3"
		self.do(gadget)

		#mov     dword ptr [ecx+4], offset off_725826D4
		#push    edi
		#xor     edx, edx
		#mov     [ecx+8], edx
		#mov     [ecx+0Ch], edx
		#mov     [ecx+10h], edx
		#xor     eax, eax
		#mov     dword ptr [ecx], offset off_72582C40
		#mov     dword ptr [ecx+4], offset off_72582C1C
		#lea     edi, [ecx+14h]
		#stosd
		#stosd
		#stosd
		#stosd
		#mov     [ecx+24h], edx
		#mov     [ecx+28h], edx
		#mov     eax, ecx
		#pop     edi
		#retn


  def test_gadget_sub_725845AD(self):
		#sub_725845AD
		gadget = "8BFF558BEC8B45088B40148B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+14h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7258481A(self):
		#sub_7258481A
		gadget = "8BFF558BEC8B45088B4D0C89484033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+40h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7258659E(self):
		#sub_7258659E
		gadget = "33C03B05786268721BC0F7D8C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     eax, dword_72686278
		#sbb     eax, eax
		#neg     eax
		#retn


  def test_gadget_sub_72586A8B(self):
		#sub_72586A8B
		gadget = "8BFF558BEC568B75088BC183600C0057C70040275872C740043C665872C74008906758728D7810A5A5A5A5836020005FC74024010000005E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#mov     eax, ecx
		#and     dword ptr [eax+0Ch], 0
		#push    edi
		#mov     dword ptr [eax], offset off_72582740
		#mov     dword ptr [eax+4], offset off_7258663C
		#mov     dword ptr [eax+8], offset off_72586790
		#lea     edi, [eax+10h]
		#movsd
		#movsd
		#movsd
		#movsd
		#and     dword ptr [eax+20h], 0
		#pop     edi
		#mov     dword ptr [eax+24h], 1
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725889F8(self):
		#sub_725889F8
		gadget = "8BFF558BEC8B45088B5004568B3089328B108B4004894204FF49105E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [eax+4]
		#push    esi
		#mov     esi, [eax]
		#mov     [edx], esi
		#mov     edx, [eax]
		#mov     eax, [eax+4]
		#mov     [edx+4], eax
		#dec     dword ptr [ecx+10h]
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72588A84(self):
		#sub_72588A84
		gadget = "33C03905B08968720F95C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     dword_726889B0, eax
		#setnz   al
		#retn


  def test_gadget_sub_7258AD1D(self):
		#sub_7258AD1D
		gadget = "8BFF558BEC8B45088B4D0C83C01C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 1Ch
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7258AFCE(self):
		#sub_7258AFCE
		gadget = "8BFF558BEC8B45088B40088B400C8B404024080FB6C0F7D81BC025054000805DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+8]
		#mov     eax, [eax+0Ch]
		#mov     eax, [eax+40h]
		#and     al, 8
		#movzx   eax, al
		#neg     eax
		#sbb     eax, eax
		#and     eax, 80004005h
		#pop     ebp
		#retn    4


  def test_gadget_sub_7258B1E2(self):
		#sub_7258B1E2
		gadget = "8BFF558BEC8BC18B4D08568B750C89088B4D10578D7804A5A5A5A58948148B4D148948188B4D1C89481C8B4D188948208B4D208948248B4D248948288B4D2889482C8B4D2C5F8948305E5DC22800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#push    esi
		#mov     esi, [ebp+arg_4]
		#mov     [eax], ecx
		#mov     ecx, [ebp+arg_8]
		#push    edi
		#lea     edi, [eax+4]
		#movsd
		#movsd
		#movsd
		#movsd
		#mov     [eax+14h], ecx
		#mov     ecx, [ebp+arg_C]
		#mov     [eax+18h], ecx
		#mov     ecx, [ebp+arg_14]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [ebp+arg_10]
		#mov     [eax+20h], ecx
		#mov     ecx, [ebp+arg_18]
		#mov     [eax+24h], ecx
		#mov     ecx, [ebp+arg_1C]
		#mov     [eax+28h], ecx
		#mov     ecx, [ebp+arg_20]
		#mov     [eax+2Ch], ecx
		#mov     ecx, [ebp+arg_24]
		#pop     edi
		#mov     [eax+30h], ecx
		#pop     esi
		#pop     ebp
		#retn    28h


  def test_gadget_sub_7258B9C1(self):
		#sub_7258B9C1
		gadget = "C70518896872FFFFFFFFC3"
		self.do(gadget)

		#mov     dword_72688918, 0FFFFFFFFh
		#retn


  def test_gadget___SEH_prolog4(self):
		#__SEH_prolog4
		gadget = "68F9665A7264FF35000000008B442410896C24108D6C24102BE0535657A12C6668723145FC33C5508965E8FF75F88B45FCC745FCFEFFFFFF8945F88D45F064A300000000C3"
		self.do(gadget)

		#push    offset sub_725A66F9
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


  def test_gadget_sub_72597EF4(self):
		#sub_72597EF4
		gadget = "8BFF558BEC8B450C8B008B4D0889410433C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     eax, [eax]
		#mov     ecx, [ebp+arg_0]
		#mov     [ecx+4], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72597F0F(self):
		#sub_72597F0F
		gadget = "8BFF558BEC8B45088B4D0C89480833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+8], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72597FC5(self):
		#sub_72597FC5
		gadget = "8BFF558BEC8BC18B4D08836024008948108B4D0C8948148B4D108948188B4D1489481C8B4D18C70030805972C7400420805972C7400810805972C7400C010000008948205DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+24h], 0
		#mov     [eax+10h], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+14h], ecx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+18h], ecx
		#mov     ecx, [ebp+arg_C]
		#mov     [eax+1Ch], ecx
		#mov     ecx, [ebp+arg_10]
		#mov     dword ptr [eax], offset off_72598030
		#mov     dword ptr [eax+4], offset off_72598020
		#mov     dword ptr [eax+8], offset off_72598010
		#mov     dword ptr [eax+0Ch], 1
		#mov     [eax+20h], ecx
		#pop     ebp
		#retn    14h


  def test_gadget_sub_72598084(self):
		#sub_72598084
		gadget = "33C089410489410889410C89411089411489411889411C89412489412889412C89413089413489413889413C89414089414489414889414CC3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [ecx+4], eax
		#mov     [ecx+8], eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#mov     [ecx+18h], eax
		#mov     [ecx+1Ch], eax
		#mov     [ecx+24h], eax
		#mov     [ecx+28h], eax
		#mov     [ecx+2Ch], eax
		#mov     [ecx+30h], eax
		#mov     [ecx+34h], eax
		#mov     [ecx+38h], eax
		#mov     [ecx+3Ch], eax
		#mov     [ecx+40h], eax
		#mov     [ecx+44h], eax
		#mov     [ecx+48h], eax
		#mov     [ecx+4Ch], eax
		#retn


  def test_gadget_sub_72598751(self):
		#sub_72598751
		gadget = "8BFF558BEC8B45088B48088B098B5510890A8B008B40F48B4D0C89015DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+8]
		#mov     ecx, [ecx]
		#mov     edx, [ebp+arg_8]
		#mov     [edx], ecx
		#mov     eax, [eax]
		#mov     eax, [eax-0Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72598781(self):
		#sub_72598781
		gadget = "8BFF558BEC8B45088B40085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+8]
		#pop     ebp
		#retn    4


  def test_gadget_sub_725994D7(self):
		#sub_725994D7
		gadget = "8BFF558BEC8BC18B4D088908648B0D180000008B89800F00008B516C89500489416C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax], ecx
		#mov     ecx, large fs:18h
		#mov     ecx, [ecx+0F80h]
		#mov     edx, [ecx+6Ch]
		#mov     [eax+4], edx
		#mov     [ecx+6Ch], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7259C168(self):
		#sub_7259C168
		gadget = "8BC133C9C70000545872C7400464665872C74008E8655872C7400C01000000894810894814894818C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_72585400
		#mov     dword ptr [eax+4], offset off_72586664
		#mov     dword ptr [eax+8], offset off_725865E8
		#mov     dword ptr [eax+0Ch], 1
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#retn


  def test_gadget_sub_7259C206(self):
		#sub_7259C206
		gadget = "8BFF558BEC8B450CC7000500070033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword ptr [eax], 70005h
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7259C7B1(self):
		#sub_7259C7B1
		gadget = "8BFF558BEC8B55088BC133C9C700B8CE5972C7400434D9597289482C89480889480C8948108950308948345DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7259CEB8
		#mov     dword ptr [eax+4], offset off_7259D934
		#mov     [eax+2Ch], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+30h], edx
		#mov     [eax+34h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7259C82D(self):
		#sub_7259C82D
		gadget = "8BC133C9C700A8EC587289480489480889480C89481089481489481889481C894820894828894824C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7258ECA8
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+24h], ecx
		#retn


  def test_gadget_sub_7259EC87(self):
		#sub_7259EC87
		gadget = "B890EC5972C3"
		self.do(gadget)

		#mov     eax, offset a4c8cc1556c1e11; "{4c8cc155-6c1e-11d1-8e41-00c04fb9386d}"
		#retn


  def test_gadget_sub_7259FD34(self):
		#sub_7259FD34
		gadget = "2575009090909090"
		self.do(gadget)

		#and     eax, 90900075h
		#nop
		#nop
		#nop


  def test_gadget_sub_725A137D(self):
		#sub_725A137D
		gadget = "8BFF558BEC568B75088BC15733C941894804894808C700A8135A728D780CA5A5A5A55F5E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#mov     eax, ecx
		#push    edi
		#xor     ecx, ecx
		#inc     ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     dword ptr [eax], offset off_725A13A8
		#lea     edi, [eax+0Ch]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725A24E7(self):
		#sub_725A24E7
		gadget = "8BFF558BEC8B4D0833C039410C0F94C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#xor     eax, eax
		#cmp     [ecx+0Ch], eax
		#setz    al
		#pop     ebp
		#retn    4


  def test_gadget_sub_725A2670(self):
		#sub_725A2670
		gadget = "8BFF558BEC8BC133C989480C894810894814894818668B4D0C6689481C8B4D108948088B4D08C7003C325A72C74004010000008948205DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     cx, [ebp+arg_4]
		#mov     [eax+1Ch], cx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_725A323C
		#mov     dword ptr [eax+4], 1
		#mov     [eax+20h], ecx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725A33D8(self):
		#sub_725A33D8
		gadget = "F641040A6A00580F94C0C3"
		self.do(gadget)

		#test    byte ptr [ecx+4], 0Ah
		#push    0
		#pop     eax
		#setz    al
		#retn


  def test_gadget_sub_725A4316(self):
		#sub_725A4316
		gadget = "8BFF558BEC8B45088B40185DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+18h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_725A4B75(self):
		#sub_725A4B75
		gadget = "B8E3010480C21000"
		self.do(gadget)

		#mov     eax, 800401E3h
		#retn    10h


  def test_gadget_sub_725A4EB3(self):
		#sub_725A4EB3
		gadget = "8BFF558BEC8BC1568B75085733C9C70000235872C74004F84E5A72C740088CDB5C72C7400C0100000089482489482889482C8948308D7810A5A5A5A55F8948205E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#push    esi
		#mov     esi, [ebp+arg_0]
		#push    edi
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_72582300
		#mov     dword ptr [eax+4], offset off_725A4EF8
		#mov     dword ptr [eax+8], offset off_725CDB8C
		#mov     dword ptr [eax+0Ch], 1
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#lea     edi, [eax+10h]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#mov     [eax+20h], ecx
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725A6A8E(self):
		#sub_725A6A8E
		gadget = "64A1180000008B40308B80D80100002500001000C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+30h]
		#mov     eax, [eax+1D8h]
		#and     eax, 100000h
		#retn


  def test_gadget_sub_725A6D88(self):
		#sub_725A6D88
		gadget = "8BFF558BEC8B45088B50208951208B50348951348B50388951388B403C89413C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [eax+20h]
		#mov     [ecx+20h], edx
		#mov     edx, [eax+34h]
		#mov     [ecx+34h], edx
		#mov     edx, [eax+38h]
		#mov     [ecx+38h], edx
		#mov     eax, [eax+3Ch]
		#mov     [ecx+3Ch], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_725A713B(self):
		#sub_725A713B
		gadget = "B001C20400"
		self.do(gadget)

		#mov     al, 1
		#retn    4


  def test_gadget_sub_725A7527(self):
		#sub_725A7527
		gadget = "8BFF558BEC8BC18B4D088360040089088B4D0C894808C6400C005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+4], 0
		#mov     [eax], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+8], ecx
		#mov     byte ptr [eax+0Ch], 0
		#pop     ebp
		#retn    8


  def test_gadget_sub_725A8D0F(self):
		#sub_725A8D0F
		gadget = "8BFF558BEC8B4508C64114018320005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     byte ptr [ecx+14h], 1
		#and     dword ptr [eax], 0
		#pop     ebp
		#retn    4


  def test_gadget_sub_725A8D60(self):
		#sub_725A8D60
		gadget = "8A4114C3"
		self.do(gadget)

		#mov     al, [ecx+14h]
		#retn


  def test_gadget_sub_725A9217(self):
		#sub_725A9217
		gadget = "8BFF558BEC8B45088B008B4D0C2B015DC3"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax]
		#mov     ecx, [ebp+arg_4]
		#sub     eax, [ecx]
		#pop     ebp
		#retn


  def test_gadget_sub_725AA529(self):
		#sub_725AA529
		gadget = "8BFF558BEC8BC18B4D08C70048A55A72C74004010000008948085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_725AA548
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725AAC1C(self):
		#sub_725AAC1C
		gadget = "8B41348B51388950048B41388B513489108361340083613800C3"
		self.do(gadget)

		#mov     eax, [ecx+34h]
		#mov     edx, [ecx+38h]
		#mov     [eax+4], edx
		#mov     eax, [ecx+38h]
		#mov     edx, [ecx+34h]
		#mov     [eax], edx
		#and     dword ptr [ecx+34h], 0
		#and     dword ptr [ecx+38h], 0
		#retn


  def test_gadget_sub_725AB52A(self):
		#sub_725AB52A
		gadget = "8BFF558BEC8B550C668389BC00000010568B750823750C8D81B4000000F7D223100BD6891033C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_4]
		#or      word ptr [ecx+0BCh], 10h
		#push    esi
		#mov     esi, [ebp+arg_0]
		#and     esi, [ebp+arg_4]
		#lea     eax, [ecx+0B4h]
		#not     edx
		#and     edx, [eax]
		#or      edx, esi
		#mov     [eax], edx
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_725AD969(self):
		#sub_725AD969
		gadget = "83613CFC834944FF33C0BAB0040000C7410450525053C741080100000089410C8941108941148941186689514089414889414CC3"
		self.do(gadget)

		#and     dword ptr [ecx+3Ch], 0FFFFFFFCh
		#or      dword ptr [ecx+44h], 0FFFFFFFFh
		#xor     eax, eax
		#mov     edx, 4B0h
		#mov     dword ptr [ecx+4], 53505250h
		#mov     dword ptr [ecx+8], 1
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#mov     [ecx+18h], eax
		#mov     [ecx+40h], dx
		#mov     [ecx+48h], eax
		#mov     [ecx+4Ch], eax
		#retn


  def test_gadget_sub_725ADC80(self):
		#sub_725ADC80
		gadget = "05D5CDD59C2E1B10939708002B2CF9AE"
		self.do(gadget)

		#add     eax, 9CD5CDD5h
		#sbb     edx, cs:[eax]
		#xchg    eax, ebx
		#xchg    eax, edi
		#or      [eax], al
		#sub     ebp, [ecx+edi*8]
		#scasb


  def test_gadget_sub_725AFCBB(self):
		#sub_725AFCBB
		gadget = "8BFF558BEC8B45088B40048B4D0C2B41045DC3"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4]
		#mov     ecx, [ebp+arg_4]
		#sub     eax, [ecx+4]
		#pop     ebp
		#retn


  def test_gadget_sub_725B1F65(self):
		#sub_725B1F65
		gadget = "33C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget_OleBuildVersion(self):
		#OleBuildVersion
		gadget = "B838031700C3"
		self.do(gadget)

		#mov     eax, 170338h    ; CoBuildVersion
		#retn


  def test_gadget_sub_725B54C4(self):
		#sub_725B54C4
		gadget = "8BFF558BEC8B55088BC133C9890889500489481089480C8948085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], edx
		#mov     [eax+10h], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+8], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725B5E70(self):
		#sub_725B5E70
		gadget = "3F009090909090"
		self.do(gadget)

		#aas
		#add     [eax-6F6F6F70h], dl


  def test_gadget_sub_725B68A2(self):
		#sub_725B68A2
		gadget = "33C0C21000"
		self.do(gadget)

		#xor     eax, eax
		#retn    10h


  def test_gadget_sub_725B7EBE(self):
		#sub_725B7EBE
		gadget = "8BFF558BEC8B516C8B450C89108B51708950048B516C8B450889108B51708950048B51648B451089108B49688948045DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ecx+6Ch]
		#mov     eax, [ebp+arg_4]
		#mov     [eax], edx
		#mov     edx, [ecx+70h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+6Ch]
		#mov     eax, [ebp+arg_0]
		#mov     [eax], edx
		#mov     edx, [ecx+70h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+64h]
		#mov     eax, [ebp+arg_8]
		#mov     [eax], edx
		#mov     ecx, [ecx+68h]
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725BA526(self):
		#sub_725BA526
		gadget = "8B0183C004C3"
		self.do(gadget)

		#mov     eax, [ecx]
		#add     eax, 4
		#retn


  def test_gadget_sub_725BB5AE(self):
		#sub_725BB5AE
		gadget = "8BFF558BEC8B4508560FB7712833D2F7F68B550C5E89020FB749288B450833D2F7F18B451066891033C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#push    esi
		#movzx   esi, word ptr [ecx+28h]
		#xor     edx, edx
		#div     esi
		#mov     edx, [ebp+arg_4]
		#pop     esi
		#mov     [edx], eax
		#movzx   ecx, word ptr [ecx+28h]
		#mov     eax, [ebp+arg_0]
		#xor     edx, edx
		#div     ecx
		#mov     eax, [ebp+arg_8]
		#mov     [eax], dx
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725BBC3E(self):
		#sub_725BBC3E
		gadget = "8BFF558BEC8B45088B550C568BB4C18800000089328B84C18C00000089420433C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [ebp+arg_4]
		#push    esi
		#mov     esi, [ecx+eax*8+88h]
		#mov     [edx], esi
		#mov     eax, [ecx+eax*8+8Ch]
		#mov     [edx+4], eax
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_725BC3C9(self):
		#sub_725BC3C9
		gadget = "8BFF558BEC8B55088BC15633F6468ACAD3E68B4D0C6609B0BC000000898CD0880000008B4D10898CD08C00000033C05E5DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#push    esi
		#xor     esi, esi
		#inc     esi
		#mov     cl, dl
		#shl     esi, cl
		#mov     ecx, [ebp+arg_4]
		#or      [eax+0BCh], si
		#mov     [eax+edx*8+88h], ecx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+edx*8+8Ch], ecx
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725BCE3A(self):
		#sub_725BCE3A
		gadget = "8BFF558BEC56578B7D088DB1A4000000A5A5A5A55F33C05E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_0]
		#lea     esi, [ecx+0A4h]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725BCE67(self):
		#sub_725BCE67
		gadget = "8BFF558BEC8B81B40000008B4D08890133C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ecx+0B4h]
		#mov     ecx, [ebp+arg_0]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_725BCE8E(self):
		#sub_725BCE8E
		gadget = "8BFF558BEC568B7508578DB9A4000000A5A5A5A5668389BC000000085F33C05E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#push    edi
		#lea     edi, [ecx+0A4h]
		#movsd
		#movsd
		#movsd
		#movsd
		#or      word ptr [ecx+0BCh], 8
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725BD2CF(self):
		#sub_725BD2CF
		gadget = "8BC1832000C3"
		self.do(gadget)

		#mov     eax, ecx
		#and     dword ptr [eax], 0
		#retn


  def test_gadget_sub_725BD43B(self):
		#sub_725BD43B
		gadget = "8BFF558BEC8BC133C989480489480889480C8948108B4D08C70038DE57728948145DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_7257DE38
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725BD465(self):
		#sub_725BD465
		gadget = "8BFF558BEC8B45088B550C5657BEA49A58728BF9A5A5A5A589412433C0834938FF5F89412889412C89413089513489413C89414489414889414C8941508941545E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [ebp+arg_4]
		#push    esi
		#push    edi
		#mov     esi, offset stru_72589AA4
		#mov     edi, ecx
		#movsd
		#movsd
		#movsd
		#movsd
		#mov     [ecx+24h], eax
		#xor     eax, eax
		#or      dword ptr [ecx+38h], 0FFFFFFFFh
		#pop     edi
		#mov     [ecx+28h], eax
		#mov     [ecx+2Ch], eax
		#mov     [ecx+30h], eax
		#mov     [ecx+34h], edx
		#mov     [ecx+3Ch], eax
		#mov     [ecx+44h], eax
		#mov     [ecx+48h], eax
		#mov     [ecx+4Ch], eax
		#mov     [ecx+50h], eax
		#mov     [ecx+54h], eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_725BE983(self):
		#sub_725BE983
		gadget = "8BFF558BEC8B550C8BC133C98950308B55088950408B5510C70010425C72C740040100000089480889483489482C89482889483889483C89502489480C89481089481489481889481C8948208948448948485DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_4]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+30h], edx
		#mov     edx, [ebp+arg_0]
		#mov     [eax+40h], edx
		#mov     edx, [ebp+arg_8]
		#mov     dword ptr [eax], offset off_725C4210
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+38h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+24h], edx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725C0644(self):
		#sub_725C0644
		gadget = "8BFF558BEC8B51108B450889108B51148950048B51088B450C89108B510C8950048B118B451089108B49048948045DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ecx+10h]
		#mov     eax, [ebp+arg_0]
		#mov     [eax], edx
		#mov     edx, [ecx+14h]
		#mov     [eax+4], edx
		#mov     edx, [ecx+8]
		#mov     eax, [ebp+arg_4]
		#mov     [eax], edx
		#mov     edx, [ecx+0Ch]
		#mov     [eax+4], edx
		#mov     edx, [ecx]
		#mov     eax, [ebp+arg_8]
		#mov     [eax], edx
		#mov     ecx, [ecx+4]
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725C35D1(self):
		#sub_725C35D1
		gadget = "FF412C81490480000000C3"
		self.do(gadget)

		#inc     dword ptr [ecx+2Ch]
		#or      dword ptr [ecx+4], 80h
		#retn


  def test_gadget_sub_725C4255(self):
		#sub_725C4255
		gadget = "8BFF558BEC8B4D0833C03941340F94C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#xor     eax, eax
		#cmp     [ecx+34h], eax
		#setz    al
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C4581(self):
		#sub_725C4581
		gadget = "C701503F5C72C74104283F5C72C74108803D5C72C7410C38DE5772C3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_725C3F50
		#mov     dword ptr [ecx+4], offset off_725C3F28
		#mov     dword ptr [ecx+8], offset off_725C3D80
		#mov     dword ptr [ecx+0Ch], offset off_7257DE38
		#retn


  def test_gadget_sub_725C4792(self):
		#sub_725C4792
		gadget = "C74118183D5C72C7411C183C5C72C74120A83D5C72C74124943C5C72C7412810405C72C70138DE5772C3"
		self.do(gadget)

		#mov     dword ptr [ecx+18h], offset off_725C3D18
		#mov     dword ptr [ecx+1Ch], offset off_725C3C18
		#mov     dword ptr [ecx+20h], offset off_725C3DA8
		#mov     dword ptr [ecx+24h], offset off_725C3C94
		#mov     dword ptr [ecx+28h], offset off_725C4010
		#mov     dword ptr [ecx], offset off_7257DE38
		#retn


  def test_gadget_sub_725C5739(self):
		#sub_725C5739
		gadget = "C701E0BA5572C3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_7255BAE0
		#retn


  def test_gadget_sub_725C5B39(self):
		#sub_725C5B39
		gadget = "8BFF558BEC8B91980000008B450889108B899C0000008948045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ecx+98h]
		#mov     eax, [ebp+arg_0]
		#mov     [eax], edx
		#mov     ecx, [ecx+9Ch]
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C5FC8(self):
		#sub_725C5FC8
		gadget = "8BFF558BEC8B55088BC18A4838D3EA8B4D0C8911668B403A662345088B4D106689015DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#mov     cl, [eax+38h]
		#shr     edx, cl
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], edx
		#mov     ax, [eax+3Ah]
		#and     ax, word ptr [ebp+arg_0]
		#mov     ecx, [ebp+arg_8]
		#mov     [ecx], ax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_725C6F81(self):
		#sub_725C6F81
		gadget = "8BFF558BEC8BC18B4D08836010FE8360080083600400C700A4525872C7400C50535354C74018010000008948145DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+10h], 0FFFFFFFEh
		#and     dword ptr [eax+8], 0
		#and     dword ptr [eax+4], 0
		#mov     dword ptr [eax], offset off_725852A4
		#mov     dword ptr [eax+0Ch], 54535350h
		#mov     dword ptr [eax+18h], 1
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C6FDF(self):
		#sub_725C6FDF
		gadget = "8BFF558BEC8BC18B4D0881E1FFFFFEFF89481C33C9836008FEC7001CC35C72C7400408C35C7289480C8948148948108948188948205DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     ecx, 0FFFEFFFFh
		#mov     [eax+1Ch], ecx
		#xor     ecx, ecx
		#and     dword ptr [eax+8], 0FFFFFFFEh
		#mov     dword ptr [eax], offset off_725CC31C
		#mov     dword ptr [eax+4], offset off_725CC308
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+20h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C71AC(self):
		#sub_725C71AC
		gadget = "8BFF558BEC8B45088941108B450C8941185DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+10h], eax
		#mov     eax, [ebp+arg_4]
		#mov     [ecx+18h], eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_725C7B31(self):
		#sub_725C7B31
		gadget = "8BFF558BEC53668B5D0856578BD16A06586689422066895A1EC74238001000008D7A08BEA49A5872A5A5A5A56A3EB8FEFF00006689421C58668942186A0958663BC31BC0F7D883C0036689421A83C8FF6A6D598D724C8BFEF3AB33C0406AFE5989422C89423033C033FF668942226A0958663BC31BC0F7D8893E897A48897A40897A34897A24894228894A44894A3CA1D87B5C728902A1DC7B5C725F5E8942048BC25B5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    ebx
		#mov     bx, [ebp+arg_0]
		#push    esi
		#push    edi
		#mov     edx, ecx
		#push    6
		#pop     eax
		#mov     [edx+20h], ax
		#mov     [edx+1Eh], bx
		#mov     dword ptr [edx+38h], 1000h
		#lea     edi, [edx+8]
		#mov     esi, offset stru_72589AA4
		#movsd
		#movsd
		#movsd
		#movsd
		#push    3Eh
		#mov     eax, 0FFFEh
		#mov     [edx+1Ch], ax
		#pop     eax
		#mov     [edx+18h], ax
		#push    9
		#pop     eax
		#cmp     ax, bx
		#sbb     eax, eax
		#neg     eax
		#add     eax, 3
		#mov     [edx+1Ah], ax
		#or      eax, 0FFFFFFFFh
		#push    6Dh
		#pop     ecx
		#lea     esi, [edx+4Ch]
		#mov     edi, esi
		#rep stosd
		#xor     eax, eax
		#inc     eax
		#push    0FFFFFFFEh
		#pop     ecx
		#mov     [edx+2Ch], eax
		#mov     [edx+30h], eax
		#xor     eax, eax
		#xor     edi, edi
		#mov     [edx+22h], ax
		#push    9
		#pop     eax
		#cmp     ax, bx
		#sbb     eax, eax
		#neg     eax
		#mov     [esi], edi
		#mov     [edx+48h], edi
		#mov     [edx+40h], edi
		#mov     [edx+34h], edi
		#mov     [edx+24h], edi
		#mov     [edx+28h], eax
		#mov     [edx+44h], ecx
		#mov     [edx+3Ch], ecx
		#mov     eax, ds:dword_725C7BD8
		#mov     [edx], eax
		#mov     eax, ds:dword_725C7BDC
		#pop     edi
		#pop     esi
		#mov     [edx+4], eax
		#mov     eax, edx
		#pop     ebx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C7C24(self):
		#sub_725C7C24
		gadget = "8BFF558BEC8B55088BC133C9890889480489480889480C8950108948148948185DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], edx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C91EA(self):
		#sub_725C91EA
		gadget = "8BFF558BEC8B450805FF3F00002500C0FFFF5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#add     eax, 3FFFh
		#and     eax, 0FFFFC000h
		#pop     ebp
		#retn    4


  def test_gadget_sub_725C9F1C(self):
		#sub_725C9F1C
		gadget = "8BFF558BEC8B45088B40148B40205DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+14h]
		#mov     eax, [eax+20h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_725CA975(self):
		#sub_725CA975
		gadget = "8BFF558BEC8B45088941108B450C8941148B45108941088B451489410C8B451889018B451C8941045DC21800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+10h], eax
		#mov     eax, [ebp+arg_4]
		#mov     [ecx+14h], eax
		#mov     eax, [ebp+arg_8]
		#mov     [ecx+8], eax
		#mov     eax, [ebp+arg_C]
		#mov     [ecx+0Ch], eax
		#mov     eax, [ebp+arg_10]
		#mov     [ecx], eax
		#mov     eax, [ebp+arg_14]
		#mov     [ecx+4], eax
		#pop     ebp
		#retn    18h


  def test_gadget_sub_725CABE2(self):
		#sub_725CABE2
		gadget = "8BFF558BEC8B51688B450889108B496C8948045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ecx+68h]
		#mov     eax, [ebp+arg_0]
		#mov     [eax], edx
		#mov     ecx, [ecx+6Ch]
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_725CB825(self):
		#sub_725CB825
		gadget = "8BFF558BEC8B51048B45088901568B72088970088B720C89700C8B5210895010C74108010000005E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ecx+4]
		#mov     eax, [ebp+arg_0]
		#mov     [ecx], eax
		#push    esi
		#mov     esi, [edx+8]
		#mov     [eax+8], esi
		#mov     esi, [edx+0Ch]
		#mov     [eax+0Ch], esi
		#mov     edx, [edx+10h]
		#mov     [eax+10h], edx
		#mov     dword ptr [ecx+8], 1
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725CC13A(self):
		#sub_725CC13A
		gadget = "C701D8885572C3"
		self.do(gadget)

		#mov     dword ptr [ecx], offset off_725588D8
		#retn


  def test_gadget_nullsub_12(self):
		#nullsub_12
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_sub_725CD4C5(self):
		#sub_725CD4C5
		gadget = "8BC183200083600400C3"
		self.do(gadget)

		#mov     eax, ecx
		#and     dword ptr [eax], 0
		#and     dword ptr [eax+4], 0
		#retn


  def test_gadget_sub_725CE1DB(self):
		#sub_725CE1DB
		gadget = "33C0C20800"
		self.do(gadget)

		#xor     eax, eax
		#retn    8


  def test_gadget_sub_725CEA43(self):
		#sub_725CEA43
		gadget = "8BFF558BEC8B45088B502C8951048B5034568951088B50205789510C8B700C83C61C8D7910A5A5A5A55F5E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [eax+2Ch]
		#mov     [ecx+4], edx
		#mov     edx, [eax+34h]
		#push    esi
		#mov     [ecx+8], edx
		#mov     edx, [eax+20h]
		#push    edi
		#mov     [ecx+0Ch], edx
		#mov     esi, [eax+0Ch]
		#add     esi, 1Ch
		#lea     edi, [ecx+10h]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_725CEC91(self):
		#sub_725CEC91
		gadget = "8B41188B511C89501C8B411C8B511889501889491C894918C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#mov     edx, [ecx+1Ch]
		#mov     [eax+1Ch], edx
		#mov     eax, [ecx+1Ch]
		#mov     edx, [ecx+18h]
		#mov     [eax+18h], edx
		#mov     [ecx+1Ch], ecx
		#mov     [ecx+18h], ecx
		#retn


  def test_gadget_sub_725CF1FA(self):
		#sub_725CF1FA
		gadget = "8B81CC00000083E001C3"
		self.do(gadget)

		#mov     eax, [ecx+0CCh]
		#and     eax, 1
		#retn


  def test_gadget_sub_725CFFFF(self):
		#sub_725CFFFF
		gadget = "FF41148B4114C3"
		self.do(gadget)

		#inc     dword ptr [ecx+14h]
		#mov     eax, [ecx+14h]
		#retn


  def test_gadget_sub_725D0091(self):
		#sub_725D0091
		gadget = "8BFF558BEC8B4508FF40108B40105DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+10h]
		#mov     eax, [eax+10h]
		#pop     ebp
		#retn    4


  def test_gadget_nullsub_11(self):
		#nullsub_11
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_10(self):
		#nullsub_10
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_9(self):
		#nullsub_9
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_sub_725F2F09(self):
		#sub_725F2F09
		gadget = "8B65E833F68975E4"
		self.do(gadget)

		#mov     esp, [ebp-18h]
		#xor     esi, esi
		#mov     [ebp-1Ch], esi


  def test_gadget_sub_725F2F82(self):
		#sub_725F2F82
		gadget = "8B65E833F6"
		self.do(gadget)

		#mov     esp, [ebp-18h]
		#xor     esi, esi


  def test_gadget_sub_725F2FB1(self):
		#sub_725F2FB1
		gadget = "8B65E833F6"
		self.do(gadget)

		#mov     esp, [ebp-18h]
		#xor     esi, esi


  def test_gadget_sub_725F2FEA(self):
		#sub_725F2FEA
		gadget = "8B65E833F6"
		self.do(gadget)

		#mov     esp, [ebp-18h]
		#xor     esi, esi


  def test_gadget_sub_725F304F(self):
		#sub_725F304F
		gadget = "8B65E833F68975E4"
		self.do(gadget)

		#mov     esp, [ebp-18h]
		#xor     esi, esi
		#mov     [ebp-1Ch], esi


  def test_gadget_sub_725F585C(self):
		#sub_725F585C
		gadget = "8B45EC8B008B008945E033C040C3"
		self.do(gadget)

		#mov     eax, [ebp-14h]
		#mov     eax, [eax]
		#mov     eax, [eax]
		#mov     [ebp-20h], eax
		#xor     eax, eax
		#inc     eax
		#retn


  def test_gadget_sub_725F5BD8(self):
		#sub_725F5BD8
		gadget = "8B45EC8B008B008945DC33C040C3"
		self.do(gadget)

		#mov     eax, [ebp-14h]
		#mov     eax, [eax]
		#mov     eax, [eax]
		#mov     [ebp-24h], eax
		#xor     eax, eax
		#inc     eax
		#retn


  def test_gadget_nullsub_14(self):
		#nullsub_14
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_13(self):
		#nullsub_13
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_3(self):
		#nullsub_3
		gadget = "CB"
		self.do(gadget)

		#retf


  def test_gadget_nullsub_4(self):
		#nullsub_4
		gadget = "CB"
		self.do(gadget)

		#retf


  def test_gadget_sub_725FCD07(self):
		#sub_725FCD07
		gadget = "8BFF558BEC8B4508FF40248B40245DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+24h]
		#mov     eax, [eax+24h]
		#pop     ebp
		#retn    4


  def test_gadget_IsEqualGUID(self):
		#IsEqualGUID
		gadget = "8BFF558BEC568B7508578B7D0C6A045933C0F3A75F0F94C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_0]
		#push    edi
		#mov     edi, [ebp+arg_4]
		#push    4
		#pop     ecx
		#xor     eax, eax
		#repe cmpsd
		#pop     edi
		#setz    al
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72600AA6(self):
		#sub_72600AA6
		gadget = "8BFF558BEC8B55088BC133C98950148B550C89480489480889480CC700489E5F7289501089481889481C89482089482489482889482C89483489484089485089484C89483089483C8948385DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_0]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+14h], edx
		#mov     edx, [ebp+arg_4]
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     dword ptr [eax], offset off_725F9E48
		#mov     [eax+10h], edx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+38h], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260123D(self):
		#sub_7260123D
		gadget = "64A1180000008B80800F00008B400C83E004C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+0F80h]
		#mov     eax, [eax+0Ch]
		#and     eax, 4
		#retn


  def test_gadget_sub_726060C2(self):
		#sub_726060C2
		gadget = "C7411840AD5472C7411C809F5F72C7412000C15472C74124609F5F72C74128389F5F72C70138DE5772C3"
		self.do(gadget)

		#mov     dword ptr [ecx+18h], offset off_7254AD40
		#mov     dword ptr [ecx+1Ch], offset off_725F9F80
		#mov     dword ptr [ecx+20h], offset off_7254C100
		#mov     dword ptr [ecx+24h], offset off_725F9F60
		#mov     dword ptr [ecx+28h], offset off_725F9F38
		#mov     dword ptr [ecx], offset off_7257DE38
		#retn


  def test_gadget_sub_726076C2(self):
		#sub_726076C2
		gadget = "8B75088B7DE09090909090"
		self.do(gadget)

		#mov     esi, [ebp+8]
		#mov     edi, [ebp-20h]
		#nop
		#nop
		#nop
		#nop
		#nop


  def test_gadget_sub_72609594(self):
		#sub_72609594
		gadget = "33C0C20800"
		self.do(gadget)

		#xor     eax, eax
		#retn    8


  def test_gadget_sub_7260A7A2(self):
		#sub_7260A7A2
		gadget = "33C0C21400"
		self.do(gadget)

		#xor     eax, eax
		#retn    14h


  def test_gadget_sub_7260AB27(self):
		#sub_7260AB27
		gadget = "8BC1C70038AB6072C7400401000000C3"
		self.do(gadget)

		#mov     eax, ecx
		#mov     dword ptr [eax], offset off_7260AB38
		#mov     dword ptr [eax+4], 1
		#retn


  def test_gadget_sub_7260BA4A(self):
		#sub_7260BA4A
		gadget = "8BFF558BEC8B450CC7000100000033C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword ptr [eax], 1
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7260C144(self):
		#sub_7260C144
		gadget = "8BFF558BEC8B45088B4044C1E802F7D083E0015DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+44h]
		#shr     eax, 2
		#not     eax
		#and     eax, 1
		#pop     ebp
		#retn    4


  def test_gadget_sub_7260D49A(self):
		#sub_7260D49A
		gadget = "8BFF558BEC8B450CC7000300000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword ptr [eax], 3
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260DB86(self):
		#sub_7260DB86
		gadget = "8BFF558BEC8B450CC7000500000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword ptr [eax], 5
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260DB9F(self):
		#sub_7260DB9F
		gadget = "8BFF558BEC8B4510832000B8014000805DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#mov     eax, 80004001h
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7260E818(self):
		#sub_7260E818
		gadget = "8BFF558BEC56578B7D0CBEB8575672A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_725657B8
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260E898(self):
		#sub_7260E898
		gadget = "8BFF558BEC8B450C83600400C7001400000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax+4], 0
		#mov     dword ptr [eax], 14h
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260EAB7(self):
		#sub_7260EAB7
		gadget = "8BFF558BEC8B450CC7000A00000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword ptr [eax], 0Ah
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260F2FB(self):
		#sub_7260F2FB
		gadget = "8BFF558BEC8B4518832000B8014000805DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_10]
		#and     dword ptr [eax], 0
		#mov     eax, 80004001h
		#pop     ebp
		#retn    14h


  def test_gadget_sub_7260F314(self):
		#sub_7260F314
		gadget = "8BFF558BEC8B450C832000B8EC0104805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#mov     eax, 800401ECh
		#pop     ebp
		#retn    8


  def test_gadget_sub_7260F35B(self):
		#sub_7260F35B
		gadget = "8BFF558BEC8B4514832000B8014000805DC21000"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_C]
		#and     dword ptr [eax], 0
		#mov     eax, 80004001h
		#pop     ebp
		#retn    10h


  def test_gadget_sub_7260F374(self):
		#sub_7260F374
		gadget = "8BFF558BEC8B451C832000B8014000805DC21800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_14]
		#and     dword ptr [eax], 0
		#mov     eax, 80004001h
		#pop     ebp
		#retn    18h


  def test_gadget_sub_72610E2C(self):
		#sub_72610E2C
		gadget = "8BFF558BEC8B550C33C08951088B550889410489510C8941108941145DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_4]
		#xor     eax, eax
		#mov     [ecx+8], edx
		#mov     edx, [ebp+arg_0]
		#mov     [ecx+4], eax
		#mov     [ecx+0Ch], edx
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72611B72(self):
		#sub_72611B72
		gadget = "8B81CC0000002500000100C3"
		self.do(gadget)

		#mov     eax, [ecx+0CCh]
		#and     eax, 10000h
		#retn


  def test_gadget_sub_72611B83(self):
		#sub_72611B83
		gadget = "8B81CC0000002500000200C3"
		self.do(gadget)

		#mov     eax, [ecx+0CCh]
		#and     eax, 20000h
		#retn


  def test_gadget_sub_72611B94(self):
		#sub_72611B94
		gadget = "81A1CC000000FFFFF7FFC3"
		self.do(gadget)

		#and     dword ptr [ecx+0CCh], 0FFF7FFFFh
		#retn


  def test_gadget_sub_72611D82(self):
		#sub_72611D82
		gadget = "8BFF558BEC8B81CC0000008B4D0883E003890133C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ecx+0CCh]
		#mov     ecx, [ebp+arg_0]
		#and     eax, 3
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_72612F8E(self):
		#sub_72612F8E
		gadget = "6A0258C20400"
		self.do(gadget)

		#push    2
		#pop     eax
		#retn    4


  def test_gadget_sub_72612FE3(self):
		#sub_72612FE3
		gadget = "B8FFFF0080C21C00"
		self.do(gadget)

		#mov     eax, 8000FFFFh
		#retn    1Ch


  def test_gadget_nullsub_5(self):
		#nullsub_5
		gadget = "C20400"
		self.do(gadget)

		#retn    4


  def test_gadget_sub_7261456C(self):
		#sub_7261456C
		gadget = "8BFF558BEC56578B7D10BE78575672A5A5A5A55F33C05E5DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_8]
		#mov     esi, offset dword_72565778
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72615CA0(self):
		#sub_72615CA0
		gadget = "8BFF558BEC8B4D088B01568BD0C1EA088BF0C1E60833D681E2FF00FF00C1E00833D0C1C21089115E5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     eax, [ecx]
		#push    esi
		#mov     edx, eax
		#shr     edx, 8
		#mov     esi, eax
		#shl     esi, 8
		#xor     edx, esi
		#and     edx, 0FF00FFh
		#shl     eax, 8
		#xor     edx, eax
		#rol     edx, 10h
		#mov     [ecx], edx
		#pop     esi
		#pop     ebp
		#retn    4


  def test_gadget_sub_72615CD1(self):
		#sub_72615CD1
		gadget = "8BFF558BEC8B4508660FB64801668B1066C1E208660BCA6689085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#movzx   cx, byte ptr [eax+1]
		#mov     dx, [eax]
		#shl     dx, 8
		#or      cx, dx
		#mov     [eax], cx
		#pop     ebp
		#retn    4


  def test_gadget_nullsub_6(self):
		#nullsub_6
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_7(self):
		#nullsub_7
		gadget = "C20100"
		self.do(gadget)

		#retn    1


  def test_gadget_sub_7261648D(self):
		#sub_7261648D
		gadget = "8BFF558BEC8B45148320005DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_C]
		#and     dword ptr [eax], 0
		#pop     ebp
		#retn    14h


  def test_gadget_sub_72617597(self):
		#sub_72617597
		gadget = "8BFF558BEC8BC18B4D08C700B8756172C74004010000008948085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_726175B8
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_726176DA(self):
		#sub_726176DA
		gadget = "8BFF558BEC8BC18B4D08C700F8766172C74004010000008948085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_726176F8
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_72618AEB(self):
		#sub_72618AEB
		gadget = "8BFF558BEC8B4508C74004E86A68728B0DE86A68728941048B0DE86A68728908A3E86A68725DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     dword ptr [eax+4], offset dword_72686AE8
		#mov     ecx, dword_72686AE8
		#mov     [ecx+4], eax
		#mov     ecx, dword_72686AE8
		#mov     [eax], ecx
		#mov     dword_72686AE8, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_72618B19(self):
		#sub_72618B19
		gadget = "8BFF558BEC8B45088B48048B1089118B088B500489510489400489005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+4]
		#mov     edx, [eax]
		#mov     [ecx], edx
		#mov     ecx, [eax]
		#mov     edx, [eax+4]
		#mov     [ecx+4], edx
		#mov     [eax+4], eax
		#mov     [eax], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_72619B6E(self):
		#sub_72619B6E
		gadget = "8BFF558BEC8B450CA32089687233C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     dword_72688920, eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7261A97E(self):
		#sub_7261A97E
		gadget = "8BFF558BEC8B45088B4D0C8988E00000005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+0E0h], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7261A998(self):
		#sub_7261A998
		gadget = "8BFF558BEC8B45088B80E00000005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0E0h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_7261C26D(self):
		#sub_7261C26D
		gadget = "8BFF558BEC8B4508FF400C8B400C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+0Ch]
		#mov     eax, [eax+0Ch]
		#pop     ebp
		#retn    4


  def test_gadget_sub_7261CD44(self):
		#sub_7261CD44
		gadget = "8BFF558BEC8B4508FF005DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax]
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7261CD57(self):
		#sub_7261CD57
		gadget = "8BFF558BEC8B450C8B4D088B49048B551083C0028904915DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     ecx, [ebp+arg_0]
		#mov     ecx, [ecx+4]
		#mov     edx, [ebp+arg_8]
		#add     eax, 2
		#mov     [ecx+edx*4], eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7261D1BC(self):
		#sub_7261D1BC
		gadget = "8BC18360080083600C0033C941C70098EB5872894804894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#and     dword ptr [eax+8], 0
		#and     dword ptr [eax+0Ch], 0
		#xor     ecx, ecx
		#inc     ecx
		#mov     dword ptr [eax], offset off_7258EB98
		#mov     [eax+4], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_7261D7F6(self):
		#sub_7261D7F6
		gadget = "8BFF558BEC64A1180000008B80800F00008B4D088321008B40248B40405DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, large fs:18h
		#mov     eax, [eax+0F80h]
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [ecx], 0
		#mov     eax, [eax+24h]
		#mov     eax, [eax+40h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_7261F5D6(self):
		#sub_7261F5D6
		gadget = "8BFF558BEC8BC18B4D088360040083600800890089480CC74010010000005DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+4], 0
		#and     dword ptr [eax+8], 0
		#mov     [eax], eax
		#mov     [eax+0Ch], ecx
		#mov     dword ptr [eax+10h], 1
		#pop     ebp
		#retn    4


  def test_gadget_sub_72624BF0(self):
		#sub_72624BF0
		gadget = "B805400080C20C00"
		self.do(gadget)

		#mov     eax, 80004005h
		#retn    0Ch


  def test_gadget_sub_72624BFD(self):
		#sub_72624BFD
		gadget = "8BFF558BEC8B451083200033C0405DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#xor     eax, eax
		#inc     eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72624CF0(self):
		#sub_72624CF0
		gadget = "8BFF558BEC8B45088B80C80000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0C8h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72624D57(self):
		#sub_72624D57
		gadget = "8BFF558BEC8B45088B80CC0000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0CCh]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72624DBE(self):
		#sub_72624DBE
		gadget = "8BFF558BEC8B45088B80D00000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0D0h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72624DDC(self):
		#sub_72624DDC
		gadget = "8BFF558BEC8B45088B80D40000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0D4h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72624DFA(self):
		#sub_72624DFA
		gadget = "8BFF558BEC8B45088B80DC0000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0DCh]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72624E18(self):
		#sub_72624E18
		gadget = "8BFF558BEC8B45088B80D80000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0D8h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_726272B6(self):
		#sub_726272B6
		gadget = "8BFF558BEC8B4518832000B8054000805DC21800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_10]
		#and     dword ptr [eax], 0
		#mov     eax, 80004005h
		#pop     ebp
		#retn    18h


  def test_gadget_sub_726272CF(self):
		#sub_726272CF
		gadget = "8BFF558BEC8B4518832000B8014000805DC21800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_10]
		#and     dword ptr [eax], 0
		#mov     eax, 80004001h
		#pop     ebp
		#retn    18h


  def test_gadget_sub_726272E8(self):
		#sub_726272E8
		gadget = "B854010480C20800"
		self.do(gadget)

		#mov     eax, 80040154h
		#retn    8


  def test_gadget_sub_726272F5(self):
		#sub_726272F5
		gadget = "8BFF558BEC8B45088B4D0C83C00C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 0Ch
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7262750D(self):
		#sub_7262750D
		gadget = "8BFF558BEC8B45088B4D0C83C010890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#add     eax, 10h
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627528(self):
		#sub_72627528
		gadget = "8BFF558BEC8B45088B40248B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+24h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627543(self):
		#sub_72627543
		gadget = "8BFF558BEC8B45088B483C8B550C890A8B403CF7D81BC025FBBFFF7F05054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+3Ch]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+3Ch]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 7FFFBFFBh
		#add     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_7262756D(self):
		#sub_7262756D
		gadget = "8BFF558BEC8B45088B482C8B550C890A8B4028F7D81BC025FBBFFF7F05054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+2Ch]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+28h]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 7FFFBFFBh
		#add     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627597(self):
		#sub_72627597
		gadget = "8BFF558BEC8B45088B40308B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+30h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_726275B2(self):
		#sub_726275B2
		gadget = "8BFF558BEC8B45088B40388B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+38h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_726275CD(self):
		#sub_726275CD
		gadget = "8BFF558BEC8B45088B48348B550C890A8B4034F7D81BC025FBBFFF7F05054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+34h]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+34h]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 7FFFBFFBh
		#add     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627640(self):
		#sub_72627640
		gadget = "8BFF558BEC8B45088B48548B550C890A8B4054F7D81BC025FBBFFF7F05054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+54h]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+54h]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 7FFFBFFBh
		#add     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627701(self):
		#sub_72627701
		gadget = "8BFF558BEC8B45088B40688B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+68h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7262771C(self):
		#sub_7262771C
		gadget = "8BFF558BEC8B45088B404C8B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627737(self):
		#sub_72627737
		gadget = "8BFF558BEC8B45088B40508B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+50h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627752(self):
		#sub_72627752
		gadget = "8BFF558BEC8B45088B40748B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+74h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7262776D(self):
		#sub_7262776D
		gadget = "B805400080C20800"
		self.do(gadget)

		#mov     eax, 80004005h
		#retn    8


  def test_gadget_sub_72627815(self):
		#sub_72627815
		gadget = "8BFF558BEC8B4510832000B8054000805DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#mov     eax, 80004005h
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7262782E(self):
		#sub_7262782E
		gadget = "8BFF558BEC8B450C832000B8054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#mov     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627847(self):
		#sub_72627847
		gadget = "8BFF558BEC8B450C832000B8540104805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#mov     eax, 80040154h
		#pop     ebp
		#retn    8


  def test_gadget_sub_726278F0(self):
		#sub_726278F0
		gadget = "8BFF558BEC33C039450C0F95C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#xor     eax, eax
		#cmp     [ebp+arg_4], eax
		#setnz   al
		#pop     ebp
		#retn    8


  def test_gadget_sub_72627926(self):
		#sub_72627926
		gadget = "8BC183600400C70034796272C3"
		self.do(gadget)

		#mov     eax, ecx
		#and     dword ptr [eax+4], 0
		#mov     dword ptr [eax], offset off_72627934
		#retn


  def test_gadget_sub_7262BB11(self):
		#sub_7262BB11
		gadget = "8BFF558BEC8B45088B48108B550C890A8B40148B4D10890133C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+10h]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+14h]
		#mov     ecx, [ebp+arg_8]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7262BE17(self):
		#sub_7262BE17
		gadget = "8BFF558BEC8B45088B4D0C89480C5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+0Ch], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7262BE2E(self):
		#sub_7262BE2E
		gadget = "8BFF558BEC8B450883C0FC5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#add     eax, 0FFFFFFFCh
		#pop     ebp
		#retn    4


  def test_gadget_sub_7262D0C1(self):
		#sub_7262D0C1
		gadget = "8BFF558BEC8B45088B4D0C8948045DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+4], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7262D0D8(self):
		#sub_7262D0D8
		gadget = "8BFF558BEC8B45088B1089118B50048951048B50088951088B500C89510C668B5010668951108B50148951148B50188951188B501C89511C8B40208941205DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     edx, [eax]
		#mov     [ecx], edx
		#mov     edx, [eax+4]
		#mov     [ecx+4], edx
		#mov     edx, [eax+8]
		#mov     [ecx+8], edx
		#mov     edx, [eax+0Ch]
		#mov     [ecx+0Ch], edx
		#mov     dx, [eax+10h]
		#mov     [ecx+10h], dx
		#mov     edx, [eax+14h]
		#mov     [ecx+14h], edx
		#mov     edx, [eax+18h]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+1Ch]
		#mov     [ecx+1Ch], edx
		#mov     eax, [eax+20h]
		#mov     [ecx+20h], eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7262D463(self):
		#sub_7262D463
		gadget = "8BFF558BEC8B4510832000B8570007805DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#mov     eax, 80070057h
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7262D6B0(self):
		#sub_7262D6B0
		gadget = "8BFF558BEC8B45088B40045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4]
		#pop     ebp
		#retn    4


  def test_gadget_sub_72636548(self):
		#sub_72636548
		gadget = "8BFF558BEC8BC18B500833550C33C956418948045723D18B4D08315008C70020A457728BF18D780CA5A5A58B49085F8948185E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     edx, [eax+8]
		#xor     edx, [ebp+arg_4]
		#xor     ecx, ecx
		#push    esi
		#inc     ecx
		#mov     [eax+4], ecx
		#push    edi
		#and     edx, ecx
		#mov     ecx, [ebp+arg_0]
		#xor     [eax+8], edx
		#mov     dword ptr [eax], offset off_7257A420
		#mov     esi, ecx
		#lea     edi, [eax+0Ch]
		#movsd
		#movsd
		#movsd
		#mov     ecx, [ecx+8]
		#pop     edi
		#mov     [eax+18h], ecx
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_72636D5D(self):
		#sub_72636D5D
		gadget = "B8FFFF0080C20800"
		self.do(gadget)

		#mov     eax, 8000FFFFh
		#retn    8


  def test_gadget_sub_726380BE(self):
		#sub_726380BE
		gadget = "8BFF558BEC8BC18B550C8B4D0889500C33D289505CBA40746372895060BAC3746372895068BAE77D6372895070BA7D6C6372895078BAA3756372899080000000BAB376637289908800000089480433C933D2899094000000BA00776372899098000000BA677763728990A0000000BAAB6C63728990A8000000BA187863728990B0000000BA5D6D6372C700149D5F7289480889481489481889481C89482089482489482889482C89483089483489483C89484089484489484889484C89485089485489485889486489486C89487489487C89888400000089888C00000089889000000089889C0000008988A40000008988AC0000008988B40000008990B80000008988BC0000005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     edx, [ebp+arg_4]
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+0Ch], edx
		#xor     edx, edx
		#mov     [eax+5Ch], edx
		#mov     edx, offset sub_72637440
		#mov     [eax+60h], edx
		#mov     edx, offset sub_726374C3
		#mov     [eax+68h], edx
		#mov     edx, offset sub_72637DE7
		#mov     [eax+70h], edx
		#mov     edx, offset sub_72636C7D
		#mov     [eax+78h], edx
		#mov     edx, offset sub_726375A3
		#mov     [eax+80h], edx
		#mov     edx, offset sub_726376B3
		#mov     [eax+88h], edx
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#xor     edx, edx
		#mov     [eax+94h], edx
		#mov     edx, offset sub_72637700
		#mov     [eax+98h], edx
		#mov     edx, offset sub_72637767
		#mov     [eax+0A0h], edx
		#mov     edx, offset sub_72636CAB
		#mov     [eax+0A8h], edx
		#mov     edx, offset sub_72637818
		#mov     [eax+0B0h], edx
		#mov     edx, offset sub_72636D5D
		#mov     dword ptr [eax], offset off_725F9D14
		#mov     [eax+8], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+74h], ecx
		#mov     [eax+7Ch], ecx
		#mov     [eax+84h], ecx
		#mov     [eax+8Ch], ecx
		#mov     [eax+90h], ecx
		#mov     [eax+9Ch], ecx
		#mov     [eax+0A4h], ecx
		#mov     [eax+0ACh], ecx
		#mov     [eax+0B4h], ecx
		#mov     [eax+0B8h], edx
		#mov     [eax+0BCh], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_726382F1(self):
		#sub_726382F1
		gadget = "8BFF558BEC8BC18B550C8B4D0889500C33D289505CBAD6786372895060BA59796372895068BAE77D6372895070BAE66C6372895078BA3F7A6372899080000000BAB376637289908800000089480433C933D2899094000000BA627B6372899098000000BAC97B63728990A0000000BA1B6D63728990A8000000BA187863728990B0000000BA5D6D6372C700149D5F7289480889481489481889481C89482089482489482889482C89483089483489483C89484089484489484889484C89485089485489485889486489486C89487489487C89888400000089888C00000089889000000089889C0000008988A40000008988AC0000008988B40000008990B80000008988BC0000005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     edx, [ebp+arg_4]
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+0Ch], edx
		#xor     edx, edx
		#mov     [eax+5Ch], edx
		#mov     edx, offset sub_726378D6
		#mov     [eax+60h], edx
		#mov     edx, offset sub_72637959
		#mov     [eax+68h], edx
		#mov     edx, offset sub_72637DE7
		#mov     [eax+70h], edx
		#mov     edx, offset sub_72636CE6
		#mov     [eax+78h], edx
		#mov     edx, offset sub_72637A3F
		#mov     [eax+80h], edx
		#mov     edx, offset sub_726376B3
		#mov     [eax+88h], edx
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#xor     edx, edx
		#mov     [eax+94h], edx
		#mov     edx, offset sub_72637B62
		#mov     [eax+98h], edx
		#mov     edx, offset sub_72637BC9
		#mov     [eax+0A0h], edx
		#mov     edx, offset sub_72636D1B
		#mov     [eax+0A8h], edx
		#mov     edx, offset sub_72637818
		#mov     [eax+0B0h], edx
		#mov     edx, offset sub_72636D5D
		#mov     dword ptr [eax], offset off_725F9D14
		#mov     [eax+8], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+74h], ecx
		#mov     [eax+7Ch], ecx
		#mov     [eax+84h], ecx
		#mov     [eax+8Ch], ecx
		#mov     [eax+90h], ecx
		#mov     [eax+9Ch], ecx
		#mov     [eax+0A4h], ecx
		#mov     [eax+0ACh], ecx
		#mov     [eax+0B4h], ecx
		#mov     [eax+0B8h], edx
		#mov     [eax+0BCh], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_726384C0(self):
		#sub_726384C0
		gadget = "8BFF558BEC8BC18B550C8B4D0889500C33D289505CBA7E7C6372895060BA017D6372895068BAE77D6372895070BA6A6D6372895078BA7F7E6372899080000000BAB376637289908800000089480433C933D2899094000000BAA27F6372899098000000BA098063728990A0000000BA9F6D63728990A8000000BA187863728990B0000000BA5D6D6372C700149D5F7289480889481489481889481C89482089482489482889482C89483089483489483C89484089484489484889484C89485089485489485889486489486C89487489487C89888400000089888C00000089889000000089889C0000008988A40000008988AC0000008988B40000008990B80000008988BC0000005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     edx, [ebp+arg_4]
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+0Ch], edx
		#xor     edx, edx
		#mov     [eax+5Ch], edx
		#mov     edx, offset sub_72637C7E
		#mov     [eax+60h], edx
		#mov     edx, offset sub_72637D01
		#mov     [eax+68h], edx
		#mov     edx, offset sub_72637DE7
		#mov     [eax+70h], edx
		#mov     edx, offset sub_72636D6A
		#mov     [eax+78h], edx
		#mov     edx, offset sub_72637E7F
		#mov     [eax+80h], edx
		#mov     edx, offset sub_726376B3
		#mov     [eax+88h], edx
		#mov     [eax+4], ecx
		#xor     ecx, ecx
		#xor     edx, edx
		#mov     [eax+94h], edx
		#mov     edx, offset sub_72637FA2
		#mov     [eax+98h], edx
		#mov     edx, offset sub_72638009
		#mov     [eax+0A0h], edx
		#mov     edx, offset sub_72636D9F
		#mov     [eax+0A8h], edx
		#mov     edx, offset sub_72637818
		#mov     [eax+0B0h], edx
		#mov     edx, offset sub_72636D5D
		#mov     dword ptr [eax], offset off_725F9D14
		#mov     [eax+8], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#mov     [eax+24h], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+34h], ecx
		#mov     [eax+3Ch], ecx
		#mov     [eax+40h], ecx
		#mov     [eax+44h], ecx
		#mov     [eax+48h], ecx
		#mov     [eax+4Ch], ecx
		#mov     [eax+50h], ecx
		#mov     [eax+54h], ecx
		#mov     [eax+58h], ecx
		#mov     [eax+64h], ecx
		#mov     [eax+6Ch], ecx
		#mov     [eax+74h], ecx
		#mov     [eax+7Ch], ecx
		#mov     [eax+84h], ecx
		#mov     [eax+8Ch], ecx
		#mov     [eax+90h], ecx
		#mov     [eax+9Ch], ecx
		#mov     [eax+0A4h], ecx
		#mov     [eax+0ACh], ecx
		#mov     [eax+0B4h], ecx
		#mov     [eax+0B8h], edx
		#mov     [eax+0BCh], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_72638774(self):
		#sub_72638774
		gadget = "8BFF558BEC8B45088B400433C93848200F95C18BC15DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4]
		#xor     ecx, ecx
		#cmp     [eax+20h], cl
		#setnz   cl
		#mov     eax, ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7263A9D2(self):
		#sub_7263A9D2
		gadget = "8BFF558BEC8B450C83200033C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_CLIPFORMAT_UserFree(self):
		#CLIPFORMAT_UserFree
		gadget = "C20800"
		self.do(gadget)

		#retn    8


  def test_gadget_sub_7263BD99(self):
		#sub_7263BD99
		gadget = "B801400080C20C00"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    0Ch


  def test_gadget_sub_7263CFA1(self):
		#sub_7263CFA1
		gadget = "8BFF558BEC8B45088941548B450C89413C8B4150C74018010000005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+54h], eax
		#mov     eax, [ebp+arg_4]
		#mov     [ecx+3Ch], eax
		#mov     eax, [ecx+50h]
		#mov     dword ptr [eax+18h], 1
		#pop     ebp
		#retn    8


  def test_gadget_sub_7263DC22(self):
		#sub_7263DC22
		gadget = "B800000400C20800"
		self.do(gadget)

		#mov     eax, 40000h
		#retn    8


  def test_gadget_sub_7263DC5B(self):
		#sub_7263DC5B
		gadget = "8BFF558BEC8B45088B400433C9837844020F94C18BC15DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4]
		#xor     ecx, ecx
		#cmp     dword ptr [eax+44h], 2
		#setz    cl
		#mov     eax, ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7263DC7A(self):
		#sub_7263DC7A
		gadget = "8BFF558BEC8B4508568B7004578B7D0C83C648A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#push    esi
		#mov     esi, [eax+4]
		#push    edi
		#mov     edi, [ebp+arg_4]
		#add     esi, 48h
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7263DC9E(self):
		#sub_7263DC9E
		gadget = "B800000400C20C00"
		self.do(gadget)

		#mov     eax, 40000h
		#retn    0Ch


  def test_gadget_sub_7263E809(self):
		#sub_7263E809
		gadget = "8BFF558BEC8B45088B400433C93988E80000000F95C18BC15DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+4]
		#xor     ecx, ecx
		#cmp     [eax+0E8h], ecx
		#setnz   cl
		#mov     eax, ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7263EEC9(self):
		#sub_7263EEC9
		gadget = "B8ED010480C21400"
		self.do(gadget)

		#mov     eax, 800401EDh
		#retn    14h


  def test_gadget_sub_7264058F(self):
		#sub_7264058F
		gadget = "8BFF558BEC8BC18B4D08C7400440DE5772C74008B0DD577283600C00C7003C255872C7400478F15772C7400804AF59728948105DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax+4], offset off_7257DE40
		#mov     dword ptr [eax+8], offset off_7257DDB0
		#and     dword ptr [eax+0Ch], 0
		#mov     dword ptr [eax], offset off_7258253C
		#mov     dword ptr [eax+4], offset off_7257F178
		#mov     dword ptr [eax+8], offset off_7259AF04
		#mov     [eax+10h], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_726405CB(self):
		#sub_726405CB
		gadget = "B801400080C21000"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    10h


  def test_gadget_sub_726424DE(self):
		#sub_726424DE
		gadget = "8BFF558BEC668B4D0833C0663B0DA48868720F94C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     cx, [ebp+arg_0]
		#xor     eax, eax
		#cmp     cx, word_726888A4
		#setz    al
		#pop     ebp
		#retn    4


  def test_gadget_sub_72643473(self):
		#sub_72643473
		gadget = "8BFF558BEC8B4D088B4104FF40448B41048B40445DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     eax, [ecx+4]
		#inc     dword ptr [eax+44h]
		#mov     eax, [ecx+4]
		#mov     eax, [eax+44h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_726437BB(self):
		#sub_726437BB
		gadget = "8BFF558BEC8BC18B4D08C7400440DE5772C74008B0DD577283601000C7003C255872C7400478F15772C7400804AF597289480C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     dword ptr [eax+4], offset off_7257DE40
		#mov     dword ptr [eax+8], offset off_7257DDB0
		#and     dword ptr [eax+10h], 0
		#mov     dword ptr [eax], offset off_7258253C
		#mov     dword ptr [eax+4], offset off_7257F178
		#mov     dword ptr [eax+8], offset off_7259AF04
		#mov     [eax+0Ch], ecx
		#pop     ebp
		#retn    4


  def test_gadget_sub_7264484A(self):
		#sub_7264484A
		gadget = "B801400080C20400"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    4


  def test_gadget_nullsub_17(self):
		#nullsub_17
		gadget = "C20C00"
		self.do(gadget)

		#retn    0Ch


  def test_gadget_sub_72644A79(self):
		#sub_72644A79
		gadget = "8BFF558BEC8B4508FF40048B40045DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+4]
		#mov     eax, [eax+4]
		#pop     ebp
		#retn    4


  def test_gadget_sub_72644C3D(self):
		#sub_72644C3D
		gadget = "33C0C21800"
		self.do(gadget)

		#xor     eax, eax
		#retn    18h


  def test_gadget_sub_7264652C(self):
		#sub_7264652C
		gadget = "8BFF558BEC8B4518832000B8030004805DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_10]
		#and     dword ptr [eax], 0
		#mov     eax, 80040003h
		#pop     ebp
		#retn    14h


  def test_gadget_sub_72646545(self):
		#sub_72646545
		gadget = "B804000480C20800"
		self.do(gadget)

		#mov     eax, 80040004h
		#retn    8


  def test_gadget_sub_72646552(self):
		#sub_72646552
		gadget = "8BFF558BEC8B450C832000B8030004805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#mov     eax, 80040003h
		#pop     ebp
		#retn    8


  def test_gadget_sub_72648774(self):
		#sub_72648774
		gadget = "8BFF558BEC8B450C8B50208B4D088951148B50248951188B502889511C668B106689118B50088951048B50108951088B501489510C8B40188941105DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#mov     edx, [eax+20h]
		#mov     ecx, [ebp+arg_0]
		#mov     [ecx+14h], edx
		#mov     edx, [eax+24h]
		#mov     [ecx+18h], edx
		#mov     edx, [eax+28h]
		#mov     [ecx+1Ch], edx
		#mov     dx, [eax]
		#mov     [ecx], dx
		#mov     edx, [eax+8]
		#mov     [ecx+4], edx
		#mov     edx, [eax+10h]
		#mov     [ecx+8], edx
		#mov     edx, [eax+14h]
		#mov     [ecx+0Ch], edx
		#mov     eax, [eax+18h]
		#mov     [ecx+10h], eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72649281(self):
		#sub_72649281
		gadget = "8BFF558BEC8B4508FF40088B40085DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#inc     dword ptr [eax+8]
		#mov     eax, [eax+8]
		#pop     ebp
		#retn    4


  def test_gadget_sub_7264A018(self):
		#sub_7264A018
		gadget = "8BFF558BEC8B4510832000B8FFFF00805DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#mov     eax, 8000FFFFh
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7264A031(self):
		#sub_7264A031
		gadget = "B8FFFF0080C21800"
		self.do(gadget)

		#mov     eax, 8000FFFFh
		#retn    18h


  def test_gadget_sub_7264A532(self):
		#sub_7264A532
		gadget = "8BFF558BEC8BC18B4D0C8948048B4D088948088B4D188948188B4D1089480C8B4D14C70070005D72C74010010000008948145DC21400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+4], ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_10]
		#mov     [eax+18h], ecx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [ebp+arg_C]
		#mov     dword ptr [eax], offset off_725D0070
		#mov     dword ptr [eax+10h], 1
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    14h


  def test_gadget_sub_7264ACB8(self):
		#sub_7264ACB8
		gadget = "8BFF558BEC8BC18B4D0883600C00836010008948088B4D0CC700189E5F72C74004010000008948145DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+0Ch], 0
		#and     dword ptr [eax+10h], 0
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     dword ptr [eax], offset off_725F9E18
		#mov     dword ptr [eax+4], 1
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7264C118(self):
		#sub_7264C118
		gadget = "8BFF558BEC8B45088360100033C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [eax+10h], 0
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7264C8DA(self):
		#sub_7264C8DA
		gadget = "8BFF558BEC8BC18B4D0883602C008948088B4D108948108B4D0CC70008C96472C740040100000089480C5DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#and     dword ptr [eax+2Ch], 0
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_8]
		#mov     [eax+10h], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     dword ptr [eax], offset off_7264C908
		#mov     dword ptr [eax+4], 1
		#mov     [eax+0Ch], ecx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7264DA62(self):
		#sub_7264DA62
		gadget = "8BFF558BEC8B4D0833C03941280F94C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#xor     eax, eax
		#cmp     [ecx+28h], eax
		#setz    al
		#pop     ebp
		#retn    4


  def test_gadget_sub_7264E3CB(self):
		#sub_7264E3CB
		gadget = "8BFF558BEC8B550C8BC133C98950248B5508C70028EC5872C740040100000089480889482889503489482089481C89482C89483089480C8948108948145DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     edx, [ebp+arg_4]
		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+24h], edx
		#mov     edx, [ebp+arg_0]
		#mov     dword ptr [eax], offset off_7258EC28
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+28h], ecx
		#mov     [eax+34h], edx
		#mov     [eax+20h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+2Ch], ecx
		#mov     [eax+30h], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_7264FF68(self):
		#sub_7264FF68
		gadget = "8BC133C989480889481089480C894814890866894804C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     [eax+8], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], ecx
		#mov     [eax], ecx
		#mov     [eax+4], cx
		#retn


  def test_gadget_sub_7264FF84(self):
		#sub_7264FF84
		gadget = "8BFF56578BC183601000BEA49A58728BF8A5A5A5A55F5EC3"
		self.do(gadget)

		#mov     edi, edi
		#push    esi
		#push    edi
		#mov     eax, ecx
		#and     dword ptr [eax+10h], 0
		#mov     esi, offset stru_72589AA4
		#mov     edi, eax
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#pop     esi
		#retn


  def test_gadget_sub_72654F94(self):
		#sub_72654F94
		gadget = "B8FE000380C21800"
		self.do(gadget)

		#mov     eax, 800300FEh
		#retn    18h


  def test_gadget_sub_72655185(self):
		#sub_72655185
		gadget = "8B411883A03C02000000C3"
		self.do(gadget)

		#mov     eax, [ecx+18h]
		#and     dword ptr [eax+23Ch], 0
		#retn


  def test_gadget_sub_72656878(self):
		#sub_72656878
		gadget = "B801000380C21000"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    10h


  def test_gadget_sub_72656F7B(self):
		#sub_72656F7B
		gadget = "8BFF558BEC56578B7D0CBE60F25872A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_7258F260
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7265796A(self):
		#sub_7265796A
		gadget = "B801000380C21C00"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    1Ch


  def test_gadget_sub_72657977(self):
		#sub_72657977
		gadget = "B801000380C21400"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    14h


  def test_gadget_sub_72657984(self):
		#sub_72657984
		gadget = "B801000380C20C00"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    0Ch


  def test_gadget_sub_72657A2A(self):
		#sub_72657A2A
		gadget = "B801000380C20800"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    8


  def test_gadget_sub_72657B6A(self):
		#sub_72657B6A
		gadget = "8BC133C9C7002CA15F72C7400408A15F7289480889480C894814894818C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_725FA12C
		#mov     dword ptr [eax+4], offset off_725FA108
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#retn


  def test_gadget_sub_72657E06(self):
		#sub_72657E06
		gadget = "8BFF558BEC8BC18B4D088948088B4D0CC70064A15F72C740040100000089480C5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+8], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     dword ptr [eax], offset off_725FA164
		#mov     dword ptr [eax+4], 1
		#mov     [eax+0Ch], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_726584AE(self):
		#sub_726584AE
		gadget = "B8FE000380C20800"
		self.do(gadget)

		#mov     eax, 800300FEh
		#retn    8


  def test_gadget_sub_726584BB(self):
		#sub_726584BB
		gadget = "B801000380C20400"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    4


  def test_gadget_sub_72658859(self):
		#sub_72658859
		gadget = "8BFF558BEC8B45088B480889480C33C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+8]
		#mov     [eax+0Ch], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7265BCB6(self):
		#sub_7265BCB6
		gadget = "B801400080C21C00"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    1Ch


  def test_gadget_sub_7265BCC3(self):
		#sub_7265BCC3
		gadget = "B801400080C21400"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    14h


  def test_gadget_sub_7265FDDC(self):
		#sub_7265FDDC
		gadget = "B801400080C21800"
		self.do(gadget)

		#mov     eax, 80004001h
		#retn    18h


  def test_gadget_sub_72660E05(self):
		#sub_72660E05
		gadget = "8BFF558BEC8B450883C00A5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#add     eax, 0Ah
		#pop     ebp
		#retn    4


  def test_gadget_sub_726617C4(self):
		#sub_726617C4
		gadget = "8BFF558BEC8B45088B400C8B4D1089015DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0Ch]
		#mov     ecx, [ebp+arg_8]
		#mov     [ecx], eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_726617DD(self):
		#sub_726617DD
		gadget = "8BFF558BEC8B45108320005DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_72661A0C(self):
		#sub_72661A0C
		gadget = "8BFF558BEC8B4508C7401C010000008B450C8320005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     dword ptr [eax+1Ch], 1
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#pop     ebp
		#retn    8


  def test_gadget_sub_72661A2A(self):
		#sub_72661A2A
		gadget = "8BFF558BEC8B45088A401C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     al, [eax+1Ch]
		#pop     ebp
		#retn    4


  def test_gadget_sub_72661BA6(self):
		#sub_72661BA6
		gadget = "836108E533C089410C8941108941148941186689411E6689411CC3"
		self.do(gadget)

		#and     dword ptr [ecx+8], 0FFFFFFE5h
		#xor     eax, eax
		#mov     [ecx+0Ch], eax
		#mov     [ecx+10h], eax
		#mov     [ecx+14h], eax
		#mov     [ecx+18h], eax
		#mov     [ecx+1Eh], ax
		#mov     [ecx+1Ch], ax
		#retn


  def test_gadget_sub_72661BC6(self):
		#sub_72661BC6
		gadget = "8BFF558BEC8B45088B4008C1E01EC1F81F5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+8]
		#shl     eax, 1Eh
		#sar     eax, 1Fh
		#pop     ebp
		#retn    4


  def test_gadget_sub_726636C5(self):
		#sub_726636C5
		gadget = "64A1180000008B40308B80D80100002500020000C3"
		self.do(gadget)

		#mov     eax, large fs:18h
		#mov     eax, [eax+30h]
		#mov     eax, [eax+1D8h]
		#and     eax, 200h
		#retn


  def test_gadget_sub_72663D85(self):
		#sub_72663D85
		gadget = "8BC133C9C7007CE25572C740080100000089480489480C894810894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7255E27C
		#mov     dword ptr [eax+8], 1
		#mov     [eax+4], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_72664005(self):
		#sub_72664005
		gadget = "8BFF558BEC8B45088B480C8B550C890A8B40148B4D10890133C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+0Ch]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+14h]
		#mov     ecx, [ebp+arg_8]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7266639F(self):
		#sub_7266639F
		gadget = "8BFF558BEC8B4508836010008360180033C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [eax+10h], 0
		#and     dword ptr [eax+18h], 0
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_726663BA(self):
		#sub_726663BA
		gadget = "8BFF558BEC8B450889410C8B450C89410833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     [ecx+0Ch], eax
		#mov     eax, [ebp+arg_4]
		#mov     [ecx+8], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72666816(self):
		#sub_72666816
		gadget = "8BC133C9C7008CEC587289480489480C89481489480889481089481889481CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7258EC8C
		#mov     [eax+4], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+8], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn


  def test_gadget_sub_7266692E(self):
		#sub_7266692E
		gadget = "8BC133C9C700C052587289481889480489480889480C894810894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_725852C0
		#mov     [eax+18h], ecx
		#mov     [eax+4], ecx
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_7266742B(self):
		#sub_7266742B
		gadget = "8BC133C9C700C4EC5872C740040100000089480889481089480C894814C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7258ECC4
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+14h], ecx
		#retn


  def test_gadget_sub_72668FD5(self):
		#sub_72668FD5
		gadget = "8BFF558BEC8B450C8320005DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#and     dword ptr [eax], 0
		#pop     ebp
		#retn    8


  def test_gadget_sub_726697A3(self):
		#sub_726697A3
		gadget = "8BFF558BEC836D086D8B4508560FB7711C33D2F7F68B550C5E89020FB7491C8B450833D2F7F18B45106689105DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#sub     [ebp+arg_0], 6Dh
		#mov     eax, [ebp+arg_0]
		#push    esi
		#movzx   esi, word ptr [ecx+1Ch]
		#xor     edx, edx
		#div     esi
		#mov     edx, [ebp+arg_4]
		#pop     esi
		#mov     [edx], eax
		#movzx   ecx, word ptr [ecx+1Ch]
		#mov     eax, [ebp+arg_0]
		#xor     edx, edx
		#div     ecx
		#mov     eax, [ebp+arg_8]
		#mov     [eax], dx
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7266A535(self):
		#sub_7266A535
		gadget = "C7010D0000C0C3"
		self.do(gadget)

		#mov     dword ptr [ecx], 0C000000Dh
		#retn


  def test_gadget_sub_7266C820(self):
		#sub_7266C820
		gadget = "B801000380C21800"
		self.do(gadget)

		#mov     eax, 80030001h
		#retn    18h


  def test_gadget_sub_7266C86A(self):
		#sub_7266C86A
		gadget = "8BFF558BEC8B45088B4D0C89481C33C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+1Ch], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CA3F(self):
		#sub_7266CA3F
		gadget = "8BFF558BEC8B45088B4D0C89481833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+18h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CA58(self):
		#sub_7266CA58
		gadget = "8BFF558BEC8B45088B401C8B40088B008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     eax, [eax+8]
		#mov     eax, [eax]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CA78(self):
		#sub_7266CA78
		gadget = "8BFF558BEC8B45088B401C8B40088B40048B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     eax, [eax+8]
		#mov     eax, [eax+4]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CA99(self):
		#sub_7266CA99
		gadget = "8BFF558BEC8B45088B401C8B40088B400C8B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     eax, [eax+8]
		#mov     eax, [eax+0Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CABA(self):
		#sub_7266CABA
		gadget = "8BFF558BEC8B45088B401C8B40088B40108B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     eax, [eax+8]
		#mov     eax, [eax+10h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CADB(self):
		#sub_7266CADB
		gadget = "8BFF558BEC8B45088B401C8B40088B40188B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     eax, [eax+8]
		#mov     eax, [eax+18h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CAFC(self):
		#sub_7266CAFC
		gadget = "8BFF558BEC8B45088B401C8B4D0C89480833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+8], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CBA8(self):
		#sub_7266CBA8
		gadget = "8BFF558BEC8B450833C989481489481889480C33C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#xor     ecx, ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+0Ch], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7266CC5E(self):
		#sub_7266CC5E
		gadget = "8BFF558BEC8B450833C989481889481489480C33C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#xor     ecx, ecx
		#mov     [eax+18h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+0Ch], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7266CCCA(self):
		#sub_7266CCCA
		gadget = "8BFF558BEC8B45088B48148B550C890A8B40188B4D10890133C05DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [eax+14h]
		#mov     edx, [ebp+arg_4]
		#mov     [edx], ecx
		#mov     eax, [eax+18h]
		#mov     ecx, [ebp+arg_8]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7266CD56(self):
		#sub_7266CD56
		gadget = "8BFF558BEC8B45088B40208B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+20h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CD71(self):
		#sub_7266CD71
		gadget = "8BFF558BEC8B4508568B750C57C74024010000008D782CA5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#push    esi
		#mov     esi, [ebp+arg_4]
		#push    edi
		#mov     dword ptr [eax+24h], 1
		#lea     edi, [eax+2Ch]
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CD99(self):
		#sub_7266CD99
		gadget = "8BFF558BEC8B45088B4D0C89483C33C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+3Ch], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CDB2(self):
		#sub_7266CDB2
		gadget = "8BFF558BEC8B45088B403C8B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+3Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CE4A(self):
		#sub_7266CE4A
		gadget = "8BFF558BEC8B45088B404423450CF7D81BC025FBBFFF7F05054000805DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+44h]
		#and     eax, [ebp+arg_4]
		#neg     eax
		#sbb     eax, eax
		#and     eax, 7FFFBFFBh
		#add     eax, 80004005h
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CE6F(self):
		#sub_7266CE6F
		gadget = "8BFF558BEC8B45088B4D0C09484433C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#or      [eax+44h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CE88(self):
		#sub_7266CE88
		gadget = "8BFF558BEC8B4D0C8B4508F7D121484433C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_4]
		#mov     eax, [ebp+arg_0]
		#not     ecx
		#and     [eax+44h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CEA3(self):
		#sub_7266CEA3
		gadget = "8BFF558BEC8B45088B4D0C8348440489484833C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#or      dword ptr [eax+44h], 4
		#mov     [eax+48h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266CEF6(self):
		#sub_7266CEF6
		gadget = "8BFF558BEC8B4508836044FB8360480033C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [eax+44h], 0FFFFFFFBh
		#and     dword ptr [eax+48h], 0
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7266CFBD(self):
		#sub_7266CFBD
		gadget = "8BFF558BEC56578B7D0CBEA49A5872A5A5A5A55FB8014000805E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset stru_72589AA4
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#mov     eax, 80004001h
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266D07C(self):
		#sub_7266D07C
		gadget = "8BFF558BEC8B4510832000B8024000805DC20C00"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_8]
		#and     dword ptr [eax], 0
		#mov     eax, 80004002h
		#pop     ebp
		#retn    0Ch


  def test_gadget_sub_7266D1AE(self):
		#sub_7266D1AE
		gadget = "8BC133C9C74004D426587289480889480C894810C700AC3F5872C74004F8A45F7289481489481889481CC3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax+4], offset off_725826D4
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     dword ptr [eax], offset off_72583FAC
		#mov     dword ptr [eax+4], offset off_725FA4F8
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#retn


  def test_gadget_sub_7266D1DE(self):
		#sub_7266D1DE
		gadget = "8BFF558BEC8B45088B808C0000008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+8Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266D1FC(self):
		#sub_7266D1FC
		gadget = "8BFF558BEC8B45088B4D0C8988A001000033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     ecx, [ebp+arg_4]
		#mov     [eax+1A0h], ecx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266D218(self):
		#sub_7266D218
		gadget = "8BFF558BEC8B45088B80A00100008B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+1A0h]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266D299(self):
		#sub_7266D299
		gadget = "8BFF558BEC568B750C578B7D0883C71CA5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#mov     esi, [ebp+arg_4]
		#push    edi
		#mov     edi, [ebp+arg_0]
		#add     edi, 1Ch
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266DCB2(self):
		#sub_7266DCB2
		gadget = "8BFF558BEC8B45088B8094FEFFFF8B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax-16Ch]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266DCD0(self):
		#sub_7266DCD0
		gadget = "8BFF558BEC8B45088B40088B4D0C890133C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+8]
		#mov     ecx, [ebp+arg_4]
		#mov     [ecx], eax
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266DE5A(self):
		#sub_7266DE5A
		gadget = "8BFF558BEC8B41348B550889028B4158836134008B550C89028361580033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ecx+34h]
		#mov     edx, [ebp+arg_0]
		#mov     [edx], eax
		#mov     eax, [ecx+58h]
		#and     dword ptr [ecx+34h], 0
		#mov     edx, [ebp+arg_4]
		#mov     [edx], eax
		#and     dword ptr [ecx+58h], 0
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266E7AC(self):
		#sub_7266E7AC
		gadget = "8BFF558BEC8B45088360080033C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [eax+8], 0
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266E851(self):
		#sub_7266E851
		gadget = "8BFF558BEC56578B7D0CBE48255772A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_72572548
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


  def test_gadget_sub_7266F1CD(self):
		#sub_7266F1CD
		gadget = "8BFF558BEC8B45088360080033C05DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#and     dword ptr [eax+8], 0
		#xor     eax, eax
		#pop     ebp
		#retn    4


  def test_gadget_sub_7266F24C(self):
		#sub_7266F24C
		gadget = "8BC133C9C700FCEC5872C740040100000089480889480C894810C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7258ECFC
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#retn


  def test_gadget_sub_7266F6AA(self):
		#sub_7266F6AA
		gadget = "8BFF558BEC8B450C6A05596689086A07596689480233C05DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_4]
		#push    5
		#pop     ecx
		#mov     [eax], cx
		#push    7
		#pop     ecx
		#mov     [eax+2], cx
		#xor     eax, eax
		#pop     ebp
		#retn    8


  def test_gadget_sub_72670085(self):
		#sub_72670085
		gadget = "8BFF558BEC8B45088B400C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, [ebp+arg_0]
		#mov     eax, [eax+0Ch]
		#pop     ebp
		#retn    4


  def test_gadget_sub_72670099(self):
		#sub_72670099
		gadget = "8BFF558BEC8B4D088B41188B511C5DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     eax, [ecx+18h]
		#mov     edx, [ecx+1Ch]
		#pop     ebp
		#retn    4


  def test_gadget_sub_726700B0(self):
		#sub_726700B0
		gadget = "8BFF558BEC8B4D088B41108B51145DC20400"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     ecx, [ebp+arg_0]
		#mov     eax, [ecx+10h]
		#mov     edx, [ecx+14h]
		#pop     ebp
		#retn    4


  def test_gadget_sub_72670146(self):
		#sub_72670146
		gadget = "8BFF558BEC8BC18B4D0889480C8B4D0CC70030ED5872C74004010000008948085DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#mov     eax, ecx
		#mov     ecx, [ebp+arg_0]
		#mov     [eax+0Ch], ecx
		#mov     ecx, [ebp+arg_4]
		#mov     dword ptr [eax], offset off_7258ED30
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#pop     ebp
		#retn    8


  def test_gadget_sub_726701A3(self):
		#sub_726701A3
		gadget = "8BC133C9C70048ED5872C740040100000089480889480C89481089481489481889481C894820C3"
		self.do(gadget)

		#mov     eax, ecx
		#xor     ecx, ecx
		#mov     dword ptr [eax], offset off_7258ED48
		#mov     dword ptr [eax+4], 1
		#mov     [eax+8], ecx
		#mov     [eax+0Ch], ecx
		#mov     [eax+10h], ecx
		#mov     [eax+14h], ecx
		#mov     [eax+18h], ecx
		#mov     [eax+1Ch], ecx
		#mov     [eax+20h], ecx
		#retn


  def test_gadget_sub_726735E1(self):
		#sub_726735E1
		gadget = "8BFF558BEC56578B7D0CBE48575672A5A5A5A55F33C05E5DC20800"
		self.do(gadget)

		#mov     edi, edi
		#push    ebp
		#mov     ebp, esp
		#push    esi
		#push    edi
		#mov     edi, [ebp+arg_4]
		#mov     esi, offset dword_72565748
		#movsd
		#movsd
		#movsd
		#movsd
		#pop     edi
		#xor     eax, eax
		#pop     esi
		#pop     ebp
		#retn    8


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()
