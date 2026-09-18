import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsinglefield
import calculatesinglefield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits
import getmolarweight

def readsinglecolumnintegral( expid, var, date):
############################
    '''
    INPUT
        expid   : experiment name
        var     : name for 3D field (does not have the word "column integral" in it)
        date    : YYYY-MM
    '''
    print('+++ readsinglecolumnintegral +++')
    print('date : '+date)

    grav  =  9.81
    Mwair = 28.97  # gram/mole
    Rair  =287.058
#
#   read 3D field
    if ( var == 'EXT_MODE01_AeroTab_NCONC_RELHUM' \
      or var == 'EXT_MODE01_AeroTab_NCONC_SPEHUM' \
      or var == 'EXT_MODE01_AeroTab_NCONC' \
      or var == 'EXT_MODE05_AeroTab_NCONC_RELHUM' \
      or var == 'EXT_MODE05_AeroTab_NCONC_SPEHUM' \
      or var == 'EXT_MODE05_AeroTab_NCONC' ) :
        D = calculatesinglefield.calculatesinglefield(expid=expid,var=var,date=date)
    else :   
        D = readsinglefield.readsinglefield(expid=expid,var=var,date=date)

    nlev, nlat, nlon = D['field'].shape

#   read 3D temperature field
    ta = readsinglefield.readsinglefield(expid=expid,var='T',date=date)
    if ( ta['units'] == 'C' ) : 
        ta['field']=ta['field'] + 273.15
        ta['units'] = 'K'
    elif ( ta['units'] == 'K' ) :
        print('... ok ...')
    else :   
        print('incorrect units')
        quit()


# get standard units
    units=getstandardunits.getstandardunits(units=D['units'])

#    if ( units != 'mol mol-1' ) :
#        print('Units can only be mol mol-1 !')
#        quit()
#
#    mw=getmolarweight.getmolarweight(var=var) # gram/mole
#
#    massfield=np.zeros((nlev,nlat,nlon), dtype=float)    
#    for ilev in range (nlev) :
#       massfield[ilev,:,:] = D['field'][ilev,:,:] * ( p0      * ( hyai[ilev+1] - hyai[ilev] ) \
#                                                    + ps[:,:] * ( hybi[ilev+1] - hybi[ilev] ) ) \
#                                                    / grav \
#                                                    * mw \
#                                                    / mwdry     
#
# 
#    columnfield=np.sum(massfield,axis=0) 
#
#    newunits = 'kg m-2'

    if ( units == 'mol mol-1' or units == 'molecules cm-3 s-1' ) :
        Mw = getmolarweight.getmolarweight(var=var) # gram/mole

#   standard : whole column
    column = np.zeros( ( nlat,nlon ) )  # new  array

    for ilev in range(nlev) :

        pressure = D['hyam'][ilev] * D['p0'] + D['hybm'][ilev] * D['ps'][:,:] # mid-level pressure
        density  = pressure / Rair / ta['field'][ilev,:,:]         # density                         

#       airmass
        dm = abs( ( D['hyai'][ilev+1] - D['hyai'][ilev] ) * D['p0'] + ( D['hybi'][ilev+1] - D['hybi'][ilev] ) * D['ps'][:,:] ) / 9.81    # dm = dp / g

        if   ( units == 'mol mol-1'          ) : column = column + dm * D['field'][ilev,:,:] * Mw / Mwair                         ; newunits = 'kg m-2'
        elif ( units == 'kg kg-1'            ) : column = column + dm * D['field'][ilev,:,:]                                      ; newunits = 'kg m-2'
        elif ( units == 'm-3'                ) : column = column + dm * D['field'][ilev,:,:] / density                            ; newunits = 'm-2'
        elif ( units == 'm3 m-3'             ) : column = column + dm * D['field'][ilev,:,:] / density                            ; newunits = 'm3 m-2'
        elif ( units == 'cm-3'               ) : column = column + dm * D['field'][ilev,:,:] / density    *1.e6                   ; newunits = 'm-2'
        elif ( units == 'molecules cm-3 s-1' ) : column = column + dm * D['field'][ilev,:,:] / density    *1.e6 * Mw *1.e-3 / Nav ; newunits = 'kg m-2 s-1'
        elif ( units == 'm-1'                ) : column = column + dm * D['field'][ilev,:,:] / density                            ; newunits = ''
        elif ( units == 'km-1'               ) : column = column + dm * D['field'][ilev,:,:] / density * 1.e-3                    ; newunits = ''
        else :
            print('Unit not recognized : '+units)
            quit()

    data = { 'z'         : column, \
             'lons'      : D['longitude'], \
             'lats'      : D['latitude'], \
             'nlon'      : D['nlon'], \
             'nlat'      : D['nlat'], \
             'units'     : newunits}

    print('MIN - MAX readsinglecolumnintegral()') 
    print('INPUT')
    print(np.amin(D['field']))
    print(np.amax(D['field']))    
    print('OUTPUT')
    print(np.amin(column))
    print(np.amax(column))
    print('--- readsinglecolumnintegral ---')

    return data

