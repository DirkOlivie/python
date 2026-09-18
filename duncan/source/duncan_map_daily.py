import numpy as np
from netCDF4 import Dataset

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import plotmap

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')

expid='NorESM2-LM_ssp245_r1i1p1f1_gn'
refid='NorESM2-LM_piControl_r1i1p1f1_gn'

f_expid_tasmin='/projects/NS9034K/CMIP6/ScenarioMIP/NCC/NorESM2-LM/ssp245/r1i1p1f1/day/tasmin/gn/latest/tasmin_day_'+expid+'_20910101-21001231.nc'
f_expid_tasmax='/projects/NS9034K/CMIP6/ScenarioMIP/NCC/NorESM2-LM/ssp245/r1i1p1f1/day/tasmax/gn/latest/tasmax_day_'+expid+'_20910101-21001231.nc'
f_refid_tasmin='/projects/NS9034K/CMIP6/CMIP/NCC/NorESM2-LM/piControl/r1i1p1f1/day/tasmin/gn/latest/tasmin_day_'+refid+'_18410101-18501231.nc'
f_refid_tasmax='/projects/NS9034K/CMIP6/CMIP/NCC/NorESM2-LM/piControl/r1i1p1f1/day/tasmax/gn/latest/tasmax_day_'+refid+'_18410101-18501231.nc'

year0=2100 #2091
year1=2100
season='YEA'
wlist=[1.,-1.]
var='tasmaxmin'

# read all data
nc_fid= Dataset(f_expid_tasmin, 'r')
lats=np.array(nc_fid.variables['lat'][:])  # latitudes
lons=np.array(nc_fid.variables['lon'][:])  # longitudes
tasmin_expid=np.squeeze(np.array(nc_fid.variables['tasmin'][:]))
nc_fid.close

nc_fid= Dataset(f_expid_tasmax, 'r') ; tasmax_expid=np.squeeze(np.array(nc_fid.variables['tasmax'][:])) ; nc_fid.close
nc_fid= Dataset(f_refid_tasmin, 'r') ; tasmin_refid=np.squeeze(np.array(nc_fid.variables['tasmin'][:])) ; nc_fid.close
nc_fid= Dataset(f_refid_tasmax, 'r') ; tasmax_refid=np.squeeze(np.array(nc_fid.variables['tasmax'][:])) ; nc_fid.close

# sum/difference over fields
field_expid = tasmax_expid - tasmin_expid
field_refid = tasmax_refid - tasmin_refid

# select only last year
t0=365*9
t1=365*10
field_expid=field_expid[t0:t1,:,:]
field_refid=field_refid[t0:t1,:,:]

print(field_expid.ndim)

# average over time
field_expid= np.mean(field_expid, axis=0)
field_refid= np.mean(field_refid, axis=0)

print(field_expid.ndim)



expdata = { 'lats' : lats, 'lons' : lons, 'z' : field_expid, 'units' : 'K'}
refdata = { 'lats' : lats, 'lons' : lons, 'z' : field_refid, 'units' : 'K'}

plotmap.plotmap(expid=expid, refid=refid, var=var, wlist=wlist, year0=year0, year1=year1, season=season, expdata=expdata, refdata=refdata, figlayout=figlayout0)
#plotmap.plotmap(expid=expid, refid=refid, var=var, wlist=wlist, year0=year0, year1=year1, season=season, expdata=expdata, refdata=refdata, figlayout=figlayout1)
