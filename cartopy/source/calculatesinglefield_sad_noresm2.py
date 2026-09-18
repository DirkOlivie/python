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


def calculatesinglefield_sad_noresm2( expid, var, date):
####################################    
    '''
    MODIFICATIONS
        (2023-01-18) : creation     
    '''
#
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield_sad_noresm2 +++')
    print('date : '+date)
#
#   constant
    Rair  =287.058
#
#   allowed variables
    if   ( var == 'sad_noresm2_dry_m01' ) : cnum='NCONC01' ; cradius='NMR01'    ; csigma='SIGMA01'
    elif ( var == 'sad_noresm2_dry_m02' ) : cnum='NCONC02' ; cradius='NMR02'    ; csigma='SIGMA02'
    elif ( var == 'sad_noresm2_dry_m04' ) : cnum='NCONC04' ; cradius='NMR04'    ; csigma='SIGMA04'
    elif ( var == 'sad_noresm2_dry_m05' ) : cnum='NCONC05' ; cradius='NMR05'    ; csigma='SIGMA05'
    elif ( var == 'sad_noresm2_dry_m06' ) : cnum='NCONC06' ; cradius='NMR06'    ; csigma='SIGMA06'
    elif ( var == 'sad_noresm2_dry_m07' ) : cnum='NCONC07' ; cradius='NMR07'    ; csigma='SIGMA07'
    elif ( var == 'sad_noresm2_dry_m08' ) : cnum='NCONC08' ; cradius='NMR08'    ; csigma='SIGMA08'
    elif ( var == 'sad_noresm2_dry_m09' ) : cnum='NCONC09' ; cradius='NMR09'    ; csigma='SIGMA09'
    elif ( var == 'sad_noresm2_dry_m10' ) : cnum='NCONC10' ; cradius='NMR10'    ; csigma='SIGMA10'
    elif ( var == 'sad_noresm2_dry_m12' ) : cnum='NCONC12' ; cradius='NMR12'    ; csigma='SIGMA12'
    elif ( var == 'sad_noresm2_dry_m14' ) : cnum='NCONC14' ; cradius='NMR14'    ; csigma='SIGMA14'
#
#   obtain number concentration : units = [#/m3] probably
    nconc = readsingleh0field.readsingleh0field(expid=expid,var=cnum,date=date)
    units_nconc = nconc['units']
    if ( units_nconc.strip() != '#/m3' ) :
        print('Units not recognized : '+units_nconc)
        print('Units should be : #/m3')
        quit()
#
#   obtain the radius
    radius = readsingleh0field.readsingleh0field(expid=expid,var=cradius,date=date)
    units_radius = radius['units']
    if ( units_radius.strip() != 'm' ) :
        print('Units not recognized : '+units_radius)
        print('Units should be : m')
        quit()
#
#   obtain sigma
    sigma = readsingleh0field.readsingleh0field(expid=expid,var=csigma,date=date)
    units_sigma = sigma['units']
    if ( units_sigma.strip() != '-' ) :
        print('Units not recognized : '+units_sigma)
        print('Units should be : m')
        quit()
#
#   dimensions
    nlev, nlat, nlon = nconc['field'].shape

#   calculate sad
    sad = np.zeros([nlev,nlat,nlon])
    sad = nconc['field'] \
        * 4. * math.pi * radius['field']* radius['field']*sigma['field']*sigma['field']*1.e-2 # m2/m3 -> cm2/cm3

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
    print('--- calculatesinglefield_sad_noresm2 ---')
#
    return data
