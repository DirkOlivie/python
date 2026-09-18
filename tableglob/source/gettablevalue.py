import numpy as np
import math

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import readseries

def gettablevalue (expid, var, year0, year1, season, stattype) :
#----------------
    '''
    MODIFICATIONS
	(2021-11-27) : creation
        (2023-11-07) : added keyword stattype : 'mean', 'standard_deviation', 'error_on_mean'
        (2024-04-26) : allowed for vartype (NH, SH, 28S28N, ...) in var : cb_O3-29S28N
            selection is done on presence of "-"

    INPUT
        expid
        var
        year0
        year1
        season
        stattype

    RETURNS
        series of annual values (for specific season)
        units
    '''

    print('+++ gettablevalue +++')
    print('expid = ', expid)
    print('var   = ', var)
    print('year0 = ', year0)
    print('year1 = ', year1)
    print('season= ', season)
    print('--- gettablevalue ---')
#
#   seperate variable and typevar (if present)
    line=var.split('-')
    if ( len(line) == 1 ) :
        varorig=var
        typevar=''
    elif ( len(line) == 2 ) :
        varorig=line[0]
        typevar=line[1]
    else :
        print('Not able to split var+typevar : ', var)
        quit()
         
#   contributing months
    if   ( season == 'JAN' ) : monthlist=[1]
    elif ( season == 'FEB' ) : monthlist=[2]
    elif ( season == 'MAR' ) : monthlist=[3]
    elif ( season == 'APR' ) : monthlist=[4]
    elif ( season == 'MAY' ) : monthlist=[5]
    elif ( season == 'JUN' ) : monthlist=[6]
    elif ( season == 'JUL' ) : monthlist=[7]
    elif ( season == 'AUG' ) : monthlist=[8]
    elif ( season == 'SEP' ) : monthlist=[9]
    elif ( season == 'OCT' ) : monthlist=[10]
    elif ( season == 'NOV' ) : monthlist=[11]
    elif ( season == 'DEC' ) : monthlist=[12]

    elif ( season == 'YEA' ) : monthlist=[1,2,3,4,5,6,7,8,9,10,11,12]

    elif ( season == 'MAM' ) : monthlist=[3,4,5]
    elif ( season == 'JJA' ) : monthlist=[6,7,8]
    elif ( season == 'SON' ) : monthlist=[9,10,11]
    elif ( season == 'DJF' ) : monthlist=[1,2,12]
    else : exit()

#   read the timeseries
#   a = readseries.readseries(expid=expid, variable=var, typevar='')
    a = readseries.readseries(expid=expid, variable=varorig, typevar=typevar)

#   summing/averaging over correct years and seasons
    yearlist = np.zeros(year1-year0+1)

    for month in monthlist :
        yearlist = yearlist + a["valuelist"][ ( a["yearlist"] >= year0 ) & ( a["yearlist"] <= year1) & (a["monthlist"] == month ) ]

    yearlist = yearlist / float(len(monthlist))

#   do the statistics  

#    if   ( stattype == 'mean'               ) : total = yearlist.sum() / float(year1-year0+1)
#    elif ( stattype == 'standard_deviation' ) : total = yearlist.std() 
#    elif ( stattype == 'error_on_mean'      ) : total = yearlist.std() / np.sqrt(float(year1-year0+1))
#    else : 
#        print('No stattype recognized : '+stattype)
#        print('--- gettablevalue ---')
#        quit()

#   conversion for ozone : Tg -> DU
    units = a['units']
    
    if ( ( varorig == 'cb_O3'              \
        or varorig == 'O3_columnburden'    \
        or varorig == 'O3_columnburden_belowtropopause' \
        or varorig == 'O3_columnburden_abovetropopause' \
        or varorig == 'ozone_columnburden' 
        or varorig == 'ozone_columnburden_belowtropopause' 
        or varorig == 'ozone_columnburden_abovetropopause' ) and units == 'Tg') :
        factor = 1.e9 / ( 4. * math.pi *6.37e6 * 6.37e6) * 1. / 2.1415e-5 * a['areaglob'] / a['area']
        newunits='DU'
    else :
        factor = 1.
        newunits=units

#    total = total * factor
    yearlist = yearlist * factor

#    return total, units 
    return yearlist, units
