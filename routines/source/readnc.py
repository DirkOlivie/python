from netCDF4 import Dataset
import numpy as np

def readnc(variable,filename,auto_mask=True,auto_maskandscale=True):
#---------
    '''
    REMARK
        converts field to np-array

    MODIFICATIONS
        (2025-07-31) creation
        (2026-07-23) added keywords : auto_mask and auto_maksandscale

    '''
    nc_fid= Dataset(filename, 'r')
#   OLD 
#   field=np.array(nc_fid.variables[variable][:])   # latitudes
#   +++ NEW +++
    varid=nc_fid.variables[variable]
    if ( auto_mask == False ) : varid.set_auto_mask(False)
    if ( auto_maskandscale == False ) : varid.set_auto_maskandscale(False)
#   varid.set_auto_maskandscale(False)
    field=np.array(varid[:])
#   --- NEW ---

    nc_fid.close
    return field
