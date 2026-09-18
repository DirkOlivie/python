import numpy as np

def wvlbnds2wvl(wavelength_bnds) :
#--------------
    '''
    INPUT
        wavelength_bnds : array of wavelenght bounds

    MODIFICATIONS
        (2025-12-29) creation 

    '''
    nwvl=len(wavelength_bnds) - 1

#   find wavelength bounds
    wavelength=np.zeros(nwvl,dtype=float)

    wavelength_bnds[0:nwvl] = 0.5 * ( wavelength_bnds[0:nwvl] + wavelength_bnds[1:nwvl+1] )
#
    return wavelength
