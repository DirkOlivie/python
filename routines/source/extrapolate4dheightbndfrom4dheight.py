import numpy as np

def extrapolate4dheightbndfrom4dheight(height):
#-------------------------------------
#
#   MODIFICATION
#       (2025-05-28)
#           changed input variables into hya and hyb (instead of hyam and hybm)
#           aimed to work both for hyam/hybm and hyai/hybi
#

#------------------------------------
#
    print('+++ calculate4dheightbndfrom4dheight ++++')
    print('height (shape) : ', height.shape)
#   
    ntime, nlev, nlat, nlon = height.shape
#
    heightbnd = np.zeros( ( ntime, nlev+1, nlat, nlon ), dtype=float )

#   1 -> nlev-1
    for ilev in range(1,nlev) :

        heightbnd[:,ilev,:,:] = 0.5 ( height[:,ilev-1,:,:] + height[:,ilev,:,:] )
#
#   ilev=0
    heightbnd[:,0,:,:] = height[:,0,:,:] + 0.5 * ( height[:,0,:,:] - height[:,1,:,:] )    
#
#   ilev=nlev
    heightbnd[:,nlev,:,:] = height[:,nlev-1,:,:] + 0.5 * ( height[:,nlev-1,:,:] - height[:,nlev-2,:,:] )

    return heightbnd
