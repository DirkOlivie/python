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


def calculatesinglefield_vmr_from_layermass( expid, var, date):
#------------------------------------------
    '''
    MODIFICATIONS
        (2023-07-10) : creation     
        (2024-04-30) : addition for O3 and ozone
        (2026-09-07) : addded 'gridtype' in datastructure
    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_vmr_from_layermass +++')
    print('date : '+date)
#
#   constant
    Rair  =287.058
#
#   allowed variables
    if   ( var == 'm_CO2_c_as_vmr' )       : clayermass='m_CO2_c'       ; molarweight_species='CO2' ; mixing=''
    elif ( var == 'm_CH4_c_as_vmr' )       : clayermass='m_CH4_c'       ; molarweight_species='CH4' ; mixing=''
    elif ( var == 'm_N2O_c_as_vmr' )       : clayermass='m_N2O_c'       ; molarweight_species='N2O' ; mixing=''
    elif ( var == 'm_CFC11_c_as_vmr' )     : clayermass='m_CFC11_c'     ; molarweight_species='CFC11' ; mixing=''
    elif ( var == 'm_CFC11STAR_c_as_vmr' ) : clayermass='m_CFC11STAR_c' ; molarweight_species='CFC11' ; mixing=''
    elif ( var == 'm_CFC12_c_as_vmr' )     : clayermass='m_CFC12_c'     ; molarweight_species='CFC12' ; mixing=''
    elif ( var == 'm_O3_c_as_vmr' )        : clayermass='m_O3_c'        ; molarweight_species='O3' ; mixing=''
    elif ( var == 'm_ozone_c_as_vmr' )     : clayermass='m_ozone_c'     ; molarweight_species='ozone' ; mixing=''

    elif ( var == 'm_CO2_c_as_vmr_drytest' )       : clayermass='m_CO2_c'       ; molarweight_species='CO2'    ; mixing='drytest'
    elif ( var == 'm_CH4_c_as_vmr_drytest' )       : clayermass='m_CH4_c'       ; molarweight_species='CH4' ; mixing='drytest'
    elif ( var == 'm_N2O_c_as_vmr_drytest' )       : clayermass='m_N2O_c'       ; molarweight_species='N2O' ; mixing='drytest'
    elif ( var == 'm_CFC11_c_as_vmr_drytest' )     : clayermass='m_CFC11_c'     ; molarweight_species='CFC11' ; mixing='drytest'
    elif ( var == 'm_CFC11STAR_c_as_vmr_drytest' ) : clayermass='m_CFC11STAR_c' ; molarweight_species='CFC11' ; mixing='drytest'
    elif ( var == 'm_CFC12_c_as_vmr_drytest' )     : clayermass='m_CFC12_c'     ; molarweight_species='CFC12' ; mixing='drytest'
    elif ( var == 'm_O3_c_as_vmr_drytest' )        : clayermass='m_O3_c'        ; molarweight_species='O3' ; mixing='drytest'
    elif ( var == 'm_ozone_c_as_vmr_drytest' )     : clayermass='m_ozone_c'     ; molarweight_species='ozone' ; mixing='drytest'


    else                                 : 
        print('No var recognized : '+var)
        quit() 
#
#   obtain layermass : units = [kg/m^2] probably
    layermass = readsingleh0field.readsingleh0field(expid=expid,var=clayermass,date=date)
    units_layermass = getstandardunits.getstandardunits(units=layermass['units'])
    if ( units_layermass.strip() != 'kg m-2' ) :
        print('Units not recognized : '+units_mmr)
        print('Units should be : kg m-2 (or equivalent, e.g : kg/m2, kg/m^2, ...)')
        quit()
#
#   obtain layer mass
    airmass = readsingleh0field.readsingleh0field(expid=expid,var='AIRMASSL',date=date) # temperature
    units_airmass = getstandardunits.getstandardunits(units=airmass['units'])
    if ( units_airmass.strip() != 'kg m-2' ) :
        print('Units not recognized : '+units_airmass)
        print('Units should be : g m-2 (or equivalent, e.g : kg/m2, kg/m^2, ...)')
        quit()
#
#   obtain humidity
    if ( mixing == 'drytest' ) :
        q = readsingleh0field.readsingleh0field(expid=expid,var='Q',date=date) # temperature
        units_q = getstandardunits.getstandardunits(units=q['units'])
        if ( units_q.strip() != 'kg kg-1' ) :
            print('Units not recognized : '+units_q)
            print('Units should be : kg kg-1 (or equivalent, e.g : kg/kg, 1, ...)')
            quit()
    elif ( mixing == '' ) : 
        print('ok')
    else : 
        print('Mixing not recognized : '+mixing)
        quit()

#   obtain surface pressure
    units_ps = layermass['units_ps']
    if ( units_ps.strip() != 'Pa' ) :
        print('Units not recognized : '+units_ps)
        print('Units should be : Pa')
        quit()
#
#   dimensions
    nlev, nlat, nlon = layermass['field'].shape

#   calculate volume mixing ratio
    vmr = layermass['field'] / airmass['field'] * 28.97 / getmolarweight.getmolarweight(molarweight_species)

#   correcting for dry mass
    if ( mixing == 'drytest' ) :
        vmr = vmr / (1. - q['field'])
    
#   units
    units='mole mole-1'
#
#   create structure
    data = { 'field'     : vmr, \
             'longitude' : layermass['longitude'], \
             'latitude'  : layermass['latitude'], \
             'nlon'      : layermass['nlon'], \
             'nlat'      : layermass['nlat'], \
             'units'     : units, \
             'p0'        : layermass['p0'], \
             'ps'        : layermass['ps'], \
             'hyai'      : layermass['hyai'], \
             'hybi'      : layermass['hybi'], \
             'hyam'      : layermass['hyam'], \
             'hybm'      : layermass['hybm'], \
             'units_ps'  : layermass['units_ps'], \
             'units_p0'  : layermass['units_p0'], \
             'nlev'      : layermass['nlev'], \
             'gridtype'  : layermass['gridtype'], \
             'area'      : layermass['area'], \
             'area_units': layermass['area_units']}
#
    print('MIN - MAX')
    print(np.min(vmr))
    print(np.max(vmr))
    print('--- calculatesinglefield_vmr_from_layermass ---')
#
    return data
