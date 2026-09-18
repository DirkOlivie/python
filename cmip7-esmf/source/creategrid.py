import numpy as np
import math

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lat2latbnds
import lon2lonbnds

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


def creategrid(grid):
#-------------
    '''
    REMARK
        Corners should be listed counterclockwise in SCRIP file
         1       4  
         |       |
         |       |
         2 ----- 3

    INPUT
        grid

    RETURN  datastructure

    '''
#
    if   ( grid=='lat0.25xlon0.25_lon0minus179.875_lat0plus89.875' ) : nlon = 360 * 4 ; nlat = 180 * 4 ; lon0=-179.875 ; lat0= 89.875 ; latorientation=-1.  
    elif ( grid=='lat0.5xlon0.5_lon0minus179.75_lat0minus89.75'    )   : nlon = 360 * 2 ; nlat = 180 * 2 ; lon0=-179.75  ; lat0=-89.75  ; latorientation= 1.
    else :
        print('+++ creategrid +++')
        print('No grid recognized : ', grid)
        quit()
#
    nsize    = nlon * nlat
    ncorners = 4
    nrank    = 2 # for regular lat-lon grids
        
    grid_center_lat = np.zeros((nsize), dtype='d')           # degrees    
    grid_center_lon = np.zeros((nsize), dtype='d')           # degrees 
    grid_corner_lat = np.zeros((nsize, ncorners), dtype='d') # degrees
    grid_corner_lon = np.zeros((nsize, ncorners), dtype='d') # degrees
    grid_dims = (nlon,nlat)
    grid_imask = np.zeros((nsize), dtype='i4')     # unitless
    grid_area = np.zeros((nsize), dtype='d')       # square radians   
#
#   longitude
    longitude=np.arange(lon0,lon0+360., 360./float(nlon),dtype='d')
    if ( len(longitude) != nlon) : 
        print('+++ creategrd +++')
        print('longitude array does not have nlon longitudes : ', len(longitude), nlon)
        quit()


#    for ilon in range(0,nlon) :
#        print('longitude : ', ilon, longitude[ilon])
#    quit()

#   latitude
    latitude=np.arange(lat0,lat0+180.*latorientation, 180./float(nlat) * latorientation, dtype='d')
    if ( len(latitude) != nlat) :
        print('+++ creategrd +++')
        print('latitude array does not have nlat latitudes : ', len(latitude), nlat)
        quit()

#    for ilat in range(0,nlat) :
#        print('latitude : ', ilat, latitude[ilat])
#    quit()

#   area
    lonbnds = lon2lonbnds.lon2lonbnds(longitude=longitude)
    latbnds = lat2latbnds.lat2latbnds(latitude=latitude)
#
#   areaweight in radiand
    areaweight = 4. * math.pi * areafraction.areafraction(latitude=latitude,longitude=longitude,outputtype='weight') 

    print('Sum areaweight (should be 1) : ', np.sum(areaweight)/4./math.pi )

    i=0
    for ilat in range(0,nlat) :
        for ilon in range(0,nlon) :
#           center
            grid_center_lat[i] = latitude[ilat]
            grid_center_lon[i] = longitude[ilon]

#           corners [should be counterclockwise            
            grid_corner_lat[i,0] = latbnds[ilat+ (1+int(latorientation)) // 2]
            grid_corner_lat[i,1] = latbnds[ilat+ (1-int(latorientation)) // 2]
            grid_corner_lat[i,2] = latbnds[ilat+ (1-int(latorientation)) // 2]
            grid_corner_lat[i,3] = latbnds[ilat+ (1+int(latorientation)) // 2]

            grid_corner_lon[i,0] = lonbnds[ilon]
            grid_corner_lon[i,1] = lonbnds[ilon]
            grid_corner_lon[i,2] = lonbnds[ilon+1]
            grid_corner_lon[i,3] = lonbnds[ilon+1]

#           mask       
            grid_imask[i] = 1

#           areaweight (sums up to 4*pi]
            grid_area[i] = areaweight[ilat,ilon]

            i = i + 1
#
#   datastructure
    data = { 'nsize'    : nsize, \
             'ncorners' : ncorners, \
             'nrank'    : nrank, \
             'grid_center_lat' : grid_center_lat, \
             'grid_center_lon' : grid_center_lon, \
             'grid_corner_lat' : grid_corner_lat, \
             'grid_corner_lon' : grid_corner_lon, \
             'grid_dims' : grid_dims, \
             'grid_imask' : grid_imask, \
             'grid_area' : grid_area}

    return data
