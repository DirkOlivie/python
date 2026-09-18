import re
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import wvl2wvlbnds

def readfile_aerotab(var):
#-------------------
#
    '''
    REMARK
        Units : not mentioned in the file, but I assume they are 'W m-2 nm-1 (as in Climate Data Records NetCDF file)'

    CALLED BY
        readspectrum_aerotab

    CALLS

    '''
    filename='/datalake/NS2345K/olivie/volcaod-auxiliary/solar-spectrum-aerotab/xtspec.dat'
    wavelength_units='nm'

    f=open(filename)

    wavelength=[]
    valuelist=[]

    for line in f:

        line=line.strip()       # removes also leading and trailing blanks
        line=re.sub(' +',' ',line) # reduced blanks to single blanks
        content=line.split(" ")

        wavelength.append(float(content[0]))
        valuelist.append(float(content[1]))
#
    f.close()
#
    units='W m-2 nm-1' # I assume these are the correct units
#
#   convert wavelenght array and value array into numpy arrays
    wavelength = np.array(wavelength, dtype=float)
    valuelist  = np.array(valuelist,  dtype=float)    

#    nwvl=len(wavelength)

#   find wavelength bounds
#    wavelength_bnds=np.zeros(nwvl+1,dtype=float)
#    wavelength_bnds[0]      = wavelength[0] - 0.5 * ( wavelength[1] - wavelength[0] )
#    wavelength_bnds[1:nwvl] = 0.5 * ( wavelength[0:nwvl-1] + wavelength[1:nwvl] )
#    wavelength_bnds[nwvl]   = wavelength[nwvl-1] + 0.5 * ( wavelength[nwvl-1] - wavelength[nwvl-2] )
    wavelength_bnds = wvl2wvlbnds.wvl2wvlbnds(wavelength=wavelength)

#   data structure
    data= { 'variable' : var, \
            'valuelist' : valuelist, \
            'units'     : units, \
            'wavelength' : wavelength, \
            'wavelength_bnds' : wavelength_bnds, \
            'wavelength_units' : wavelength_units}
#
    return data
