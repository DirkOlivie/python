import numpy as np

import calculate3dpressure

def calculate3ddensity(t,ps,p0,hyam,hybm) :
#---------------------
#
    '''
    MODIFICATIONS
        2026-09-07 : extension to irregular grid

    

    '''

    Rair=287.058
#
    ndim = t.ndim

    if   ( ndim == 3 ) : nlev, nlat, nlon = t.shape ; density  = np.zeros( ( nlev, nlat, nlon ) )
    elif ( ndim == 2 ) : nlev, ncol       = t.shape ; density  = np.zeros( ( nlev, ncol       ) )
#
    pressure = calculate3dpressure.calculate3dpressure(ps=ps,p0=p0,hyam=hyam,hybm=hybm)
# 
    for ilev in range(nlev) :
#
        if   ( ndim == 3 ) : density[ilev,:,:] = pressure[ilev,:,:] / Rair / t[ilev,:,:]
        elif ( ndim == 2 ) : density[ilev,:  ] = pressure[ilev,:  ] / Rair / t[ilev,:  ]
#
    return density    
