import numpy as np
from netCDF4 import Dataset

import readsinglefield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits

def readsinglelayer( expid, var, date, clayer):
#------------------
    '''
    INPUT
        expid
        var
        date
        
    '''
    print('+++ readsinglelayer +++')
    print('date : '+date)
#
#   read the field
    D = readsinglefield.readsinglefield(expid=expid,var=var,date=date)

#   obtain dimension
    nlev, nlat, nlon = D['field'].shape

#   get standard units
    units=getstandardunits.getstandardunits(units=D['units'])

#   extract specific level
    if ( clayer == 'surfacelayer' )         : ilev=nlev-1
    elif ( clayer == 'secondsurfacelayer' ) : ilev=nlev-2
    elif ( clayer == 'thirdsurfacelayer' )  : ilev=nlev-3
    else : quit()

    field = D['field'][ilev,:,:]

    data = { 'z'         : field, \
             'lons'      : D['longitude'], \
             'lats'      : D['latitude'], \
             'nlon'      : D['nlon'], \
             'nlat'      : D['nlat'], \
             'units'     : units}

    print('--- readsinglelayer ---')

    return data

