import dill

# dump gadgets to file
def dumpGadgets(gadgets, fn):
    f = open(fn, 'wb')
    dill.dump(gadgets, f)
    f.close()

# read gadgets from file
def readGadgets(fn):
    gadgets = []

    f = open(fn, 'rb')
    while True:
        try:
            g = dill.load(f)
            gadgets += g
        except EOFError:
            break
    f.close()
       
    return gadgets


