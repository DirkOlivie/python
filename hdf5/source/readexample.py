import h5py
import numpy as np

def printname(name):
#-------------------
    print(name)


def print_attrs(name, obj):
#--------------------------
    print(name)
    for key, val in obj.attrs.items():
        print("    %s: %s" % (key, val))

def main():
#----------

    f=h5py.File('/scratch/olivie/GFED4.1s_1997.hdf5')
    ls=list(f.keys())               #
    base_items = list(f.items())    #
   
    k = list(f.attrs.keys())
    v = list(f.attrs.values())

    g1=f.get('ancill')
    g1_ls=list(g1.keys())
    g1_items=list(g1.items())
    k1 = list(g1.attrs.keys())
    v1 = list(g1.attrs.values())
 

    f.visit(printname)  

    f.visititems(print_attrs)

    f.close()

    print('Keys : ', ls)
    print('Base items : ', base_items)
    print('Attribute keys : ', k)
    print('Attribute values : ', v)

    print('Keys : ', g1_ls)
#    print('Base items : ', g1_items)
    g1_items
    print('Attribute keys : ', k1)
    print('Attribute values : ', v1)

if __name__ == '__main__':
    main()
