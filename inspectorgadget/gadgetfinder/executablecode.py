from ElfBinary import getHexStreamsFromElfExecutableSections
from PEBinary import getHexStreamFromPE

def getCodeSegments(inputbinary):
    #check whether it's elf or pe
    # we'll do it cheap, extension .exe and .dll is PE, anything else is ELF
       
    if inputbinary[len(inputbinary) - 4 : len(inputbinary)] == ".exe":
        return getHexStreamFromPE(inputbinary)
    
    if inputbinary[len(inputbinary) - 4 : len(inputbinary)] == ".dll":
        return getHexStreamFromPE(inputbinary)
    
    return getHexStreamsFromElfExecutableSections(inputbinary)



