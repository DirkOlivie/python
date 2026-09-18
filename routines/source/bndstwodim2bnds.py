import numpy as np

def bndstwodim2bnds(lowerbnds, upperbnds) :
#--------------------
    '''
    INPUT
        lowerbnds
        upperbnds

    RETURN

    '''
    nlow=len(lowerbnds)
    nhgh=len(upperbnds)
#
    if ( nlow != nhgh ) :
        print('+++ bndstwodim2bnds +++')
        print('lower bounds and upper bounds have different size : ', nlow, nhgh)
        quit()

    n = nlow

#   check whether 
    for i in range(1,n-1) :
        if ( lowerbnds[i+1] != upperbnds[i] ) :
            print('+++ bndstwodim2bnds +++')
            print('lower bounds[i+1] and upper bounds[i] are different : ', lowerbnds[i+1], upperbnds[i])
            quit()    
#
    bnds = np.zeros((n+1), dtype=float)

    bnds[0:n] = lowerbnds[0:n]
    bnds[  n] = upperbnds[n-1]
#
    return bnds
