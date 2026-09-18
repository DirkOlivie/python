from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys
import datetime


sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lat2latbnds
import lon2lonbnds
import getmonthlength

import getfinalexpidinfo
import getaerocomvarcomponents
import obtainfield

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname


def aerocomize_internal(expid,var,year0,year1,version,freqfile,overwrite=False) :
#---------------------------------------------------------------------
    '''
    INPUT
        expid
        var 
        year0
        year1
        version 
        freqfile : 'monthly' or 'daily'
        overwrite : True or False

    CALLS
        getfinalexpidinfo
        getaerocomvarcomponents
        getexpidinfo
        getbasicexpidname   
        getmonthlength
        obtainfield : is from scripts-python
        lat2latbnds
        lon2lonbnds

    MODIFICATIONS
        (2024-05-24) no_overwrite 

    '''

    print('+++ aerocomize_internal +++')
    print('Expid : ', expid)
    print('var : ', var)
    print('year0 : ', year0)
    print('year1 : ', year1)
    print('version : ', version)
    print('overwrite : ', overwrite)

#   obtain information on the exmeriment
    finalexpidinfo=getfinalexpidinfo.getfinalexpidinfo(expid=expid)

    scenario    = finalexpidinfo['scenario']
    realisation = finalexpidinfo['realisation']
    grid        = finalexpidinfo['grid']
    calendar    = finalexpidinfo['calendar']
    model       = finalexpidinfo['model']

#   making output directory
    path = '/scratch/olivie/code/python/cmip6-aerocomization/'+expid+'/'+version
    if  not os.path.isdir(path) : os.makedirs(path)
#
#   attributes for variable
    varinfo=getaerocomvarcomponents.getaerocomvarcomponents(var=var,expid=expid)
    vtype=varinfo['vtype']
    long_name=varinfo['long_name']

#   reading some information from first file
#-------------------------------------------
    
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid']

    camversion='cam'

#   experiment might be combined : find the correct base    
    yyyy = str("%4.4i"% (year0))

    basicexpid=getbasicexpidname.getbasicexpidname ( cexpid, yyyy+'-01' )
    nc_f=subdir+'/'+basicexpid+'/atm/hist/'+basicexpid+'.'+camversion+'.h0.'+yyyy+'-01.nc'
    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')

    latitude=np.array(nc_fid.variables['lat'][:])  # latitudes
    longitude=np.array(nc_fid.variables['lon'][:])  # longitudes

    hyai=np.array(nc_fid.variables['hyai'][:]) # hyai
    hybi=np.array(nc_fid.variables['hybi'][:]) # hybi

    hyam=np.array(nc_fid.variables['hyam'][:]) # hyam
    hybm=np.array(nc_fid.variables['hybm'][:]) # hybm

    p0_input=np.array(nc_fid.variables['P0'][:]) # reference pressure

    nc_fid.close

    nlon=len(longitude)
    nlat=len(latitude)
    nbnds=2
#
#######################
# create one new file #
#######################
    if ( year0 == year1 ) : cperiod=str("%4.4i"% year0)
    else                  : cperiod=str("%4.4i"% year0)+'-'+str("%4.4i"% year1)
#   aerocom3_NorESM2-met2010_AP3-CTRL-v3-nosoa_od870csaer_Column_2010_monthly.nc    
    fn=path+'/aerocom3_'+model+'_'+scenario+'-'+realisation+'_'+var+'_'+vtype+'_'+cperiod+'_'+freqfile+'.nc'
    print(fn)

    if ( os.path.isfile(fn) and ( overwrite == False) ) : return
#   ds = nc.Dataset(fn, 'w', format='NETCDF4')
    print('File exists : ', os.path.isfile(fn))
    print('Overwrite : ', overwrite)
    print('Type : ', type(overwrite))

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   create dimensions
    time = ds.createDimension('time', None)
    lat = ds.createDimension('lat', nlat)
    lon = ds.createDimension('lon', nlon)
    bnds = ds.createDimension('bnds', nbnds)

#   create variables
    times = ds.createVariable('time', 'f4', ('time',))
    lats = ds.createVariable('lat', 'f4', ('lat',))
    lons = ds.createVariable('lon', 'f4', ('lon',))
    latbnds = ds.createVariable('lat_bnds', 'f4', ('lat','bnds',))
    lonbnds = ds.createVariable('lon_bnds', 'f4', ('lon','bnds',))


#   final field for the variable
    value = ds.createVariable(var, 'f4', ('time', 'lat', 'lon',), fill_value=1.e+20)

#   attributes time
    time_units="days since 0001-01-01 00:00:00"
#    calendar="noleap"

    times.bounds        = "time_bnds"
    times.units         = time_units
    times.calendar      = calendar
    times.axis          = "T"
    times.long_name     = "time"
    times.standard_name = "time"

# attributes lat  
    lats.bounds        = "lat_bnds"
    lats.units         = "degrees_north"
    lats.axis          = "Y"
    lats.long_name     = "Latitude"
    lats.standard_name = "latitude"

# attributes lon
    lons.bounds        = "lon_bnds"
    lons.units         = "degrees_east"
    lons.axis          = "X"
    lons.long_name     = "Longitude"
    lons.standard_name = "longitude"
#
# 
#   information for variable
    value.standard_name = varinfo['long_name']
    value.long_name     = varinfo['long_name']
#
#   GLOBAL ATTRIBUTES
    ds.description = 'Trying global attribute'
#
#   LOOP OVER ALL YEARS
    nyear=year1-year0+1

#   LOOP OVER ALL MONTHS
    nmonth=12
#
#   HOW MANY TIMES
    if ( freqfile == 'monthly' ) : 
        ntime = nyear * nmonth
    elif ( freqfile == 'daily' ) :
        ntime=0
        for year in range(year0,year1+1) :
            for month in range(1,nmonth+1) : 
                ntime = ntime + getmonthlength.getmonthlength(year=year,month=month, calendar=calendar) # get total number of days
    else :
        print('No freqfile recognized : ', freqfile)
        quit() 
#
    timelist=np.zeros( (ntime), dtype=float)

#   LOOP OVER ALL TIMES
    itime=0
    for year in range(year0,year1+1) :
        for month in range(1,nmonth+1) :

#           monthly
            if ( freqfile == 'monthly' ) : 

#               obtain values + units
                D=obtainfield.obtainfield(year=year,month=month,day=None,expid=expid,var=var)

                value[itime,:,:]  =        D['field'][:,:]
            
                date = datetime.datetime(year, month, 15)
                timelist[itime] = nc.date2num(date, time_units, calendar=calendar)

                itime = itime +1

#           daily
            elif ( freqfile == 'daily' ) :           

                monthlength = getmonthlength.getmonthlength(year=year,month=month, calendar=calendar)

                for day in range(1,monthlength+1) :

#                   obtain values + units
                    D=obtainfield.obtainfield(year=year,month=month,day=day,expid=expid,var=var)

                    value[itime,:,:]  =        D['field'][:,:]

                    date = datetime.datetime(year, month, day)
                    timelist[itime] = nc.date2num(date, time_units, calendar=calendar)

                    itime = itime +1
#
            else :
                print('No freqfile recognized : '+freqfile)
                quit()

    times[0:itime] = timelist[0:itime]
#
#   UNITS
    value.units=D['units']    
#
#   LATITUDES / LONGITUDES
    lats[0:nlat] = latitude[0:nlat]
    lons[0:nlon] = longitude[0:nlon]  

#   LAT_BNDS / LON_BNDS 
    latitude_bnds= lat2latbnds.lat2latbnds(latitude=latitude)
    latbnds[:,0] = latitude_bnds[0:nlat]
    latbnds[:,1] = latitude_bnds[1:nlat+1]

    longitude_bnds = lon2lonbnds.lon2lonbnds(longitude=longitude)
    lonbnds[:,0] = longitude_bnds[0:nlon]
    lonbnds[:,1] = longitude_bnds[1:nlon+1]
 #
    ds.close()
