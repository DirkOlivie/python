import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import datetime
import glob


import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc

#
def buildemiach4corr(year, var, refvar, overwrite):
#------------------
    '''
    MODIFICATIONS
        (2026-04-02) : add area in output file

    AIM
        - original file has 1982 months [dec 1849, jan 1850, ... dec 2014, jan 2015] -> generate file for every year between 1979 and 2014 
        - original file has 129 longitudes -> reduce to 128 
        - original file : calendar days since 1849-12-01

    REFERENCE FILE
        - has 12 months
        - calendar days since 1850-01-01

    INPUT

    CALLED BY

    CALLS

   ''' 
#
#   period
    cyear=str("%4.4i"% year)
    period=cyear+'01'+'-'+cyear+'12'
#
    dir='/datalake/NS2345K/olivie/noresm/cases-group/esm2025-ch4/data-download/CanESM5/amip-CH4ems'
#
#   1. ORIGINAL FILE 184912-201501
    origfile=dir+'/emiach4_cmip6_canesm.nc'
#
    field         = readnc.readnc('emiach4',origfile)
    latitude      = readnc.readnc('lat',origfile)
    longitude     = readnc.readnc('lon',origfile) # 129 !!! [0., 2.8125, 5.625, ..., 357.1875, 360]
    time_origfile = readnc.readnc('time',origfile)

    time_units_origfile = readattributenc.readattributenc('time',origfile,'units')
    calendar_origfile   = readattributenc.readattributenc('time',origfile,'calendar') # days since 1849-12-01

    nlat  = len(latitude)
    nlon  = len(longitude) - 1 # !!!!!!!!!!!!!!!!
    ntime = len(time_origfile)

#   find itime0 and itime1
    for itime in range(ntime) :
        dt=nc.num2date(time_origfile[itime], time_units_origfile, calendar=calendar_origfile)
        if ( dt.year == year and dt.month == 1  ) : itime0=itime
        if ( dt.year == year and dt.month == 12 ) : itime1=itime

#   REMOVE LAST LONGITUDE
    field = field[0:ntime,0:nlat,0:nlon]

#   2. REFERENCE ANNUAL FILE
    reffile=dir+'/'+refvar+'_AERmon_CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn_'+period+'.nc'
#
#   READ VARIABLES
    latitude =readnc.readnc('lat', reffile)
    longitude=readnc.readnc('lon', reffile)
    time     =readnc.readnc('time', reffile)        

#   ATTRIBUTES
    emiach4_standard_name = readattributenc.readattributenc('emiach4', reffile,'standard_name')
    emiach4_long_name     = readattributenc.readattributenc('emiach4', reffile,'long_name')
    emiach4_units         = readattributenc.readattributenc('emiach4', reffile,'units')
    emiach4_original_name = readattributenc.readattributenc('emiach4', reffile,'original_name')
    emiach4_cell_methods  = readattributenc.readattributenc('emiach4', reffile,'cell_methods')
    emiach4_cell_measures = readattributenc.readattributenc('emiach4', reffile,'cell_measures')
    emiach4_history       = readattributenc.readattributenc('emiach4', reffile,'history')
    emiach4_missing_value = readattributenc.readattributenc('emiach4', reffile,'missing_value')
    emiach4_FillValue     = readattributenc.readattributenc('emiach4', reffile,'_FillValue')

#   latitude
    latitude_bounds        = readattributenc.readattributenc('lat', reffile,'bounds')
    latitude_units         = readattributenc.readattributenc('lat', reffile,'units')
    latitude_axis          = readattributenc.readattributenc('lat', reffile,'axis')
    latitude_long_name     = readattributenc.readattributenc('lat', reffile,'long_name')
    latitude_standard_name = readattributenc.readattributenc('lat', reffile,'standard_name')
#   longitude
    longitude_bounds        = readattributenc.readattributenc('lon', reffile,'bounds')
    longitude_units         = readattributenc.readattributenc('lon', reffile,'units')
    longitude_axis          = readattributenc.readattributenc('lon', reffile,'axis')
    longitude_long_name     = readattributenc.readattributenc('lon', reffile,'long_name')
    longitude_standard_name = readattributenc.readattributenc('lon', reffile,'standard_name')
#   time
    time_bounds        = readattributenc.readattributenc('time', reffile,'bounds')
    time_units         = readattributenc.readattributenc('time', reffile,'units')
    time_calendar      = readattributenc.readattributenc('time', reffile,'calendar')
    time_axis          = readattributenc.readattributenc('time', reffile,'axis')
    time_long_name     = readattributenc.readattributenc('time', reffile,'long_name')
    time_standard_name = readattributenc.readattributenc('time', reffile,'standard_name')
    
    nlon=len(longitude)
    nlat=len(latitude)
    ntime=len(time)
#
#
##############
#   New file #
##############
    filename=var+'_AERmon_CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn_'+period+'.nc'

#   create new NetCDF file
    fn = dir+'/'+filename    
#
#   no overwriting
    if ( os.path.isfile(fn) and ( overwrite == False) ) : return

    print('File exists : ', os.path.isfile(fn))
    print('Overwrite : ', overwrite)
    print('Type : ', type(overwrite))

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

######################
#   CreateDimensions #
######################
#
#   horizontal
    londimid = ds.createDimension('lon', nlon)
    latdimid = ds.createDimension('lat', nlat)

#   time
    timedimid = ds.createDimension('time', None)

######################
#   Define variables #
######################
# 
#   horizontal
    latid  = ds.createVariable('lat' , 'f8', ('lat',))
    lonid  = ds.createVariable('lon' , 'f8', ('lon',))
#   time
    timeid = ds.createVariable('time', 'f8', ('time',))
#
#   name of emissions will be name of sector
    varid = ds.createVariable(var,'f4', ('time','lat','lon',))
# 
################
#   ATTRIBUTES #
################
#   latitude
    latid.bounds        = latitude_bounds
    latid.units         = latitude_units
    latid.axis          = latitude_axis
    latid.long_name     = latitude_long_name
    latid.standard_name = latitude_standard_name
#   longitude
    lonid.bounds        = longitude_bounds
    lonid.units         = longitude_units
    lonid.axis          = longitude_axis
    lonid.long_name     = longitude_long_name
    lonid.standard_name = longitude_standard_name
#   time
    timeid.bounds        = time_bounds
    timeid.units         = time_units
    timeid.axis          = time_axis
    timeid.long_name     = time_long_name
    timeid.standard_name = time_standard_name
#   species
    varid.units         = emiach4_units
    varid.long_name     = emiach4_long_name
    varid.standard_name = emiach4_standard_name
    varid.original_name = emiach4_original_name
    varid.cell_methods  = emiach4_cell_methods
    varid.cell_measures = emiach4_cell_measures
    varid.history       = emiach4_history
    varid.missing_value = emiach4_missing_value
#
#   global data   
    ds.domxmin, = longitude[0], 

##################
#   WRITE FIELDS #
##################
#
#   Fill the lat/lon/lev variables
    latid[0:nlat] = latitude[0:nlat]
    lonid[0:nlon] = longitude[0:nlon]

    nmonth=12
    varid[ 0:nmonth,0:nlat,0:nlon] = field[itime0:itime1+1,0:nlat,0:nlon]

    timeid[0:nmonth] = time[0:nmonth]

    ds.close()




def buildemiach4corrloop2(varlist, refvar, year0, year1, overwrite):
#-------------------
    '''

    '''
    for var in varlist: 
        for year in range(year0,year1+1) :
            buildemiach4corr(year=year, var=var, refvar=refvar, overwrite=overwrite)



def main():
#----------    
    '''
    AIM

    '''
    print('+++ buildemiach4corrloop +++')
    print('--- buildemiach4corrloop ---')

    varlist=['emiach4corr']
    refvar='emiach4'
    year0=1979
    year1=2014
    overwrite='True'

    buildemiach4corrloop2(varlist=varlist, refvar=refvar, year0=year0, year1=year1, overwrite=overwrite)
    

if __name__ == '__main__':
    main()
