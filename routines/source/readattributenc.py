from netCDF4 import Dataset
import numpy as np

def readattributenc(variable,filename,attribute):
#------------------
    '''
    REMARK
        converts field to np-array

    MODIFICATIONS
        (2025-07-31) creation
    '''
#    print('filename : ', filename)
#    print('variable : ', variable)
#    print('attribute : ', attribute)

    nc_fid= Dataset(filename, 'r')

#   field = nc_fid.variables[variable][:]

    if   ( attribute == 'units'         ) : attributevalue=nc_fid.variables[variable].units         # units
    elif ( attribute == 'bounds'        ) : attributevalue=nc_fid.variables[variable].bounds        # bounds
    elif ( attribute == 'calendar'      ) : attributevalue=nc_fid.variables[variable].calendar      # calendar
    elif ( attribute == 'axis'          ) : attributevalue=nc_fid.variables[variable].axis          # axis
    elif ( attribute == 'long_name'     ) : attributevalue=nc_fid.variables[variable].long_name     # long_name
    elif ( attribute == 'standard_name' ) : attributevalue=nc_fid.variables[variable].standard_name # standard_name
    elif ( attribute == 'original_name' ) : attributevalue=nc_fid.variables[variable].original_name # original_name
    elif ( attribute == 'cell_methods'  ) : attributevalue=nc_fid.variables[variable].cell_methods  # cell_methods
    elif ( attribute == 'cell_measures' ) : attributevalue=nc_fid.variables[variable].cell_measures # cell_measures
    elif ( attribute == 'history'       ) : attributevalue=nc_fid.variables[variable].history       # history
    elif ( attribute == 'missing_value' ) : attributevalue=nc_fid.variables[variable].missing_value # missing_value
    elif ( attribute == '_FillValue'    ) : attributevalue=nc_fid.variables[variable]._FillValue    # FillValue
    elif ( attribute == 'positive'      ) : attributevalue=nc_fid.variables[variable].positive      # positive
    elif ( attribute == 'formula_terms' ) : attributevalue=nc_fid.variables[variable].formula_terms # formula_terms
    elif ( attribute == 'molecular_weight' ) : attributevalue=nc_fid.variables[variable].molecular_weight # molecular_weight
    else : 
        print('+++ readattributenc +++')
        print('No attribute recognized : ', attribute)
        quit()

    nc_fid.close

    return attributevalue
