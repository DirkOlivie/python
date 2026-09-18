import numpy as np

import interp1d

def interp3dzlev20(field,zfield, zunits) :
#-------------------------------
#
    '''
    MODIFICATIONS
        (2025-05-21) creation

    '''

    nlev, nlat, nlon = field.shape
#
    zlevlist = [ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, \
                10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5 ]
    zlevunits = 'km'

    if ( zlevunits == 'km' and zunits == 'm' ) :
        factor = 0.001
    else :
        print('Incompatible units :')
        print('zlevunits : ', zlevunits)
        print('zunits    : ', zunits) 
        quit()

    nlev20 = len(zlevlist) # number of levels

    newfield=np.zeros((nlev20,nlat,nlon), dtype=float)
#
    for ilat in range(0,nlat) :
        for ilon in range(0,nlon) :
            x = zfield[:,ilat,ilon] * factor  # m2 s-2 -> m -> km
            y = np.array(zlevlist)
            fx = field[:,ilat,ilon]

            newfield[:,ilat,ilon] = interp1d.interp1d(x=x, y=y,fx=fx)
#
    return newfield
