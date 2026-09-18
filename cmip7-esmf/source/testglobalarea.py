import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readvariablenamesnc
import readnc

'''


'''
gridsdir='/nird/datalake/NS2345K/olivie/emissions-auxiliary/esmf/grids'

gridlist=['lat0.25xlon0.25_lon0minus179.875_lat0plus89.875_scrip_v20251011', \
          'lat0.5xlon0.5_lon0minus179.75_lat0minus89.75_scrip_v20251011', \
          'ne16np4_scrip_171002_ESMFmesh', \
          'ne16pg3_ESMFmesh_cdf5_c20211018', \
          'ne30np4_ESMFmesh_cdf5_c20211018', \
          'ne30pg2_ESMFmesh_cdf5_c20211018', \
          'ne30pg3_ESMFmesh_cdf5_c20211018', \
          'ne30pg3_scrip_170611', \
          'ne30pg4_ESMFmesh_cdf5_c20211018']

for grid in gridlist :
    filename=gridsdir+'/'+grid+'.nc'
    variablelist=readvariablenamesnc.readvariablenamesnc(filename)
        
    areanamelist=['grid_area','elementArea']
    areanamefound=None
    for areaname in areanamelist :
        if ( areaname in variablelist ) : areanamefound=areaname

    weight = readnc.readnc(areanamefound,filename)        
    total = np.sum(weight)
    print('Total area : ', total)
