import matplotlib.pyplot as plt
import os
import numpy as np
from netCDF4 import Dataset

import getmolarweight

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

#
# AIM
#   calculating global means of emissions fikes    
#
#

def read_emissions_series(file, variable) :
#----------------------------------------

    Nav=6.022e23

    nc_fid= Dataset(file, 'r')
    lats=np.array(nc_fid.variables['lat'][:])          # latitudes
    lons=np.array(nc_fid.variables['lon'][:])          # longitudes
    field=np.array(nc_fid.variables[variable][:])
    yyyymmddlist=np.array(nc_fid.variables['date'][:]) # dates (YYYYMMDD)
    nc_fid.close

    units=nc_fid.variables[variable].units
    long_name=nc_fid.variables[variable].long_name
#    molecular_weight=nc_fid.variables[variable].molecular_weight # only exists for CESM files

    ntime, nlat, nlon = field.shape

#   left out landfraction argument
    area = areafraction.areafraction(latitude=lats, longitude=lons, outputtype='area', region='glob')
#
#   get molarweight
    Mw = getmolarweight.getmolarweight(long_name=long_name)

#  
    if ( units != 'molecules/cm2/s' \
     and units != 'molecules cm-2 s-1' ) : 

        print('Units not in correct format')
        quit()

#   create global timeseries
    valuelist=np.zeros((ntime))
    yearlist=np.zeros((ntime))
    monthlist=np.zeros((ntime))
    decimalyearlist=np.zeros((ntime))        

    for itime in range(ntime) :
        valuelist[itime]= np.sum(field[itime,:,:]*area[:,:]) * 10000. / Nav * Mw * 1e-12 * 86400. * 365. 
                   # cm-2 -> m-2  
                   # molecules s-1 -> mole s-1 -> gram s-1 
                   # gram s-1 -> Tg yr-1

        yearlist[itime]        = yyyymmddlist[itime] // 10000
        monthlist[itime]       = ( yyyymmddlist[itime] % 10000 ) // 100
        decimalyearlist[itime] = float(yearlist[itime]) + ( float(monthlist[itime]) - 0.5 ) / 12.
    
    newunits='Tg yr-1'
#
#
    data={'file'     : file, \
          'variable' : variable, \
          'units'    : newunits, \
          'yearlist' : np.array(yearlist), \
          'monthlist': np.array(monthlist), \
          'timelist' : np.array(decimalyearlist), \
          'valuelist': np.array(valuelist), \
          'ntime'    : ntime}
#
    return data
