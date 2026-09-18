import numpy as np

import readaerocomascii
import checkglobaltotal
import getgridtype

import sys 
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lon2lonbnds
import lat2latbnds
import lev2levbnds
import xlon2ilon
import xlat2ilat
import xlonxlat2icol
import intplev

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-volc/source')
import readareatopography

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-volcso2-input4mips/source')
import readeruptions

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction
#
#
def intpvolcstratclim(activity, longitude, latitude, resolution, levbnds, sector, species, year0, year1, i4mpdownload, filelocation):
#--------------------
    '''
    REMARK 
	    takes into account topography of NorESM
        original data is in m above sealevel

    IMPROVEMENT
        uses 365.25 : maybe should be 365

    INPUT
        longitude
        latitude
        resolution
        levbnds : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
                    11,12,13,14,15,16,17,18,19,20,
                    21,22,23,24,25,26,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40
        sector  : 'SINGLE
        species
        year0
        year1
        filelocation

    CALLED BY
	
    CALLS
	    readareatopography
	    lat2latbnds
	    lon2lonbnds
	    areafraction
	    readaerocomascii
	    xlon2ilon
	    xlat2ilat
        intplev
    '''
#
#   averaged climatology over the period : 
    if (   activity == 'volcstratclim1850-2021' ) : climyear0=1850 ; climyear1=2021
    elif ( activity == 'volcstratclim1750-2023' ) : climyear0=1750 ; climyear1=2023
    else : 
        print('+++ intpvolcstratclim +++')
        print('No activity recognized : ', activity) 
        quit()

#   time treatment climatology
    nmonth=12
    nyear = year1 - year0 + 1
    ntime = nyear * nmonth

#   get gridtype for final resolution
    gridtype=getgridtype.getgridtype(resolution=resolution)
    if ( gridtype == 'latlon' ) :
        nlon1=len(longitude)
        nlat1=len(latitude)
    elif ( gridtype == 'irregular' ) :
        ncol1 = len(longitude)

    nlev1=len(levbnds)-1
#
#   read topography file 
    topography = readareatopography.readareatopography(grid=resolution, variable='topography', filelocation=filelocation) # [m]
  
    topography= topography / 1000.  # [m -> km]
    print, 'TOPOGRAPHY = ', np.min(topography), np.max(topography)
#
#   boundaries
    if ( gridtype == 'latlon' ) :
        latbnds=lat2latbnds.lat2latbnds(latitude =latitude)
        lonbnds=lon2lonbnds.lon2lonbnds(longitude=longitude)
#
#   new field
    if (   gridtype == 'latlon'    ) : newfield=np.zeros((nlev1,nlat1,nlon1), dtype=float)
    elif ( gridtype == 'irregular' ) : newfield=np.zeros((nlev1,ncol1), dtype=float)
    else :
        print('+++ intpvolcano +++')
        print('No gridtype recognized')
        quit()
#
#   area [in m2]
    if (   gridtype == 'latlon'    ) : area=areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='area')
    elif ( gridtype == 'irregular' ) : area=readareatopography.readareatopography(grid=resolution, variable='area', filelocation=filelocation)
    else :
        print('+++ intpvolcano +++')
        print('No gridtype recognized')
        quit()
#
#   readaerocom data : units is Tg[SO2]/yr , height units is m, is assumed to be above sealevel
#   V = readaerocomascii.readaerocomascii(origin='aerocomascii', activity='volc', sector=sector, species=species)
    V = readeruptions.readeruptions(i4mpdownload=i4mpdownload, climyear0=climyear0, climyear1=climyear1)
#
    print, np.sum(V['valuelist'])
#
#   expected units 
    if ( V['units'] != 'kg' ) : 
        print('+++ intpstratclimvolcano +++')
        print('No units recognized (expected kg) : ', V['units'])
        quit()
    if ( V['height_units'] != 'm' \
      or V['depth_units']  != 'm' ) :
        print('+++ intpstratclimvolcano +++')
        print('No height units recognized (expected m) : ', V['height_units'])
        print('No depth  units recognized (expected m) : ', V['depth_units'])
        quit()
#
#   loop over all volcanoes : locations (and dates) can overlap (i.e., be the same for different eruptions)
    for i in range(0,V['n']):
#
#       find correct gridpoint
        if ( gridtype == 'latlon' ) :
            ilon = xlon2ilon.xlon2ilon(lonbnds=lonbnds,xlon=V['lonlist'][i])
            ilat = xlat2ilat.xlat2ilat(latbnds=latbnds,xlat=V['latlist'][i])      
        elif ( gridtype == 'irregular' ) : 
            icol = xlonxlat2icol.xlonxlat2icol(longitude=longitude,latitude=latitude,xlon=V['lonlist'][i],xlat=V['latlist'][i]) #
        else :
            print('+++ intpvolcano +++')
            print('No gridtype recognized')
            quit()

#
#       add topography
        if   ( gridtype == 'latlon'    ) : tmplevbnds=levbnds+topography[ilat,ilon]  # [km]
        elif ( gridtype == 'irregular' ) : tmplevbnds=levbnds+topography[icol]  # [km]
        else :
            print('+++ intpvolcano +++')
            print('No gridtype recognized')
            quit()

        tmplevbnds[0]=0. 

        print('longitude : ', V['lonlist'][i])
        print('latitude  : ', V['latlist'][i])
#       print('topography*1000 : ', topography[ilat,ilon]*1000.) 
        print('height_low : ', V['height_low'][i])
        print('height_hgh : ', V['height_hgh'][i])
  
        ptlev, wtlev = intplev.intplev(levinbd=[V['height_low'][i],V['height_hgh'][i]], levoutbd=tmplevbnds * 1000.) # units is m
        dh =V['height_hgh'][i]-V['height_low'][i]                                                                    # units is m
#
        for ilev1 in range(0,nlev1) :
            nlev=ptlev[ilev1,0] # first value gives number of levels that contribute
            for ilev in range(1,nlev+1) :
                ilev0=ptlev[ilev1,ilev]
                wlev=wtlev[ilev1,ilev]
#
#               division by dy to make it intrinsic

                if ( gridtype == 'latlon' ) :
                    newfield[ilev1,ilat,ilon] = newfield[ilev1,ilat,ilon] \
                                              + wlev * V['valuelist'][i]  \
                                              / area[ilat,ilon]           \
                                              / dh                        \
                                              / 86400.                    \
                                              / 365.25                    \
                                              / float(climyear1-climyear0+1)
                elif ( gridtype == 'irregular' ) :
                    newfield[ilev1,icol]      = newfield[ilev1,icol]     \
                                              + wlev * V['valuelist'][i] \
                                              / area[icol]               \
                                              / dh                       \
                                              / 86400.                   \
                                              / 365.25                   \
                                              / float(climyear1-climyear0+1)
                else :
                    print('+++ intpvolcano +++')
                    print('No gridtype recognized')
                    quit()
 
#   lowest layer deflated to actual thickness
    if   ( gridtype == 'latlon'    ) : newfield[0,:,:] = newfield[0,:,:] * (levbnds[1] + topography[:,:] - 0. ) / ( levbnds[1] - levbnds[0] )
    elif ( gridtype == 'irregular' ) : newfield[0,:  ] = newfield[0,:  ] * (levbnds[1] + topography[:  ] - 0. ) / ( levbnds[1] - levbnds[0] )
    else :
        print('+++ intpvolcano +++')
        print('No gridtype recognized')
        quit()
#
#   final field : 12 identical month
    if (   gridtype == 'latlon'    ) : 
        finalfield=np.zeros((ntime,nlev1,nlat1,nlon1), dtype=float)
        for itime in range(0,ntime):
            finalfield[itime,:,:,:] = newfield[:,:,:]
    elif ( gridtype == 'irregular' ) : 
        finalfield=np.zeros((ntime,nlev1,ncol1), dtype=float)
        for itime in range(0,ntime):
            finalfield[itime,:,:] = newfield[:,:]
    else :
        print('+++ intpvolcano +++')
        print('No gridtype recognized')
        quit()


#   data structure
    data = { 'activity'   : 'volc', \
             'sector'     : sector, \
             'species'    : species, \
#
             'field'      : finalfield, \
             'units'      : 'kg m-3 s-1', \
#
             'area'       : area, \
             'area_units' : 'm2', \
#
             'longitude'  : longitude, \
             'latitude'   : latitude, \
             'resolution' : resolution, \
             'levbnds'    : levbnds, \
             'lev_units'  : 'km', \
             'dim'        : '3d', \
             'ntime'      : ntime}  
#
#   write out globl total (as a check)
    a = checkglobaltotal.checkglobaltotal(D=data)

    return data
