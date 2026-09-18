import netCDF4 as nc
import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')

import readnc
import readattributenc
import readndimnc
import readdimensionsnc
import getstandardunits

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


def readgiemsmc(variable) :
#--------------
    '''
    MODIFICATIONS
        (2026-07-23) creation

    ARGUMENTS
    '''
#
    nmonth=12

#   FILE
    filename='/datalake/NS2345K/olivie/methane/GIEMS-MC/GIEMS-MC_compressed_v1.1.nc'    
#
#   DIMENSIONS
    longitude = readnc.readnc('longitude' ,filename)  # longitude
    latitude  = readnc.readnc('latitude' ,filename)  # latitude
    timelist  = readnc.readnc('time',filename) # time 0, 31, 60, 91, 121, 152, 182, ... : FIRST DAY OF MONTH

    nlon  = len(longitude)
    nlat  = len(latitude)
    ntime = len(timelist)
#
#   TIME
    time_calendar = readattributenc.readattributenc('time', filename, 'calendar') # proleptic_gregorian
    time_units    = readattributenc.readattributenc('time', filename, 'units')    #
    print('time_calendar : ', time_calendar)    
    print('time_units    : ', time_units)

    yearlist        = np.zeros(ntime, dtype=int)
    monthlist       = np.zeros(ntime, dtype=int)
    decimalyearlist = np.zeros(ntime, dtype=float)

    for itime in range(ntime) :
        tmp = nc.num2date(timelist[itime], time_units, calendar=time_calendar)

        yearlist[       itime] = tmp.year
        monthlist[      itime] = tmp.month
        decimalyearlist[itime] = float(tmp.year) + ( float(tmp.month)-0.5 ) / 12.
#
    print(yearlist)
    print(monthlist)
#
#   READ THE DATA
    field  = readnc.readnc(variable, filename, auto_mask=False)
    units = readattributenc.readattributenc(variable, filename, 'units')
    dimensions = readdimensionsnc.readdimensionsnc(variable, filename)
    ndim = readndimnc.readndimnc(variable, filename)
#
    if   ( ndim == 3 and 'time' in dimensions ) : 
        ntime=ntime
        freqtype='monthly'
    elif ( ndim == 3 and 'month' in dimensions ) : 
        ntime=12
        yearlist=np.zeros(ntime, dtype=int)
        monthlist=np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype=int)
        decimalyearlist=(monthlist-0.5)/12.
        freqtype='seasonalcycle'
    elif ( ndim == 2 ) : 
        ntime=0
        yearlist=[]
        monthlist=[]
        decimalyearlist=[]
        freqtype='fixed'
    else :
        print('No ndim and dimensions recognized : ', ndim, dimensions)
        quit()

#   standard writing of units
    units = getstandardunits.getstandardunits(units=units)
#
#   check for nan
    field = np.where(field < 0., 0., field)
#
#   area
    area=areafraction.areafraction(latitude=latitude, longitude=longitude, outputtype='area') # m2

#   structure
    data = { 'variable'  : variable, \
             'expid'     : '', \
             'fileorigin': 'giems-mc', \
             'field'     : field, \
             'units'     : units, \
             'area'      : area, \
             'areaunits' : 'm2', \
             'longitude' : longitude, \
             'latitude'  : latitude, \
             'yearlist'  : yearlist, \
             'monthlist' : monthlist, \
             'timelist'  : decimalyearlist, \
             'freqtype'  : 'monthly', \
             'ntime'     : ntime}
#  
    return data
