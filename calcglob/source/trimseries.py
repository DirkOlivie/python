import numpy as np

def trimseries(data) :
#-------------
    '''
    MODIFICATIONS
        (2025-10-28) : remove incomplete initial and final year
    '''
#    
    ntime=data['ntime']

#   begin     
    month0 = data['monthlist'][0]
    year0  = data['yearlist'][0]
    if ( month0 != 1 ) : 
        year0 = year0 + 1
        print('+++ trimseries +++ : shortening timeseries to have complete first year')

#   end
    month1 = data['monthlist'][-1]
    year1  = data['yearlist'][-1]
    if ( month1 != 12 ) : 
        year1 = year1 - 1
        print('+++ trimseries +++ : shortening timeseries to have complete last year')


    if ( year0 > year1 ) :
        print('+++ trimseries +++')
        print('No remaining years between year0 and year1 : ', year0, year1)
        quit()


    iset = ( data['yearlist'] >= year0 ) & ( data['yearlist'] <= year1 )  
#   
    valuelist=data['valuelist'][iset]
#
    newdata={'expid'      : data['expid'], \
             'variable'   : data['variable'], \
             'units'      : data['units'], \
             'fileorigin' : data['fileorigin'], \
             'area'       : data['area'], \
             'areaglob'   : data['areaglob'], \
             'areaunits'  : data['areaunits'], \
             'yearlist'   : data['yearlist'][iset], \
             'monthlist'  : data['monthlist'][iset], \
             'timelist'   : data['timelist'][iset], \
             'valuelist'  : valuelist, \
             'ntime'      : len(data['valuelist'][iset])}
#
    return newdata
