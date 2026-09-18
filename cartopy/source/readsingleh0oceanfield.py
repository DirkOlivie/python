import numpy as np
from netCDF4 import Dataset

import experimentdefinition

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname


'''
REMARK
        tempeatures [K] -> converted to [] : NOT ANYMORE
        conversion : molecules cm-3 -> mol mol-1

MODIFCICATION 
        (2022-07-11) : no conversion of temperature from [K] to [C]
        (2023-10-20) : introduced possibility for basic experimentname
'''


def readsingleh0oceanfield( expid, var, date):
#-------------------------
    print('+++ readsingleh0oceanfield +++')
    print('expid : '+expid)
    print('date  : '+date)
    print('var   : '+var)
    print('--- readsingleh0oceanfield ---')
#
#   basic experiment name    
    basicexpid=getbasicexpidname.getbasicexpidname(expid=expid, date=date)

#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=basicexpid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid'] # experiment you read (can be different from experiment you write)

    realm='ocn'
    
    if ( expid == 'N1850_f19_tn14_20190621') : modelversion='micom'    
    else                                     : modelversion='blom'

#   read netcdf file
    nc_f=subdir+'/'+cexpid+'/'+realm+'/hist/'+cexpid+'.'+modelversion+'.hm.'+date+'.nc'
    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')
    
    field=np.squeeze(np.array(nc_fid.variables[var][:]))
    units=nc_fid.variables[var].units
    ndim=field.ndim

    if (   ndim == 2 ) : ny, nx = field.shape
    elif ( ndim == 3)  : nlev, ny, nx = field.shape  

#    print('nlev : '+str(nlev))
    print('ny   : '+str(ny))
    print('nx   : '+str(nx))
 
#   additional fields when 3D
    if ( ndim == 3 ) : 
 
        depth=np.array(nc_fid.variables['depth'][:]) # depth
        depth_bnds=np.array(nc_fid.variables['depth_bnds'][:]) # depth_bnds
    
        units_depth=nc_fid.variables['depth'].units
    
    nc_fid.close
#
#   put undefined values (over ocean) to 0 for land model
#   if ( realm == 'lnd' ) : field=np.where(field > 1.e+30, 0., field)
#    
#   data            
    data = { 'field'     : field, \
             'units'     : units, \
             'nx'        : nx, \
             'ny'        : ny}

    if ( ndim == 3 ) :
        data.update({
             'depth'     : depth, \
             'depth_bnds': depth_bnds, \
             'units_depth' : units_depth, \
             'nlev'      : nlev})
    
    return data    
