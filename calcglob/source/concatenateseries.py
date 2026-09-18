import re
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def concatenateseries (D0, D1) :
#--------------------    
    '''
    MODIFICATIONS
        (2025-06-25) : skip overlapping period : D1 has priority

    '''
#
# check whether variable, units, area, areaglob, areaunits are the same
    if ( D0['variable'] != D1['variable'] \
      or D0['units'] != D1['units'] \
      or D0['fileorigin'] != D1['fileorigin'] \
      or D0['area'] != D1['area'] \
      or D0['areaglob'] != D1['areaglob'] \
      or D0['areaunits'] != D1['areaunits'] ) : 
        print('Experiment data can not be concatenated : ')
        print(D0['variable'], D1['variable'])
        print(D0['units'], D1['units'])
        print(D0['fileorigin'], D1['fileorigin'])
        print( D0['area'], D1['area'])
        print(D0['areaglob'], D1['areaglob'])
        print(D0['areaunits'], D1['areaunits']) 
        quit()
#
# try to find overlap
    iset=np.where(D0['timelist'] < D1['timelist'][0])

# create a dictionary
    data={'expid'      : D0['expid'], \
          'variable'   : D0['variable'], \
          'units'      : D0['units'], \
          'fileorigin' : D0['fileorigin'], \
          'area'       : D0['area'], \
          'areaglob'   : D0['areaglob'], \
          'areaunits'  : D0['areaunits'], \
          'yearlist'   : np.concatenate((D0['yearlist'][iset] ,D1['yearlist'])), \
          'monthlist'  : np.concatenate((D0['monthlist'][iset],D1['monthlist'])), \
          'timelist'   : np.concatenate((D0['timelist'][iset] ,D1['timelist'])), \
          'valuelist'  : np.concatenate((D0['valuelist'][iset],D1['valuelist'])),\
          'ntime'      : len(D0['valuelist'][iset])+D1['ntime']}
#
    return data
