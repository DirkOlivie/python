import numpy as np

def hybnds2hy(hybnds) :
#------------
    '''
    INPUT
        hybnds : 2-dim array ; can be a-values or b-values

    RETURN
        hy : 1-dim array [latbnds]

    MODIFICATIONS
        (2025-05-28) creation
    '''

#   check
#    print('+++ hybnds2hy +++')
#    print('hbnds (shape) : ', hybnds.shape)
#    print('hybnds : ', hybnds)
 
    nlev,nbnds= hybnds.shape

    if ( nbnds != 2 ) :
        print('+++ hybnds2hy +++') 
        print('nbnds should be 2 but is : ', nbhds)
        quit()
    
    if ( not np.array_equal(hybnds[1:nlev,0],hybnds[0:nlev-1,1]) ):
        print('+++ hybnds2hy +++')
        print('hybnds[1:nlev,0] != hybnds[0:nlev-1,1] : ' )
        print(hybnds)        
        quit()

    hy=np.zeros(nlev+1)

    hy[0:nlev] = hybnds[0:nlev,0]
    hy[nlev]   = hybnds[nlev-1,1]

    return hy
