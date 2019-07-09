import sys
import binascii

from elftools.elf.constants import SH_FLAGS
from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection


def getHexStreamsFromElfExecutableSections(filename):
    print("Processing file:", filename)
    execSections = []
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        
        goodSections = [".interp", ".note.ABI-tag", ".note.gnu.build-id", ".gnu.hash", ".hash", ".dynsym", ".dynstr", ".gnu.version", ".gnu.version_r", ".rela.dyn", ".rela.plt", ".init", ".plt", ".text", ".fini", ".rodata", ".eh_frame_hdr", ".eh_frame"]
        checkedSections = [".init", ".plt", ".text", ".fini"]
        
        for nsec, section in enumerate(elffile.iter_sections()):

            # check if it is an executable section containing instructions
            
            # good sections we know so far:
            #.interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .text .fini .rodata .eh_frame_hdr .eh_frame
        
#             flags = section['sh_flags']
#             if not (flags & SH_FLAGS.SHF_EXECINSTR):
#                 continue
            if section.name not in goodSections:
                continue
            
            # because we've already analysed almost everything we can remove all these
            #if section.name in checkedSections:
                #continue
            
            # add new executable section with the following information
            # - name
            # - address where the section is loaded in memory
            # - hexa string of the instructions
            name = section.name
            addr = section['sh_addr']
            byteStream = section.data()
            hexStream = binascii.hexlify(byteStream)
            newExecSection = {}
            newExecSection['name'] = name
            newExecSection['addr'] = addr
            newExecSection['hexStream'] = hexStream
            newExecSection['byteStream'] = byteStream
            execSections.append(newExecSection)

    return execSections


if __name__ == '__main__':
    if sys.argv[1] == '--test':
        for filename in sys.argv[2:]:
            r = getHexStreamsFromElfExecutableSections(filename)
            print("Found ", len(r), " executable sections:")
            i = 0
            for s in r:
                print("   ", i, ": ", s['name'], "0x", hex(s['addr']), s['hexStream'])
                i += 1
            
