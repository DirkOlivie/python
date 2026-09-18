import numpy as np

def calculate3dpressbnd(p0,ps,hyai,hybi):
#----------------------
#
    '''
    MODIFICATIONS
        (2026-09-07) : extension to irregular grid

    '''

    ndim = ps.ndim

    nlev = hyai.shape[0] # the value is actually nlev+1)

    if   ( ndim == 2 ) : nlat, nlon = ps.shape    ; pressbnd = np.zeros( ( nlev, nlat, nlon ) )
    elif ( ndim == 1 ) : ncol       = ps.shape[0] ; pressbnd = np.zeros( ( nlev, ncol       ) )

    for ilev in range(nlev) :

        if   ( ndim == 2 ) : pressbnd[ilev,:,:] = hyai[ilev] * p0 + hybi[ilev] * ps[:,:] # boundary pressure
        elif ( ndim == 1 ) : pressbnd[ilev,:  ] = hyai[ilev] * p0 + hybi[ilev] * ps[:  ] # boundary pressure 
#
    return pressbnd
