import numpy as np
#
import calculate3dpressure
import calculate3dpressbnd
import calculate3ddensity
#
def calculate3dheightbnd(p0,ps,t,hyam,hybm,hyai,hybi) :
#-----------------------
#   
#
#   start using inverse level order
#
#   --------------------- pressbnd(ilev-1)                                                     zbnd(ilev-1)
#
#   . . . . . . . . . . .                  pressure(ilev-1) 
#   
#   --------------------- pressbnd(ilev)                                                       zbnd(ilev)
#
#   . . . . . . . . . . .                  pressure(ilev)    /  density(ilev)      z(ilev)   
#   [b]
#   --------------------- pressbnd(ilev+1)                                                     zbnd(ilev+1)
#   [a]
#   . . . . . . . . . . .                  pressure(ilev+1)     density(ilev+1)    z(ilev+1)
#
#   --------------------- pressbnd(ilev+2)                                                     zbnd(ilev+2) 
#              .
#              .
#              .
#
#   --------------------- pressbnd(nlev-1)                                                     zbnd(nlev-1)   
#
#   .....................                  pressure(nlev-1)                        z(nlev-1)
#                                                                                   
#   --------------------- pressbnd(nlev)                                                       zbnd(nlev)
#   ///\\\///\\\///\\\///
#
    grav = 9.81
#
    ndim = t.ndim
#
    if   ( ndim == 3 ) : nlev, nlat, nlon = t.shape ; zbnd = np.zeros( ( nlev + 1 , nlat, nlon ) )
    elif ( ndim == 2 ) : nlev, ncol       = t.shape ; zbnd = np.zeros( ( nlev + 1 , ncol       ) )

    pressbnd = calculate3dpressbnd.calculate3dpressbnd(  p0=p0,ps=ps,                    hyai=hyai,hybi=hybi)
    density  = calculate3ddensity.calculate3ddensity(t=t,p0=p0,ps=ps,hyam=hyam,hybm=hybm)

    for ilev in reversed(range(0,nlev)) :

        if   ( ndim == 3 ) : zbnd[ilev,:,:] = zbnd[ilev+1,:,:] + ( pressbnd[ilev+1,:,:] - pressbnd[ilev,:,:] ) / density[ilev,:,:] / grav
        elif ( ndim == 2 ) : zbnd[ilev,:  ] = zbnd[ilev+1,:  ] + ( pressbnd[ilev+1,:  ] - pressbnd[ilev,:  ] ) / density[ilev,:  ] / grav
#
    return zbnd    
