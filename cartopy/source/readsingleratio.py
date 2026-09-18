import numpy as np
from netCDF4 import Dataset

import readsinglemap

'''
REMARK

'''


def readsingleratio( expid, var, date):
#--------------------------------------   
    '''
    MODIFICATIONS
        (2022-09-16) : creation     
    '''
#----------------------------------------------------------------
#
    print('+++ readsingleratio +++')
    print('date : '+date)
#
#
    if ( var == 'CHBR3_ratioextrapolate00mTOsurfacelayer') : varteller = 'CHBR3_extrapolate00m' ; varnoemer = 'CHBR3_surfacelayer'
    else :
        print('Readsingleratio : no variable recognized : '+var)
        quit()
#
#   read teller ; read noemer
    T=readsinglemap.readsinglemap(expid=expid, var=varteller, date=date)
    N=readsinglemap.readsinglemap(expid=expid, var=varnoemer, date=date)
#
#   read noemer (pointwise division)
    fractionfield=T['field'] / N['field']
#
    print(T['field'])
    print(N['field'])
    print(fractionfield)
#
#   return data 
    newdata = { 'field'     : fractionfield, \
                'longitude' : T['longitude'], \
                'latitude'  : T['latitude'], \
                'nlon'      : T['nlon'], \
                'nlat'      : T['nlat'], \
                'units'     : T['units'] }
#
    print('--- readsingleratio ---')
#
    return newdata
