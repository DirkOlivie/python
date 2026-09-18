from netCDF4 import Dataset
import numpy as np

nc_f='/datalake/NS2345K/olivie/inputdata/ocn/blom/grid/grid_tnx1v4_20170622.nc'
nc_fid= Dataset(nc_f, 'r')
#parea=np.nan_to_num(np.array(nc_fid.variables['parea'][:]))  # area [m2]
#pmask=np.nan_to_num(np.array(nc_fid.variables['pmask'][:]))  # mask
parea=np.array(nc_fid.variables['parea'][:])  # area [m2]
pmask=np.array(nc_fid.variables['pmask'][:])  # mask
plat=np.array(nc_fid.variables['plat'][:])  # latitudes
plon=np.array(nc_fid.variables['plon'][:])  # longitudes
nc_fid.close

np.place(parea, parea > 1.e20, [0.])

parea[-1,:]=0. # throw away upper gridpoints in NH (represented twice)

print(parea.ndim, parea.shape)
print(pmask.ndim, pmask.shape)
print(plat.ndim, plat.shape)
print(plon.ndim, plon.shape)
#print('plon[ 0,:] : ', plon[ 0,:])
#print('plon[-1,:] : ', plon[-1,:])
#print('plat[ 0,:] : ', plat[ 0,:])
#print('plat[-1,:] : ', plat[-1,:])


#print('plon[:,0]  : ', plon[:,0 ])
#print('plon[:,-1] : ', plon[:,-1])
#print('plat[:,0]  : ', plat[:,0 ])
#print('plat[:,-1] : ', plat[:,-1])


#print(np.sum(parea))
#print(np.sum(parea*pmask))
print(np.nansum(parea*pmask)/np.nansum(parea))
