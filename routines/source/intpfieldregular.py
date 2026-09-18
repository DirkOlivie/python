import numpy as np

import intplon
import intplat
import intplev
#
def intpfieldregular(infield, latinbd, latoutbd, loninbd, lonoutbd, levinbd=None, levoutbd=None, extrapolate=None):
#-------------------
    '''
     REMARK 

    ARGUMENTS
        infield
        outfield
        latinbd   : the latitudinal boundaries
        latoutbd  
        loninbd   : the longitudinal boundaries
        lonoutbd
        levinbd     : NEEDED if 3-dim field
        levoutbd    : NEEDED if 3-dim field
        extrapolate

    MODIFICATIONS
        (2025-10-18) extended with time dimension
    '''
#
#   original field
    if ( infield.ndim == 3 ) : 
        ntime, nlat0, nlon0 = infield.shape
    elif ( infield.ndim == 4 ) :
        ntime, nlev0, nlat0, nlon0 = infield.shape
#
#   final field
    nlon1=len(lonoutbd)-1
    nlat1=len(latoutbd)-1
#
    ptlon,wtlon = intplon.intplon(loninbd=loninbd, lonoutbd=lonoutbd)
    ptlat,wtlat = intplat.intplat(latinbd=latinbd, latoutbd=latoutbd)

#   2D case
    if ( infield.ndim == 3 ) :
#    if ( levinbd == None and levoutbd == None ) :
#
#       1) interpolation along latitude
        a=np.zeros((ntime,nlat1,nlon0),dtype=float)
        for ilat1 in range(0,nlat1) :
            nlat=ptlat[ilat1,0] # first value gives number of levels that contribute
            for ilat in range (1,nlat+1) :
                ilat0 = ptlat[ilat1,ilat]
                wlat  = wtlat[ilat1,ilat]
                a[:,ilat1,:] = a[:,ilat1,:]+infield[:,ilat0,:] * wlat
#
#       2) interpolation along longitude
        outfield=np.zeros((ntime,nlat1,nlon1),dtype=float)
        for ilon1 in range(0,nlon1) :
            nlon=ptlon[ilon1,0] # first value gives number of levels that contribute
            for ilon in range(1,nlon+1) :
                ilon0=ptlon[ilon1,ilon]
                wlon=wtlon[ilon1,ilon]
                outfield[:,:,ilon1] = outfield[:,:,ilon1] + a[:,:,ilon0] * wlon

#   3D case
#   elif ( levinbd != None and levoutbd != None ) :
    elif ( infield.ndim == 4 ) :  

#       original grid
#        nlev0=infield.shape[0]

#       final grid
        nlev1=len(levoutbd)-1

        ptlev, wtlev = intplev.intplev(levinbd=levinbd, levoutbd=levoutbd, extrapolate=extrapolate)
#
#       1) interpolation along vertical
        a=np.zeros((ntime,nlev1,nlat0,nlon0),dtype=float)
        for ilev1 in range(0,nlev1) :
            nlev=ptlev[ilev1,0] # first value gives number of levels that contribute
            for ilev in range(1,nlev+1) :
                ilev0=ptlev[ilev1,ilev]
                wlev=wtlev[ilev1,ilev]
                a[:,ilev1,:,:] = a[:,ilev1,:,:] + infield[:,ilev0,:,:] * wlev
    
#       2) interpolation along latitude
        b=np.zeros((ntime,nlev1,nlat1,nlon0),dtype=float)
        for ilat1 in range(0,nlat1) :
            nlat=ptlat[ilat1,0] # first value gives number of levels that contribute
            for ilat in range(1,nlat+1) :
                ilat0=ptlat[ilat1,ilat]
                wlat=wtlat[ilat1,ilat]
                b[:,:,ilat1,:] = b[:,:,ilat1,:] +a[:,:,ilat0,:] * wlat
#       3) interpolation along longitude
        outfield=np.zeros((ntime,nlev1,nlat1,nlon1),dtype=float)
        for ilon1 in range(0,nlon1) :
            nlon=ptlon[ilon1,0] # first value gives number of levels that contribute
            for ilon in range(1,nlon+1) :
                ilon0=ptlon[ilon1,ilon]
                wlon=wtlon[ilon1,ilon]
                outfield[:,:,:,ilon1]=outfield[:,:,:,ilon1]+b[:,:,:,ilon0]*wlon
#
    else :
        print('Combination of levinbd and levoutb not allowe : ')
        quit()

    return outfield
