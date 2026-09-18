import numpy as np

def lon2lonbnds( longitude ) :
#--------------
#
    nlon = len(longitude)

    lonbnds =np.zeros(nlon+1,dtype=float)

#   standard 
    lonbnds[1:nlon] = 0.5 * (longitude[0:nlon-1] + longitude[1:nlon] )

#   poles
    lonbnds[0]    = lonbnds[1]      - ( lonbnds[2]      - lonbnds[1]      )
    lonbnds[nlon] = lonbnds[nlon-1] + ( lonbnds[nlon-1] - lonbnds[nlon-2] )
#
    print('+++ lon2lonbnds +++')
    print('longitude = ', longitude)
    print('longbnds  = ', lonbnds)


#
    return lonbnds
