import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/curtainzonal/source')
import readzonalseries

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import season2monthnumberlist

def readmeanzonalmeanline(expid,  var, year0, year1, season, region):
#-------------------------
    '''
    INPUT
        expid
        var
        year0
        year1
        season
        region

    CALLS
        readzonalseries

    '''
    debug=0

#   read the data between 
    a = readzonalseries.readzonalseries(expid=expid, variable=var, typevar=region, year0=year0, year1=year1) # variable can be a composite variables

#   contributing months
#    if   ( season == 'JAN' ) : monthlist=[1]
#    elif ( season == 'FEB' ) : monthlist=[2]
#    elif ( season == 'MAR' ) : monthlist=[3]
#    elif ( season == 'APR' ) : monthlist=[4]
#    elif ( season == 'MAY' ) : monthlist=[5]
#    elif ( season == 'JUN' ) : monthlist=[6]
#    elif ( season == 'JUL' ) : monthlist=[7]
#    elif ( season == 'AUG' ) : monthlist=[8]
#    elif ( season == 'SEP' ) : monthlist=[9]
#    elif ( season == 'OCT' ) : monthlist=[10]
#    elif ( season == 'NOV' ) : monthlist=[11]
#    elif ( season == 'DEC' ) : monthlist=[12]
#
#    elif ( season == 'YEA' ) : monthlist=[1,2,3,4,5,6,7,8,9,10,11,12]
#
#    elif ( season == 'MAM' ) : monthlist=[3,4,5]
#    elif ( season == 'JJA' ) : monthlist=[6,7,8]
#    elif ( season == 'SON' ) : monthlist=[9,10,11]
#    elif ( season == 'DJF' ) : monthlist=[1,2,12]
#    else : exit()
    monthlist= season2monthnumberlist. season2monthnumberlist(season=season)
#
#   average over all years (only the correct ones have been read) and months
    
    b = np.zeros(a['nlat'])
    ncount=0
    for itime in range(0,a['ntime']) :
        if ( a['monthlist'][itime] in monthlist ) :
             b[:]= b[:] + a['valuelist'][itime,:]
             ncount = ncount + 1    

    if ( ncount != 0 ) : 
        b = b / float(ncount)
    else :
        print('Division by 0 as ncount : ', ncount)
        quit()

    if ( debug == 1 ) :
        print('+++ readmeanzonalmeanline +++')
        print('latitude : ', a['latitude'])
        print('values   : ', b)  
        print('size : ', len(a['latitude']), len(b))

#   new structure
    data={'expid'      : a['expid'], \
          'variable'   : a['variable'], \
          'units'      : a['units'], \
          'fileorigin' : a['fileorigin'], \
          'areaunits'  : a['areaunits'], \
          'year0'      : year0, \
          'year1'      : year1, \
          'season'     : season, \
          'valuelist'  : b, \
          'latitude' : a['latitude'], \
          'nlat'     : a['nlat'], \
          'area'     : a['area'], \
          'areafraction' : a['areafraction'], \
          'areatotal': a['areatotal'], \
          'region' : a['region']}

#   return
    return data
