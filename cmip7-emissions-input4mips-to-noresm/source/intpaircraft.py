import numpy as np

import checkglobaltotal
import getgridtype

import sys 
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lon2lonbnds
import lat2latbnds
import intplev
import intpfieldregular
import intpfieldirregular

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-volc/source')
import readareatopography

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction
#
#
def intpaircraft(D, longitude, latitude, resolution, levbnds, filelocation):
#---------------
    '''
    REMARK 
	    1) takes into account topography of NorESM
            original grid : 0, 0.610, 1.220, 1.830, 2.440, 3.050, 3.660, ... ABOVE SEALEVEL
            final grid    : 0, 0.610, 1.220, 1.830, 2.440, 3.050, 3.660, ... ABOVE LOCAL TOPOGRAPHY
                  
                  [original grid]                                [final grid]           
            ...   --------------------
                                                           1.220 ------------------
            1.830 ---------------------   
                                                           0.610 ------------------
            1.220 ---------------------   
                                                           0.000 ------------------
            0.610 ---------------------                         ///\\\///\\\///\\\ 

            0.000 --------------------- (sealevel)
                   ---
                    -

        2) order of interpolation :
            first horizontal interpolation (still on equal height grid)
            second vertical interpolation

    INPUT
        D : structure containing 
            field
            units : kg m-2 s-1 [INTEGRATED OVER LAYER THICKNESS]    
            longitude
            latitude
            levbnds
        longitude [NEW]
        latitude  [NEW]
        levbnds   [the new levels] :  0, 0.610, 1.220, 1.830, 2.440, 3.050, 3.660,  4.270,  4.880,  5.490,  6.100,
                                      6.710, 7.320, 7.930, 8.540, 9.150, 9.760, 10.370, 10.980, 11.590, 12.200,
                                      12.810,13.420,14.030,14.640,15.250]) # km

    RETURN structure containing
        field
        units
        longitude
        latitude
        levbnds
        levunits

    CALLS
	    readareatopography
        lat2latbnds
	    lon2lonbdns
	    intpfieldregular

    MODIFICATIONS
        (2025-10-18) Extension to irregular grid
        (2026-09-29) Added yearlist and monthlist in output structure

    '''

#   check units
    if ( D['units'] != 'kg m-2 s-1' ) : 
        print('Units not recognized : ', D['units'])
        quit()

#   initial resolution
    nlon0=len(D['longitude'])
    nlat0=len(D['latitude'])
    nlev0=len(D['levbnds'])-1

    ntime=D['ntime']
#
#   final resolution
    gridtype=getgridtype.getgridtype(resolution=resolution)
    if ( gridtype == 'latlon' ) :
        nlon1=len(longitude)
        nlat1=len(latitude)
    elif ( gridtype == 'irregular' ) :
        ncol1 = len(longitude) 

    nlev1=len(levbnds)-1
#
#   read topography for final resoultion 
    topography = readareatopography.readareatopography(grid=resolution, variable='topography', filelocation=filelocation) # [m]
#
#   convert topography to [km]
    topography = topography / 1000. # [m -> km]
#
#   AREAD OF FINAL RESOLUTION
#   area [in m2]
    if (   gridtype == 'latlon'    ) : area=areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='area')
    elif ( gridtype == 'irregular' ) : area=readareatopography.readareatopography(grid=resolution, variable='area', filelocation=filelocation)
    else :
        print('+++ intpvolcano +++')
        print('No gridtype recognized')
        quit()

#   BOUNDARIES
#   orig
    latbnds0=lat2latbnds.lat2latbnds(latitude =D['latitude'])
    lonbnds0=lon2lonbnds.lon2lonbnds(longitude=D['longitude'])
#   final
    if ( gridtype == 'latlon' ) :
        latbnds1=lat2latbnds.lat2latbnds(latitude =latitude)
        lonbnds1=lon2lonbnds.lon2lonbnds(longitude=longitude)
#
#   original field in intrinsic units
    infield=np.zeros((ntime,nlev0,nlat0,nlon0), dtype=float)
    for ilev in range(0,nlev0) :
        infield[:,ilev,:,:] = D['field'][:,ilev,:,:] / abs( D['levbnds'][ilev+1] - D['levbnds'][ilev] ) \
                                           / 1000.   # /km -> /m
    units='kg m-3 s-1'
#
#   new field
    if   ( gridtype == 'latlon'    ) : newfield = np.zeros((ntime,nlev1,nlat1,nlon1), dtype=float)
    elif ( gridtype == 'irregular' ) : newfield = np.zeros((ntime,nlev1,ncol1      ), dtype=float)   
    else : 
        print('+++ intpaircraft +++')
        print('No gridtype = ', gridtype)
        quit() 
    
#
#   horizontal interpolation [KEEP VERTICAL UNCHANGED]
    if   ( gridtype == 'latlon'   ) : tmpfield = intpfieldregular.intpfieldregular(infield=infield, latinbd=latbnds0, latoutbd=latbnds1, loninbd=lonbnds0, lonoutbd=lonbnds1, levinbd=D['levbnds'], levoutbd=D['levbnds'])
    elif ( gridtype == 'irregular' ) : tmpfield = intpfieldirregular.intpfieldirregular(infield=infield, latin=D['latitude'], latout=latitude, lonin=D['longitude'], lonout=longitude, filelocation=filelocation, levinbd=D['levbnds'], levoutbd=D['levbnds'])
    else : 
        print('+++ intpaircraft +++')
        print('No gridtype = ', gridtype)
        quit()
        
#   vertical interpolation
    print('starting vertical interpolation ...')

    if ( gridtype == 'latlon' ) : 
        for ilon1 in range(0,nlon1) :
    
            for ilat1 in range(0,nlat1) :
    
    #           only if there are emissions in that gridpoint
                if ( np.sum(tmpfield[:,:,ilat1,ilon1]) != 0. ) :
    
                    tmplevbnds    = levbnds+topography[ilat1,ilon1]  # 0, 0.610, 1.220, 1.830, 2.440, ... are increased by the topography
                    tmplevbnds[0] = 0.                               # lowest layer is kept at sealevel
    
                    ilev0=0  # index original grid
                    ilev1=0  # index final grid
    
                    while ( ilev0 < nlev0 and ilev1 < nlev1 ) :
    
                        zmin = max([tmplevbnds[ilev1], D['levbnds'][ilev0]]) # the highest of the lower boundaries
                        zmax = min([tmplevbnds[ilev1+1], D['levbnds'][ilev0+1]]) # the lowest of the higher boundaries
    
                        if ( zmax - zmin > 0. ) :
    #
                            newfield[:,ilev1,ilat1,ilon1] = newfield[:,ilev1,ilat1,ilon1]+ tmpfield[:,ilev0,ilat1,ilon1] * (zmax - zmin) / ( tmplevbnds[ilev1+1] - tmplevbnds[ilev1] )
    
    #                       move one with lowest toplevel up
                            if ( D['levbnds'][ilev0+1] <= tmplevbnds[ilev1+1] ) :
                                ilev0=ilev0+1
                            else :
                                ilev1=ilev1+1
    
                        else :
    #                       move one with lowest downlevel up
                            if ( D['levbnds'][ilev0] <= tmplevbnds[ilev1] ) :
                                ilev0=ilev0+1
                            else : 
                                ilev1=ilev1+1

#                   rescale lowest layer to its thinner value
                    newfield[:,0,ilat1,ilon1] = newfield[:,0,ilat1,ilon1] * ( tmplevbnds[1] - 0. ) / ( levbnds[1] - levbnds[0] )
#
    elif ( gridtype == 'irregular' ) : 
        for icol1 in range(0,ncol1) :

#           only if there are emissions in that gridpoint
            if ( np.sum(tmpfield[:,:,icol1]) != 0. ) :

                tmplevbnds    = levbnds+topography[icol1]  # 0, 0.610, 1.220, 1.830, 2.440, ... are increased by the topography
                tmplevbnds[0] = 0.                         # lowest layer is kept at sealevel

                ilev0=0  # index original grid
                ilev1=0  # index final grid

                while ( ilev0 < nlev0 and ilev1 < nlev1 ) :

                    zmin = max([tmplevbnds[ilev1], D['levbnds'][ilev0]]) # the highest of the lower boundaries
                    zmax = min([tmplevbnds[ilev1+1], D['levbnds'][ilev0+1]]) # the lowest of the higher boundaries

                    if ( zmax - zmin > 0. ) :
#
                        newfield[:,ilev1,icol1] = newfield[:,ilev1,icol1]+ tmpfield[:,ilev0,icol1] * (zmax - zmin) / ( tmplevbnds[ilev1+1] - tmplevbnds[ilev1] )

#                       move one with lowest toplevel up
                        if ( D['levbnds'][ilev0+1] <= tmplevbnds[ilev1+1] ) :
                            ilev0=ilev0+1
                        else :
                            ilev1=ilev1+1

                    else :
#                       move one with lowest downlevel up
                        if ( D['levbnds'][ilev0] <= tmplevbnds[ilev1] ) :
                            ilev0=ilev0+1
                        else : 
                            ilev1=ilev1+1

#               rescale lowest layer to its thinner value
                newfield[:,0,icol1] = newfield[:,0,icol1] * ( tmplevbnds[1] - 0. ) / ( levbnds[1] - levbnds[0] )

# final data structure
    data = { 'activity'   : D['activity'], \
             'sector'     : D['sector'], \
             'species'    : D['species'], \
#              
             'field'      : newfield, \
             'units'      : 'kg m-3 s-1', \
#
             'area'       : area, \
             'area_units' : 'm2', \
#
             'longitude'  : longitude, \
             'latitude'   : latitude, \
             'resolution' : resolution, \
#
             'levbnds'    : levbnds, \
             'lev_units'  : 'km', \
#
             'dim'        : '3d', \
             'yearlist'   : D['yearlist'], \
             'monthlist'  : D['monthlist'], \

             'ntime'      : ntime}  
#
    globaltotal=checkglobaltotal.checkglobaltotal(D=data)
#
    return data
