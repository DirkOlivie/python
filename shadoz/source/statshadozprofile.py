import numpy as np

def statshadozprofile( D ):
#-------------------------
    '''
    INPUT
        D : list of structures

    OUTPUT
        structure

    MODIFICATIONS
        (2024-02-21) creation

    '''

# get sondelist
    nsonde=len(D)

    n = len(D[0]['xlist'])

    ymin    = np.zeros(n,dtype=float) + float('nan')
    ymax    = np.zeros(n,dtype=float) + float('nan')
    ymean   = np.zeros(n,dtype=float) + float('nan')
    ymedian = np.zeros(n,dtype=float) + float('nan')
    yq25    = np.zeros(n,dtype=float) + float('nan')
    yq75    = np.zeros(n,dtype=float) + float('nan')

#
#    print(D[0]['xlist'][:])

 
    for i in range(0,n) : # loop over all the altitudes in the profile

        y = np.zeros(nsonde,dtype=float)

        for isonde in range(0,nsonde) : # loop over all sondes (at specific altitude)
                
            y[isonde] = D[isonde]['ylist'][i] # complete array    

 #       print(y)

        y = y[y < 1.e29]  # subselection to eliminate 'nan'

        if ( len(y) > 0 ) : 

            ymin[i]    = np.min(y)
            ymax[i]    = np.max(y)
            ymean[i]   = np.mean(y)
            ymedian[i] = np.median(y)
            yq25[i]    = np.quantile(y,0.25)
            yq75[i]    = np.quantile(y,0.75)

# return the data
    data={'xvar'       : D[0]['xvar' ], \
          'xunit'      : D[0]['xunit'], \
          'xlist'      : D[0]['xlist'][:], \
          'xbndlist'   : D[0]['xbndlist'][:], \
           \
          'yvar'       : D[0]['yvar' ], \
          'yunit'      : D[0]['yunit'], \
          'ymean'      : ymean     , \
          'ymin'       : ymin     , \
          'ymax'       : ymax     , \
          'ymedian'    : ymedian  , \
          'yq25'       : yq25     , \
          'yq75'       : yq75     , \
           \
          'latitude'   : D[0]['latitude' ], \
          'longitude'  : D[0]['longitude']}
#
    return data
