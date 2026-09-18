from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition


def create_flexpartgrid(grid):
#-----------------------------
#
#   Example file from Andrea:
#       /datalake/NS9560K/andrear/grid_atm_288x192.nc
#

#   files to be used
    orogdir='/scratch/olivie/noresm-inputdata/atm/cam/topo'
    if ( grid == '144x96' ) :
        orogfile=orogdir+'/fv_1.9x2.5_nc3000_Nsw084_Nrs016_Co120_Fi001_ZR_061116.nc'
        expid  = 'NHIST_f19_tn14_20190625'
    elif ( gird == '288x192' ) :
        orogfile=orogdir+'fv_0.9x1.25_nc3000_Nsw042_Nrs008_Co060_Fi001_ZR_sgh30_24km_GRNL_c170103.nc'
        expid  = 'NHISTfrc2_f09_tn14_20191001'
    else : 
        print('No grid recognized : ', grid)
        quit()

#   read from topograpghy file
    nc_f=orogfile
    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')

    latitude      =np.array(nc_fid.variables['lat'][:])  # latitudes
    lat_long_name =         nc_fid.variables['lat'].long_name
    lat_units     =         nc_fid.variables['lat'].units        

    longitude     = np.array(nc_fid.variables['lon'][:])  # longitudes
    lon_long_name =          nc_fid.variables['lon'].long_name
    lon_units     =          nc_fid.variables['lon'].units
    
    sgh               =np.array(nc_fid.variables['SGH'][:]) # hyam
    sgh_missing_value =         nc_fid.variables['SGH'].missing_value
    sgh_fill_value    =         nc_fid.variables['SGH']._FillValue
    sgh_long_name     =         nc_fid.variables['SGH'].long_name
    sgh_units         =         nc_fid.variables['SGH'].units
    sgh_filter        =         nc_fid.variables['SGH'].filter

    gridscale_input   = nc_fid.grid_length_scale
    nc_fid.close 

#   read from h0 file
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid']
    year0=expidinfo['year0']

    camversion='cam'
    yyyy = str("%4.4i"% (year0))
    nc_f=subdir+'/'+expid+'/atm/hist/'+expid+'.'+camversion+'.h0.'+yyyy+'-01.nc'

    nc_fid= Dataset(nc_f, 'r')

    landfrac               = np.array(nc_fid.variables['LANDFRAC'][:])
#    landfrac_missing_value =          nc_fid.variables['LANDFRAC'].missing_value
#    landfrac_fill_value    =          nc_fid.variables['LANDFRAC']._FillValue
    landfrac_long_name     =          nc_fid.variables['LANDFRAC'].long_name
    landfrac_units     =          nc_fid.variables['LANDFRAC'].units
    landfrac_cell_methods     =          nc_fid.variables['LANDFRAC'].cell_methods

    phis=np.array(nc_fid.variables['PHIS'][:])
    phis_long_name =          nc_fid.variables['PHIS'].long_name
    phis_units =          nc_fid.variables['PHIS'].units
#    phis_filter =          nc_fid.variables['PHIS'].filter
#    phis_missing_value =          nc_fid.variables['PHIS'].missing_value
#    phis_fill_value =          nc_fid.variables['PHIS']._FillValue

    nc_fid.close
#
#   create_new file
    nlon=len(longitude)
    nlat=len(latitude)    
   
    path='/scratch/olivie/code/python/grid-flexpart/output/' 
    fn=path+'/grid_atm_'+grid+'.nc'

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   create dimensions
    lat = ds.createDimension('lat', nlat)
    lon = ds.createDimension('lon', nlon)

#   create variables
    lats = ds.createVariable('lat', 'f8', ('lat',))
    lons = ds.createVariable('lon', 'f8', ('lon',))

    fphis     = ds.createVariable('PHIS'    , 'f8', ('lat', 'lon',))
    flandfrac = ds.createVariable('LANDFRAC', 'f8', ('lat', 'lon',))
    fsgh      = ds.createVariable('SGH'     , 'f8', ('lat', 'lon',), fill_value=sgh_fill_value)

#   global attribute
    ds.grid_length_scale = gridscale_input


#   attributes for variables
#   latitude
    lats.units         = lat_units
    lats.long_name     = lat_long_name

#   longitude
    lons.units         = lon_units
    lons.long_name     = lon_long_name

#   sgh
    print(type(sgh_missing_value))
    fsgh.missing_value = sgh_missing_value
#    fsgh._FillValue    = sgh_fill_value
    fsgh.long_name     = sgh_long_name
    fsgh.units         = sgh_units
    fsgh.filter        = sgh_filter

#   landfrac
#    flandfrac.missing_value = landfrac_missing_value
#    flandfrac._FillValue    = landfrac_fill_value
    flandfrac.long_name     = landfrac_long_name
    flandfrac.units     = landfrac_units
    flandfrac.cell_methods     = landfrac_cell_methods

#   phis
    fphis.long_name     = phis_long_name
    fphis.units         = phis_units
#    fphis.filter        = phis_filter
#    fphis.missing_value = phis_missing_value
#    fphis._FillValue    = phis_fill_value
#
#   ACTUAL VALUES TO FIELDS
    lats[:] = latitude[0:nlat]
    lons[:] = longitude[0:nlon]   
    fsgh[:,:]      = sgh[:,:]
    flandfrac[:,:] = landfrac[:,:]
    fphis[:,:]     = phis[:,:]


#   global attributes
#
    ds.close()       

