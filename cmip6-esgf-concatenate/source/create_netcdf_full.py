import netCDF4 as nc
import numpy as np

#fn = '/scratch/olivie/code/python/cmip6-esgf-concatenate/info/output/test.nc'
fn='test.nc'
#ds = nc.Dataset(fn, 'w', format='NETCDF4')
ds = nc.Dataset(fn, 'w', format='NETCDF4_CLASSIC')

print('+++ A +++')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', 10)
lon = ds.createDimension('lon', 10)

print('+++ B +++')

times = ds.createVariable('time', 'f4', ('time',))
lats = ds.createVariable('lat', 'f4', ('lat',))
lons = ds.createVariable('lon', 'f4', ('lon',))
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))

# attribute
value.units = 'Unknown'                                            # attribute
lats.units = 'Degree North'
times.units = 'Days since whatever time ...'

#
ds.description = 'Trying global attribute'
ds.source_id = 'Trying global attribute'
ds.brol = 'Trying global attribute'

print('+++ C +++')

lats[:] = np.arange(40.0, 50.0, 1.0)
lons[:] = np.arange(-110.0, -100.0, 1.0)

print('+++ D +++')

print('var size before adding data', value.shape)

# ADDING VALUES FOR TIME 0
value[0, :, :] = np.random.uniform(0, 100, size=(10, 10))

print('+++ E +++')

# ADDING VALUES FOR TIME 1
print('var size after adding first data', value.shape)
xval = np.linspace(0.5, 5.0, 10)
yval = np.linspace(0.5, 5.0, 10)
value[1, :, :] = np.array(xval.reshape(-1, 1) + yval)

print('var size after adding second data', value.shape)

print('+++ F +++')

ds.close()
