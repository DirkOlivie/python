import numpy as np
from netCDF4 import Dataset

import readsingleh0field

'''
REMARK

'''


def readsingleextrapolatetosurface( expid, var, date):
#---------------------------------   
    '''
    MODIFICATIONS
        (2022-09-12) : creation     
    '''
#----------------------------------------------------------------
#
    print('+++ readsingleextrapolatetosurface +++')
    print('date : '+date)
#
#
    Mh2o    = 18.01
    Mdryair = 28.97 
    Rair    = 287.058
    grav       = 9.81
#
    if ( var == 'CHBR3_extrapolate00m') : 
        varorig   = 'CHBR3'
        refheight = 0.
    elif ( var == 'CHBR3_extrapolate10m') :
        varorig   = 'CHBR3'
        refheight = 10.
    else :
        print('Extrapolatesurfacesinglefield : no variable recognized : '+var)
        quit()
#
#   obtain original field    
    data =  readsingleh0field.readsingleh0field(expid=expid,var=varorig,date=date)

#   obtain temperature
#    ps = readsingleh0field.readsingleh0field(expid=expid,var='PS',date=date)
    ta = readsingleh0field.readsingleh0field(expid=expid,var='T' ,date=date)
#
    nlev, nlat, nlon = ta['field'].shape

#   calculate pressure at boundaries
    z        = np.zeros( ( nlev  , nlat, nlon ) )
    density  = np.zeros( ( nlev  , nlat, nlon ) )
    pressure = np.zeros( ( nlev  , nlat, nlon ) )
    pressbnd = np.zeros( ( nlev+1, nlat, nlon ) )

#
    for ilev in range(nlev) :

        pressure[ilev,:,:] = data['hyam'][ilev] * data['p0'] + data['hybm'][ilev] * data['ps'][:,:] # mid-level pressure
        density[ ilev,:,:] = pressure[ilev,:,:] / Rair / ta['field'][ilev,:,:]

    for ilev in range(nlev+1) :

        pressbnd[ilev,:,:] = data['hyai'][ilev] * data['p0'] + data['hybi'][ilev] * data['ps'][:,:] # mid-level pressure

#
#   start using inverse level order
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


    for ilev in reversed(range(0,nlev)) : 

#       contribution [a]        
        if ( ilev != ( nlev-1) ) :
            z[ilev,:,:] = z[ilev+1,:,:] + ( pressure[ilev+1,:,:] - pressbnd[ilev+1,:,:] ) / density[ilev+1,:,:] / grav

#       contribution [b]
        z[ilev,:,:] = z[ilev,:,:] +  ( pressbnd[ilev+1,:,:] - pressure[ilev,:,:] ) / density[ilev,:,:] / grav
#
#   
#   final surface field
    surface = np.zeros( (nlat,nlon) )
#
    for ilon in range(0,nlon) : 
        for ilat in range(0,nlat) : 
#
            x=z[nlev-3:nlev,ilat,ilon]
            y=data['field'][nlev-3:nlev,ilat,ilon]
#
#           all these points lie on parabole :  y = a * x^2 + b * x  + c             
#           i.e.                             : y[0] = a * [x0]*x[0] + b * x[0] + c 
#                                              y[1] = a * [x1]*x[1] + b * x[1] + c
#                                              y[2] = a * [x2]*x[2] + b * x[2] + c
#           or in matrix notation            : / [x0]*x[0]   x[0]   1 \   / a \    / y[0] \
#                                              | [x1]*x[1]   x[1]   1 | * | b | =  | y[1] |
#                                              \ [x2]*x[2]   x[2]   1 /   \ c /    \ y[2] /
#           or shorthand matrix notation     : M * coefflist = R

            M = np.array([[x[0]*x[0], x[0], 1.], \
                          [x[1]*x[1], x[1], 1.], \
                          [x[2]*x[2], x[2], 1.]])
            R = np.array([y[0], y[1], y[2]])

            c = np.linalg.solve(M,R) # [a,b,c]

            surface[ilat,ilon] =  c[0] * refheight * refheight + c[1] *refheight + c[2]
#
#           print(x,y,surface[ilat,ilon])
#
#   create new structure

    newdata = { 'field'     : surface, \
                'longitude' : data['longitude'], \
                'latitude'  : data['latitude'], \
                'nlon'      : data['nlon'], \
                'nlat'      : data['nlat'], \
                'units'     : data['units'] }
#
    print('--- readsingleextrapolatetosurface ---')
#
    return newdata
