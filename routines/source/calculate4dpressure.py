import numpy as np

def calculate4dpressure(p0,ps,hya,hyb):
#----------------------
#
#   MODIFICATION
#       (2025-05-28)
#           changed input variables into hya and hyb (instead of hyam and hybm)
#           aimed to work both for hyam/hybm and hyai/hybi
#

#------------------------------------
#
    print('+++ calculated4dpressure ++++')
    print('p0 : ', p0)
    print('ps (shape) : ', ps.shape)
    print('hya (shape) : ', hya.shape)
    print('hyb (shape) : ', hyb.shape)
#   
    nlev = hya.shape[0]
    ntime, nlat, nlon = ps.shape
#
    pressure = np.zeros( ( ntime, nlev, nlat, nlon ) )

    for ilev in range(nlev) :

        pressure[:,ilev,:,:] = hya[ilev] * p0 + hyb[ilev] * ps[:,:,:] # mid-level pressure
#
    return pressure
