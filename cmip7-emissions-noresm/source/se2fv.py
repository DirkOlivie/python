import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc


def se2fv(D) :
#------------

    if ( len(D['longitude']) == 48600 \
     and len(D['longitude']) == 48600 ) :   
        gridfile='/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo/fv_0.9x1.25_nc3000_Nsw042_Nrs008_Co060_Fi001_ZR_sgh30_24km_GRNL_c170103.nc'
        regridweightfile='/scratch/olivie/noresm-inputdata/cpl/gridmaps/ne30pg3/map_ne30pg3_TO_fv0.9x1.25_blin.240826.nc'
    elif ( len(D['longitude']) == 13824 \
     and   len(D['latitude']) == 13824 ) :
        gridfile = '/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo/fv_1.9x2.5_nc3000_Nsw084_Nrs016_Co120_Fi001_ZR_061116.nc'
        regridweightfile = '/nird/datalake/NS9560K/diagnostics/land_xesmf_diag_data/map_ne16pg3_to_1.9x2.5_nomask_scripgrids_c250425.nc'
    else :
        print('+++ se2fc +++')
        print()
        quit()

#   read weights from regridfile
    col = readnc.readnc('col', regridweightfile) - 1 # should start at 0 !!
    row = readnc.readnc('row', regridweightfile) - 1 # should start at 0 !!
    S   = readnc.readnc('S'  , regridweightfile)

#   read new longitude/latitude
    longitude = readnc.readnc('lon', gridfile)
    latitude  = readnc.readnc('lat', gridfile)
#
    nlat = len(latitude)
    nlon = len(longitude)
#
    area = areafraction.areafraction(latitude, longitude, outputtype='area')


#   initialise new field
    newfield = np.zeros((nlat,nlon),dtype=float)

#   fill new field
    for i in range(0,len(S)) :
        newfield[row[i] // nlon,  row[i] % nlon] = newfield[row[i] // nlon,  row[i] % nlon] + S[i] * D['field'][col[i]]
#
    data = { 'species'    : D['species'], \
#
             'field'      : newfield, \
             'longitude'  : longitude, \
             'latitude'   : latitude, \
             'area'       : area, \
             'dim'        : '2d', \
             'units'      : D['units'], \
             'area_units' : 'm2', \
             'period'     : D['period']}

    return data

