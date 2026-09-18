import numpy as np
import statistics


def standardizesondetuple (S):
#-----------------------------
    '''
    MODIFICATIONA
        (2024-02-19) creation

    INPUT
        sonde : costarica_20120608T17_SHADOZV06.dat
        xvar  : Time, Press, GeopAlt, Temp, RH, O3_mPa, O3_ppmv, O3_DU, Wind_Dir, Wind_Spd, TPump, O3CellI, GPS_Lon, GPS_Lat, GPS_Alt
        yvar  :

    '''
#
#   find boundaries
    if ( S['xvar'] == 'Press' ) :
       xa=1013.25 #
       xb=   1.0  #
    elif ( S['xvar'] == 'GeopAlt' ) : 
       xa=0.
       xb=40.
    else :
       print('No xvar recognized : ' + xvar) 
       quit()
#
#   define array for xvalues
    n=30
    n=60      # number of intervals
    if ( S['xvar'] == 'Press' ) :
        xbndlist=np.geomspace(xa,xb,num=n+1)
        x0=statistics.geometric_mean(xbndlist[0:2])
        x1=statistics.geometric_mean(xbndlist[-2:])
        xlist=np.geomspace(x0,x1,num=n)
    elif ( S['xvar'] == 'GeopAlt' ) : 
        dx = (xb-xa) / float(n) 
        xlist    = np.arange(0,n,1,dtype=float)*dx + xa + dx/2.   # mid points     
        xbndlist = np.arange(0,n+1,1,dtype=float)*dx + xa         # boundaries
    else :
        print('No variable recognized : ', S['xvar'])    
        quit()



#   define array for yvalues
    ylist=np.zeros(n, dtype=float)+float('nan')
#
#   interpolation : equal weight to all contributions in interval
    for i in range(0,n) : 
        xmin=np.min((xbndlist[i],xbndlist[i+1]))
        xmax=np.max((xbndlist[i],xbndlist[i+1]))

        mask0 = np.where(S['xlist'] >= xmin,1,0)
        mask1 = np.where(S['xlist'] <  xmax,1,0)

        mask = mask0*mask1
        if (sum(mask) > 0 ) :
            ylist[i] = sum(S['ylist']*mask) / sum(mask)
        else :
            ylist[i] = float('nan')          

#   return
    sondedata={'xvar'       : S['xvar' ], \
               'xunit'      : S['xunit'], \
               'xlist'      : xlist     , \
               'xbndlist'   : xbndlist  , \
               'yvar'       : S['yvar' ], \
               'yunit'      : S['yunit'], \
               'ylist'      : ylist     , \
               'latitude'   : S['latitude' ], \
               'longitude'  : S['longitude']}
#           
    return sondedata
