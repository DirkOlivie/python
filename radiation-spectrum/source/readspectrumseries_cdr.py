import numpy as np
import math

import readfile_cdr

def readspectrumseries_cdr(var, wvlresolution, freqtype):
#----------------------
    '''
    AIMING
        averaging over


    INPUT
        var
        wvlresolution
        year0
        year1
    '''
    Rearth=6370e3


    area=4.*math.pi*Rearth*Rearth

    D = readfile_cdr.readfile_cdr(var=var, wvlresolution=wvlresolution)

#   final data
    data = {'variable' : D['variable'], \
            'valuelist' : D['field'], \
            'units' : D['units'], \
            'timelist': D['yearlist'], \
            'area' : area, \
            'areaglob' : area}

    return data
