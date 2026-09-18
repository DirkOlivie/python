from netCDF4 import Dataset

def readdimensionsnc(variable, filename):
#-------------------
    '''
    MODIFICATIONS
        (2026-07-23) creation
    '''
    print('variable : ', variable)
    print('filename : ', filename)

    nc_fid= Dataset(filename, 'r')

    dimensions = nc_fid.variables[variable].dimensions

    nc_fid.close

    return dimensions
