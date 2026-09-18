import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import season2monthnumberlist
import getmonthlength


def fillzonalmeanstatistics(data, season, year0=None, year1=None):
#--------------------------
    '''
    MODIFICATIONS
        2026-04-25 : creation
        2026-07-23 : had to add calendar keyword in call to getmonthlength

    '''
    monthlist=season2monthnumberlist.season2monthnumberlist(season=season)


#   1. limiting the data to year0-year1
    if ( year0 == None and year1 == None ) :
        year0=np.amin(data['yearlist'])
        year1=np.amax(data['yearlist'])
    elif ( year0 != None and year1 != None ) :
        data = shortenzonalmeanseries.shortenzonalmeanseries(data=data, year0=year0,year1=year1) # shorten the timeseries data set
    else :
        print('+++ fillzonalmeanstatistics +++')
        print('year0 and year1 not coherent : ', year0, year1)
        quit()

    nyear=year1-year0+1

#   2. make annual samples (average within season)
    nlat=data['nlat']

    tmpvaluelist=np.zeros((nyear,nlat), dtype=float)

    for iyear in range(nyear) : 
        year=year0+iyear

        totalweight=0.

        for month in monthlist :
            
            weight=getmonthlength.getmonthlength(month=month, year=0, calendar='noleap')
            totalweight = totalweight + weight

            isubset = ( data['yearlist'] == year ) * (data['monthlist'] == month )

            tmpvaluelist[iyear,:] = tmpvaluelist[iyear,:] + data['valuelist'][isubset,:] * weight

        tmpvaluelist[iyear,:] = tmpvaluelist[iyear,:] / totalweight

            
#   3. do the statistics
    Ex    = np.mean(tmpvaluelist             , axis=0)
    Exx   = np.mean(tmpvaluelist*tmpvaluelist, axis=0)
    sigma = np.sqrt(Exx-Ex*Ex)
    error = sigma/np.sqrt(float(nyear))    

#   OUTPUT STRUCTURE
    outputdata={'expid'        : data['expid'], \
                'variable'     : data['variable'], \
                'units'        : data['units'], \
                'fileorigin'   : data['fileorigin'], \
                'areaunits'    : data['areaunits'], \
                'year0'        : year0, \
                'year1'        : year1, \
                'season'       : season, \
                'valuelist'    : Ex, \
                'latitude'     : data['latitude'], \
                'nlat'         : data['nlat'], \
                'area'         : data['area'], \
                'areafraction' : data['areafraction'], \
                'areatotal'    : data['areatotal'], \
                'region'       : data['region']}
#
    return outputdata
