from netCDF4 import Dataset
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

# grid info
nc_f='/datalake/NS2345K/olivie/inputdata/ocn/blom/grid/grid_tnx1v4_20170622.nc'
nc_fid= Dataset(nc_f, 'r')
parea=np.nan_to_num(np.array(nc_fid.variables['parea'][:]))  # area [m2]
pmask=np.nan_to_num(np.array(nc_fid.variables['pmask'][:]))  # mask
plat=np.array(nc_fid.variables['plat'][:])  # latitudes
plon=np.array(nc_fid.variables['plon'][:])  # longitudes
nc_fid.close

np.place(parea, parea > 1.e20, [0.])
parea[:,-1]=0. # because nreg = 2

# ndep file
fdep='/scratch/olivie/noresm-inputdata/ocn/blom/bndcon/ndeposition_1850_CMIP6_tnx1v4_20250207.nc'
specieslist=['nhxdep','noydep','ndep']

for species in specieslist :

    field=readnc.readnc(species,fdep)
    nmonth=12

    series=np.zeros((nmonth), dtype=float)

    for imonth in range(nmonth) :
        series[imonth] = np.sum(field[imonth,:,:] * pmask * parea) * 14 * 1.e-9

    print(species, np.mean(series))
