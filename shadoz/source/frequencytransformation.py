import numpy as np

def frequencytransformation(D, representationtype):
#--------------------------
    '''
    MODIFICATIONS
        (2024-03-05)

    INPUT
        D : inputdatastructure
        representationtype : 'seasonal_cycle' | 'series_annual' | 'series_monthly' | 'series_seasonal'

    RETURN
        
    '''
#
    if ( representationtype == D['representationtype'] ) : 
        data = D  

#   series_monthly -> series_annual
    elif ( D['representationtype'] == 'series_monthly' \
       and representationtype        == 'series_annual' ) :

        year0=np.min(D['yearlist'])
        year1=np.max(D['yearlist'])
        nyear=year1-year0+1
        yearlist=np.arange(year0,year1+1,1)            
        valuelist=np.zeros(nyear,dtype=int)
        for iyear in range(0,nyear) : 
            year=yearlist[iyear]
            mask = np.where(D['yearlist'] == year,1,0)
            valuelist[iyear] = np.sum(mask * D['valuelist'])
#
        data={'yearlist' : yearlist, \
              'timelist' : yearlist, \
              'valuelist' : valuelist, \
              'representationtype' : representationtype}
#
#   series_monthly -> seasonal_cycle
    elif ( D['representationtype'] == 'series_monthly' \
       and representationtype      == 'seasonal_cycle') :
        
        nmonth=12
        monthlist=np.arange(1,nmonth+1,1)
        valuelist=np.zeros(nmonth,dtype=int)
        for imonth in range(0,nmonth) :
            month=monthlist[imonth]
            mask = np.where(D['monthlist'] == month,1,0)
            valuelist[imonth] = np.sum(mask * D['valuelist']) 

        data={'monthlist' : monthlist, \
              'timelist'  : monthlist, \
              'valuelist' : valuelist, \
              'representationtype' : representationtype}
#   non-recognized combinations
    else :

        print('No transformation recognized : ')
        print('from ' + D['representationtype'])
        print('to   ' + representationtype)   
        quit()

    return data
