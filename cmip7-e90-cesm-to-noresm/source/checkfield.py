import numpy as np

def checkfield(field) :
#-------------
    '''


    '''
    nmonth = 12

    ntime, nlat, nlon = field.shape


    for itime in range(ntime) :

        if ( np.max( np.abs( field[itime,:,:] - field[itime % nmonth,:,:] ) ) != 0. ) :
            print('+++ checkfield +++')
            print('Not all year are equal')
            quit()          
        else :
            print('checkfield : ', np.max(field[itime,:,:]))

