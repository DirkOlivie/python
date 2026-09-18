import matplotlib.pyplot as plt
import numpy as np
import math
import os

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits

'''
    MODIFICATIONS
'''

def convertdata2histogram(data) :
#------------------------
    '''
    INPUT
        data : structure containing
            'field'
            'weight' [areaweight]
            'periodlist'
            'variable'
            'units'    

    OUTPUT

    '''
#    
    print('+++ convertdata2histogram +++')
#
#   find min and max : values
    xmin=np.amin(data['field'])
    xmax=np.amax(data['field'])

#   generate xlist
#
#     [0]   [1]                  [nx-1] 
#   |-----|-----|-- ... --|-----|-----| : xbndlist
#      |     |               |     |    : xlist
#    xmin                        xmax 
#     [0]   [1]                 [nx-1]                          
    nx=500
#   nx=100
    dx=(xmax-xmin) / float(nx-1)
    x0=xmin-dx
    x1=xmax+dx
    xbndlist = x0   + np.arange(0,nx+1) * dx    
    xlist    = xmin + np.arange(0,nx  ) * dx
    valuelist=np.zeros(nx,dtype=float)

#   plot the individual lines
    for ix in range(0,nx) : 
       xmin=xbndlist[ix]
       xmax=xbndlist[ix+1]

       wlist = ( data['field'] >= xmin) * ( data['field'] <  xmax)  # [True, False, ...]

       valuelist[ix] = np.sum(data['weight'][wlist]) \
                     / dx
#
#   output data   
    data={ 'xlist' : xlist, \
           'valuelist' : valuelist} 
#
    return data

    print('--- convertdata2histogram ---')

    

