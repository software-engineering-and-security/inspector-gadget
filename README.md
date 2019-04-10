# inspector-gadgetRequirements

1) pyvex: 
# pip install pyvex

2) capstone: 
# apt-get install python-capstone

3) z3
git clone https://github.com/Z3Prover/z3
$ python scripts/mk_make.py --python
./configure --prefix=$HOME/mylibs/
$ cd build
$ make
# sudo make install

4) pefile
git clone https://github.com/erocarrera/pefile
setup.py build
setup.py install

5) pyelftools
# apt-get install python-pyelftools

Note: you may have to update PYTHONPATH by adding /path/to/z3.git/build/

6) dill
# pip install dill