import numpy as np

import readsingleoceancolumnintegral
import readsingleoceanfield

"""
HISTORY
	(2022-01-04) Added possibility to read CLM files/variables

METHOD
	1. standard  2D fields
	2. extract surface layer of 3D field
	3. make column burden of 3D field


"""

def readsingleoceanmap( expid, var, date):
#---------------------
    print('+++ readsingleoceanmap +++')
    print('date : '+date)
    print('--- readsingleoceanmap ---')
#
#   experiment info
#   
    if ( '_columnburden' in var ) : 
        line    = var.split("_columnburden")
        varorig = line[0].strip()
        data = readsingleoceancolumnintegral.readsingleoceancolumnintegral(expid=expid, var=varorig, date=date)
    else : 
        data = readsingleoceanfield.readsingleoceanfield(expid=expid, var=var, date=date)
#
#   return data
#
    return data

