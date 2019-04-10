import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetsqmapidll(unittest.TestCase):
    
  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x86")



  def test_gadget_sub_10001165(self):
        #sub_10001165
        gadget = "8BFF558BEC8B450833D2898134080000891189510489510889510C89911008000089911408000089911808000089911C08000089912008000089912408000089912808000089912C08000089913008000089913808000089913C0800008991400800008991440800008BC15DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #xor     edx, edx
        #mov     [ecx+834h], eax
        #mov     [ecx], edx
        #mov     [ecx+4], edx
        #mov     [ecx+8], edx
        #mov     [ecx+0Ch], edx
        #mov     [ecx+810h], edx
        #mov     [ecx+814h], edx
        #mov     [ecx+818h], edx
        #mov     [ecx+81Ch], edx
        #mov     [ecx+820h], edx
        #mov     [ecx+824h], edx
        #mov     [ecx+828h], edx
        #mov     [ecx+82Ch], edx
        #mov     [ecx+830h], edx
        #mov     [ecx+838h], edx
        #mov     [ecx+83Ch], edx
        #mov     [ecx+840h], edx
        #mov     [ecx+844h], edx
        #mov     eax, ecx
        #pop     ebp
        #retn    4


  def test_gadget___SEH_prolog4(self):
        #__SEH_prolog4
        gadget = "68C1B8021064FF35000000008B442410896C24108D6C24102BE0535657A1382103103145FC33C5508965E8FF75F88B45FCC745FCFEFFFFFF8945F88D45F064A300000000C3"
        self.do(gadget)

        #push    offset sub_1002B8C1
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


  def test_gadget_sub_10001789(self):
        #sub_10001789
        gadget = "C705C4200310FFFFFFFFC3"
        self.do(gadget)

        #mov     dword_100320C4, 0FFFFFFFFh
        #retn


  def test_gadget_sub_100031D9(self):
        #sub_100031D9
        gadget = "8BFF558BEC8B45088941345DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+34h], eax
        #pop     ebp
        #retn    4


  def test_gadget___EH_prolog3(self):
        #__EH_prolog3
        gadget = "8BC05064FF35000000008D44240C2B64240C53565789288BE8A13821031033C550FF75FCC745FCFFFFFFFF8D45F464A300000000C3"
        self.do(gadget)

        #mov     eax, eax
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
        gadget = "8BC05064FF35000000008D44240C2B64240C53565789288BE8A13821031033C5508965F0FF75FCC745FCFFFFFFFF8D45F464A300000000C3"
        self.do(gadget)

        #mov     eax, eax
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


  def test_gadget_sub_1000476F(self):
        #sub_1000476F
        gadget = "8B01C3"
        self.do(gadget)

        #mov     eax, [ecx]
        #retn


  def test_gadget_sub_10004F6B(self):
        #sub_10004F6B
        gadget = "33C089018941088941048BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     [ecx], eax
        #mov     [ecx+8], eax
        #mov     [ecx+4], eax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_100058B2(self):
        #sub_100058B2
        gadget = "8B4108C3"
        self.do(gadget)

        #mov     eax, [ecx+8]
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


  def test_gadget_sub_10005BDD(self):
        #sub_10005BDD
        gadget = "33C0C701FC5B0010834918FF89410489410889410C8941108941148BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     dword ptr [ecx], offset off_10005BFC
        #or      dword ptr [ecx+18h], 0FFFFFFFFh
        #mov     [ecx+4], eax
        #mov     [ecx+8], eax
        #mov     [ecx+0Ch], eax
        #mov     [ecx+10h], eax
        #mov     [ecx+14h], eax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_1000765E(self):
        #sub_1000765E
        gadget = "5351BBAC2403108B4C240C894B08894304896B0C55515058595D595BC20400"
        self.do(gadget)

        #push    ebx
        #push    ecx
        #mov     ebx, offset unk_100324AC
        #mov     ecx, [esp+8+arg_0]
        #mov     [ebx+8], ecx
        #mov     [ebx+4], eax
        #mov     [ebx+0Ch], ebp
        #push    ebp
        #push    ecx
        #push    eax
        #pop     eax
        #pop     ecx
        #pop     ebp
        #pop     ecx
        #pop     ebx
        #retn    4


  def test_gadget_sub_1000BAAF(self):
        #sub_1000BAAF
        gadget = "8B65E833F68975E4"
        self.do(gadget)

        #mov     esp, [ebp-18h]
        #xor     esi, esi
        #mov     [ebp-1Ch], esi


  def test_gadget_sub_1000BB28(self):
        #sub_1000BB28
        gadget = "8B65E833F6"
        self.do(gadget)

        #mov     esp, [ebp-18h]
        #xor     esi, esi


  def test_gadget_sub_1000BB57(self):
        #sub_1000BB57
        gadget = "8B65E833F6"
        self.do(gadget)

        #mov     esp, [ebp-18h]
        #xor     esi, esi


  def test_gadget_sub_1000BB90(self):
        #sub_1000BB90
        gadget = "8B65E833F6"
        self.do(gadget)

        #mov     esp, [ebp-18h]
        #xor     esi, esi


  def test_gadget_sub_1000BBF6(self):
        #sub_1000BBF6
        gadget = "8B65E833F68975E4"
        self.do(gadget)

        #mov     esp, [ebp-18h]
        #xor     esi, esi
        #mov     [ebp-1Ch], esi


  def test_gadget_sub_1000DBF7(self):
        #sub_1000DBF7
        gadget = "33C0890189410489410889410C89411089411489411889411C8941208BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     [ecx], eax
        #mov     [ecx+4], eax
        #mov     [ecx+8], eax
        #mov     [ecx+0Ch], eax
        #mov     [ecx+10h], eax
        #mov     [ecx+14h], eax
        #mov     [ecx+18h], eax
        #mov     [ecx+1Ch], eax
        #mov     [ecx+20h], eax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_1000F448(self):
        #sub_1000F448
        gadget = "33C0C70134C40010834918FF89410489410889410C8941108941148BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     dword ptr [ecx], offset off_1000C434
        #or      dword ptr [ecx+18h], 0FFFFFFFFh
        #mov     [ecx+4], eax
        #mov     [ecx+8], eax
        #mov     [ecx+0Ch], eax
        #mov     [ecx+10h], eax
        #mov     [ecx+14h], eax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_1000F4A9(self):
        #sub_1000F4A9
        gadget = "8B410CC3"
        self.do(gadget)

        #mov     eax, [ecx+0Ch]
        #retn


  def test_gadget_sub_1000FA75(self):
        #sub_1000FA75
        gadget = "8B4164C3"
        self.do(gadget)

        #mov     eax, [ecx+64h]
        #retn


  def test_gadget_sub_100113AA(self):
        #sub_100113AA
        gadget = "8BFF558BEC8B450889412C5DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+2Ch], eax
        #pop     ebp
        #retn    4


  def test_gadget_sub_10011711(self):
        #sub_10011711
        gadget = "33C0C7017CC50010834918FF89410489410889410C8941108941148BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     dword ptr [ecx], offset off_1000C57C
        #or      dword ptr [ecx+18h], 0FFFFFFFFh
        #mov     [ecx+4], eax
        #mov     [ecx+8], eax
        #mov     [ecx+0Ch], eax
        #mov     [ecx+10h], eax
        #mov     [ecx+14h], eax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_10012412(self):
        #sub_10012412
        gadget = "8B4140C3"
        self.do(gadget)

        #mov     eax, [ecx+40h]
        #retn


  def test_gadget_sub_1001241B(self):
        #sub_1001241B
        gadget = "8B4144C3"
        self.do(gadget)

        #mov     eax, [ecx+44h]
        #retn


  def test_gadget_sub_10012424(self):
        #sub_10012424
        gadget = "668B4148C3"
        self.do(gadget)

        #mov     ax, [ecx+48h]
        #retn


  def test_gadget_sub_1001242E(self):
        #sub_1001242E
        gadget = "8B414CC3"
        self.do(gadget)

        #mov     eax, [ecx+4Ch]
        #retn


  def test_gadget_sub_1001479C(self):
        #sub_1001479C
        gadget = "C70150C60010C3"
        self.do(gadget)

        #mov     dword ptr [ecx], offset off_1000C650
        #retn


  def test_gadget_sub_1001484A(self):
        #sub_1001484A
        gadget = "8D4110C3"
        self.do(gadget)

        #lea     eax, [ecx+10h]
        #retn


  def test_gadget_sub_10014F45(self):
        #sub_10014F45
        gadget = "33C0890189410489818800000089818C000000898190000000898194000000898198000000668941088BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     [ecx], eax
        #mov     [ecx+4], eax
        #mov     [ecx+88h], eax
        #mov     [ecx+8Ch], eax
        #mov     [ecx+90h], eax
        #mov     [ecx+94h], eax
        #mov     [ecx+98h], eax
        #mov     [ecx+8], ax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_1001B8D0(self):
        #sub_1001B8D0
        gadget = "33C089410889410C894104894114894110C70104BF00108BC1C3"
        self.do(gadget)

        #xor     eax, eax
        #mov     [ecx+8], eax
        #mov     [ecx+0Ch], eax
        #mov     [ecx+4], eax
        #mov     [ecx+14h], eax
        #mov     [ecx+10h], eax
        #mov     dword ptr [ecx], offset off_1000BF04
        #mov     eax, ecx
        #retn


  def test_gadget_sub_1001BBE3(self):
        #sub_1001BBE3
        gadget = "8B410833D2C3"
        self.do(gadget)

        #mov     eax, [ecx+8]
        #xor     edx, edx
        #retn


  def test_gadget_sub_1001BC43(self):
        #sub_1001BC43
        gadget = "834904FFC70120BF00108BC1C3"
        self.do(gadget)

        #or      dword ptr [ecx+4], 0FFFFFFFFh
        #mov     dword ptr [ecx], offset off_1000BF20
        #mov     eax, ecx
        #retn


  def test_gadget_sub_1001BF3D(self):
        #sub_1001BF3D
        gadget = "8BFF558BEC8B4508836114008941048B450C8941088B451089410C8B4514894110C70144BF00108BC15DC21000"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #and     dword ptr [ecx+14h], 0
        #mov     [ecx+4], eax
        #mov     eax, [ebp+arg_4]
        #mov     [ecx+8], eax
        #mov     eax, [ebp+arg_8]
        #mov     [ecx+0Ch], eax
        #mov     eax, [ebp+arg_C]
        #mov     [ecx+10h], eax
        #mov     dword ptr [ecx], offset off_1000BF44
        #mov     eax, ecx
        #pop     ebp
        #retn    10h


  def test_gadget_sub_1001C07F(self):
        #sub_1001C07F
        gadget = "B801400080C20800"
        self.do(gadget)

        #mov     eax, 80004001h
        #retn    8


  def test_gadget_sub_1001C119(self):
        #sub_1001C119
        gadget = "C701E8BE0010C3"
        self.do(gadget)

        #mov     dword ptr [ecx], offset off_1000BEE8
        #retn


  def test_gadget_sub_1001C150(self):
        #sub_1001C150
        gadget = "83610400C3"
        self.do(gadget)

        #and     dword ptr [ecx+4], 0
        #retn


  def test_gadget_sub_1001C1D3(self):
        #sub_1001C1D3
        gadget = "B801400080C21000"
        self.do(gadget)

        #mov     eax, 80004001h
        #retn    10h


  def test_gadget_sub_1001C2F6(self):
        #sub_1001C2F6
        gadget = "8BFF558BEC8B4508894104C70160BF0010C74108010000008BC15DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+4], eax
        #mov     dword ptr [ecx], offset off_1000BF60
        #mov     dword ptr [ecx+8], 1
        #mov     eax, ecx
        #pop     ebp
        #retn    4


  def test_gadget_sub_1001C319(self):
        #sub_1001C319
        gadget = "C70160BF0010C3"
        self.do(gadget)

        #mov     dword ptr [ecx], offset off_1000BF60
        #retn


  def test_gadget_sub_1001E36C(self):
        #sub_1001E36C
        gadget = "8B81E8020000C3"
        self.do(gadget)

        #mov     eax, [ecx+2E8h]
        #retn


  def test_gadget_sub_1001E3AC(self):
        #sub_1001E3AC
        gadget = "8B81EC020000C3"
        self.do(gadget)

        #mov     eax, [ecx+2ECh]
        #retn


  def test_gadget_sub_1001E3B8(self):
        #sub_1001E3B8
        gadget = "8B81F0020000C3"
        self.do(gadget)

        #mov     eax, [ecx+2F0h]
        #retn


  def test_gadget_sub_1001E58B(self):
        #sub_1001E58B
        gadget = "8BFF558BEC8B45088981B80000005DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+0B8h], eax
        #pop     ebp
        #retn    4


  def test_gadget_sub_1001E5A2(self):
        #sub_1001E5A2
        gadget = "8B81BC000000C3"
        self.do(gadget)

        #mov     eax, [ecx+0BCh]
        #retn


  def test_gadget_sub_1001E5AE(self):
        #sub_1001E5AE
        gadget = "8B81C0000000C3"
        self.do(gadget)

        #mov     eax, [ecx+0C0h]
        #retn


  def test_gadget_sub_1001E5BA(self):
        #sub_1001E5BA
        gadget = "8B81C8000000C3"
        self.do(gadget)

        #mov     eax, [ecx+0C8h]
        #retn


  def test_gadget_sub_1001E5C6(self):
        #sub_1001E5C6
        gadget = "8B81CC000000C3"
        self.do(gadget)

        #mov     eax, [ecx+0CCh]
        #retn


  def test_gadget_sub_1001E5D2(self):
        #sub_1001E5D2
        gadget = "8B81E4020000C3"
        self.do(gadget)

        #mov     eax, [ecx+2E4h]
        #retn


  def test_gadget_sub_1001F5E3(self):
        #sub_1001F5E3
        gadget = "834914FF33C0890189410489410889410C8941108941188BC1C3"
        self.do(gadget)

        #or      dword ptr [ecx+14h], 0FFFFFFFFh
        #xor     eax, eax
        #mov     [ecx], eax
        #mov     [ecx+4], eax
        #mov     [ecx+8], eax
        #mov     [ecx+0Ch], eax
        #mov     [ecx+10h], eax
        #mov     [ecx+18h], eax
        #mov     eax, ecx
        #retn


  def test_gadget_sub_100253E9(self):
        #sub_100253E9
        gadget = "33C0C20800"
        self.do(gadget)

        #xor     eax, eax
        #retn    8


  def test_gadget_sub_1002545E(self):
        #sub_1002545E
        gadget = "33C0C3"
        self.do(gadget)

        #xor     eax, eax
        #retn


  def test_gadget_nullsub_1(self):
        #nullsub_1
        gadget = "C22000"
        self.do(gadget)

        #retn    20h


  def test_gadget_sub_1002A3E5(self):
        #sub_1002A3E5
        gadget = "B801400080C20400"
        self.do(gadget)

        #mov     eax, 80004001h
        #retn    4


  def test_gadget_sub_1002A41E(self):
        #sub_1002A41E
        gadget = "836104005733C0C70138A402108D7908ABABABAB8BC15FC3"
        self.do(gadget)

        #and     dword ptr [ecx+4], 0
        #push    edi
        #xor     eax, eax
        #mov     dword ptr [ecx], offset off_1002A438
        #lea     edi, [ecx+8]
        #stosd
        #stosd
        #stosd
        #stosd
        #mov     eax, ecx
        #pop     edi
        #retn


  def test_gadget_sub_1002A459(self):
        #sub_1002A459
        gadget = "B850C10010C3"
        self.do(gadget)

        #mov     eax, offset aRequpload; "requpload"
        #retn


  def test_gadget_sub_1002A464(self):
        #sub_1002A464
        gadget = "8BFF558BEC8B45088941045DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+4], eax
        #pop     ebp
        #retn    4


  def test_gadget_sub_1002A478(self):
        #sub_1002A478
        gadget = "8BFF558BEC568B7508578D7908A5A5A5A55F5E5DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #push    esi
        #mov     esi, [ebp+arg_0]
        #push    edi
        #lea     edi, [ecx+8]
        #movsd
        #movsd
        #movsd
        #movsd
        #pop     edi
        #pop     esi
        #pop     ebp
        #retn    4


  def test_gadget_sub_1002A516(self):
        #sub_1002A516
        gadget = "B884C10010C3"
        self.do(gadget)

        #mov     eax, offset aDataupload; "dataupload"
        #retn


  def test_gadget_sub_1002A521(self):
        #sub_1002A521
        gadget = "8BFF558BEC8B45088941088B450C89410C5DC20800"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+8], eax
        #mov     eax, [ebp+arg_4]
        #mov     [ecx+0Ch], eax
        #pop     ebp
        #retn    8


  def test_gadget_sub_1002A54E(self):
        #sub_1002A54E
        gadget = "8BFF558BEC8B45088941208B450C8941245DC20800"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+20h], eax
        #mov     eax, [ebp+arg_4]
        #mov     [ecx+24h], eax
        #pop     ebp
        #retn    8


  def test_gadget_sub_1002A568(self):
        #sub_1002A568
        gadget = "8BFF558BEC8B45088941288B450C89412C5DC20800"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     eax, [ebp+arg_0]
        #mov     [ecx+28h], eax
        #mov     eax, [ebp+arg_4]
        #mov     [ecx+2Ch], eax
        #pop     ebp
        #retn    8


  def test_gadget_sub_1002A754(self):
        #sub_1002A754
        gadget = "B85CA70210C3"
        self.do(gadget)

        #mov     eax, offset aQryrsrc; "qryrsrc"
        #retn


  def test_gadget_sub_1002A870(self):
        #sub_1002A870
        gadget = "B83CC10010C3"
        self.do(gadget)

        #mov     eax, offset aApproved; "approved"
        #retn


  def test_gadget_sub_1002A87B(self):
        #sub_1002A87B
        gadget = "8B41108B5114C3"
        self.do(gadget)

        #mov     eax, [ecx+10h]
        #mov     edx, [ecx+14h]
        #retn


  def test_gadget_sub_1002AB6C(self):
        #sub_1002AB6C
        gadget = "B864C10010C3"
        self.do(gadget)

        #mov     eax, offset aThrottle; "throttle"
        #retn


  def test_gadget_sub_1002AB77(self):
        #sub_1002AB77
        gadget = "8B4104C3"
        self.do(gadget)

        #mov     eax, [ecx+4]
        #retn


  def test_gadget_sub_1002AE50(self):
        #sub_1002AE50
        gadget = "B8C8C10010C3"
        self.do(gadget)

        #mov     eax, offset aRsrc; "rsrc"
        #retn


  def test_gadget_sub_1002AE5B(self):
        #sub_1002AE5B
        gadget = "8BFF558BEC668B41048B5508668902668B410666894202668B410866894204668B410A668942065DC20400"
        self.do(gadget)

        #mov     edi, edi
        #push    ebp
        #mov     ebp, esp
        #mov     ax, [ecx+4]
        #mov     edx, [ebp+arg_0]
        #mov     [edx], ax
        #mov     ax, [ecx+6]
        #mov     [edx+2], ax
        #mov     ax, [ecx+8]
        #mov     [edx+4], ax
        #mov     ax, [ecx+0Ah]
        #mov     [edx+6], ax
        #pop     ebp
        #retn    4


  def test_gadget_sub_1002B111(self):
        #sub_1002B111
        gadget = "B878C10010C3"
        self.do(gadget)

        #mov     eax, offset aError; "error"
        #retn


  def test_gadget_sub_1002B11C(self):
        #sub_1002B11C
        gadget = "33C0C20400"
        self.do(gadget)

        #xor     eax, eax
        #retn    4


  def test_gadget_sub_1002B191(self):
        #sub_1002B191
        gadget = "B824C60010C3"
        self.do(gadget)

        #mov     eax, offset aNone; "none"
        #retn


  def test_gadget___EH_prolog3_GS(self):
        #__EH_prolog3_GS
        gadget = "8BC05064FF35000000008D44240C2B64240C53565789288BE8A13821031033C5508945F0FF75FCC745FCFFFFFFFF8D45F464A300000000C3"
        self.do(gadget)

        #mov     eax, eax
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


  def test_gadget___EH_epilog3_GS(self):
        #__EH_epilog3_GS
        gadget = "8B4DF033CDE8276CFDFFE9ACA0FDFF"
        self.do(gadget)

        #mov     ecx, [ebp-10h]
        #xor     ecx, ebp
        #call    @__security_check_cookie@4; __security_check_cookie(x)
        #jmp     __EH_epilog3



if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()
