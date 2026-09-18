import numpy as np

def fillzonalmeanmemberstatistics(data) :
#--------------------------------
    '''


    MODIFICATIONS
        2026-04-25 : creation

    '''

#   number of experiments available
    nexpid=len(data)
    nlat= data[0]['nlat'] # take fro 0-th member


#   initialize final zanal emans
    valuelist        = np.zeros(nlat, dtype=float) # mean
    valuelist_median = np.zeros(nlat, dtype=float) # median
    valuelist_min    = np.zeros(nlat, dtype=float) # min
    valuelist_max    = np.zeros(nlat, dtype=float) # max

#   loop over all latitudes
    for ilat in range(0,nlat) :

#       values of all the ensemblembers in one array
        vlist=np.zeros(nexpid, dtype=float)
        for iexpid in range(0,nexpid) :
            vlist[iexpid] = data[iexpid]['valuelist'][ilat]

#       calculate ensemble statistics
        valuelist[       ilat] = np.mean(  vlist)  # mean 
        valuelist_median[ilat] = np.median(vlist)  # median
        valuelist_min[   ilat] = np.min(   vlist)  # min  
        valuelist_max   [ilat] = np.max(   vlist)  # max
#
#   OUTPUT STRUCTURE
    #   new structure
    outdata={'expid'      : 'ensemblemean', \
             'variable'   : data[0]['variable'], \
             'units'      : data[0]['units'], \
             'fileorigin' : data[0]['fileorigin'], \
             'areaunits'  : data[0]['areaunits'], \
             'year0'      : data[0]['year0'], \
             'year1'      : data[0]['year1'], \
             'season'     : data[0]['season'], \
             'valuelist'  : valuelist, \
             'valuelist_median' : valuelist_median, \
             'valuelist_min'    : valuelist_min, \
             'valuelist_max'    : valuelist_max, \
             'latitude'     : data[0]['latitude'], \
             'nlat'         : data[0]['nlat'], \
             'area'         : data[0]['area'], \
             'areafraction' : data[0]['areafraction'], \
             'areatotal'    : data[0]['areatotal'], \
             'region'       : data[0]['region'] \
            }    
#
    return outdata

