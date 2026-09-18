import numpy as np

import sys
#sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
#import season2monthlist


def fillensemblestatistics (data, estimator) :
#---------------------------------------------
    '''
    INPUT
        data      : list of structure
        estimator : 'min' | 'max' | 'mean' | 'median' | <experiment name>

    MODIFICATIONS	
	2021-04-05
        2021-07-08 : adaptation to work both for annual and monthly timeseries



    '''
    
#   number of experiments available
    nexpid=len(data)

#   find minimum length contained in all experiments
    timelist = np.zeros(nexpid, dtype=int)
    for iexpid in range(0,nexpid) : 
        timelist[iexpid] = data[iexpid]['ntime']
    
    ntime=np.amin(timelist) # minimum length of all experiments
    print(ntime) 
#  
    valuelist = np.zeros(ntime, dtype=float)
    for itime in range(0,ntime) :

#       values of all the ensemblembers in one array
        vlist=np.zeros(nexpid, dtype=float)
        for iexpid in range(0,nexpid) :
            vlist[iexpid] = data[iexpid]['valuelist'][itime]

#       calculate ensemble statistics
        if   ( estimator == 'min'    ) : valuelist[itime] = np.amin(vlist)
        elif ( estimator == 'max'    ) : valuelist[itime] = np.amax(vlist)
        elif ( estimator == 'mean'   ) : valuelist[itime] = np.mean(vlist)
        elif ( estimator == 'median' ) : valuelist[itime] = np.median(vlist)
        else : 
           for iexpid in range(0,nexpid) : 
               if ( estimator == data[iexpid]['expid'] ) : valuelist[itime] = vlist[iexpid]
#
#   OUTPUT STRUCTURE
    outdata = { 'expid'     : estimator, \
                'variable'  : data[0]['variable'], \
                'units'     : data[0]['units'], \
                'area'      : data[0]['area'], \
                'areaglob'  : data[0]['areaglob'], \
                'timelist'  : data[0]['timelist'][0:ntime], \
                'valuelist' : valuelist}
#
    return outdata
