import math
import numpy as np
from netCDF4 import Dataset

import experimentdefinition
#import readsingleh0field
import readsinglefield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getmolarweight
import getstandardunits

'''
REMARK

'''


def calculatesinglefield_partpress_from_vmr( expid, var, date):
###########################################    
    '''
    MODIFICATIONS
        (2024-03-10) : creation     
        (2024-04-29) : replaced readsingleh0field by readsinglefield
    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_partpress_from_vmr +++')
    print('date : '+date)
#
    if   ( var == 'O3_as_partpress'    ) : cvar='O3'
    elif ( var == 'ozone_as_partpress' ) : cvar='ozone'
    elif ( var == 'ozone_extclim_as_partpress' ) : cvar='ozone_extclim'
    elif ( var == 'm_O3_c_as_vmr_as_partpress' ) : cvar='m_O3_c_as_vmr'
    elif ( var == 'm_ozone_c_as_vmr_as_partpress' ) : cvar='m_ozone_c_as_vmr'
    elif ( var == 'SO2_as_partpress' ) : cvar='SO2'
    elif ( var == 'H2SO4_as_partpress' ) : cvar='H2SO4'
    else :
        print('No var recognized : '+var)     
        quit()        

#   obtain vmr : units = [mol/mol] probably
#   vmr = readsingleh0field.readsingleh0field(expid=expid,var=cvar,date=date)
    vmr = readsinglefield.readsinglefield(expid=expid,var=cvar,date=date)
    units_vmr = vmr['units']
    units_vmr=getstandardunits.getstandardunits(units=units_vmr) # standard way of writing, e.g. : mol/mol -> mol mol-1

    if ( units_vmr.strip() != 'mol mol-1' ) :
        print('Units not recognized : '+units_vmr)
        print('Units should be : mol mol-1')
        quit()
#
#   dimensions
    nlev, nlat, nlon = vmr['field'].shape

#   calculate pressure
    pressure = np.zeros([nlev,nlat,nlon])
    for ilev in range(0,nlev) :
        pressure[ilev,:,:] = vmr['hyam'][ilev] * vmr['p0'] + vmr['hybm'][ilev] * vmr['ps'][:,:] # mid-level pressure

#        for ilat in range(0,nlat) :
#            for ilon in range(0,nlon) :
#               pressure                  
#                pressure[ilev,ilat,ilon]    = vmr['hyam'][ilev] * vmr['p0'] + vmr['hybm'][ilev] * vmr['ps'][ilat,ilon]           # mid-level pressure

#   partial pressure
    partpress = vmr['field'] * pressure

#   units
    units='Pa'
#
#   create structure
    data = { 'field'     : partpress, \
             'longitude' : vmr['longitude'], \
             'latitude'  : vmr['latitude'], \
             'nlon'      : vmr['nlon'], \
             'nlat'      : vmr['nlat'], \
             'units'     : units, \
             'p0'        : vmr['p0'], \
             'ps'        : vmr['ps'], \
             'hyai'      : vmr['hyai'], \
             'hybi'      : vmr['hybi'], \
             'hyam'      : vmr['hyam'], \
             'hybm'      : vmr['hybm'], \
             'units_ps'  : vmr['units_ps'], \
             'units_p0'  : vmr['units_p0'], \
             'nlev'      : vmr['nlev']}
#
    print('MIN - MAX')
    print(np.amin(partpress))
    print(np.amax(partpress))
    print('--- calculatesinglefield_partpress_from_vmr ---')
#
    return data
