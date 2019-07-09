import sys
import binascii
import pefile
import os


def getHexStreamFromPE(filename):

    pe = pefile.PE(filename)
    
    execSections = []

    textSection = None
    for section in pe.sections:
        sName = section.Name
        print("name: '%s'" % sName.rstrip())
        # why doesn't this work? if sName == '.text':
        if sName.startswith('.text'):
            print("found .text section")
            textSection = section

            byteStream = textSection.get_data()
            hexStream = binascii.hexlify(byteStream)
    
            newExecSection = {}
            newExecSection['name'] = sName
            newExecSection['addr'] = textSection.VirtualAddress
            newExecSection['hexStream'] = hexStream
            execSections.append(newExecSection)
            break


    
    
    return execSections

if __name__ == '__main__':
    if sys.argv[1] == '--test':
        for filename in sys.argv[2:]:
            print("handling '", filename ,"'")
            r = getHexStreamFromPE(filename)
            print("code in ", os.path.basename(filename))
            print(" --> # of executable sections found: ", len(r))
            i = 0
            for s in r:
                print("   ", i, ": ", s['name'], "0x", hex(s['addr']), s['hexStream'])
                i += 1
