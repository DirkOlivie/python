import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import season2monthnumberlist
import getmonthlength


def fillstatistics (data, freqtype, year0=None, year1=None) :
#-----------------    
    '''
    MODIFICATIONS	
        2022-07-07 : allows for monthly frequency
            modified terminology
                'timelist' (instead of year_annavg)                
                'valuelist' (instead of 'value_seasonavg')
                'ntime' (instead of 'nyear')
        2022-09-01 :    
        2025-10-16 : annual/seasonal mean takes correct number of days in month into account

    INPUT 
        data                : structure as read by readseries
        freqtype            : 'YEA','JAN','FEB', ..., 'DJF', 'MAM', ...
                              'monthly'
                              'seasonalcycle'
        year0    [optional] :
        year1    [optional] : 

    '''    
    nmonth=12

#   1. limiting the data to year0-year1
    if ( year0 == None and year1 == None ) :
        year0=np.amin(data['yearlist'])
        year1=np.amax(data['yearlist'])
    elif ( year0 != None and year1 != None ) :
        data = shortenseries.shortenseries(data=data, year0=year0,year1=year1) # shorten the timeseries data set
    else : 
        print('+++ fillstatistics +++')
        print('year0 and year1 not coherent : ', year0, year1)
        quit()
#
#   2.a monthly [KEEP ALL THE DATA]
    if ( freqtype == 'monthly' ) :
#       
#       data to be used
        timelist  = data['timelist']
        valuelist = data['valuelist']
        ntime     = len(data['timelist'])
#
#   2.b seasonal cycle
    elif ( freqtype == 'seasonalcycle' ) :
        timelist=np.arange(0,nmonth)   # months-array [0,1,2,3,...,11]

#       data to be used
        valuelist=np.zeros(nmonth)           # Ex
        valuelist_Exx=np.zeros(nmonth)       # Exx
        valuelist_sigma=np.zeros(nmonth)     # sigma
#
        for imonth in range(0,nmonth) :
#
            month=imonth+1
#
            boolarr = ( data['monthlist'] == month )
#
            valuelist[imonth]       = np.mean(data['valuelist'][boolarr])
            valuelist_Exx[imonth]   = np.mean(data['valuelist'][boolarr]*data['valuelist'][boolarr])
            valuelist_sigma[imonth] = np.sqrt(valuelist_Exx[imonth]-valuelist[imonth]*valuelist[imonth])

#   2.c creating seasonal mean timeseries
    elif ( freqtype in ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                        'MAM','JJA','SON','DJF', \
                        'YEA' ] ) :
#
#       months contributing to a season
        monthlist=season2monthnumberlist.season2monthnumberlist(season=freqtype) # monthlist has values between 1 and 12 
        ncontribution=len(monthlist)
        
#       nyear = year1-year0+1 (only works if consecutive years in series)
        ntime     = len(data['timelist'])
        nyear     = ntime // nmonth

        print('nyear : ', nyear)

#       timelist=np.arange(year0,year1+1)
        timelist=np.zeros(nyear,dtype=int)
        timelist[:] = data['yearlist'][::nmonth] # sample only first month

        valuelist=np.zeros(nyear,dtype=float)

        totalweight=0.

        for month in monthlist : # accumulating over all contributing months; month has values between 1 and 12

            weight=getmonthlength.getmonthlength(month=month, year=0, calendar='noleap')
            totalweight = totalweight + weight

            boolarr = ( data['monthlist'] == month )
            valuelist[:] = valuelist[:] + data['valuelist'][boolarr] * weight # weight with length of month

#
#        valuelist = valuelist / float(ncontribution)   
        valuelist = valuelist / float(totalweight)   
#  
    else :
        print('+++ fillstatistics +++')
        print('No freqtype recognized : ', freqtype)
        quit()    

# 3. some additional statistics
    ntime=len(valuelist)    
    Ex   = np.mean(valuelist)
    Exx  = np.mean(valuelist*valuelist)
    sigma = np.sqrt(Exx-Ex*Ex)
    error = sigma/np.sqrt(float(ntime))    

#
#   OUTPUT STRUCTURE
    outdata = { 'expid'    : data['expid'], \
                'variable' : data['variable'], \
                'units'    : data['units'], \
                'freqtype' : freqtype, \
                'area'     : data['area'], \
                'areaglob' : data['areaglob'], \
                'timelist' : timelist, \
                'valuelist': valuelist, \
                'ntime'    : len(valuelist), \
#                additional statistics                  
                'Ex'       : Ex, \
                'Exx'      : Exx, \
                'sigma'    : sigma, \
                'error'    : error}
#
    return outdata
