import netCDF4 as nc
import numpy as np
import datetime


import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

Nav=6.022e23
Mw=2.

file='/scratch/olivie/code/python/cmip6-emissions-gfdl/input/emissions.h2.0.5x0.5.1849-2019.nc'

# read variables
longitude=readnc.readnc('lon',file)
latitude=readnc.readnc('lat',file)
time=readnc.readnc('time',file)
ntime=len(time)

area=areafraction.areafraction(longitude=longitude, latitude=latitude, outputtype='area')

specieslist=['anthro','ocean','soil']
specieslist=['anthro']
#specieslist=['ocean']
#specieslist=['soil']

calendar=readattributenc.readattributenc('time', file, 'calendar')
time_units=readattributenc.readattributenc('time', file, 'units')

dt=nc.num2date(time, time_units, calendar=calendar)

yearlist=np.zeros(ntime, dtype=int)
monthlist=np.zeros(ntime, dtype=int)
for itime in range(ntime) :
    yearlist[itime] = dt[itime].year
    monthlist[itime] = dt[itime].month

    year0=np.min(yearlist)
    year1=np.max(yearlist)
    
for species in specieslist :

    field=readnc.readnc(species,file)
    units=readattributenc.readattributenc(species,file,'units') 

    if ( units != 'molec/cm2/s' ) : 
        print('No units recognized : ', units)
        quit()

    valuelist=np.zeros(ntime, dtype=float)

    for itime in range(ntime) :
        valuelist[itime]=np.sum(area*field[itime,:,:]) / Nav * Mw *1.e-3 * 86400 * 365 *1.e-9 * 1.e4
    
#        print(dt[itime].year, dt[itime].month, globtotal)

    for year in range(year0,year1+1) :
        isubset= ( yearlist == year) 
        annavg=np.mean(valuelist[isubset])
        print(species, year, annavg)
