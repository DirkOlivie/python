import haversine

def xlonxlat2icol(longitude, latitude, xlon, xlat) :
#------------
    '''
    MODIFICATIONS
        (2025-10-18) creation

    '''
    if ( len(longitude) != len(latitude) ) :
        print('+++ xlonxlat2icol +++')
        print('Longitude and latitude have different size : ', len(longitude), len(latitude))
        quit()    
    ncol=len(longitude)

    icolfound=-1
    dmin=1.e20

#   loop over all columns
    for icol in range(0,ncol) :

        d = haversine.haversine_distance(lat1=latitude[icol], \
                                         lon1=longitude[icol], \
                                         lat2=xlat, \
                                         lon2=xlon)

        if ( d < dmin) :
            dmin = d
            icolfound=icol
#
    if ( icolfound < 0 ) :
        print('+++ xlonxlat2icol +++')
        print('No nearest point found ...')
        quit()
#
    return icolfound
