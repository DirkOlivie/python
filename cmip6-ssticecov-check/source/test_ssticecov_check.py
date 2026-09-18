import matplotlib.pyplot as plt
import os
import numpy as np
from netCDF4 import Dataset

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

# file with SST and SIC [18490116, 18490215, ... 20151116, 20151216] 2004 values = ( 165 + 2) * 12
dir='/scratch/olivie/noresm-inputdata/noresm-only/atm/cam/sst'
nc_f=dir+'/fice-micom-divocn_sst-micom-dow_NHIST_f19_tn14_20190625_1849-2015_series_version20190726_ts.nc'
nc_fid= Dataset(nc_f, 'r')
lats=np.array(nc_fid.variables['lat'][:])  # latitudes
lons=np.array(nc_fid.variables['lon'][:])  # longitudes
field=np.array(nc_fid.variables['ice_cov'][:])
nc_fid.close

ntime, nlat, nlon = field.shape

# file with land/sea mask
dir='/projects/NS9560K/noresm/cases/NHIST_f19_tn14_20190625/atm/hist'
nc_g=dir+'/NHIST_f19_tn14_20190625.cam.h0.1949-12.nc'
nc_gid=Dataset(nc_g, 'r')
landfrac=np.squeeze(np.array(nc_gid.variables['LANDFRAC'][:])) # landfraction
gridarea=np.squeeze(np.array(nc_gid.variables['GRIDAREA'][:])) # landfraction
nc_gid.close

seafrac=-landfrac+1.

#area = areafraction.areafraction(latitude=lats, longitude=lons, landfraction=landfrac, outputtype='area', region='glob')
area = areafraction.areafraction(latitude=lats, longitude=lons, landfraction=landfrac, outputtype='area', region='NH')

field = np.clip(field,0.,1.)


print(np.amin(seafrac),np.amax(seafrac))
print(np.amin(area),np.amax(area))

nmonth=12
valuelist=np.zeros((ntime//nmonth))
yearlist=np.zeros((ntime//nmonth))

for itime in range(ntime) :
#   ttt= np.sum(field[itime,:,:]             *area[:,:]) / np.sum(area[:,:])
    ttt= np.sum(field[itime,:,:]*seafrac[:,:]*area[:,:]) / np.sum(area[:,:])
    valuelist[itime//nmonth] = valuelist[itime//nmonth] + ttt / float(nmonth) 
    yearlist[itime//nmonth] = 1849 + itime//nmonth
    print(itime, valuelist[itime//nmonth])


fig, ax = plt.subplots(figsize=[8,4],dpi=100)
ax.set_xlabel('Time [yr]')
ax.set_ylabel('[fraction]') # use first experiment to obtain units
ax.set_title('Sea ice cover')
ax.plot(yearlist,valuelist)

path='/projects/NS2345K/www/people/olivie/plots'
if  not os.path.isdir(path) : os.mkdir(path)

fig.savefig(path+'/test_icecov.ps' , bbox_inches='tight')
fig.savefig(path+'/test_icecov.png', bbox_inches='tight')
