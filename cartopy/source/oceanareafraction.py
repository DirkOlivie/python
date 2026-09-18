import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import regiondefinition

import numpy as np

def oceanareafraction(plat, plon, parea, outputtype='area', region='global') :
#--------------------
    '''
    MODIFICATION
	    (2025-02-13) : creation

    INPUT
        plon
        plat
        parea
	    outputtype : 
            'area' -> output in m2 : total will be surface area of Earth
            'weight' -> output in fraction : total will be one (in case of region='global') or smaller than one
	    region : name of region you want
	    fileorigin : -> determines which mask file has to be read

    RETURNS
	    or) the area [m2] of each gridbox
	    or) the fraction [dimensionless] of each gridbox w.r.t. total surface of Earth

    CALLS
	    regiondef : obtains coordinates of region [latA, latB, lonA, lonB, zonal, mask ...
    '''
    #
    # print('+++ areafraction +++')
    #
    # obtain description of studied region
    regiondef=regiondefinition.getregiondefinition(region=region)
    cmask  = regiondef['cmask']
    czonal = regiondef['czonal']
    latA   = regiondef['latA']
    latB   = regiondef['latB']
    lonA   = regiondef['lonA']
    lonB   = regiondef['lonB']
    #
    nlat, nlon = parea.shape
    #
    wA=np.zeros((nlat,nlon), dtype=float)
    np.place(wA, latA <= plat , [1.]) 
    wB=np.zeros((nlat,nlon), dtype=float)
    np.place(wB,  plat <= latB , [1.]) 
    weight = wA * wB

    #weight or area
    if outputtype=='area' :
        weight=weight*parea
    elif outputtype=='weight' :
        weight=weight
    else : quit()
    #
    # print('--- areafraction ---') 
    #
    return weight
