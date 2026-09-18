import math
import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleh0field

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getmolarweight
import getstandardunits

'''
REMARK

'''


def calculatesinglefield_conc_from_vmr( expid, var, date):
######################################    
    '''
    MODIFICATIONS
        (2024-01-18) : creation     
        (2026-07-03) : extension to SO2 and H2SO4
    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_conc_from_vmr +++')
    print('date : '+date)
#
#   constant
    Rair  =287.058
# 

#   allowed variables
    if   ( var == 'CHBR3_as_concentration' ) : cvmr='CHBR3'
    elif ( var == 'SO2_as_concentration'   ) : cvmr='SO2'
    elif ( var == 'H2SO4_as_concentration' ) : cvmr='H2SO4'
    else :
        print('Var not recognize : ', var)
        quit()

#
#   obtain vmr : units = [mol/mol] probably
    vmr = readsingleh0field.readsingleh0field(expid=expid,var=cvmr,date=date)
    units_vmr = vmr['units']
    units_vmr=getstandardunits.getstandardunits(units=units_vmr) # standard way of writing, e.g. : mol/mol -> mol mol-1

    if ( units_vmr.strip() != 'mol mol-1' ) :
        print('Units not recognized : '+units_vmr)
        print('Units should be : mol mol-1')
        quit()
#
#   obtain temperature (surface pressure is part of this field)
    t = readsingleh0field.readsingleh0field(expid=expid,var='T',date=date) # temperature
    units_t = t['units']
    if ( units_t.strip() != 'K' ) :
        print('Units not recognized : '+units_t)
        print('Units should be : K')
        quit()
    units_ps = t['units_ps']
    if ( units_ps.strip() != 'Pa' ) :
        print('Units not recognized : '+units_ps)
        print('Units should be : Pa')
        quit()
#
#   dimensions
    nlev, nlat, nlon = vmr['field'].shape

#   calculate air density
    rho = np.zeros([nlev,nlat,nlon])
    for ilev in range(0,nlev) :
        for ilat in range(0,nlat) :
            for ilon in range(0,nlon) :
#               pressure                  
                p    = t['hyam'][ilev] * t['p0'] + t['hybm'][ilev] * t['ps'][ilat,ilon]           # mid-level pressure
#               density                
                rho[ilev,ilat,ilon]  = p / Rair / t['field'][ilev,ilat,ilon]  
#
#   molar weight
    Mw_air =28.97
    Mw=getmolarweight.getmolarweight(var=cvmr)

#   calculate concentration
    conc = vmr['field'] * Mw / Mw_air * rho  

#   units
    units='kg m-3'
#
#   create structure
    data = { 'field'     : conc, \
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
    print(np.amin(conc))
    print(np.amax(conc))
    print('--- calculatesinglefield_conc_from_vmr ---')
#
    return data
