import math
import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleh0field

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/aerotabread/source')

'''
REMARK

'''


def calculatesinglefield_sad_cesm2( expid, var, date):
##################################    
    '''
    MODIFICATIONS
        (2023-01-18) : creation     
    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_sad_cesm2 +++')
    print('date : '+date)
#
#   constant
    Rair  =287.058
#
#   allowed variables
    if   ( var == 'sad_cesm2_dry_a1' ) : cnum='num_a1' ; cdiameter='dgnum1'    ; sigma=1.6 
    elif ( var == 'sad_cesm2_dry_a2' ) : cnum='num_a2' ; cdiameter='dgnum2'    ; sigma=1.6
    elif ( var == 'sad_cesm2_dry_a3' ) : cnum='num_a3' ; cdiameter='dgnum3'    ; sigma=1.2
    elif ( var == 'sad_cesm2_dry_a4' ) : cnum='num_a4' ; cdiameter='dgnum4'    ; sigma=1.6
    elif ( var == 'sad_cesm2_wet_a1' ) : cnum='num_a1' ; cdiameter='dgnumwet1' ; sigma=1.6 
    elif ( var == 'sad_cesm2_wet_a2' ) : cnum='num_a2' ; cdiameter='dgnumwet2' ; sigma=1.6
    elif ( var == 'sad_cesm2_wet_a3' ) : cnum='num_a3' ; cdiameter='dgnumwet3' ; sigma=1.2
    elif ( var == 'sad_cesm2_wet_a4' ) : cnum='num_a4' ; cdiameter='dgnumwet4' ; sigma=1.6
#
#   obtain number concentration : units = [1/kg] probably
    nconc = readsingleh0field.readsingleh0field(expid=expid,var=cnum,date=date)
    units_nconc = nconc['units']
    if ( units_nconc.strip() != '1/kg' ) :
        print('Units not recognized : '+units_nconc)
        print('Units should be : 1/kg')
        quit()
#
#   obtain the diameter 
    diameter = readsingleh0field.readsingleh0field(expid=expid,var=cdiameter,date=date)
    units_diameter = diameter['units']
    if ( units_diameter.strip() != 'm' ) :
        print('Units not recognized : '+units_diameter)
        print('Units should be : m')
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
    nlev, nlat, nlon = nconc['field'].shape

#   calculate air density
    rho = np.zeros([nlev,nlat,nlon])
    for ilev in range(0,nlev) :
        for ilat in range(0,nlat) :
            for ilon in range(0,nlon) :
#               pressure                  
                p    = t['hyam'][ilev] * t['p0'] + t['hybm'][ilev] * t['ps'][ilat,ilon]           # mid-level pressure
#               density                
                rho[ilev,ilat,ilon]  = p / Rair / t['field'][ilev,ilat,ilon]  

#   calculate sad
    sad = np.zeros([nlev,nlat,nlon])
    sad = nconc['field'] \
        * rho            \
        * math.pi * diameter['field']* diameter['field']*sigma*sigma*1.e-2 # m2/m3 -> cm2/cm3

#   units
    units='cm-2 cm-3'
#
#   create structure
    data = { 'field'     : sad, \
             'longitude' : nconc['longitude'], \
             'latitude'  : nconc['latitude'], \
             'nlon'      : nconc['nlon'], \
             'nlat'      : nconc['nlat'], \
             'units'     : units, \
             'p0'        : nconc['p0'], \
             'ps'        : nconc['ps'], \
             'hyai'      : nconc['hyai'], \
             'hybi'      : nconc['hybi'], \
             'hyam'      : nconc['hyam'], \
             'hybm'      : nconc['hybm'], \
             'units_ps'  : nconc['units_ps'], \
             'units_p0'  : nconc['units_p0'], \
             'nlev'      : nconc['nlev']}
#
    print('MIN - MAX')
    print(np.amin(sad))
    print(np.amax(sad))
    print('--- calculatesinglefield_sad_cesm2 ---')
#
    return data
