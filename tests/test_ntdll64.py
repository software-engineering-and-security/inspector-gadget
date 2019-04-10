import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetX64(unittest.TestCase):

  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x64")


  def test_gadget_isalpha(self):
		#isalpha
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B058B2413000FB704482503010000C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 103h
		#retn


  def test_gadget_RtlIsGenericTableEmptyAvl(self):
		#RtlIsGenericTableEmptyAvl
		gadget = "33C039412C0F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [rcx+2Ch], eax
		#setz    al
		#retn


  def test_gadget_sub_78E53970(self):
		#sub_78E53970
		gadget = "8B0289018B42048941548B42088981A80000000FB7420C668941440FB7420E668941460FB74210668941520FB74212668941480FB742146689414A0FB742166689414C0FB742186689414E0FB7421A668941500FB7421C668981980000000FB7421E6689819A0000000FB74220668981A60000000FB742226689819C0000000FB742246689819E0000000FB74226668981A00000000FB74228668981A20000000FB7422A668981A4000000C3"
		self.do(gadget)

		#mov     eax, [rdx]
		#mov     [rcx], eax
		#mov     eax, [rdx+4]
		#mov     [rcx+54h], eax
		#mov     eax, [rdx+8]
		#mov     [rcx+0A8h], eax
		#movzx   eax, word ptr [rdx+0Ch]
		#mov     [rcx+44h], ax
		#movzx   eax, word ptr [rdx+0Eh]
		#mov     [rcx+46h], ax
		#movzx   eax, word ptr [rdx+10h]
		#mov     [rcx+52h], ax
		#movzx   eax, word ptr [rdx+12h]
		#mov     [rcx+48h], ax
		#movzx   eax, word ptr [rdx+14h]
		#mov     [rcx+4Ah], ax
		#movzx   eax, word ptr [rdx+16h]
		#mov     [rcx+4Ch], ax
		#movzx   eax, word ptr [rdx+18h]
		#mov     [rcx+4Eh], ax
		#movzx   eax, word ptr [rdx+1Ah]
		#mov     [rcx+50h], ax
		#movzx   eax, word ptr [rdx+1Ch]
		#mov     [rcx+98h], ax
		#movzx   eax, word ptr [rdx+1Eh]
		#mov     [rcx+9Ah], ax
		#movzx   eax, word ptr [rdx+20h]
		#mov     [rcx+0A6h], ax
		#movzx   eax, word ptr [rdx+22h]
		#mov     [rcx+9Ch], ax
		#movzx   eax, word ptr [rdx+24h]
		#mov     [rcx+9Eh], ax
		#movzx   eax, word ptr [rdx+26h]
		#mov     [rcx+0A0h], ax
		#movzx   eax, word ptr [rdx+28h]
		#mov     [rcx+0A2h], ax
		#movzx   eax, word ptr [rdx+2Ah]
		#mov     [rcx+0A4h], ax
		#retn


  def test_gadget_RtlNumberOfSetBitsUlongPtr(self):
		#RtlNumberOfSetBitsUlongPtr
		gadget = "488BC148BA555555555555555548D1E84823C2482BC848B83333333333333333488BD14823C848C1EA024823D04803D148B90F0F0F0F0F0F0F0F488BC248C1E8044803C24823C148B90101010101010101480FAFC148C1E838C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rdx, 5555555555555555h
		#shr     rax, 1
		#and     rax, rdx
		#sub     rcx, rax
		#mov     rax, 3333333333333333h
		#mov     rdx, rcx
		#and     rcx, rax
		#shr     rdx, 2
		#and     rdx, rax
		#add     rdx, rcx
		#mov     rcx, 0F0F0F0F0F0F0F0Fh
		#mov     rax, rdx
		#shr     rax, 4
		#add     rax, rdx
		#and     rax, rcx
		#mov     rcx, 101010101010101h
		#imul    rax, rcx
		#shr     rax, 38h
		#retn


  def test_gadget_sub_78E545D0(self):
		#sub_78E545D0
		gadget = "488B11488B41084C8D0522AF120048891048894208488B0D1CAF1200488911488B42084889050EAF1200488B42084C890048894A08C3"
		self.do(gadget)

		#mov     rdx, [rcx]
		#mov     rax, [rcx+8]
		#lea     r8, off_78F7F500
		#mov     [rax], rdx
		#mov     [rdx+8], rax
		#mov     rcx, cs:off_78F7F508
		#mov     [rcx], rdx
		#mov     rax, [rdx+8]
		#mov     cs:off_78F7F508, rax
		#mov     rax, [rdx+8]
		#mov     [rax], r8
		#mov     [rdx+8], rcx
		#retn


  def test_gadget_RtlNumberGenericTableElementsAvl(self):
		#RtlNumberGenericTableElementsAvl
		gadget = "8B412CC3"
		self.do(gadget)

		#mov     eax, [rcx+2Ch]
		#retn


  def test_gadget_RtlGetLongestNtPathLength(self):
		#RtlGetLongestNtPathLength
		gadget = "B80D010000C3"
		self.do(gadget)

		#mov     eax, 10Dh
		#retn


  def test_gadget_A_SHAInit(self):
		#A_SHAInit
		gadget = "33C0C7414001234567C7414489ABCDEFC74148FEDCBA98C7414C76543210C74150F0E1D2C3894154894158C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword ptr [rcx+40h], 67452301h
		#mov     dword ptr [rcx+44h], 0EFCDAB89h
		#mov     dword ptr [rcx+48h], 98BADCFEh
		#mov     dword ptr [rcx+4Ch], 10325476h
		#mov     dword ptr [rcx+50h], 0C3D2E1F0h
		#mov     [rcx+54h], eax
		#mov     [rcx+58h], eax
		#retn


  def test_gadget_sub_78E58E10(self):
		#sub_78E58E10
		gadget = "48894C24085355565741544155415641574883EC48448B19448B6108448B4104448B510C8B3A488BDA8B51108B73048B6B08448B6B10448B7314418BCA4133CC418BC30FCE4123C8C1C0050FCF4133CA03C2418BD003C8C1C21E458BC3448D8C399979825A418BCC0FCD33CA418BC1410FCD4123CBC1C005410FCE4133CC03C68974242C03C841C1C01E458D940A9979825A8BCA4133C8418BC24123C9C1C00533CA03C503C841C1C11E458D9C0C9979825A448B630C418BC94133C8418BC3410FCC4123CAC1C0054133C84103C403C841C1C21E8D940A9979825A418BC94133CA8BC24123CBC1C0054133C94103C503C841C1C31E458D84089979825A418BCA4133CB418BC023CAC1C0054103C64133CA03C8C1C21E458D8C099979825A448B7B18418BCB418BC133CAC1C005410FCF4123C84103C74133CB03C88B431C41C1C01E458D940A9979825A0FC88BCA4133C88944240C418BC28B74240C4123C9C1C00533CA03C68B732003C841C1C11E0FCE458D9C0B9979825A89742424418BC94133C8418BC34123CAC1C0054133C803C603C88B432441C1C21E8D940A9979825A0FC8418BC94133CA8904248BC28B34244123CBC1C0054133C903C68B732803C841C1C31E0FCE458D84089979825A89742414418BCA4133CB418BC023CAC1C00503C68B732C4133CA03C80FCEC1C21E458D8C099979825A89742410418BCB33CA418BC14123C8C1C00503C68B73304133CB03C80FCE41C1C01E458D940A9979825A897424048BCA418BC24133C8C1C0054123C903C68B733433CA0FCE03C841C1C11E8974241C458D9C0B9979825A418BC94133C8418BC34123CAC1C0054133C803C603C88B43388B5B3C8D940A9979825A41C1C21E0FC889842498000000418BC90FCB8BB424980000004133CA8BC24123CBC1C005899C24A00000004133C903C68B74242403C841C1C31E458D84089979825A418BCA4133CB418BC023CAC1C0054133CA03C303C8C1C21E418D9C099979825A448B4C241C418BCB4433CE8B74242C33CA4123C84433CD8BC34433CF8BBC24980000004133CB333C2441D1C1C1C0054103C14133FC44898C24A800000003C841C1C01E33FE458D8C0A9979825AD1C78BCA4133C8418BC1897C240823CBC1C00533CA8BB424A000000003C73374241403C8C1C31E458D940B9979825A4133F58BCB4133C833F58B6C24104123C9D1C6418BC24133C8C1C0058974241803C603C841C1C11E448D9C0A9979825A8BCB8BD54133C94133D6418BC34123CA4133D4339424A800000033CBD1C2C1C00503C28954242803C841C1C21E418D94089979825A448B442404418BC94133CA4533C78BC24133CB4533C54433C78B7C241C41D1C0C1C0054103C0448944241003C841C1C31E448D840BA1EBD96E8B5C240C418BCA33FB4133CB418BC04133FE33CA33FE8BB42498000000D1C7C1C00503C7897C242C8B7C242403C833F7C1C21E4133F7458D8C09A1EBD96E418BC8337424284133CB418BC1D1C6C1C00533CA03C68974240C03C88B3424448BB424A0000000448B7C24104433F6458D940AA1EBD96E4433F38B5C241441C1C01E4533F7418BC2418BC84133C941D1C6C1C0054103C633CA448974242403C841C1C11E448BF34433F78B7C242C458D9C0BA1EBD96E4433F7418BC3418BC84433B424A80000004133C94133CA41D1C6C1C0054103C603C841C1C21E8BC533C68B74240C8D940AA1EBD96E33C6418BC9334424084133CAD1C04133CB894424208BC2448B642420C1C0054103C4448B64240403C841C1C31E418BC433C38B5C2424458D8408A1EBD96E33C3418BCA334424184133CBD1C033CA89442404418BC0448B6C2404C1C0054103C5448B6C241C03C8C1C21E418BC533C58B6C2428458D8C09A1EBD96E4133C633C5D1C0890424418BC1C1C0058B2C24418BC803C54133CB8BAC249800000033CA4133EC448B64242003C84133EC41C1C01E4133EF458D940AA1EBD96E418BC84133C9D1C5418BC2C1C00533CA896C242C03C503C88B8424A000000041C1C11E4133C5458D9C0BA1EBD96E418BC8334424044133C933C74133CAD1C08944240C418BC3448B6C240CC1C0054103C503C88B84249800000041C1C21E3304248D940AA1EBD96E418BC933C64133CA338424A80000004133CBD1C0898424980000008BC2448BBC2498000000C1C0054103C7448BBC24A000000003C84433FD41C1C31E4433FB458D8408A1EBD96E418BED44337C2408448B6C24184133EE41D1C74133ED418BC033AC24A8000000C1C005418BCA4133CB4103C74489BC24A000000033CA03C8C1C21ED1C5458D8C09A1EBD96E89AC24A8000000418BC8418BC1C1C00503C58B6C24284133CB33CA03C88B84249800000041C1C01E4133C4458D940AA1EBD96E418BC833C54133C93344240833CAD1C089442408418BC2448B642408C1C0054103C4458BE7448B7C2410443364240403C841C1C11E458D9C0BA1EBD96E4533E7418BC84133C94533E5448B2C244133CA41D1C4418BC3C1C00544896424104103C403C841C1C21E418BC533C78D940AA1EBD96E418BC933C54133CA338424A80000004133CBD1C08904248BC28B2C24C1C00503C58B6C242C03C841C1C31E8BC533C6458D8408A1EBD96E418BCA4133C74133CB3344240833CAD1C089442414418BC0448B7C2414C1C0054103C7448B7C240C03C8418BC7C1C21E33C3458D8C09A1EBD96E33C74133C4D1C089442428418BC1448B6424288BBC2498000000C1C0054103C4448B6424204133FE33FE8BB424A8000000418BC8333C244133CB33CA03C841C1C01ED1C7458D940AA1EBD96E897C2424418BC84133C9418BC233CAC1C00503C78BBC24A000000003C84133FC41C1C11E458D9C0BA1EBD96E33FB418BC8337C24144133C9418BC34133CAD1C7C1C00503C7897C241C8B7C240403C841C1C21E8BC74133C6448B7424288D9C0AA1EBD96E4133C68BD3418BCA33C6410BCBD1C04123C9C1C205898424A8000000418BC24123C30BC8418BC5038C24A80000004133C4448B642408334424244103C841C1C31E448D8411DCBC1B8F4133C4418BCBD1C00BCB418BD0894424184123CAC1C205418BC323C30BC88BC5034C24184103C9C1C31E448D8C11DCBC1B8F33C78B7C2410418BC83344241C0BCB418BD133C74123CBD1C0C1C20589442420418BC023C30BC8418BC7034C24204133C5448B2C24338424A80000004103CA41C1C01E448D9411DCBC1B8F4133C5418BC8D1C0410BC9418BD223CB89442408C1C205418BC04123C10BC88B842498000000034C240833C58B6C2414334424184103CB41C1C11E448D9C11DCBC1B8F33C5418BC9D1C0410BCA418BD34123C889442404C1C205418BC14123C20BC88B8424A0000000034C24044133C7448BBC24980000003344242044337C240803CB44337C24248D9C11DCBC1B8F4133C641C1C21ED1C08BD3890424C1C205418BCA448B3424410BCB418BC24123C94123C34433FE0BC84103CE4103C841C1C31E41D1C74489BC2498000000448D8411DCBC1B8F4433B424A8000000418BD0418BCB0BCBC1C2054433F74123CA4433F6418BC323C30BC88B8424A0000000334424044103CF44337C24183344241C4103C9C1C31E448D8C11DCBC1B8F4133C44533FDD1C04533FC418BC80BCB898424A0000000418BC04123CB23C3418BD10BC8C1C205038C24A00000004103CA41C1C01E41D1C6448D9411DCBC1B8F4489742414418BC8410BC9418BC0418BD223CB4123C1C1C2050BC84103CE448BB424A000000044337424204103CB41C1C11E448D9C11DCBC1B8F41D1C74433F54433F7418BC9418BC1410BCA4123C2418BD34123C8C1C20544897C24100BC84103CF03CB41C1C21E41D1C68D9C11DCBC1B8F418BCA418BC2410BCB4123C38BD34123C9C1C20544897424300BC84103CE4103C8448D8411DCBC1B8F448B6424288B7C24088B34243374241C4133FC448B642404337424284133FD448B6C2424337C241441C1C31E4533E5D1C74433E58BAC249800000033AC24A80000004533E74133F64133ED448BAC24A0000000418BCB44336C24180BCB33EF44336C241C4123CA418BC323C3418BD0897C240C0BC8C1C205418BC003CF4103C9C1C31E41D1C4448D8C11DCBC1B8F23C3418BC80BCB418BD14533EC4123CBC1C205448964242C0BC84103CC4103CA41C1C01ED1C6448D9411DCBC1B8F418BC8418BC0410BC94123C1418BD223CBC1C205897424240BC803CE4103CB41C1C11ED1C5448D9C11DCBC1B8F418BC9418BC1410BCA4123C2418BD34123C8C1C205896C24280BC803CD03CB41C1C21E41D1C544896C241C8DBC11DCBC1B8F418BCA418BC28BD7410BCB4123C3C1C2054123C90BC84103CD4103C8448B44242041C1C31E44338424A80000008D9C11DCBC1B8F418BCB0BCF4433C68B7424084433442414337424184123CA41D1C033F5418BC323C74133F7448B7C240444337C24200BC88BD34103C8C1C2054533FD4103C9C1C71ED1C6448D8C11DCBC1B8F4533FE448B342444337424088BCB8BC30BCF23C74533F0443374240C4123CB418BD10BC8C1C20544898424A800000003CE897424184103CAC1C31E41D1C7448D9411DCBC1B8F8BCB8BC3410BC94123C1418BD223CFC1C20544897C24200BC84103CF4103CB41C1C11E41D1C6448D9C11DCBC1B8F418BC9418BC1410BCA4123C2418BD323CBC1C20544897424080BC84103CE03CF8BBC249800000041C1C21E448D8411DCBC1B8F8BEF4133FE336C2404337C2428418BC14133C233EE418BC84133C34133EC448BA424A000000044332424D1C5C1C10503C54533E7896C2404443364242403C38B5C24148D9408D6C162CA41C1C31E33FB41D1C4418BC28BCA4133C3C1C105448924244133C04103C44103C141C1C01ED1C7448D8C08D6C162CA89BC24980000008BC24133C3418BC94133C0C1C10503C78BBC24A00000004103C233FDC1C21E448D9408D6C162CA4133FD8BC2337C24104133C1418BCA4133C0D1C7C1C10503C7458BEC89BC24A00000004433AC24A80000008B7C24304103C3448D9C08D6C162CA41C1C11E4433EF4433EB8B9C24980000008BC24133C141D1C5418BCB4133C2C1C10544896C24144103C54103C041C1C21E448D8408D6C162CA443364241C33DE8BB424A0000000335C240C4133F7448B7C2428335C24103374242C4133EF336C242CD1C333F733EB418BFE448B7424244133FE4533E6448BB42498000000337C240C418BC1418BC84133C2C1C1054133FD4133C3895C241003C303C241C1C31ED1C68D9408D6C162CA4433E6418BC24133C38BCA4133C0C1C10503C64103C141C1C01ED1C7448D8C08D6C162CA8BC2897C24304133C3418BC94133C0C1C10503C74103C2C1C21ED1C5448D9408D6C162CA8BC2896C242C4133C1418BCA4133C0C1C10503C54103C341C1C11E41D1C4448D9C08D6C162CA8BC2448964240C4133C1418BCB4133C2C1C1054103C44103C0448B8424A800000041C1C21E4533F08D9C08D6C162CA4533F78BCB4433F741D1C6C1C105448BBC24A0000000418BC144337C24184133C244337C241C4133C34103C64433FD03C241C1C31E41D1C78DBC08D6C162CA418BC24133C38BCF33C3C1C1054103C74103C1448B4C2420C1C31E8DAC08D6C162CA418BD18BC74133C34133D08BCD33C34133D44133D5D1C2C1C10503C24103C2448B542408C1C71E448DA408D6C162CA458BC28BC7443344241833C5418BCC33C34533C6443344241041D1C0C1C1054103C04103C3448B5C2404C1C51E448DAC08D6C162CA4533D9448B0C244533DF4533CA448B9424980000004433DE4433CA8BC744334C243033C541D1C34133C4418BCD4103C3C1C10503C341C1C41E41D1C18DB408D6C162CA8BC54133C48BCE4133C5C1C1054103C103C741C1C51E44335424048DBC08D6C162CA4533D08BCF418BC4443354242C4133C533C641D1C2C1C1054103C203C58BAC24A0000000C1C61E8D9C08D6C162CA8BD54133EA3314244133EF8BC7336C24104133C54133D33354240C33C68BCBD1C2C1C10503C28B9424980000004103C44133D14C8B8C2490000000448D8408D6C162CA4133D6C1C71E33542414418BC88BC733C3D1C2C1C10533C603C24103C5C1C31ED1C58D9408D6C162CA418B098BC2C1C00503E88BC733C34133C003C68D8428D6C162CA03C8418B410403C241C1C01E4189094503410841894104418B410C03C3458941084189410C418B411003C7418941104883C448415F415E415D415C5F5E5D5BC3"
		self.do(gadget)

		#mov     [rsp+arg_0], rcx
		#push    rbx
		#push    rbp
		#push    rsi
		#push    rdi
		#push    r12
		#push    r13
		#push    r14
		#push    r15
		#sub     rsp, 48h
		#mov     r11d, [rcx]
		#mov     r12d, [rcx+8]
		#mov     r8d, [rcx+4]
		#mov     r10d, [rcx+0Ch]
		#mov     edi, [rdx]
		#mov     rbx, rdx
		#mov     edx, [rcx+10h]
		#mov     esi, [rbx+4]
		#mov     ebp, [rbx+8]
		#mov     r13d, [rbx+10h]
		#mov     r14d, [rbx+14h]
		#mov     ecx, r10d
		#xor     ecx, r12d
		#mov     eax, r11d
		#bswap   esi
		#and     ecx, r8d
		#rol     eax, 5
		#bswap   edi
		#xor     ecx, r10d
		#add     eax, edx
		#mov     edx, r8d
		#add     ecx, eax
		#rol     edx, 1Eh
		#mov     r8d, r11d
		#lea     r9d, [rcx+rdi+5A827999h]
		#mov     ecx, r12d
		#bswap   ebp
		#xor     ecx, edx
		#mov     eax, r9d
		#bswap   r13d
		#and     ecx, r11d
		#rol     eax, 5
		#bswap   r14d
		#xor     ecx, r12d
		#add     eax, esi
		#mov     [rsp+88h+var_5C], esi
		#add     ecx, eax
		#rol     r8d, 1Eh
		#lea     r10d, [r10+rcx+5A827999h]
		#mov     ecx, edx
		#xor     ecx, r8d
		#mov     eax, r10d
		#and     ecx, r9d
		#rol     eax, 5
		#xor     ecx, edx
		#add     eax, ebp
		#add     ecx, eax
		#rol     r9d, 1Eh
		#lea     r11d, [r12+rcx+5A827999h]
		#mov     r12d, [rbx+0Ch]
		#mov     ecx, r9d
		#xor     ecx, r8d
		#mov     eax, r11d
		#bswap   r12d
		#and     ecx, r10d
		#rol     eax, 5
		#xor     ecx, r8d
		#add     eax, r12d
		#add     ecx, eax
		#rol     r10d, 1Eh
		#lea     edx, [rdx+rcx+5A827999h]
		#mov     ecx, r9d
		#xor     ecx, r10d
		#mov     eax, edx
		#and     ecx, r11d
		#rol     eax, 5
		#xor     ecx, r9d
		#add     eax, r13d
		#add     ecx, eax
		#rol     r11d, 1Eh
		#lea     r8d, [r8+rcx+5A827999h]
		#mov     ecx, r10d
		#xor     ecx, r11d
		#mov     eax, r8d
		#and     ecx, edx
		#rol     eax, 5
		#add     eax, r14d
		#xor     ecx, r10d
		#add     ecx, eax
		#rol     edx, 1Eh
		#lea     r9d, [r9+rcx+5A827999h]
		#mov     r15d, [rbx+18h]
		#mov     ecx, r11d
		#mov     eax, r9d
		#xor     ecx, edx
		#rol     eax, 5
		#bswap   r15d
		#and     ecx, r8d
		#add     eax, r15d
		#xor     ecx, r11d
		#add     ecx, eax
		#mov     eax, [rbx+1Ch]
		#rol     r8d, 1Eh
		#lea     r10d, [r10+rcx+5A827999h]
		#bswap   eax
		#mov     ecx, edx
		#xor     ecx, r8d
		#mov     [rsp+88h+var_7C], eax
		#mov     eax, r10d
		#mov     esi, [rsp+88h+var_7C]
		#and     ecx, r9d
		#rol     eax, 5
		#xor     ecx, edx
		#add     eax, esi
		#mov     esi, [rbx+20h]
		#add     ecx, eax
		#rol     r9d, 1Eh
		#bswap   esi
		#lea     r11d, [r11+rcx+5A827999h]
		#mov     [rsp+88h+var_64], esi
		#mov     ecx, r9d
		#xor     ecx, r8d
		#mov     eax, r11d
		#and     ecx, r10d
		#rol     eax, 5
		#xor     ecx, r8d
		#add     eax, esi
		#add     ecx, eax
		#mov     eax, [rbx+24h]
		#rol     r10d, 1Eh
		#lea     edx, [rdx+rcx+5A827999h]
		#bswap   eax
		#mov     ecx, r9d
		#xor     ecx, r10d
		#mov     [rsp+88h+var_88], eax
		#mov     eax, edx
		#mov     esi, [rsp+88h+var_88]
		#and     ecx, r11d
		#rol     eax, 5
		#xor     ecx, r9d
		#add     eax, esi
		#mov     esi, [rbx+28h]
		#add     ecx, eax
		#rol     r11d, 1Eh
		#bswap   esi
		#lea     r8d, [r8+rcx+5A827999h]
		#mov     [rsp+88h+var_74], esi
		#mov     ecx, r10d
		#xor     ecx, r11d
		#mov     eax, r8d
		#and     ecx, edx
		#rol     eax, 5
		#add     eax, esi
		#mov     esi, [rbx+2Ch]
		#xor     ecx, r10d
		#add     ecx, eax
		#bswap   esi
		#rol     edx, 1Eh
		#lea     r9d, [r9+rcx+5A827999h]
		#mov     [rsp+88h+var_78], esi
		#mov     ecx, r11d
		#xor     ecx, edx
		#mov     eax, r9d
		#and     ecx, r8d
		#rol     eax, 5
		#add     eax, esi
		#mov     esi, [rbx+30h]
		#xor     ecx, r11d
		#add     ecx, eax
		#bswap   esi
		#rol     r8d, 1Eh
		#lea     r10d, [r10+rcx+5A827999h]
		#mov     [rsp+88h+var_84], esi
		#mov     ecx, edx
		#mov     eax, r10d
		#xor     ecx, r8d
		#rol     eax, 5
		#and     ecx, r9d
		#add     eax, esi
		#mov     esi, [rbx+34h]
		#xor     ecx, edx
		#bswap   esi
		#add     ecx, eax
		#rol     r9d, 1Eh
		#mov     [rsp+88h+var_6C], esi
		#lea     r11d, [r11+rcx+5A827999h]
		#mov     ecx, r9d
		#xor     ecx, r8d
		#mov     eax, r11d
		#and     ecx, r10d
		#rol     eax, 5
		#xor     ecx, r8d
		#add     eax, esi
		#add     ecx, eax
		#mov     eax, [rbx+38h]
		#mov     ebx, [rbx+3Ch]
		#lea     edx, [rdx+rcx+5A827999h]
		#rol     r10d, 1Eh
		#bswap   eax
		#mov     [rsp+88h+arg_8], eax
		#mov     ecx, r9d
		#bswap   ebx
		#mov     esi, [rsp+88h+arg_8]
		#xor     ecx, r10d
		#mov     eax, edx
		#and     ecx, r11d
		#rol     eax, 5
		#mov     [rsp+88h+arg_10], ebx
		#xor     ecx, r9d
		#add     eax, esi
		#mov     esi, [rsp+88h+var_64]
		#add     ecx, eax
		#rol     r11d, 1Eh
		#lea     r8d, [r8+rcx+5A827999h]
		#mov     ecx, r10d
		#xor     ecx, r11d
		#mov     eax, r8d
		#and     ecx, edx
		#rol     eax, 5
		#xor     ecx, r10d
		#add     eax, ebx
		#add     ecx, eax
		#rol     edx, 1Eh
		#lea     ebx, [r9+rcx+5A827999h]
		#mov     r9d, [rsp+88h+var_6C]
		#mov     ecx, r11d
		#xor     r9d, esi
		#mov     esi, [rsp+88h+var_5C]
		#xor     ecx, edx
		#and     ecx, r8d
		#xor     r9d, ebp
		#mov     eax, ebx
		#xor     r9d, edi
		#mov     edi, [rsp+88h+arg_8]
		#xor     ecx, r11d
		#xor     edi, [rsp+88h+var_88]
		#rol     r9d, 1
		#rol     eax, 5
		#add     eax, r9d
		#xor     edi, r12d
		#mov     [rsp+88h+arg_18], r9d
		#add     ecx, eax
		#rol     r8d, 1Eh
		#xor     edi, esi
		#lea     r9d, [r10+rcx+5A827999h]
		#rol     edi, 1
		#mov     ecx, edx
		#xor     ecx, r8d
		#mov     eax, r9d
		#mov     [rsp+88h+var_80], edi
		#and     ecx, ebx
		#rol     eax, 5
		#xor     ecx, edx
		#mov     esi, [rsp+88h+arg_10]
		#add     eax, edi
		#xor     esi, [rsp+88h+var_74]
		#add     ecx, eax
		#rol     ebx, 1Eh
		#lea     r10d, [r11+rcx+5A827999h]
		#xor     esi, r13d
		#mov     ecx, ebx
		#xor     ecx, r8d
		#xor     esi, ebp
		#mov     ebp, [rsp+88h+var_78]
		#and     ecx, r9d
		#rol     esi, 1
		#mov     eax, r10d
		#xor     ecx, r8d
		#rol     eax, 5
		#mov     [rsp+88h+var_70], esi
		#add     eax, esi
		#add     ecx, eax
		#rol     r9d, 1Eh
		#lea     r11d, [rdx+rcx+5A827999h]
		#mov     ecx, ebx
		#mov     edx, ebp
		#xor     ecx, r9d
		#xor     edx, r14d
		#mov     eax, r11d
		#and     ecx, r10d
		#xor     edx, r12d
		#xor     edx, [rsp+88h+arg_18]
		#xor     ecx, ebx
		#rol     edx, 1
		#rol     eax, 5
		#add     eax, edx
		#mov     [rsp+88h+var_60], edx
		#add     ecx, eax
		#rol     r10d, 1Eh
		#lea     edx, [r8+rcx+5A827999h]
		#mov     r8d, [rsp+88h+var_84]
		#mov     ecx, r9d
		#xor     ecx, r10d
		#xor     r8d, r15d
		#mov     eax, edx
		#xor     ecx, r11d
		#xor     r8d, r13d
		#xor     r8d, edi
		#mov     edi, [rsp+88h+var_6C]
		#rol     r8d, 1
		#rol     eax, 5
		#add     eax, r8d
		#mov     [rsp+88h+var_78], r8d
		#add     ecx, eax
		#rol     r11d, 1Eh
		#lea     r8d, [rbx+rcx+6ED9EBA1h]
		#mov     ebx, [rsp+88h+var_7C]
		#mov     ecx, r10d
		#xor     edi, ebx
		#xor     ecx, r11d
		#mov     eax, r8d
		#xor     edi, r14d
		#xor     ecx, edx
		#xor     edi, esi
		#mov     esi, [rsp+88h+arg_8]
		#rol     edi, 1
		#rol     eax, 5
		#add     eax, edi
		#mov     [rsp+88h+var_5C], edi
		#mov     edi, [rsp+88h+var_64]
		#add     ecx, eax
		#xor     esi, edi
		#rol     edx, 1Eh
		#xor     esi, r15d
		#lea     r9d, [r9+rcx+6ED9EBA1h]
		#mov     ecx, r8d
		#xor     esi, [rsp+88h+var_60]
		#xor     ecx, r11d
		#mov     eax, r9d
		#rol     esi, 1
		#rol     eax, 5
		#xor     ecx, edx
		#add     eax, esi
		#mov     [rsp+88h+var_7C], esi
		#add     ecx, eax
		#mov     esi, [rsp+88h+var_88]
		#mov     r14d, [rsp+88h+arg_10]
		#mov     r15d, [rsp+88h+var_78]
		#xor     r14d, esi
		#lea     r10d, [r10+rcx+6ED9EBA1h]
		#xor     r14d, ebx
		#mov     ebx, [rsp+88h+var_74]
		#rol     r8d, 1Eh
		#xor     r14d, r15d
		#mov     eax, r10d
		#mov     ecx, r8d
		#xor     ecx, r9d
		#rol     r14d, 1
		#rol     eax, 5
		#add     eax, r14d
		#xor     ecx, edx
		#mov     [rsp+88h+var_64], r14d
		#add     ecx, eax
		#rol     r9d, 1Eh
		#mov     r14d, ebx
		#xor     r14d, edi
		#mov     edi, [rsp+88h+var_5C]
		#lea     r11d, [r11+rcx+6ED9EBA1h]
		#xor     r14d, edi
		#mov     eax, r11d
		#mov     ecx, r8d
		#xor     r14d, [rsp+88h+arg_18]
		#xor     ecx, r9d
		#xor     ecx, r10d
		#rol     r14d, 1
		#rol     eax, 5
		#add     eax, r14d
		#add     ecx, eax
		#rol     r10d, 1Eh
		#mov     eax, ebp
		#xor     eax, esi
		#mov     esi, [rsp+88h+var_7C]
		#lea     edx, [rdx+rcx+6ED9EBA1h]
		#xor     eax, esi
		#mov     ecx, r9d
		#xor     eax, [rsp+88h+var_80]
		#xor     ecx, r10d
		#rol     eax, 1
		#xor     ecx, r11d
		#mov     [rsp+88h+var_68], eax
		#mov     eax, edx
		#mov     r12d, [rsp+88h+var_68]
		#rol     eax, 5
		#add     eax, r12d
		#mov     r12d, [rsp+88h+var_84]
		#add     ecx, eax
		#rol     r11d, 1Eh
		#mov     eax, r12d
		#xor     eax, ebx
		#mov     ebx, [rsp+88h+var_64]
		#lea     r8d, [r8+rcx+6ED9EBA1h]
		#xor     eax, ebx
		#mov     ecx, r10d
		#xor     eax, [rsp+88h+var_70]
		#xor     ecx, r11d
		#rol     eax, 1
		#xor     ecx, edx
		#mov     [rsp+88h+var_84], eax
		#mov     eax, r8d
		#mov     r13d, [rsp+88h+var_84]
		#rol     eax, 5
		#add     eax, r13d
		#mov     r13d, [rsp+88h+var_6C]
		#add     ecx, eax
		#rol     edx, 1Eh
		#mov     eax, r13d
		#xor     eax, ebp
		#mov     ebp, [rsp+88h+var_60]
		#lea     r9d, [r9+rcx+6ED9EBA1h]
		#xor     eax, r14d
		#xor     eax, ebp
		#rol     eax, 1
		#mov     [rsp+88h+var_88], eax
		#mov     eax, r9d
		#rol     eax, 5
		#mov     ebp, [rsp+88h+var_88]
		#mov     ecx, r8d
		#add     eax, ebp
		#xor     ecx, r11d
		#mov     ebp, [rsp+88h+arg_8]
		#xor     ecx, edx
		#xor     ebp, r12d
		#mov     r12d, [rsp+88h+var_68]
		#add     ecx, eax
		#xor     ebp, r12d
		#rol     r8d, 1Eh
		#xor     ebp, r15d
		#lea     r10d, [r10+rcx+6ED9EBA1h]
		#mov     ecx, r8d
		#xor     ecx, r9d
		#rol     ebp, 1
		#mov     eax, r10d
		#rol     eax, 5
		#xor     ecx, edx
		#mov     [rsp+88h+var_5C], ebp
		#add     eax, ebp
		#add     ecx, eax
		#mov     eax, [rsp+88h+arg_10]
		#rol     r9d, 1Eh
		#xor     eax, r13d
		#lea     r11d, [r11+rcx+6ED9EBA1h]
		#mov     ecx, r8d
		#xor     eax, [rsp+88h+var_84]
		#xor     ecx, r9d
		#xor     eax, edi
		#xor     ecx, r10d
		#rol     eax, 1
		#mov     [rsp+88h+var_7C], eax
		#mov     eax, r11d
		#mov     r13d, [rsp+88h+var_7C]
		#rol     eax, 5
		#add     eax, r13d
		#add     ecx, eax
		#mov     eax, [rsp+88h+arg_8]
		#rol     r10d, 1Eh
		#xor     eax, [rsp+88h+var_88]
		#lea     edx, [rdx+rcx+6ED9EBA1h]
		#mov     ecx, r9d
		#xor     eax, esi
		#xor     ecx, r10d
		#xor     eax, [rsp+88h+arg_18]
		#xor     ecx, r11d
		#rol     eax, 1
		#mov     [rsp+88h+arg_8], eax
		#mov     eax, edx
		#mov     r15d, [rsp+88h+arg_8]
		#rol     eax, 5
		#add     eax, r15d
		#mov     r15d, [rsp+88h+arg_10]
		#add     ecx, eax
		#xor     r15d, ebp
		#rol     r11d, 1Eh
		#xor     r15d, ebx
		#lea     r8d, [r8+rcx+6ED9EBA1h]
		#mov     ebp, r13d
		#xor     r15d, [rsp+88h+var_80]
		#mov     r13d, [rsp+88h+var_70]
		#xor     ebp, r14d
		#rol     r15d, 1
		#xor     ebp, r13d
		#mov     eax, r8d
		#xor     ebp, [rsp+88h+arg_18]
		#rol     eax, 5
		#mov     ecx, r10d
		#xor     ecx, r11d
		#add     eax, r15d
		#mov     [rsp+88h+arg_10], r15d
		#xor     ecx, edx
		#add     ecx, eax
		#rol     edx, 1Eh
		#rol     ebp, 1
		#lea     r9d, [r9+rcx+6ED9EBA1h]
		#mov     [rsp+88h+arg_18], ebp
		#mov     ecx, r8d
		#mov     eax, r9d
		#rol     eax, 5
		#add     eax, ebp
		#mov     ebp, [rsp+88h+var_60]
		#xor     ecx, r11d
		#xor     ecx, edx
		#add     ecx, eax
		#mov     eax, [rsp+88h+arg_8]
		#rol     r8d, 1Eh
		#xor     eax, r12d
		#lea     r10d, [r10+rcx+6ED9EBA1h]
		#mov     ecx, r8d
		#xor     eax, ebp
		#xor     ecx, r9d
		#xor     eax, [rsp+88h+var_80]
		#xor     ecx, edx
		#rol     eax, 1
		#mov     [rsp+88h+var_80], eax
		#mov     eax, r10d
		#mov     r12d, [rsp+88h+var_80]
		#rol     eax, 5
		#add     eax, r12d
		#mov     r12d, r15d
		#mov     r15d, [rsp+88h+var_78]
		#xor     r12d, [rsp+88h+var_84]
		#add     ecx, eax
		#rol     r9d, 1Eh
		#lea     r11d, [r11+rcx+6ED9EBA1h]
		#xor     r12d, r15d
		#mov     ecx, r8d
		#xor     ecx, r9d
		#xor     r12d, r13d
		#mov     r13d, [rsp+88h+var_88]
		#xor     ecx, r10d
		#rol     r12d, 1
		#mov     eax, r11d
		#rol     eax, 5
		#mov     [rsp+88h+var_78], r12d
		#add     eax, r12d
		#add     ecx, eax
		#rol     r10d, 1Eh
		#mov     eax, r13d
		#xor     eax, edi
		#lea     edx, [rdx+rcx+6ED9EBA1h]
		#mov     ecx, r9d
		#xor     eax, ebp
		#xor     ecx, r10d
		#xor     eax, [rsp+88h+arg_18]
		#xor     ecx, r11d
		#rol     eax, 1
		#mov     [rsp+88h+var_88], eax
		#mov     eax, edx
		#mov     ebp, [rsp+88h+var_88]
		#rol     eax, 5
		#add     eax, ebp
		#mov     ebp, [rsp+88h+var_5C]
		#add     ecx, eax
		#rol     r11d, 1Eh
		#mov     eax, ebp
		#xor     eax, esi
		#lea     r8d, [r8+rcx+6ED9EBA1h]
		#mov     ecx, r10d
		#xor     eax, r15d
		#xor     ecx, r11d
		#xor     eax, [rsp+88h+var_80]
		#xor     ecx, edx
		#rol     eax, 1
		#mov     [rsp+88h+var_74], eax
		#mov     eax, r8d
		#mov     r15d, [rsp+88h+var_74]
		#rol     eax, 5
		#add     eax, r15d
		#mov     r15d, [rsp+88h+var_7C]
		#add     ecx, eax
		#mov     eax, r15d
		#rol     edx, 1Eh
		#xor     eax, ebx
		#lea     r9d, [r9+rcx+6ED9EBA1h]
		#xor     eax, edi
		#xor     eax, r12d
		#rol     eax, 1
		#mov     [rsp+88h+var_60], eax
		#mov     eax, r9d
		#mov     r12d, [rsp+88h+var_60]
		#mov     edi, [rsp+88h+arg_8]
		#rol     eax, 5
		#add     eax, r12d
		#mov     r12d, [rsp+88h+var_68]
		#xor     edi, r14d
		#xor     edi, esi
		#mov     esi, [rsp+88h+arg_18]
		#mov     ecx, r8d
		#xor     edi, [rsp+88h+var_88]
		#xor     ecx, r11d
		#xor     ecx, edx
		#add     ecx, eax
		#rol     r8d, 1Eh
		#rol     edi, 1
		#lea     r10d, [r10+rcx+6ED9EBA1h]
		#mov     [rsp+88h+var_64], edi
		#mov     ecx, r8d
		#xor     ecx, r9d
		#mov     eax, r10d
		#xor     ecx, edx
		#rol     eax, 5
		#add     eax, edi
		#mov     edi, [rsp+88h+arg_10]
		#add     ecx, eax
		#xor     edi, r12d
		#rol     r9d, 1Eh
		#lea     r11d, [r11+rcx+6ED9EBA1h]
		#xor     edi, ebx
		#mov     ecx, r8d
		#xor     edi, [rsp+88h+var_74]
		#xor     ecx, r9d
		#mov     eax, r11d
		#xor     ecx, r10d
		#rol     edi, 1
		#rol     eax, 5
		#add     eax, edi
		#mov     [rsp+88h+var_6C], edi
		#mov     edi, [rsp+88h+var_84]
		#add     ecx, eax
		#rol     r10d, 1Eh
		#mov     eax, edi
		#xor     eax, r14d
		#mov     r14d, [rsp+88h+var_60]
		#lea     ebx, [rdx+rcx+6ED9EBA1h]
		#xor     eax, r14d
		#mov     edx, ebx
		#mov     ecx, r10d
		#xor     eax, esi
		#or      ecx, r11d
		#rol     eax, 1
		#and     ecx, r9d
		#rol     edx, 5
		#mov     [rsp+88h+arg_18], eax
		#mov     eax, r10d
		#and     eax, r11d
		#or      ecx, eax
		#mov     eax, r13d
		#add     ecx, [rsp+88h+arg_18]
		#xor     eax, r12d
		#mov     r12d, [rsp+88h+var_80]
		#xor     eax, [rsp+88h+var_64]
		#add     ecx, r8d
		#rol     r11d, 1Eh
		#lea     r8d, [rcx+rdx-70E44324h]
		#xor     eax, r12d
		#mov     ecx, r11d
		#rol     eax, 1
		#or      ecx, ebx
		#mov     edx, r8d
		#mov     [rsp+88h+var_70], eax
		#and     ecx, r10d
		#rol     edx, 5
		#mov     eax, r11d
		#and     eax, ebx
		#or      ecx, eax
		#mov     eax, ebp
		#add     ecx, [rsp+88h+var_70]
		#add     ecx, r9d
		#rol     ebx, 1Eh
		#lea     r9d, [rcx+rdx-70E44324h]
		#xor     eax, edi
		#mov     edi, [rsp+88h+var_78]
		#mov     ecx, r8d
		#xor     eax, [rsp+88h+var_6C]
		#or      ecx, ebx
		#mov     edx, r9d
		#xor     eax, edi
		#and     ecx, r11d
		#rol     eax, 1
		#rol     edx, 5
		#mov     [rsp+88h+var_68], eax
		#mov     eax, r8d
		#and     eax, ebx
		#or      ecx, eax
		#mov     eax, r15d
		#add     ecx, [rsp+88h+var_68]
		#xor     eax, r13d
		#mov     r13d, [rsp+88h+var_88]
		#xor     eax, [rsp+88h+arg_18]
		#add     ecx, r10d
		#rol     r8d, 1Eh
		#lea     r10d, [rcx+rdx-70E44324h]
		#xor     eax, r13d
		#mov     ecx, r8d
		#rol     eax, 1
		#or      ecx, r9d
		#mov     edx, r10d
		#and     ecx, ebx
		#mov     [rsp+88h+var_80], eax
		#rol     edx, 5
		#mov     eax, r8d
		#and     eax, r9d
		#or      ecx, eax
		#mov     eax, [rsp+88h+arg_8]
		#add     ecx, [rsp+88h+var_80]
		#xor     eax, ebp
		#mov     ebp, [rsp+88h+var_74]
		#xor     eax, [rsp+88h+var_70]
		#add     ecx, r11d
		#rol     r9d, 1Eh
		#lea     r11d, [rcx+rdx-70E44324h]
		#xor     eax, ebp
		#mov     ecx, r9d
		#rol     eax, 1
		#or      ecx, r10d
		#mov     edx, r11d
		#and     ecx, r8d
		#mov     [rsp+88h+var_84], eax
		#rol     edx, 5
		#mov     eax, r9d
		#and     eax, r10d
		#or      ecx, eax
		#mov     eax, [rsp+88h+arg_10]
		#add     ecx, [rsp+88h+var_84]
		#xor     eax, r15d
		#mov     r15d, [rsp+88h+arg_8]
		#xor     eax, [rsp+88h+var_68]
		#xor     r15d, [rsp+88h+var_80]
		#add     ecx, ebx
		#xor     r15d, [rsp+88h+var_64]
		#lea     ebx, [rcx+rdx-70E44324h]
		#xor     eax, r14d
		#rol     r10d, 1Eh
		#rol     eax, 1
		#mov     edx, ebx
		#mov     [rsp+88h+var_88], eax
		#rol     edx, 5
		#mov     ecx, r10d
		#mov     r14d, [rsp+88h+var_88]
		#or      ecx, r11d
		#mov     eax, r10d
		#and     ecx, r9d
		#and     eax, r11d
		#xor     r15d, esi
		#or      ecx, eax
		#add     ecx, r14d
		#add     ecx, r8d
		#rol     r11d, 1Eh
		#rol     r15d, 1
		#mov     [rsp+88h+arg_8], r15d
		#lea     r8d, [rcx+rdx-70E44324h]
		#xor     r14d, [rsp+88h+arg_18]
		#mov     edx, r8d
		#mov     ecx, r11d
		#or      ecx, ebx
		#rol     edx, 5
		#xor     r14d, edi
		#and     ecx, r10d
		#xor     r14d, esi
		#mov     eax, r11d
		#and     eax, ebx
		#or      ecx, eax
		#mov     eax, [rsp+88h+arg_10]
		#xor     eax, [rsp+88h+var_84]
		#add     ecx, r15d
		#xor     r15d, [rsp+88h+var_70]
		#xor     eax, [rsp+88h+var_6C]
		#add     ecx, r9d
		#rol     ebx, 1Eh
		#lea     r9d, [rcx+rdx-70E44324h]
		#xor     eax, r12d
		#xor     r15d, r13d
		#rol     eax, 1
		#xor     r15d, r12d
		#mov     ecx, r8d
		#or      ecx, ebx
		#mov     [rsp+88h+arg_10], eax
		#mov     eax, r8d
		#and     ecx, r11d
		#and     eax, ebx
		#mov     edx, r9d
		#or      ecx, eax
		#rol     edx, 5
		#add     ecx, [rsp+88h+arg_10]
		#add     ecx, r10d
		#rol     r8d, 1Eh
		#rol     r14d, 1
		#lea     r10d, [rcx+rdx-70E44324h]
		#mov     [rsp+88h+var_74], r14d
		#mov     ecx, r8d
		#or      ecx, r9d
		#mov     eax, r8d
		#mov     edx, r10d
		#and     ecx, ebx
		#and     eax, r9d
		#rol     edx, 5
		#or      ecx, eax
		#add     ecx, r14d
		#mov     r14d, [rsp+88h+arg_10]
		#xor     r14d, [rsp+88h+var_68]
		#add     ecx, r11d
		#rol     r9d, 1Eh
		#lea     r11d, [rcx+rdx-70E44324h]
		#rol     r15d, 1
		#xor     r14d, ebp
		#xor     r14d, edi
		#mov     ecx, r9d
		#mov     eax, r9d
		#or      ecx, r10d
		#and     eax, r10d
		#mov     edx, r11d
		#and     ecx, r8d
		#rol     edx, 5
		#mov     [rsp+88h+var_78], r15d
		#or      ecx, eax
		#add     ecx, r15d
		#add     ecx, ebx
		#rol     r10d, 1Eh
		#rol     r14d, 1
		#lea     ebx, [rcx+rdx-70E44324h]
		#mov     ecx, r10d
		#mov     eax, r10d
		#or      ecx, r11d
		#and     eax, r11d
		#mov     edx, ebx
		#and     ecx, r9d
		#rol     edx, 5
		#mov     [rsp+88h+var_58], r14d
		#or      ecx, eax
		#add     ecx, r14d
		#add     ecx, r8d
		#lea     r8d, [rcx+rdx-70E44324h]
		#mov     r12d, [rsp+88h+var_60]
		#mov     edi, [rsp+88h+var_80]
		#mov     esi, [rsp+88h+var_88]
		#xor     esi, [rsp+88h+var_6C]
		#xor     edi, r12d
		#mov     r12d, [rsp+88h+var_84]
		#xor     esi, [rsp+88h+var_60]
		#xor     edi, r13d
		#mov     r13d, [rsp+88h+var_64]
		#xor     edi, [rsp+88h+var_74]
		#rol     r11d, 1Eh
		#xor     r12d, r13d
		#rol     edi, 1
		#xor     r12d, ebp
		#mov     ebp, [rsp+88h+arg_8]
		#xor     ebp, [rsp+88h+arg_18]
		#xor     r12d, r15d
		#xor     esi, r14d
		#xor     ebp, r13d
		#mov     r13d, [rsp+88h+arg_10]
		#mov     ecx, r11d
		#xor     r13d, [rsp+88h+var_70]
		#or      ecx, ebx
		#xor     ebp, edi
		#xor     r13d, [rsp+88h+var_6C]
		#and     ecx, r10d
		#mov     eax, r11d
		#and     eax, ebx
		#mov     edx, r8d
		#mov     [rsp+88h+var_7C], edi
		#or      ecx, eax
		#rol     edx, 5
		#mov     eax, r8d
		#add     ecx, edi
		#add     ecx, r9d
		#rol     ebx, 1Eh
		#rol     r12d, 1
		#lea     r9d, [rcx+rdx-70E44324h]
		#and     eax, ebx
		#mov     ecx, r8d
		#or      ecx, ebx
		#mov     edx, r9d
		#xor     r13d, r12d
		#and     ecx, r11d
		#rol     edx, 5
		#mov     [rsp+88h+var_5C], r12d
		#or      ecx, eax
		#add     ecx, r12d
		#add     ecx, r10d
		#rol     r8d, 1Eh
		#rol     esi, 1
		#lea     r10d, [rcx+rdx-70E44324h]
		#mov     ecx, r8d
		#mov     eax, r8d
		#or      ecx, r9d
		#and     eax, r9d
		#mov     edx, r10d
		#and     ecx, ebx
		#rol     edx, 5
		#mov     [rsp+88h+var_64], esi
		#or      ecx, eax
		#add     ecx, esi
		#add     ecx, r11d
		#rol     r9d, 1Eh
		#rol     ebp, 1
		#lea     r11d, [rcx+rdx-70E44324h]
		#mov     ecx, r9d
		#mov     eax, r9d
		#or      ecx, r10d
		#and     eax, r10d
		#mov     edx, r11d
		#and     ecx, r8d
		#rol     edx, 5
		#mov     [rsp+88h+var_60], ebp
		#or      ecx, eax
		#add     ecx, ebp
		#add     ecx, ebx
		#rol     r10d, 1Eh
		#rol     r13d, 1
		#mov     [rsp+88h+var_6C], r13d
		#lea     edi, [rcx+rdx-70E44324h]
		#mov     ecx, r10d
		#mov     eax, r10d
		#mov     edx, edi
		#or      ecx, r11d
		#and     eax, r11d
		#rol     edx, 5
		#and     ecx, r9d
		#or      ecx, eax
		#add     ecx, r13d
		#add     ecx, r8d
		#mov     r8d, [rsp+88h+var_68]
		#rol     r11d, 1Eh
		#xor     r8d, [rsp+88h+arg_18]
		#lea     ebx, [rcx+rdx-70E44324h]
		#mov     ecx, r11d
		#or      ecx, edi
		#xor     r8d, esi
		#mov     esi, [rsp+88h+var_80]
		#xor     r8d, [rsp+88h+var_74]
		#xor     esi, [rsp+88h+var_70]
		#and     ecx, r10d
		#rol     r8d, 1
		#xor     esi, ebp
		#mov     eax, r11d
		#and     eax, edi
		#xor     esi, r15d
		#mov     r15d, [rsp+88h+var_84]
		#xor     r15d, [rsp+88h+var_68]
		#or      ecx, eax
		#mov     edx, ebx
		#add     ecx, r8d
		#rol     edx, 5
		#xor     r15d, r13d
		#add     ecx, r9d
		#rol     edi, 1Eh
		#rol     esi, 1
		#lea     r9d, [rcx+rdx-70E44324h]
		#xor     r15d, r14d
		#mov     r14d, [rsp+88h+var_88]
		#xor     r14d, [rsp+88h+var_80]
		#mov     ecx, ebx
		#mov     eax, ebx
		#or      ecx, edi
		#and     eax, edi
		#xor     r14d, r8d
		#xor     r14d, [rsp+88h+var_7C]
		#and     ecx, r11d
		#mov     edx, r9d
		#or      ecx, eax
		#rol     edx, 5
		#mov     [rsp+88h+arg_18], r8d
		#add     ecx, esi
		#mov     [rsp+88h+var_70], esi
		#add     ecx, r10d
		#rol     ebx, 1Eh
		#rol     r15d, 1
		#lea     r10d, [rcx+rdx-70E44324h]
		#mov     ecx, ebx
		#mov     eax, ebx
		#or      ecx, r9d
		#and     eax, r9d
		#mov     edx, r10d
		#and     ecx, edi
		#rol     edx, 5
		#mov     [rsp+88h+var_68], r15d
		#or      ecx, eax
		#add     ecx, r15d
		#add     ecx, r11d
		#rol     r9d, 1Eh
		#rol     r14d, 1
		#lea     r11d, [rcx+rdx-70E44324h]
		#mov     ecx, r9d
		#mov     eax, r9d
		#or      ecx, r10d
		#and     eax, r10d
		#mov     edx, r11d
		#and     ecx, ebx
		#rol     edx, 5
		#mov     [rsp+88h+var_80], r14d
		#or      ecx, eax
		#add     ecx, r14d
		#add     ecx, edi
		#mov     edi, [rsp+88h+arg_8]
		#rol     r10d, 1Eh
		#lea     r8d, [rcx+rdx-70E44324h]
		#mov     ebp, edi
		#xor     edi, r14d
		#xor     ebp, [rsp+88h+var_84]
		#xor     edi, [rsp+88h+var_60]
		#mov     eax, r9d
		#xor     eax, r10d
		#xor     ebp, esi
		#mov     ecx, r8d
		#xor     eax, r11d
		#xor     ebp, r12d
		#mov     r12d, [rsp+88h+arg_10]
		#xor     r12d, [rsp+88h+var_88]
		#rol     ebp, 1
		#rol     ecx, 5
		#add     eax, ebp
		#xor     r12d, r15d
		#mov     [rsp+88h+var_84], ebp
		#xor     r12d, [rsp+88h+var_64]
		#add     eax, ebx
		#mov     ebx, [rsp+88h+var_74]
		#lea     edx, [rax+rcx-359D3E2Ah]
		#rol     r11d, 1Eh
		#xor     edi, ebx
		#rol     r12d, 1
		#mov     eax, r10d
		#mov     ecx, edx
		#xor     eax, r11d
		#rol     ecx, 5
		#mov     [rsp+88h+var_88], r12d
		#xor     eax, r8d
		#add     eax, r12d
		#add     eax, r9d
		#rol     r8d, 1Eh
		#rol     edi, 1
		#lea     r9d, [rax+rcx-359D3E2Ah]
		#mov     [rsp+88h+arg_8], edi
		#mov     eax, edx
		#xor     eax, r11d
		#mov     ecx, r9d
		#xor     eax, r8d
		#rol     ecx, 5
		#add     eax, edi
		#mov     edi, [rsp+88h+arg_10]
		#add     eax, r10d
		#xor     edi, ebp
		#rol     edx, 1Eh
		#lea     r10d, [rax+rcx-359D3E2Ah]
		#xor     edi, r13d
		#mov     eax, edx
		#xor     edi, [rsp+88h+var_78]
		#xor     eax, r9d
		#mov     ecx, r10d
		#xor     eax, r8d
		#rol     edi, 1
		#rol     ecx, 5
		#add     eax, edi
		#mov     r13d, r12d
		#mov     [rsp+88h+arg_10], edi
		#xor     r13d, [rsp+88h+arg_18]
		#mov     edi, [rsp+88h+var_58]
		#add     eax, r11d
		#lea     r11d, [rax+rcx-359D3E2Ah]
		#rol     r9d, 1Eh
		#xor     r13d, edi
		#xor     r13d, ebx
		#mov     ebx, [rsp+88h+arg_8]
		#mov     eax, edx
		#xor     eax, r9d
		#rol     r13d, 1
		#mov     ecx, r11d
		#xor     eax, r10d
		#rol     ecx, 5
		#mov     [rsp+88h+var_74], r13d
		#add     eax, r13d
		#add     eax, r8d
		#rol     r10d, 1Eh
		#lea     r8d, [rax+rcx-359D3E2Ah]
		#xor     r12d, [rsp+88h+var_6C]
		#xor     ebx, esi
		#mov     esi, [rsp+88h+arg_10]
		#xor     ebx, [rsp+88h+var_7C]
		#xor     esi, r15d
		#mov     r15d, [rsp+88h+var_60]
		#xor     ebx, [rsp+88h+var_78]
		#xor     esi, [rsp+88h+var_5C]
		#xor     ebp, r15d
		#xor     ebp, [rsp+88h+var_5C]
		#rol     ebx, 1
		#xor     esi, edi
		#xor     ebp, ebx
		#mov     edi, r14d
		#mov     r14d, [rsp+88h+var_64]
		#xor     edi, r14d
		#xor     r12d, r14d
		#mov     r14d, [rsp+88h+arg_8]
		#xor     edi, [rsp+88h+var_7C]
		#mov     eax, r9d
		#mov     ecx, r8d
		#xor     eax, r10d
		#rol     ecx, 5
		#xor     edi, r13d
		#xor     eax, r11d
		#mov     [rsp+88h+var_78], ebx
		#add     eax, ebx
		#add     eax, edx
		#rol     r11d, 1Eh
		#rol     esi, 1
		#lea     edx, [rax+rcx-359D3E2Ah]
		#xor     r12d, esi
		#mov     eax, r10d
		#xor     eax, r11d
		#mov     ecx, edx
		#xor     eax, r8d
		#rol     ecx, 5
		#add     eax, esi
		#add     eax, r9d
		#rol     r8d, 1Eh
		#rol     edi, 1
		#lea     r9d, [rax+rcx-359D3E2Ah]
		#mov     eax, edx
		#mov     [rsp+88h+var_58], edi
		#xor     eax, r11d
		#mov     ecx, r9d
		#xor     eax, r8d
		#rol     ecx, 5
		#add     eax, edi
		#add     eax, r10d
		#rol     edx, 1Eh
		#rol     ebp, 1
		#lea     r10d, [rax+rcx-359D3E2Ah]
		#mov     eax, edx
		#mov     [rsp+88h+var_5C], ebp
		#xor     eax, r9d
		#mov     ecx, r10d
		#xor     eax, r8d
		#rol     ecx, 5
		#add     eax, ebp
		#add     eax, r11d
		#rol     r9d, 1Eh
		#rol     r12d, 1
		#lea     r11d, [rax+rcx-359D3E2Ah]
		#mov     eax, edx
		#mov     [rsp+88h+var_7C], r12d
		#xor     eax, r9d
		#mov     ecx, r11d
		#xor     eax, r10d
		#rol     ecx, 5
		#add     eax, r12d
		#add     eax, r8d
		#mov     r8d, [rsp+88h+arg_18]
		#rol     r10d, 1Eh
		#xor     r14d, r8d
		#lea     ebx, [rax+rcx-359D3E2Ah]
		#xor     r14d, r15d
		#mov     ecx, ebx
		#xor     r14d, edi
		#rol     r14d, 1
		#rol     ecx, 5
		#mov     r15d, [rsp+88h+arg_10]
		#mov     eax, r9d
		#xor     r15d, [rsp+88h+var_70]
		#xor     eax, r10d
		#xor     r15d, [rsp+88h+var_6C]
		#xor     eax, r11d
		#add     eax, r14d
		#xor     r15d, ebp
		#add     eax, edx
		#rol     r11d, 1Eh
		#rol     r15d, 1
		#lea     edi, [rax+rcx-359D3E2Ah]
		#mov     eax, r10d
		#xor     eax, r11d
		#mov     ecx, edi
		#xor     eax, ebx
		#rol     ecx, 5
		#add     eax, r15d
		#add     eax, r9d
		#mov     r9d, [rsp+88h+var_68]
		#rol     ebx, 1Eh
		#lea     ebp, [rax+rcx-359D3E2Ah]
		#mov     edx, r9d
		#mov     eax, edi
		#xor     eax, r11d
		#xor     edx, r8d
		#mov     ecx, ebp
		#xor     eax, ebx
		#xor     edx, r12d
		#xor     edx, r13d
		#rol     edx, 1
		#rol     ecx, 5
		#add     eax, edx
		#add     eax, r10d
		#mov     r10d, [rsp+88h+var_80]
		#rol     edi, 1Eh
		#lea     r12d, [rax+rcx-359D3E2Ah]
		#mov     r8d, r10d
		#mov     eax, edi
		#xor     r8d, [rsp+88h+var_70]
		#xor     eax, ebp
		#mov     ecx, r12d
		#xor     eax, ebx
		#xor     r8d, r14d
		#xor     r8d, [rsp+88h+var_78]
		#rol     r8d, 1
		#rol     ecx, 5
		#add     eax, r8d
		#add     eax, r11d
		#mov     r11d, [rsp+88h+var_84]
		#rol     ebp, 1Eh
		#lea     r13d, [rax+rcx-359D3E2Ah]
		#xor     r11d, r9d
		#mov     r9d, [rsp+88h+var_88]
		#xor     r11d, r15d
		#xor     r9d, r10d
		#mov     r10d, [rsp+88h+arg_8]
		#xor     r11d, esi
		#xor     r9d, edx
		#mov     eax, edi
		#xor     r9d, [rsp+88h+var_58]
		#xor     eax, ebp
		#rol     r11d, 1
		#xor     eax, r12d
		#mov     ecx, r13d
		#add     eax, r11d
		#rol     ecx, 5
		#add     eax, ebx
		#rol     r12d, 1Eh
		#rol     r9d, 1
		#lea     esi, [rax+rcx-359D3E2Ah]
		#mov     eax, ebp
		#xor     eax, r12d
		#mov     ecx, esi
		#xor     eax, r13d
		#rol     ecx, 5
		#add     eax, r9d
		#add     eax, edi
		#rol     r13d, 1Eh
		#xor     r10d, [rsp+88h+var_84]
		#lea     edi, [rax+rcx-359D3E2Ah]
		#xor     r10d, r8d
		#mov     ecx, edi
		#mov     eax, r12d
		#xor     r10d, [rsp+88h+var_5C]
		#xor     eax, r13d
		#xor     eax, esi
		#rol     r10d, 1
		#rol     ecx, 5
		#add     eax, r10d
		#add     eax, ebp
		#mov     ebp, [rsp+88h+arg_10]
		#rol     esi, 1Eh
		#lea     ebx, [rax+rcx-359D3E2Ah]
		#mov     edx, ebp
		#xor     ebp, r10d
		#xor     edx, [rsp+88h+var_88]
		#xor     ebp, r15d
		#mov     eax, edi
		#xor     ebp, [rsp+88h+var_78]
		#xor     eax, r13d
		#xor     edx, r11d
		#xor     edx, [rsp+88h+var_7C]
		#xor     eax, esi
		#mov     ecx, ebx
		#rol     edx, 1
		#rol     ecx, 5
		#add     eax, edx
		#mov     edx, [rsp+88h+arg_8]
		#add     eax, r12d
		#xor     edx, r9d
		#mov     r9, [rsp+88h+arg_0]
		#lea     r8d, [rax+rcx-359D3E2Ah]
		#xor     edx, r14d
		#rol     edi, 1Eh
		#xor     edx, [rsp+88h+var_74]
		#mov     ecx, r8d
		#mov     eax, edi
		#xor     eax, ebx
		#rol     edx, 1
		#rol     ecx, 5
		#xor     eax, esi
		#add     eax, edx
		#add     eax, r13d
		#rol     ebx, 1Eh
		#rol     ebp, 1
		#lea     edx, [rax+rcx-359D3E2Ah]
		#mov     ecx, [r9]
		#mov     eax, edx
		#rol     eax, 5
		#add     ebp, eax
		#mov     eax, edi
		#xor     eax, ebx
		#xor     eax, r8d
		#add     eax, esi
		#lea     eax, [rax+rbp-359D3E2Ah]
		#add     ecx, eax
		#mov     eax, [r9+4]
		#add     eax, edx
		#rol     r8d, 1Eh
		#mov     [r9], ecx
		#add     r8d, [r9+8]
		#mov     [r9+4], eax
		#mov     eax, [r9+0Ch]
		#add     eax, ebx
		#mov     [r9+8], r8d
		#mov     [r9+0Ch], eax
		#mov     eax, [r9+10h]
		#add     eax, edi
		#mov     [r9+10h], eax
		#add     rsp, 48h
		#pop     r15
		#pop     r14
		#pop     r13
		#pop     r12
		#pop     rdi
		#pop     rsi
		#pop     rbp
		#pop     rbx
		#retn


  def test_gadget_sub_78E5D488(self):
		#sub_78E5D488
		gadget = "834A182083C8FFC3"
		self.do(gadget)

		#or      dword ptr [rdx+18h], 20h
		#or      eax, 0FFFFFFFFh
		#retn


  def test_gadget_sub_78E5D4A4(self):
		#sub_78E5D4A4
		gadget = "834A1820B8FFFF0000C3"
		self.do(gadget)

		#or      dword ptr [rdx+18h], 20h
		#mov     eax, 0FFFFh
		#retn


  def test_gadget_RtlCopyLuid(self):
		#RtlCopyLuid
		gadget = "488B02488901C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#retn


  def test_gadget_sub_78E60FE0(self):
		#sub_78E60FE0
		gadget = "33C0890189410489410889410C894110C60101C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [rcx], eax
		#mov     [rcx+4], eax
		#mov     [rcx+8], eax
		#mov     [rcx+0Ch], eax
		#mov     [rcx+10h], eax
		#mov     byte ptr [rcx], 1
		#retn


  def test_gadget_AlpcMaxAllowedMessageLength(self):
		#AlpcMaxAllowedMessageLength
		gadget = "48C7C0FFFF0000C3"
		self.do(gadget)

		#mov     rax, 0FFFFh
		#retn


  def test_gadget_RtlQueryDepthSList(self):
		#RtlQueryDepthSList
		gadget = "668B01C3"
		self.do(gadget)

		#mov     ax, [rcx]
		#retn


  def test_gadget_nullsub_1(self):
		#nullsub_1
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_isdigit(self):
		#isdigit
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B053BD311000FB7044883E004C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 4
		#retn


  def test_gadget___isascii(self):
		#__isascii
		gadget = "33C081F9800000000F92C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     ecx, 80h
		#setb    al
		#retn


  def test_gadget_sub_78E67264(self):
		#sub_78E67264
		gadget = "488B0585D21100C3"
		self.do(gadget)

		#mov     rax, cs:off_78F844F0
		#retn


  def test_gadget_isxdigit(self):
		#isxdigit
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B0573CC11000FB704482580000000C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 80h
		#retn


  def test_gadget_RtlInitializeBitMap(self):
		#RtlInitializeBitMap
		gadget = "44890148895108C3"
		self.do(gadget)

		#mov     [rcx], r8d
		#mov     [rcx+8], rdx
		#retn


  def test_gadget_RtlIdentifierAuthoritySid(self):
		#RtlIdentifierAuthoritySid
		gadget = "488D4102C3"
		self.do(gadget)

		#lea     rax, [rcx+2]
		#retn


  def test_gadget_RtlIsGenericTableEmpty(self):
		#RtlIsGenericTableEmpty
		gadget = "33C04839010F94C0C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [rcx], rax
		#setz    al
		#retn


  def test_gadget_RtlPopFrame(self):
		#RtlPopFrame
		gadget = "65488B142530000000488B4108488982C0170000C3"
		self.do(gadget)

		#mov     rdx, gs:30h
		#mov     rax, [rcx+8]
		#mov     [rdx+17C0h], rax
		#retn


  def test_gadget_RtlPushFrame(self):
		#RtlPushFrame
		gadget = "65488B142530000000488B82C01700004889410848898AC0170000C3"
		self.do(gadget)

		#mov     rdx, gs:30h
		#mov     rax, [rdx+17C0h]
		#mov     [rcx+8], rax
		#mov     [rdx+17C0h], rcx
		#retn


  def test_gadget_RtlNumberGenericTableElements(self):
		#RtlNumberGenericTableElements
		gadget = "8B4124C3"
		self.do(gadget)

		#mov     eax, [rcx+24h]
		#retn


  def test_gadget_RtlGetCurrentTransaction(self):
		#RtlGetCurrentTransaction
		gadget = "65488B042530000000488B80B8170000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rax, [rax+17B8h]
		#retn


  def test_gadget_RtlLengthSid(self):
		#RtlLengthSid
		gadget = "0FB641018D048508000000C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx+1]
		#lea     eax, ds:8[rax*4]
		#retn


  def test_gadget_RtlSubAuthoritySid(self):
		#RtlSubAuthoritySid
		gadget = "8BC2488D448108C3"
		self.do(gadget)

		#mov     eax, edx
		#lea     rax, [rcx+rax*4+8]
		#retn


  def test_gadget_sub_78E7EB70(self):
		#sub_78E7EB70
		gadget = "F6D10FB6C183E001C3"
		self.do(gadget)

		#not     cl
		#movzx   eax, cl
		#and     eax, 1
		#retn


  def test_gadget_RtlSubAuthorityCountSid(self):
		#RtlSubAuthorityCountSid
		gadget = "488D4101C3"
		self.do(gadget)

		#lea     rax, [rcx+1]
		#retn


  def test_gadget_sub_78E834D0(self):
		#sub_78E834D0
		gadget = "48895424104C894424184C894C2420C3"
		self.do(gadget)

		#mov     [rsp+arg_8], rdx
		#mov     [rsp+arg_10], r8
		#mov     [rsp+arg_18], r9
		#retn


  def test_gadget_RtlRunOnceInitialize(self):
		#RtlRunOnceInitialize
		gadget = "48C70100000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0; RtlInitializeConditionVariable
		#retn


  def test_gadget_RtlRandomEx(self):
		#RtlRandomEx
		gadget = "FFF34883EC20488BD9488D0D90CC0F004533C033D2E88600000085C00F88E5DF02003D030100000F840D610000448B0B448B058D480F0048B805000000020000004183E07F4D69C9EDFFFF7F4981C1C3FFFF7F498BC949F7E1488D0550CC0F00482BCA48D1E94803CA48C1E91E4869C9FFFFFF7F4C2BC944890B46870C80418BC9F00FC10D3B480F00418BC14883C4205BC3488D0D5F6B0F004533C033D2E8350000004533C0488D0D4B6B0F0085C00F84D87E020033D2E88C55FFFF85C00F89C19EFFFFE9AD7E0200488D5424308BC8C644243000E8D882050090E90F20FDFF488D5424308BC8C644243001E8C182050090E9F81FFDFFBA04000000E8B1D6FCFF85C00F89E61FFDFF488D5424308BC8C644243002E89882050090E9CF1FFDFF"
		self.do(gadget)

		#push    rbx
		#sub     rsp, 20h
		#mov     rbx, rcx
		#lea     rcx, RunOnce    ; RunOnce
		#xor     r8d, r8d        ; Context
		#xor     edx, edx        ; Flags
		#call    RtlRunOnceBeginInitialize
		#test    eax, eax
		#js      loc_78EB8757
		#cmp     eax, 103h
		#jz      loc_78E9088A
		#mov     r9d, [rbx]
		#mov     r8d, cs:dword_78F7F014
		#mov     rax, 200000005h
		#and     r8d, 7Fh
		#imul    r9, 7FFFFFEDh
		#add     r9, 7FFFFFC3h
		#mov     rcx, r9
		#mul     r9
		#lea     rax, unk_78F87400
		#sub     rcx, rdx
		#shr     rcx, 1
		#add     rcx, rdx
		#shr     rcx, 1Eh
		#imul    rcx, 7FFFFFFFh
		#sub     r9, rcx
		#mov     [rbx], r9d
		#xchg    r9d, [rax+r8*4]
		#mov     ecx, r9d
		#lock xadd cs:dword_78F7F014, ecx
		#mov     eax, r9d
		#add     rsp, 20h
		#pop     rbx
		#retn
		#lea     rcx, RunOnce
		#xor     r8d, r8d
		#xor     edx, edx
		#call    sub_78E908D0
		#xor     r8d, r8d        ; Context
		#lea     rcx, RunOnce    ; RunOnce
		#test    eax, eax
		#jz      loc_78EB8785
		#xor     edx, edx        ; Flags
		#call    RtlRunOnceComplete
		#test    eax, eax
		#jns     loc_78E8A77D
		#jmp     loc_78EB876E
		#lea     rdx, [rsp+28h+arg_0]
		#mov     ecx, eax
		#mov     [rsp+28h+arg_0], 0
		#call    sub_78F10A40
		#nop
		#jmp     loc_78E8A77D
		#lea     rdx, [rsp+28h+arg_0]
		#mov     ecx, eax
		#mov     [rsp+28h+arg_0], 1
		#call    sub_78F10A40
		#nop
		#jmp     loc_78E8A77D
		#mov     edx, 4          ; Flags
		#call    RtlRunOnceComplete
		#test    eax, eax
		#jns     loc_78E8A77D
		#lea     rdx, [rsp+28h+arg_0]
		#mov     ecx, eax
		#mov     [rsp+28h+arg_0], 2
		#call    sub_78F10A40
		#nop
		#jmp     loc_78E8A77D


  def test_gadget_RtlGetNtGlobalFlags(self):
		#RtlGetNtGlobalFlags
		gadget = "65488B042530000000488B48608B81BC000000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rcx, [rax+60h]
		#mov     eax, [rcx+0BCh]
		#retn


  def test_gadget_sub_78E8EC40(self):
		#sub_78E8EC40
		gadget = "8B0566060F0033D283B9B8000000010F44C2890554060F00C3"
		self.do(gadget)

		#mov     eax, cs:dword_78F7F2AC
		#xor     edx, edx
		#cmp     dword ptr [rcx+0B8h], 1
		#cmovz   eax, edx
		#mov     cs:dword_78F7F2AC, eax
		#retn


  def test_gadget_sub_78E8EC60(self):
		#sub_78E8EC60
		gadget = "8B054A060F0033D283B9B8000000010F44C2890538060F00C3"
		self.do(gadget)

		#mov     eax, cs:dword_78F7F2B0
		#xor     edx, edx
		#cmp     dword ptr [rcx+0B8h], 1
		#cmovz   eax, edx
		#mov     cs:dword_78F7F2B0, eax
		#retn


  def test_gadget_sub_78E904C0(self):
		#sub_78E904C0
		gadget = "BA400000000FB6C13ACA0F47C2830DA0EB0E00FF33C90FB6C048890D80EB0E0048890D81EB0E00890D8BED0E00890D89ED0E00890D8BED0E00890571EB0E00C3"
		self.do(gadget)

		#mov     edx, 40h
		#movzx   eax, cl
		#cmp     cl, dl
		#cmova   eax, edx
		#or      cs:dword_78F7F074, 0FFFFFFFFh
		#xor     ecx, ecx
		#movzx   eax, al
		#mov     cs:qword_78F7F060, rcx
		#mov     cs:qword_78F7F068, rcx
		#mov     cs:dword_78F7F278, ecx
		#mov     cs:dword_78F7F27C, ecx
		#mov     cs:dword_78F7F284, ecx
		#mov     cs:dword_78F7F070, eax
		#retn


  def test_gadget_RtlUniform(self):
		#RtlUniform
		gadget = "448B0948B805000000020000004D69C9EDFFFF7F4981C1C3FFFF7F4D8BC149F7E14C2BC249D1E84C03C249C1E81E4D69C0FFFFFF7F4D2BC8448909418BC1C3"
		self.do(gadget)

		#mov     r9d, [rcx]
		#mov     rax, 200000005h
		#imul    r9, 7FFFFFEDh
		#add     r9, 7FFFFFC3h
		#mov     r8, r9
		#mul     r9
		#sub     r8, rdx
		#shr     r8, 1
		#add     r8, rdx
		#shr     r8, 1Eh
		#imul    r8, 7FFFFFFFh
		#sub     r9, r8
		#mov     [rcx], r9d
		#mov     eax, r9d
		#retn


  def test_gadget_RtlInitializeHandleTable(self):
		#RtlInitializeHandleTable
		gadget = "33C0498900498940084989401049894018498940204989402841890841895004C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [r8], rax
		#mov     [r8+8], rax
		#mov     [r8+10h], rax
		#mov     [r8+18h], rax
		#mov     [r8+20h], rax
		#mov     [r8+28h], rax
		#mov     [r8], ecx
		#mov     [r8+4], edx
		#retn


  def test_gadget_RtlSetThreadPoolStartFunc(self):
		#RtlSetThreadPoolStartFunc
		gadget = "48890D69DC0E004889156ADC0E0033C0C3"
		self.do(gadget)

		#mov     cs:off_78F7F320, rcx
		#mov     cs:off_78F7F328, rdx
		#xor     eax, eax
		#retn


  def test_gadget_LdrSetDllManifestProber(self):
		#LdrSetDllManifestProber
		gadget = "48890D69DC0E004889151A620F004C890563DC0E00C3"
		self.do(gadget)

		#mov     cs:qword_78F7F340, rcx
		#mov     cs:qword_78F878F8, rdx
		#mov     cs:qword_78F7F348, r8
		#retn


  def test_gadget_RtlInitializeGenericTable(self):
		#RtlInitializeGenericTable
		gadget = "488D41084533D24C89114889400848890048894118488B4424284489512444895120488951284C894130488941404C894938C3"
		self.do(gadget)

		#lea     rax, [rcx+8]
		#xor     r10d, r10d
		#mov     [rcx], r10
		#mov     [rax+8], rax
		#mov     [rax], rax
		#mov     [rcx+18h], rax
		#mov     rax, [rsp+arg_20]
		#mov     [rcx+24h], r10d
		#mov     [rcx+20h], r10d
		#mov     [rcx+28h], rdx
		#mov     [rcx+30h], r8
		#mov     [rcx+40h], rax
		#mov     [rcx+38h], r9
		#retn


  def test_gadget_RtlReleaseMemoryStream(self):
		#RtlReleaseMemoryStream
		gadget = "33C0C3"
		self.do(gadget)

		#xor     eax, eax        ; CsrIdentifyAlertableThread
		#retn


  def test_gadget_RtlDecodeSystemPointer(self):
		#RtlDecodeSystemPointer
		gadget = "448B04253003FE7F4C8BC9B940000000418BD0418BC083E23F2BCA49D3C94933C1C3"
		self.do(gadget)

		#mov     r8d, ds:7FFE0330h
		#mov     r9, rcx
		#mov     ecx, 40h
		#mov     edx, r8d
		#mov     eax, r8d
		#and     edx, 3Fh
		#sub     ecx, edx
		#ror     r9, cl
		#xor     rax, r9
		#retn


  def test_gadget_RtlEncodeSystemPointer(self):
		#RtlEncodeSystemPointer
		gadget = "8B04253003FE7F488BD18BC84833C283E13F48D3C8C3"
		self.do(gadget)

		#mov     eax, ds:7FFE0330h
		#mov     rdx, rcx
		#mov     ecx, eax
		#xor     rax, rdx
		#and     ecx, 3Fh
		#ror     rax, cl
		#retn


  def test_gadget_LdrProcessInitializationComplete(self):
		#LdrProcessInitializationComplete
		gadget = "F0830524520E0001C3"
		self.do(gadget)

		#lock add cs:dword_78F7F01C, 1
		#retn


  def test_gadget_nullsub_2(self):
		#nullsub_2
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_RtlGetCurrentProcessorNumber(self):
		#RtlGetCurrentProcessorNumber
		gadget = "B8530000000F03C0C1E80EC3"
		self.do(gadget)

		#mov     eax, 53h
		#lsl     eax, eax
		#shr     eax, 0Eh
		#retn


  def test_gadget_RtlGetCurrentProcessorNumberEx(self):
		#RtlGetCurrentProcessorNumberEx
		gadget = "B8530000000F03C0668BD06681E2FF03668911C1E80E66894102C3"
		self.do(gadget)

		#mov     eax, 53h
		#lsl     eax, eax
		#mov     dx, ax
		#and     dx, 3FFh
		#mov     [rcx], dx
		#shr     eax, 0Eh
		#mov     [rcx+2], ax
		#retn


  def test_gadget_RtlpUmsThreadYield(self):
		#RtlpUmsThreadYield
		gadget = "65488B1425A01400000FBAB2F0040000054C8D42104C8BD24981C27F0500004983E2C066410F7FB20001000066410F7FBA1001000066450F7F822001000066450F7F8A3001000066450F7F924001000066450F7F9A5001000066450F7FA26001000066450F7FAA7001000066450F7FB28001000066450F7FBA90010000410FAE5A18DBE29B41D93A498998900000004989A8A00000004989B0A80000004989B8B00000004D89A0D80000004D89A8E00000004D89B0E80000004D89B8F00000004C8D4C24084D8988980000004C8B0C244D8988F80000004C8B922005000066458B5A50418EEBF04883A2F804000003"
		self.do(gadget)

		#mov     rdx, gs:14A0h
		#btr     dword ptr [rdx+4F0h], 5
		#lea     r8, [rdx+10h]
		#mov     r10, rdx
		#add     r10, 57Fh
		#and     r10, 0FFFFFFFFFFFFFFC0h
		#movdqa  xmmword ptr [r10+100h], xmm6
		#movdqa  xmmword ptr [r10+110h], xmm7
		#movdqa  xmmword ptr [r10+120h], xmm8
		#movdqa  xmmword ptr [r10+130h], xmm9
		#movdqa  xmmword ptr [r10+140h], xmm10
		#movdqa  xmmword ptr [r10+150h], xmm11
		#movdqa  xmmword ptr [r10+160h], xmm12
		#movdqa  xmmword ptr [r10+170h], xmm13
		#movdqa  xmmword ptr [r10+180h], xmm14
		#movdqa  xmmword ptr [r10+190h], xmm15
		#stmxcsr dword ptr [r10+18h]
		#fnclex
		#fstcw   word ptr [r10]
		#mov     [r8+90h], rbx
		#mov     [r8+0A0h], rbp
		#mov     [r8+0A8h], rsi
		#mov     [r8+0B0h], rdi
		#mov     [r8+0D8h], r12
		#mov     [r8+0E0h], r13
		#mov     [r8+0E8h], r14
		#mov     [r8+0F0h], r15
		#lea     r9, [rsp+arg_0]
		#mov     [r8+98h], r9
		#mov     r9, [rsp+0]
		#mov     [r8+0F8h], r9
		#mov     r10, [rdx+520h]
		#mov     r11w, [r10+50h]
		#mov     gs, r11d
		#lock and qword ptr [rdx+4F8h], 3


  def test_gadget_DbgBreakPoint(self):
		#DbgBreakPoint
		gadget = "CCC3"
		self.do(gadget)

		#int     3               ; Trap to Debugger
		#retn


  def test_gadget_DbgUserBreakPoint(self):
		#DbgUserBreakPoint
		gadget = "CCC3"
		self.do(gadget)

		#int     3               ; Trap to Debugger
		#retn


  def test_gadget_sub_78E9C6B0(self):
		#sub_78E9C6B0
		gadget = "CCC3"
		self.do(gadget)

		#int     3               ; Trap to Debugger
		#retn


  def test_gadget_sub_78E9C6BC(self):
		#sub_78E9C6BC
		gadget = "458BC8448BC2668B11488B4908B801000000CD2DCCC3"
		self.do(gadget)

		#mov     r9d, r8d
		#mov     r8d, edx
		#mov     dx, [rcx]
		#mov     rcx, [rcx+8]
		#mov     eax, 1
		#int     2Dh             ; Windows NT - eax = 1: debug print
		#int     3               ; Trap to Debugger
		#retn


  def test_gadget_sub_78E9C6DC(self):
		#sub_78E9C6DC
		gadget = "66448B4A024C8B4208668B11488B4908B802000000CD2DCCC3"
		self.do(gadget)

		#mov     r9w, [rdx+2]
		#mov     r8, [rdx+8]
		#mov     dx, [rcx]
		#mov     rcx, [rcx+8]
		#mov     eax, 2
		#int     2Dh             ; Windows NT - eax = 2: debug prompt
		#int     3               ; Trap to Debugger
		#retn


  def test_gadget_RtlCaptureContext(self):
		#RtlCaptureContext
		gadget = "9C8C49388C593A8C413C8C51428C613E8C694048894178488989800000004889918800000048899990000000488D442410488981980000004889A9A00000004889B1A80000004889B9B00000004C8981B80000004C8989C00000004C8991C80000004C8999D00000004C89A1D80000004C89A9E00000004C89B1E80000004C89B9F00000000FAE81000100000F2981A00100000F2989B00100000F2991C00100000F2999D00100000F29A1E00100000F29A9F00100000F29B1000200000F29B910020000440F298120020000440F298930020000440F299140020000440F299950020000440F29A160020000440F29A970020000440F29B180020000440F29B9900200000FAE5934488B442408488981F80000008B0424894144C741300F0010004883C408C3"
		self.do(gadget)

		#pushfq
		#mov     word ptr [rcx+38h], cs
		#mov     word ptr [rcx+3Ah], ds
		#mov     word ptr [rcx+3Ch], es
		#mov     word ptr [rcx+42h], ss
		#mov     word ptr [rcx+3Eh], fs
		#mov     word ptr [rcx+40h], gs
		#mov     [rcx+78h], rax
		#mov     [rcx+80h], rcx
		#mov     [rcx+88h], rdx
		#mov     [rcx+90h], rbx
		#lea     rax, [rsp+8+arg_0]
		#mov     [rcx+98h], rax
		#mov     [rcx+0A0h], rbp
		#mov     [rcx+0A8h], rsi
		#mov     [rcx+0B0h], rdi
		#mov     [rcx+0B8h], r8
		#mov     [rcx+0C0h], r9
		#mov     [rcx+0C8h], r10
		#mov     [rcx+0D0h], r11
		#mov     [rcx+0D8h], r12
		#mov     [rcx+0E0h], r13
		#mov     [rcx+0E8h], r14
		#mov     [rcx+0F0h], r15
		#fxsave  dword ptr [rcx+100h]
		#movaps  xmmword ptr [rcx+1A0h], xmm0
		#movaps  xmmword ptr [rcx+1B0h], xmm1
		#movaps  xmmword ptr [rcx+1C0h], xmm2
		#movaps  xmmword ptr [rcx+1D0h], xmm3
		#movaps  xmmword ptr [rcx+1E0h], xmm4
		#movaps  xmmword ptr [rcx+1F0h], xmm5
		#movaps  xmmword ptr [rcx+200h], xmm6
		#movaps  xmmword ptr [rcx+210h], xmm7
		#movaps  xmmword ptr [rcx+220h], xmm8
		#movaps  xmmword ptr [rcx+230h], xmm9
		#movaps  xmmword ptr [rcx+240h], xmm10
		#movaps  xmmword ptr [rcx+250h], xmm11
		#movaps  xmmword ptr [rcx+260h], xmm12
		#movaps  xmmword ptr [rcx+270h], xmm13
		#movaps  xmmword ptr [rcx+280h], xmm14
		#movaps  xmmword ptr [rcx+290h], xmm15
		#stmxcsr dword ptr [rcx+34h]
		#mov     rax, [rsp+8]
		#mov     [rcx+0F8h], rax
		#mov     eax, [rsp+8+var_8]
		#mov     [rcx+44h], eax
		#mov     dword ptr [rcx+30h], 10000Fh
		#add     rsp, 8
		#retn


  def test_gadget__setjmpex(self):
		#_setjmpex
		gadget = "488911488959084889691848897120488979284C8961304C8969384C8971404C8979484C8D4424084C8941104C8B04244C8941500FAE5958D9795C660F7F7160660F7F797066440F7F818000000066440F7F899000000066440F7F91A000000066440F7F99B000000066440F7FA1C000000066440F7FA9D000000066440F7FB1E000000066440F7FB9F000000033C0C3"
		self.do(gadget)

		#mov     [rcx], rdx
		#mov     [rcx+8], rbx
		#mov     [rcx+18h], rbp
		#mov     [rcx+20h], rsi
		#mov     [rcx+28h], rdi
		#mov     [rcx+30h], r12
		#mov     [rcx+38h], r13
		#mov     [rcx+40h], r14
		#mov     [rcx+48h], r15
		#lea     r8, [rsp+arg_0]
		#mov     [rcx+10h], r8
		#mov     r8, [rsp+0]
		#mov     [rcx+50h], r8
		#stmxcsr dword ptr [rcx+58h]
		#fnstcw  word ptr [rcx+5Ch]
		#movdqa  xmmword ptr [rcx+60h], xmm6
		#movdqa  xmmword ptr [rcx+70h], xmm7
		#movdqa  xmmword ptr [rcx+80h], xmm8
		#movdqa  xmmword ptr [rcx+90h], xmm9
		#movdqa  xmmword ptr [rcx+0A0h], xmm10
		#movdqa  xmmword ptr [rcx+0B0h], xmm11
		#movdqa  xmmword ptr [rcx+0C0h], xmm12
		#movdqa  xmmword ptr [rcx+0D0h], xmm13
		#movdqa  xmmword ptr [rcx+0E0h], xmm14
		#movdqa  xmmword ptr [rcx+0F0h], xmm15
		#xor     eax, eax
		#retn


  def test_gadget_sub_78EA2CC0(self):
		#sub_78EA2CC0
		gadget = "B8BD066B39F7E1B8C703FB25448BCA41C1E90F458BD14569D24FC5FDFF4403D1458BC2456BC0644183C04B41F7E0442BC241D1E84403C241C1E815418BC069C05471FFFF4403D0B873B06D1641F7E28BCAC1E9078BC169C0B5050000442BD0B8E1E5AAE5456BD2644183C24B41F7E2438D04886BC019C1EA0F03C18D0482C3"
		self.do(gadget)

		#mov     eax, 396B06BDh
		#mul     ecx
		#mov     eax, 25FB03C7h
		#mov     r9d, edx
		#shr     r9d, 0Fh
		#mov     r10d, r9d
		#imul    r10d, 0FFFDC54Fh
		#add     r10d, ecx
		#mov     r8d, r10d
		#imul    r8d, 64h
		#add     r8d, 4Bh
		#mul     r8d
		#sub     r8d, edx
		#shr     r8d, 1
		#add     r8d, edx
		#shr     r8d, 15h
		#mov     eax, r8d
		#imul    eax, 0FFFF7154h
		#add     r10d, eax
		#mov     eax, 166DB073h
		#mul     r10d
		#mov     ecx, edx
		#shr     ecx, 7
		#mov     eax, ecx
		#imul    eax, 5B5h
		#sub     r10d, eax
		#mov     eax, 0E5AAE5E1h
		#imul    r10d, 64h
		#add     r10d, 4Bh
		#mul     r10d
		#lea     eax, [r8+r9*4]
		#imul    eax, 19h
		#shr     edx, 0Fh
		#add     eax, ecx
		#lea     eax, [rdx+rax*4]
		#retn


  def test_gadget_sub_78EA6B10(self):
		#sub_78EA6B10
		gadget = "894C24080FAE542408C3"
		self.do(gadget)

		#mov     [rsp+arg_0], ecx
		#ldmxcsr [rsp+arg_0]
		#retn


  def test_gadget_sub_78EA6B1A(self):
		#sub_78EA6B1A
		gadget = "0FAE5C2408B9C0FFFFFF214C24080FAE542408C3"
		self.do(gadget)

		#stmxcsr [rsp+arg_0]
		#mov     ecx, 0FFFFFFC0h
		#and     [rsp+arg_0], ecx
		#ldmxcsr [rsp+arg_0]
		#retn


  def test_gadget_sub_78EA7720(self):
		#sub_78EA7720
		gadget = "4883EC080FAE1C248B04244883C408C3"
		self.do(gadget)

		#sub     rsp, 8
		#stmxcsr [rsp+8+var_8]
		#mov     eax, [rsp+8+var_8]
		#add     rsp, 8
		#retn


  def test_gadget_nullsub_3(self):
		#nullsub_3
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_sub_78ECA310(self):
		#sub_78ECA310
		gadget = "33C0894118488901488D410848894008488900C7411C010000008B04250400FE7F488B14252003FE7F480FAFD048C1EA18895120C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     [rcx+18h], eax
		#mov     [rcx], rax
		#lea     rax, [rcx+8]
		#mov     [rax+8], rax
		#mov     [rax], rax
		#mov     dword ptr [rcx+1Ch], 1
		#mov     eax, ds:7FFE0004h
		#mov     rdx, ds:7FFE0320h
		#imul    rdx, rax
		#shr     rdx, 18h
		#mov     [rcx+20h], edx
		#retn


  def test_gadget_isupper(self):
		#isupper
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B0597990B000FB7044883E001C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 1
		#retn


  def test_gadget_islower(self):
		#islower
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B0573990B000FB7044883E002C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 2
		#retn


  def test_gadget_isspace(self):
		#isspace
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B054F990B000FB7044883E008C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 8
		#retn


  def test_gadget_ispunct(self):
		#ispunct
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B052B990B000FB7044883E010C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 10h
		#retn


  def test_gadget_isalnum(self):
		#isalnum
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B0507990B000FB704482507010000C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 107h
		#retn


  def test_gadget_isprint(self):
		#isprint
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B05DF980B000FB704482557010000C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 157h
		#retn


  def test_gadget_isgraph(self):
		#isgraph
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B05B7980B000FB704482517010000C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 117h
		#retn


  def test_gadget_iscntrl(self):
		#iscntrl
		gadget = "0FB6C183CAFF3BCA0F44C24863C8488B058F980B000FB7044883E020C3"
		self.do(gadget)

		#movzx   eax, cl
		#or      edx, 0FFFFFFFFh
		#cmp     ecx, edx
		#cmovz   eax, edx
		#movsxd  rcx, eax
		#mov     rax, cs:off_78F84310
		#movzx   eax, word ptr [rax+rcx*2]
		#and     eax, 20h
		#retn


  def test_gadget___toascii(self):
		#__toascii
		gadget = "83E17F8BC1C3"
		self.do(gadget)

		#and     ecx, 7Fh
		#mov     eax, ecx
		#retn


  def test_gadget_labs(self):
		#labs
		gadget = "8BC1F7D885C90F49C1C3"
		self.do(gadget)

		#mov     eax, ecx        ; abs
		#neg     eax
		#test    ecx, ecx
		#cmovns  eax, ecx
		#retn


  def test_gadget_sub_78ECBEC4(self):
		#sub_78ECBEC4
		gadget = "4883EC28F20F102D408B0900660F28D80F297424100F293C24F20F59D8660F28F8F20F1005BB8B0900660F28F1660F28CD660F28D3F20F59151F8C0900F20F59FE0F28742410660F28E3F20F5CC2F20F5925CE8B0900F20F59C3F20F5CCCF20F5C05EE8B0900F20F5CE9F20F59C3F20F5805668B0900F20F5CECF20F59C3F20F5C05C68B0900F20F5CEF0F283C24F20F59C3F20F59DBF20F5805368B0900F20F59C3F20F58C5F20F58C14883C428C3"
		self.do(gadget)

		#sub     rsp, 28h
		#movsd   xmm5, cs:qword_78F64A10
		#movapd  xmm3, xmm0
		#movaps  [rsp+28h+var_18], xmm6
		#movaps  [rsp+28h+var_28], xmm7
		#mulsd   xmm3, xmm0
		#movapd  xmm7, xmm0
		#movsd   xmm0, cs:qword_78F64AA8
		#movapd  xmm6, xmm1
		#movapd  xmm1, xmm5
		#movapd  xmm2, xmm3
		#mulsd   xmm2, cs:qword_78F64B20
		#mulsd   xmm7, xmm6
		#movaps  xmm6, [rsp+28h+var_18]
		#movapd  xmm4, xmm3
		#subsd   xmm0, xmm2
		#mulsd   xmm4, cs:qword_78F64AE8
		#mulsd   xmm0, xmm3
		#subsd   xmm1, xmm4
		#subsd   xmm0, cs:qword_78F64B18
		#subsd   xmm5, xmm1
		#mulsd   xmm0, xmm3
		#addsd   xmm0, cs:qword_78F64AA0
		#subsd   xmm5, xmm4
		#mulsd   xmm0, xmm3
		#subsd   xmm0, cs:qword_78F64B10
		#subsd   xmm5, xmm7
		#movaps  xmm7, [rsp+28h+var_28]
		#mulsd   xmm0, xmm3
		#mulsd   xmm3, xmm3
		#addsd   xmm0, cs:qword_78F64A98
		#mulsd   xmm0, xmm3
		#addsd   xmm0, xmm5
		#addsd   xmm0, xmm1
		#add     rsp, 28h
		#retn


  def test_gadget_sub_78ECC7A4(self):
		#sub_78ECC7A4
		gadget = "488B05457D0B000FB6D10FB704502500800000C3"
		self.do(gadget)

		#mov     rax, cs:off_78F844F0
		#movzx   edx, cl
		#movzx   eax, word ptr [rax+rdx*2]
		#and     eax, 8000h
		#retn


  def test_gadget_sub_78ED0178(self):
		#sub_78ED0178
		gadget = "488B0D71790B0033C04883C90148390DF48A0B000F94C0C3"
		self.do(gadget)

		#mov     rcx, cs:qword_78F87AF0
		#xor     eax, eax
		#or      rcx, 1
		#cmp     cs:qword_78F88C80, rcx
		#setz    al
		#retn


  def test_gadget_sub_78ED0264(self):
		#sub_78ED0264
		gadget = "33C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget_sub_78ED0314(self):
		#sub_78ED0314
		gadget = "8349180483610800488D412083200048894110C7412402000000488901C3"
		self.do(gadget)

		#or      dword ptr [rcx+18h], 4
		#and     dword ptr [rcx+8], 0
		#lea     rax, [rcx+20h]
		#and     dword ptr [rax], 0
		#mov     [rcx+10h], rax
		#mov     dword ptr [rcx+24h], 2
		#mov     [rcx], rax
		#retn


  def test_gadget_sub_78ED376C(self):
		#sub_78ED376C
		gadget = "83C8FFC3"
		self.do(gadget)

		#or      eax, 0FFFFFFFFh
		#retn


  def test_gadget_sub_78ED385C(self):
		#sub_78ED385C
		gadget = "B8FFFF0000C3"
		self.do(gadget)

		#mov     eax, 0FFFFh
		#retn


  def test_gadget_MD4Init(self):
		#MD4Init
		gadget = "33C0C70101234567C7410489ABCDEFC74108FEDCBA98C7410C76543210894110894114C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword ptr [rcx], 67452301h
		#mov     dword ptr [rcx+4], 0EFCDAB89h
		#mov     dword ptr [rcx+8], 98BADCFEh
		#mov     dword ptr [rcx+0Ch], 10325476h
		#mov     [rcx+10h], eax
		#mov     [rcx+14h], eax
		#retn


  def test_gadget_sub_78ED38A0(self):
		#sub_78ED38A0
		gadget = "48894C24085355565741544155415641574883EC28448B5904448B410C448B49084C8BD28B11418BC0418B0A418B7A10458B62204133C1894C2478897C24144123C34133C003C2418B520403C1891424418BC94133CBC1C00323C84133C903CA418BD34103C8458B420833D0C1C107448984248000000023D14133D34103D0448BC14103D1458B4A0C4433C0C1C20B44894C24084423C24433C04503C1448BC94433CA4503C3458B5A1441C1C01344895C24044523C84433C94403CF4403C88BC24133C041C1C1034123C133C24103C3458B5A1803C1418BC844899C24880000004133C9C1C00723C84133C84103CB458B5A1C03CA8BD044895C24104133D1C1C10B23D14133D14103D34103D0448BC04433C1C1C2134423C2418B5A24458B5A2C458B6A28418B7230458B7234418B6A38458B7A3C4433C0895C24184503C444895C240C4503C1448BC94433CA41C1C0034523C84433C94403CB4403C88BC24133C041C1C1074123C133C24103C503C1418BC94133C8C1C00B23C84133C84103CB03CA418BD1C1C11333D023D14133D103D64103D0448BC04433C1C1C2034423C24433C04503C64503C1448BC94433CA41C1C0074523C8458BD04433C94433D24403CD4403C841C1C10B4523D1418BC14433D24503D74403D1418BC941C1C213410BCA4123C24123C80BC8418BC2034C24788D940A9979825A418BCAC1C2030BCA23C24123C90BC803CF458D84089979825A41C1C005418BC80BCA418BC04123CA23C20BC8418BC04103CC458D8C099979825A418BC841C1C109410BC94123C123CA0BC8418BC103CE458D940A9979825A418BC941C1C20D410BCA4123C24123C80BC8418BC2030C24448D9C0A9979825A418BCA41C1C303410BCB4123C34123C90BC8034C2404418D94089979825AC1C2058BCA8BC2410BCB4123C34123CA0BC88BC203CB468D84099979825A8BCA41C1C009410BC84123C04123CB0BC8418BC04103CE458D8C0A9979825A418BC841C1C10D410BC94123C123CA0BC8418BC1038C2480000000458D940B9979825A418BC941C1C203410BCA4123C24123C80BC8038C2488000000448D9C0A9979825A41C1C305418BCB418BC3410BCA4123C24123C90BC84103CD428D9C019979825A418BCBC1C3090BCB418BC323C34123CA0BC88BC303CD428DBC099979825A8BCBC1C70D23C70BCF4123CB0BC88BC7034C2408428D94119979825A8BCFC1C20323C20BCA23CB0BC8034C2410468D84199979825A41C1C005418BC8418BC023C20BCA23CF0BC8418BC0034C240C448D8C199979825A418BC841C1C1094123C1410BC923CA0BC8418BC04133C14103CF448D94399979825A41C1C20D4133C2034424788D9410A1EBD96E418BC14133C2C1C20333C24103C4468D8400A1EBD96E41C1C009418BC0418BC84133C233C203442414468D8C08A1EBD96E41C1C10B4133C98BC133C203C6468D9410A1EBD96E418BC141C1C20F4133C24133CA038C2480000000448D9C11A1EBD96E41C1C3034133C34103C5428D9400A1EBD96EC1C2098BC24133C24133C38BCA03842488000000468D8408A1EBD96E41C1C00B4133C88BC14133C303C5468D8C10A1EBD96E418BC041C1C10F4133C14133C9030C24458D9C0BA1EBD96E41C1C3034133C3034424188D9410A1EBD96EC1C2098BC28BCA4133C14133C303442404428D9C00A1EBD96EC1C30B33CB8BC14133C34103C6468D9408A1EBD96E8BC341C1C20F4133C24133CA034C2408468D8C19A1EBD96E41C1C1034133C10344240C448D8410A1EBD96E41C1C009418BC04133C24133C1034424108D9418A1EBD96E418BC0C1C20B33C24133C14103C7428D8C10A1EBD96E4C8B542470418B02C1C10F4103C1418902418B420403C141894204418B420803C241894208418B420C4103C04189420C4883C428415F415E415D415C5F5E5D5BC3"
		self.do(gadget)

		#mov     [rsp+arg_0], rcx
		#push    rbx
		#push    rbp
		#push    rsi
		#push    rdi
		#push    r12
		#push    r13
		#push    r14
		#push    r15
		#sub     rsp, 28h
		#mov     r11d, [rcx+4]
		#mov     r8d, [rcx+0Ch]
		#mov     r9d, [rcx+8]
		#mov     r10, rdx
		#mov     edx, [rcx]
		#mov     eax, r8d
		#mov     ecx, [r10]
		#mov     edi, [r10+10h]
		#mov     r12d, [r10+20h]
		#xor     eax, r9d
		#mov     [rsp+68h+arg_8], ecx
		#mov     [rsp+68h+var_54], edi
		#and     eax, r11d
		#xor     eax, r8d
		#add     eax, edx
		#mov     edx, [r10+4]
		#add     eax, ecx
		#mov     [rsp+68h+var_68], edx
		#mov     ecx, r9d
		#xor     ecx, r11d
		#rol     eax, 3
		#and     ecx, eax
		#xor     ecx, r9d
		#add     ecx, edx
		#mov     edx, r11d
		#add     ecx, r8d
		#mov     r8d, [r10+8]
		#xor     edx, eax
		#rol     ecx, 7
		#mov     [rsp+68h+arg_10], r8d
		#and     edx, ecx
		#xor     edx, r11d
		#add     edx, r8d
		#mov     r8d, ecx
		#add     edx, r9d
		#mov     r9d, [r10+0Ch]
		#xor     r8d, eax
		#rol     edx, 0Bh
		#mov     [rsp+68h+var_60], r9d
		#and     r8d, edx
		#xor     r8d, eax
		#add     r8d, r9d
		#mov     r9d, ecx
		#xor     r9d, edx
		#add     r8d, r11d
		#mov     r11d, [r10+14h]
		#rol     r8d, 13h
		#mov     [rsp+68h+var_64], r11d
		#and     r9d, r8d
		#xor     r9d, ecx
		#add     r9d, edi
		#add     r9d, eax
		#mov     eax, edx
		#xor     eax, r8d
		#rol     r9d, 3
		#and     eax, r9d
		#xor     eax, edx
		#add     eax, r11d
		#mov     r11d, [r10+18h]
		#add     eax, ecx
		#mov     ecx, r8d
		#mov     [rsp+68h+arg_18], r11d
		#xor     ecx, r9d
		#rol     eax, 7
		#and     ecx, eax
		#xor     ecx, r8d
		#add     ecx, r11d
		#mov     r11d, [r10+1Ch]
		#add     ecx, edx
		#mov     edx, eax
		#mov     [rsp+68h+var_58], r11d
		#xor     edx, r9d
		#rol     ecx, 0Bh
		#and     edx, ecx
		#xor     edx, r9d
		#add     edx, r11d
		#add     edx, r8d
		#mov     r8d, eax
		#xor     r8d, ecx
		#rol     edx, 13h
		#and     r8d, edx
		#mov     ebx, [r10+24h]
		#mov     r11d, [r10+2Ch]
		#mov     r13d, [r10+28h]
		#mov     esi, [r10+30h]
		#mov     r14d, [r10+34h]
		#mov     ebp, [r10+38h]
		#mov     r15d, [r10+3Ch]
		#xor     r8d, eax
		#mov     [rsp+68h+var_50], ebx
		#add     r8d, r12d
		#mov     [rsp+68h+var_5C], r11d
		#add     r8d, r9d
		#mov     r9d, ecx
		#xor     r9d, edx
		#rol     r8d, 3
		#and     r9d, r8d
		#xor     r9d, ecx
		#add     r9d, ebx
		#add     r9d, eax
		#mov     eax, edx
		#xor     eax, r8d
		#rol     r9d, 7
		#and     eax, r9d
		#xor     eax, edx
		#add     eax, r13d
		#add     eax, ecx
		#mov     ecx, r9d
		#xor     ecx, r8d
		#rol     eax, 0Bh
		#and     ecx, eax
		#xor     ecx, r8d
		#add     ecx, r11d
		#add     ecx, edx
		#mov     edx, r9d
		#rol     ecx, 13h
		#xor     edx, eax
		#and     edx, ecx
		#xor     edx, r9d
		#add     edx, esi
		#add     edx, r8d
		#mov     r8d, eax
		#xor     r8d, ecx
		#rol     edx, 3
		#and     r8d, edx
		#xor     r8d, eax
		#add     r8d, r14d
		#add     r8d, r9d
		#mov     r9d, ecx
		#xor     r9d, edx
		#rol     r8d, 7
		#and     r9d, r8d
		#mov     r10d, r8d
		#xor     r9d, ecx
		#xor     r10d, edx
		#add     r9d, ebp
		#add     r9d, eax
		#rol     r9d, 0Bh
		#and     r10d, r9d
		#mov     eax, r9d
		#xor     r10d, edx
		#add     r10d, r15d
		#add     r10d, ecx
		#mov     ecx, r9d
		#rol     r10d, 13h
		#or      ecx, r10d
		#and     eax, r10d
		#and     ecx, r8d
		#or      ecx, eax
		#mov     eax, r10d
		#add     ecx, [rsp+68h+arg_8]
		#lea     edx, [rdx+rcx+5A827999h]
		#mov     ecx, r10d
		#rol     edx, 3
		#or      ecx, edx
		#and     eax, edx
		#and     ecx, r9d
		#or      ecx, eax
		#add     ecx, edi
		#lea     r8d, [r8+rcx+5A827999h]
		#rol     r8d, 5
		#mov     ecx, r8d
		#or      ecx, edx
		#mov     eax, r8d
		#and     ecx, r10d
		#and     eax, edx
		#or      ecx, eax
		#mov     eax, r8d
		#add     ecx, r12d
		#lea     r9d, [r9+rcx+5A827999h]
		#mov     ecx, r8d
		#rol     r9d, 9
		#or      ecx, r9d
		#and     eax, r9d
		#and     ecx, edx
		#or      ecx, eax
		#mov     eax, r9d
		#add     ecx, esi
		#lea     r10d, [r10+rcx+5A827999h]
		#mov     ecx, r9d
		#rol     r10d, 0Dh
		#or      ecx, r10d
		#and     eax, r10d
		#and     ecx, r8d
		#or      ecx, eax
		#mov     eax, r10d
		#add     ecx, [rsp+68h+var_68]
		#lea     r11d, [rdx+rcx+5A827999h]
		#mov     ecx, r10d
		#rol     r11d, 3
		#or      ecx, r11d
		#and     eax, r11d
		#and     ecx, r9d
		#or      ecx, eax
		#add     ecx, [rsp+68h+var_64]
		#lea     edx, [r8+rcx+5A827999h]
		#rol     edx, 5
		#mov     ecx, edx
		#mov     eax, edx
		#or      ecx, r11d
		#and     eax, r11d
		#and     ecx, r10d
		#or      ecx, eax
		#mov     eax, edx
		#add     ecx, ebx
		#lea     r8d, [rcx+r9+5A827999h]
		#mov     ecx, edx
		#rol     r8d, 9
		#or      ecx, r8d
		#and     eax, r8d
		#and     ecx, r11d
		#or      ecx, eax
		#mov     eax, r8d
		#add     ecx, r14d
		#lea     r9d, [r10+rcx+5A827999h]
		#mov     ecx, r8d
		#rol     r9d, 0Dh
		#or      ecx, r9d
		#and     eax, r9d
		#and     ecx, edx
		#or      ecx, eax
		#mov     eax, r9d
		#add     ecx, [rsp+68h+arg_10]
		#lea     r10d, [r11+rcx+5A827999h]
		#mov     ecx, r9d
		#rol     r10d, 3
		#or      ecx, r10d
		#and     eax, r10d
		#and     ecx, r8d
		#or      ecx, eax
		#add     ecx, [rsp+68h+arg_18]
		#lea     r11d, [rdx+rcx+5A827999h]
		#rol     r11d, 5
		#mov     ecx, r11d
		#mov     eax, r11d
		#or      ecx, r10d
		#and     eax, r10d
		#and     ecx, r9d
		#or      ecx, eax
		#add     ecx, r13d
		#lea     ebx, [rcx+r8+5A827999h]
		#mov     ecx, r11d
		#rol     ebx, 9
		#or      ecx, ebx
		#mov     eax, r11d
		#and     eax, ebx
		#and     ecx, r10d
		#or      ecx, eax
		#mov     eax, ebx
		#add     ecx, ebp
		#lea     edi, [rcx+r9+5A827999h]
		#mov     ecx, ebx
		#rol     edi, 0Dh
		#and     eax, edi
		#or      ecx, edi
		#and     ecx, r11d
		#or      ecx, eax
		#mov     eax, edi
		#add     ecx, [rsp+68h+var_60]
		#lea     edx, [rcx+r10+5A827999h]
		#mov     ecx, edi
		#rol     edx, 3
		#and     eax, edx
		#or      ecx, edx
		#and     ecx, ebx
		#or      ecx, eax
		#add     ecx, [rsp+68h+var_58]
		#lea     r8d, [rcx+r11+5A827999h]
		#rol     r8d, 5
		#mov     ecx, r8d
		#mov     eax, r8d
		#and     eax, edx
		#or      ecx, edx
		#and     ecx, edi
		#or      ecx, eax
		#mov     eax, r8d
		#add     ecx, [rsp+68h+var_5C]
		#lea     r9d, [rcx+rbx+5A827999h]
		#mov     ecx, r8d
		#rol     r9d, 9
		#and     eax, r9d
		#or      ecx, r9d
		#and     ecx, edx
		#or      ecx, eax
		#mov     eax, r8d
		#xor     eax, r9d
		#add     ecx, r15d
		#lea     r10d, [rcx+rdi+5A827999h]
		#rol     r10d, 0Dh
		#xor     eax, r10d
		#add     eax, [rsp+68h+arg_8]
		#lea     edx, [rax+rdx+6ED9EBA1h]
		#mov     eax, r9d
		#xor     eax, r10d
		#rol     edx, 3
		#xor     eax, edx
		#add     eax, r12d
		#lea     r8d, [rax+r8+6ED9EBA1h]
		#rol     r8d, 9
		#mov     eax, r8d
		#mov     ecx, r8d
		#xor     eax, r10d
		#xor     eax, edx
		#add     eax, [rsp+68h+var_54]
		#lea     r9d, [rax+r9+6ED9EBA1h]
		#rol     r9d, 0Bh
		#xor     ecx, r9d
		#mov     eax, ecx
		#xor     eax, edx
		#add     eax, esi
		#lea     r10d, [rax+r10+6ED9EBA1h]
		#mov     eax, r9d
		#rol     r10d, 0Fh
		#xor     eax, r10d
		#xor     ecx, r10d
		#add     ecx, [rsp+68h+arg_10]
		#lea     r11d, [rcx+rdx+6ED9EBA1h]
		#rol     r11d, 3
		#xor     eax, r11d
		#add     eax, r13d
		#lea     edx, [rax+r8+6ED9EBA1h]
		#rol     edx, 9
		#mov     eax, edx
		#xor     eax, r10d
		#xor     eax, r11d
		#mov     ecx, edx
		#add     eax, [rsp+68h+arg_18]
		#lea     r8d, [rax+r9+6ED9EBA1h]
		#rol     r8d, 0Bh
		#xor     ecx, r8d
		#mov     eax, ecx
		#xor     eax, r11d
		#add     eax, ebp
		#lea     r9d, [rax+r10+6ED9EBA1h]
		#mov     eax, r8d
		#rol     r9d, 0Fh
		#xor     eax, r9d
		#xor     ecx, r9d
		#add     ecx, [rsp+68h+var_68]
		#lea     r11d, [r11+rcx+6ED9EBA1h]
		#rol     r11d, 3
		#xor     eax, r11d
		#add     eax, [rsp+68h+var_50]
		#lea     edx, [rax+rdx+6ED9EBA1h]
		#rol     edx, 9
		#mov     eax, edx
		#mov     ecx, edx
		#xor     eax, r9d
		#xor     eax, r11d
		#add     eax, [rsp+68h+var_64]
		#lea     ebx, [rax+r8+6ED9EBA1h]
		#rol     ebx, 0Bh
		#xor     ecx, ebx
		#mov     eax, ecx
		#xor     eax, r11d
		#add     eax, r14d
		#lea     r10d, [rax+r9+6ED9EBA1h]
		#mov     eax, ebx
		#rol     r10d, 0Fh
		#xor     eax, r10d
		#xor     ecx, r10d
		#add     ecx, [rsp+68h+var_60]
		#lea     r9d, [rcx+r11+6ED9EBA1h]
		#rol     r9d, 3
		#xor     eax, r9d
		#add     eax, [rsp+68h+var_5C]
		#lea     r8d, [rax+rdx+6ED9EBA1h]
		#rol     r8d, 9
		#mov     eax, r8d
		#xor     eax, r10d
		#xor     eax, r9d
		#add     eax, [rsp+68h+var_58]
		#lea     edx, [rax+rbx+6ED9EBA1h]
		#mov     eax, r8d
		#rol     edx, 0Bh
		#xor     eax, edx
		#xor     eax, r9d
		#add     eax, r15d
		#lea     ecx, [rax+r10+6ED9EBA1h]
		#mov     r10, [rsp+68h+arg_0]
		#mov     eax, [r10]
		#rol     ecx, 0Fh
		#add     eax, r9d
		#mov     [r10], eax
		#mov     eax, [r10+4]
		#add     eax, ecx
		#mov     [r10+4], eax
		#mov     eax, [r10+8]
		#add     eax, edx
		#mov     [r10+8], eax
		#mov     eax, [r10+0Ch]
		#add     eax, r8d
		#mov     [r10+0Ch], eax
		#add     rsp, 28h
		#pop     r15
		#pop     r14
		#pop     r13
		#pop     r12
		#pop     rdi
		#pop     rsi
		#pop     rbp
		#pop     rbx
		#retn


  def test_gadget_MD5Init(self):
		#MD5Init
		gadget = "33C0C7410801234567C7410C89ABCDEFC74110FEDCBA98C74114765432108901894104C3"
		self.do(gadget)

		#xor     eax, eax
		#mov     dword ptr [rcx+8], 67452301h
		#mov     dword ptr [rcx+0Ch], 0EFCDAB89h
		#mov     dword ptr [rcx+10h], 98BADCFEh
		#mov     dword ptr [rcx+14h], 10325476h
		#mov     [rcx], eax
		#mov     [rcx+4], eax
		#retn


  def test_gadget_sub_78ED4080(self):
		#sub_78ED4080
		gadget = "48894C24085355565741544155415641574883EC28448B5104448B4908448B410C488BDA8B11418BC04133C18B0B448B73144123C28B6B1C894C24784133C003C18D8C1078A46AD78B5304418BC14133C2C1C107899424880000004103CA23C14133C103C2428D940056B7C7E8448B4308418BC233C1C1C20C448944240C03D123C24133C24103C0468D8408DB702024448B4B0C8BC233C141C1C01144898C24800000004403C24123C033C14103C1468D8C10EECEBDC1448B53108BC24133C041C1C11644895424044503C84123C133C24103C2448D9408AF0F7CF5418BC04133C141C1C2074503D14123C24133C04103C68D8C102AC687478B5318418BC14133C2C1C10C8914244103CA23C14133C103C2428D9400134630A88BC14133C2C1C21103D123C24133C203C5468D8408019546FD448B7B20448B63288B7330448B6B348B7B3841C1C0164403C28BC133C24123C033C14103C7468D8C10D8988069448B53248BC24133C041C1C10744895424104503C84123C133C24103C2448D9408AFF7448B418BC04133C141C1C20C4503D14123C24133C04103C48D8C10B15BFFFF8B532C8B5B3CC1C11189542408418BC24133C14103CA23C14133C103C2468D9C00BED75C89418BC233C141C1C3164403D94123C34133C203C6428D94082211906B8BC14133C3C1C2074103D323C233C14103C5468D8410937198FD418BC333C241C1C00C4403C24123C04133C303C7448D8C088E4379A6418BC033C241C1C1114503C84123C133C203C3428D8C182108B449418BC1C1C1164103C933C14123C04133C1038424880000008D941062251EF68BC1C1C20503D133C24123C133C1030424468D840040B340C041C1C0094403C2418BC033C223C133C203442408468D8C08515A5E26418BC041C1C10E4503C84133C123C24133C003442478448D9408AAC7B6E9418BC141C1C2144503D14133C24123C04133C14103C68D8C105D102FD6418BC2C1C1054103CA33C14123C14133C24103C4428D940053144402C1C20903D18BC233C14123C233C103C3468D840881E6A1D88BC241C1C00E4403C24133C023C133C203442404468D8C10C8FBD3E7418BC041C1C1144503C84133C123C24133C003442410448D9408E6CDE121418BC141C1C2054503D14133C24123C04133C103C78D8C10D60737C3C1C1094103CA8BC14133C24123C14133C203842480000000428D9400870DD5F4C1C20E8BC103D133C24123C233C14103C7468D9C08ED145A458BC241C1C3144403DA4133C323C133C24103C5468D841005E9E3A9418BC341C1C0054503C34133C023C24133C30344240C448D8C08F8A3EFFC41C1C1094503C8418BC1418BC94133C04123C34133C003C5448D9410D9026F6741C1C20E4503D14133CA8BC14123C04133C103C6428D94188A4C2A8D418BC2C1C2144103D233C233CA4103CE468D84014239FAFF41C1C0044403C24133C04103C7468D8C0881F6718741C1C10B4503C8418BC1418BC933C24133C003442408468D941022619D6D41C1C2104503D14133CA8BC14133C003C7448D9C100C38E5FD418BC241C1C3174503DA4133CB4133C3038C2488000000428D940144EABEA4C1C2044103D333C203442404468D8408A9CFDE4B41C1C00B4403C2418BC0418BC84133C333C203C5468D8C10604BBBF641C1C1104503C84133C98BC133C24103C4468D941870BCBFBE418BC141C1C2174503D14133C24133CA4103CD448D9C11C67E9B2841C1C3044503DA4133C303442478468D8400FA27A1EA41C1C00B4503C3418BC0418BC84133C24133C303842480000000468D8C088530EFD441C1C1104503C84133C98BC14133C3030424428D9410051D8804418BC1C1C2174103D133C233CA034C2410468D941939D0D4D941C1C2044403D24133C203C6428D8C00E599DBE6C1C10B4103CA8BC133C24133C203C3468D8408F87CA21F8BC141C1C0104403C14133C04133C20344240C448D8C106556ACC48BC1F7D041C1C1174503C8410BC14133C003442478428D9410442229F4418BC0C1C206F7D04103D10BC24133C103C5448D940897FF2A43418BC1F7D041C1C20A4403D2410BC233C203C7428D8C00A72394AB8BC2F7D0C1C10F4103CA0BC14133C24103C6468D840839A093FC418BC2F7D041C1C0154403C1410BC033C103C6448D8C10C3595B658BC1F7D041C1C1064503C8410BC14133C003842480000000428D941092CC0C8F418BC0F7D0C1C20A4103D10BC24133C14103C4448D94087DF4EFFF418BC1F7D041C1C20F4403D2410BC233C203842488000000428D8C00D15D84858BC2F7D0C1C1154103CA0BC14133C24103C7468D84084F7EA86F418BC2F7D041C1C0064403C1410BC033C103C3448D9C10E0E62CFE8BC1F7D041C1C30A4503D8410BC34133C0030424428D9410144301A3418BC0F7D0C1C20F4103D30BC24133C34103C5448D9408A111084E418BC3F7D041C1C2154403D2410BC233C203442404468D8C00827E53F78BC2F7D041C1C1064503CA410BC14133C203442408468D841835F23ABD418BC2F7D041C1C00A4503C1410BC04133C10344240C8D9410BBD2D72A418BC1F7D0C1C20F4103D00BC24133C003442410428D8C1091D386EB4C8B542470418B02C1C1154103C103CA418902418B420403C141894204418B420803C241894208418B420C4103C04189420C4883C428415F415E415D415C5F5E5D5BC3"
		self.do(gadget)

		#mov     [rsp+arg_0], rcx
		#push    rbx
		#push    rbp
		#push    rsi
		#push    rdi
		#push    r12
		#push    r13
		#push    r14
		#push    r15
		#sub     rsp, 28h
		#mov     r10d, [rcx+4]
		#mov     r9d, [rcx+8]
		#mov     r8d, [rcx+0Ch]
		#mov     rbx, rdx
		#mov     edx, [rcx]
		#mov     eax, r8d
		#xor     eax, r9d
		#mov     ecx, [rbx]
		#mov     r14d, [rbx+14h]
		#and     eax, r10d
		#mov     ebp, [rbx+1Ch]
		#mov     [rsp+68h+arg_8], ecx
		#xor     eax, r8d
		#add     eax, ecx
		#lea     ecx, [rax+rdx-28955B88h]
		#mov     edx, [rbx+4]
		#mov     eax, r9d
		#xor     eax, r10d
		#rol     ecx, 7
		#mov     [rsp+68h+arg_18], edx
		#add     ecx, r10d
		#and     eax, ecx
		#xor     eax, r9d
		#add     eax, edx
		#lea     edx, [rax+r8-173848AAh]
		#mov     r8d, [rbx+8]
		#mov     eax, r10d
		#xor     eax, ecx
		#rol     edx, 0Ch
		#mov     [rsp+68h+var_5C], r8d
		#add     edx, ecx
		#and     eax, edx
		#xor     eax, r10d
		#add     eax, r8d
		#lea     r8d, [rax+r9+242070DBh]
		#mov     r9d, [rbx+0Ch]
		#mov     eax, edx
		#xor     eax, ecx
		#rol     r8d, 11h
		#mov     [rsp+68h+arg_10], r9d
		#add     r8d, edx
		#and     eax, r8d
		#xor     eax, ecx
		#add     eax, r9d
		#lea     r9d, [rax+r10-3E423112h]
		#mov     r10d, [rbx+10h]
		#mov     eax, edx
		#xor     eax, r8d
		#rol     r9d, 16h
		#mov     [rsp+68h+var_64], r10d
		#add     r9d, r8d
		#and     eax, r9d
		#xor     eax, edx
		#add     eax, r10d
		#lea     r10d, [rax+rcx-0A83F051h]
		#mov     eax, r8d
		#xor     eax, r9d
		#rol     r10d, 7
		#add     r10d, r9d
		#and     eax, r10d
		#xor     eax, r8d
		#add     eax, r14d
		#lea     ecx, [rax+rdx+4787C62Ah]
		#mov     edx, [rbx+18h]
		#mov     eax, r9d
		#xor     eax, r10d
		#rol     ecx, 0Ch
		#mov     [rsp+68h+var_68], edx
		#add     ecx, r10d
		#and     eax, ecx
		#xor     eax, r9d
		#add     eax, edx
		#lea     edx, [rax+r8-57CFB9EDh]
		#mov     eax, ecx
		#xor     eax, r10d
		#rol     edx, 11h
		#add     edx, ecx
		#and     eax, edx
		#xor     eax, r10d
		#add     eax, ebp
		#lea     r8d, [rax+r9-2B96AFFh]
		#mov     r15d, [rbx+20h]
		#mov     r12d, [rbx+28h]
		#mov     esi, [rbx+30h]
		#mov     r13d, [rbx+34h]
		#mov     edi, [rbx+38h]
		#rol     r8d, 16h
		#add     r8d, edx
		#mov     eax, ecx
		#xor     eax, edx
		#and     eax, r8d
		#xor     eax, ecx
		#add     eax, r15d
		#lea     r9d, [rax+r10+698098D8h]
		#mov     r10d, [rbx+24h]
		#mov     eax, edx
		#xor     eax, r8d
		#rol     r9d, 7
		#mov     [rsp+68h+var_58], r10d
		#add     r9d, r8d
		#and     eax, r9d
		#xor     eax, edx
		#add     eax, r10d
		#lea     r10d, [rax+rcx-74BB0851h]
		#mov     eax, r8d
		#xor     eax, r9d
		#rol     r10d, 0Ch
		#add     r10d, r9d
		#and     eax, r10d
		#xor     eax, r8d
		#add     eax, r12d
		#lea     ecx, [rax+rdx-0A44Fh]
		#mov     edx, [rbx+2Ch]
		#mov     ebx, [rbx+3Ch]
		#rol     ecx, 11h
		#mov     [rsp+68h+var_60], edx
		#mov     eax, r10d
		#xor     eax, r9d
		#add     ecx, r10d
		#and     eax, ecx
		#xor     eax, r9d
		#add     eax, edx
		#lea     r11d, [rax+r8-76A32842h]
		#mov     eax, r10d
		#xor     eax, ecx
		#rol     r11d, 16h
		#add     r11d, ecx
		#and     eax, r11d
		#xor     eax, r10d
		#add     eax, esi
		#lea     edx, [rax+r9+6B901122h]
		#mov     eax, ecx
		#xor     eax, r11d
		#rol     edx, 7
		#add     edx, r11d
		#and     eax, edx
		#xor     eax, ecx
		#add     eax, r13d
		#lea     r8d, [rax+r10-2678E6Dh]
		#mov     eax, r11d
		#xor     eax, edx
		#rol     r8d, 0Ch
		#add     r8d, edx
		#and     eax, r8d
		#xor     eax, r11d
		#add     eax, edi
		#lea     r9d, [rax+rcx-5986BC72h]
		#mov     eax, r8d
		#xor     eax, edx
		#rol     r9d, 11h
		#add     r9d, r8d
		#and     eax, r9d
		#xor     eax, edx
		#add     eax, ebx
		#lea     ecx, [rax+r11+49B40821h]
		#mov     eax, r9d
		#rol     ecx, 16h
		#add     ecx, r9d
		#xor     eax, ecx
		#and     eax, r8d
		#xor     eax, r9d
		#add     eax, [rsp+68h+arg_18]
		#lea     edx, [rax+rdx-9E1DA9Eh]
		#mov     eax, ecx
		#rol     edx, 5
		#add     edx, ecx
		#xor     eax, edx
		#and     eax, r9d
		#xor     eax, ecx
		#add     eax, [rsp+68h+var_68]
		#lea     r8d, [rax+r8-3FBF4CC0h]
		#rol     r8d, 9
		#add     r8d, edx
		#mov     eax, r8d
		#xor     eax, edx
		#and     eax, ecx
		#xor     eax, edx
		#add     eax, [rsp+68h+var_60]
		#lea     r9d, [rax+r9+265E5A51h]
		#mov     eax, r8d
		#rol     r9d, 0Eh
		#add     r9d, r8d
		#xor     eax, r9d
		#and     eax, edx
		#xor     eax, r8d
		#add     eax, [rsp+68h+arg_8]
		#lea     r10d, [rax+rcx-16493856h]
		#mov     eax, r9d
		#rol     r10d, 14h
		#add     r10d, r9d
		#xor     eax, r10d
		#and     eax, r8d
		#xor     eax, r9d
		#add     eax, r14d
		#lea     ecx, [rax+rdx-29D0EFA3h]
		#mov     eax, r10d
		#rol     ecx, 5
		#add     ecx, r10d
		#xor     eax, ecx
		#and     eax, r9d
		#xor     eax, r10d
		#add     eax, r12d
		#lea     edx, [rax+r8+2441453h]
		#rol     edx, 9
		#add     edx, ecx
		#mov     eax, edx
		#xor     eax, ecx
		#and     eax, r10d
		#xor     eax, ecx
		#add     eax, ebx
		#lea     r8d, [rax+r9-275E197Fh]
		#mov     eax, edx
		#rol     r8d, 0Eh
		#add     r8d, edx
		#xor     eax, r8d
		#and     eax, ecx
		#xor     eax, edx
		#add     eax, [rsp+68h+var_64]
		#lea     r9d, [rax+r10-182C0438h]
		#mov     eax, r8d
		#rol     r9d, 14h
		#add     r9d, r8d
		#xor     eax, r9d
		#and     eax, edx
		#xor     eax, r8d
		#add     eax, [rsp+68h+var_58]
		#lea     r10d, [rax+rcx+21E1CDE6h]
		#mov     eax, r9d
		#rol     r10d, 5
		#add     r10d, r9d
		#xor     eax, r10d
		#and     eax, r8d
		#xor     eax, r9d
		#add     eax, edi
		#lea     ecx, [rax+rdx-3CC8F82Ah]
		#rol     ecx, 9
		#add     ecx, r10d
		#mov     eax, ecx
		#xor     eax, r10d
		#and     eax, r9d
		#xor     eax, r10d
		#add     eax, [rsp+68h+arg_10]
		#lea     edx, [rax+r8-0B2AF279h]
		#rol     edx, 0Eh
		#mov     eax, ecx
		#add     edx, ecx
		#xor     eax, edx
		#and     eax, r10d
		#xor     eax, ecx
		#add     eax, r15d
		#lea     r11d, [rax+r9+455A14EDh]
		#mov     eax, edx
		#rol     r11d, 14h
		#add     r11d, edx
		#xor     eax, r11d
		#and     eax, ecx
		#xor     eax, edx
		#add     eax, r13d
		#lea     r8d, [rax+r10-561C16FBh]
		#mov     eax, r11d
		#rol     r8d, 5
		#add     r8d, r11d
		#xor     eax, r8d
		#and     eax, edx
		#xor     eax, r11d
		#add     eax, [rsp+68h+var_5C]
		#lea     r9d, [rax+rcx-3105C08h]
		#rol     r9d, 9
		#add     r9d, r8d
		#mov     eax, r9d
		#mov     ecx, r9d
		#xor     eax, r8d
		#and     eax, r11d
		#xor     eax, r8d
		#add     eax, ebp
		#lea     r10d, [rax+rdx+676F02D9h]
		#rol     r10d, 0Eh
		#add     r10d, r9d
		#xor     ecx, r10d
		#mov     eax, ecx
		#and     eax, r8d
		#xor     eax, r9d
		#add     eax, esi
		#lea     edx, [rax+r11-72D5B376h]
		#mov     eax, r10d
		#rol     edx, 14h
		#add     edx, r10d
		#xor     eax, edx
		#xor     ecx, edx
		#add     ecx, r14d
		#lea     r8d, [rcx+r8-5C6BEh]
		#rol     r8d, 4
		#add     r8d, edx
		#xor     eax, r8d
		#add     eax, r15d
		#lea     r9d, [rax+r9-788E097Fh]
		#rol     r9d, 0Bh
		#add     r9d, r8d
		#mov     eax, r9d
		#mov     ecx, r9d
		#xor     eax, edx
		#xor     eax, r8d
		#add     eax, [rsp+68h+var_60]
		#lea     r10d, [rax+r10+6D9D6122h]
		#rol     r10d, 10h
		#add     r10d, r9d
		#xor     ecx, r10d
		#mov     eax, ecx
		#xor     eax, r8d
		#add     eax, edi
		#lea     r11d, [rax+rdx-21AC7F4h]
		#mov     eax, r10d
		#rol     r11d, 17h
		#add     r11d, r10d
		#xor     ecx, r11d
		#xor     eax, r11d
		#add     ecx, [rsp+68h+arg_18]
		#lea     edx, [rcx+r8-5B4115BCh]
		#rol     edx, 4
		#add     edx, r11d
		#xor     eax, edx
		#add     eax, [rsp+68h+var_64]
		#lea     r8d, [rax+r9+4BDECFA9h]
		#rol     r8d, 0Bh
		#add     r8d, edx
		#mov     eax, r8d
		#mov     ecx, r8d
		#xor     eax, r11d
		#xor     eax, edx
		#add     eax, ebp
		#lea     r9d, [rax+r10-944B4A0h]
		#rol     r9d, 10h
		#add     r9d, r8d
		#xor     ecx, r9d
		#mov     eax, ecx
		#xor     eax, edx
		#add     eax, r12d
		#lea     r10d, [rax+r11-41404390h]
		#mov     eax, r9d
		#rol     r10d, 17h
		#add     r10d, r9d
		#xor     eax, r10d
		#xor     ecx, r10d
		#add     ecx, r13d
		#lea     r11d, [rcx+rdx+289B7EC6h]
		#rol     r11d, 4
		#add     r11d, r10d
		#xor     eax, r11d
		#add     eax, [rsp+68h+arg_8]
		#lea     r8d, [rax+r8-155ED806h]
		#rol     r8d, 0Bh
		#add     r8d, r11d
		#mov     eax, r8d
		#mov     ecx, r8d
		#xor     eax, r10d
		#xor     eax, r11d
		#add     eax, [rsp+68h+arg_10]
		#lea     r9d, [rax+r9-2B10CF7Bh]
		#rol     r9d, 10h
		#add     r9d, r8d
		#xor     ecx, r9d
		#mov     eax, ecx
		#xor     eax, r11d
		#add     eax, [rsp+68h+var_68]
		#lea     edx, [rax+r10+4881D05h]
		#mov     eax, r9d
		#rol     edx, 17h
		#add     edx, r9d
		#xor     eax, edx
		#xor     ecx, edx
		#add     ecx, [rsp+68h+var_58]
		#lea     r10d, [rcx+r11-262B2FC7h]
		#rol     r10d, 4
		#add     r10d, edx
		#xor     eax, r10d
		#add     eax, esi
		#lea     ecx, [rax+r8-1924661Bh]
		#rol     ecx, 0Bh
		#add     ecx, r10d
		#mov     eax, ecx
		#xor     eax, edx
		#xor     eax, r10d
		#add     eax, ebx
		#lea     r8d, [rax+r9+1FA27CF8h]
		#mov     eax, ecx
		#rol     r8d, 10h
		#add     r8d, ecx
		#xor     eax, r8d
		#xor     eax, r10d
		#add     eax, [rsp+68h+var_5C]
		#lea     r9d, [rax+rdx-3B53A99Bh]
		#mov     eax, ecx
		#not     eax
		#rol     r9d, 17h
		#add     r9d, r8d
		#or      eax, r9d
		#xor     eax, r8d
		#add     eax, [rsp+68h+arg_8]
		#lea     edx, [rax+r10-0BD6DDBCh]
		#mov     eax, r8d
		#rol     edx, 6
		#not     eax
		#add     edx, r9d
		#or      eax, edx
		#xor     eax, r9d
		#add     eax, ebp
		#lea     r10d, [rax+rcx+432AFF97h]
		#mov     eax, r9d
		#not     eax
		#rol     r10d, 0Ah
		#add     r10d, edx
		#or      eax, r10d
		#xor     eax, edx
		#add     eax, edi
		#lea     ecx, [rax+r8-546BDC59h]
		#mov     eax, edx
		#not     eax
		#rol     ecx, 0Fh
		#add     ecx, r10d
		#or      eax, ecx
		#xor     eax, r10d
		#add     eax, r14d
		#lea     r8d, [rax+r9-36C5FC7h]
		#mov     eax, r10d
		#not     eax
		#rol     r8d, 15h
		#add     r8d, ecx
		#or      eax, r8d
		#xor     eax, ecx
		#add     eax, esi
		#lea     r9d, [rax+rdx+655B59C3h]
		#mov     eax, ecx
		#not     eax
		#rol     r9d, 6
		#add     r9d, r8d
		#or      eax, r9d
		#xor     eax, r8d
		#add     eax, [rsp+68h+arg_10]
		#lea     edx, [rax+r10-70F3336Eh]
		#mov     eax, r8d
		#not     eax
		#rol     edx, 0Ah
		#add     edx, r9d
		#or      eax, edx
		#xor     eax, r9d
		#add     eax, r12d
		#lea     r10d, [rax+rcx-100B83h]
		#mov     eax, r9d
		#not     eax
		#rol     r10d, 0Fh
		#add     r10d, edx
		#or      eax, r10d
		#xor     eax, edx
		#add     eax, [rsp+68h+arg_18]
		#lea     ecx, [rax+r8-7A7BA22Fh]
		#mov     eax, edx
		#not     eax
		#rol     ecx, 15h
		#add     ecx, r10d
		#or      eax, ecx
		#xor     eax, r10d
		#add     eax, r15d
		#lea     r8d, [rax+r9+6FA87E4Fh]
		#mov     eax, r10d
		#not     eax
		#rol     r8d, 6
		#add     r8d, ecx
		#or      eax, r8d
		#xor     eax, ecx
		#add     eax, ebx
		#lea     r11d, [rax+rdx-1D31920h]
		#mov     eax, ecx
		#not     eax
		#rol     r11d, 0Ah
		#add     r11d, r8d
		#or      eax, r11d
		#xor     eax, r8d
		#add     eax, [rsp+68h+var_68]
		#lea     edx, [rax+r10-5CFEBCECh]
		#mov     eax, r8d
		#not     eax
		#rol     edx, 0Fh
		#add     edx, r11d
		#or      eax, edx
		#xor     eax, r11d
		#add     eax, r13d
		#lea     r10d, [rax+rcx+4E0811A1h]
		#mov     eax, r11d
		#not     eax
		#rol     r10d, 15h
		#add     r10d, edx
		#or      eax, r10d
		#xor     eax, edx
		#add     eax, [rsp+68h+var_64]
		#lea     r9d, [rax+r8-8AC817Eh]
		#mov     eax, edx
		#not     eax
		#rol     r9d, 6
		#add     r9d, r10d
		#or      eax, r9d
		#xor     eax, r10d
		#add     eax, [rsp+68h+var_60]
		#lea     r8d, [rax+r11-42C50DCBh]
		#mov     eax, r10d
		#not     eax
		#rol     r8d, 0Ah
		#add     r8d, r9d
		#or      eax, r8d
		#xor     eax, r9d
		#add     eax, [rsp+68h+var_5C]
		#lea     edx, [rax+rdx+2AD7D2BBh]
		#mov     eax, r9d
		#not     eax
		#rol     edx, 0Fh
		#add     edx, r8d
		#or      eax, edx
		#xor     eax, r8d
		#add     eax, [rsp+68h+var_58]
		#lea     ecx, [rax+r10-14792C6Fh]
		#mov     r10, [rsp+68h+arg_0]
		#mov     eax, [r10]
		#rol     ecx, 15h
		#add     eax, r9d
		#add     ecx, edx
		#mov     [r10], eax
		#mov     eax, [r10+4]
		#add     eax, ecx
		#mov     [r10+4], eax
		#mov     eax, [r10+8]
		#add     eax, edx
		#mov     [r10+8], eax
		#mov     eax, [r10+0Ch]
		#add     eax, r8d
		#mov     [r10+0Ch], eax
		#add     rsp, 28h
		#pop     r15
		#pop     r14
		#pop     r13
		#pop     r12
		#pop     rdi
		#pop     rsi
		#pop     rbp
		#pop     rbx
		#retn


  def test_gadget_sub_78EEF1D0(self):
		#sub_78EEF1D0
		gadget = "48C701800F05FD488BC1C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0FFFFFFFFFD050F80h
		#mov     rax, rcx
		#retn


  def test_gadget_sub_78EEF250(self):
		#sub_78EEF250
		gadget = "488B1133C0813A060000C00F94C0C3"
		self.do(gadget)

		#mov     rdx, [rcx]
		#xor     eax, eax
		#cmp     dword ptr [rdx], 0C0000006h
		#setz    al
		#retn


  def test_gadget_sub_78EEF6F0(self):
		#sub_78EEF6F0
		gadget = "FFC23B15F07709001BC023C2C3"
		self.do(gadget)

		#inc     edx
		#cmp     edx, cs:dword_78F86EE8
		#sbb     eax, eax
		#and     eax, edx
		#retn


  def test_gadget_TpDbgSetLogRoutine(self):
		#TpDbgSetLogRoutine
		gadget = "48890DC1FC0800C3"
		self.do(gadget)

		#mov     cs:qword_78F7F3D8, rcx
		#retn


  def test_gadget_sub_78EEF960(self):
		#sub_78EEF960
		gadget = "F30F6F422C4C8BC2F30F7F41188B823C0100008941408B823801000089413C488B8250010000489948F73D59580700894144418B80C0000000C1E80A894130418B80D4000000894160418B80D0000000894134418B80CC000000894138418B8068010000894168418B80D8000000894164418B807001000089416C418B806C0100008361740083614C00894170498B401848894178418B4010894128410FB74014C6410B0166894108C3"
		self.do(gadget)

		#movdqu  xmm0, xmmword ptr [rdx+2Ch]
		#mov     r8, rdx
		#movdqu  xmmword ptr [rcx+18h], xmm0
		#mov     eax, [rdx+13Ch]
		#mov     [rcx+40h], eax
		#mov     eax, [rdx+138h]
		#mov     [rcx+3Ch], eax
		#mov     rax, [rdx+150h]
		#cqo
		#idiv    cs:qword_78F651E8
		#mov     [rcx+44h], eax
		#mov     eax, [r8+0C0h]
		#shr     eax, 0Ah
		#mov     [rcx+30h], eax
		#mov     eax, [r8+0D4h]
		#mov     [rcx+60h], eax
		#mov     eax, [r8+0D0h]
		#mov     [rcx+34h], eax
		#mov     eax, [r8+0CCh]
		#mov     [rcx+38h], eax
		#mov     eax, [r8+168h]
		#mov     [rcx+68h], eax
		#mov     eax, [r8+0D8h]
		#mov     [rcx+64h], eax
		#mov     eax, [r8+170h]
		#mov     [rcx+6Ch], eax
		#mov     eax, [r8+16Ch]
		#and     dword ptr [rcx+74h], 0
		#and     dword ptr [rcx+4Ch], 0
		#mov     [rcx+70h], eax
		#mov     rax, [r8+18h]
		#mov     [rcx+78h], rax
		#mov     eax, [r8+10h]
		#mov     [rcx+28h], eax
		#movzx   eax, word ptr [r8+14h]
		#mov     byte ptr [rcx+0Bh], 1
		#mov     [rcx+8], ax
		#retn


  def test_gadget_sub_78EEFA90(self):
		#sub_78EEFA90
		gadget = "8B0D7AF5080033C0F00FB10D70F508000F95C0C3"
		self.do(gadget)

		#mov     ecx, cs:dword_78F7F010
		#xor     eax, eax
		#lock cmpxchg cs:dword_78F7F010, ecx
		#setnz   al
		#retn


  def test_gadget_sub_78EF13E0(self):
		#sub_78EF13E0
		gadget = "2BCA442BC2413BC80F96C0C3"
		self.do(gadget)

		#sub     ecx, edx
		#sub     r8d, edx
		#cmp     ecx, r8d
		#setbe   al
		#retn


  def test_gadget_RtlRandom(self):
		#RtlRandom
		gadget = "448B114C8BC948B90500000002000000488BC141BBC3FFFF7F4D69D2EDFFFF7F4D03D34D8BC249F7E2488BC14C2BC249D1E84C03C249C1E81E4D69C0FFFFFF7F4D2BD0458BC24D69C0EDFFFF7F4D03C3498BC849F7E0488D05336C0900482BCA48D1E94803CA48C1E91E4869C9FFFFFF7F4C2BC14589014183E07F46871480418BC2C3"
		self.do(gadget)

		#mov     r10d, [rcx]
		#mov     r9, rcx
		#mov     rcx, 200000005h
		#mov     rax, rcx
		#mov     r11d, 7FFFFFC3h
		#imul    r10, 7FFFFFEDh
		#add     r10, r11
		#mov     r8, r10
		#mul     r10
		#mov     rax, rcx
		#sub     r8, rdx
		#shr     r8, 1
		#add     r8, rdx
		#shr     r8, 1Eh
		#imul    r8, 7FFFFFFFh
		#sub     r10, r8
		#mov     r8d, r10d
		#imul    r8, 7FFFFFEDh
		#add     r8, r11
		#mov     rcx, r8
		#mul     r8
		#lea     rax, unk_78F88240
		#sub     rcx, rdx
		#shr     rcx, 1
		#add     rcx, rdx
		#shr     rcx, 1Eh
		#imul    rcx, 7FFFFFFFh
		#sub     r8, rcx
		#mov     [r9], r8d
		#and     r8d, 7Fh
		#xchg    r10d, [rax+r8*4]
		#mov     eax, r10d
		#retn


  def test_gadget_sub_78EF1730(self):
		#sub_78EF1730
		gadget = "4881F9000000011BC02572F0FFFF054F250000C3"
		self.do(gadget)

		#cmp     rcx, 1000000h
		#sbb     eax, eax
		#and     eax, 0FFFFF072h
		#add     eax, 254Fh
		#retn


  def test_gadget_RtlKnownExceptionFilter(self):
		#RtlKnownExceptionFilter
		gadget = "488B1133C0813A940100C00F95C0FFC8C3"
		self.do(gadget)

		#mov     rdx, [rcx]
		#xor     eax, eax
		#cmp     dword ptr [rdx], 0C0000194h
		#setnz   al
		#dec     eax
		#retn


  def test_gadget_sub_78EF1FB0(self):
		#sub_78EF1FB0
		gadget = "488B5120483951280F92C0C3"
		self.do(gadget)

		#mov     rdx, [rcx+20h]
		#cmp     [rcx+28h], rdx
		#setb    al
		#retn


  def test_gadget_sub_78EF1FD0(self):
		#sub_78EF1FD0
		gadget = "488B5108483951100F94C0C3"
		self.do(gadget)

		#mov     rdx, [rcx+8]
		#cmp     [rcx+10h], rdx
		#setz    al
		#retn


  def test_gadget_sub_78EF20B0(self):
		#sub_78EF20B0
		gadget = "81C10054FFFFB827AE746FF7E9C1FA088BC2C1E81F03D0B89324499269D24C0200002BCAF7E903D1C1FA048BC2C1E81F8D840261110000C3"
		self.do(gadget)

		#add     ecx, 0FFFF5400h
		#mov     eax, 6F74AE27h
		#imul    ecx
		#sar     edx, 8
		#mov     eax, edx
		#shr     eax, 1Fh
		#add     edx, eax
		#mov     eax, 92492493h
		#imul    edx, 24Ch
		#sub     ecx, edx
		#imul    ecx
		#add     edx, ecx
		#sar     edx, 4
		#mov     eax, edx
		#shr     eax, 1Fh
		#lea     eax, [rdx+rax+1161h]
		#retn


  def test_gadget_sub_78EF20F0(self):
		#sub_78EF20F0
		gadget = "81C10054FFFFB827AE746FF7E9C1FA088BC2C1E81F8D840200110000C3"
		self.do(gadget)

		#add     ecx, 0FFFF5400h
		#mov     eax, 6F74AE27h
		#imul    ecx
		#sar     edx, 8
		#mov     eax, edx
		#shr     eax, 1Fh
		#lea     eax, [rdx+rax+1100h]
		#retn


  def test_gadget_sub_78EF2120(self):
		#sub_78EF2120
		gadget = "81C158EEFFFF83F91A0F96C0C3"
		self.do(gadget)

		#add     ecx, 0FFFFEE58h
		#cmp     ecx, 1Ah
		#setbe   al
		#retn


  def test_gadget_sub_78EF2140(self):
		#sub_78EF2140
		gadget = "81C19FEEFFFF83F9140F96C0C3"
		self.do(gadget)

		#add     ecx, 0FFFFEE9Fh
		#cmp     ecx, 14h
		#setbe   al
		#retn


  def test_gadget_sub_78EF2160(self):
		#sub_78EF2160
		gadget = "81C100EFFFFF83F9120F96C0C3"
		self.do(gadget)

		#add     ecx, 0FFFFEF00h
		#cmp     ecx, 12h
		#setbe   al
		#retn


  def test_gadget_sub_78EF2180(self):
		#sub_78EF2180
		gadget = "81C10054FFFF81F9A32B00000F96C0C3"
		self.do(gadget)

		#add     ecx, 0FFFF5400h
		#cmp     ecx, 2BA3h
		#setbe   al
		#retn


  def test_gadget_sub_78EF2370(self):
		#sub_78EF2370
		gadget = "F6D10FB6C1D1E883E001C3"
		self.do(gadget)

		#not     cl
		#movzx   eax, cl
		#shr     eax, 1
		#and     eax, 1
		#retn


  def test_gadget_sub_78EF2480(self):
		#sub_78EF2480
		gadget = "81F9800000000F92C0C3"
		self.do(gadget)

		#cmp     ecx, 80h
		#setb    al
		#retn


  def test_gadget_sub_78EF2490(self):
		#sub_78EF2490
		gadget = "6683E9416683F9190F96C0C3"
		self.do(gadget)

		#sub     cx, 41h
		#cmp     cx, 19h
		#setbe   al
		#retn


  def test_gadget_sub_78EF25E0(self):
		#sub_78EF25E0
		gadget = "8D810000FFFFB90004000099F7F98D8200DC0000C3"
		self.do(gadget)

		#lea     eax, [rcx-10000h]
		#mov     ecx, 400h
		#cdq
		#idiv    ecx
		#lea     eax, [rdx+0DC00h]
		#retn


  def test_gadget_sub_78EF2600(self):
		#sub_78EF2600
		gadget = "8D810000FFFFB90004000099F7F90500D80000C3"
		self.do(gadget)

		#lea     eax, [rcx-10000h]
		#mov     ecx, 400h
		#cdq
		#idiv    ecx
		#add     eax, 0D800h
		#retn


  def test_gadget_sub_78EF2620(self):
		#sub_78EF2620
		gadget = "B800280000BAFF0700006603C8663BCA0F96C0C3"
		self.do(gadget)

		#mov     eax, 2800h
		#mov     edx, 7FFh
		#add     cx, ax
		#cmp     cx, dx
		#setbe   al
		#retn


  def test_gadget_sub_78EF2640(self):
		#sub_78EF2640
		gadget = "81F9000001000F9DC0C3"
		self.do(gadget)

		#cmp     ecx, 10000h
		#setnl   al
		#retn


  def test_gadget_RtlGetEnabledExtendedFeatures(self):
		#RtlGetEnabledExtendedFeatures
		gadget = "488B0425E003FE7F4823C1C3"
		self.do(gadget)

		#mov     rax, ds:7FFE03E0h
		#and     rax, rcx
		#retn


  def test_gadget_RtlInitializeGenericTableAvl(self):
		#RtlInitializeGenericTableAvl
		gadget = "48895C240848896C24104889742418574883EC20488BDA33D2498BF8448D4268498BE9488BF1E855BCFAFF488B44245048895E48488B5C243048896E58488B6C24384889466048893648897E50488B7424404883C4205FC3"
		self.do(gadget)

		#mov     [rsp+arg_0], rbx
		#mov     [rsp+arg_8], rbp
		#mov     [rsp+arg_10], rsi
		#push    rdi
		#sub     rsp, 20h
		#mov     rbx, rdx
		#xor     edx, edx        ; Val
		#mov     rdi, r8
		#lea     r8d, [rdx+68h]  ; Size
		#mov     rbp, r9
		#mov     rsi, rcx
		#call    memset
		#mov     rax, [rsp+28h+arg_20]
		#mov     [rsi+48h], rbx
		#mov     rbx, [rsp+28h+arg_0]
		#mov     [rsi+58h], rbp
		#mov     rbp, [rsp+28h+arg_8]
		#mov     [rsi+60h], rax
		#mov     [rsi], rsi
		#mov     [rsi+50h], rdi
		#mov     rsi, [rsp+28h+arg_10]
		#add     rsp, 20h
		#pop     rdi
		#retn


  def test_gadget_sub_78EF41A0(self):
		#sub_78EF41A0
		gadget = "B85F0200C0C3"
		self.do(gadget)

		#mov     eax, 0C000025Fh
		#retn


  def test_gadget_RtlTestBit(self):
		#RtlTestBit
		gadget = "488B41080FA3100F92C0C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#bt      [rax], edx
		#setb    al
		#retn


  def test_gadget_RtlGetFunctionTableListHead(self):
		#RtlGetFunctionTableListHead
		gadget = "488D0539950800C3"
		self.do(gadget)

		#lea     rax, qword_78F7F510
		#retn


  def test_gadget_RtlAreAnyAccessesGranted(self):
		#RtlAreAnyAccessesGranted
		gadget = "85CA0F95C0C3"
		self.do(gadget)

		#test    edx, ecx
		#setnz   al
		#retn


  def test_gadget_RtlCopyLuidAndAttributesArray(self):
		#RtlCopyLuidAndAttributesArray
		gadget = "85C97429492BD0448BC9428B0402418900428B4402044983C00C4983E901418940F8428B4402FC418940FC75DDF3C3"
		self.do(gadget)

		#test    ecx, ecx
		#jz      short locret_78EF64BD
		#sub     rdx, r8
		#mov     r9d, ecx
		#mov     eax, [rdx+r8]
		#mov     [r8], eax
		#mov     eax, [rdx+r8+4]
		#add     r8, 0Ch
		#sub     r9, 1
		#mov     [r8-8], eax
		#mov     eax, [rdx+r8-4]
		#mov     [r8-4], eax
		#jnz     short loc_78EF649A
		#rep retn


  def test_gadget_PfxInitialize(self):
		#PfxInitialize
		gadget = "B8000200004889490866890133C066894102C3"
		self.do(gadget)

		#mov     eax, 200h
		#mov     [rcx+8], rcx
		#mov     [rcx], ax
		#xor     eax, eax
		#mov     [rcx+2], ax
		#retn


  def test_gadget_AlpcGetOutstandingCompletionListMessageCount(self):
		#AlpcGetOutstandingCompletionListMessageCount
		gadget = "8B81000100008B89800100002BC1C3"
		self.do(gadget)

		#mov     eax, [rcx+100h]
		#mov     ecx, [rcx+180h]
		#sub     eax, ecx
		#retn


  def test_gadget_AlpcGetCompletionListLastMessageInformation(self):
		#AlpcGetCompletionListLastMessageInformation
		gadget = "8B818800000089028B818C000000418900C3"
		self.do(gadget)

		#mov     eax, [rcx+88h]
		#mov     [rdx], eax
		#mov     eax, [rcx+8Ch]
		#mov     [r8], eax
		#retn


  def test_gadget_RtlWow64EnableFsRedirectionEx(self):
		#RtlWow64EnableFsRedirectionEx
		gadget = "B8020000C0C3"
		self.do(gadget)

		#mov     eax, 0C0000002h ; RtlCreateUmsThread
		#retn


  def test_gadget_sub_78EF81AC(self):
		#sub_78EF81AC
		gadget = "55488BEA5DC3"
		self.do(gadget)

		#push    rbp
		#mov     rbp, rdx
		#pop     rbp
		#retn


  def test_gadget_RtlUpdateClonedSRWLock(self):
		#RtlUpdateClonedSRWLock
		gadget = "F7DA481BC083E0104883C801488901C3"
		self.do(gadget)

		#neg     edx
		#sbb     rax, rax
		#and     eax, 10h
		#or      rax, 1
		#mov     [rcx], rax
		#retn


  def test_gadget_RtlTryAcquireSRWLockExclusive(self):
		#RtlTryAcquireSRWLockExclusive
		gadget = "F0480FBA29000F93C0C3"
		self.do(gadget)

		#lock bts qword ptr [rcx], 0
		#setnb   al
		#retn


  def test_gadget_RtlIsCriticalSectionLocked(self):
		#RtlIsCriticalSectionLocked
		gadget = "8A4108F6D00FBEC083E001C3"
		self.do(gadget)

		#mov     al, [rcx+8]
		#not     al
		#movsx   eax, al
		#and     eax, 1
		#retn


  def test_gadget_RtlWriteMemoryStream(self):
		#RtlWriteMemoryStream
		gadget = "B801400080C3"
		self.do(gadget)

		#mov     eax, 80004001h  ; RtlCloneMemoryStream
		#retn


  def test_gadget___misaligned_access(self):
		#__misaligned_access
		gadget = "C20000"
		self.do(gadget)

		#retn    0               ; RtlDebugPrintTimes


  def test_gadget_CsrSetPriorityClass(self):
		#CsrSetPriorityClass
		gadget = "B80D0000C0C3"
		self.do(gadget)

		#mov     eax, 0C000000Dh
		#retn


  def test_gadget_LdrGetFailureData(self):
		#LdrGetFailureData
		gadget = "488D05E9600800C3"
		self.do(gadget)

		#lea     rax, dword_78F7F6A0
		#retn


  def test_gadget_RtlGetUnloadEventTraceEx(self):
		#RtlGetUnloadEventTraceEx
		gadget = "488D0549ED0800488901488D05235A0800488902488D05B55A0800498900C3"
		self.do(gadget)

		#lea     rax, unk_78F885D0
		#mov     [rcx], rax
		#lea     rax, dword_78F7F2B4
		#mov     [rdx], rax
		#lea     rax, qword_78F7F350
		#mov     [r8], rax
		#retn


  def test_gadget_RtlGetUnloadEventTrace(self):
		#RtlGetUnloadEventTrace
		gadget = "488D0589AC0800C3"
		self.do(gadget)

		#lea     rax, unk_78F84540
		#retn


  def test_gadget_CsrGetProcessId(self):
		#CsrGetProcessId
		gadget = "488B0521590800C3"
		self.do(gadget)

		#mov     rax, cs:qword_78F7F478
		#retn


  def test_gadget_sub_78EFA7A0(self):
		#sub_78EFA7A0
		gadget = "83622C004C8D4220B80100000049832000F0480FC1818801000048FFC048894218488B81F80000004C89004C8981F8000000F08381D800000001C3"
		self.do(gadget)

		#and     dword ptr [rdx+2Ch], 0
		#lea     r8, [rdx+20h]
		#mov     eax, 1
		#and     qword ptr [r8], 0
		#lock xadd [rcx+188h], rax
		#inc     rax
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+0F8h]
		#mov     [rax], r8
		#mov     [rcx+0F8h], r8
		#lock add dword ptr [rcx+0D8h], 1
		#retn


  def test_gadget_sub_78EFA92C(self):
		#sub_78EFA92C
		gadget = "554883EC20488BEA48894D30488B018B08894D2CC74524000000008B45244883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#mov     [rbp+30h], rcx
		#mov     rax, [rcx]
		#mov     ecx, [rax]
		#mov     [rbp+2Ch], ecx
		#mov     dword ptr [rbp+24h], 0
		#mov     eax, [rbp+24h]
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_RtlGetLastWin32Error(self):
		#RtlGetLastWin32Error
		gadget = "65488B0425300000008B4068C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     eax, [rax+68h]
		#retn


  def test_gadget_RtlGetLastNtStatus(self):
		#RtlGetLastNtStatus
		gadget = "65488B0425300000008B8050120000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     eax, [rax+1250h]
		#retn


  def test_gadget_RtlGetCurrentPeb(self):
		#RtlGetCurrentPeb
		gadget = "65488B042530000000488B4060C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rax, [rax+60h]
		#retn


  def test_gadget_sub_78EFDBE0(self):
		#sub_78EFDBE0
		gadget = "5B009090909090909090909090909090252525750090909090909090909090905D3A2575009090909090909090909090"
		self.do(gadget)

		#pop     rbx
		#add     [rax-6F6F6F70h], dl
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#and     eax, 752525h
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#pop     rbp
		#cmp     ah, cs:97FDC7Ch
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop


  def test_gadget_NtGetTickCount(self):
		#NtGetTickCount
		gadget = "8B0C250400FE7F488B04252003FE7F480FAFC148C1E818C3"
		self.do(gadget)

		#mov     ecx, ds:7FFE0004h
		#mov     rax, ds:7FFE0320h
		#imul    rax, rcx
		#shr     rax, 18h
		#retn


  def test_gadget_RtlSecondsSince1970ToTime(self):
		#RtlSecondsSince1970ToTime
		gadget = "83642414004C8B057C020500894C2410488B4C24104C03C14D69C0809698004C8902C3"
		self.do(gadget)

		#and     dword ptr [rsp+arg_8+4], 0
		#mov     r8, cs:qword_78F51428
		#mov     dword ptr [rsp+arg_8], ecx
		#mov     rcx, [rsp+arg_8]
		#add     r8, rcx
		#imul    r8, 989680h
		#mov     [rdx], r8
		#retn


  def test_gadget_RtlSecondsSince1980ToTime(self):
		#RtlSecondsSince1980ToTime
		gadget = "83642414004C8B05AC120500894C2410488B4C24104C03C14D69C0809698004C8902C3"
		self.do(gadget)

		#and     dword ptr [rsp+arg_8+4], 0
		#mov     r8, cs:qword_78F52488
		#mov     dword ptr [rsp+arg_8], ecx
		#mov     rcx, [rsp+arg_8]
		#add     r8, rcx
		#imul    r8, 989680h
		#mov     [rdx], r8
		#retn


  def test_gadget_sub_78F032F4(self):
		#sub_78F032F4
		gadget = "554883EC20488BEA488B4578C68081000000004883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#mov     rax, [rbp+78h]
		#mov     byte ptr [rax+81h], 0
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_RtlEnableEarlyCriticalSectionEventCreation(self):
		#RtlEnableEarlyCriticalSectionEventCreation
		gadget = "65488B042530000000488B48600FBAA9BC0000001CC3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rcx, [rax+60h]
		#bts     dword ptr [rcx+0BCh], 1Ch
		#retn


  def test_gadget_RtlUpdateClonedCriticalSection(self):
		#RtlUpdateClonedCriticalSection
		gadget = "65488B042530000000488B50484883611800C74108FEFFFFFF48895110C7410C01000000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rdx, [rax+48h]
		#and     qword ptr [rcx+18h], 0
		#mov     dword ptr [rcx+8], 0FFFFFFFEh
		#mov     [rcx+10h], rdx
		#mov     dword ptr [rcx+0Ch], 1
		#retn


  def test_gadget_RtlIsCriticalSectionLockedByThread(self):
		#RtlIsCriticalSectionLockedByThread
		gadget = "65488B14253000000033C0488B5248483951100F94C0C3"
		self.do(gadget)

		#mov     rdx, gs:30h
		#xor     eax, eax
		#mov     rdx, [rdx+48h]
		#cmp     [rcx+10h], rdx
		#setz    al
		#retn


  def test_gadget_RtlGetFrame(self):
		#RtlGetFrame
		gadget = "65488B042530000000488B80C0170000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rax, [rax+17C0h]
		#retn


  def test_gadget_RtlGetThreadErrorMode(self):
		#RtlGetThreadErrorMode
		gadget = "65488B0425300000008B80B0160000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     eax, [rax+16B0h]
		#retn


  def test_gadget_DbgUiSetThreadDebugObject(self):
		#DbgUiSetThreadDebugObject
		gadget = "65488B042530000000488988A8160000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     [rax+16A8h], rcx
		#retn


  def test_gadget_DbgUiGetThreadDebugObject(self):
		#DbgUiGetThreadDebugObject
		gadget = "65488B042530000000488B80A8160000C3"
		self.do(gadget)

		#mov     rax, gs:30h
		#mov     rax, [rax+16A8h]
		#retn


  def test_gadget_sub_78F04824(self):
		#sub_78F04824
		gadget = "554883EC20488D6A20488B0133C98138FD0000C00F94C18BC18BC14883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#lea     rbp, [rdx+20h]
		#mov     rax, [rcx]
		#xor     ecx, ecx
		#cmp     dword ptr [rax], 0C00000FDh
		#setz    cl
		#mov     eax, ecx
		#mov     eax, ecx
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_sub_78F090E8(self):
		#sub_78F090E8
		gadget = "554883EC20488BEA48894D28488B018B08894D24C74520000000008B45204883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#mov     [rbp+28h], rcx
		#mov     rax, [rcx]
		#mov     ecx, [rax]
		#mov     [rbp+24h], ecx
		#mov     dword ptr [rbp+20h], 0
		#mov     eax, [rbp+20h]
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_sub_78F17894(self):
		#sub_78F17894
		gadget = "554883EC20488BEA4883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_sub_78F178F0(self):
		#sub_78F178F0
		gadget = "554883EC20488BEA4883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_sub_78F1E9E0(self):
		#sub_78F1E9E0
		gadget = "554883EC30488BEA4883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#mov     rbp, rdx
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F1F588(self):
		#sub_78F1F588
		gadget = "554883EC20488BEA48894D28488B018B08894D24C74520000000008B45204883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#mov     [rbp+28h], rcx
		#mov     rax, [rcx]
		#mov     ecx, [rax]
		#mov     [rbp+24h], ecx
		#mov     dword ptr [rbp+20h], 0
		#mov     eax, [rbp+20h]
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_sub_78F212FC(self):
		#sub_78F212FC
		gadget = "554883EC30488BEA488B4560F083400CFF4883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#mov     rbp, rdx
		#mov     rax, [rbp+60h]
		#lock add dword ptr [rax+0Ch], 0FFFFFFFFh
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F21314(self):
		#sub_78F21314
		gadget = "554883EC30488BEA488B45408B4814488D15F6380600F083048AFF4883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#mov     rbp, rdx
		#mov     rax, [rbp+40h]
		#mov     ecx, [rax+14h]
		#lea     rdx, dword_78F84C20
		#lock add dword ptr [rdx+rcx*4], 0FFFFFFFFh
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F21BA4(self):
		#sub_78F21BA4
		gadget = "554883EC30488D6A3048898D80000000488B018B08894D7033C081F9FD0000C00F94C04883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#lea     rbp, [rdx+30h]
		#mov     [rbp+80h], rcx
		#mov     rax, [rcx]
		#mov     ecx, [rax]
		#mov     [rbp+70h], ecx
		#xor     eax, eax
		#cmp     ecx, 0C00000FDh
		#setz    al
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F21CA4(self):
		#sub_78F21CA4
		gadget = "554883EC30488BEA488B4548F083400CFF4883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#mov     rbp, rdx
		#mov     rax, [rbp+48h]
		#lock add dword ptr [rax+0Ch], 0FFFFFFFFh
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F2267C(self):
		#sub_78F2267C
		gadget = "554883EC30488BEA488B4558F083400CFF4883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#mov     rbp, rdx
		#mov     rax, [rbp+58h]
		#lock add dword ptr [rax+0Ch], 0FFFFFFFFh
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F22694(self):
		#sub_78F22694
		gadget = "554883EC30488BEA488B45388B4814488D0576250600F0830488FF4883C4305DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 30h
		#mov     rbp, rdx
		#mov     rax, [rbp+38h]
		#mov     ecx, [rax+14h]
		#lea     rax, dword_78F84C20
		#lock add dword ptr [rax+rcx*4], 0FFFFFFFFh
		#add     rsp, 30h
		#pop     rbp
		#retn


  def test_gadget_sub_78F22934(self):
		#sub_78F22934
		gadget = "554883EC20488BEA48894D58488B018B08894D40C7452C000000008B452C4883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#mov     [rbp+58h], rcx
		#mov     rax, [rcx]
		#mov     ecx, [rax]
		#mov     [rbp+40h], ecx
		#mov     dword ptr [rbp+2Ch], 0
		#mov     eax, [rbp+2Ch]
		#add     rsp, 20h
		#pop     rbp
		#retn


  def test_gadget_sub_78F30660(self):
		#sub_78F30660
		gadget = "5300520020002D00200000009090909090909090909090909090909090909090"
		self.do(gadget)

		#push    rbx
		#add     [rdx+0], dl
		#and     [rax], al
		#sub     eax, 2000h
		#add     [rax-6F6F6F70h], dl
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop
		#nop


  def test_gadget_sub_78F45BA0(self):
		#sub_78F45BA0
		gadget = "554883EC20488BEA488B0133C98138050000C00F94C18BC14883C4205DC3"
		self.do(gadget)

		#push    rbp
		#sub     rsp, 20h
		#mov     rbp, rdx
		#mov     rax, [rcx]
		#xor     ecx, ecx
		#cmp     dword ptr [rax], 0C0000005h
		#setz    cl
		#mov     eax, ecx
		#add     rsp, 20h
		#pop     rbp
		#retn

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()
    