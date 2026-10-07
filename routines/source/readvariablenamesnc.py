from netCDF4 import Dataset

import readndimnc


def readvariablenamesnc(filename, ndim=None):
#----------------------
    '''
    MODIFICATIONS
        (2026-01-07) creation
        (2026-10-02) extension with ndim keyword
            - None : list all variables 
            - 0,1,2,3 ... : list all variable with that dimension
    '''
    print('filename : ', filename)
#
#   read list of all variables in fle
    nc_fid= Dataset(filename, 'r')

    variable_names_all = nc_fid.variables.keys()

    nc_fid.close
#
#   find all variables with correct dimensions
    if ( ndim == None ) : 
        variable_names_final = variable_names_all
    else : 
        variable_names_final=[]

        for variable in variable_names_all :

            ndim_var = readndimnc.readndimnc(variable=variable, filename=filename)

            if (ndim == ndim_var)  : variable_names_final.append(variable)
#
#   return
    return variable_names_final
