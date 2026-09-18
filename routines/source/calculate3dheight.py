import numpy as np
#
import calculate3dpressure
import calculate3dpressbnd
import calculate3ddensity
#
def calculate3dheight(p0,ps,t,hyam,hybm,hyai,hybi) :
#--------------------
#   
#
#   start using inverse level order
#   --------------------- pressbnd(0)                                                           
#
#   . . . . . . . . . . .                  pressure(0)
#
#   --------------------- pressbnd(1)
#              .  
#              .
#              .
#
#   --------------------- pressbnd(ilev-1)
#
#   . . . . . . . . . . .                  pressure(ilev-1) 
#   
#   --------------------- pressbnd(ilev)
#
#   . . . . . . . . . . .                  pressure(ilev)    /  density(ilev)      z(ilev)   
#   [b]
#   --------------------- pressbnd(ilev+1)
#   [a]
#   . . . . . . . . . . .                  pressure(ilev+1)     density(ilev+1)    z(ilev+1)
#
#   --------------------- pressbnd(ilev+2)
#              .
#              .
#              .
#              
#   --------------------- pressbnd(nlev-1)
#
#   .....................                  pressure(nlev-1)                        z(nlev-1)
#                                                                                   
#   --------------------- pressbnd(nlev)                                            
#   ///\\\///\\\///\\\///
#
    grav = 9.81
#
    ndim = t.ndim
#
    if   ( ndim == 3 ) : nlev, nlat, nlon = t.shape ; z = np.zeros( ( nlev, nlat, nlon ) )
    elif ( ndim == 2 ) : nlev, ncol       = t.shape ; z = np.zeros( ( nlev, ncol       ) )

    pressure = calculate3dpressure.calculate3dpressure(  p0=p0,ps=ps,hyam=hyam,hybm=hybm)
    pressbnd = calculate3dpressbnd.calculate3dpressbnd(  p0=p0,ps=ps,                    hyai=hyai,hybi=hybi)
    density  = calculate3ddensity.calculate3ddensity(t=t,p0=p0,ps=ps,hyam=hyam,hybm=hybm)
   
    for ilev in reversed(range(0,nlev)) :

#       contribution [a]        
        if ( ilev != ( nlev-1) ) :
            if   ( ndim == 3 ) : z[ilev,:,:] = z[ilev+1,:,:] + ( pressure[ilev+1,:,:] - pressbnd[ilev+1,:,:] ) / density[ilev+1,:,:] / grav
            elif ( ndim == 2 ) : z[ilev,:  ] = z[ilev+1,:  ] + ( pressure[ilev+1,:  ] - pressbnd[ilev+1,:  ] ) / density[ilev+1,:  ] / grav

#       contribution [b]
        if   ( ndim == 3 ) : z[ilev,:,:] = z[ilev,:,:] +  ( pressbnd[ilev+1,:,:] - pressure[ilev,:,:] ) / density[ilev,:,:] / grav
        elif ( ndim == 2 ) : z[ilev,:  ] = z[ilev,:  ] +  ( pressbnd[ilev+1,:  ] - pressure[ilev,:  ] ) / density[ilev,:  ] / grav
#
    return z    
