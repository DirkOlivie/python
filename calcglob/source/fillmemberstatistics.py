import numpy as np

import sys
#sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
#import season2monthlist


def fillmemberstatistics(data) :
#-----------------------
    '''
    REMARK
        APPLIED AFTER STANDARD fillstatistics : so works most often already on annual-mean, seasonal-mean, ...


    INPUT
        data      : list of structure - individual statistics ia already done

    MODIFICATIONS	
        2026-04-07 : creation
        2026-08-24 : added smooth_min and smooth_max for NAVIGATE manuscript

    CALLED BY
        readseries_internal

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
#   STANDARD APPROACH : mean, median, min, max
#   initialize final timeseries
    valuelist        = np.zeros(ntime, dtype=float) # mean
    valuelist_median = np.zeros(ntime, dtype=float) # median
    valuelist_min    = np.zeros(ntime, dtype=float) # min
    valuelist_max    = np.zeros(ntime, dtype=float) # max

#   loop over all times
    for itime in range(0,ntime) :

#       values of all the ensemblembers in one array
        vlist=np.zeros(nexpid, dtype=float)
        for iexpid in range(0,nexpid) :
            vlist[iexpid] = data[iexpid]['valuelist'][itime]

#       calculate ensemble statistics
        valuelist[       itime] = np.mean(vlist)    # mean 
        valuelist_median[itime] = np.median(vlist)  # median
        valuelist_min[   itime] = np.min(vlist)     # min  
        valuelist_max   [itime] = np.max(vlist)     # max
#   
#   SLIGHTLY MORE COMPLICATED
#   initialize final timeseries
    valuelist_smooth_min    = np.zeros(ntime, dtype=float) # min
    valuelist_smooth_max    = np.zeros(ntime, dtype=float) # max    

#   temporary timeseries
    valuelist_smooth_member = np.zeros((nexpid,ntime), dtype=float) # running average per member
#   calculate running average
    for iexpid in range(0,nexpid) :

        for itime in range(0,ntime) :

            smoothlen = 5
            actuallen=min([smoothlen, itime, ntime-1-itime])

#           squared running average
            valuelist_smooth_member[iexpid, itime]=sum(data[iexpid]['valuelist'][itime-actuallen:itime+actuallen+1]) / float(2*actuallen+1)

#   calculate smooth_min and smooth_max
    for itime in range(0,ntime) : 

        actuallen=min([smoothlen, itime, ntime-1-itime])

        variance = 0.

        for iexpid in range(0,nexpid) :

            variance = variance + 1 / float(nexpid) * np.sum(( data[iexpid]['valuelist'][itime-actuallen:itime+actuallen+1] - valuelist_smooth_member[iexpid, itime] )**2) / float(2*actuallen+1)

        valuelist_smooth_min[itime] = np.mean(valuelist_smooth_member[:, itime]) + np.sqrt(variance)  
        valuelist_smooth_max[itime] = np.mean(valuelist_smooth_member[:, itime]) - np.sqrt(variance)

#   OUTPUT STRUCTURE
    outdata = { 'expid'     : 'ensemblemean', \
                'variable'  : data[0]['variable'], \
                'units'     : data[0]['units'], \
                'area'      : data[0]['area'], \
                'areaglob'  : data[0]['areaglob'], \
                'timelist'  : data[0]['timelist'][0:ntime], \
                'valuelist'        : valuelist, \
                'valuelist_median' : valuelist_median, \
                'valuelist_min'    : valuelist_min, \
                'valuelist_max'    : valuelist_max, \
                'valuelist_smooth_min' : valuelist_smooth_min, \
                'valuelist_smooth_max' : valuelist_smooth_max  \
              }
#
    return outdata
