import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleh0oceanfield

'''
REMARK
	tempeatures [K] -> converted to []  

'''


def readsingleoceanfield( expid, var, date):
#-----------------------
    print('+++ readsingleoceanfield +++')
    print('date : '+date)
    print('--- readsingleoceanfield ---')

#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    chem=expidinfo['chem']

#   two options
    D = readsingleh0oceanfield.readsingleh0oceanfield(expid=expid,var=var,date=date)

    return D

