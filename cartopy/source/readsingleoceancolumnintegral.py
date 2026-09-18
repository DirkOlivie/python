import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleoceanfield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits

def readsingleoceancolumnintegral( expid, var, date):
#--------------------------------
    '''





    '''
    print('+++ readsingleoceancolumnintegral +++')
    print('date : '+date)
#
#   read original 3D field
    if ( var == 'oceanheat' ) : varorig='templvl'
    else                      : 
        print('var not recognized : '+var)
        quit()


    D = readsingleoceanfield.readsingleoceanfield(expid=expid,var=varorig,date=date)

#   obtain the dimensions
    nlev, ny, nx = D['field'].shape

#   get standard units
    units=getstandardunits.getstandardunits(units=D['units'])

#   standard : whole column
    column = np.zeros( ( ny,nx ) )  # new  array
    columndepth  = np.zeros( ( ny,nx ) ) 

    for ilev in range(nlev) :

        mask = np.where(D['field'][ilev,:,:] > 1.e+30, 0., 1.)  

        print('MASK')
        print(mask[:,150])

        column = column + D['field'][ilev,:,:] * mask * ( D['depth_bnds'][ilev,1] - D['depth_bnds'][ilev,0] )
        columndepth= columndepth + mask * ( D['depth_bnds'][ilev,1] - D['depth_bnds'][ilev,0] )

    if ( var == 'oceanheat' ) : factor=4180.*1.e6 ; newunits='J m-2'
    else                      : 
        print('var not recognized : '+var)
        quit()

    


    data = { 'field'         : column*factor, \
             'depth'         : columndepth, \
             'units'         : newunits, \
             'units_depth'   : D['units_depth'] \
           } 

    print('--- readsingleoceancolumnintegral ---')

    return data

