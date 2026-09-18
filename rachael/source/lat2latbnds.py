import numpy as np

def lat2latbnds(latitude, skiptest=0) :
#--------------
    '''
    INPUT
        latitude : 1-dim array [nlat]

    RETURN
       latbnds : 1-dim array [latbnds]

    MODIFICATIONS
        (2022-11-01 ) added skiptest keyword : for latitude ranges that do not cover the whole [-90,90] range, but, e.g., only [45,90]
            WRONGLY IMPLEMENTED : default should be "skiptest=0" instead of "skiptest=1"
        (20223-01-10) corrected : now         
    '''

#   check 
    if ( np.absolute(np.sum(latitude)) > 5.e-4 ):
        print, 'Latitude not correct ...'
        print, 'Sum is : ', np.sum(latitude)
        print, 'First latitude = ', latitude(0)
        print, 'Last  latitude = ', latitude(-1)
        print, latitude
        if ( skiptest != 1 ) :
            quit()
     
    nlat = len(latitude)
    latbnds =np.zeros(nlat+1,dtype=float)

#   standard points
    latbnds[1:nlat] = 0.5 * (latitude[0:nlat-1] + latitude[1:nlat] )

#   poloes
    if ( skiptest == 1 ) :
#       extrapolation - maybe does not end nicely on -90 and +90, but needed if only limited range, e.g., [45,90]    
        latbnds[0]    = latbnds[1]      - ( latbnds[2]      - latbnds[1]      )
        latbnds[nlat] = latbnds[nlat-1] + ( latbnds[nlat-1] - latbnds[nlat-2] )
#
    else :
#       impose exactly -90 and +90 values    
        if ( ( latitude[1] - latitude [0] ) > 0. ) :
            latbnds[0]    = -90.
            latbnds[nlat] =  90.
        elif ( ( latitude[1] - latitude [0] ) < 0. ) :
            latbnds[0]    =  90.
            latbnds[nlat] = -90.
        else :        
           print(latitude)
           print('Latitudes seem strange')
           quit()
#
    print('+++ lat2latbnds +++')
    print('latitude = ', latitude)
    print('latbnds  = ', latbnds)    

    return latbnds
