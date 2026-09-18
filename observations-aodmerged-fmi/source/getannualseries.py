import numpy as np

import season2monthnumberlist

def getannualseries(data, season):
#-------------------
    '''
    INPUT
        data   : timeseries data
        season : which season you want to average over

    RETURN
       structure containing seasonal cyccle
               var
               Ex
               Exx
               sigma
               Emin            
               Emax

    CALLED BY
        analyseseries
 
    CALLS 

    '''
#------------------------------------------------------------
#
    nmonth=12
#
    year0=np.min(data['yearlist'])
    year1=np.max(data['yearlist'])

    nyear=year1-year0+1

    ntime=nmonth*nyear
#
#   new data
    valuelist=np.zeros(nyear, dtype=float)
    masklist=np.zeros(nyear,dtype=float)
    yearlist=np.arange(year0,year1+1, dtype=int)  # [year0, year0 + 1, year0 + 2, ..., year1]
    timelist=yearlist

#   subselect on year and season
    for iyear in range(0,nyear) :

        year=yearlist[iyear]

#       subselect on year
        iset = ( data['yearlist'] == year )   #[ False, False, ..., True, True, ..., False, False, ...]
        valuesublist = data['valuelist'][iset]
        masksublist  = data['masklist'][iset]

#       subselect on season
        iset = np.array(season2monthnumberlist.season2monthnumberlist(season=season)) - 1  
        valuesublist = valuesublist[iset]
        masksublist  = masksublist[iset]

#       valuelist
        valuelist[iyear] = np.sum ( valuesublist * masksublist) / np.sum (masksublist)
        masklist[iyear]  = np.sum (                masksublist) / float(len(masksublist)) 

    outputdata = { 'var'       : data['var'], \
                   'region'    : data['region'], \
                   'units'     : data['units'], \
                   'valuelist' : valuelist, \
                   'masklist'  : masklist, \
                   'yearlist'  : yearlist, \
                   'timelist'  : timelist, \
                   'season'    : season} 
#
    return outputdata
