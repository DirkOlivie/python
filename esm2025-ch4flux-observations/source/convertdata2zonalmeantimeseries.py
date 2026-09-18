import numpy as np

def convertdata2zonalmeantimeseries(data, region):
#----------------------------------
    '''
    INPUT
        data

    '''
#    
    ntime = data['ntime']
    nlat  = len(data['latitude'])

#   create first monthly mean
    valuelist= np.mean(data['field'], axis = 2) # average over the longitude
#
#   zonalmean area
    area =np.mean(data['area'], axis = 1)

# DATA STRUCTURE
    outputdata={'expid'      : data['expid'], \
                'variable'   : data['variable'], \
                'units'      : data['units'], \
                'fileorigin' : data['fileorigin'], \
                'latitude'   : data['latitude'], \
                'nlat'       : nlat, \
                'area'       : area, \
                'areatotal'  : area, \
                'areafraction' : area*0. + 1., \
                'areaunits'  : data['areaunits'], \
                'yearlist'   : data['yearlist'], \
                'monthlist'  : data['monthlist'], \
                'timelist'   : data['timelist'], \
                'valuelist'  : valuelist, \
                'ntime'      : data['ntime'], \
                'region'     : region \
               }

    return outputdata
