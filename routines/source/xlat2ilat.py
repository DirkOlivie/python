import numpy as np

def xlat2ilat (latbnds, xlat) :
#------------
    '''
    MODIFICATIONS
        (2024-03-10)

    '''

    nlat = len(latbnds) - 1

    ilatfound=-1

    for ilat in range(0,nlat) :

        latmin=np.amin([latbnds[ilat], latbnds[ilat+1]])
        latmax=np.amax([latbnds[ilat], latbnds[ilat+1]])

        if ( latmin <= xlat and xlat <= latmax ) : ilatfound = ilat

#   final check
    if ( ilatfound == -1 ) :
        print('latbnds = ', latbnds)
        print('nlat = ', nlat)
        print('No latitude grid found for xlat : ', xlat)
        quit()

    print('latbnds = ', latbnds)
    print('xlat = ', xlat)
    print('ilat = ', ilat)

    return ilatfound
