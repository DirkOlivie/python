import numpy as np
from netCDF4 import Dataset

import experimentdefinition


'''
REMARK
        tempeatures [K] -> converted to [] : NOT ANYMORE
        conversion : molecules cm-3 -> mol mol-1

MODIFCICATION 
        (2022-07-11) : no conversion of temperature from [K] to [C]
        (2023-10-20) : introduced possibility for basic experimentname
'''


def readsingleh0field( expid, var, date):
#####################
    print('+++ readsingleh0field +++')
    print('date : '+date)
    print('var  : '+var)
    print('--- readsingleh0field ---')
#
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid'] # experiment you read (can be different from experiment you write)
    
    realm='atm'
    modelversion='cam'
    
#   read netcdf file
    nc_f=subdir+'/'+cexpid+'/'+realm+'/hist/'+cexpid+'.'+modelversion+'.h0.'+date+'.nc'
    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')
    
    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
    field=np.squeeze(np.array(nc_fid.variables[var][:]))
    units=nc_fid.variables[var].units
    ndim=field.ndim
    nlat=len(lats)
    nlon=len(lons)
    
    if ( ndim==3 ) : 
    
        ps=np.squeeze(np.array(nc_fid.variables['PS'][:])) # surface pressure
        hyam=np.array(nc_fid.variables['hyam'][:]) # hyam
        hybm=np.array(nc_fid.variables['hybm'][:]) # hybm
        hyai=np.array(nc_fid.variables['hyai'][:]) # hyam
        hybi=np.array(nc_fid.variables['hybi'][:]) # hybm
        ta=np.squeeze(np.array(nc_fid.variables['T'][:]))
    
        p0=np.array(nc_fid.variables['P0'][:]) # reference pressure
  
        units_ps=nc_fid.variables['PS'].units
        units_p0=nc_fid.variables['P0'].units
    
        nlev = len(hyam)
    
    nc_fid.close
#
#   data            
    data = { 'field'     : field, \
             'longitude' : lons, \
             'latitude'  : lats, \
             'nlon'      : nlon, \
             'nlat'      : nlat, \
             'units'     : units}  
    
    if ( ndim == 3) :
        data.update({   
             'p0'        : p0, \
             'ps'        : ps, \
             'hyai'      : hyai, \
             'hybi'      : hybi, \
             'hyam'      : hyam, \
             'hybm'      : hybm, \
             'units_ps'  : units_ps, \
             'units_p0'  : units_p0, \
             'nlev'      : nlev})
#   
    print('--- readsingleh0field ---')
# 
    return data    
