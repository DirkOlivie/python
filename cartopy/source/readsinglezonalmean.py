import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsinglefield
#import getexternalfield

def readsinglezonalmean( expid, var, date):
    '''
    REMARK
	    tempeatures [K] -> converted to []  

    MODIFICATIONS
        (2025-10-26)
            added units of x- and y-axes
    '''
#
    print('+++ readsinglezonalmean +++')
    print('date : '+date)
    print('--- readsinglezonalmean ---')
#
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    chem=expidinfo['chem']
#
#    if ( chem == '' and \
#         ( var == 'OH' or var == 'HO2' or var == 'O3' or var == 'NO3' ) ) :
#        D= getexternalfield.getexternalfield(expid=expid,var=var,date=date)
#    else :
    D = readsinglefield.readsinglefield(expid=expid,var=var,date=date)  

# make zonal averages
    zonalmeanfield=np.mean(D['field'],axis=2) # over last dimension = lon
    zonalmeanps=np.mean(D['ps'],axis=1)       # over last dimension = lon

    nlev, nlat, nlon = D['field'].shape
# calculate x,y,z field
    x = np.zeros( (nlev, nlat) )
    y = np.zeros( (nlev, nlat) )
    z = np.zeros( (nlev, nlat) )

    for ilev in range (nlev) :
        for ilat in range (nlat) :

            x[ilev,ilat] = D['latitude'][ilat]
            y[ilev,ilat] = D['p0'] * D['hyam'][ilev] + zonalmeanps[ilat] * D['hybm'][ilev]
            z[ilev,ilat] = zonalmeanfield[ilev,ilat]

    data = { 'x' : x, \
             'y' : y, \
             'z' : z, \
             'units' : D['units'], \
             'x_units' : 'degree_north', \
             'y_units' : 'Pa'}

    return data

