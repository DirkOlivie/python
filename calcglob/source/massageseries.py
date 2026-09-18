import numpy as np

def massageseries(data, year0, nyear) :
#--------------------------------------
    '''
    MODIFICATIONS
        (2022-05-08) : creation
        (2025-10-28) : added timelist 
    '''
#    
    iset = ( data['yearlist'] >= year0 ) & ( data['yearlist'] <= (year0 + nyear -1) )  
#   
    valuelist=data['valuelist'][iset]
    valuelist[:]=np.mean(valuelist)
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
    print('+++ massageseries ++++')
    print('data[yearlist][0] : ')
    print(data['yearlist'][0])
    print('year0 : ')
    print(year0)
#
    return newdata
