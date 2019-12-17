import gadgetfinder.executablecode as ecode
import gadgetfinder.myshare as myshare
import gadgetfinder.filters as filters
import gadgetfinder.storage as storage
from InspectorGadget import passZero, determine_type
from Gadget import Gadget
#
import multiprocessing as mp
import capstone as cs
import os
import sys
import dill
import time
import logging
import traceback
import binascii

log = logging.getLogger(__name__)

ret = b'\xc3\xc2'
retn = b'\xc2'

def find_gadgets(arch, hexdata, foffset, offset, maxlen, minlen):
    assert type(hexdata) is type(b''), "current type: %s" % type(hexdata)
    assert type(offset) is type(1), "current type: %s" % type(offset)
    assert offset > 0
    assert maxlen > 0
    assert minlen > 0
    assert hexdata[offset] in ret

    print("find_gadgets: %d" % (offset))
    
    start_time = time.time()
    #print("Starting at addres " + str(off) )

    #Collects all found gagdets
    Gadgets = []
    
    if arch == "x86":
        bitlength = 32
        md = cs.Cs(cs.CS_ARCH_X86, cs.CS_MODE_32)
    elif arch == "x86-64":
        bitlength = 64
        md = cs.Cs(cs.CS_ARCH_X86, cs.CS_MODE_64)
    else:
        raise Exception("bitlength must be either 32 or 64. Got ", bitlength)
   
    offset_back = offset - 1

    while True: 
        offset_back -= 1
        # check that we do not underflow the index in hexdata
        # while looking for gadgets
        if offset_back < 0 or offset_back < (offset - 15*maxlen):
            break;

        gadget = hexdata[offset_back : offset + 1]           
                               
        length = 0
        endswithret = False
        total_size = 0
        for (address, size, mnemonic, op_str) in md.disasm_lite(gadget, offset):
            #print("   '%s' %s" % (mnemonic, type(mnemonic)))
            length += 1
            total_size += size
            if mnemonic == "ret" or mnemonic == "retf":
                #print("endswithret")
                endswithret = True
                break
        #print("%d %d %d" % (length, endswithret, total_size))
        
        # Adding a threshold is important, because a gadget might 
        # disassemble to something shorter if we go back far enough!
        # E.g., 4158415948B89090909090909090C3 disassembles to:
        # nop  ; ret # nop ; nop ; ret # etc., and if we stop when 
        # reaching the maximum of 5 instructions we miss the following:
        # pop r8 ; pop r9 ; movabs rax,0x9090909090909090 ; ret
        # Length +5 = ~10% slowdown
        if length > maxlen + 5:
            continue 
        if length <= 0:
            continue
        if not endswithret:
            continue
        if total_size < ((offset - offset_back) + 1):
            continue
       
        #print("ok")

        disas = ""
        instructions = []
        for (address, size, mnemonic, op_str) in md.disasm_lite(gadget, offset):
            disas += mnemonic + " " + op_str + " ; "
            instructions.append(mnemonic + " " + op_str)
        realaddress = offset - len(gadget) + 1 + foffset
        try:
            posts, pres, pre, post = passZero(gadget, arch)
            #for p in pres:
            #    print("pres: %s" % p)
            #for p in posts:
            #    print("post: %s" % p)
        except Exception as e:
            print("exception in passZero: %s", e)
            print("exception in process: %s" % traceback.format_exc())
            posts = "err"
            break
        
        #print("g: %s" % (instructions))
        if posts != "err":
            gtype = determine_type(posts)
            g = Gadget(realaddress, gadget, pres, pre, posts, post, 0, gtype, 0, length, instructions, "", "")
            Gadgets.append(g)

    # end of while loop
                    
      
    goodgadgets, badgadgets = filters.filterStrict(Gadgets)
    print("Stopped at addres " + str(offset_back) )
    print("Found gadgets: " + str(len(Gadgets)))
    print("Good gadgets: %i\nBad gadgets: %i\n" %(len(goodgadgets), len(badgadgets)))   
    print("--- %s seconds ---" % (time.time() - start_time))
    
    return goodgadgets, badgadgets



#
# worker code
#
def worker_start(args):
    assert len(args) is 2

    try:
        log.info("worker start...")   
    
        #if Options.DEBUG_PROCESSES:
        #    sys.stdout = open("/tmp/" + str(os.getpid()) +".out", "w")
    
        work_queue = args[0]
        result_queue = args[1]
        #hexdata = worker_shared_vars["hexdataArray"]
        hexStream_array = myshare.hexStream_array
        byteStream_array = myshare.byteStream_array
        assert type(hexStream_array) is type([]), "current type: %s" % (type(hexStream_array))
        assert len(hexStream_array) == len(byteStream_array)
    
        log.info("entering main worker loop...")
        log.info("hexdataArray #: %d" % (len(hexStream_array)))
        while True:
            print("[w] Waiting for work_queue")
            task = work_queue.get()
            print("[w] Got element from work_queue: '%s'" % str(task))
            if type(task) is type("string"):
                print("[w] Got RETURN message. Returning...")
                print("[w] work_queue size b: %d" % work_queue.qsize())
                work_queue.task_done()
                print("[w] work_queue size a: %d" % work_queue.qsize())
                break
             
            arch = task['arch']
            foffset = task['foffset']
            byteStream_offset = task['byteStream_offset']
            maxlen = task['maxlen']
            minlen = task['minlen']
            array_i = task['array_i']
            hexStream = bytes(hexStream_array[array_i])
            byteStream = bytes(byteStream_array[array_i])
              
            progress = (100. / len(byteStream) * byteStream_offset)
      
            print("[w] %f/100 %d/%d" % (progress, byteStream_offset, len(byteStream)))
              
            gg, bg = find_gadgets(arch, byteStream, foffset, byteStream_offset, maxlen, minlen)
            print("[w] Done finding gadgets")
            result_queue.put([gg, bg])

            print("[w] Done puting in result_queue")
            work_queue.task_done()
            print("[w] Task done")
    
        print("[w] Worker has finished processing gadgets %d" % os.getpid())
        sys.stdout.flush()
    except BaseException as e:
        print("exception in thread: %s" % e)
        print("exception in process: %s" % traceback.format_exc())
        return -1

    return 0

# used to share byte streams between processes
def initProcess(hexStream_array, byteStream_array):
    print ("initprocess: %s" % type(hexStream_array))
    myshare.hexStream_array = hexStream_array
    myshare.byteStream_array = byteStream_array
    print ("initprocess: %s" % type(myshare.hexStream_array))

# main function to extract gadgets
def extractGadgets(arch, in_bin_path, out_dir, maxlen, minlen, nbr_processes, spm):
    assert os.path.isdir(out_dir)
    assert os.path.isfile(in_bin_path)

    # clean up first
    try:
        os.remove(os.path.join(out_dir, os.path.basename(in_bin_path) + "_gadgets"))
        os.remove(os.path.join(out_dir, os.path.basename(in_bin_path) + "_gadgets_debug"))
    except:
        pass
    
    ftype = ""
    data = ecode.getCodeSegments(in_bin_path)
    
    # Quick and dirty, for now use file extensions, if it's exe or dll it's a PE, 
    # otherwise ELF. If the user uses a non-executable file he/she should reconsider 
    # their life choices
    in_name = in_bin_path.lower().strip()
    if in_name.endswith(".exe"):
        ftype = "pe"
    elif in_name.endswith(".dll"):
        ftype = "pe"
    else:
        ftype = "elf"
    
    hexStream_array = []
    byteStream_array = []
    for s in data:
        print("[+] name: %s" % s['name'])
        print("[+] addr: %s" % s['addr'])
        hexStream = s['hexStream']
        byteStream = s['byteStream']
        assert type(hexStream) is type (b'aaaa')
        #print("hexStream: %d %s" % (len(hexStream), hexStream))
        #print("bytestream: %d %s" % (len(byteStream), byteStream))

        hexStreamArray = mp.Array('b', len(hexStream), lock=False)
        hexStreamArray[:len(hexStream)] = hexStream
        hexStream_array.append(hexStreamArray)
        byteStreamArray = mp.Array('b', len(byteStream), lock=False)
        byteStreamArray[:len(byteStream)] = byteStream
        byteStream_array.append(byteStreamArray)
    
    print("[+] Creating manager...")
    manager = mp.Manager()    
    print("[+] Creating worker queue...")
    work_queue = manager.Queue()
    result_queue = manager.Queue()
    
    # create tasks for workers
    array_i = 0
    for s in data:
        print("section name: ", s['name'])
        print("section addr: ", s['addr'])
            
        byteStream_cur = s['byteStream']
        assert type(byteStream_cur) is type(b''), "current type: %s" % type(byteStream_cur)

        # finding ret instruction in current code section
        print("[+] Finding RET offsets...\n"    )
        byteStream_offset = 0
        ret = b'\xc3\xc2'       
        while byteStream_offset < len(byteStream_cur):
            #read a byte
            opcode = byteStream_cur[byteStream_offset]   
            #print("opcode; '%s'" % opcode)
            if opcode in ret :
                task = {}
                task['arch'] = arch
                task['foffset'] = s['addr']
                task['byteStream_offset'] = byteStream_offset
                task['maxlen'] = maxlen
                task['minlen'] = minlen
                task['array_i'] = array_i
                qsize = work_queue.qsize()
                if qsize % 1000 == 0:
                    print("qsize: ", qsize)
                work_queue.put(task)
                #print("   new task: %s" % str(task))
            byteStream_offset += 1
        
        # processing next code section
        array_i = array_i + 1
    # make sure each process receives the "return" signal
    for i in range(nbr_processes):
        work_queue.put("RETURN") 
    print("[+] queue size: %d" % (work_queue.qsize()))


    # start workers
    start_time = time.time()
    print("[+] # processes: ", nbr_processes)
    print("[+] Start workers...")
    with mp.Pool(processes=nbr_processes, 
            initializer=initProcess, 
            initargs=(hexStream_array, byteStream_array,)) as pool:
        for i in range(nbr_processes):
            res = pool.apply_async(worker_start, ([work_queue, result_queue,],))
            print("result: %d" % res.get()) 
            if res.get() != 0:
                print ("error in process. quitting.")
                sys.exit(-1)
   
    # jobs finished
    len_gg = 0
    len_bg = 0
    
    # open files
    log.info("opening files...")
    fo, fgg, fag, fb = openGadgetFiles(in_bin_path, out_dir)

    # consume results
    log.info("consuming results...")
    current_gg = []
    current_bg = []
    while not work_queue.empty():
        print("work queue: %d" % work_queue.qsize())
        while not result_queue.empty():
            print("result queue: %d" % result_queue.qsize())
            gg, bg = result_queue.get()
            len_gg += len(gg)
            len_bg += len(bg)
            
            current_gg += gg
            current_bg += bg
            
            if len(current_gg) + len (current_bg) > 1000:
                print("dumping gadgets to disk...")
                dumpCurrentGadgets(current_gg, current_bg, fo, fgg, fag, fb, spm)
                allgg += gg
                current_gg = []
                current_bg = []  
            
            result_queue.task_done()
            qsize = result_queue.qsize()

    # end of: with ... as pool

    # dump remaining gadgets
    if len(current_gg) + len (current_bg) > 0:
        print("[+] Dumping remaining gadgets to disk...")
        dumpCurrentGadgets(current_gg, current_bg, fo, fgg, fag, fb, spm)
        
    # sending special message to workers to ask them to return
    print("[+] Waiting for processes to compute gadgets...")
    while not work_queue.empty():
        time.sleep(2)
    pool.close()  
    print("pool: ", work_queue.qsize())
    while not work_queue.empty():
        time.sleep(2)
        print("size: ", work_queue.qsize())
        print("pool processes: ", pool._processes)
    work_queue.join()
    print('close pool')
    time.sleep(2) # do not remove
    pool.close()
    print("join pool")
    pool.join()
    print("processes ended.")
    
    # empty results
    while not result_queue.empty():
        gg, bg = result_queue.get()
        len_gg += len(gg)
        len_bg += len(bg)
        
        print("dumping yet remaining gadgets to disk...")
        dumpCurrentGadgets(gg, bg, fo, fgg, fag, fb, spm)
        
        result_queue.task_done()
        qsize = result_queue.qsize()
                       
    print("Total: %i\tGood: %i\tBad: %i" %((len_gg + len_bg), len_gg, len_bg))
    
    # write summary
    summary = open(in_bin_path + "_summary", "w+")
    summary.write("Total: %i\tGood: %i\tBad: %i\n" %((len_gg + len_bg), len_gg, len_bg))
    summary.write("--- %s seconds ---" % (time.time() - start_time))
    summary.close()
    
    # close gadget files
    closeGadgetFiles([fo, fgg, fag])
    
    # read gadgets from file
    goodgadgets = storage.readGadgets(
        os.path.join(out_dir, os.path.basename(in_bin_path)) + ".pkl")
    log.info("Good gadgets #: %d" % len(goodgadgets))
    log.info("Finished!")

    return goodgadgets
 
# create new file 'fn', overwrite existing file if it exists
# returns file handler to 'fn'
def createCleanFile(in_bin_path, out_dir, suffix):
    fn = os.path.join(out_dir, (os.path.basename(in_bin_path) + suffix))
    print("[+] create new file: '%s'" % fn)
    f = open(fn, "w")
    f.close()
    f = open(fn, "ab")
    return f 
  
# open all files to write gadgets
# returns file handlers to all files
def openGadgetFiles(in_bin_path, out_dir):
    assert not in_bin_path is None
    assert not out_dir is None

    f_objects = createCleanFile(in_bin_path, out_dir, ".pkl")
    f_ggadgets = createCleanFile(in_bin_path, out_dir, "_gadgets")
    f_all_gadgets = createCleanFile(in_bin_path, out_dir, "_all_gadgets")
    f_bgadgets = createCleanFile(in_bin_path, out_dir, "_bad.pkl")
    
    return f_objects, f_ggadgets, f_all_gadgets, f_bgadgets

# close all file handlers
def closeGadgetFiles(files):
    for f in files:
        f.close()

# dump gadgets 'gadgets' to disk with file handler 'f'
def dumpGadgetsToFile(gadgets, f, spm):
        
    for g in gadgets:
        f.write(bytes("0x%x : " %(g.address), "utf8"))
        for i in g.instructions:
            f.write(bytes("%s ; " % i, "utf8"))
        f.write(bytes("\nPreconditions: %s\n" %(g.preconditions), "utf8"))
        
        postconds_write = []
        for post in g.postconditions:
            if "store" not in post:
                postconds_write.append(post)
        
        if spm == 0:
            f.write(bytes("Postconditions: %s\n" %(postconds_write),"utf8"))
        else:
            f.write(bytes("Postconditions: %s\n" %(g.postconditions),"utf8"))
        f.write(bytes("Bytestream: %s\n" %(binascii.hexlify(g.opcodes)), "utf8"))
        f.write(bytes("Length: %i\n\n" %(g.length), "utf8"))
        
# dump gadgets 'gg' and 'bg' to disk using file handlers
# f_objects to write gadget objects, f_ggadgets to write good gadgets
# and f_all_gadgets to write all gadgets
def dumpCurrentGadgets(gg, bg, f_objects, f_ggadgets, f_all_gadgets, f_bad_gadgets, spm):
    
        dill.dump(gg + bg, f_objects)
        dumpGadgetsToFile(gg, f_ggadgets, spm)
        dumpGadgetsToFile(gg + bg, f_all_gadgets, spm)
        #dill.dump(bg, f_bad_gadgets)


