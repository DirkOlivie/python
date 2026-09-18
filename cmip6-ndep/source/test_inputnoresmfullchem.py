from netCDF4 import Dataset
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

Nav=6.022e23
Mwnh3=17.

# ndep file
filename='/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015/emissions-cmip6_NH3_other_surface_1750-2015_0.9x1.25_c20170322.nc'
specieslist=['emiss_soils','emiss_oceans']

# landfrac file
f1x1='/datalake/NS2345K/olivie/emissions-auxiliary/cases/SOA_r610_PD/atm/hist/SOA_r610_PD.cam.h0.1979-01.nc'
f2x2='/datalake/NS2345K/olivie/emissions-auxiliary/cases/Test149f19_f19/atm/hist/Test149f19_f19.cam.h0.0001-01.nc'
regionlist=['global','LAND','SEA']

#
for species in specieslist :

#   emissions file
    field=readnc.readnc(species,filename)
    longitude=readnc.readnc('lon', filename)
    latitude=readnc.readnc('lat', filename)
    ntime, nlat, nlon = field.shape

#   landfrac file
    if   ( nlat == 192 and nlon == 288 ) : f = f1x1
    elif ( nlat ==  96 and nlon == 144 ) : f = f2x2
    else :
        print('No resolution recognized (nlat, nlon) : ', nlat, nlon)    
        quit()
    landfraction=readnc.readnc('LANDFRAC', f)
    landfrac_longitude = readnc.readnc('lon', f)
    landfrac_latitude  = readnc.readnc('lat', f)

#   checnk whether same longitudes /latitudes  
    print(np.max(latitude-landfrac_latitude), np.min(latitude-landfrac_latitude))
    print(np.max(longitude-landfrac_longitude), np.min(longitude-landfrac_longitude))
#
    for region in regionlist :   

        area=areafraction.areafraction(longitude=longitude,latitude=latitude,region=region,outputtype='area',landfraction=landfraction)

#    nmonth=3192

        series=np.zeros((ntime), dtype=float)

        for imonth in range(ntime) :
            series[imonth] = np.sum(field[imonth,:,:] * area) / Nav * Mwnh3 * 1.e-12 *86400 * 365. *10000.

        print(species, region, np.mean(series[0:11]))
