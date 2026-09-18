import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc


import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc

#
def buildptp(year, var, refvar, overwrite):
#-----------
    '''
    MODIFICATIONS
        (2026-03-27) : add area in output file

    AIM
        - originak file has 12 months (one seasonal cycle) -> generate file for every year between 1979 and 2014 
        - original file has 129 longitudes -> reduce to 128 

    INPUT

    CALLED BY

    CALLS

   ''' 
#



#   period
    cyear=str("%4.4i"% year)
    period=cyear+'01'+'-'+cyear+'12'
#
    dir='/datalake/NS2345K/olivie/noresm/cases-group/esm2025-ch4/data-download/CanESM5'
#
#   1. ORIGINAL FILE
    ptpfile=dir+'/ptp_canesm_tropopause_inPa.nc'
#
    field     = readnc.readnc('TROP',ptpfile)
    latitude  = readnc.readnc('lat',ptpfile)
    longitude = readnc.readnc('lon',ptpfile) # 129 !!! [0., 2.8125, 5.625, ..., 357.1875, 360]
    time      = readnc.readnc('time',ptpfile)

    nlat  = len(latitude)
    nlon  = len(longitude) - 1 # !!!!!!!!!!!!!!!!
    ntime = len(time)

#   REMOVE LAST LONGITUDE
    field = field[0:ntime,0:nlat,0:nlon]

#   2. REFERENCE FILE
    reffile=dir+'/'+refvar+'_AERmon_CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn_'+period+'.nc'
#
#   READ VARIABLES
    latitude =readnc.readnc('lat', reffile)
    longitude=readnc.readnc('lon',reffile)
    time     =readnc.readnc('time', reffile)        

#   ATTRIBUTES
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
    varid.units     = 'Pa'
    varid.long_name = 'Tropopause Air Pressure'
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
    varid[0:nmonth,0:nlat,0:nlon]=field[0:nmonth,0:nlat,0:nlon]

    ds.close()




def buildptploop2(varlist, refvar, year0, year1, overwrite):
#----------------
    '''

    '''
    for var in varlist: 
        for year in range(year0,year1+1) :
            buildptp(year=year, var=var, refvar=refvar, overwrite=overwrite)



def main():
#----------    
    '''
    AIM

    '''
    print('+++ buildptploop +++')
    print('--- buildptploop ---')

    varlist=['ptp']
    refvar='emiach4'
    year0=1979
    year1=2014
    overwrite='True'

    buildptploop2(varlist=varlist, refvar=refvar, year0=year0, year1=year1, overwrite=overwrite)
    

if __name__ == '__main__':
    main()
