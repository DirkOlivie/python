from netCDF4 import Dataset
import numpy as np

def readglobalattributenc(filename,attribute):
#------------------------
    '''
    REMARK

    MODIFICATIONS
        (2026-10-03) creation
    '''
#    print('filename : ', filename)
#    print('variable : ', variable)
#    print('attribute : ', attribute)

    nc_fid= Dataset(filename, 'r')

#   field = nc_fid.variables[variable][:]

    if   ( attribute == 'data_title'       ) : attributevalue=nc_fid.data_title
    elif ( attribute == 'molecular_weight' ) : attributevalue=nc_fid.molecular_weight
    elif ( attribute == 'data_creator'     ) : attributevalue=nc_fid.data_creator
    elif ( attribute == 'data_summary'     ) : attributevalue=nc_fid.data_summary
    elif ( attribute == 'cesm_contact'     ) : attributevalue=nc_fid.cesm_contact
    elif ( attribute == 'creation_date'    ) : attributevalue=nc_fid.creation_date
    elif ( attribute == 'update_date'      ) : attributevalue=nc_fid.update_date
    elif ( attribute == 'history'          ) : attributevalue=nc_fid.history
    elif ( attribute == 'data_script'      ) : attributevalue=nc_fid.data_script
    elif ( attribute == 'data_source_url'  ) : attributevalue=nc_fid.data_source_url
    elif ( attribute == 'data_reference'   ) : attributevalue=nc_fid.data_reference
    else : 
        print('+++ readattributenc +++')
        print('No attribute recognized : ', attribute)
        quit()

    nc_fid.close

    return attributevalue
