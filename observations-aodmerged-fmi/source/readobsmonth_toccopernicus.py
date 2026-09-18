from netCDF4 import Dataset
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits

def readobsmonth_toccopernicus(var, year, month):
#-----------------------------
    '''
    REMARK
        197004-197812 : 181x240, version v0023
        197901-201812 : 361x720, version v0023
        201912-202112 : 361x720, version v0024  (201812 has also v0024 version)
        202201-202212 : 361x720, version v0025

        Fill_value is "0", so have to select on that to define the mask 

    CALLED BY
        readobsmodelperiod

    CALLS
       readnc

    DATA TO READ
        period : 197004-202212, one file per month
        variables : total_ozone_column, total_ozone_column_standard_deviation
        resolution : 361x720 (0.5x0.5 degree)

    RETURNS structure
        var 
        field
        mask : if field variable is not finite, then mask (and field) is put to 0
    '''

    dir='/projects/NS9560K/users/olivie/observations/toccopernicus/v20240209'
    cyear =str("%4.4i"% (year)) 
    cmonth=str("%2.2i"% (month))
#
    print('+++ readobsmonth_toccopernicus +++')
    print('Reading ')
    print('Var   : ', var)
    print('Year  : ', cyear)
    print('Month : ', cmonth)
#
#   filenames : different years have different version
    if ( year < 1979 ) :
        print, 'Data on lower resolution - not implemented for now'
        quit()
    elif ( 1979 <= year and year <= 2018 ) :
        version='v0023'
    elif ( 2019 <= year and year <= 2021 ) :
        version='v0024'
    elif ( 2022 <= year and year <= 2022 ) :
        version='v0025'
    else : 
        print, 'No year recognized : ', year
        quit()

    nc_f=dir+'/'+cyear+cmonth+'-C3S-L4_OZONE-O3_PRODUCTS-MSR-ASSIM-ALG-MONTHLY-'+version+'.nc'
    print('File to read : ', nc_f)

    if ( var == 'toc' ) :
        cvar='total_ozone_column'
    else :
        print('No variable recognized : '+var)
        quit()

    nc_fid= Dataset(nc_f, 'r') # open NetCDF file

    field=np.squeeze(np.array(nc_fid.variables[cvar][:]))
    units=nc_fid.variables[cvar].units
    latitude=np.array(nc_fid.variables['latitude'][:])  # latitudes
    longitude=np.array(nc_fid.variables['longitude'][:])  # longitudes

    nc_fid.close # close NetCDF file

    nlon=len(longitude)
    nlat=len(latitude)
#   
    units=getstandardunits.getstandardunits(units=units)

#   geneate mask
    mask=np.zeros([nlon,nlat],dtype=float)
    mask=np.where(field == 0., 0., 1.)      # fill_value is zero : use that to create the mask 

    print, '# points without observation : ', nlon*nlat - np.sum(mask)

    data = { 'var'   : var, \
             'field' : field, \
             'units' : units, \
             'longitude' : longitude, \
             'latitude'  : latitude, \
             'mask'      : mask}

    return data
