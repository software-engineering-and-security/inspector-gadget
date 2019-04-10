import unittest
import logging
from inspectorgadget import InspectorGadget


class TestGadgetX64(unittest.TestCase):

  def do(self, gadget):
      InspectorGadget.doAnalysis(gadget, "x64")



  def test_gadget_sub_6FC483F0(self):
		#sub_6FC483F0
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget_sub_6FC48400(self):
		#sub_6FC48400
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget_sub_6FC48410(self):
		#sub_6FC48410
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget_sub_6FC49750(self):
		#sub_6FC49750
		gadget = "DBE3C3"
		self.do(gadget)

		#fninit
		#retn


  def test_gadget_sub_6FC499B0(self):
		#sub_6FC499B0
		gadget = "B8FFFFFFFF31D2F00FB111F7D0C1E81FC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#xor     edx, edx
		#lock cmpxchg [rcx], edx
		#not     eax
		#shr     eax, 1Fh
		#retn


  def test_gadget_sub_6FC49BF0(self):
		#sub_6FC49BF0
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget_sub_6FC49C00(self):
		#sub_6FC49C00
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget_sub_6FC4B6B0(self):
		#sub_6FC4B6B0
		gadget = "488B0559420C008B00C3"
		self.do(gadget)

		#mov     rax, cs:qword_6FD0F910
		#mov     eax, [rax]
		#retn


  def test_gadget_sub_6FC54BD0(self):
		#sub_6FC54BD0
		gadget = "488D0559CB0900488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF1730
		#mov     [rcx], rax
		#retn


  def test_gadget_sub_6FC54CF0(self):
		#sub_6FC54CF0
		gadget = "488D05B9CB0900488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF18B0
		#mov     [rcx], rax
		#retn


  def test_gadget_sub_6FC54FD0(self):
		#sub_6FC54FD0
		gadget = "48C70100000000C741080000000048C741100000000048C7411800000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     dword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#retn


  def test_gadget_sub_6FC56220(self):
		#sub_6FC56220
		gadget = "488D05A9CB0900488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF2DD0
		#mov     [rcx], rax
		#retn


  def test_gadget_sub_6FC56240(self):
		#sub_6FC56240
		gadget = "488D0589CB0900488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF2DD0
		#mov     [rcx], rax
		#retn


  def test_gadget_nullsub_2(self):
		#nullsub_2
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_3(self):
		#nullsub_3
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_4(self):
		#nullsub_4
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_5(self):
		#nullsub_5
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_6(self):
		#nullsub_6
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_7(self):
		#nullsub_7
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_8(self):
		#nullsub_8
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_9(self):
		#nullsub_9
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_10(self):
		#nullsub_10
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_11(self):
		#nullsub_11
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_12(self):
		#nullsub_12
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_13(self):
		#nullsub_13
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZN9__gnu_cxx12__atomic_addEPVii(self):
		#_ZN9__gnu_cxx12__atomic_addEPVii
		gadget = "F00111C3"
		self.do(gadget)

		#lock add [rcx], edx
		#retn


  def test_gadget_nullsub_14(self):
		#nullsub_14
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_15(self):
		#nullsub_15
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_16(self):
		#nullsub_16
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_17(self):
		#nullsub_17
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_18(self):
		#nullsub_18
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_19(self):
		#nullsub_19
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_20(self):
		#nullsub_20
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_21(self):
		#nullsub_21
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_22(self):
		#nullsub_22
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_23(self):
		#nullsub_23
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_24(self):
		#nullsub_24
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_25(self):
		#nullsub_25
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_26(self):
		#nullsub_26
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_27(self):
		#nullsub_27
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_28(self):
		#nullsub_28
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_29(self):
		#nullsub_29
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_30(self):
		#nullsub_30
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_31(self):
		#nullsub_31
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_32(self):
		#nullsub_32
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_33(self):
		#nullsub_33
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_34(self):
		#nullsub_34
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_35(self):
		#nullsub_35
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_36(self):
		#nullsub_36
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_37(self):
		#nullsub_37
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_38(self):
		#nullsub_38
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_39(self):
		#nullsub_39
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_40(self):
		#nullsub_40
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_41(self):
		#nullsub_41
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZN9__gnu_cxx17__pool_alloc_base16_M_get_free_listEy(self):
		#_ZN9__gnu_cxx17__pool_alloc_base16_M_get_free_listEy
		gadget = "488D05592209004883C20748C1EA03488D44D0F8C3"
		self.do(gadget)

		#lea     rax, unk_6FCEDD60
		#add     rdx, 7
		#shr     rdx, 3
		#lea     rax, [rax+rdx*8-8]
		#retn


  def test_gadget__ZN9__gnu_cxx18__exchange_and_addEPVii(self):
		#_ZN9__gnu_cxx18__exchange_and_addEPVii
		gadget = "89D0F00FC101C3"
		self.do(gadget)

		#mov     eax, edx
		#lock xadd [rcx], eax
		#retn


  def test_gadget__ZN9__gnu_cxx18stdio_sync_filebufIcSt11char_traitsIcEE4fileEv(self):
		#_ZN9__gnu_cxx18stdio_sync_filebufIcSt11char_traitsIcEE4fileEv
		gadget = "488B4140C3"
		self.do(gadget)

		#mov     rax, [rcx+40h]
		#retn


  def test_gadget__ZN9__gnu_cxx18stdio_sync_filebufIwSt11char_traitsIwEE4fileEv(self):
		#_ZN9__gnu_cxx18stdio_sync_filebufIwSt11char_traitsIwEE4fileEv
		gadget = "488B4140C3"
		self.do(gadget)

		#mov     rax, [rcx+40h]
		#retn


  def test_gadget_nullsub_42(self):
		#nullsub_42
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_43(self):
		#nullsub_43
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_44(self):
		#nullsub_44
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_45(self):
		#nullsub_45
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_46(self):
		#nullsub_46
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_47(self):
		#nullsub_47
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_48(self):
		#nullsub_48
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_49(self):
		#nullsub_49
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_50(self):
		#nullsub_50
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_51(self):
		#nullsub_51
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_52(self):
		#nullsub_52
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_53(self):
		#nullsub_53
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_54(self):
		#nullsub_54
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_55(self):
		#nullsub_55
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_56(self):
		#nullsub_56
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_57(self):
		#nullsub_57
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_58(self):
		#nullsub_58
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_59(self):
		#nullsub_59
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_60(self):
		#nullsub_60
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_61(self):
		#nullsub_61
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_62(self):
		#nullsub_62
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_nullsub_63(self):
		#nullsub_63
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZN9__gnu_cxx6__poolILb0EE16_M_reclaim_blockEPcy(self):
		#_ZN9__gnu_cxx6__poolILb0EE16_M_reclaim_blockEPcy
		gadget = "488B4138482B11420FB7044048C1E00448034148488B00488B0848890A488910C3"
		self.do(gadget)

		#mov     rax, [rcx+38h]
		#sub     rdx, [rcx]
		#movzx   eax, word ptr [rax+r8*2]
		#shl     rax, 4
		#add     rax, [rcx+48h]
		#mov     rax, [rax]
		#mov     rcx, [rax]
		#mov     [rdx], rcx
		#mov     [rax], rdx
		#retn


  def test_gadget__ZN9__gnu_cxx6__poolILb1EE21_M_destroy_thread_keyEPv(self):
		#_ZN9__gnu_cxx6__poolILb1EE21_M_destroy_thread_keyEPv
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget_sub_6FC5E470(self):
		#sub_6FC5E470
		gadget = "488B0148894108C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     [rcx+8], rax
		#retn


  def test_gadget_sub_6FC5E5F0(self):
		#sub_6FC5E5F0
		gadget = "4883690808C3"
		self.do(gadget)

		#sub     qword ptr [rcx+8], 8
		#retn


  def test_gadget_sub_6FC5E630(self):
		#sub_6FC5E630
		gadget = "48C7010000000048C741080000000048C7411000000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     qword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#retn


  def test_gadget_sub_6FC5E650(self):
		#sub_6FC5E650
		gadget = "48C7010000000048C741080000000048C7411000000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     qword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#retn


  def test_gadget_sub_6FC5E680(self):
		#sub_6FC5E680
		gadget = "488B0148894108C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     [rcx+8], rax
		#retn


  def test_gadget_sub_6FC5E830(self):
		#sub_6FC5E830
		gadget = "4883690810C3"
		self.do(gadget)

		#sub     qword ptr [rcx+8], 10h
		#retn


  def test_gadget_sub_6FC5E880(self):
		#sub_6FC5E880
		gadget = "48C7010000000048C741080000000048C7411000000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     qword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#retn


  def test_gadget_sub_6FC5E8A0(self):
		#sub_6FC5E8A0
		gadget = "48C7010000000048C741080000000048C7411000000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     qword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#retn


  def test_gadget_sub_6FC5E8D0(self):
		#sub_6FC5E8D0
		gadget = "488B0148894108C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     [rcx+8], rax
		#retn


  def test_gadget_sub_6FC5EA80(self):
		#sub_6FC5EA80
		gadget = "4883690810C3"
		self.do(gadget)

		#sub     qword ptr [rcx+8], 10h
		#retn


  def test_gadget_sub_6FC5EAD0(self):
		#sub_6FC5EAD0
		gadget = "48C7010000000048C741080000000048C7411000000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     qword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#retn


  def test_gadget_sub_6FC5EAF0(self):
		#sub_6FC5EAF0
		gadget = "48C7010000000048C741080000000048C7411000000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#mov     qword ptr [rcx+8], 0
		#mov     qword ptr [rcx+10h], 0
		#retn


  def test_gadget_sub_6FC5F6D0(self):
		#sub_6FC5F6D0
		gadget = "488B024839010F94C0C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#cmp     [rcx], rax
		#setz    al
		#retn


  def test_gadget_sub_6FC5F6E0(self):
		#sub_6FC5F6E0
		gadget = "488B024839010F94C0C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#cmp     [rcx], rax
		#setz    al
		#retn


  def test_gadget_sub_6FC5F6F0(self):
		#sub_6FC5F6F0
		gadget = "488B024839010F94C0C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#cmp     [rcx], rax
		#setz    al
		#retn


  def test_gadget_sub_6FC5F700(self):
		#sub_6FC5F700
		gadget = "488B024839010F94C0C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#cmp     [rcx], rax
		#setz    al
		#retn


  def test_gadget__ZNK10__cxxabiv117__class_type_info20__do_find_public_srcExPKvPKS0_S2_(self):
		#_ZNK10__cxxabiv117__class_type_info20__do_find_public_srcExPKvPKS0_S2_
		gadget = "31C04C394424280F94C08D448001C3"
		self.do(gadget)

		#xor     eax, eax
		#cmp     [rsp+arg_20], r8
		#setz    al
		#lea     eax, [rax+rax*4+1]
		#retn


  def test_gadget__ZNK10__cxxabiv119__pointer_type_info14__is_pointer_pEv(self):
		#_ZNK10__cxxabiv119__pointer_type_info14__is_pointer_pEv
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget__ZNK10__cxxabiv120__function_type_info15__is_function_pEv(self):
		#_ZNK10__cxxabiv120__function_type_info15__is_function_pEv
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget__ZNK11__gnu_debug16_Error_formatter10_M_messageENS_13_Debug_msg_idE(self):
		#_ZNK11__gnu_debug16_Error_formatter10_M_messageENS_13_Debug_msg_idE
		gadget = "4889C8488D0D36BC08004863D2488B14D148899010020000C3"
		self.do(gadget)

		#mov     rax, rcx
		#lea     rcx, off_6FCEC160
		#movsxd  rdx, edx
		#mov     rdx, [rcx+rdx*8]
		#mov     [rax+210h], rdx
		#retn


  def test_gadget_sub_6FC61660(self):
		#sub_6FC61660
		gadget = "488D0559500900C3"
		self.do(gadget)

		#lea     rax, aFuture    ; "future"
		#retn


  def test_gadget_sub_6FC61830(self):
		#sub_6FC61830
		gadget = "488D05F14D0900C3"
		self.do(gadget)

		#lea     rax, aSystem    ; "system"
		#retn


  def test_gadget_sub_6FC61870(self):
		#sub_6FC61870
		gadget = "488D05A94D0900C3"
		self.do(gadget)

		#lea     rax, aGeneric   ; "generic"
		#retn


  def test_gadget_sub_6FC618B0(self):
		#sub_6FC618B0
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC618C0(self):
		#sub_6FC618C0
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC618D0(self):
		#sub_6FC618D0
		gadget = "48C7C0FFFFFFFFC3"
		self.do(gadget)

		#mov     rax, 0FFFFFFFFFFFFFFFFh
		#retn


  def test_gadget_sub_6FC618E0(self):
		#sub_6FC618E0
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC618F0(self):
		#sub_6FC618F0
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC61900(self):
		#sub_6FC61900
		gadget = "48B8FFFFFFFFFFFFFF7FC3"
		self.do(gadget)

		#mov     rax, 7FFFFFFFFFFFFFFFh
		#retn


  def test_gadget_sub_6FC61910(self):
		#sub_6FC61910
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC61920(self):
		#sub_6FC61920
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC61930(self):
		#sub_6FC61930
		gadget = "48C7C0FFFFFFFFC3"
		self.do(gadget)

		#mov     rax, 0FFFFFFFFFFFFFFFFh
		#retn


  def test_gadget_sub_6FC61940(self):
		#sub_6FC61940
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC61950(self):
		#sub_6FC61950
		gadget = "4889D0C3"
		self.do(gadget)

		#mov     rax, rdx
		#retn


  def test_gadget_sub_6FC61960(self):
		#sub_6FC61960
		gadget = "48B8FFFFFFFFFFFFFF7FC3"
		self.do(gadget)

		#mov     rax, 7FFFFFFFFFFFFFFFh
		#retn


  def test_gadget_sub_6FC61970(self):
		#sub_6FC61970
		gadget = "488D0589360900C3"
		self.do(gadget)

		#lea     rax, a__gnu_cxx__con; "__gnu_cxx::__concurrence_lock_error"
		#retn


  def test_gadget_sub_6FC61980(self):
		#sub_6FC61980
		gadget = "488D05A1360900C3"
		self.do(gadget)

		#lea     rax, a__gnu_cxx__c_0; "__gnu_cxx::__concurrence_unlock_error"
		#retn


  def test_gadget_sub_6FC61990(self):
		#sub_6FC61990
		gadget = "488B4110482B410848C1F803C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#sub     rax, [rcx+8]
		#sar     rax, 3
		#retn


  def test_gadget_sub_6FC619A0(self):
		#sub_6FC619A0
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget_sub_6FC619B0(self):
		#sub_6FC619B0
		gadget = "488B41084883E808C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#sub     rax, 8
		#retn


  def test_gadget_sub_6FC619C0(self):
		#sub_6FC619C0
		gadget = "488B4108482B0148C1F803C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#sub     rax, [rcx]
		#sar     rax, 3
		#retn


  def test_gadget_sub_6FC619D0(self):
		#sub_6FC619D0
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget_sub_6FC619E0(self):
		#sub_6FC619E0
		gadget = "488D04D500000000480301C3"
		self.do(gadget)

		#lea     rax, ds:0[rdx*8]
		#add     rax, [rcx]
		#retn


  def test_gadget_sub_6FC619F0(self):
		#sub_6FC619F0
		gadget = "488B4110482B410848C1F804C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#sub     rax, [rcx+8]
		#sar     rax, 4
		#retn


  def test_gadget_sub_6FC61A00(self):
		#sub_6FC61A00
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget_sub_6FC61A10(self):
		#sub_6FC61A10
		gadget = "488B41084883E810C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#sub     rax, 10h
		#retn


  def test_gadget_sub_6FC61A20(self):
		#sub_6FC61A20
		gadget = "488B4108482B0148C1F804C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#sub     rax, [rcx]
		#sar     rax, 4
		#retn


  def test_gadget_sub_6FC61A30(self):
		#sub_6FC61A30
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget_sub_6FC61A40(self):
		#sub_6FC61A40
		gadget = "4889D048C1E004480301C3"
		self.do(gadget)

		#mov     rax, rdx
		#shl     rax, 4
		#add     rax, [rcx]
		#retn


  def test_gadget_sub_6FC61A50(self):
		#sub_6FC61A50
		gadget = "488B4110482B410848C1F804C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#sub     rax, [rcx+8]
		#sar     rax, 4
		#retn


  def test_gadget_sub_6FC61A60(self):
		#sub_6FC61A60
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget_sub_6FC61A70(self):
		#sub_6FC61A70
		gadget = "488B41084883E810C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#sub     rax, 10h
		#retn


  def test_gadget_sub_6FC61A80(self):
		#sub_6FC61A80
		gadget = "488B4108482B0148C1F804C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#sub     rax, [rcx]
		#sar     rax, 4
		#retn


  def test_gadget_sub_6FC61A90(self):
		#sub_6FC61A90
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget_sub_6FC61AA0(self):
		#sub_6FC61AA0
		gadget = "4889D048C1E004480301C3"
		self.do(gadget)

		#mov     rax, rdx
		#shl     rax, 4
		#add     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE13get_allocatorEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE13get_allocatorEv
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE3endEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE3endEv
		gadget = "488B01488B50E8488D0450C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rax-18h]
		#lea     rax, [rax+rdx*2]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4_Rep12_M_is_leakedEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4_Rep12_M_is_leakedEv
		gadget = "8B4110C1E81FC3"
		self.do(gadget)

		#mov     eax, [rcx+10h]
		#shr     eax, 1Fh
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4_Rep12_M_is_sharedEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4_Rep12_M_is_sharedEv
		gadget = "8B411085C00F9FC0C3"
		self.do(gadget)

		#mov     eax, [rcx+10h]
		#test    eax, eax
		#setnle  al
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4backEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4backEv
		gadget = "488B01488B50E8488D4450FEC3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rax-18h]
		#lea     rax, [rax+rdx*2-2]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4cendEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4cendEv
		gadget = "488B01488B50E8488D0450C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rax-18h]
		#lea     rax, [rax+rdx*2]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4dataEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4dataEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4rendEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4rendEv
		gadget = "488B124889C8488911C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE4sizeEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE4sizeEv
		gadget = "488B01488B40E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE5beginEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE5beginEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE5c_strEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE5c_strEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE5crendEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE5crendEv
		gadget = "488B124889C8488911C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE5emptyEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE5emptyEv
		gadget = "488B01488378E8000F94C0C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#cmp     qword ptr [rax-18h], 0
		#setz    al
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE5frontEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE5frontEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE6_M_repEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE6_M_repEv
		gadget = "488B014883E818C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#sub     rax, 18h
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE6cbeginEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE6cbeginEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE6lengthEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE6lengthEv
		gadget = "488B01488B40E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE6rbeginEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE6rbeginEv
		gadget = "488B124889C8488B4AE8488D144A488910C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#mov     rcx, [rdx-18h]
		#lea     rdx, [rdx+rcx*2]
		#mov     [rax], rdx
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE7_M_dataEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE7_M_dataEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE7_M_iendEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE7_M_iendEv
		gadget = "488B01488B50E8488D0450C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rax-18h]
		#lea     rax, [rax+rdx*2]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE7crbeginEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE7crbeginEv
		gadget = "488B124889C8488B4AE8488D144A488910C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#mov     rcx, [rdx-18h]
		#lea     rdx, [rdx+rcx*2]
		#mov     [rax], rdx
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE8_M_limitEyy(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE8_M_limitEyy
		gadget = "488B01488B40E84829D04939C0490F46C0C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-18h]
		#sub     rax, rdx
		#cmp     r8, rax
		#cmovbe  rax, r8
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE8capacityEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE8capacityEv
		gadget = "488B01488B40F0C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-10h]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE8max_sizeEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE8max_sizeEv
		gadget = "48B8FCFFFFFFFFFFFF1FC3"
		self.do(gadget)

		#mov     rax, 1FFFFFFFFFFFFFFCh
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEE9_M_ibeginEv(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEE9_M_ibeginEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSbIwSt11char_traitsIwESaIwEEixEy(self):
		#_ZNKSbIwSt11char_traitsIwESaIwEEixEy
		gadget = "488D0412480301C3"
		self.do(gadget)

		#lea     rax, [rdx+rdx]
		#add     rax, [rcx]
		#retn


  def test_gadget__ZNKSi6gcountEv(self):
		#_ZNKSi6gcountEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSi6sentrycvbEv(self):
		#_ZNKSi6sentrycvbEv
		gadget = "0FB601C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx]
		#retn


  def test_gadget__ZNKSo6sentrycvbEv(self):
		#_ZNKSo6sentrycvbEv
		gadget = "0FB601C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx]
		#retn


  def test_gadget__ZNKSs13get_allocatorEv(self):
		#_ZNKSs13get_allocatorEv
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNKSs3endEv(self):
		#_ZNKSs3endEv
		gadget = "488B01480340E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#add     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSs4_Rep12_M_is_leakedEv(self):
		#_ZNKSs4_Rep12_M_is_leakedEv
		gadget = "8B4110C1E81FC3"
		self.do(gadget)

		#mov     eax, [rcx+10h]
		#shr     eax, 1Fh
		#retn


  def test_gadget__ZNKSs4_Rep12_M_is_sharedEv(self):
		#_ZNKSs4_Rep12_M_is_sharedEv
		gadget = "448B59104585DB0F9FC0C3"
		self.do(gadget)

		#mov     r11d, [rcx+10h]
		#test    r11d, r11d
		#setnle  al
		#retn


  def test_gadget__ZNKSs4backEv(self):
		#_ZNKSs4backEv
		gadget = "488B01488B50E8488D4410FFC3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rax-18h]
		#lea     rax, [rax+rdx-1]
		#retn


  def test_gadget__ZNKSs4cendEv(self):
		#_ZNKSs4cendEv
		gadget = "488B01480340E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#add     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSs4dataEv(self):
		#_ZNKSs4dataEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSs4rendEv(self):
		#_ZNKSs4rendEv
		gadget = "488B124889C8488911C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSs4sizeEv(self):
		#_ZNKSs4sizeEv
		gadget = "488B01488B40E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSs5beginEv(self):
		#_ZNKSs5beginEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSs5c_strEv(self):
		#_ZNKSs5c_strEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSs5crendEv(self):
		#_ZNKSs5crendEv
		gadget = "488B124889C8488911C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSs5emptyEv(self):
		#_ZNKSs5emptyEv
		gadget = "488B01488378E8000F94C0C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#cmp     qword ptr [rax-18h], 0
		#setz    al
		#retn


  def test_gadget__ZNKSs5frontEv(self):
		#_ZNKSs5frontEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSs6_M_repEv(self):
		#_ZNKSs6_M_repEv
		gadget = "488B014883E818C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#sub     rax, 18h
		#retn


  def test_gadget__ZNKSs6cbeginEv(self):
		#_ZNKSs6cbeginEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSs6lengthEv(self):
		#_ZNKSs6lengthEv
		gadget = "488B01488B40E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSs6rbeginEv(self):
		#_ZNKSs6rbeginEv
		gadget = "488B124889C8480352E8488911C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#add     rdx, [rdx-18h]
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSs7_M_dataEv(self):
		#_ZNKSs7_M_dataEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSs7_M_iendEv(self):
		#_ZNKSs7_M_iendEv
		gadget = "488B01480340E8C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#add     rax, [rax-18h]
		#retn


  def test_gadget__ZNKSs7crbeginEv(self):
		#_ZNKSs7crbeginEv
		gadget = "488B124889C8480352E8488911C3"
		self.do(gadget)

		#mov     rdx, [rdx]
		#mov     rax, rcx
		#add     rdx, [rdx-18h]
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSs8_M_limitEyy(self):
		#_ZNKSs8_M_limitEyy
		gadget = "488B01488B40E84829D04939C0490F46C0C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-18h]
		#sub     rax, rdx
		#cmp     r8, rax
		#cmovbe  rax, r8
		#retn


  def test_gadget__ZNKSs8capacityEv(self):
		#_ZNKSs8capacityEv
		gadget = "488B01488B40F0C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-10h]
		#retn


  def test_gadget__ZNKSs8max_sizeEv(self):
		#_ZNKSs8max_sizeEv
		gadget = "48B8F9FFFFFFFFFFFF3FC3"
		self.do(gadget)

		#mov     rax, 3FFFFFFFFFFFFFF9h
		#retn


  def test_gadget__ZNKSs9_M_ibeginEv(self):
		#_ZNKSs9_M_ibeginEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSsixEy(self):
		#_ZNKSsixEy
		gadget = "4889D0480301C3"
		self.do(gadget)

		#mov     rax, rdx
		#add     rax, [rcx]
		#retn


  def test_gadget__ZNKSt10bad_typeid4whatEv(self):
		#_ZNKSt10bad_typeid4whatEv
		gadget = "488D05D9400900C3"
		self.do(gadget)

		#lea     rax, aStdBad_typeid; "std::bad_typeid"
		#retn


  def test_gadget__ZNKSt10istrstream5rdbufEv(self):
		#_ZNKSt10istrstream5rdbufEv
		gadget = "488D4110C3"
		self.do(gadget)

		#lea     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb0EE13do_neg_formatEv(self):
		#_ZNKSt10moneypunctIcLb0EE13do_neg_formatEv
		gadget = "488B41108B4060C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+60h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb0EE13do_pos_formatEv(self):
		#_ZNKSt10moneypunctIcLb0EE13do_pos_formatEv
		gadget = "488B41108B405CC3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+5Ch]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb0EE14do_frac_digitsEv(self):
		#_ZNKSt10moneypunctIcLb0EE14do_frac_digitsEv
		gadget = "488B41108B4058C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+58h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb0EE16do_decimal_pointEv(self):
		#_ZNKSt10moneypunctIcLb0EE16do_decimal_pointEv
		gadget = "488B41100FB64021C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, byte ptr [rax+21h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb0EE16do_thousands_sepEv(self):
		#_ZNKSt10moneypunctIcLb0EE16do_thousands_sepEv
		gadget = "488B41100FB64022C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, byte ptr [rax+22h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb1EE13do_neg_formatEv(self):
		#_ZNKSt10moneypunctIcLb1EE13do_neg_formatEv
		gadget = "488B41108B4060C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+60h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb1EE13do_pos_formatEv(self):
		#_ZNKSt10moneypunctIcLb1EE13do_pos_formatEv
		gadget = "488B41108B405CC3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+5Ch]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb1EE14do_frac_digitsEv(self):
		#_ZNKSt10moneypunctIcLb1EE14do_frac_digitsEv
		gadget = "488B41108B4058C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+58h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb1EE16do_decimal_pointEv(self):
		#_ZNKSt10moneypunctIcLb1EE16do_decimal_pointEv
		gadget = "488B41100FB64021C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, byte ptr [rax+21h]
		#retn


  def test_gadget__ZNKSt10moneypunctIcLb1EE16do_thousands_sepEv(self):
		#_ZNKSt10moneypunctIcLb1EE16do_thousands_sepEv
		gadget = "488B41100FB64022C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, byte ptr [rax+22h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb0EE13do_neg_formatEv(self):
		#_ZNKSt10moneypunctIwLb0EE13do_neg_formatEv
		gadget = "488B41108B4060C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+60h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb0EE13do_pos_formatEv(self):
		#_ZNKSt10moneypunctIwLb0EE13do_pos_formatEv
		gadget = "488B41108B405CC3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+5Ch]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb0EE14do_frac_digitsEv(self):
		#_ZNKSt10moneypunctIwLb0EE14do_frac_digitsEv
		gadget = "488B41108B4058C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+58h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb0EE16do_decimal_pointEv(self):
		#_ZNKSt10moneypunctIwLb0EE16do_decimal_pointEv
		gadget = "488B41100FB74022C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, word ptr [rax+22h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb0EE16do_thousands_sepEv(self):
		#_ZNKSt10moneypunctIwLb0EE16do_thousands_sepEv
		gadget = "488B41100FB74024C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, word ptr [rax+24h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb1EE13do_neg_formatEv(self):
		#_ZNKSt10moneypunctIwLb1EE13do_neg_formatEv
		gadget = "488B41108B4060C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+60h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb1EE13do_pos_formatEv(self):
		#_ZNKSt10moneypunctIwLb1EE13do_pos_formatEv
		gadget = "488B41108B405CC3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+5Ch]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb1EE14do_frac_digitsEv(self):
		#_ZNKSt10moneypunctIwLb1EE14do_frac_digitsEv
		gadget = "488B41108B4058C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     eax, [rax+58h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb1EE16do_decimal_pointEv(self):
		#_ZNKSt10moneypunctIwLb1EE16do_decimal_pointEv
		gadget = "488B41100FB74022C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, word ptr [rax+22h]
		#retn


  def test_gadget__ZNKSt10moneypunctIwLb1EE16do_thousands_sepEv(self):
		#_ZNKSt10moneypunctIwLb1EE16do_thousands_sepEv
		gadget = "488B41100FB74024C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, word ptr [rax+24h]
		#retn


  def test_gadget__ZNKSt10ostrstream5rdbufEv(self):
		#_ZNKSt10ostrstream5rdbufEv
		gadget = "488D4108C3"
		self.do(gadget)

		#lea     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt11__timepunctIcE15_M_am_pm_formatEPKc(self):
		#_ZNKSt11__timepunctIcE15_M_am_pm_formatEPKc
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNKSt11__timepunctIcE15_M_date_formatsEPPKc(self):
		#_ZNKSt11__timepunctIcE15_M_date_formatsEPPKc
		gadget = "488B4110488B4010488902488B4110488B401848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+10h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+18h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE15_M_time_formatsEPPKc(self):
		#_ZNKSt11__timepunctIcE15_M_time_formatsEPPKc
		gadget = "488B4110488B4020488902488B4110488B402848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+20h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+28h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE19_M_days_abbreviatedEPPKc(self):
		#_ZNKSt11__timepunctIcE19_M_days_abbreviatedEPPKc
		gadget = "488B4110488B8090000000488902488B4110488B809800000048894208488B4110488B80A000000048894210488B4110488B80A800000048894218488B4110488B80B000000048894220488B4110488B80B800000048894228488B4110488B80C000000048894230C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+90h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+98h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0A0h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0A8h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0B0h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0B8h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0C0h]
		#mov     [rdx+30h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE20_M_date_time_formatsEPPKc(self):
		#_ZNKSt11__timepunctIcE20_M_date_time_formatsEPPKc
		gadget = "488B4110488B4030488902488B4110488B403848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+30h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+38h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE21_M_months_abbreviatedEPPKc(self):
		#_ZNKSt11__timepunctIcE21_M_months_abbreviatedEPPKc
		gadget = "488B4110488B8028010000488902488B4110488B803001000048894208488B4110488B803801000048894210488B4110488B804001000048894218488B4110488B804801000048894220488B4110488B805001000048894228488B4110488B805801000048894230488B4110488B806001000048894238488B4110488B806801000048894240488B4110488B807001000048894248488B4110488B807801000048894250488B4110488B808001000048894258C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+128h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+130h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+138h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+140h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+148h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+150h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+158h]
		#mov     [rdx+30h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+160h]
		#mov     [rdx+38h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+168h]
		#mov     [rdx+40h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+170h]
		#mov     [rdx+48h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+178h]
		#mov     [rdx+50h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+180h]
		#mov     [rdx+58h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE7_M_daysEPPKc(self):
		#_ZNKSt11__timepunctIcE7_M_daysEPPKc
		gadget = "488B4110488B4058488902488B4110488B406048894208488B4110488B406848894210488B4110488B407048894218488B4110488B407848894220488B4110488B808000000048894228488B4110488B808800000048894230C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+58h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+60h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+68h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+70h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+78h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+80h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+88h]
		#mov     [rdx+30h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE8_M_am_pmEPPKc(self):
		#_ZNKSt11__timepunctIcE8_M_am_pmEPPKc
		gadget = "488B4110488B4040488902488B4110488B404848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+40h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+48h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIcE9_M_monthsEPPKc(self):
		#_ZNKSt11__timepunctIcE9_M_monthsEPPKc
		gadget = "488B4110488B80C8000000488902488B4110488B80D000000048894208488B4110488B80D800000048894210488B4110488B80E000000048894218488B4110488B80E800000048894220488B4110488B80F000000048894228488B4110488B80F800000048894230488B4110488B800001000048894238488B4110488B800801000048894240488B4110488B801001000048894248488B4110488B801801000048894250488B4110488B802001000048894258C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0C8h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0D0h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0D8h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0E0h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0E8h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0F0h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0F8h]
		#mov     [rdx+30h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+100h]
		#mov     [rdx+38h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+108h]
		#mov     [rdx+40h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+110h]
		#mov     [rdx+48h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+118h]
		#mov     [rdx+50h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+120h]
		#mov     [rdx+58h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE15_M_am_pm_formatEPKw(self):
		#_ZNKSt11__timepunctIwE15_M_am_pm_formatEPKw
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNKSt11__timepunctIwE15_M_date_formatsEPPKw(self):
		#_ZNKSt11__timepunctIwE15_M_date_formatsEPPKw
		gadget = "488B4110488B4010488902488B4110488B401848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+10h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+18h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE15_M_time_formatsEPPKw(self):
		#_ZNKSt11__timepunctIwE15_M_time_formatsEPPKw
		gadget = "488B4110488B4020488902488B4110488B402848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+20h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+28h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE19_M_days_abbreviatedEPPKw(self):
		#_ZNKSt11__timepunctIwE19_M_days_abbreviatedEPPKw
		gadget = "488B4110488B8090000000488902488B4110488B809800000048894208488B4110488B80A000000048894210488B4110488B80A800000048894218488B4110488B80B000000048894220488B4110488B80B800000048894228488B4110488B80C000000048894230C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+90h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+98h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0A0h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0A8h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0B0h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0B8h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0C0h]
		#mov     [rdx+30h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE20_M_date_time_formatsEPPKw(self):
		#_ZNKSt11__timepunctIwE20_M_date_time_formatsEPPKw
		gadget = "488B4110488B4030488902488B4110488B403848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+30h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+38h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE21_M_months_abbreviatedEPPKw(self):
		#_ZNKSt11__timepunctIwE21_M_months_abbreviatedEPPKw
		gadget = "488B4110488B8028010000488902488B4110488B803001000048894208488B4110488B803801000048894210488B4110488B804001000048894218488B4110488B804801000048894220488B4110488B805001000048894228488B4110488B805801000048894230488B4110488B806001000048894238488B4110488B806801000048894240488B4110488B807001000048894248488B4110488B807801000048894250488B4110488B808001000048894258C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+128h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+130h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+138h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+140h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+148h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+150h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+158h]
		#mov     [rdx+30h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+160h]
		#mov     [rdx+38h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+168h]
		#mov     [rdx+40h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+170h]
		#mov     [rdx+48h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+178h]
		#mov     [rdx+50h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+180h]
		#mov     [rdx+58h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE7_M_daysEPPKw(self):
		#_ZNKSt11__timepunctIwE7_M_daysEPPKw
		gadget = "488B4110488B4058488902488B4110488B406048894208488B4110488B406848894210488B4110488B407048894218488B4110488B407848894220488B4110488B808000000048894228488B4110488B808800000048894230C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+58h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+60h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+68h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+70h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+78h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+80h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+88h]
		#mov     [rdx+30h], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE8_M_am_pmEPPKw(self):
		#_ZNKSt11__timepunctIwE8_M_am_pmEPPKw
		gadget = "488B4110488B4040488902488B4110488B404848894208C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+40h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+48h]
		#mov     [rdx+8], rax
		#retn


  def test_gadget__ZNKSt11__timepunctIwE9_M_monthsEPPKw(self):
		#_ZNKSt11__timepunctIwE9_M_monthsEPPKw
		gadget = "488B4110488B80C8000000488902488B4110488B80D000000048894208488B4110488B80D800000048894210488B4110488B80E000000048894218488B4110488B80E800000048894220488B4110488B80F000000048894228488B4110488B80F800000048894230488B4110488B800001000048894238488B4110488B800801000048894240488B4110488B801001000048894248488B4110488B801801000048894250488B4110488B802001000048894258C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0C8h]
		#mov     [rdx], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0D0h]
		#mov     [rdx+8], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0D8h]
		#mov     [rdx+10h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0E0h]
		#mov     [rdx+18h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0E8h]
		#mov     [rdx+20h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0F0h]
		#mov     [rdx+28h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+0F8h]
		#mov     [rdx+30h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+100h]
		#mov     [rdx+38h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+108h]
		#mov     [rdx+40h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+110h]
		#mov     [rdx+48h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+118h]
		#mov     [rdx+50h], rax
		#mov     rax, [rcx+10h]
		#mov     rax, [rax+120h]
		#mov     [rdx+58h], rax
		#retn


  def test_gadget__ZNKSt11logic_error4whatEv(self):
		#_ZNKSt11logic_error4whatEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt12__basic_fileIcE7is_openEv(self):
		#_ZNKSt12__basic_fileIcE7is_openEv
		gadget = "488339000F95C0C3"
		self.do(gadget)

		#cmp     qword ptr [rcx], 0
		#setnz   al
		#retn


  def test_gadget__ZNKSt12bad_weak_ptr4whatEv(self):
		#_ZNKSt12bad_weak_ptr4whatEv
		gadget = "488D05391E0900C3"
		self.do(gadget)

		#lea     rax, aStdBad_weak_pt; "std::bad_weak_ptr"
		#retn


  def test_gadget__ZNKSt13bad_exception4whatEv(self):
		#_ZNKSt13bad_exception4whatEv
		gadget = "488D05282D0900C3"
		self.do(gadget)

		#lea     rax, aStdBad_excepti; "std::bad_exception"
		#retn


  def test_gadget__ZNKSt13basic_fstreamIcSt11char_traitsIcEE5rdbufEv(self):
		#_ZNKSt13basic_fstreamIcSt11char_traitsIcEE5rdbufEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt13basic_fstreamIwSt11char_traitsIwEE5rdbufEv(self):
		#_ZNKSt13basic_fstreamIwSt11char_traitsIwEE5rdbufEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt13basic_istreamIwSt11char_traitsIwEE6gcountEv(self):
		#_ZNKSt13basic_istreamIwSt11char_traitsIwEE6gcountEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt13basic_istreamIwSt11char_traitsIwEE6sentrycvbEv(self):
		#_ZNKSt13basic_istreamIwSt11char_traitsIwEE6sentrycvbEv
		gadget = "0FB601C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx]
		#retn


  def test_gadget__ZNKSt13basic_ostreamIwSt11char_traitsIwEE6sentrycvbEv(self):
		#_ZNKSt13basic_ostreamIwSt11char_traitsIwEE6sentrycvbEv
		gadget = "0FB601C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx]
		#retn


  def test_gadget__ZNKSt13runtime_error4whatEv(self):
		#_ZNKSt13runtime_error4whatEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt14basic_ifstreamIcSt11char_traitsIcEE5rdbufEv(self):
		#_ZNKSt14basic_ifstreamIcSt11char_traitsIcEE5rdbufEv
		gadget = "488D4110C3"
		self.do(gadget)

		#lea     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt14basic_ifstreamIwSt11char_traitsIwEE5rdbufEv(self):
		#_ZNKSt14basic_ifstreamIwSt11char_traitsIwEE5rdbufEv
		gadget = "488D4110C3"
		self.do(gadget)

		#lea     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt14basic_ofstreamIcSt11char_traitsIcEE5rdbufEv(self):
		#_ZNKSt14basic_ofstreamIcSt11char_traitsIcEE5rdbufEv
		gadget = "488D4108C3"
		self.do(gadget)

		#lea     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt14basic_ofstreamIwSt11char_traitsIwEE5rdbufEv(self):
		#_ZNKSt14basic_ofstreamIwSt11char_traitsIwEE5rdbufEv
		gadget = "488D4108C3"
		self.do(gadget)

		#lea     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt14error_category23default_error_conditionEi(self):
		#_ZNKSt14error_category23default_error_conditionEi
		gadget = "4889C844890148895108C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     [rcx], r8d
		#mov     [rcx+8], rdx
		#retn


  def test_gadget__ZNKSt15__exception_ptr13exception_ptr20__cxa_exception_typeEv(self):
		#_ZNKSt15__exception_ptr13exception_ptr20__cxa_exception_typeEv
		gadget = "488B01488B4090C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rax, [rax-70h]
		#retn


  def test_gadget_sub_6FC64B60(self):
		#sub_6FC64B60
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSt15__exception_ptr13exception_ptrntEv(self):
		#_ZNKSt15__exception_ptr13exception_ptrntEv
		gadget = "488339000F94C0C3"
		self.do(gadget)

		#cmp     qword ptr [rcx], 0
		#setz    al
		#retn


  def test_gadget__ZNKSt15basic_streambufIcSt11char_traitsIcEE4gptrEv(self):
		#_ZNKSt15basic_streambufIcSt11char_traitsIcEE4gptrEv
		gadget = "488B4110C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIcSt11char_traitsIcEE4pptrEv(self):
		#_ZNKSt15basic_streambufIcSt11char_traitsIcEE4pptrEv
		gadget = "488B4128C3"
		self.do(gadget)

		#mov     rax, [rcx+28h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIcSt11char_traitsIcEE5ebackEv(self):
		#_ZNKSt15basic_streambufIcSt11char_traitsIcEE5ebackEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt15basic_streambufIcSt11char_traitsIcEE5egptrEv(self):
		#_ZNKSt15basic_streambufIcSt11char_traitsIcEE5egptrEv
		gadget = "488B4118C3"
		self.do(gadget)

		#mov     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIcSt11char_traitsIcEE5epptrEv(self):
		#_ZNKSt15basic_streambufIcSt11char_traitsIcEE5epptrEv
		gadget = "488B4130C3"
		self.do(gadget)

		#mov     rax, [rcx+30h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIcSt11char_traitsIcEE5pbaseEv(self):
		#_ZNKSt15basic_streambufIcSt11char_traitsIcEE5pbaseEv
		gadget = "488B4120C3"
		self.do(gadget)

		#mov     rax, [rcx+20h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIwSt11char_traitsIwEE4gptrEv(self):
		#_ZNKSt15basic_streambufIwSt11char_traitsIwEE4gptrEv
		gadget = "488B4110C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIwSt11char_traitsIwEE4pptrEv(self):
		#_ZNKSt15basic_streambufIwSt11char_traitsIwEE4pptrEv
		gadget = "488B4128C3"
		self.do(gadget)

		#mov     rax, [rcx+28h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIwSt11char_traitsIwEE5ebackEv(self):
		#_ZNKSt15basic_streambufIwSt11char_traitsIwEE5ebackEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt15basic_streambufIwSt11char_traitsIwEE5egptrEv(self):
		#_ZNKSt15basic_streambufIwSt11char_traitsIwEE5egptrEv
		gadget = "488B4118C3"
		self.do(gadget)

		#mov     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIwSt11char_traitsIwEE5epptrEv(self):
		#_ZNKSt15basic_streambufIwSt11char_traitsIwEE5epptrEv
		gadget = "488B4130C3"
		self.do(gadget)

		#mov     rax, [rcx+30h]
		#retn


  def test_gadget__ZNKSt15basic_streambufIwSt11char_traitsIwEE5pbaseEv(self):
		#_ZNKSt15basic_streambufIwSt11char_traitsIwEE5pbaseEv
		gadget = "488B4120C3"
		self.do(gadget)

		#mov     rax, [rcx+20h]
		#retn


  def test_gadget__ZNKSt18basic_stringstreamIcSt11char_traitsIcESaIcEE5rdbufEv(self):
		#_ZNKSt18basic_stringstreamIcSt11char_traitsIcESaIcEE5rdbufEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt18basic_stringstreamIwSt11char_traitsIwESaIwEE5rdbufEv(self):
		#_ZNKSt18basic_stringstreamIwSt11char_traitsIwESaIwEE5rdbufEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt19basic_istringstreamIcSt11char_traitsIcESaIcEE5rdbufEv(self):
		#_ZNKSt19basic_istringstreamIcSt11char_traitsIcESaIcEE5rdbufEv
		gadget = "488D4110C3"
		self.do(gadget)

		#lea     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt19basic_istringstreamIwSt11char_traitsIwESaIwEE5rdbufEv(self):
		#_ZNKSt19basic_istringstreamIwSt11char_traitsIwESaIwEE5rdbufEv
		gadget = "488D4110C3"
		self.do(gadget)

		#lea     rax, [rcx+10h]
		#retn


  def test_gadget__ZNKSt19basic_ostringstreamIcSt11char_traitsIcESaIcEE5rdbufEv(self):
		#_ZNKSt19basic_ostringstreamIcSt11char_traitsIcESaIcEE5rdbufEv
		gadget = "488D4108C3"
		self.do(gadget)

		#lea     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt19basic_ostringstreamIwSt11char_traitsIwESaIwEE5rdbufEv(self):
		#_ZNKSt19basic_ostringstreamIwSt11char_traitsIwESaIwEE5rdbufEv
		gadget = "488D4108C3"
		self.do(gadget)

		#lea     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt5ctypeIcE10do_tolowerEc(self):
		#_ZNKSt5ctypeIcE10do_tolowerEc
		gadget = "488B4930440FB6C289D08D502042F60441010F45C2C3"
		self.do(gadget)

		#mov     rcx, [rcx+30h]
		#movzx   r8d, dl
		#mov     eax, edx
		#lea     edx, [rax+20h]
		#test    byte ptr [rcx+r8*2], 1
		#cmovnz  eax, edx
		#retn


  def test_gadget__ZNKSt5ctypeIcE10do_toupperEc(self):
		#_ZNKSt5ctypeIcE10do_toupperEc
		gadget = "488B4930440FB6C289D08D50E042F60441020F45C2C3"
		self.do(gadget)

		#mov     rcx, [rcx+30h]
		#movzx   r8d, dl
		#mov     eax, edx
		#lea     edx, [rax-20h]
		#test    byte ptr [rcx+r8*2], 2
		#cmovnz  eax, edx
		#retn


  def test_gadget__ZNKSt5ctypeIcE8do_widenEc(self):
		#_ZNKSt5ctypeIcE8do_widenEc
		gadget = "89D0C3"
		self.do(gadget)

		#mov     eax, edx
		#retn


  def test_gadget__ZNKSt5ctypeIcE9do_narrowEcc(self):
		#_ZNKSt5ctypeIcE9do_narrowEcc
		gadget = "89D0C3"
		self.do(gadget)

		#mov     eax, edx
		#retn


  def test_gadget__ZNKSt5ctypeIwE8do_widenEc(self):
		#_ZNKSt5ctypeIwE8do_widenEc
		gadget = "0FB6D20FB784519A000000C3"
		self.do(gadget)

		#movzx   edx, dl
		#movzx   eax, word ptr [rcx+rdx*2+9Ah]
		#retn


  def test_gadget__ZNKSt7codecvtIcciE10do_unshiftERiPcS2_RS2_(self):
		#_ZNKSt7codecvtIcciE10do_unshiftERiPcS2_RS2_
		gadget = "488B4424284C8900B803000000C3"
		self.do(gadget)

		#mov     rax, [rsp+arg_20]
		#mov     [rax], r8
		#mov     eax, 3
		#retn


  def test_gadget__ZNKSt7codecvtIcciE11do_encodingEv(self):
		#_ZNKSt7codecvtIcciE11do_encodingEv
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget__ZNKSt7codecvtIcciE13do_max_lengthEv(self):
		#_ZNKSt7codecvtIcciE13do_max_lengthEv
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget__ZNKSt7codecvtIcciE16do_always_noconvEv(self):
		#_ZNKSt7codecvtIcciE16do_always_noconvEv
		gadget = "B801000000C3"
		self.do(gadget)

		#mov     eax, 1
		#retn


  def test_gadget__ZNKSt7codecvtIcciE5do_inERiPKcS3_RS3_PcS5_RS5_(self):
		#_ZNKSt7codecvtIcciE5do_inERiPKcS3_RS3_PcS5_RS5_
		gadget = "488B442428488B5424304C8900488B442440488910B803000000C3"
		self.do(gadget)

		#mov     rax, [rsp+arg_20]
		#mov     rdx, [rsp+arg_28]
		#mov     [rax], r8
		#mov     rax, [rsp+arg_38]
		#mov     [rax], rdx
		#mov     eax, 3
		#retn


  def test_gadget__ZNKSt7codecvtIcciE6do_outERiPKcS3_RS3_PcS5_RS5_(self):
		#_ZNKSt7codecvtIcciE6do_outERiPKcS3_RS3_PcS5_RS5_
		gadget = "488B442428488B5424304C8900488B442440488910B803000000C3"
		self.do(gadget)

		#mov     rax, [rsp+arg_20]
		#mov     rdx, [rsp+arg_28]
		#mov     [rax], r8
		#mov     rax, [rsp+arg_38]
		#mov     [rax], rdx
		#mov     eax, 3
		#retn


  def test_gadget__ZNKSt7codecvtIcciE9do_lengthERiPKcS3_y(self):
		#_ZNKSt7codecvtIcciE9do_lengthERiPKcS3_y
		gadget = "488B4424284D29C14939C1490F46C1C3"
		self.do(gadget)

		#mov     rax, [rsp+arg_20]
		#sub     r9, r8
		#cmp     r9, rax
		#cmovbe  rax, r9
		#retn


  def test_gadget__ZNKSt7codecvtIwciE10do_unshiftERiPcS2_RS2_(self):
		#_ZNKSt7codecvtIwciE10do_unshiftERiPcS2_RS2_
		gadget = "488B4424284C8900B803000000C3"
		self.do(gadget)

		#mov     rax, [rsp+arg_20]
		#mov     [rax], r8
		#mov     eax, 3
		#retn


  def test_gadget__ZNKSt7codecvtIwciE11do_encodingEv(self):
		#_ZNKSt7codecvtIwciE11do_encodingEv
		gadget = "488B05E17F0D008338010F94C00FB6C0C3"
		self.do(gadget)

		#mov     rax, cs:__imp___mb_cur_max
		#cmp     dword ptr [rax], 1
		#setz    al
		#movzx   eax, al
		#retn


  def test_gadget__ZNKSt7codecvtIwciE13do_max_lengthEv(self):
		#_ZNKSt7codecvtIwciE13do_max_lengthEv
		gadget = "488B05C17F0D008B00C3"
		self.do(gadget)

		#mov     rax, cs:__imp___mb_cur_max
		#mov     eax, [rax]
		#retn


  def test_gadget__ZNKSt7codecvtIwciE16do_always_noconvEv(self):
		#_ZNKSt7codecvtIwciE16do_always_noconvEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt8bad_cast4whatEv(self):
		#_ZNKSt8bad_cast4whatEv
		gadget = "488D0589C50700C3"
		self.do(gadget)

		#lea     rax, aStdBad_cast; "std::bad_cast"
		#retn


  def test_gadget__ZNKSt8ios_base7failure4whatEv(self):
		#_ZNKSt8ios_base7failure4whatEv
		gadget = "488B4108C3"
		self.do(gadget)

		#mov     rax, [rcx+8]
		#retn


  def test_gadget__ZNKSt8messagesIcE18_M_convert_to_charERKSs(self):
		#_ZNKSt8messagesIcE18_M_convert_to_charERKSs
		gadget = "488B02C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#retn


  def test_gadget__ZNKSt8messagesIcE20_M_convert_from_charEPc(self):
		#_ZNKSt8messagesIcE20_M_convert_from_charEPc
		gadget = "488D15712D07004889C8488911C3"
		self.do(gadget)

		#lea     rdx, dword_6FCEDE78
		#mov     rax, rcx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSt8messagesIcE7do_openERKSsRKSt6locale(self):
		#_ZNKSt8messagesIcE7do_openERKSsRKSt6locale
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt8messagesIcE8do_closeEi(self):
		#_ZNKSt8messagesIcE8do_closeEi
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNKSt8messagesIwE18_M_convert_to_charERKSbIwSt11char_traitsIwESaIwEE(self):
		#_ZNKSt8messagesIwE18_M_convert_to_charERKSbIwSt11char_traitsIwESaIwEE
		gadget = "488B02C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#retn


  def test_gadget__ZNKSt8messagesIwE20_M_convert_from_charEPc(self):
		#_ZNKSt8messagesIwE20_M_convert_from_charEPc
		gadget = "488D15912C07004889C8488911C3"
		self.do(gadget)

		#lea     rdx, unk_6FCEDE58
		#mov     rax, rcx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNKSt8messagesIwE7do_openERKSsRKSt6locale(self):
		#_ZNKSt8messagesIwE7do_openERKSsRKSt6locale
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt8messagesIwE8do_closeEi(self):
		#_ZNKSt8messagesIwE8do_closeEi
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNKSt8numpunctIcE16do_decimal_pointEv(self):
		#_ZNKSt8numpunctIcE16do_decimal_pointEv
		gadget = "488B41100FB64048C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, byte ptr [rax+48h]
		#retn


  def test_gadget__ZNKSt8numpunctIcE16do_thousands_sepEv(self):
		#_ZNKSt8numpunctIcE16do_thousands_sepEv
		gadget = "488B41100FB64049C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, byte ptr [rax+49h]
		#retn


  def test_gadget__ZNKSt8numpunctIwE16do_decimal_pointEv(self):
		#_ZNKSt8numpunctIwE16do_decimal_pointEv
		gadget = "488B41100FB74048C3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, word ptr [rax+48h]
		#retn


  def test_gadget__ZNKSt8numpunctIwE16do_thousands_sepEv(self):
		#_ZNKSt8numpunctIwE16do_thousands_sepEv
		gadget = "488B41100FB7404AC3"
		self.do(gadget)

		#mov     rax, [rcx+10h]
		#movzx   eax, word ptr [rax+4Ah]
		#retn


  def test_gadget__ZNKSt8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEE13do_date_orderEv(self):
		#_ZNKSt8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEE13do_date_orderEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEE13do_date_orderEv(self):
		#_ZNKSt8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEE13do_date_orderEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt8valarrayIyE4sizeEv(self):
		#_ZNKSt8valarrayIyE4sizeEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNKSt9bad_alloc4whatEv(self):
		#_ZNKSt9bad_alloc4whatEv
		gadget = "488D05396C0700C3"
		self.do(gadget)

		#lea     rax, aStdBad_alloc; "std::bad_alloc"
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE10exceptionsEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE10exceptionsEv
		gadget = "8B411CC3"
		self.do(gadget)

		#mov     eax, [rcx+1Ch]
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE3badEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE3badEv
		gadget = "8B412083E001C3"
		self.do(gadget)

		#mov     eax, [rcx+20h]
		#and     eax, 1
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE3eofEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE3eofEv
		gadget = "F64120020F95C0C3"
		self.do(gadget)

		#test    byte ptr [rcx+20h], 2
		#setnz   al
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE3tieEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE3tieEv
		gadget = "488B81D8000000C3"
		self.do(gadget)

		#mov     rax, [rcx+0D8h]
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv
		gadget = "F64120050F95C0C3"
		self.do(gadget)

		#test    byte ptr [rcx+20h], 5
		#setnz   al
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE4goodEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE4goodEv
		gadget = "8B412085C00F94C0C3"
		self.do(gadget)

		#mov     eax, [rcx+20h]
		#test    eax, eax
		#setz    al
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE5rdbufEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE5rdbufEv
		gadget = "488B81E8000000C3"
		self.do(gadget)

		#mov     rax, [rcx+0E8h]
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEE7rdstateEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEE7rdstateEv
		gadget = "8B4120C3"
		self.do(gadget)

		#mov     eax, [rcx+20h]
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEEcvPvEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEEcvPvEv
		gadget = "31C0F6412005480F44C1C3"
		self.do(gadget)

		#xor     eax, eax
		#test    byte ptr [rcx+20h], 5
		#cmovz   rax, rcx
		#retn


  def test_gadget__ZNKSt9basic_iosIcSt11char_traitsIcEEntEv(self):
		#_ZNKSt9basic_iosIcSt11char_traitsIcEEntEv
		gadget = "F64120050F95C0C3"
		self.do(gadget)

		#test    byte ptr [rcx+20h], 5
		#setnz   al
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE10exceptionsEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE10exceptionsEv
		gadget = "8B411CC3"
		self.do(gadget)

		#mov     eax, [rcx+1Ch]
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE3badEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE3badEv
		gadget = "8B412083E001C3"
		self.do(gadget)

		#mov     eax, [rcx+20h]
		#and     eax, 1
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE3eofEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE3eofEv
		gadget = "F64120020F95C0C3"
		self.do(gadget)

		#test    byte ptr [rcx+20h], 2
		#setnz   al
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE3tieEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE3tieEv
		gadget = "488B81D8000000C3"
		self.do(gadget)

		#mov     rax, [rcx+0D8h]
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE4failEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE4failEv
		gadget = "F64120050F95C0C3"
		self.do(gadget)

		#test    byte ptr [rcx+20h], 5
		#setnz   al
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE4goodEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE4goodEv
		gadget = "8B492085C90F94C0C3"
		self.do(gadget)

		#mov     ecx, [rcx+20h]
		#test    ecx, ecx
		#setz    al
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE5rdbufEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE5rdbufEv
		gadget = "488B81E8000000C3"
		self.do(gadget)

		#mov     rax, [rcx+0E8h]
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEE7rdstateEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEE7rdstateEv
		gadget = "8B4120C3"
		self.do(gadget)

		#mov     eax, [rcx+20h]
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEEcvPvEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEEcvPvEv
		gadget = "31C0F6412005480F44C1C3"
		self.do(gadget)

		#xor     eax, eax
		#test    byte ptr [rcx+20h], 5
		#cmovz   rax, rcx
		#retn


  def test_gadget__ZNKSt9basic_iosIwSt11char_traitsIwEEntEv(self):
		#_ZNKSt9basic_iosIwSt11char_traitsIwEEntEv
		gadget = "F64120050F95C0C3"
		self.do(gadget)

		#test    byte ptr [rcx+20h], 5
		#setnz   al
		#retn


  def test_gadget__ZNKSt9exception4whatEv(self):
		#_ZNKSt9exception4whatEv
		gadget = "488D0579690700C3"
		self.do(gadget)

		#lea     rax, aStdException; "std::exception"
		#retn


  def test_gadget__ZNKSt9strstream5rdbufEv(self):
		#_ZNKSt9strstream5rdbufEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNKSt9type_info11__do_upcastEPKN10__cxxabiv117__class_type_infoEPPv(self):
		#_ZNKSt9type_info11__do_upcastEPKN10__cxxabiv117__class_type_infoEPPv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt9type_info14__is_pointer_pEv(self):
		#_ZNKSt9type_info14__is_pointer_pEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNKSt9type_info15__is_function_pEv(self):
		#_ZNKSt9type_info15__is_function_pEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSaIcEC1ERKS_(self):
		#_ZNSaIcEC1ERKS_
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIcEC1Ev(self):
		#_ZNSaIcEC1Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIcEC2ERKS_(self):
		#_ZNSaIcEC2ERKS_
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIcEC2Ev(self):
		#_ZNSaIcEC2Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIcED1Ev(self):
		#_ZNSaIcED1Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIcED2Ev(self):
		#_ZNSaIcED2Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIwEC1ERKS_(self):
		#_ZNSaIwEC1ERKS_
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIwEC1Ev(self):
		#_ZNSaIwEC1Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIwEC2ERKS_(self):
		#_ZNSaIwEC2ERKS_
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIwEC2Ev(self):
		#_ZNSaIwEC2Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIwED1Ev(self):
		#_ZNSaIwED1Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSaIwED2Ev(self):
		#_ZNSaIwED2Ev
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE12_Alloc_hiderC1EPwRKS1_(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE12_Alloc_hiderC1EPwRKS1_
		gadget = "488911C3"
		self.do(gadget)

		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE12_Alloc_hiderC2EPwRKS1_(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE12_Alloc_hiderC2EPwRKS1_
		gadget = "488911C3"
		self.do(gadget)

		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE12_S_empty_repEv(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE12_S_empty_repEv
		gadget = "488D05E93D0600C3"
		self.do(gadget)

		#lea     rax, _ZNSbIwSt11char_traitsIwESaIwEE4_Rep20_S_empty_rep_storageE; std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t>>::_Rep::_S_empty_rep_storage
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE4_Rep10_M_refdataEv(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE4_Rep10_M_refdataEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE4_Rep12_S_empty_repEv(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE4_Rep12_S_empty_repEv
		gadget = "488D05093A0600C3"
		self.do(gadget)

		#lea     rax, _ZNSbIwSt11char_traitsIwESaIwEE4_Rep20_S_empty_rep_storageE; std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t>>::_Rep::_S_empty_rep_storage
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE4_Rep13_M_set_leakedEv(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE4_Rep13_M_set_leakedEv
		gadget = "C74110FFFFFFFFC3"
		self.do(gadget)

		#mov     dword ptr [rcx+10h], 0FFFFFFFFh
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE4_Rep15_M_set_sharableEv(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE4_Rep15_M_set_sharableEv
		gadget = "C7411000000000C3"
		self.do(gadget)

		#mov     dword ptr [rcx+10h], 0
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEE7_M_dataEPw(self):
		#_ZNSbIwSt11char_traitsIwESaIwEE7_M_dataEPw
		gadget = "4889D0488911C3"
		self.do(gadget)

		#mov     rax, rdx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEEC1EOS2_(self):
		#_ZNSbIwSt11char_traitsIwESaIwEEC1EOS2_
		gadget = "488B02488901488D05AB230600488902C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#lea     rax, unk_6FCEDE58
		#mov     [rdx], rax
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEEC1Ev(self):
		#_ZNSbIwSt11char_traitsIwESaIwEEC1Ev
		gadget = "488D05C1210600488901C3"
		self.do(gadget)

		#lea     rax, unk_6FCEDE58
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEEC2EOS2_(self):
		#_ZNSbIwSt11char_traitsIwESaIwEEC2EOS2_
		gadget = "488B02488901488D05FB200600488902C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#lea     rax, unk_6FCEDE58
		#mov     [rdx], rax
		#retn


  def test_gadget__ZNSbIwSt11char_traitsIwESaIwEEC2Ev(self):
		#_ZNSbIwSt11char_traitsIwESaIwEEC2Ev
		gadget = "488D05111F0600488901C3"
		self.do(gadget)

		#lea     rax, unk_6FCEDE58
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSdD2Ev(self):
		#_ZNSdD2Ev
		gadget = "488B02488901488B40E84C8B42284C890401488B423048894110488B421848894110488B40E84C8B42204C89440110488B4208488901488B40E8488B52104889140148C7410800000000C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     r8, [rdx+28h]
		#mov     [rcx+rax], r8
		#mov     rax, [rdx+30h]
		#mov     [rcx+10h], rax
		#mov     rax, [rdx+18h]
		#mov     [rcx+10h], rax
		#mov     rax, [rax-18h]
		#mov     r8, [rdx+20h]
		#mov     [rcx+rax+10h], r8
		#mov     rax, [rdx+8]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     rdx, [rdx+10h]
		#mov     [rcx+rax], rdx
		#mov     qword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSiD2Ev(self):
		#_ZNSiD2Ev
		gadget = "488B02488901488B40E8488B52084889140148C7410800000000C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     rdx, [rdx+8]
		#mov     [rcx+rax], rdx
		#mov     qword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSoD2Ev(self):
		#_ZNSoD2Ev
		gadget = "488B02488901488B40E8488B520848891401C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     rdx, [rdx+8]
		#mov     [rcx+rax], rdx
		#retn


  def test_gadget__ZNSs12_Alloc_hiderC1EPcRKSaIcE(self):
		#_ZNSs12_Alloc_hiderC1EPcRKSaIcE
		gadget = "488911C3"
		self.do(gadget)

		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNSs12_Alloc_hiderC2EPcRKSaIcE(self):
		#_ZNSs12_Alloc_hiderC2EPcRKSaIcE
		gadget = "488911C3"
		self.do(gadget)

		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNSs12_S_empty_repEv(self):
		#_ZNSs12_S_empty_repEv
		gadget = "488D05395F0500C3"
		self.do(gadget)

		#lea     rax, _ZNSs4_Rep20_S_empty_rep_storageE; std::string::_Rep::_S_empty_rep_storage
		#retn


  def test_gadget__ZNSs4_Rep10_M_refdataEv(self):
		#_ZNSs4_Rep10_M_refdataEv
		gadget = "488D4118C3"
		self.do(gadget)

		#lea     rax, [rcx+18h]
		#retn


  def test_gadget__ZNSs4_Rep12_S_empty_repEv(self):
		#_ZNSs4_Rep12_S_empty_repEv
		gadget = "488D05495B0500C3"
		self.do(gadget)

		#lea     rax, _ZNSs4_Rep20_S_empty_rep_storageE; std::string::_Rep::_S_empty_rep_storage
		#retn


  def test_gadget__ZNSs4_Rep13_M_set_leakedEv(self):
		#_ZNSs4_Rep13_M_set_leakedEv
		gadget = "C74110FFFFFFFFC3"
		self.do(gadget)

		#mov     dword ptr [rcx+10h], 0FFFFFFFFh
		#retn


  def test_gadget__ZNSs4_Rep15_M_set_sharableEv(self):
		#_ZNSs4_Rep15_M_set_sharableEv
		gadget = "C7411000000000C3"
		self.do(gadget)

		#mov     dword ptr [rcx+10h], 0
		#retn


  def test_gadget__ZNSs7_M_dataEPc(self):
		#_ZNSs7_M_dataEPc
		gadget = "4889D0488911C3"
		self.do(gadget)

		#mov     rax, rdx
		#mov     [rcx], rdx
		#retn


  def test_gadget__ZNSsC1EOSs(self):
		#_ZNSsC1EOSs
		gadget = "488B02488901488D052B460500488902C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#lea     rax, dword_6FCEDE78
		#mov     [rdx], rax
		#retn


  def test_gadget__ZNSsC1Ev(self):
		#_ZNSsC1Ev
		gadget = "488D0541440500488901C3"
		self.do(gadget)

		#lea     rax, dword_6FCEDE78
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSsC2EOSs(self):
		#_ZNSsC2EOSs
		gadget = "488B02488901488D057B430500488902C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#lea     rax, dword_6FCEDE78
		#mov     [rdx], rax
		#retn


  def test_gadget__ZNSsC2Ev(self):
		#_ZNSsC2Ev
		gadget = "488D0591410500488901C3"
		self.do(gadget)

		#lea     rax, dword_6FCEDE78
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt10money_base20_S_construct_patternEccc(self):
		#_ZNSt10money_base20_S_construct_patternEccc
		gadget = "8B050AE10500C3"
		self.do(gadget)

		#mov     eax, cs:_ZNSt10money_base18_S_default_patternE; std::money_base::_S_default_pattern
		#retn


  def test_gadget__ZNSt12__basic_fileIcE4fileEv(self):
		#_ZNSt12__basic_fileIcE4fileEv
		gadget = "488B01C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#retn


  def test_gadget__ZNSt12__basic_fileIcEC2EP17__gthread_mutex_t(self):
		#_ZNSt12__basic_fileIcEC2EP17__gthread_mutex_t
		gadget = "48C70100000000C6410800C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0; std::__basic_file<char>::__basic_file(__gthread_mutex_t *)
		#mov     byte ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt12strstreambuf6setbufEPcx(self):
		#_ZNSt12strstreambuf6setbufEPcx
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNSt13bad_exceptionD2Ev(self):
		#_ZNSt13bad_exceptionD2Ev
		gadget = "488D05592D0500488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF4250; std::bad_exception::~bad_exception()
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt13basic_istreamIwSt11char_traitsIwEED2Ev(self):
		#_ZNSt13basic_istreamIwSt11char_traitsIwEED2Ev
		gadget = "488B02488901488B40E8488B52084889140148C7410800000000C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     rdx, [rdx+8]
		#mov     [rcx+rax], rdx
		#mov     qword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt13basic_ostreamIwSt11char_traitsIwEED2Ev(self):
		#_ZNSt13basic_ostreamIwSt11char_traitsIwEED2Ev
		gadget = "488B02488901488B40E8488B520848891401C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     rdx, [rdx+8]
		#mov     [rcx+rax], rdx
		#retn


  def test_gadget__ZNSt14basic_iostreamIwSt11char_traitsIwEED2Ev(self):
		#_ZNSt14basic_iostreamIwSt11char_traitsIwEED2Ev
		gadget = "488B02488901488B40E84C8B42284C890401488B423048894110488B421848894110488B40E84C8B42204C89440110488B4208488901488B40E8488B52104889140148C7410800000000C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     r8, [rdx+28h]
		#mov     [rcx+rax], r8
		#mov     rax, [rdx+30h]
		#mov     [rcx+10h], rax
		#mov     rax, [rdx+18h]
		#mov     [rcx+10h], rax
		#mov     rax, [rax-18h]
		#mov     r8, [rdx+20h]
		#mov     [rcx+rax+10h], r8
		#mov     rax, [rdx+8]
		#mov     [rcx], rax
		#mov     rax, [rax-18h]
		#mov     rdx, [rdx+10h]
		#mov     [rcx+rax], rdx
		#mov     qword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt14error_categoryC2Ev(self):
		#_ZNSt14error_categoryC2Ev
		gadget = "488D05998D0300488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF2DD0; std::error_category::error_category(void)
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt14error_categoryD2Ev(self):
		#_ZNSt14error_categoryD2Ev
		gadget = "488D05798D0300488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF2DD0; std::error_category::~error_category()
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15_List_node_base4hookEPS_(self):
		#_ZNSt15_List_node_base4hookEPS_
		gadget = "488B420848891148894108488B420848894A08488908C3"
		self.do(gadget)

		#mov     rax, [rdx+8]
		#mov     [rcx], rdx
		#mov     [rcx+8], rax
		#mov     rax, [rdx+8]
		#mov     [rdx+8], rcx
		#mov     [rax], rcx
		#retn


  def test_gadget__ZNSt15_List_node_base6unhookEv(self):
		#_ZNSt15_List_node_base6unhookEv
		gadget = "488B01488B510848890248895008C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rcx+8]
		#mov     [rdx], rax
		#mov     [rax+8], rdx
		#retn


  def test_gadget__ZNSt15_List_node_base7_M_hookEPS_(self):
		#_ZNSt15_List_node_base7_M_hookEPS_
		gadget = "488B420848891148894108488B420848894A08488908C3"
		self.do(gadget)

		#mov     rax, [rdx+8]
		#mov     [rcx], rdx
		#mov     [rcx+8], rax
		#mov     rax, [rdx+8]
		#mov     [rdx+8], rcx
		#mov     [rax], rcx
		#retn


  def test_gadget__ZNSt15_List_node_base9_M_unhookEv(self):
		#_ZNSt15_List_node_base9_M_unhookEv
		gadget = "488B01488B510848890248895008C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rcx+8]
		#mov     [rdx], rax
		#mov     [rax+8], rdx
		#retn


  def test_gadget_nullsub_1(self):
		#nullsub_1
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSt15__exception_ptr13exception_ptr4swapERS0_(self):
		#_ZNSt15__exception_ptr13exception_ptr4swapERS0_
		gadget = "488B014C8B024C8901488902C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     r8, [rdx]
		#mov     [rcx], r8
		#mov     [rdx], rax
		#retn


  def test_gadget__ZNSt15__exception_ptr13exception_ptrC2EMS0_FvvE(self):
		#_ZNSt15__exception_ptr13exception_ptrC2EMS0_FvvE
		gadget = "48C70100000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0; std::__exception_ptr::exception_ptr::exception_ptr(void (std::__exception_ptr::exception_ptr::*)(void))
		#retn


  def test_gadget__ZNSt15__exception_ptr13exception_ptrC2Ev(self):
		#_ZNSt15__exception_ptr13exception_ptrC2Ev
		gadget = "48C70100000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0; std::__exception_ptr::exception_ptr::exception_ptr(void)
		#retn


  def test_gadget__ZNSt15__exception_ptreqERKNS_13exception_ptrES2_(self):
		#_ZNSt15__exception_ptreqERKNS_13exception_ptrES2_
		gadget = "488B024839010F94C0C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#cmp     [rcx], rax
		#setz    al
		#retn


  def test_gadget__ZNSt15__exception_ptrneERKNS_13exception_ptrES2_(self):
		#_ZNSt15__exception_ptrneERKNS_13exception_ptrES2_
		gadget = "488B024839010F95C0C3"
		self.do(gadget)

		#mov     rax, [rdx]
		#cmp     [rcx], rax
		#setnz   al
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE12__safe_gbumpEx(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE12__safe_gbumpEx
		gadget = "48015110C3"
		self.do(gadget)

		#add     [rcx+10h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE12__safe_pbumpEx(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE12__safe_pbumpEx
		gadget = "48015128C3"
		self.do(gadget)

		#add     [rcx+28h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE4setgEPcS3_S3_(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE4setgEPcS3_S3_
		gadget = "488951084C8941104C894918C3"
		self.do(gadget)

		#mov     [rcx+8], rdx
		#mov     [rcx+10h], r8
		#mov     [rcx+18h], r9
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE4setpEPcS3_(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE4setpEPcS3_
		gadget = "48895128488951204C894130C3"
		self.do(gadget)

		#mov     [rcx+28h], rdx
		#mov     [rcx+20h], rdx
		#mov     [rcx+30h], r8
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE4syncEv(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE4syncEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE5gbumpEi(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE5gbumpEi
		gadget = "4863D248015110C3"
		self.do(gadget)

		#movsxd  rdx, edx
		#add     [rcx+10h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE5imbueERKSt6locale(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE5imbueERKSt6locale
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE5pbumpEi(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE5pbumpEi
		gadget = "4863D248015128C3"
		self.do(gadget)

		#movsxd  rdx, edx
		#add     [rcx+28h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE6setbufEPcx(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE6setbufEPcx
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE7seekoffExSt12_Ios_SeekdirSt13_Ios_Openmode(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE7seekoffExSt12_Ios_SeekdirSt13_Ios_Openmode
		gadget = "4889C848C701FFFFFFFFC7410800000000C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     qword ptr [rcx], 0FFFFFFFFFFFFFFFFh
		#mov     dword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE7seekposESt4fposIiESt13_Ios_Openmode(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE7seekposESt4fposIiESt13_Ios_Openmode
		gadget = "4889C848C701FFFFFFFFC7410800000000C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     qword ptr [rcx], 0FFFFFFFFFFFFFFFFh
		#mov     dword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE8overflowEi(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE8overflowEi
		gadget = "B8FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE9pbackfailEi(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE9pbackfailEi
		gadget = "B8FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE9showmanycEv(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE9showmanycEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEE9underflowEv(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEE9underflowEv
		gadget = "B8FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#retn


  def test_gadget__ZNSt15basic_streambufIcSt11char_traitsIcEEaSERKS2_(self):
		#_ZNSt15basic_streambufIcSt11char_traitsIcEEaSERKS2_
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE12__safe_gbumpEx(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE12__safe_gbumpEx
		gadget = "4801D248015110C3"
		self.do(gadget)

		#add     rdx, rdx
		#add     [rcx+10h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE12__safe_pbumpEx(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE12__safe_pbumpEx
		gadget = "4801D248015128C3"
		self.do(gadget)

		#add     rdx, rdx
		#add     [rcx+28h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE4setgEPwS3_S3_(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE4setgEPwS3_S3_
		gadget = "488951084C8941104C894918C3"
		self.do(gadget)

		#mov     [rcx+8], rdx
		#mov     [rcx+10h], r8
		#mov     [rcx+18h], r9
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE4setpEPwS3_(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE4setpEPwS3_
		gadget = "48895128488951204C894130C3"
		self.do(gadget)

		#mov     [rcx+28h], rdx
		#mov     [rcx+20h], rdx
		#mov     [rcx+30h], r8
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE4syncEv(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE4syncEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE5gbumpEi(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE5gbumpEi
		gadget = "4863D24801D248015110C3"
		self.do(gadget)

		#movsxd  rdx, edx
		#add     rdx, rdx
		#add     [rcx+10h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE5imbueERKSt6locale(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE5imbueERKSt6locale
		gadget = "C3"
		self.do(gadget)

		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE5pbumpEi(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE5pbumpEi
		gadget = "4863D24801D248015128C3"
		self.do(gadget)

		#movsxd  rdx, edx
		#add     rdx, rdx
		#add     [rcx+28h], rdx
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE6setbufEPwx(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE6setbufEPwx
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE7seekoffExSt12_Ios_SeekdirSt13_Ios_Openmode(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE7seekoffExSt12_Ios_SeekdirSt13_Ios_Openmode
		gadget = "4889C848C701FFFFFFFFC7410800000000C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     qword ptr [rcx], 0FFFFFFFFFFFFFFFFh
		#mov     dword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE7seekposESt4fposIiESt13_Ios_Openmode(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE7seekposESt4fposIiESt13_Ios_Openmode
		gadget = "4889C848C701FFFFFFFFC7410800000000C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     qword ptr [rcx], 0FFFFFFFFFFFFFFFFh
		#mov     dword ptr [rcx+8], 0
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE8overflowEt(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE8overflowEt
		gadget = "B8FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE9pbackfailEt(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE9pbackfailEt
		gadget = "B8FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE9showmanycEv(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE9showmanycEv
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEE9underflowEv(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEE9underflowEv
		gadget = "B8FFFFFFFFC3"
		self.do(gadget)

		#mov     eax, 0FFFFFFFFh
		#retn


  def test_gadget__ZNSt15basic_streambufIwSt11char_traitsIwEEaSERKS2_(self):
		#_ZNSt15basic_streambufIwSt11char_traitsIwEEaSERKS2_
		gadget = "4889C8C3"
		self.do(gadget)

		#mov     rax, rcx
		#retn


  def test_gadget__ZNSt15time_get_bynameIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1EPKcy(self):
		#_ZNSt15time_get_bynameIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1EPKcy
		gadget = "31C04D85C00F95C0894108488D054E570300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF31B0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_get_bynameIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2EPKcy(self):
		#_ZNSt15time_get_bynameIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2EPKcy
		gadget = "31C04D85C00F95C0894108488D052E570300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF31B0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_get_bynameIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1EPKcy(self):
		#_ZNSt15time_get_bynameIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1EPKcy
		gadget = "31C04D85C00F95C0894108488D051E570300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3210
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_get_bynameIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2EPKcy(self):
		#_ZNSt15time_get_bynameIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2EPKcy
		gadget = "31C04D85C00F95C0894108488D05FE560300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3210
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_put_bynameIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1EPKcy(self):
		#_ZNSt15time_put_bynameIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1EPKcy
		gadget = "31C04D85C00F95C0894108488D05EE560300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3270
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_put_bynameIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2EPKcy(self):
		#_ZNSt15time_put_bynameIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2EPKcy
		gadget = "31C04D85C00F95C0894108488D05CE560300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3270
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_put_bynameIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1EPKcy(self):
		#_ZNSt15time_put_bynameIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1EPKcy
		gadget = "31C04D85C00F95C0894108488D059E560300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF32B0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt15time_put_bynameIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2EPKcy(self):
		#_ZNSt15time_put_bynameIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2EPKcy
		gadget = "31C04D85C00F95C0894108488D057E560300488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    r8, r8
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF32B0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt16__numpunct_cacheIcEC1Ey(self):
		#_ZNSt16__numpunct_cacheIcEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200048C7412800000000894108488D05A24F030048C741300000000048C741380000000048C7414000000000488901C6414800C6414900C6818800000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3330
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     byte ptr [rcx+48h], 0
		#mov     byte ptr [rcx+49h], 0
		#mov     byte ptr [rcx+88h], 0
		#retn


  def test_gadget__ZNSt16__numpunct_cacheIcEC2Ey(self):
		#_ZNSt16__numpunct_cacheIcEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200048C7412800000000894108488D05424F030048C741300000000048C741380000000048C7414000000000488901C6414800C6414900C6818800000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3330
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     byte ptr [rcx+48h], 0
		#mov     byte ptr [rcx+49h], 0
		#mov     byte ptr [rcx+88h], 0
		#retn


  def test_gadget__ZNSt16__numpunct_cacheIwEC1Ey(self):
		#_ZNSt16__numpunct_cacheIwEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200048C7412800000000894108488D051247030048C741300000000048C741380000000048C741400000000048890166C74148000066C7414A0000C681C800000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3350
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     word ptr [rcx+48h], 0
		#mov     word ptr [rcx+4Ah], 0
		#mov     byte ptr [rcx+0C8h], 0
		#retn


  def test_gadget__ZNSt16__numpunct_cacheIwEC2Ey(self):
		#_ZNSt16__numpunct_cacheIwEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200048C7412800000000894108488D05B246030048C741300000000048C741380000000048C741400000000048890166C74148000066C7414A0000C681C800000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3350
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     word ptr [rcx+48h], 0
		#mov     word ptr [rcx+4Ah], 0
		#mov     byte ptr [rcx+0C8h], 0
		#retn


  def test_gadget__ZNSt17__timepunct_cacheIcEC1Ey(self):
		#_ZNSt17__timepunct_cacheIcEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C048C741200000000048C7412800000000894108488D054E45030048C741300000000048C741380000000048C741400000000048890148C741480000000048C741500000000048C741580000000048C741600000000048C741680000000048C741700000000048C741780000000048C781800000000000000048C781880000000000000048C781900000000000000048C781980000000000000048C781A00000000000000048C781A80000000000000048C781B00000000000000048C781B80000000000000048C781C00000000000000048C781C80000000000000048C781D00000000000000048C781D80000000000000048C781E00000000000000048C781E80000000000000048C781F00000000000000048C781F80000000000000048C781000100000000000048C781080100000000000048C781100100000000000048C781180100000000000048C781200100000000000048C781280100000000000048C781300100000000000048C781380100000000000048C781400100000000000048C781480100000000000048C781500100000000000048C781580100000000000048C781600100000000000048C781680100000000000048C781700100000000000048C781780100000000000048C7818001000000000000C6818801000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     qword ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF33D0
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     qword ptr [rcx+58h], 0
		#mov     qword ptr [rcx+60h], 0
		#mov     qword ptr [rcx+68h], 0
		#mov     qword ptr [rcx+70h], 0
		#mov     qword ptr [rcx+78h], 0
		#mov     qword ptr [rcx+80h], 0
		#mov     qword ptr [rcx+88h], 0
		#mov     qword ptr [rcx+90h], 0
		#mov     qword ptr [rcx+98h], 0
		#mov     qword ptr [rcx+0A0h], 0
		#mov     qword ptr [rcx+0A8h], 0
		#mov     qword ptr [rcx+0B0h], 0
		#mov     qword ptr [rcx+0B8h], 0
		#mov     qword ptr [rcx+0C0h], 0
		#mov     qword ptr [rcx+0C8h], 0
		#mov     qword ptr [rcx+0D0h], 0
		#mov     qword ptr [rcx+0D8h], 0
		#mov     qword ptr [rcx+0E0h], 0
		#mov     qword ptr [rcx+0E8h], 0
		#mov     qword ptr [rcx+0F0h], 0
		#mov     qword ptr [rcx+0F8h], 0
		#mov     qword ptr [rcx+100h], 0
		#mov     qword ptr [rcx+108h], 0
		#mov     qword ptr [rcx+110h], 0
		#mov     qword ptr [rcx+118h], 0
		#mov     qword ptr [rcx+120h], 0
		#mov     qword ptr [rcx+128h], 0
		#mov     qword ptr [rcx+130h], 0
		#mov     qword ptr [rcx+138h], 0
		#mov     qword ptr [rcx+140h], 0
		#mov     qword ptr [rcx+148h], 0
		#mov     qword ptr [rcx+150h], 0
		#mov     qword ptr [rcx+158h], 0
		#mov     qword ptr [rcx+160h], 0
		#mov     qword ptr [rcx+168h], 0
		#mov     qword ptr [rcx+170h], 0
		#mov     qword ptr [rcx+178h], 0
		#mov     qword ptr [rcx+180h], 0
		#mov     byte ptr [rcx+188h], 0
		#retn


  def test_gadget__ZNSt17__timepunct_cacheIcEC2Ey(self):
		#_ZNSt17__timepunct_cacheIcEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C048C741200000000048C7412800000000894108488D054E43030048C741300000000048C741380000000048C741400000000048890148C741480000000048C741500000000048C741580000000048C741600000000048C741680000000048C741700000000048C741780000000048C781800000000000000048C781880000000000000048C781900000000000000048C781980000000000000048C781A00000000000000048C781A80000000000000048C781B00000000000000048C781B80000000000000048C781C00000000000000048C781C80000000000000048C781D00000000000000048C781D80000000000000048C781E00000000000000048C781E80000000000000048C781F00000000000000048C781F80000000000000048C781000100000000000048C781080100000000000048C781100100000000000048C781180100000000000048C781200100000000000048C781280100000000000048C781300100000000000048C781380100000000000048C781400100000000000048C781480100000000000048C781500100000000000048C781580100000000000048C781600100000000000048C781680100000000000048C781700100000000000048C781780100000000000048C7818001000000000000C6818801000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     qword ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF33D0
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     qword ptr [rcx+58h], 0
		#mov     qword ptr [rcx+60h], 0
		#mov     qword ptr [rcx+68h], 0
		#mov     qword ptr [rcx+70h], 0
		#mov     qword ptr [rcx+78h], 0
		#mov     qword ptr [rcx+80h], 0
		#mov     qword ptr [rcx+88h], 0
		#mov     qword ptr [rcx+90h], 0
		#mov     qword ptr [rcx+98h], 0
		#mov     qword ptr [rcx+0A0h], 0
		#mov     qword ptr [rcx+0A8h], 0
		#mov     qword ptr [rcx+0B0h], 0
		#mov     qword ptr [rcx+0B8h], 0
		#mov     qword ptr [rcx+0C0h], 0
		#mov     qword ptr [rcx+0C8h], 0
		#mov     qword ptr [rcx+0D0h], 0
		#mov     qword ptr [rcx+0D8h], 0
		#mov     qword ptr [rcx+0E0h], 0
		#mov     qword ptr [rcx+0E8h], 0
		#mov     qword ptr [rcx+0F0h], 0
		#mov     qword ptr [rcx+0F8h], 0
		#mov     qword ptr [rcx+100h], 0
		#mov     qword ptr [rcx+108h], 0
		#mov     qword ptr [rcx+110h], 0
		#mov     qword ptr [rcx+118h], 0
		#mov     qword ptr [rcx+120h], 0
		#mov     qword ptr [rcx+128h], 0
		#mov     qword ptr [rcx+130h], 0
		#mov     qword ptr [rcx+138h], 0
		#mov     qword ptr [rcx+140h], 0
		#mov     qword ptr [rcx+148h], 0
		#mov     qword ptr [rcx+150h], 0
		#mov     qword ptr [rcx+158h], 0
		#mov     qword ptr [rcx+160h], 0
		#mov     qword ptr [rcx+168h], 0
		#mov     qword ptr [rcx+170h], 0
		#mov     qword ptr [rcx+178h], 0
		#mov     qword ptr [rcx+180h], 0
		#mov     byte ptr [rcx+188h], 0
		#retn


  def test_gadget__ZNSt17__timepunct_cacheIwEC1Ey(self):
		#_ZNSt17__timepunct_cacheIwEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C048C741200000000048C7412800000000894108488D051E41030048C741300000000048C741380000000048C741400000000048890148C741480000000048C741500000000048C741580000000048C741600000000048C741680000000048C741700000000048C741780000000048C781800000000000000048C781880000000000000048C781900000000000000048C781980000000000000048C781A00000000000000048C781A80000000000000048C781B00000000000000048C781B80000000000000048C781C00000000000000048C781C80000000000000048C781D00000000000000048C781D80000000000000048C781E00000000000000048C781E80000000000000048C781F00000000000000048C781F80000000000000048C781000100000000000048C781080100000000000048C781100100000000000048C781180100000000000048C781200100000000000048C781280100000000000048C781300100000000000048C781380100000000000048C781400100000000000048C781480100000000000048C781500100000000000048C781580100000000000048C781600100000000000048C781680100000000000048C781700100000000000048C781780100000000000048C7818001000000000000C6818801000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     qword ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF33F0
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     qword ptr [rcx+58h], 0
		#mov     qword ptr [rcx+60h], 0
		#mov     qword ptr [rcx+68h], 0
		#mov     qword ptr [rcx+70h], 0
		#mov     qword ptr [rcx+78h], 0
		#mov     qword ptr [rcx+80h], 0
		#mov     qword ptr [rcx+88h], 0
		#mov     qword ptr [rcx+90h], 0
		#mov     qword ptr [rcx+98h], 0
		#mov     qword ptr [rcx+0A0h], 0
		#mov     qword ptr [rcx+0A8h], 0
		#mov     qword ptr [rcx+0B0h], 0
		#mov     qword ptr [rcx+0B8h], 0
		#mov     qword ptr [rcx+0C0h], 0
		#mov     qword ptr [rcx+0C8h], 0
		#mov     qword ptr [rcx+0D0h], 0
		#mov     qword ptr [rcx+0D8h], 0
		#mov     qword ptr [rcx+0E0h], 0
		#mov     qword ptr [rcx+0E8h], 0
		#mov     qword ptr [rcx+0F0h], 0
		#mov     qword ptr [rcx+0F8h], 0
		#mov     qword ptr [rcx+100h], 0
		#mov     qword ptr [rcx+108h], 0
		#mov     qword ptr [rcx+110h], 0
		#mov     qword ptr [rcx+118h], 0
		#mov     qword ptr [rcx+120h], 0
		#mov     qword ptr [rcx+128h], 0
		#mov     qword ptr [rcx+130h], 0
		#mov     qword ptr [rcx+138h], 0
		#mov     qword ptr [rcx+140h], 0
		#mov     qword ptr [rcx+148h], 0
		#mov     qword ptr [rcx+150h], 0
		#mov     qword ptr [rcx+158h], 0
		#mov     qword ptr [rcx+160h], 0
		#mov     qword ptr [rcx+168h], 0
		#mov     qword ptr [rcx+170h], 0
		#mov     qword ptr [rcx+178h], 0
		#mov     qword ptr [rcx+180h], 0
		#mov     byte ptr [rcx+188h], 0
		#retn


  def test_gadget__ZNSt17__timepunct_cacheIwEC2Ey(self):
		#_ZNSt17__timepunct_cacheIwEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C048C741200000000048C7412800000000894108488D051E3F030048C741300000000048C741380000000048C741400000000048890148C741480000000048C741500000000048C741580000000048C741600000000048C741680000000048C741700000000048C741780000000048C781800000000000000048C781880000000000000048C781900000000000000048C781980000000000000048C781A00000000000000048C781A80000000000000048C781B00000000000000048C781B80000000000000048C781C00000000000000048C781C80000000000000048C781D00000000000000048C781D80000000000000048C781E00000000000000048C781E80000000000000048C781F00000000000000048C781F80000000000000048C781000100000000000048C781080100000000000048C781100100000000000048C781180100000000000048C781200100000000000048C781280100000000000048C781300100000000000048C781380100000000000048C781400100000000000048C781480100000000000048C781500100000000000048C781580100000000000048C781600100000000000048C781680100000000000048C781700100000000000048C781780100000000000048C7818001000000000000C6818801000000C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     qword ptr [rcx+20h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF33F0
		#mov     qword ptr [rcx+30h], 0
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     qword ptr [rcx+58h], 0
		#mov     qword ptr [rcx+60h], 0
		#mov     qword ptr [rcx+68h], 0
		#mov     qword ptr [rcx+70h], 0
		#mov     qword ptr [rcx+78h], 0
		#mov     qword ptr [rcx+80h], 0
		#mov     qword ptr [rcx+88h], 0
		#mov     qword ptr [rcx+90h], 0
		#mov     qword ptr [rcx+98h], 0
		#mov     qword ptr [rcx+0A0h], 0
		#mov     qword ptr [rcx+0A8h], 0
		#mov     qword ptr [rcx+0B0h], 0
		#mov     qword ptr [rcx+0B8h], 0
		#mov     qword ptr [rcx+0C0h], 0
		#mov     qword ptr [rcx+0C8h], 0
		#mov     qword ptr [rcx+0D0h], 0
		#mov     qword ptr [rcx+0D8h], 0
		#mov     qword ptr [rcx+0E0h], 0
		#mov     qword ptr [rcx+0E8h], 0
		#mov     qword ptr [rcx+0F0h], 0
		#mov     qword ptr [rcx+0F8h], 0
		#mov     qword ptr [rcx+100h], 0
		#mov     qword ptr [rcx+108h], 0
		#mov     qword ptr [rcx+110h], 0
		#mov     qword ptr [rcx+118h], 0
		#mov     qword ptr [rcx+120h], 0
		#mov     qword ptr [rcx+128h], 0
		#mov     qword ptr [rcx+130h], 0
		#mov     qword ptr [rcx+138h], 0
		#mov     qword ptr [rcx+140h], 0
		#mov     qword ptr [rcx+148h], 0
		#mov     qword ptr [rcx+150h], 0
		#mov     qword ptr [rcx+158h], 0
		#mov     qword ptr [rcx+160h], 0
		#mov     qword ptr [rcx+168h], 0
		#mov     qword ptr [rcx+170h], 0
		#mov     qword ptr [rcx+178h], 0
		#mov     qword ptr [rcx+180h], 0
		#mov     byte ptr [rcx+188h], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIcLb0EEC1Ey(self):
		#_ZNSt18__moneypunct_cacheIcLb0EEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C6412000C6412100894108488D0576280300C641220048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6416F00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     byte ptr [rcx+21h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3650
		#mov     byte ptr [rcx+22h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+6Fh], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIcLb0EEC2Ey(self):
		#_ZNSt18__moneypunct_cacheIcLb0EEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C6412000C6412100894108488D05E6270300C641220048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6416F00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     byte ptr [rcx+21h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3650
		#mov     byte ptr [rcx+22h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+6Fh], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIcLb1EEC1Ey(self):
		#_ZNSt18__moneypunct_cacheIcLb1EEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C6412000C6412100894108488D05561F0300C641220048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6416F00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     byte ptr [rcx+21h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3670
		#mov     byte ptr [rcx+22h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+6Fh], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIcLb1EEC2Ey(self):
		#_ZNSt18__moneypunct_cacheIcLb1EEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C6412000C6412100894108488D05C61E0300C641220048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6416F00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     byte ptr [rcx+21h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3670
		#mov     byte ptr [rcx+22h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+6Fh], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIwLb0EEC1Ey(self):
		#_ZNSt18__moneypunct_cacheIwLb0EEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200066C741220000894108488D057414030066C74124000048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6417A00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     word ptr [rcx+22h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3690
		#mov     word ptr [rcx+24h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+7Ah], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIwLb0EEC2Ey(self):
		#_ZNSt18__moneypunct_cacheIwLb0EEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200066C741220000894108488D05D413030066C74124000048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6417A00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     word ptr [rcx+22h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3690
		#mov     word ptr [rcx+24h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+7Ah], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIwLb1EEC1Ey(self):
		#_ZNSt18__moneypunct_cacheIwLb1EEC1Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200066C741220000894108488D057409030066C74124000048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6417A00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     word ptr [rcx+22h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF36B0
		#mov     word ptr [rcx+24h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+7Ah], 0
		#retn


  def test_gadget__ZNSt18__moneypunct_cacheIwLb1EEC2Ey(self):
		#_ZNSt18__moneypunct_cacheIwLb1EEC2Ey
		gadget = "31C04885D248C741100000000048C74118000000000F95C0C641200066C741220000894108488D05D408030066C74124000048C741280000000048C741300000000048890148C741380000000048C741400000000048C741480000000048C7415000000000C7415800000000C6415C00C6415D00C6415E00C6415F00C6416000C6416100C6416200C6416300C6417A00C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#mov     qword ptr [rcx+10h], 0
		#mov     qword ptr [rcx+18h], 0
		#setnz   al
		#mov     byte ptr [rcx+20h], 0
		#mov     word ptr [rcx+22h], 0
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF36B0
		#mov     word ptr [rcx+24h], 0
		#mov     qword ptr [rcx+28h], 0
		#mov     qword ptr [rcx+30h], 0
		#mov     [rcx], rax
		#mov     qword ptr [rcx+38h], 0
		#mov     qword ptr [rcx+40h], 0
		#mov     qword ptr [rcx+48h], 0
		#mov     qword ptr [rcx+50h], 0
		#mov     dword ptr [rcx+58h], 0
		#mov     byte ptr [rcx+5Ch], 0
		#mov     byte ptr [rcx+5Dh], 0
		#mov     byte ptr [rcx+5Eh], 0
		#mov     byte ptr [rcx+5Fh], 0
		#mov     byte ptr [rcx+60h], 0
		#mov     byte ptr [rcx+61h], 0
		#mov     byte ptr [rcx+62h], 0
		#mov     byte ptr [rcx+63h], 0
		#mov     byte ptr [rcx+7Ah], 0
		#retn


  def test_gadget__ZNSt5ctypeIcE13classic_tableEv(self):
		#_ZNSt5ctypeIcE13classic_tableEv
		gadget = "488D0599580300C3"
		self.do(gadget)

		#lea     rax, unk_6FCFD7A0
		#retn


  def test_gadget__ZNSt6__norm15_List_node_base4hookEPS0_(self):
		#_ZNSt6__norm15_List_node_base4hookEPS0_
		gadget = "488B420848891148894108488B420848894A08488908C3"
		self.do(gadget)

		#mov     rax, [rdx+8]
		#mov     [rcx], rdx
		#mov     [rcx+8], rax
		#mov     rax, [rdx+8]
		#mov     [rdx+8], rcx
		#mov     [rax], rcx
		#retn


  def test_gadget__ZNSt6__norm15_List_node_base6unhookEv(self):
		#_ZNSt6__norm15_List_node_base6unhookEv
		gadget = "488B01488B510848890248895008C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rcx+8]
		#mov     [rdx], rax
		#mov     [rax+8], rdx
		#retn


  def test_gadget__ZNSt6__norm15_List_node_base7_M_hookEPS0_(self):
		#_ZNSt6__norm15_List_node_base7_M_hookEPS0_
		gadget = "488B420848891148894108488B420848894A08488908C3"
		self.do(gadget)

		#mov     rax, [rdx+8]
		#mov     [rcx], rdx
		#mov     [rcx+8], rax
		#mov     rax, [rdx+8]
		#mov     [rdx+8], rcx
		#mov     [rax], rcx
		#retn


  def test_gadget__ZNSt6__norm15_List_node_base9_M_unhookEv(self):
		#_ZNSt6__norm15_List_node_base9_M_unhookEv
		gadget = "488B01488B510848890248895008C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rcx+8]
		#mov     [rdx], rax
		#mov     [rax+8], rdx
		#retn


  def test_gadget__ZNSt6locale5facet13_S_get_c_nameEv(self):
		#_ZNSt6locale5facet13_S_get_c_nameEv
		gadget = "488D05F9F00200C3"
		self.do(gadget)

		#lea     rax, qword_6FCFB440
		#retn


  def test_gadget__ZNSt6locale5facet17_S_clone_c_localeERPi(self):
		#_ZNSt6locale5facet17_S_clone_c_localeERPi
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSt6locale5facet19_S_destroy_c_localeERPi(self):
		#_ZNSt6locale5facet19_S_destroy_c_localeERPi
		gadget = "48C70100000000C3"
		self.do(gadget)

		#mov     qword ptr [rcx], 0
		#retn


  def test_gadget_sub_6FCCC400(self):
		#sub_6FCCC400
		gadget = "31C0C3"
		self.do(gadget)

		#xor     eax, eax
		#retn


  def test_gadget__ZNSt6locale5facetD2Ev(self):
		#_ZNSt6locale5facetD2Ev
		gadget = "488D05A95A0200488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF1ED0; std::locale::facet::~facet()
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt6localeC2EPNS_5_ImplE(self):
		#_ZNSt6localeC2EPNS_5_ImplE
		gadget = "488911C3"
		self.do(gadget)

		#mov     [rcx], rdx      ; std::locale::locale(std::locale::_Impl *)
		#retn


  def test_gadget__ZNSt7num_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1Ey(self):
		#_ZNSt7num_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1Ey
		gadget = "31C04885D20F95C0894108488D051E550200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3D30
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2Ey(self):
		#_ZNSt7num_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2Ey
		gadget = "31C04885D20F95C0894108488D05FE540200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3D30
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1Ey(self):
		#_ZNSt7num_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1Ey
		gadget = "31C04885D20F95C0894108488D050E550200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3DB0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2Ey(self):
		#_ZNSt7num_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2Ey
		gadget = "31C04885D20F95C0894108488D05EE540200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3DB0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1Ey(self):
		#_ZNSt7num_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1Ey
		gadget = "31C04885D20F95C0894108488D05FE540200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3E30
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2Ey(self):
		#_ZNSt7num_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2Ey
		gadget = "31C04885D20F95C0894108488D05DE540200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3E30
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1Ey(self):
		#_ZNSt7num_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1Ey
		gadget = "31C04885D20F95C0894108488D05CE540200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3E90
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt7num_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2Ey(self):
		#_ZNSt7num_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2Ey
		gadget = "31C04885D20F95C0894108488D05AE540200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF3E90
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8__detail15_List_node_base7_M_hookEPS0_(self):
		#_ZNSt8__detail15_List_node_base7_M_hookEPS0_
		gadget = "488B420848891148894108488B420848894A08488908C3"
		self.do(gadget)

		#mov     rax, [rdx+8]
		#mov     [rcx], rdx
		#mov     [rcx+8], rax
		#mov     rax, [rdx+8]
		#mov     [rdx+8], rcx
		#mov     [rax], rcx
		#retn


  def test_gadget__ZNSt8__detail15_List_node_base9_M_unhookEv(self):
		#_ZNSt8__detail15_List_node_base9_M_unhookEv
		gadget = "488B01488B510848890248895008C3"
		self.do(gadget)

		#mov     rax, [rcx]
		#mov     rdx, [rcx+8]
		#mov     [rdx], rax
		#mov     [rax+8], rdx
		#retn


  def test_gadget__ZNSt8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1Ey(self):
		#_ZNSt8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1Ey
		gadget = "31C04885D20F95C0894108488D05DE200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4090
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2Ey(self):
		#_ZNSt8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2Ey
		gadget = "31C04885D20F95C0894108488D05BE200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4090
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1Ey(self):
		#_ZNSt8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1Ey
		gadget = "31C04885D20F95C0894108488D05AE200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF40F0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2Ey(self):
		#_ZNSt8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2Ey
		gadget = "31C04885D20F95C0894108488D058E200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF40F0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1Ey(self):
		#_ZNSt8time_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1Ey
		gadget = "31C04885D20F95C0894108488D057E200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4150
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2Ey(self):
		#_ZNSt8time_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2Ey
		gadget = "31C04885D20F95C0894108488D055E200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4150
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1Ey(self):
		#_ZNSt8time_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1Ey
		gadget = "31C04885D20F95C0894108488D052E200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4190
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8time_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2Ey(self):
		#_ZNSt8time_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2Ey
		gadget = "31C04885D20F95C0894108488D050E200200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4190
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt8valarrayIyEixEy(self):
		#_ZNSt8valarrayIyEixEy
		gadget = "488D04D50000000048034108C3"
		self.do(gadget)

		#lea     rax, ds:0[rdx*8]
		#add     rax, [rcx+8]
		#retn


  def test_gadget__ZNSt9__atomic011atomic_flag12test_and_setESt12memory_order(self):
		#_ZNSt9__atomic011atomic_flag12test_and_setESt12memory_order
		gadget = "0FB601C60101C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx]
		#mov     byte ptr [rcx], 1
		#retn


  def test_gadget__ZNSt9__atomic011atomic_flag5clearESt12memory_order(self):
		#_ZNSt9__atomic011atomic_flag5clearESt12memory_order
		gadget = "C60100C3"
		self.do(gadget)

		#mov     byte ptr [rcx], 0
		#retn


  def test_gadget__ZNSt9basic_iosIcSt11char_traitsIcEE3tieEPSo(self):
		#_ZNSt9basic_iosIcSt11char_traitsIcEE3tieEPSo
		gadget = "488B81D8000000488991D8000000C3"
		self.do(gadget)

		#mov     rax, [rcx+0D8h]
		#mov     [rcx+0D8h], rdx
		#retn


  def test_gadget__ZNSt9basic_iosIwSt11char_traitsIwEE3tieEPSt13basic_ostreamIwS1_E(self):
		#_ZNSt9basic_iosIwSt11char_traitsIwEE3tieEPSt13basic_ostreamIwS1_E
		gadget = "488B81D8000000488991D8000000C3"
		self.do(gadget)

		#mov     rax, [rcx+0D8h]
		#mov     [rcx+0D8h], rdx
		#retn


  def test_gadget__ZNSt9exceptionD2Ev(self):
		#_ZNSt9exceptionD2Ev
		gadget = "488D05590B0200488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF4250; std::exception::~exception()
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1Ey(self):
		#_ZNSt9money_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC1Ey
		gadget = "31C04885D20F95C0894108488D057E0B0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4290
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2Ey(self):
		#_ZNSt9money_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEC2Ey
		gadget = "31C04885D20F95C0894108488D055E0B0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4290
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1Ey(self):
		#_ZNSt9money_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC1Ey
		gadget = "31C04885D20F95C0894108488D052E0B0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF42D0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2Ey(self):
		#_ZNSt9money_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEC2Ey
		gadget = "31C04885D20F95C0894108488D050E0B0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF42D0
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1Ey(self):
		#_ZNSt9money_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC1Ey
		gadget = "31C04885D20F95C0894108488D05DE0A0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4310
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2Ey(self):
		#_ZNSt9money_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEC2Ey
		gadget = "31C04885D20F95C0894108488D05BE0A0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4310
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1Ey(self):
		#_ZNSt9money_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC1Ey
		gadget = "31C04885D20F95C0894108488D058E0A0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4350
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9money_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2Ey(self):
		#_ZNSt9money_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEC2Ey
		gadget = "31C04885D20F95C0894108488D056E0A0200488901C3"
		self.do(gadget)

		#xor     eax, eax
		#test    rdx, rdx
		#setnz   al
		#mov     [rcx+8], eax
		#lea     rax, off_6FCF4350
		#mov     [rcx], rax
		#retn


  def test_gadget__ZNSt9type_infoD2Ev(self):
		#_ZNSt9type_infoD2Ev
		gadget = "488D05A9FD0100488901C3"
		self.do(gadget)

		#lea     rax, off_6FCF4410; std::type_info::~type_info()
		#mov     [rcx], rax
		#retn


  def test_gadget__ZSt13set_terminatePFvvE(self):
		#_ZSt13set_terminatePFvvE
		gadget = "488B052977010048890D22770100C3"
		self.do(gadget)

		#mov     rax, cs:off_6FCEC130
		#mov     cs:off_6FCEC130, rcx
		#retn


  def test_gadget__ZSt14set_unexpectedPFvvE(self):
		#_ZSt14set_unexpectedPFvvE
		gadget = "488B05D96E010048890DD26E0100C3"
		self.do(gadget)

		#mov     rax, cs:off_6FCEC140
		#mov     cs:off_6FCEC140, rcx
		#retn


  def test_gadget__ZSt15set_new_handlerPFvvE(self):
		#_ZSt15set_new_handlerPFvvE
		gadget = "488B0539F3010048890D32F30100C3"
		self.do(gadget)

		#mov     rax, cs:qword_6FCF4710
		#mov     cs:qword_6FCF4710, rcx
		#retn


  def test_gadget__ZSt15system_categoryv(self):
		#_ZSt15system_categoryv
		gadget = "488D0589800100C3"
		self.do(gadget)

		#lea     rax, qword_6FCED470
		#retn


  def test_gadget__ZSt16generic_categoryv(self):
		#_ZSt16generic_categoryv
		gadget = "488D05E9700100C3"
		self.do(gadget)

		#lea     rax, qword_6FCED480
		#retn


  def test_gadget_sub_6FCD8E40(self):
		#sub_6FCD8E40
		gadget = "89C8C3"
		self.do(gadget)

		#mov     eax, ecx
		#retn


  def test_gadget_sub_6FCD8E50(self):
		#sub_6FCD8E50
		gadget = "89C8C3"
		self.do(gadget)

		#mov     eax, ecx
		#retn


  def test_gadget__ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St12_Setiosflags(self):
		#_ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St12_Setiosflags
		gadget = "4889C8488B09488B49E84801C1095118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#or      [rcx+18h], edx
		#retn


  def test_gadget__ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St13_Setprecision(self):
		#_ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St13_Setprecision
		gadget = "4889C8488B094863D2488B49E84889540808C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+8], rdx
		#retn


  def test_gadget__ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St14_Resetiosflags(self):
		#_ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St14_Resetiosflags
		gadget = "4889C8488B09F7D2488B49E84801C1215118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#not     edx
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#and     [rcx+18h], edx
		#retn


  def test_gadget__ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St5_Setw(self):
		#_ZStlsIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_St5_Setw
		gadget = "4889C8488B094863D2488B49E84889540810C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+10h], rdx
		#retn


  def test_gadget__ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St12_Setiosflags(self):
		#_ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St12_Setiosflags
		gadget = "4889C8488B09488B49E84801C1095118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#or      [rcx+18h], edx
		#retn


  def test_gadget__ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St13_Setprecision(self):
		#_ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St13_Setprecision
		gadget = "4889C8488B094863D2488B49E84889540808C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+8], rdx
		#retn


  def test_gadget__ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St14_Resetiosflags(self):
		#_ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St14_Resetiosflags
		gadget = "4889C8488B09F7D2488B49E84801C1215118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#not     edx
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#and     [rcx+18h], edx
		#retn


  def test_gadget__ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St5_Setw(self):
		#_ZStlsIwSt11char_traitsIwEERSt13basic_ostreamIT_T0_ES6_St5_Setw
		gadget = "4889C8488B094863D2488B49E84889540810C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+10h], rdx
		#retn


  def test_gadget__ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St12_Setiosflags(self):
		#_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St12_Setiosflags
		gadget = "4889C8488B09488B49E84801C1095118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#or      [rcx+18h], edx
		#retn


  def test_gadget__ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St13_Setprecision(self):
		#_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St13_Setprecision
		gadget = "4889C8488B094863D2488B49E84889540808C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+8], rdx
		#retn


  def test_gadget__ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St14_Resetiosflags(self):
		#_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St14_Resetiosflags
		gadget = "4889C8488B09F7D2488B49E84801C1215118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#not     edx
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#and     [rcx+18h], edx
		#retn


  def test_gadget__ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St5_Setw(self):
		#_ZStrsIcSt11char_traitsIcEERSt13basic_istreamIT_T0_ES6_St5_Setw
		gadget = "4889C8488B094863D2488B49E84889540810C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+10h], rdx
		#retn


  def test_gadget__ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St12_Setiosflags(self):
		#_ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St12_Setiosflags
		gadget = "4889C8488B09488B49E84801C1095118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#or      [rcx+18h], edx
		#retn


  def test_gadget__ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St13_Setprecision(self):
		#_ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St13_Setprecision
		gadget = "4889C8488B094863D2488B49E84889540808C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+8], rdx
		#retn


  def test_gadget__ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St14_Resetiosflags(self):
		#_ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St14_Resetiosflags
		gadget = "4889C8488B09F7D2488B49E84801C1215118C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#not     edx
		#mov     rcx, [rcx-18h]
		#add     rcx, rax
		#and     [rcx+18h], edx
		#retn


  def test_gadget__ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St5_Setw(self):
		#_ZStrsIwSt11char_traitsIwEERSt13basic_istreamIT_T0_ES6_St5_Setw
		gadget = "4889C8488B094863D2488B49E84889540810C3"
		self.do(gadget)

		#mov     rax, rcx
		#mov     rcx, [rcx]
		#movsxd  rdx, edx
		#mov     rcx, [rcx-18h]
		#mov     [rax+rcx+10h], rdx
		#retn


  def test_gadget___atomic_flag_for_address(self):
		#__atomic_flag_for_address
		gadget = "4889CA4889C848C1E00448C1EA024801C24801D14889CA4889C848C1E00548C1EA074801C24801CA4889D14889D048C1E91148C1E00D4801C84801C24889D048C1E81F4801D0488D15B3B6000083E00F4801D0C3"
		self.do(gadget)

		#mov     rdx, rcx
		#mov     rax, rcx
		#shl     rax, 4
		#shr     rdx, 2
		#add     rdx, rax
		#add     rcx, rdx
		#mov     rdx, rcx
		#mov     rax, rcx
		#shl     rax, 5
		#shr     rdx, 7
		#add     rdx, rax
		#add     rdx, rcx
		#mov     rcx, rdx
		#mov     rax, rdx
		#shr     rcx, 11h
		#shl     rax, 0Dh
		#add     rax, rcx
		#add     rdx, rax
		#mov     rax, rdx
		#shr     rax, 1Fh
		#add     rax, rdx
		#lea     rdx, unk_6FCEC300
		#and     eax, 0Fh
		#add     rax, rdx
		#retn


  def test_gadget___cxa_get_exception_ptr(self):
		#__cxa_get_exception_ptr
		gadget = "488B41F8C3"
		self.do(gadget)

		#mov     rax, [rcx-8]
		#retn


  def test_gadget_sub_6FCE34C0(self):
		#sub_6FCE34C0
		gadget = "488D0509F90000488905B29F0000C3"
		self.do(gadget)

		#lea     rax, off_6FCF2DD0
		#mov     cs:qword_6FCED480, rax
		#retn


  def test_gadget_sub_6FCE3590(self):
		#sub_6FCE3590
		gadget = "488D0539F80000488905D29E0000C3"
		self.do(gadget)

		#lea     rax, off_6FCF2DD0
		#mov     cs:qword_6FCED470, rax
		#retn


  def test_gadget_atomic_flag_clear_explicit(self):
		#atomic_flag_clear_explicit
		gadget = "C60100C3"
		self.do(gadget)

		#mov     byte ptr [rcx], 0
		#retn


  def test_gadget_atomic_flag_test_and_set_explicit(self):
		#atomic_flag_test_and_set_explicit
		gadget = "0FB601C60101C3"
		self.do(gadget)

		#movzx   eax, byte ptr [rcx]
		#mov     byte ptr [rcx], 1
		#retn


  def test_gadget_sub_6FCE3BC0(self):
		#sub_6FCE3BC0
		gadget = "C741100000000048891166C74451180000C3"
		self.do(gadget)

		#mov     dword ptr [rcx+10h], 0
		#mov     [rcx], rdx
		#mov     word ptr [rcx+rdx*2+18h], 0
		#retn
        
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(filename)s.%(funcName)s() - %(levelname)s : %(message)s',
                        level=logging.DEBUG)
    unittest.main()
    

     