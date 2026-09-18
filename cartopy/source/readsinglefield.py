import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleh0field
import getsingleexternalfield

'''
REMARK
	tempeatures [K] -> converted to []  

'''


def readsinglefield( expid, var, date):
#------------------
    print('+++ readsinglefield +++')
    print('date : '+date)
    print('var : '+var)
    print('--- readsinglefield ---')

#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    chem=expidinfo['chem']

#   two options
    if ( False \
        and chem == '' \
        and ( var == 'OH' or var == 'HO2' or var == 'O3' or var == 'NO3' ) \
        and ( expid != 'NHISTfrc2_f09_tn14_20191025' ) )  :
        D= getsingleexternalfield.getsingleexternalfield(expid=expid,var=var,date=date, climtype='oxidant')
    elif ( var == 'ozone_extclim' ) :
        D= getsingleexternalfield.getsingleexternalfield(expid=expid,var='O3',date=date, climtype='ozone')
    else :
        D = readsingleh0field.readsingleh0field(expid=expid,var=var,date=date)

    return D

