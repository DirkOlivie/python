import numpy as np

def shortenzonalmeanseries(data, year0, year1) :
#-------------------------
    '''
    MODIFICATIONS

    INPUT
        D0
        year0 
        year1
    '''
#
    boolarr =np.logical_and( (data['yearlist'] >= year0 ) , ( data['yearlist'] <= year1 ) )

# create a dictionary
    data={'expid'      : data['expid'], \
          'variable'   : data['variable'], \
          'units'      : data['units'], \
          'fileorigin' : data['fileorigin'], \
          'area'       : data['area'], \
          'areaglob'   : data['areaglob'], \
          'areaunits'  : data['areaunits'], \
          'yearlist'   : data['yearlist'][boolarr], \
          'monthlist'  : data['monthlist'][boolarr], \
          'timelist'   : data['timelist'][boolarr], \
          'valuelist'  : data['valuelist'][boolarr],\
          'ntime'      : len(data['valuelist'][boolarr])}
#
    return data
