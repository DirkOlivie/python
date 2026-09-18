import numpy as np

def fitconstantseries (data) :
#--------------------
    '''
    MODIFICATIONS

    INPUT
        data
    '''
#
    newvaluelist=np.zeros((data['ntime']))
    newvaluelist[:]=np.mean(data['valuelist'])


# create a dictionary
    data={'expid'      : data['expid'], \
          'variable'   : data['variable'], \
          'units'      : data['units'], \
          'fileorigin' : data['fileorigin'], \
          'area'       : data['area'], \
          'areaglob'   : data['areaglob'], \
          'areaunits'  : data['areaunits'], \
          'yearlist'   : data['yearlist'], \
          'monthlist'  : data['monthlist'], \
          'timelist'   : data['timelist'], \
          'valuelist'  : newvaluelist,\
          'ntime'      : data['ntime']}
#
    return data
