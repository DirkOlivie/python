def xlon2ilon(lonbnds, xlon) :
#------------
    '''
    MODIFICATIONS
        (2024-03-10) creation

    '''
    nlon=len(lonbnds)-1

    dx = 360. / float(nlon)

    ilonfound=-1

    for ilon in range(0,nlon):

        if ( ( ( xlon            + 720. - lonbnds[ilon] ) % 360. ) <= dx * 1.1 \
         and ( ( lonbnds[ilon+1] + 720. - xlon          ) % 360. ) <= dx * 1.1 ) : ilonfound=ilon

#   final check
    if ( ilonfound == -1 ) :
        print('No longitude grid found')
        quit()

#
    return ilonfound
