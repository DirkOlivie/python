import numpy as np
#
import calculate3dheightbnd
#
def calculate3dheightdelta(p0,ps,t,hyam,hybm,hyai,hybi) :
#-------------------------
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
    nlev, nlat, nlon = t.shape
#
    zbnd = calculate3dheightbnd.calculate3dheightbnd(p0=p0,ps=ps,t=t,hyam=hyam,hybm=hybm,hyai=hyai,hybi=hybi)

    zdelta = np.zeros( ( nlev, nlat, nlon ), dtype=float )

    for ilev in range(0,nlev) :

        zdelta[ilev,:,:] = np.abs(zbnd[ilev+1,:,:] - zbnd[ilev,:,:])
#
#    print('calculate3dheightbnd')
#    print(np.sum(np.mean(zdelta, axis=(1,2))))
#    quit()

    return zdelta
