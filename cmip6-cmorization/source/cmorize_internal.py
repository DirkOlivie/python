from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys
import datetime


sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition
import areafraction

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lat2latbnds
import lon2lonbnds

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname

import getfinalexpidinfo
import getattributeinfo
import obtainfield

def cmorize_internal(expid,var,freqfile,realm,version,filenameformat,prodlossunits,overwrite=False) :
#-------------------
    '''
    INPUT
        expid
        var
        freqfile
        realm
        version
        filenameformat : 'cmor' | 'hyway'
        prodlossunits  : 'hyway'
        overwrite      : True | False

    CALLS
        getfinalexpidinfo
        getattributeinfo
        getonlineattributeinfo
        getexpidinfo
        areafraction
        obtainfield
        lat2latbnds
        lon2lonbnds


    MODIFICATIONS
        (2024-05-24) no_overwrite 
        (2024-10-01) bug correction (previously all 3D fields had Pa as unit, taken from ps field)
        (2024-12-09) added possibility for variables which are not in offical cmortables (e.g., h2)
        (2025-05-21) added 
        (2024-06-27) reading info from basicexpidname
        (2026-02-07) modified day-since and calendar

    '''

    print('+++ cmorize_internal +++')
    print('expid          : ', expid)
    print('var            : ', var)
    print('freqfile       : ', freqfile)
    print('realm          : ', realm)
    print('version        : ', version)
    print('filenameformat : ', filenameformat)
    print('overwrite      : ', overwrite)

#   pressure levels
    plevlist = [100000., 92500., 85000., 70000., 60000., 50000., 40000., 30000., 25000., \
             20000., 15000., 10000., 7000., 5000., 3000., 2000., 1000., 500., 100.]

#   z levels (for Jan)
    zlevlist = [ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, \
                10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5 ] 

#   obtain information on the exmeriment
    finalexpidinfo=getfinalexpidinfo.getfinalexpidinfo(expid=expid)

    year0       = finalexpidinfo['year0']
    year1       = finalexpidinfo['year1']
    scenario    = finalexpidinfo['scenario']
    realisation = finalexpidinfo['realisation']
    grid        = finalexpidinfo['grid']
#    freqfile=finalexpidinfo['freqfile'] # e.g., monthly
    model=finalexpidinfo['model']

#   making output directory
    path = '/scratch/olivie/code/python/cmip6-cmorization/'+expid+'/'+version+'/'+scenario+'/'+realm
    if  not os.path.isdir(path) : os.makedirs(path)
#
#   attributes for variable
    attributeinfo=getattributeinfo.getattributeinfo(var=var, realm=realm)

#   correct units for HYWAY : mol m-3 s-1 -> kg m-3 s-1
#--------------------------
    if ( ( 'loss' in var or 'prod' in var ) and ( prodlossunits=='hyway' ) and ( attributeinfo['units'] == 'mol m-3 s-1' ) ) :
        attributeinfo['units'] = 'kg m-3 s-1'

    cdim=attributeinfo['cdim']
    desiredunits=attributeinfo['units']

#   reading some information from first monthly file
#---------------------------------------------------
   
    yyyy = str("%4.4i"% (year1))
 
    expidinfo=experimentdefinition.getexpidinfo(expid=getbasicexpidname.getbasicexpidname(expid=expid,date=yyyy+'-01')) # use basicexpidname
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
    if (   cdim == '3d'        ) : nlev=len(hyam)
    elif ( cdim == '3d-half'   ) : nlev=len(hyai)
    elif ( cdim == '3d-plev19' ) : nlev=len(plevlist)
    elif ( cdim == '3d-zlev20' ) : nlev=len(zlevlist)
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
#   filename
    if ( freqfile == 'monthly' ) : 
        if (   filenameformat == 'cmor'  ) : fn=path+'/'+var+'_'+realm+'_'+model+'_'+scenario+'_'+realisation+'_'+grid+'_'+period+'.nc'
        elif ( filenameformat == 'hyway' ) : fn=path+'/'+var+'_'+freqfile+'_'+model+'_hyway_'+scenario+'_'+realisation+'_'+period+'.nc' 
        else :
            print('No filenameformat recognized : ', filenameformat)
            quit()
    elif ( freqfile == '3hourly' ) : 
        if ( filenameformat == 'hyway' ) : fn=path+'/'+var+'_'+freqfile+'_'+model+'_hyway_'+scenario+'_'+realisation+'_'+period+'.nc' 
        else :
            print('No filenameformat recognized : ', filenameformat)
            quit()
    elif ( freqfile == 'fixed' ) : 
        if (   filenameformat == 'cmor'  ) : fn=path+'/'+var+'_'+realm+'_'+model+'_'+scenario+'_'+realisation+'_'+grid+'.nc'
        elif ( filenameformat == 'hyway' ) : fn=path+'/'+var+'_fixed_'+model+'_hyway.nc'
        else :
            print('No filenameformat recognized : ', filenameformat)
            quit()
    else :
        print('No freqfile recognized : ', freqfile)
        quit()

    print(fn)

#    if ( os.path.isfile(fn) ) : return
    if ( os.path.isfile(fn) and ( overwrite == False) ) : return
#   ds = nc.Dataset(fn, 'w', format='NETCDF4')
    print('File exists : ', os.path.isfile(fn))
    print('Overwrite : ', overwrite)
    print('Type : ', type(overwrite))

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   create dimensions
    if ( freqfile != 'fixed' ) : time = ds.createDimension('time', None)
    lat = ds.createDimension('lat', nlat)
    lon = ds.createDimension('lon', nlon)
    bnds = ds.createDimension('bnds', nbnds)
    if   ( cdim == '3d' \
        or cdim == '3d-half'  )  : lev = ds.createDimension('lev' , nlev)
    elif ( cdim == '3d-plev19' ) : lev = ds.createDimension('plev', nlev)
    elif ( cdim == '3d-zlev20' ) : lev = ds.createDimension('altitude' , nlev)

#   create variables
    if ( freqfile != 'fixed' ) : times = ds.createVariable('time', 'f4', ('time',))
    lats = ds.createVariable('lat', 'f4', ('lat',))
    lons = ds.createVariable('lon', 'f4', ('lon',))
    latbnds = ds.createVariable('lat_bnds', 'f4', ('lat','bnds',))
    lonbnds = ds.createVariable('lon_bnds', 'f4', ('lon','bnds',))

    if ( cdim == '3d'  \
      or cdim == '3d-half' ) : 
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
    elif ( cdim == '3d-zlev20' ) :
        zlevs=ds.createVariable('altitude', 'f4', ('altitude',))

#   final field for the variable
#   including time
    if   (   cdim == '2d'        and freqfile != 'fixed'   ) : value = ds.createVariable(var, 'f4', ('time',              'lat', 'lon',), fill_value=1.e+20)
    elif ( ( cdim == '3d'        and freqfile != 'fixed' ) \
        or ( cdim == '3d-half'   and freqfile != 'fixed' ) ) : value = ds.createVariable(var, 'f4', ('time', 'lev' ,      'lat', 'lon',), fill_value=1.e+20)
    elif (   cdim == '3d-plev19' and freqfile != 'fixed'   ) : value = ds.createVariable(var, 'f4', ('time', 'plev',      'lat', 'lon',), fill_value=1.e+20)
    elif (   cdim == '3d-zlev20' and freqfile != 'fixed'   ) : value = ds.createVariable(var, 'f4', ('time', 'altitude' , 'lat', 'lon',), fill_value=1.e+20)
#   NOT including time
    elif (   cdim == '2d'        and freqfile == 'fixed'   ) : value = ds.createVariable(var, 'f4', (                     'lat', 'lon',), fill_value=1.e+20)
    else : 
        print('No dimension description recognized : ', cdim)
        quit()

#   attributes time
#   time_units="days since 0001-01-01 00:00:00"   # before 2026-02-06
#   calendar="noleap"                             #
    time_units="days since 2000-01-01 00:00:00"   # after 2026-02-06
    calendar="gregorian"                          #

    if ( freqfile != 'fixed' ) :
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
# attributes levels
    if ( cdim == '3d' \
      or cdim == '3d-half' ) :
#
#       attributes lev
        levs.bounds = "lev_bnds" 
        levs.units = "1" 
        levs.axis = "Z" 
        levs.positive = "down" 
        levs.long_name = "hybrid sigma pressure coordinate" 
        levs.standard_name = "atmosphere_hybrid_sigma_pressure_coordinate" 
        levs.formula = 'p = a*p0 + b*ps' 
        levs.formula_terms = 'p0: p0 a: a b: b ps: ps'
        levs.units='Pa' 
#
#       attributes levbnds
        levbnds.formula       = 'p = a*p0 + b*ps'
        levbnds.standard_name = 'atmosphere_hybrid_sigma_pressure_coordinate'
        levbnds.units         = '1'
        levbnds.formula_terms = 'p0: p0 a: a_bnds b: b_bnds ps: ps'
        levbnds.units         = 'Pa'
#
#       attributes p0
        p0.standard_name = "reference_air_pressure_for_atmosphere_vertical_coordinate" 
        p0.long_name     = "vertical coordinate formula term: reference pressure" 
        p0.units         = "Pa" 

#       hyam
        a.long_name = "vertical coordinate formula term: a" 
#       hybm
        b.long_name = "vertical coordinate formula term: b" 
#       ps
        ps.standard_name = "air_pressure" 
        ps.long_name     = "Surface Air Pressure" 
        ps.units         = "Pa" 
#       hyai
        abnds.long_name = "vertical coordinate formula term: a(k+1/2)" 
#       hybi
        bbnds.long_name = "vertical coordinate formula term: b(k+1/2)" 
#
    elif ( cdim == '3d-plev19' ) :
#       attributes plev
        plevs.axis = "Z" 
        plevs.positive = "down"
        plevs.long_name = "pressure"
        plevs.standard_name = "air_pressure" 
        plevs.units='Pa'
#
    elif ( cdim == '3d-zlev20' ) :
#       attributes zlev
        zlevs.axis = "Z" 
        zlevs.positive = "up"
        zlevs.long_name = "altitude"
        zlevs.standard_name = "altitude" 
        zlevs.units='km'

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
#   GENERATE THE DATES
    nyear=year1-year0+1
    if ( freqfile == 'monthly' \
      or freqfile == 'fixed' ) :
        nmonth=12
        ntime=nyear*nmonth
        datetimelist = []  # numerical value
        numtimelist  = []
        for iyear in range(nyear) :
            year=year0+iyear
            for imonth in range(nmonth) :
                month=imonth+1
                datetimelist.append(datetime.datetime(year, month, 15))
                numtimelist.append(nc.date2num(datetime.datetime(year, month, 15), time_units, calendar=calendar))
                    

    elif ( freqfile == '3hourly' ) :
        month0=1
        day0=1
        hour0=0
        dhour=3
        ntime=nyear*8*365 
        datet=datetime.datetime(year0,month0,day0,hour0)         

        datetimelist=[]
        numtimelist=[]

        for itime in range(ntime) :

            numt=nc.date2num(datet, time_units, calendar=calendar)

#           increase            
            numt=numt+dhour/24.            
            datet=nc.num2date(numt, time_units, calendar=calendar)

            datetimelist.append(datet)
            numtimelist.append(numt)
           
    else : 
        print('+++ cmorize_internal +++')
        print('No freqfile recognized : ', freqfile)
        quit()


#    timelist=np.zeros( (ntime ), dtype=float)
#    itime=0
#    for iyear in range(0,nyear) : 
#        year=year0+iyear
#        for imonth in range(0,nmonth) :
#            month=imonth+1

    for itime in range(ntime) :
#       obtain values + units
        year=datetimelist[itime].year        
        month=datetimelist[itime].month        
        day=datetimelist[itime].day       
        hour=datetimelist[itime].hour        

        D=obtainfield.obtainfield(year=year,month=month,day=day,hour=hour,expid=expid,var=var,desiredunits=desiredunits,cdim=cdim,freqfile=freqfile) # cdim : '2d', '3d', '3d-half', ...

#       correction : GRIDAREA = 0 in cam.h0 files
        if ( var == 'areacella' ) :
            D['field'][:,:] = areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='area')

        print('... now here ...')

        print('cdim : ', cdim)
#           
#       time-varying fields
        if   (   cdim == '2d'        and freqfile != 'fixed'   ) : value[itime,:,:]  =        D['field'][:,:]
        elif ( ( cdim == '3d'        and freqfile != 'fixed' ) \
            or ( cdim == '3d-half'   and freqfile != 'fixed' ) ) : value[itime,:,:,:]=np.flip(D['field'][:,:,:], axis=0) # flipping vertical axis
        elif (   cdim == '3d-plev19' and freqfile != 'fixed'   ) : value[itime,:,:,:]=        D['field'][:,:,:]
        elif (   cdim == '3d-zlev20' and freqfile != 'fixed'   ) : value[itime,:,:,:]=        D['field'][:,:,:]
#       constant fields   
        elif (   cdim == '2d'        and freqfile == 'fixed'   ) : value[      :,:]  =        D['field'][:,:] 
        else :
            print('+++ cmorize_internal +++')
            print('No cdim and freqfile recognized : ', cdim, freqfile)
            quit() 

#       surface pressure (only for 3D fields)
        if ( cdim == '3d' \
          or cdim == '3d-half' ) :
            S=obtainfield.obtainfield(year=year,month=month,day=day,hour=hour,expid=expid,var='ps',desiredunits='Pa',cdim='2d',freqfile=freqfile) # surface pressure
            ps[itime,:,:]=S['field'][:,:]

#       fille the time
#        date = datetime.datetime(year, month, 15) # had standard day 15
#        if ( freqfile != 'fixed') : timelist[itime] = nc.date2num(date, time_units, calendar=calendar)


    if ( freqfile != 'fixed' ) : times[0:ntime] = numtimelist[0:ntime]
#
    value.units=D['units']    

    print('... now even here ...')

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
    if ( cdim == '3d' \
      or cdim == '3d-half' ) :
         
        if ( cdim == '3d' ) : Lhyai = hyai; Lhybi=hybi ; Lhyam = hyam ; Lhybm = hybm
        elif ( cdim == '3d-half' ) : 
                              Lhyai = np.concatenate(([hyai[0]], (hyai[0:nlev-1]+hyai[1:nlev])*0.5, [hyai[nlev-1]]), axis=0)
                              Lhybi = np.concatenate(([hybi[0]], (hybi[0:nlev-1]+hybi[1:nlev])*0.5, [hybi[nlev-1]]), axis=0)

                              Lhyam = hyai
                              Lhybm = hybi
                               
#       levels
        levs[:]      = np.flip( p0_input * Lhyam[:]        + 101325. * Lhybm[:]        ) / 101325.    # FLIPPED !
#       levbnds 
        levbnds[:,1] = np.flip( p0_input * Lhyai[0:nlev]   + 101325. * Lhybi[0:nlev]   ) / 101325.    # FLIPPED !
        levbnds[:,0] = np.flip( p0_input * Lhyai[1:nlev+1] + 101325. * Lhybi[1:nlev+1] ) / 101325.    # FLIPPED !
#       p0
        p0[:]        = p0_input
#       hyam  
        a[:]         = np.flip( Lhyam[:] )
#       hyai
        abnds[:,1]   = np.flip( Lhyai[0:nlev]   )
        abnds[:,0]   = np.flip( Lhyai[1:nlev+1] )
#       hybm
        b[:]         = np.flip( Lhybm[:] )
#       hybi
        bbnds[:,1]   = np.flip( Lhybi[0:nlev]   )
        bbnds[:,0]   = np.flip( Lhybi[1:nlev+1] )
    elif ( cdim == '3d-plev19' ) :
        plevs[0:nlev] = plevlist[0:nlev]
    elif ( cdim == '3d-zlev20' ) :
        zlevs[0:nlev] = zlevlist[0:nlev]

 #
    ds.close()
