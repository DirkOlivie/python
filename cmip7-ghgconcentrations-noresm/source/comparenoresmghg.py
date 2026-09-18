from netCDF4 import Dataset
import numpy as np
import math

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import trimseries
import fillstatistics

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

def comparenoresmghg(filename0, filename1, species):
#-------------------
    '''
    AIM
        caluculated timeseries of global totals of processed emissions
        convert units : molecules cm-2 s-1 and molecules cm-3 s-1 to Tg yr-1

    INPUT
        filename
        freqtype : 'YEA' | ...

    RETURN
        list of datastructures

    '''
#
    print('#################')
    print('Species : ', species)
    print('#################')
#
#   open NetCDF file
    print('File 0')
    print(filename0)
    nc_fid = Dataset(filename0, 'r')
    datelist0  = np.array(nc_fid.variables['date'][:])   # date
    field0     = np.array(nc_fid.variables[species][:])
    nc_fid.close
    print(field0[2000,:])

#
    print('File 1')
    print(filename1)
    nc_fid = Dataset(filename1, 'r')
    datelist1  = np.array(nc_fid.variables['date'][:])   # date
    field1     = np.array(nc_fid.variables[species][:])
    nc_fid.close    
    print(field1[2000,:])

    print(field1[2000,:]-field0[2000,:])
