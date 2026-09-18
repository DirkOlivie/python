from netCDF4 import Dataset
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

# ndep file
specieslist=['drynhx','drynoy','wetnhx','wetnoy']
nmonth=12

for species in specieslist :

    filename='/scratch/olivie/code/python/cmip6-ndep/data/input/'+species+'_input4MIPs_surfaceFluxes_CMIP_NCAR-CCMI-2-0_gn_185001-185012.nc'

    field=readnc.readnc(species,filename)

    longitude=readnc.readnc('lon', filename)
    latitude=readnc.readnc('lat', filename)

    landfraction=readnc.readnc('LANDFRAC', '/datalake/NS2345K/olivie/grid_atm_144x96.nc')

    print(landfraction.shape)

    region='SEA'

    area=areafraction.areafraction(longitude=longitude,latitude=latitude,region=region,outputtype='area',landfraction=landfraction)

    series=np.zeros((nmonth), dtype=float)

    for imonth in range(nmonth) :
        series[imonth] = np.sum(field[imonth,:,:] * area) * 86400 * 365 * 1.e-9

    print(species, np.mean(series))



