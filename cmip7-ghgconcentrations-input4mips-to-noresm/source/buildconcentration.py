import numpy as np
import os
from netCDF4 import Dataset
import netCDF4 as nc

import getspeciesinfo
import composeseries

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import daysince

#
def buildconcentration(scenario, yearrange, specieslist, timeresolution, time_units, calendar, region, version, i4mpdownload, nlat, overwrite):
#-----------------------
    '''
    REMARKS
	    if nlat = 360 : gets the longitudes from some standard WACCM lbc file (LBC_1750-2015_CMIP6_GlobAnnAvg_c180926.nc)

    MODIFICATIONS
	    (2025-09-12) added possibility for cmip7 in the filename
        (2026-08-29) added possibility for non-cmip7 species : CH2BR2, H2, OCS

    AIM 
	    create ANNUAL files (containing full annual cycle)
	    rename variables to
	    renames experiments
	    eventually add up variables

    INPUT
	    scenario       :'CMIP' | 'ScenarioMIP' 
	    yearrange      : 2-element array  [year0,year1]
	    specieslist    : list of GHGs, e.g. : 'CO2_LBC','CH4_LBC','N2O_LBC','CFC11eq_LBC','CF2CL2_LBC'
	    timeresolution : time resolution : 'annual' or 'monthly'
        time_units     : 'days since 1850-01-01' or 'days since 0001-01-01'
        calendar       : 'noleap'
        region         :'GLOBAL' or 'ZONAL' [original data]
 	    version        : string describing the version
	    i4mpdownload   : downloaded version of input4MIPs data
	    nlat           : 1, 360, ... [determines number of latitudes in the end]
        overwrite      : True or False

    CALLED BY
	    buildconcentrationloop

    CALLS
	    readnc
        getspeciesinfo : information on input speciesname and output speciesname/units
	    composeseries : currently always with argument region='GLOBAL'
        daysince [CURRENTLY NOT EXISTING]
    '''
#------------------------------------------------ 
#
    print, 'Doing ... ', scenario
    print, 'specieslist = ', specieslist
#
#   nspecies
    nspecies=len(specieslist)
#
#   I. TIME
#----------
#   time timeresolution
    if   ( timeresolution == 'monthly' ) : nmonth=12
    elif ( timeresolution == 'annual'  ) : nmonth=1
    else :
        print('No timeresolution recognized : ', timeresolution)
        quit()

#   begin/start year wanted
    year0=yearrange[0]
    year1=yearrange[1]
#
#   new file
    cyear0=str("%4.4i"% year0)
    cyear1=str("%4.4i"% year1)
#
    if ( year0 == year1 ) : cperiod=cyear0
    else                  : cperiod=cyear0+'-'+cyear1 

#   II. LATITUDE RESOLUTION
#--------------------------
#   latitude timeresolution  
    if ( nlat == 360 ) :
        cgrid='0p5degLat'
        latitude=readnc.readnc('lat','/datalake/NS2345K/olivie/ghgconcentrations-auxiliary/inputdata/atm/waccm/lb/LBC_1750-2015_CMIP6_GlobAnnAvg_c180926.nc')
        if ( len(latitude) != nlat ) :
            print('Number of latitudes do not agree')
            quit
    elif ( nlat == 1 ) :
        cgrid='global'
        latitude=np.array([0],dtype=float) # latitude array with 1 element : latitude value at equator
    else :
        print('No #latitudes recognized : ', nlat)
        quit()
#
#   III. OUTPUT FILE
#-------------------
#   outdir
    outdir='/scratch/olivie/code/python/cmip7-ghgconcentratations-input4mips-to-noresm/data/output/'+version
    if  not os.path.isdir(outdir) : os.makedirs(outdir)

#   output filename
    if   ( region == 'GLOBAL' ) : suffix = 'gm'
    elif ( region == 'ZONAL' ) : suffix = 'gnz'
    else :
        print('+++ buildconcentration +++')
        print('No region recognized : ', region)
        quit()

    filename='ghg_cmip7_'+scenario+'_'+i4mpdownload+'_'+cperiod+'_'+timeresolution+'_'+suffix+'_'+cgrid+'_'+version+'.nc'
#
#   IV. create new NetCDF file
#-----------------------------
    fn = outdir+'/'+filename
#
#   no overwriting
    if ( os.path.isfile(fn) and ( overwrite == False) ) : return

    print('File exists : ', os.path.isfile(fn))
    print('Overwrite : ', overwrite)
    print('Type : ', type(overwrite))

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   DIMENSIONS
    if ( nlat > 1 ) : latdimid = ds.createDimension('lat', nlat)  # latitude dimension (if needed)
    timedimid = ds.createDimension('time', None)                  # time dimension (if needed)

#   VARIABLES
#   Define variables corresponding with dimensions
    if (nlat > 1 ) : latid= ds.createVariable('lat', 'f4', ('lat',)) # latitude variable
    timeid = ds.createVariable('time', 'f4', ('time',))              # time variable

#   Name of species
    speciesidlist=[]
    for species in specieslist :

        Sinfo=getspeciesinfo.getspeciesinfo(species=species, i4mpdownload=i4mpdownload)    

        if (   nlat == 1 ) : speciesidlist.append(ds.createVariable(species,'f4', ('time'      ,)))
        elif ( nlat >  1 ) : speciesidlist.append(ds.createVariable(species,'f4', ('time','lat',)))
        else :
            print('No nlat recognized : ', nlat)
            quit()

# 
    dateid    = ds.createVariable('date'   , 'i4', ('time',))  # integer


#   ATTRIBUTES
#   latitude
    if ( nlat > 1 ) :
        latid.bounds        = "lat_bnds"
        latid.units         = "degrees_north"
        latid.axis          = "Y"
        latid.long_name     = "Latitude"
        latid.standard_name = "latitude"

#   time 
    timeid.bounds        = "time_bnds"
    timeid.units         = time_units   # 2026-07-27
    timeid.calendar      = calendar     # 2026-07-27     
    timeid.axis          = "T"
    timeid.long_name     = "time"
    timeid.standard_name = "time"

#   species
    for species in specieslist :

        Sinfo=getspeciesinfo.getspeciesinfo(species=species, i4mpdownload=i4mpdownload)

        ispecies = specieslist.index(species)

        speciesidlist[ispecies].units = Sinfo['finalunits']
        speciesidlist[ispecies].long_name = Sinfo['finallongname']

#   date
    dateid.long_name = 'current date as 8 digit integer (YYYYMMDD)'

#   global data   
    ds.x_units = 'deg'
    ds.x_display_units = 'Longitude deg'
#    ds.domymin, -90., /FLOAT
#    ds.domymax, 90., /FLOAT
    ds.y_units = 'deg'
    ds.y_display_units = 'Latitude deg'
#    ds.domtmin, 1., /FLOAT
#    ds.domtmax, 12., /FLOAT
    ds.t_units = 'month'
    ds.t_display_units = 'Time month'


#   V. WRITE FIELDS
#------------------
#   
#   LATITUDES
    if ( nlat > 1 ) : latid[0:nlat] = latitude[0:nlat]

#   LOOP OVER ALL GHGs
    for ispecies in range(0,nspecies) :

        species=specieslist[ispecies]
        Sinfo=getspeciesinfo.getspeciesinfo(species=species, i4mpdownload=i4mpdownload) # info on original species name and final species name/units

        print, Sinfo['origspecies']
#
#       obtain data : origspecies
        F = composeseries.composeseries(scenario=scenario, yearrange=yearrange, species=Sinfo['origspecies'], source=Sinfo['source'], fixedvalue=Sinfo['fixedvalue'], timeresolution=timeresolution, region=region, latitude=latitude, i4mpdownload=i4mpdownload)
#
#       check whether units are as desired    
        if ( F['units'] == Sinfo['finalunits'] ) :
            factor=1.
        elif ( Sinfo['finalunits'] == 'mol mol-1' ) :
        
            if   ( F['units'] == '1e-6 mol mol-1' ) : factor = 1e-6
            elif ( F['units'] == '1e-9 mol mol-1' ) : factor = 1e-9
            elif ( F['units'] == '1e-12 mol mol-1' ) : factor = 1e-12
            else :
                print('+++ buildconcentration +++')
                print('No units recognized : ', F['units'])
                quit()
        else :
            print('+++ buildconcentration +++')
            print('No units recognized')
            print('data units : ', F['units'])
            print('desired units : ', Sinfo['finalunits'])
            quit()

#       change units / values
        F['valuelist'][:,:] = F['valuelist'][:,:] * factor
        F['units']          = Sinfo['finalunits']
    
#       write ghg-concentration [whole series at once]
        print('speciesidlist[ispecies][:,:] : ', speciesidlist[ispecies].shape)
        print('F[valuelist][:,:] : ', F['valuelist'].shape)

        if (   nlat > 1 ) : speciesidlist[ispecies][:,:] = F['valuelist'][:,:]
        elif ( nlat == 1 ) : speciesidlist[ispecies][:] = F['valuelist'][:,:]
        else : 
            print('+++ buildconcentration +++')
            print('No nlat recognized : ', nlat)
            quit()

#   DATE (YYYYMMDD) [whole series at once]
    dateid[:]=F['timelist'][:]

#   TIME (time daysince)
    ntime=len(F['timelist'])
    if   ( time_units == 'days since 0000-01-01' ) : refdate=     101
    elif ( time_units == 'days since 1750-01-01' ) : refdate=17500101
    elif ( time_units == 'days since 1850-01-01' ) : refdate=18500101
    else : 
        print('+++ buildconcentration +++')
        print('No time_units recognized : ', time_units)
        quit()

    for itime in range(ntime) :
        timeid[itime] = daysince.daysince(refdate=refdate,enddate=F['timelist'][itime], calendar=calendar)
