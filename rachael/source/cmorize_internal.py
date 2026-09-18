from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys
import datetime


import experimentdefinition

import lat2latbnds
import lon2lonbnds

import getfinalexpidinfo
#import getattributeinfo
import getonlineattributeinfo
import obtainfield

def cmorize_internal(expid,var,realm,overwrite=True) :
#-----------------------------------------------------
    '''
    INPUT


    MODIFICATIONS
        (2024-05-24) no_overwrite 

    '''

    print('Expid : ', expid)
    plevlist = [100000., 92500., 85000., 70000., 60000., 50000., 40000., 30000., 25000., \
             20000., 15000., 10000., 7000., 5000., 3000., 2000., 1000., 500., 100.]

#   obtain information on the exmeriment
    finalexpidinfo=getfinalexpidinfo.getfinalexpidinfo(expid=expid)

    year0=finalexpidinfo['year0']
    year1=finalexpidinfo['year1']
    scenario=finalexpidinfo['scenario']
    realisation=finalexpidinfo['realisation']
    grid=finalexpidinfo['grid']
    freqfile=finalexpidinfo['freqfile']
    model=finalexpidinfo['model']

#   making output directory
    path = '/scratch/olivie/code/python/cmip6-cmorization/'+expid
    if  not os.path.isdir(path) : os.mkdir(path)
#
#   attributes for variable
    attributeinfo=getonlineattributeinfo.getonlineattributeinfo(var=var, realm=realm)
    cdim=attributeinfo['cdim']
    desiredunits=attributeinfo['units']

#   reading some information from first file
#-------------------------------------------
    
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid']

    camversion='cam'

    yyyy = str("%4.4i"% (year1))
    nc_f=subdir+'/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.h0.'+yyyy+'-01.nc'
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
    if ( cdim == '3d' ) : nlev=len(hyam)
    elif (cdim == '3d-plev19' ) : nlev=len(plevlist)
#
#------------------------------------------
#    realm=getrealm.getrealm(var=var, freqfile=freqfile)

#   attributes for variable
#   attributeinfo=getattributeinfo.getattributeinfo(var=var)
#    attributeinfo=getonlineattributeinfo.getonlineattributeinfo(var=var, realm=realm)
#
#######################
# create one new file #
#######################
    cyear0=str("%4.4i"% year0)
    cyear1=str("%4.4i"% year1)

    period=cyear0+'01-'+cyear1+'12'
#    
    fn=path+'/'+var+'_'+realm+'_'+model+'_'+scenario+'_'+realisation+'_'+grid+'_'+period+'.nc'

    if ( os.path.isfile(fn) and not overwrite ) : return
#   ds = nc.Dataset(fn, 'w', format='NETCDF4')
    print(fn)

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   create dimensions
    time = ds.createDimension('time', None)
    lat = ds.createDimension('lat', nlat)
    lon = ds.createDimension('lon', nlon)
    bnds = ds.createDimension('bnds', nbnds)
    if ( cdim == '3d' ) : lev = ds.createDimension('lev', nlev)
    elif (cdim == '3d-plev19' ) : lev = ds.createDimension('plev', nlev)

#   create variables
    times = ds.createVariable('time', 'f4', ('time',))
    lats = ds.createVariable('lat', 'f4', ('lat',))
    lons = ds.createVariable('lon', 'f4', ('lon',))
    latbnds = ds.createVariable('lat_bnds', 'f4', ('lat','bnds',))
    lonbnds = ds.createVariable('lon_bnds', 'f4', ('lon','bnds',))

    if ( cdim == '3d' ) : 
        levs=ds.createVariable('lev', 'f4', ('lev',))
        levbnds=ds.createVariable('lev_bnds', 'f4', ('lev','bnds',))
        p0=ds.createVariable('p0', 'f4')
        a=ds.createVariable('a','f4', ('lev',))
        b=ds.createVariable('b','f4', ('lev',))
        abnds=ds.createVariable('a_bnds','f4', ('lev','bnds',))
        bbnds=ds.createVariable('b_bnds','f4', ('lev','bnds',))        
        ps=ds.createVariable('ps','f4', ('time', 'lat', 'lon',), fill_value=1.e+20)
    elif ( cdim == '3d-plev19' ) : 
        plevs=ds.createVariable('plev', 'f4', ('plev',))

#   final field for the variable
    if (   cdim == '2d'        ) : value = ds.createVariable(var, 'f4', ('time', 'lat', 'lon',), fill_value=1.e+20)
    elif ( cdim == '3d'        ) : value = ds.createVariable(var, 'f4', ('time', 'lev', 'lat', 'lon',), fill_value=1.e+20)
    elif ( cdim == '3d-plev19' ) : value = ds.createVariable(var, 'f4', ('time', 'plev', 'lat', 'lon',), fill_value=1.e+20)
    else : 
        print('No dimension description recognized : ', cdim)
        quit()

#   attributes time
    time_units="days since 0001-01-01 00:00:00"
    calendar="noleap"

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
    if ( cdim == '3d' ) :
#       attributes lev
        levs.bounds = "lev_bnds" 
        levs.units = "1" 
        levs.axis = "Z" 
        levs.positive = "down" 
        levs.long_name = "hybrid sigma pressure coordinate" 
        levs.standard_name = "atmosphere_hybrid_sigma_pressure_coordinate" 
        levs.formula = 'p = a*p0 + b*ps' 
        levs.formula_terms = 'p0: p0 a: a b: b ps: ps' 
#       attributes levbnds
        levbnds.formula       = 'p = a*p0 + b*ps'
        levbnds.standard_name = 'atmosphere_hybrid_sigma_pressure_coordinate'
        levbnds.units         = '1'
        levbnds.formula_terms = 'p0: p0 a: a_bnds b: b_bnds ps: ps'
#       attributes p0
        p0.standard_name = "reference_air_pressure_for_atmosphere_vertical_coordinate" 
        p0.long_name = "vertical coordinate formula term: reference pressure" 
        p0.units = "Pa" 

#       hyam
        a.long_name = "vertical coordinate formula term: a" 
#       hybm
        b.long_name = "vertical coordinate formula term: b" 
#       ps
        ps.standard_name = "air_pressure" 
        ps.long_name = "Surface Air Pressure" 
        ps.units = "Pa" 
#       hyai
        abnds.long_name = "vertical coordinate formula term: a(k+1/2)" 
#       hybi
        bbnds.long_name = "vertical coordinate formula term: b(k+1/2)" 
    elif ( cdim == '3d-plev19' ) :
#       attributes plev
        plevs.axis = "Z" 
        plevs.positive = "down"
        plevs.long_name = "pressure"
        plevs.standard_name = "air_pressure" 

#   information for variable
    value.standard_name = attributeinfo['standard_name']
    value.long_name     = attributeinfo['long_name']
#   value.comment       = var_comment
#    value.units         = var_units
#    value.original_name = var_original_name
#    value.cell_methods  = var_cell_methods
#    value.cell_measures = var_cell_measures
#   value.history       = var_history
#   value.coordinates   = var_coordinates
#    value.missing_value = var_missing_value
#    value._FillValue    = var__FillValue  # should be done during creation of value
#
# GLOBAL ATTRIBUTES
#
    ds.description = 'Trying global attribute'
#    ds.source_id = 'Trying global attribute'
#    ds.brol = 'Trying global attribute'
#
#   DATES
    nmonth=12
    nyear=year1-year0+1

    ntime=nyear*nmonth
    timelist=np.zeros( (ntime ), dtype=float)
    itime=0
    for iyear in range(0,nyear) : 
        year=year0+iyear
        for imonth in range(0,nmonth) :
            month=imonth+1

#           obtain values + units
            D=obtainfield.obtainfield(year=year,month=month,expid=expid,var=var,desiredunits=desiredunits,cdim=cdim)

            print('cdim : ', cdim)
            if   ( cdim == '2d' )        : value[itime,:,:]  =        D['field'][:,:]
            elif ( cdim == '3d' )        : value[itime,:,:,:]=np.flip(D['field'][:,:,:], axis=0) # flipping vertical axis
            elif ( cdim == '3d-plev19' ) : value[itime,:,:,:]=        D['field'][:,:,:]
            else :
                quit() 

#           surface pressure (only for 3D fields)
            if ( cdim == '3d' ) :
                D=obtainfield.obtainfield(year=year,month=month,expid=expid,var='ps',desiredunits='Pa',cdim='2d') # surface pressure
                ps[itime,:,:]=D['field'][:,:]

#           fille the time
            date = datetime.datetime(year, month, 15)
            timelist[itime] = nc.date2num(date, time_units, calendar=calendar)


            itime=itime+1

    times[0:ntime] = timelist[0:ntime]
#
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

#   LEVELS
    if ( cdim == '3d' ) :
#       levels
        levs[:]      = np.flip( p0_input * hyam[:]        + 101325. * hybm[:]        ) / 101325.    # FLIPPED !
#       levbnds 
        levbnds[:,1] = np.flip( p0_input * hyai[0:nlev]   + 101325. * hybi[0:nlev]   ) / 101325.    # FLIPPED !
        levbnds[:,0] = np.flip( p0_input * hyai[1:nlev+1] + 101325. * hybi[1:nlev+1] ) / 101325.    # FLIPPED !
#       p0
        p0[:]        = p0_input
#       hyam  
        a[:]         = np.flip( hyam[:] )
#       hyai
        abnds[:,1]   = np.flip( hyai[0:nlev]   )
        abnds[:,0]   = np.flip( hyai[1:nlev+1] )
#       hybm
        b[:]         = np.flip( hybm[:] )
#       hybi
        bbnds[:,1]   = np.flip( hybi[0:nlev]   )
        bbnds[:,0]   = np.flip( hybi[1:nlev+1] )
    elif ( cdim == '3d-plev19' ) :
        plevs[0:nlev] = plevlist[0:nlev]

 #
    ds.close()
