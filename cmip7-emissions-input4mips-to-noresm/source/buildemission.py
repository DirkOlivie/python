import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc

import getgridtype
import getspeciesinfo
import getfullsectorlist
import getfinallevels
import getreadyearlist
import yearlist2blocklist
import composefield

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction
sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-volc/source')
import readareatopography

#
def buildemission(period, species, activity, sectorliststring, vertdist, resolution, vertintp, version, noresmversion, scenario, i4mpdownload, project, filelocation, overwrite):
#----------------
    '''
    MODIFICATIONS
        (2026-01-16) : add area in output file
        (2026-07-22) : added period possibility 2022-2101-cmip7scenario

    AIM 
	    create ANNUAL files (containing full annual cycle)

    INPUT
        period
        species
        activity
        sectorliststring
        vertdist
        resolution : 0.9x1.25, 1.9x2.5, ne16pg3, ne30pg3
        vertintp
        version
        noresmversion : 'noresm_c1.2' | 'noresm2'
        scenario
        i4mpdownload
        project : 'cmip7'
        filelocation
        overwrite 

    CALLED BY
	    buildemissionloop2

    CALLS
	    getspeciesinfo
        getgridtype
	    readnc
	    getfinallevels
	    composefield
 	    daysince
   ''' 
#
    print('+++ Starting : buildemission +++')
#
#   sectorliststring -> sectorlist
    sectorlist=sectorliststring.split('-')

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
        elif ( period == '2022-2101-cmip7scenario'  ) : yearlist=[2022,2023,2024,2025,2030,2035,2040,2045,2050,2055,2060,2065,2070,2075,2080,2085,2090,2095,2100,2101] 
        else :
            print('No period recognized = ', period)
            quit()                        

    print('Doing ... ', species)
    print('verdist = ', vertdist)
    print('sectorlist = ', sectorlist)
#
#   Navogadro
    Nav=6.022e23

#   nsector
    nsector=len(sectorlist)

#   original species
    speciesinfo = getspeciesinfo.getspeciesinfo(species=species,activity=activity)             

#   final dimesions / final units
    if ( vertdist == 'surface-to-surface' ) :
        dim='2-dim'
        finalunits='molecules cm-2 s-1'
    elif ( vertdist == 'surface-to-profile' ) :
        dim='3-dim'
        finalunits='molecules cm-3 s-1'
    elif ( vertdist == 'profile-to-profile' ) :
        dim='3-dim'
        finalunits='molecules cm-3 s-1'
    else :
        print('No dim recognized = ', dim)
        quit()

# final horizontal resolution
    gridtype=getgridtype.getgridtype(resolution=resolution)

#    if (  resolution == '0.9x1.25' ) :
#        nc_f='/nird/datalake/NS2345K/olivie/emissions-auxiliary/cases/SOA_r610_PD/atm/hist/SOA_r610_PD.cam.h0.1979-01.nc'    
#    elif ( resolution == '1.9x2.5' ) :
#        nc_f='/nird/datalake/NS2345K/olivie/emissions-auxiliary/cases/Test149f19_f19/atm/hist/Test149f19_f19.cam.h0.0001-01.nc'
#    elif ( resolution == 'ne30pg3' ) :
#        nc_f='/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_20240720.nc'        
#    elif ( resolution == 'ne16pg3' ) :
#        nc_f='/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo/se/ne16pg3_gmted2010_modis_bedmachine_nc3000_Laplace0200_20230202.nc'
#    else :
#        print('+++ buildemission +++')
#        print('No resolution recognized = ', resolution)
#        quit()
    nc_f=filelocation.topofile(grid=resolution) # filename depends on resolution 
    print('FILELOCATION : ', filelocation.topo_fv09)
    print('FILELOCATION : ', filelocation.topo_fv19)
    print('FILELOCATION : ', filelocation.topo_ne16pg3)
    print('FILELOCATION : ', filelocation.topo_ne30pg3)
#
    print('FILENAME : ', nc_f)

    nc_fid= Dataset(nc_f, 'r')
#
    latitude=np.array(nc_fid.variables['lat'][:])  # latitudes
    longitude=np.array(nc_fid.variables['lon'][:])  # longitudes


    nc_fid.close
#
#   area
    if (   gridtype == 'latlon'    ) : area=areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='area')
    elif ( gridtype == 'irregular' ) : area=readareatopography.readareatopography(grid=resolution, variable='area', filelocation=filelocation)
    else :
        print('+++ buildemission +++')
        print('No gridtype recognized')
        quit()
#  
    if ( gridtype == 'latlon' ) :     
        nlon=len(longitude)
        nlat=len(latitude)
    elif ( gridtype == 'irregular' ) :
        ncol=len(longitude)
    else :
        print('+++ buildemission +++')
        print('No gridtype recognized : ', gridtype)
        quit()

#
# readscenario
    if (   scenario == 'ScenarioMIP_IAMC-IMAGE-ssp119-1-1-lineardecrease2250'             ) : readscenario = 'ScenarioMIP_IAMC-IMAGE-ssp119-1-1'
    elif ( scenario == 'ScenarioMIP_IAMC-IMAGE-ssp126-1-1-lineardecrease2250'             ) : readscenario = 'ScenarioMIP_IAMC-IMAGE-ssp126-1-1'
    elif ( scenario == 'ScenarioMIP_IAMC-MESSAGE-GLOBIOM-ssp245-1-1-lineardecrease2250'   ) : readscenario = 'ScenarioMIP_IAMC-MESSAGE-GLOBIOM-ssp245-1-1'
    elif ( scenario == 'ScenarioMIP_IAMC-REMIND-MAGPIE-ssp534-over-1-1-lineardecrease2250') : readscenario = 'ScenarioMIP_IAMC-REMIND-MAGPIE-ssp534-over-1-1'
    else                                                                                    : readscenario = scenario

#   final vertical resolution : find nlev, altitude and altitude_int
    if ( dim == '2-dim' ) :
        altitude_int=None

    elif ( dim == '3-dim' ) :
#
        ifound=0
# 
        for sector in sectorlist :

            if ( sector == 'ALL' ) : complist=getfullsectorlist.getfullsectorlist(activity=activity,scenario=readscenario,i4mpdownload=i4mpdownload)
            else                   : complist=[sector]

            for comp in complist :

                if ( ifound == 0 ) :
                    P = getfinallevels.getfinallevels(activity=activity, sector=comp, vertintp=vertintp)

                    nlev=P['nlev']
                    altitude=P['altitude']
                    altitude_int=P['altitude_int']
                    altitude_units=P['altitude_units']

                    ifound=1

#          check whether all other sectors in the list give the same level distribution
                elif ( ifound == 1 ) : 

                    Q = getfinallevels.getfinallevels(activity=activity, sector=comp, vertintp=vertintp)

                    if ( Q['nlev'] != nlev \
                        or np.sum(np.abs(Q['altitude'] - altitude)) != 0. \
                        or np.sum(np.abs(Q['altitude_int'] - altitude_int)) != 0. ) :
                        print('Different sectors have different vertical resolutions')
                        quit()
#
#
#   III. time
#
    nmonth=12

    nyear=len(yearlist)
    year0=yearlist[0]       # first element
    year1=yearlist[-1]      # last element 
  
    date=np.zeros(nyear*nmonth,dtype=int)     # integer  
    datesec=np.zeros(nyear*nmonth,dtype=int)  # integer

    for iyear in range(0,nyear) :
        year=yearlist[iyear]
        date[iyear*nmonth:(iyear+1)*nmonth] = np.array([116, 216, 316, 416, 516, 616, 716, 816, 916, 1016, 1116, 1216], dtype=int) + 10000 * year
  
    datesec[:]=0
#
#   IV. new file
#
    cyear0=str("%4.4i"% year0)
    cyear1=str("%2.2i"% year1)

#   sectorgroupname : concatenate all individual sector names
    sectorgroupname=''
    for sector in sectorlist : 
        sectorgroupname=sectorgroupname+sector

#   cperiod
    if ( year0 == year1 ) :
        cperiod=cyear0              # one single year
    else :
        cperiod=cyear0+'-'+cyear1   # multiple years

#   cperiod
    if (   dim == '2-dim' ) : cdim='surface'
    elif ( dim == '3-dim' ) : 
        if (   vertintp == 'native' ) : cdim = 'vertical'
        elif ( vertintp == 'L21'    ) : cdim =  vertintp
        else : 
            print('No vertintp recognize : ', vertintp)
            quit()
    else :
        print(' No dim recognized : ', dim)
        quit() 

    suffix=''            
#    suffix = getvalue_commonblock(descriptor='suffix')
#    if ( suffix ne '' ) then suffix='_'+suffix  ; add '_' in front 

#   FILENAME
    filename='emissions_'+project+'_'+noresmversion+'_'+species+'_'+activity+sectorgroupname+'_'+cdim+'_'+cperiod+'_'+resolution+'_'+i4mpdownload+'_'+version+suffix+'.nc'

##############
#   New file #
##############

#   create new directory
    outdir='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/'+version+'/individual/'+scenario+'/'+resolution
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
    if ( gridtype == 'latlon' ) :
        londimid = ds.createDimension('lon', nlon)
        latdimid = ds.createDimension('lat', nlat)
    elif (gridtype == 'irregular' ) :
        coldimid = ds.createDimension('ncol', ncol)
    else :
        print('No gridtype recognized : ', gridtype)
        quit()

#   vertical
    if ( dim == '3-dim' ) : levdimid  = ds.createDimension('altitude'    , nlev  )
    if ( dim == '3-dim' ) : ilevdimid = ds.createDimension('altitude_int', nlev+1)
#   time
    timedimid = ds.createDimension('time', None)

######################
#   Define variables #
######################
# 
#   horizontal
    if ( gridtype == 'latlon' ) : 
        latid  = ds.createVariable('lat' , 'f4', ('lat',))
        lonid  = ds.createVariable('lon' , 'f4', ('lon',))
        areaid = ds.createVariable('area', 'f4', ('lat','lon'))
    elif ( gridtype == 'irregular' ) :
        latid  = ds.createVariable('lat' , 'f4', ('ncol',))
        lonid  = ds.createVariable('lon' , 'f4', ('ncol',))
        areaid = ds.createVariable('area', 'f4', ('ncol',))
    else :
        print('No gridtype recognized : ', gridtype)
        quit()

#   vertical
    if ( dim == '3-dim' ) :  levid = ds.createVariable('altitude', 'f4', ('altitude',))
    if ( dim == '3-dim' ) : ilevid = ds.createVariable('altitude_int', 'f4', ('altitude_int',))
#   time
    timeid = ds.createVariable('time', 'f4', ('time',))
#
#   name of emissions will be name of sector
    sectoridlist=[]
    for sector in sectorlist :
        
        if (   dim == '2-dim' and gridtype == 'latlon'    ) : sectoridlist.append(ds.createVariable('emiss_'+activity+'_'+sector,'f4', ('time'           ,'lat','lon',)))
        elif ( dim == '3-dim' and gridtype == 'latlon'    ) : sectoridlist.append(ds.createVariable('emiss_'+activity+'_'+sector,'f4', ('time','altitude','lat','lon',)))
        elif ( dim == '2-dim' and gridtype == 'irregular' ) : sectoridlist.append(ds.createVariable('emiss_'+activity+'_'+sector,'f4', ('time'           ,'ncol',)))
        elif ( dim == '3-dim' and gridtype == 'irregular' ) : sectoridlist.append(ds.createVariable('emiss_'+activity+'_'+sector,'f4', ('time','altitude','ncol',)))
        else :
            print('No dim recognized : ', dim)
            quit()
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
    lonid.bounds        = "lon_bnds"
    lonid.units         = "degrees_east"
    lonid.axis          = "X"
    lonid.long_name     = "Longitude"
    lonid.standard_name = "longitude"

#   area
    areaid.units         = "m2"    # normalized would be another option
    areaid.long_name     = "Area"
    areaid.standard_name = "gridpoint area"

#   altitude
    if ( dim == '3-dim' ) :
        levid.axis = "Z"
        levid.positive = "up"
        levid.long_name = "altitude at middle of layers"
        levid.standard_name = "Altitude"
        levid.units='km'

        ilevid.axis = "Z"
        ilevid.positive = "up"
        ilevid.long_name = "altitude at layer interfaces"
        ilevid.standard_name = "Altitude"
        ilevid.units='km'

#   time 
    timeid.bounds        = "time_bnds"
    timeid.units         = "days since ..."
#    timeid.calendar      = calendar
    timeid.axis          = "T"
    timeid.long_name     = "time"
    timeid.standard_name = "time"

#   species
    for sector in sectorlist :

        if ( sector == 'ALL' ) :
            complist=getfullsectorlist.getfullsectorlist(activity=activity,scenario=readscenario,i4mpdownload=i4mpdownload)

#           to make one long name        
            csector=''
            for comp in complist : 
                csector=csector+comp  
        
        else :
            csector=sector 

        isector = sectorlist.index(sector)

        sectoridlist[isector].units = finalunits
        sectoridlist[isector].long_name = 'Emissions of '+species+' from '+csector+' in '+ activity


#   date
    dateid.long_name = 'current date as 8 digit integer (YYYYMMDD)'
#   datesec
    datesecid.long_name = 'seconds of current date'
    datesecid.units ='s'
#
#   global data   
    ds.domxmin, = longitude[0], 
#    ds.domxmax, longitude(nlon-1), /FLOAT
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

##################
#   WRITE FIELDS #
##################
#
#   Fill the lat/lon/lev variables
    if ( gridtype == 'latlon' ) :
        latid[0:nlat] = latitude[0:nlat]
        lonid[0:nlon] = longitude[0:nlon]
        areaid[0:nlat,0:nlon] = area[0:nlat,0:nlon] 
    elif ( gridtype == 'irregular' ) :
        latid[0:ncol] = latitude[0:ncol]
        lonid[0:ncol] = longitude[0:ncol]
        areaid[0:ncol] = area[0:ncol] 
    else :  
        print('No gridtype recognized : ', gridtype)
        quit()


    if ( dim == '3-dim' ) :  levid[0:nlev]   = altitude[0:nlev]
    if ( dim == '3-dim' ) : ilevid[0:nlev+1] = altitude_int[0:nlev+1]
#
#   Add the emission
#   convert yearlist to readyearlist
    readyearlist=getreadyearlist.getreadyearlist(yearlist=yearlist, scenario=scenario, activity=activity, i4mpdownload=i4mpdownload) # this should not depend on sector, as sectors end up in same file with same time axis

    yearblocklist=yearlist2blocklist.yearlist2blocklist(yearlist=readyearlist, activity=activity, resolution=resolution)

#   
#    print('yearlist      : ', yearlist)
#    print('readyearlist  : ', readyearlist)
#    print('yearblocklist : ', yearblocklist)  
    
    itime0=0 # important

    nblock=len(yearblocklist)    
    for iblock in range(nblock) :
        readyear0=yearblocklist[iblock][0]       # first element in specific block
        readyear1=yearblocklist[iblock][-1]      # last element in specific block

        nyear=readyear1-readyear0+1

        itime1=itime0 + nyear*nmonth

        for isector in range(0,nsector) :
            sector=sectorlist[isector]

            F = composefield.composefield(activity=activity, sector=sector, species=species, dim=dim, vertdist=vertdist, year0=readyear0, year1=readyear1, longitude=longitude, latitude=latitude, resolution=resolution, altitude_int=altitude_int, scenario=readscenario, i4mpdownload=i4mpdownload, filelocation=filelocation)


            if   ( dim == '2-dim' and gridtype == 'latlon'    ) : sectoridlist[isector][itime0:itime1       ,0:nlat,0:nlon]=F['field'][0:nyear*nmonth,       0:nlat,0:nlon]
            elif ( dim == '3-dim' and gridtype == 'latlon'    ) : sectoridlist[isector][itime0:itime1,0:nlev,0:nlat,0:nlon]=F['field'][0:nyear*nmonth,0:nlev,0:nlat,0:nlon]
            elif ( dim == '2-dim' and gridtype == 'irregular' ) : sectoridlist[isector][itime0:itime1       ,0:ncol       ]=F['field'][0:nyear*nmonth,       0:ncol       ]
            elif ( dim == '3-dim' and gridtype == 'irregular' ) : sectoridlist[isector][itime0:itime1,0:nlev,0:ncol       ]=F['field'][0:nyear*nmonth,0:nlev,0:ncol       ]
            else :
                print('+++ buildemission +++')
                print('No dim recognized : ', dim)
                quit()

            dateid[   itime0:itime1] = date[itime0:itime1]
            datesecid[itime0:itime1] = datesec[itime0:itime1]
            timeid[   itime0:itime1] = 0 # timid, daysince(refdate=17500101L,enddate=date(itime)), OFFSET=[itime]


        itime0=itime0+ nyear*nmonth





#    for iyear in range(0, nyear) :
#        print('iyear = ', iyear)
#
#        itime0=iyear*nmonth
#        itime1=iyear*nmonth + nmonth
#        
#        year=yearlist[iyear]
        
#       read different sectors
#        for isector in range(0,nsector) :
#            sector=sectorlist[isector]

#               obtain orig year
#            if   ( scenario == 'hist' and year == 2024 ) : yearread = 2023
#            elif ( scenario == 'hist' and year == 2025 ) : yearread = 2023
#            else : yearread=year
#
#            F = composefield.composefield(activity=activity, sector=sector, species=species, dim=dim, vertdist=vertdist, year=yearread, longitude=longitude, latitude=latitude, resolution=resolution, altitude_int=altitude_int, scenario=readscenario, i4mpdownload_anthro=i4mpdownload_anthro, i4mpdownload_bb=i4mpdownload_bb, filelocation=filelocation)


#            if   ( dim == '2-dim' and gridtype == 'latlon'    ) : sectoridlist[isector][itime0:itime1       ,0:nlat,0:nlon]=F['field'][0:nmonth,       0:nlat,0:nlon]
#            elif ( dim == '3-dim' and gridtype == 'latlon'    ) : sectoridlist[isector][itime0:itime1,0:nlev,0:nlat,0:nlon]=F['field'][0:nmonth,0:nlev,0:nlat,0:nlon]
#            elif ( dim == '2-dim' and gridtype == 'irregular' ) : sectoridlist[isector][itime0:itime1       ,0:ncol       ]=F['field'][0:nmonth,       0:ncol       ]
#            elif ( dim == '3-dim' and gridtype == 'irregular' ) : sectoridlist[isector][itime0:itime1,0:nlev,0:ncol       ]=F['field'][0:nmonth,0:nlev,0:ncol       ]
#            else :
#                    print('No dim recognized : ', dim)
#                    quit()
##
#            dateid[   itime0:itime1] = date[itime0:itime1]
#            datesecid[itime0:itime1] = datesec[itime0:itime1]
#            timeid[   itime0:itime1] = 0 # timid, daysince(refdate=17500101L,enddate=date(itime)), OFFSET=[itime]

    ds.close()

