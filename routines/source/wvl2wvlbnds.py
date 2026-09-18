import numpy as np

def wvl2wvlbnds(wavelength) :
#--------------
    '''
    INPUT
        wavelength : array of wavelenghts

    '''
    nwvl=len(wavelength)

#   find wavelength bounds
    wavelength_bnds=np.zeros(nwvl+1,dtype=float)

    wavelength_bnds[0]      = wavelength[0] - 0.5 * ( wavelength[1] - wavelength[0] )
    wavelength_bnds[1:nwvl] = 0.5 * ( wavelength[0:nwvl-1] + wavelength[1:nwvl] )
    wavelength_bnds[nwvl]   = wavelength[nwvl-1] + 0.5 * ( wavelength[nwvl-1] - wavelength[nwvl-2] )
#
    return wavelength_bnds
