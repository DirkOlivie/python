import numpy as np

def statmodelprofile( D ):
#-------------------------
    '''
    INPUT
        D :

    OUTPUT
        data [structure]

    MODIFICATIONS
        (204-02-21) creation

    '''

# get sondelist
    nsonde=len(D)

    n = len(D[0]['valuelist'])

    ymin=np.zeros(n,dtype=float) + float('nan')
    ymax=np.zeros(n,dtype=float) + float('nan')
    ymean=np.zeros(n,dtype=float) + float('nan')
    ymedian=np.zeros(n,dtype=float) + float('nan')
    yq25=np.zeros(n,dtype=float) + float('nan')
    yq75=np.zeros(n,dtype=float) + float('nan')

#
#    print(D[0]['zlist'][:])

 
    for i in range(0,n) : # loop over all the altitudes in the profile

        y = np.zeros(nsonde,dtype=float)

        for isonde in range(0,nsonde) : # loop over all sondes (at specific altitude)
                
            y[isonde] = D[isonde]['valuelist'][i] # complete array    

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
    data={'xvar'       : D[0]['verticalaxis' ], \
          'xunit'      : D[0]['zunits'], \
          'xlist'      : D[0]['zlist'][:], \
#          'xbndlist'   : D[0]['zbndlist'][:], \   maybe not needed
           \
          'yvar'       : D[0]['var' ], \
          'yunit'      : D[0]['units'], \
          'ymean'      : ymean    , \
          'ymin'       : ymin     , \
          'ymax'       : ymax     , \
          'ymedian'    : ymedian  , \
          'yq25'       : yq25     , \
          'yq75'       : yq75     , \
           \
          'latitude'   : D[0]['xlat' ], \
          'longitude'  : D[0]['xlon']}
#
    return data
