from netCDF4 import Dataset

def readshapenc(variable, filename):
#--------------
    '''
    MODIFICATIONS
        (2026-07-23) creation
    '''
    print('variable : ', variable)
    print('filename : ', filename)

    nc_fid= Dataset(filename, 'r')

    shape = nc_fid.variables[variable].shape

    nc_fid.close

    return shape
