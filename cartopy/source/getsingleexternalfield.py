import numpy as np
import readsingleexternalfield
import readsingleh0field
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import gridmanipulation
import intplon
import intplat
import interp1d


def getsingleexternalfield (expid, var, date, climtype) :
#-------------------------
    '''
    AIM 
        read fields from external oxidant/ozone climatology
        interpolates it to the grid of the current simulation (expid)

    INPUT
        expid
        var
	    date : format = 'yyyy-mm'
        climtype : 'oxidant' | 'ozone'

    CALLS
        readsingleexternalfield
        lat2latbnds
        lon2lonbnds
        readsingleh0field  
        intplon
        intplat
        interp1d

    MODIFICATIONS
        2024-04-26 :
            added possibility for radozone
        2024-04-30 : bug corrections (last latitude and last longitude were 0)
            for ilon1 in range(0,nlon1-1) -> for ilon1 in range(0,nlon1)
            for ilat1 in range(0,nlat1-1) -> for ilat1 in range(0,nlat1)     
    '''
# read external field (3D) : H [high resolution data]
    H = readsingleexternalfield.readsingleexternalfield( expid=expid, var=var, date=date, climtype=climtype)
        
    latbnds0=gridmanipulation.lat2latbnds(latitude=H['latitude'])
    lonbnds0=gridmanipulation.lon2lonbnds(longitude=H['longitude'])

    nlev0, nlat0, nlon0 = H['field'].shape

# read pressure field (2D) from NorESM simulation : G [final grid and pressure]
    G = readsingleh0field.readsingleh0field( expid=expid, var='T', date=date) # read arbritrary 3D field
    
    latbnds1=gridmanipulation.lat2latbnds(latitude=G['latitude'])
    lonbnds1=gridmanipulation.lon2lonbnds(longitude=G['longitude'])  
  
    nlev1, nlat1, nlon1 = G['field'].shape

# interpolate 
    print('preparing ptlon, wtlon')
    ptlon, wtlon = intplon.intplon(loninbd=lonbnds0, lonoutbd=lonbnds1)
    print('preparing ptlat, wtlat')
    ptlat, wtlat = intplat.intplat(latinbd=latbnds0, latoutbd=latbnds1)

# 1. interpolate longitude
    print('interpolating longitudes')
    a  = np.zeros((nlev0,nlat0,nlon1), dtype=float)
    pa = np.zeros((      nlat0,nlon1), dtype=float)
#   for ilon1 in range(0,nlon1-1) : bug correcion 2024-04-30
    for ilon1 in range(0,nlon1) :
        nlon=ptlon[ilon1,0]  # first value gives number of longitudes that contribute
        for ilon in range(1,nlon+1) :
            ilon0=ptlon[ilon1,ilon]
            wlon=wtlon[ilon1,ilon]
            a[:,:,ilon1] = a[:,:,ilon1]+H['field'][:,:,ilon0]*wlon
            pa[ :,ilon1] = pa[ :,ilon1]+H['ps'][     :,ilon0]*wlon

# 2. interpolate latitude
    print('interpolating latitudes')
    b  = np.zeros((nlev0,nlat1,nlon1), dtype=float)
    pb = np.zeros((      nlat1,nlon1), dtype=float)
#   for ilat1 in range(0,nlat1-1) : bug correction 2024-04-30
    for ilat1 in range(0,nlat1) :
        nlat=ptlat[ilat1,0]  # first value gives number of latitudes that contribute
        for ilat in range(1,nlat+1) :
            ilat0=ptlat[ilat1,ilat]
            wlat=wtlat[ilat1,ilat]
            b[:,ilat1,:] = b[ :,ilat1,:]+a[:,ilat0,:]*wlat 
            pb[ ilat1,:] = pb[  ilat1,:]+pa[ ilat0,:]*wlat 

# 3. interpolate levels 
    print('interpolating levels +++')
    c=np.zeros((nlev1,nlat1,nlon1), dtype=float)
    for ilat in range(0,nlat1) :
        for ilon in range(0,nlon1) :
            x = H['hyam'] * H['p0'] + H['hybm'] * pb[ilat,ilon]        # original (but interpolated to final grid)
            y = G['hyam'] * G['p0'] + G['hybm'] * G['ps'][ilat,ilon] # final pressure
            fx = b[:,ilat,ilon] 

            c[:,ilat,ilon] = interp1d.interp1d(x=x, y=y,fx=fx)
#           c[:,ilat,ilon] = 0.
    print('interpolating levels ---')
#
# return data
    data={'field'     : c, \
          'latitude'  : G['latitude'], \
          'longitude' : G['longitude'], \
          'units'     : H['units'], \
          'units_ps'  : G['units'], \
          'units_p0'  : G['units'], \
          'ps'    : pb, \
          'p0'    : G['p0'], \
          'hyam'  : G['hyam'], \
          'hybm'  : G['hybm'], \
          'hyai'  : G['hyai'], \
          'hybi'  : G['hybi'], \
          'nlon'  : G['nlon'],\
          'nlat'  : G['nlat'],\
          'nlev'  : G['nlev']}
#
# switch off interpolation
#    data={'field'     : H['field'], \
#          'latitude'  : H['latitude'], \
#          'longitude' : H['longitude'], \
#          'units'     : H['units'], \
#          'units_ps'  : G['units'], \
#          'units_p0'  : G['units'], \
#          'ps'    : H['ps'], \
#          'p0'    : H['p0'], \
#          'hyam'  : H['hyam'], \
#          'hybm'  : H['hybm'], \
#          'hyai'  : H['hyai'], \
#          'hybi'  : H['hybi']}
#
    return data
