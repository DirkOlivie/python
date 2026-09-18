from netCDF4 import Dataset
import numpy as np
import netCDF4
import datetime
'''
See : https://unidata.github.io/netcdf4-python/
See : https://unidata.github.io/netcdf4-python/#num2date
'''
nc_f='/projects/NS9252K/ESGF_betzy/CMIP6/CMIP/MOHC/UKESM1-0-LL/historical/r1i1p1f2/Amon/tas/gn/latest/tas_Amon_UKESM1-0-LL_historical_r1i1p1f2_gn_185001-194912.nc'

nc_fid= Dataset(nc_f, 'r')
print('HALLO HALLO')
lats=np.array(nc_fid.variables['lat'][:])  # latitudes
lons=np.array(nc_fid.variables['lon'][:])  # longitudes
times=np.array(nc_fid.variables['time'][:])  # longitudes

nc_fid.close

units=nc_fid.parent_time_units             # global attribute
calendar=nc_fid.variables['time'].calendar # time attribute

print(nc_fid.variables['lon'].units)
print(nc_fid.variables['lon'].standard_name)
print(nc_fid.branch_time_in_parent)
print(nc_fid.parent_activity_id)
print(nc_fid.parent_experiment_id)
print(nc_fid.parent_mip_era)
print(nc_fid.parent_source_id)
print(nc_fid.parent_time_units)
print(nc_fid.parent_variant_label)

print(nc_fid.variables['time'].calendar)

print('+++ time in this file +++')
dates=netCDF4.num2date(times,units,calendar=calendar) 
print(times)
print(dates)

print('+++ branch time +++')
branchtime=nc_fid.branch_time_in_parent
branchdate=netCDF4.num2date(branchtime,units,calendar=calendar)
print(branchtime)
print(branchdate)
print(branchdate.year)
