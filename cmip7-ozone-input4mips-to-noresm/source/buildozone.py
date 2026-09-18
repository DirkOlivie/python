import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc

import getreadyearlistozone

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-ozone-input4mips/source')
import readfieldozone

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-input4mips-to-noresm/source')
import yearlist2blocklist

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import daysince 


#
def buildozone(species, period, version, scenario, i4mpdownload, fromclim, dolon, overwrite, calendar, time_units):
#-------------
    '''
    REMARK
        levels are flipped when writing !!! [otherwise simulation went wrong]

    AIM 

    INPUT
        species : 'vmro3'
        period
        version
        scenario
        i4mpdownload
        fromclim  : ''   | '-clim'
        dolon     : True | False
        overwrite : True | False

    CALLED BY
	    buildozoneloop2

    CALLS
	    readnc
	    getfinallevels
 	    daysince
   ''' 
#
    if   ( time_units == 'days since 0000-01-01' ) : refdate=     101
    elif ( time_units == 'days since 1750-01-01' ) : refdate=17500101
    elif ( time_units == 'days since 1850-01-01' ) : refdate=18500101
    else :
        print('+++ buildozone +++')
        print('No time_units recognized : ', time_units)
        quit()

#   I. PERIOD
#------------
#   period -> yearlist
    line=period.split('-')

#   standard method
    if ( len(line) == 2) : #  
#       1850-2015 
        year0 = int(line[0])
        year1 = int(line[1])
        yearlist=np.arange(year0,year1+1) # list  of consecutive years
#   exceptions
    elif ( len(line) == 3 ) :
        if   ( period == '2015-2100-decadal'        ) : yearlist=[     2015,2020,2030,2040,2050,2060,2070,2080,2090,2100          ]
        elif ( period == '2014-2301-decadal'        ) : yearlist=[2014,2015,2020,2030,2040,2050,2060,2070,2080,2090,2100,     2301]
        elif ( period == '2014-2301-decadalwith2250') : yearlist=[2014,2015,2020,2030,2040,2050,2060,2070,2080,2090,2100,2250,2301]
        elif ( period == '2014-2051-covid'          ) : yearlist=[2014,2015,2019,2020,2021,2023,2030,2040,2050,2051]
        elif ( period == '2014-2051-halfdecadal'    ) : yearlist=[2014,2015,2020,2025,2030,2035,2040,2045,2050,2051]
        else :
            print('+++ buildozone +++')
            print('No period recognized = ', period)
            quit()                        
#
    readscenario=scenario
#
#
#   II. DIMENSIONS
#-----------------
    if   ( scenario == 'CMIP'        ) : yeartest=yearlist[-1] # last year is test year
    elif ( scenario == 'ScenarioMIP' ) : yeartest=yearlist[0]  # fist year is test year

    test      = readfieldozone.readfieldozone(species=species, year0=yeartest, year1=yeartest, scenario=scenario, i4mpdownload=i4mpdownload, fromclim=fromclim)
    latitude  = test['latitude']
    longitude = test['longitude']
    level     = test['level']
    levbnds   = test['levbnds']
    lev_units = test['lev_units']
    units     = test['units']

#   units
    if ( units == 'mole mole-1'  \
      or units == 'moles mole-1' ) : 
        units='mol/mol'
    else : 
        print('+++ buildozone +++')
        print('No units recognized : ', units)
        quit()

#   level units
    if ( lev_units == 'hPa' ) : 
#        level = level * 100.
#        levbnds = levbnds * 100.
#        lev_units = 'Pa'
#        p0=100000.
        print('ok')
    else :
        print('+++ buildozone +++')
        print('No lev_units recognized : ', lev_units)
        quit()


#   dimensions
    nlat=len(latitude)
    nlon=len(longitude)
    nlev=len(level)

    if ( nlat == 96 and nlon == 144 ) : resolution='1.9x2.5'
    else :
        print('+++ buildozone +++')
        print('No resolution recognized with nlat and nlon : ', nlat, nlon)
        quit()

#   III. TIME
#------------
    nmonth=12

    nyear = len(yearlist)
    year0 = yearlist[0]       # first element
    year1 = yearlist[-1]      # last element 
  
    date    = np.zeros(nyear*nmonth,dtype=int)  # integer  
    datesec = np.zeros(nyear*nmonth,dtype=int)  # integer

    for iyear in range(0,nyear) :
        year=yearlist[iyear]
        date[   iyear*nmonth:(iyear+1)*nmonth] = [116, 215, 316, 416, 516, 616, 716, 816, 916, 1016, 1116, 1216] + 10000 * year
        datesec[iyear*nmonth:(iyear+1)*nmonth] = [43200,0,43200,0,43200,0,43200,43200,0,43200,0,43200]
#
#   IV. NEW FILE
#----------------
    cyear0=str("%4.4i"% year0)
    cyear1=str("%2.2i"% year1)

#   cperiod
    if ( year0 == year1 ) :
        cperiod=cyear0              # one single year
    else :
        cperiod=cyear0+'-'+cyear1   # multiple years

#   FILENAME
    filename='ozone_'+species+'_'+scenario+'_'+i4mpdownload+'_'+cperiod+fromclim+'_'+resolution+'_'+version+'.nc'

##############
#   New file #
##############

#   create new directory
    outdir='/scratch/olivie/code/python/cmip7-ozone-input4mips-to-noresm/data/output/'+version
    if  not os.path.isdir(outdir) : os.makedirs(outdir)

#   create new NetCDF file
    fn = outdir+'/'+filename    
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
    if ( dolon ) : londimid = ds.createDimension('lon', nlon)
    latdimid = ds.createDimension('lat', nlat)

#   vertical
    levdimid  = ds.createDimension('lev' , nlev  )
    ilevdimid = ds.createDimension('ilev', nlev+1)

#   time
    timedimid = ds.createDimension('time', None)

######################
#   Define variables #
######################
# 
#   horizontal
    latid  = ds.createVariable('lat' , 'f4', ('lat',))
    if ( dolon ) : lonid  = ds.createVariable('lon' , 'f4', ('lon',))

#   vertical
    levid  = ds.createVariable('lev' , 'f4', ('lev' ,))
    ilevid = ds.createVariable('ilev', 'f4', ('ilev',))

    # p0id=ds.createVariable('P0', 'f4')
    # hyamid=ds.createVariable('hyam','f4', ('lev',))
    # hybmid=ds.createVariable('hybm','f4', ('lev',))
    # hyaiid=ds.createVariable('hyai','f4', ('ilev',))
    # hybiid=ds.createVariable('hybi','f4', ('ilev',))

    #if ( dolon ) : psid=ds.createVariable('PS','f4', ('time', 'lat', 'lon',), fill_value=1.e+20)
    #else         : psid=ds.createVariable('PS','f4', ('time', 'lat',       ), fill_value=1.e+20)

#   time
    timeid = ds.createVariable('time', 'f4', ('time',))
#
#   species
    if ( dolon ) : speciesid = ds.createVariable('O3','f4', ('time','lev','lat','lon',))
    else         : speciesid = ds.createVariable('O3','f4', ('time','lev','lat',      ))
# 
#   date
    dateid    = ds.createVariable('date'   , 'i4', ('time',))
    datesecid = ds.createVariable('datesec', 'i4', ('time',))
#
################
#   ATTRIBUTES #
################
#   latitude
    latid.bounds        = "lat_bnds"
    latid.units         = "degrees_north"
    latid.axis          = "Y"
    latid.long_name     = "Latitude"
    latid.standard_name = "latitude"

#   longitude
    if ( dolon ) : 
        lonid.bounds        = "lon_bnds"
        lonid.units         = "degrees_east"
        lonid.axis          = "X"
        lonid.long_name     = "Longitude"
        lonid.standard_name = "longitude"

#   altitude
#    levid.axis = "Z"
    levid.positive      = "down"
#   levid.positive      = "up"
    levid.long_name     = "hybrid level at midpoints (1000*(A+B))"
    levid.standard_name = "atmosphere_hybrid_sigma_pressure_coordinate"
    levid.formula_terms = "a: hyam b: hybm p0: P0 ps: PS"
    levid.units         = lev_units

#    ilevid.axis = "Z"
    ilevid.positive      = "down"
#   ilevid.positive      = "up"
    ilevid.long_name     = "hybrid level at interfaces (1000*(A+B))"
    ilevid.standard_name = "atmosphere_hybrid_sigma_pressure_coordinate"
    ilevid.formula_terms = "a: hyai b: hybi p0: P0 ps: PS" ;
    ilevid.units         = lev_units
    

#    p0id.long_name = "reference pressure"
#    p0id.units = "Pa"

#    hyamid.long_name = "hybrid A coefficient at layer midpoints" 
#    hybmid.long_name = "hybrid B coefficient at layer midpoints" 

#    hyaiid.long_name = "hybrid A coefficient at layer interfaces"
#    hybiid.long_name = "hybrid B coefficient at layer interfaces"
    
#    psid.units = "Pa" ;
#    psid.long_name = "Surface pressure" ;    
#
#   time 
    timeid.bounds        = "time_bnds"
    timeid.units         = time_units
    timeid.calendar      = calendar
    timeid.axis          = "T"
    timeid.long_name     = "time"
    timeid.standard_name = "time"

#   species
    speciesid.units     = units
    speciesid.long_name = 'O3 concentration'

#   date
    dateid.long_name = 'current date as 8 digit integer (YYYYMMDD)'
    dateid.calendar  = calendar

#   datesec
    datesecid.long_name = 'seconds of current date'
    datesecid.units     = 's'
#
#   global data   
    ds.domxmin = longitude[0] 
    ds.domxmax = longitude[-1]
    ds.x_units = 'deg'
    ds.x_display_units = 'Longitude deg'
    ds.domymin = -90.
    ds.domymax =  90.
    ds.y_units = 'deg'
    ds.y_display_units = 'Latitude deg'
#    ds.domtmin, 1., /FLOAT
#    ds.domtmax, 12., /FLOAT
    ds.t_units = 'month'
    ds.t_display_units = 'Time month'

##################
#   WRITE FIELDS #
##################
#
    latid[0:nlat] = latitude[ 0:nlat]
    if ( dolon ) : lonid[0:nlon] = longitude[0:nlon]

#    levid[ 0:nlev  ] = level[  0:nlev  ]
#    ilevid[0:nlev+1] = levbnds[0:nlev+1]
    levid[ 0:nlev  ] = np.flip(level[  0:nlev  ])
    ilevid[0:nlev+1] = np.flip(levbnds[0:nlev+1])

#    hyamid[0:nlev] = np.zeros((nlev), dtype=float)
#    hybmid[0:nlev] = np.flip(level[  0:nlev  ] / p0)

#    hyaiid[0:nlev+1] = np.zeros((nlev+1), dtype=float)
#    hybiid[0:nlev+1] = np.flip(levbnds[  0:nlev+1  ] / p0)

#    p0id[:] = p0
#
#   Add the emission
#   convert yearlist -> readyearlist
    readyearlist=getreadyearlistozone.getreadyearlistozone(yearlist=yearlist, scenario=scenario, activity='ozone', i4mpdownload=i4mpdownload) # this should not depend on sector, as sectors end up in same file with same time axis

#   convert readyeasrlist -> yearblocklist
    yearblocklist=yearlist2blocklist.yearlist2blocklist(yearlist=readyearlist, activity='ozone', resolution=resolution)

#   
    print('yearlist      : ', yearlist)
    print('readyearlist  : ', readyearlist)
    print('yearblocklist : ', yearblocklist)  
    
    itime0=0 # important

    nblock=len(yearblocklist)    
    for iblock in range(nblock) :
        readyear0=yearblocklist[iblock][0]       # first element in specific block
        readyear1=yearblocklist[iblock][-1]      # last element in specific block

        nyear=readyear1-readyear0+1

        itime1=itime0 + nyear*nmonth

        F = readfieldozone.readfieldozone(species=species, year0=readyear0, year1=readyear1, scenario=readscenario, i4mpdownload=i4mpdownload, fromclim=fromclim)

#       speciesid[itime0:itime1,0:nlev,0:nlat,0:nlon]=F['field'][0:nyear*nmonth,0:nlev,0:nlat,0:nlon]
        if ( dolon ) : speciesid[itime0:itime1,0:nlev,0:nlat,0:nlon] =         np.flip(F['field'][0:nyear*nmonth,0:nlev,0:nlat,0:nlon], axis=1)
        else         : speciesid[itime0:itime1,0:nlev,0:nlat       ] = np.mean(np.flip(F['field'][0:nyear*nmonth,0:nlev,0:nlat,0:nlon], axis=1),axis=3)

        print(len(dateid[   itime0:itime1]), len(date[   itime0:itime1]))

        dateid[   itime0:itime1] = date[   itime0:itime1]
        datesecid[itime0:itime1] = datesec[itime0:itime1]
        
        for itime in range(itime0,itime1) :
            timeid[itime] = daysince.daysince(refdate=refdate,enddate=date[itime], calendar=calendar) + float(datesec[itime]) / 86400. 

        itime0=itime0+ nyear*nmonth

#    if ( dolon ) : psid[:,:,:] = 100000.
#    else         : psid[:,:  ] = 100000.

    ds.close()

