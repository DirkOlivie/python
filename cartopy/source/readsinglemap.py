import numpy as np

import readsinglesurfacelayer
import readsinglecolumnintegral
import readsingleextrapolatetosurface
import readsingleratio
import readsinglefield

"""
HISTORY
	(2022-01-04) Added possibility to read CLM files/variables

METHOD
	1. standard  2D fields
	2. extract surface layer of 3D field
	3. make column burden of 3D field


"""

def readsinglemap( expid, var, date):
#----------------
    print('+++ readsinglemap +++')
    print('date : '+date)
    print('var  : '+var)
    print('--- readsinglemap ---')
#
#   experiment info
#   
    if ( '_surfacelayer' in var )   : 
        line    = var.split("_surfacelayer")
        varorig = line[0].strip()
        data    = readsinglesurfacelayer.readsinglesurfacelayer(expid=expid, var=varorig, date=date)    
    elif ( '_columnburden' in var ) : 
        line    = var.split("_columnburden")
        varorig = line[0].strip()
        data = readsinglecolumnintegral.readsinglecolumnintegral(expid=expid, var=varorig, date=date)
    elif ( '_extrapolate' in var ) :
        data = readsingleextrapolatetosurface.readsingleextrapolatetosurface(expid=expid, var=var, date=date)
    elif ( '_ratio' in var ) :
        data = readsingleratio.readsingleratio(expid=expid, var=var, date=date)
    else : 
        data = readsinglefield.readsinglefield(expid=expid, var=var, date=date)
#
#   return data
#
    return data

