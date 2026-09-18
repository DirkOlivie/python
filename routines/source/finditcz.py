import numpy as np

def finditcz(data, lon0):
#-----------
    '''


    '''
    nlon=len(data['longitude'])

    positionlist=np.zeros(nlon, dtype=float)

    print(data['latitude'])

    isubset = ( data['latitude'] >= - 20. ) * ( data['latitude'] <= 20. )

    for ilon in range(nlon) :

        positionlist[ilon] = np.sum(data['field'][isubset,ilon]*data['latitude'][isubset]) \
                           / np.sum(data['field'][isubset,ilon]                          )

        
    x = data['longitude']
    y = positionlist

#   
    x= ( (x - lon0) + 720 ) % 360 + lon0  # renaming / applying module
    y=y[np.argsort(x)]
    x.sort()


    newdata = { 'x' : x, \
                'y' : y, \
                'x_units' : 'degrees_east', \
                'y_units' : 'degrees_west' }

    return newdata
