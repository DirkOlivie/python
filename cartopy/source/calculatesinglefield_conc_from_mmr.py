import math
import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleh0field

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits

'''
REMARK

'''


def calculatesinglefield_conc_from_mmr( expid, var, date):
######################################    
    '''
    MODIFICATIONS
        (2023-01-19) : creation    
        (2024-06-28) : initially only for num_a1, num_a2, num_a2 and num_a4
            now also extended                        

    INPUT
        var : num_a1_as_concentration -> num_a1
              num_a2_as_concentration -> num_a2
              num_a3_as_concentration -> num_a3
              num_a4_as_concentration -> num_a4

              mmr_BC_as_concentration ->   

    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_conc_from_mmr +++')
    print('date : '+date)
#
#   constant
    Rair  =287.058
#
#   allowed variables
    if ( '_as_concentration' in var )   :
        line = var.split("_as_concentration")
        cmmr = line[0].strip()
    else : 
        print('No variable recognized : ', var)
        print('Should contain _as_concentration')  
        quit()
#
#   obtain mmr : units = [#/kg] or [kg kg-1]probably
    mmr = readsingleh0field.readsingleh0field(expid=expid,var=cmmr,date=date)
    units_mmr = getstandardunits.getstandardunits(mmr['units'])
    if ( units_mmr.strip() != 'kg-1' \
     and units_mmr.strip() != 'kg kg-1' ) :
        print('Units not recognized : '+units_mmr)
        print('Units should be : kg-1 or  kg kg-1')
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
    nlev, nlat, nlon = mmr['field'].shape

#   calculate air density
    rho = np.zeros([nlev,nlat,nlon])
    for ilev in range(0,nlev) :
        for ilat in range(0,nlat) :
            for ilon in range(0,nlon) :
#               pressure                  
                p    = t['hyam'][ilev] * t['p0'] + t['hybm'][ilev] * t['ps'][ilat,ilon]           # mid-level pressure
#               density                
                rho[ilev,ilat,ilon]  = p / Rair / t['field'][ilev,ilat,ilon]  

#   calculate concentration
    conc = mmr['field'] * rho  

#   units
    if ( units_mmr == 'kg-1' ) : units='m-3'
    elif ( units_mmr == 'kg kg-1' ) : units='kg m-3'
    else : 
        print('Units not recognized : ', mmr_units)
        print('Units should be : kg-1 or kg kg-1')
        quit()
#
#   create structure
    data = { 'field'     : conc, \
             'longitude' : mmr['longitude'], \
             'latitude'  : mmr['latitude'], \
             'nlon'      : mmr['nlon'], \
             'nlat'      : mmr['nlat'], \
             'units'     : units, \
             'p0'        : mmr['p0'], \
             'ps'        : mmr['ps'], \
             'hyai'      : mmr['hyai'], \
             'hybi'      : mmr['hybi'], \
             'hyam'      : mmr['hyam'], \
             'hybm'      : mmr['hybm'], \
             'units_ps'  : mmr['units_ps'], \
             'units_p0'  : mmr['units_p0'], \
             'nlev'      : mmr['nlev']}
#
    print('MIN - MAX')
    print(np.amin(conc))
    print(np.amax(conc))
    print('--- calculatesinglefield_conc_from_mmr ---')
#
    return data
