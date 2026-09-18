from netCDF4 import Dataset
import numpy as np
import time

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits

def readobsmonth_aodmergedfmi(var, year, month):
#----------------------------
    '''
    CALLED BY
        readobsmodelperiod

    CALLS
        readnc

    DATA TO READ
        period : 1995-2017, one file per year
        variables : od550aer, od550aer_unc (=uncertainty)
        resolution : 180x360 (1x1 degree)

    MISSING VALUES
        missing values are NaN in the NetCDF file

    RETURNS structure
        var 
        field
        mask : if field variable is not finite, then mask (and field) is put to 

   '''

    dir='/projects/NS9560K/users/olivie/observations/aodmerged-fmi'
    cyear =str("%4.4i"% (year)) 
    cmonth=str("%2.2i"% (month))
#
    print('+++ readobsmonth_aodmergedfmi +++')
    print('Reading ')
    print('Var   : ', var)
    print('Year  : ', cyear)
    print('Month : ', cmonth)
#
    nc_f=dir+'/FMI_SAT_AOD-MERGED-L3_Ver1.0_Column_od550aer_'+cyear+'_monthly.nc'
    print('File to read : ', nc_f)

#   variable named used in the NetCDF file
    if ( var == 'od550aer' ) :
        cvar=var
    else :
        print('No variable recognized : '+var)
        quit()

    nc_fid= Dataset(nc_f, 'r') # open NetCDF file

    field=np.squeeze(np.array(nc_fid.variables[cvar][:]))
    units=nc_fid.variables[cvar].units
    latitude=np.array(nc_fid.variables['lat'][:])  # latitudes
    longitude=np.array(nc_fid.variables['lon'][:])  # longitudes

    nc_fid.close # close NetCDF file

    nlon=len(longitude)
    nlat=len(latitude)
#   
    units=getstandardunits.getstandardunits(units=units)

#   select the correct month
    imonth=month-1
    field=field[imonth,:,:]
    mask=np.zeros([nlat,nlon],dtype=float)


#   generate mask : it should be checked on "not a finite value" - maybe good to set the value then to zero (see IDL version)
    mask=np.zeros([nlat,nlon],dtype=float)
    mask=np.where(np.isnan(field), 0., 1.)      # fill_value is zero : use that to create the mask 
    field=np.where(mask == 0., 0., field)

#    print('MASK')
#    print(mask)
#
#    for ilon in range(nlon) :
#        for ilat in range(nlat) :
#            print(ilon, ilat, field[ilat,ilon], mask[ilat,ilon])
#            time.sleep(0.01)
#    quit()

    print('# points (total)              : ' , nlon*nlat)
    print('# points (with observations)   : ',             np.sum(mask))
    print('# points (without observation) : ', nlon*nlat - np.sum(mask))

#    time.sleep(0.1)

    data = { 'var'   : var, \
             'field' : field, \
             'units' : units, \
             'longitude' : longitude, \
             'latitude'  : latitude, \
             'mask'      : mask}

    return data
