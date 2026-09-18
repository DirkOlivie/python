import numpy as np
#
def lev2levbnds(level, imposelower=None):
#--------------
    '''
    REMARK 
       Can impose 

    INPUT
        level : array of mid-level values
        imposelower (optional) : explicit value can be given


    RETURN
        the half-level (boundary) values

    '''
    nlev = len(level)
    levbnds =np.zeros((nlev+1), dtype=float)

#
    levbnds[1:nlev] = 0.5 * ( level[0:nlev-1] + level[1:nlev] )

#   
    levbnds[0] = levbnds[1] - ( levbnds[2] - levbnds[1] )
    levbnds[nlev] = levbnds[nlev-1] + ( levbnds[nlev-1] - levbnds[nlev-2] )
#
    direction = abs( level[nlev-1]-level[0] ) / ( level[nlev-1] - level[0] )
#
    if ( imposelower != None ) :
        if ( direction > 0. ) : #  bvb : [0 m, 100 m, 300 m, ...] or [10 hPa, 50 hPa, ... ]
            levbnds[0] = imposelower
            if ( levbnds[0] > levbnds[1] ) :
                print('levbnds[0] is larger than levbnd[1] : ')
                print('levbnds[0] : ', levbnds[0])
                print('levbnds[1] : ', levbnds[1])    
                quit()
        elif ( direction < 0. ) : # ; bvb : [35 km, 32km , 27 km, ...] or [1000 hPa, 950 hPa, 850 hPa, 700 hPa... ]
            levbnds[nlev] = imposelower
            if ( levbnds(nlev) > levbnds(nlev-1) ) :
                print('levbnds[nlev] is larger than levbnd[nlev-1] : ')
                print('levbnds[nlev] : ', levbnds[nlev])
                print('levbnds[nlev-1] : ', levbnds[nlev-1])
                quit()
        else :
            print('No diretion recognized')
            quit()
#
    return levbnds
