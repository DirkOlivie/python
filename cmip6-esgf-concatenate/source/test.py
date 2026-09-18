import datetime as dt
import numpy as np
from netCDF4 import Dataset

import ncdump


# INPUT FILE
nc_f = '/projects/NS9034K/CMIP6/ScenarioMIP/NCC/NorESM2-LM/ssp245/r1i1p1f1/Amon/tas/gn/latest/tas_Amon_NorESM2-LM_ssp245_r1i1p1f1_gn_201501-202012.nc'  # Your filename
nc_fid = Dataset(nc_f, 'r')  # Dataset is the class behavior to open the file
                             # and create an instance of the ncCDF4 class
nc_attrs, nc_dims, nc_vars = ncdump.ncdump(nc_fid)
# Extract data from NetCDF file
lats = nc_fid.variables['lat'][:]  # extract/copy the data
lons = nc_fid.variables['lon'][:]
time = nc_fid.variables['time'][:]
tas = nc_fid.variables['tas'][:]  # shape is time, lat, lon as shown above

time_idx = 6  # some random day in 2012
# Python and the renalaysis are slightly off in time so this fixes that problem
offset = dt.timedelta(hours=48)
# List of all times in the file as datetime objects
dt_time = [dt.date(1, 1, 1) + dt.timedelta(hours=t) - offset\
           for t in time]
cur_time = dt_time[time_idx]

# OUTPUT FILE
# Open a new NetCDF file to write the data to. For format, you can choose from
# 'NETCDF3_CLASSIC', 'NETCDF3_64BIT', 'NETCDF4_CLASSIC', and 'NETCDF4'
#w_nc_fid = Dataset('/scratch/olivie/code/python/cmip6-esgf-concatenate/info/output/trial.nc', 'w', format='NETCDF4')
w_nc_fid = Dataset('trial.nc', 'w', format='NETCDF4')
#w_nc_fid.description = "The departure of the NCEP/NCAR Reanalysis " +\
#                      "%s from its value at %s. %s" %\
#                      (nc_fid.variables['tas'].var_desc.lower(),\
#                       'Probeersel', nc_fid.description)
# Using our previous dimension information, we can create the new dimensions
data = {}
for dim in nc_dims:
    print(dim)
    w_nc_fid.createDimension(dim, nc_fid.variables[dim].size)
    data[dim] = w_nc_fid.createVariable(dim, nc_fid.variables[dim].dtype,\
                                        (dim,))
    # You can do this step yourself but someone else did the work for us.
    for ncattr in nc_fid.variables[dim].ncattrs():
        data[dim].setncattr(ncattr, nc_fid.variables[dim].getncattr(ncattr))
# Assign the dimension data to the new NetCDF file.
w_nc_fid.variables['time'][:] = time
w_nc_fid.variables['lat'][:] = lats
w_nc_fid.variables['lon'][:] = lons

# Ok, time to create our departure variable
w_nc_var = w_nc_fid.createVariable('tas', 'f8', ('time', 'lat', 'lon'))
w_nc_var.setncatts({'long_name': u"mean Daily Air temperature departure",\
                    'units': u"degK", 'level_desc': u'Surface',\
                    'var_desc': u"Air temperature departure",\
                    'statistic': u'Mean\nM'})
w_nc_fid.variables['tas'][:] = tas
w_nc_fid.close()  # close the new file

nc_fid.close()
