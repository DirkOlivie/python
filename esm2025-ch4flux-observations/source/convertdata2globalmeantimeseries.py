import numpy as np

def convertdata2globalmeantimeseries(data):
#-----------------------------------
    '''
    '''
#    
    ntime = data['ntime']

#   create first monthly mean
    valuelist=np.zeros(data['ntime'], dtype=float)

    for itime in range(ntime) :
         valuelist[itime] = np.sum(data['field'][itime,:,:] * data['area'] )

    totalarea=np.sum(data['area'])

#   unit conversion
    if   ( data['units'] == 'kg m-2 s-1' )  : factor = 1.e-9  * 365 *86400. ; newunits = 'Tg yr-1' # kg -> Tg and day-1 -> yr-1 
    elif ( data['units'] == 'fraction'   )  : factor = 1.                   ; newunits = data['areaunits'] # fraction -> m2
    else :
        print('+++ convertdata2globalmeantimeseries +++')
        print('No data units recognized : ', data['units'])
        quit()    
#
    valuelist=valuelist * factor

# DATA STRUCTURE
    outputdata={'expid'      : data['expid'], \
                'variable'   : data['variable'], \
                'units'      : newunits, \
                'fileorigin' : data['fileorigin'], \
                'area'       : totalarea, \
                'areaglob'   : totalarea, \
                'areaunits'  : data['areaunits'], \
                'yearlist'   : data['yearlist'], \
                'monthlist'  : data['monthlist'], \
                'timelist'   : data['timelist'], \
                'valuelist'  : valuelist, \
                'ntime'      : data['ntime'] \
               }

    return outputdata
