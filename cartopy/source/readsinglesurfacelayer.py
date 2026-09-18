import numpy as np
import readsinglefield

def readsinglesurfacelayer( expid, var, date):
#-------------------------
#
    print('+++ readsinglesurfacelayer +++')
    print('date : '+date)
    print('--- readsinglesurfacelayer ---')

#
#   read 3D field
    D = readsinglefield.readsinglefield(expid=expid,var=var,date=date)
    nlev, nlat, nlon = D['field'].shape

#   output
    data = { 'field'     : D['field'][nlev-1,:,:], \
             'longitude' : D['longitude'], \
             'latitude'  : D['latitude'], \
             'nlon'      : D['nlon'], \
             'nlat'      : D['nlat'], \
             'units'     : D['units']}

    return data

