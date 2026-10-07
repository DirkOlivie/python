import numpy as np
import getemissionprofile

def expandfield(D, sector, activity):
#--------------
    '''
     MODIFICATIONS
    	(2019-07-01) : added possibility of FORE to have regionally different vertical profiles
        (2025-10-18) : added time dimension
        (2026-09-29) : added yearlist, monthlist to return structure

    CALLS
	    getemissionprofile
    '''
#-----------------------------------------------
#   get profile info
    P = getemissionprofile.getemissionprofile(activity=activity, sector=sector)

#   get longitudes/latitudes 
    nlon=len(D['longitude'])
    nlat=len(D['latitude'])
    ntime=D['ntime']

    newfield = np.zeros((ntime,P['nlev'],nlat,nlon))

#   check units
    if ( D['units'] != 'kg m-2 s-1' ) :
        print('Units different from kg m-2 s-1 : ', D['units'])
        quit()

#   calculate expanded field
    if ( sector != 'FORE' ) :

         for ilev in range (0,P['nlev']) : 

            newfield[:,ilev,:,:] = D['field'] \
                               * P['profileweight'][ilev] \
                               / abs(P['altitude_int'][ilev+1]-P['altitude_int'][ilev]) \
                               / 1000. 

     

    else :  # sector = 'FORE'

        P_DEFO = getemissionprofile.getemissionprofile(activity=activity, sector='DEFO')
        P_TEMF = getemissionprofile.getemissionprofile(activity=activity, sector='TEMF')
        P_BORF = getemissionprofile.getemissionprofile(activity=activity, sector='BORF')
 
        for ilat in range(0,nlat) :
        
            if (   abs(D['latitude'][ilat]) <= 30. ) : P_local=P_DEFO # tropics : 30S--30N
            elif ( abs(D['latitude'][ilat]) <= 60. ) : P_local=P_TEMF # extra tropics : 60S--30S and 30N--60N        
            else                                     : P_local=P_BORF # high latitudes : 90S--60S and 60N--90N

            for ilev in range(0,P['nlev']) :

                # km-1 m-2 -> m-3
                newfield[:,ilev,ilat,:] = D['field'][:,ilat,:] \
                                        * P_local['profileweight'][ilev] \
                                        / abs(P_local['altitude_int'][ilev+1]-P_local['altitude_int'][ilev]) \
                                        / 1000.                                                        

#   data structure
    data = { 'activity'       : D['activity'], \
             'sector'         : D['sector'], \
             'species'        : D['species'], \
#
             'field'          : newfield, \
             'units'          : 'kg m-3 s-1', \
#
             'area'           : D['area'], \
             'area_units'     : D['area_units'], \
#
             'longitude'      : D['longitude'], \
             'latitude'       : D['latitude'], \
             'altitude'       : P['altitude'], \
             'altitude_int'   : P['altitude_int'], \
             'altitude_units' : 'km', \
             'dim'            : '3d', \
#
             'yearlist'       : D['yearlist'], \
             'monthlist'      : D['monthlist'], \
             'ntime'          : D['ntime']} 
  
    return data
