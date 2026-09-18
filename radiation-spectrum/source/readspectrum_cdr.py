import numpy as np

import readfile_cdr

def readspectrum_cdr(var, wvlresolution, year0, year1):
#----------------------
    '''
    AIMING
        averaging over

    INPUT
        var
        wvlresolution : 'standard' | 'high'
        year0
        year1
    '''
#
    D = readfile_cdr.readfile_cdr(var=var, wvlresolution=wvlresolution)

#   make subselection
    iset = ( D['yearlist'] >= year0 ) & ( D['yearlist'] <= year1 )
    field = D['field'][iset,:] # subselection on time

#   average over timedimension
    valuelist = np.mean(field, axis=0)  # averaging over time

#   final data
    data = {'variable' : D['variable'], \
            'valuelist' : valuelist, \
            'units' : D['units'], \
            'wavelength' : D['wavelength'], \
            'wavelength_bnds' : D['wavelength_bnds'], \
            'wavelength_units' : D['wavelength_units']}
#
    return data
