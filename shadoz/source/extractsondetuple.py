import numpy as np


def extractsondetuple (S, xvar, yvar):
#---------------------------------------
    '''
    MODIFICATIONA
        (2024-02-19) creation

    INPUT
        sonde : costarica_20120608T17_SHADOZV06.dat
        xvar  : Time, Press, GeopAlt, Temp, RH, O3_mPa, O3_ppmv, O3_DU, Wind_Dir, Wind_Spd, TPump, O3CellI, GPS_Lon, GPS_Lat, GPS_Alt
        yvar  :

    '''
#
#   extract station from sonde
    iposx=S['varlist'].index(xvar)
    iposy=S['varlist'].index(yvar)
            
# 
    sondedata={'xvar'       : xvar, \
               'xunit'      : S['unitlist'][iposx], \
               'xlist'      : S['data'][iposx,:], \
               'yvar'       : yvar, \
               'yunit'      : S['unitlist'][iposy], \
               'ylist'      : S['data'][iposy,:], \
               'latitude'   : S['latitude'], \
               'longitude'  : S['longitude']}
#    
    return sondedata
