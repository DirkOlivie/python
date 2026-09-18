import json

def getattributeinfo_online(var, realm):
#--------------------------
    '''
    TABLES CAN BE FOUND AT
    https://github.com/PCMDI/cmip6-cmor-tables/blob/main/Tables/CMIP6_Emon.json

    INPUT
        var
        realm

    RETURN structure containing
            'standard_name' : 
            'long_name'     :
            'units'         :
            'original_name' :
            'cell_methods'  :
            'cell_measures' :
            'cdim'          : '3d', '3d-half', '3d-plev19', '2d'

    CALLS

    TO BE MODIFIED
        (2024-12-09)
        at bottom one finds :
            'cell_methods'  : 'cell_methods', \
            'cell_measures' : 'cell_measures', \
        maybe this should be :
            'cell_methods'  : cell_methods, \
            'cell_measures' : cell_measures, \
    '''

    print('+++ getonlineattributeinfo +++') 
    print('var : ', var)
    print('realm : ', realm)

#   json file
    filename='/nird/home/olivie/code/json/cmip6-cmor-tables/Tables/CMIP6_'+realm+'.json'

    fid = open(filename) # open json file
 
    table=json.load(fid) # load json file

    units         = table['variable_entry'][var]['units']
    standard_name = table['variable_entry'][var]['standard_name']
    long_name     = table['variable_entry'][var]['long_name']
    cell_methods  = table['variable_entry'][var]['cell_methods']
    cell_measures = table['variable_entry'][var]['cell_measures']
    dimensions    = table['variable_entry'][var]['dimensions'] # e.g. : longitude latitude alevel time

    missing_value=table['Header']['missing_value']

    fid.close()         # close json file

#   cdim : 2d or 3d
    if   ( 'alevel'   in dimensions ) : cdim = '3d'
    elif ( 'alevhalf' in dimensions ) : cdim = '3d-half'
    elif ( 'plev19'   in dimensions ) : cdim = '3d-plev19' 
    else : cdim='2d'

#   return data structure
    data={ 'standard_name' : standard_name, \
           'long_name'     : long_name, \
           'units'         : units, \
           'original_name' : '', \
           'cell_methods'  : 'cell_methods', \
           'cell_measures' : 'cell_measures', \
           'cdim'          : cdim }

    return data  
