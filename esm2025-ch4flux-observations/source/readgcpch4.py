import netCDF4 as nc
import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')

import readnc
import readattributenc
#import checknan
import year0year1_to_yearlistmonthlist
import getstandardunits
import getconversionfactorunits

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


def readgcpch4(expid) :
#-------------
    '''
    MODIFICATIONS
        (2026-04-25) creation

    ARGUMENTS
    '''
#
    line=expid.split('_')
    model=line[0]
    forcing=line[1]


    print('reading : ', model, forcing)
#
    nmonth=12
#
    filename='/datalake/NS2345K/olivie/methane/GCP-CH4/netcdf_totflux/'+model+'_totflux_'+forcing+'_prognostic.nc'    

    longitude = readnc.readnc('lon',filename)
    latitude  = readnc.readnc('lat',filename)
    timelist  = readnc.readnc('time',filename)

    nlon  = len(longitude)
    nlat  = len(latitude)
    ntime = len(timelist)
#
#   TIME
    time_calendar = readattributenc.readattributenc('time', filename, 'calendar')
    time_units    = readattributenc.readattributenc('time', filename, 'units')
    print('time_calendar : ', time_calendar)    
    print('time_units    : ', time_units)
    if ( time_calendar == '365_day' and time_units == 'months since 2000-1-15 12:00:00' ) : time_calendar='360_day' # ELM-CRU

    yearlist        = np.zeros(ntime, dtype=int)
    monthlist       = np.zeros(ntime, dtype=int)
    decimalyearlist = np.zeros(ntime, dtype=float)


    if ( ( time_units == "years since 0-1-1 00:00:00" and time_calendar == "standard") \
      or ( time_units == "years since 0-1-1"          and time_calendar == "standard") ) : # 2000.04166666667, 2000.11979708035, 2000.20833

        for itime in range(ntime) :
            yearlist[itime] = int(timelist[itime])
            monthlist[itime]   = round(( ( timelist[itime] - float(yearlist[itime]) ) + 1./24. ) * 12.)

            decimalyearlist[itime] = float(yearlist[itime]) + ( float(monthlist[itime])-0.5 ) / 12.

    elif ( "since" in time_units ) :  

        if ( time_units == "months since 1860-01-01 00:00:00" and time_calendar == "standard" ) : time_calendar = "360_day"
        if ( time_units == "months since 1860-01-01"          and time_calendar == "standard" ) : time_calendar = "360_day"
#        if ( time_units == "years since 0-1-1 00:00:00"       and time_calendar == "standard" ) : 

        for itime in range(ntime) :
            tmp = nc.num2date(timelist[itime], time_units, calendar=time_calendar)

            yearlist[       itime] = tmp.year
            monthlist[      itime] = tmp.month
            decimalyearlist[itime] = float(tmp.year) + ( float(tmp.month)-0.5 ) / 12.

    elif ( time_units == "day as %Y%m%d.%f" ) : 

        for itime in range(ntime) :
            yyyymmdd = int(timelist[itime])            

            yearlist[       itime] = yyyymmdd // 10000
            monthlist[      itime] = (yyyymmdd % 10000 ) // 100
            decimalyearlist[itime] = float(yearlist[itime]) + ( float(monthlist[itime])-0.5 ) / 12.

    elif ( time_units == "month as %Y%m.%f" ) : 

        for itime in range(ntime) :
            yyyymm = int(timelist[itime])            

            yearlist[       itime] = yyyymm // 100
            monthlist[      itime] = yyyymm % 100 
            decimalyearlist[itime] = float(yearlist[itime]) + ( float(monthlist[itime])-0.5 ) / 12.

    else :
        print('+++ readgcpch4 +++')
        print('No time units recognized : ', time_units)
        quit()
#
    print(yearlist)
    print(monthlist)
#
#   read the data
    field  = readnc.readnc('totflux', filename)

#   read the units
    if ( expid == 'ORCHIDEE_CRU' \
      or expid == 'ORCHIDEE_GSWP3' ) : units = 'kg m-2 s-1'
    else : units = readattributenc.readattributenc('totflux', filename, 'units')

#   standard writing of units
    units = getstandardunits.getstandardunits(units=units)

#   units I would like to have
    finalunits='kg m-2 s-1'        
    factor = getconversionfactorunits.getconversionfactorunits(origunits=units, finalunits=finalunits)
#
#   apply factor for final units
    field=field*factor    
#
#   check for nan
    field = np.where(field >  1.e-5, 0., field)
    field = np.where(field < -1.e-5, 0., field)
#
#   area
    area=areafraction.areafraction(latitude=latitude, longitude=longitude, outputtype='area') # m2

#   structure
    data = { 'variable'  : 'ch4', \
             'expid'     : expid, \
             'fileorigin': 'gcp-ch4', \
             'field'     : field, \
             'units'     : finalunits, \
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
#    for itime in range(ntime) :
#        print(itime, np.max(field[itime,:,:]))
#
#    quit()
 
    return data
