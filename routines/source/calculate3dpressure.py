import numpy as np

def calculate3dpressure(p0,ps,hyam,hybm):
#----------------------
#
    '''
    MODIFICATIONS
        (2026-09-07) : extension to irregular grid

    '''

    ndim = ps.ndim

    nlev = hyam.shape[0]
    
    if   ( ndim == 2 ) : nlat, nlon = ps.shape    ; pressure = np.zeros( ( nlev, nlat, nlon ) )
    elif ( ndim == 1 ) : ncol       = ps.shape[0] ; pressure = np.zeros( ( nlev, ncol       ) )

    for ilev in range(nlev) : 
        if   ( ndim == 2 ) : pressure[ilev,:,:] = hyam[ilev] * p0 + hybm[ilev] * ps[:,:] # mid-level pressure
        elif ( ndim == 1 ) : pressure[ilev,:  ] = hyam[ilev] * p0 + hybm[ilev] * ps[:  ] # mid-level pressure
#
    return pressure
