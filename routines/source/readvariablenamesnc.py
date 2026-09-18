from netCDF4 import Dataset

def readvariablenamesnc(filename):
#----------------------
    '''
    MODIFICATIONS
        (2026-01-07) creation
    '''
    print('filename : ', filename)

    nc_fid= Dataset(filename, 'r')

    variable_names = nc_fid.variables.keys()

    nc_fid.close

    return variable_names
