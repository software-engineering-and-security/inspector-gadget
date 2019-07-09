# What is inspector gadget?

Inspector-gadget (a.k.a. PSHAPE - Practical Support for Half-Automated Program Exploitation) 
is an open source tool  which  assists  analysts  in  exploit  development.  It 
discovers gadgets, chains gadgets together, and ensures that side effects
such  as  register  dereferences  do  not  crash  the  program.  

It relies on the notion of gadget summaries , a compact representation
of the effects a gadget or a chain of gadgets has on memory and registers
These semantic summaries enable analysts to quickly determine the
usefulness of long, complex gadgets that use a lot of aliasing or involve
memory accesses.

If you use inspector-gadget in your research, please cite the following paper:

**Andreas Follner, Alexandre Bartel, Hui Peng, Yu-Chen Chang, Kyriakos Ispoglou, Mathias Payer, Eric Bodden: PSHAPE: Automatically Combining Gadgets for Arbitrary Method Execution, in Security and Trust Management Workshop (STM@ESORICS), Heraklion, Greece, 2016** 
[\[bib\]](https://www.abartel.net/static/p/stm2016-combiningGadgets.bib.txt) [\[pdf\]](https://www.abartel.net/static/p/stm2016-combiningGadgets.pdf)
[\[www\]](https://sites.google.com/site/exploitdevpshape/)

# Requirements

0) python3
```console
# apt-get install python3
```

1) pyvex: 
```console
# pip3 install pyvex
```

2) capstone: 
```console
# apt-get install python3-capstone
```

3) z3
```console
$ git clone https://github.com/Z3Prover/z3
$ python scripts/mk_make.py --python
$ ./configure --python --prefix=$HOME/mylibs/
$ cd build
$ make
# sudo make install
```
Note: you may have to update PYTHONPATH by adding /path/to/z3.git/build/

4) pefile
```console
# apt-get install python3-pefile
```

5) pyelftools
```console
# apt-get install python3-pyelftools
```


6) dill
```console
# pip3 install dill
```

# Output

Inspector-gadget produces four files:

* **filename.pkl** is a blob containing all discovered gadgets. It can be read by Inspector-gadget, so gadget discovery has to be done only once.
* **filename_all_gadgets** is a textfile containing all gadgets, even the ones Inspector-gadget cannot analyse properly due to jumps etc.
* **filename_gadgets** is a textfile containing gadgets Inspector-gadget analyzed and uses for autochaining.
* **filename_summary** is a textfile containing a summary of the analysis.


# Usage

```console
$ ./ig.sh <parameters>
```
* -b path and name of the binary (we support ELF and PE for now)
* -maxlen maximum length of gadgets (in instructions)
* -minlen minimum length of gadgets (in instructions)
* -arg number of registers to initialize by the auto-chainer (Linux: 2 to 6; Windows: 2 to 4)
* -p number of threads (greatly enhances gadget discovery and summaries! If you have a multicore CPU, use this)
* -spm show effects on memory in output files
* -a architecture (default is x86-64, x86 is experimental and only works for gadget discovery, not chaining)
* -o output directory


# Examples

```console
$ mkdir ./output/
$ ./ig.sh -b ./input/libc-2.28.so -maxlen 10 -arg 2 -o ./output/ -p 20
```
This finds all gadgets that contain up to 10 instructions in file "libc-2.28.so" stored in ./input/ and creates a chain to initialize rdi and rsi.
Running it the first time takes a long time to construct the gadgets.
Running the exact some command a second time will be much faster (the gadgets are stored on the disk the first time).


