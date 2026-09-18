#import math
import numpy as np
#from netCDF4 import Dataset

#import experimentdefinition
import readsingleh0field

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/aerotabread/source')

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits
import getmolarweight

'''
REMARK

'''


def calculatesinglefield_vmr_from_mmr( expid, var, date):
#####################################
    '''
    MODIFICATIONS
        (2026-07-03) : addition for O3 and ozone
    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_vmr_from_mmr +++')
    print('date : '+date)
#
#   constant
    Rair  =287.058
#
#   allowed variables
    if   ( var == 'CO2_as_vmr' ) : origspecies='CO2'
    elif ( var == 'CH4_as_vmr' ) : origspecies='CH4'
    elif ( var == 'N2O_as_vmr' ) : origspecies='N2O'
    else                         : 
        print('No var recognized : '+var)
        quit() 
#
#   obtain mmr : units = [kg/kg] probably
    data = readsingleh0field.readsingleh0field(expid=expid,var=origspecies,date=date) # read original species, e.g., CO2
    units_mmr = getstandardunits.getstandardunits(units=data['units'])
    if ( units_mmr.strip() != 'kg kg-1' ) :
        print('Units not recognized : '+units_mmr)
        print('Units should be : kg kg-1 (or equivalent, e.g : kg/kg, ...)')
        quit()
#
#   calculate volume mixing ratio
    vmr = data['field'] * 28.97 / getmolarweight.getmolarweight(origspecies)

#   units
    units='mole mole-1'
#
#   create structure
    data = { 'field'     : vmr, \
             'longitude' : data['longitude'], \
             'latitude'  : data['latitude'], \
             'nlon'      : data['nlon'], \
             'nlat'      : data['nlat'], \
             'units'     : units, \
             'p0'        : data['p0'], \
             'ps'        : data['ps'], \
             'hyai'      : data['hyai'], \
             'hybi'      : data['hybi'], \
             'hyam'      : data['hyam'], \
             'hybm'      : data['hybm'], \
             'units_ps'  : data['units_ps'], \
             'units_p0'  : data['units_p0'], \
             'nlev'      : data['nlev']}
#
    print('MIN - MAX')
    print(np.min(vmr))
    print(np.max(vmr))
    print('--- calculatesinglefield_vmr_from_mmr ---')
#
    return data
