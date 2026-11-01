from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys
#import datetime

#import modifyunitsfield
#import correctnanfield
#import interpolatefield
#import transposefield
import origindescriptionlist2ascii

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-volcaod-input4mips/source')
import getstandardunits
import readfield_volc_cmip7_input4mips
import assemblefield_volc_cmip7_input4mips

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
#import bndstwodim2bnds

def buildvolcaodbenjohnson(inputversion, origindescriptionlist, outputversion, hybridperiod, desiredheightunits, desiredextinctionunits, intpmethod, overwrite) :
#-------------------------
    '''
    REMARK
        New file should have dimensions order : (time, altitude, lat)
        Based on CMIP6 file : /cluster/shared/noresm/inputdata/atm/cam/volc/CMIP_CAM6_radiation_v3_reformatted.nc

    METHODOLOGY
        latitudes : keep from input4MIPS lat, lat_bnds           -> latitide
        height    : keep from input4MIPS height, height_bnds [m] -> altitude, altitude_int [km]
                                                                 -> datesec
                                                                 -> time
                                                                 -> date   

    INPUT
        period
        inputversion           : 'UOEXETER-CMIP-1-2-0' | ...
        outputversion
        desiredheightunits
        desiredextinctionunits
        intpmethod
        overwrite

    CALLED BY
       loopvolc2 

    CALLS
        getstandardunits
        readfield_volc_cmip7_input4mips
        interpolatefield

    MODIFICATIONS
        (2025-01-15) creation

    NETCDF
        Specifier   Datatype                    Old typecodes
        'f4'        32-bit floating point   'f'
        'f8'        64-bit floating point   'd'
        'i4'        32-bit signed integer   'i' 'l'
        'i2'        16-bit signed integer   'h' 's'
        'i8'        64-bit signed integer   
        'i1'        8-bit signed integer    'b' 'B'
        'u1'        8-bit unsigned integer  
        'u2'        16-bit unsigned integer     
        'u4'        32-bit unsigned integer     
        'u8'        64-bit unsigned integer     
        'S1'        single-character string     'c'

    '''

    print('+++ volc_internal +++')

#   making output directory
    path = '/scratch/olivie/code/python/cmip7-volcaod-benjohnson-to-noresm/data/output'
    if  not os.path.isdir(path) : os.makedirs(path)
#
############################################################
#   1. reading some information from CMIP7 benjohnson file # lat, lat_bnds, height, height_bnds
############################################################

#   ext_solar = readfield_volc_cmip7_input4mips.readfield_volc_cmip7_input4mips(var='ext',mipversion=inputversion,period=period,origin='benjohnson',spectrum='sw', intpmethod=intpmethod)
    ext_solar = readfield_volc_cmip7_input4mips.readfield_volc_cmip7_input4mips(var='ext',mipversion=origindescriptionlist[0]['i4mpdownload'], \
                                                                                          period=origindescriptionlist[0]['origperiod'], \
                                                                                          scenario=origindescriptionlist[0]['scenario'], \
                                                                                          origin='benjohnson',spectrum='sw', intpmethod=intpmethod)
    latitude       = ext_solar['latitude']
    latitude_units = ext_solar['latitude_units']
    latitude_bnds  = ext_solar['latitude_bnds']
    nlat           = len(ext_solar['latitude'])

    height       = ext_solar['height']
    height_units = ext_solar['height_units']
    height_bnds  = ext_solar['height_bnds']
    nheight      = len(ext_solar['height'])

    nsun = len(ext_solar['wavelength'])

    ext_earth = readfield_volc_cmip7_input4mips.readfield_volc_cmip7_input4mips(var='ext',mipversion=origindescriptionlist[0]['i4mpdownload'], \
                                                                                          period=origindescriptionlist[0]['origperiod'], \
                                                                                          scenario=origindescriptionlist[0]['scenario'], \
                                                                                          origin='benjohnson',spectrum='lw', intpmethod=intpmethod)
    nearth    = len(ext_earth['wavelength'])

#   CHECK DESIRED UNITS
    if ( ( ext_solar['units'] != desiredextinctionunits ) \
      or ( ext_earth['units'] != desiredextinctionunits ) ) :
        print('+++ buildvolcaodbenjohnson +++')
        print('Units of extinction differ from desired units : ', ext_solar['units'], ext_earth['units'], desiredextinctionunits)
        quit()

#   CHECK HEIGHT UNITS
    if ( ( ext_solar['height_units'] != desiredheightunits ) \
      or ( ext_earth['height_units'] != desiredheightunits ) ) :
        print('+++ buildvolcaodbenjohnson +++')
        print('Units height differ from desired units : ', ext_solar['height_units'], ext_earth['height_units'], desiredheightunits)
        quit()

############################
#   2. create one new file #
############################
#
#    year0=origindescriptionlist[0]['year']
#    year1=origindescriptionlist[-1]['year']

#    period=str("%4.4i"% (year0))+'01-'+str("%4.4i"% (year1))+'12'    
    fn=path+'/'+inputversion+'_'+hybridperiod+'_'+intpmethod+'_'+outputversion+'.nc'
    print(fn)

#   stop when file exists
    if ( os.path.isfile(fn) and ( overwrite == False) ) : return

    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   2.a create dimensions [name starts with "d"]
    dtime       = ds.createDimension('time', None)
    dheight     = ds.createDimension('altitude', nheight)
    dheight_int = ds.createDimension('altitude_int', nheight+1)
    dlatitude   = ds.createDimension('lat',nlat)

#   2.b create basic variables [name startw with "v"]
    vtime       = ds.createVariable('time'        , 'f8', ('time',))
    vdate       = ds.createVariable('date'        , 'f8', ('time',) , fill_value=-9999.)   # YYYYMMDD, where DD=16
    vdatesec    = ds.createVariable('datesec'     , 'i4', ('time',) , fill_value=-9999) 
    vheight     = ds.createVariable('altitude'    , 'f8', ('altitude',))
    vheight_int = ds.createVariable('altitude_int', 'f8', ('altitude_int',))
    vlatitude   = ds.createVariable('lat'         , 'f8', ('lat',))

    vlatitude.units = latitude_units      # take over from original file
    vheight.units   = desiredheightunits  # impose desired units

#   2.c create relevant fields and units attributes for shortwave
    vext_sun   = [] # empty list
    vomega_sun = [] # empty list
    vg_sun     = [] # empty list   

    vext_sun_units   = []
    vomega_sun_units = []
    vg_sun_units     = []
 
#   loop over all SW bands
    for i in range(nsun) : 
        strcounter=str(i+1) # starts at 1 - ... - 14 
#       creating variables 
        vext_sun.append(  ds.createVariable('ext_sun'  +strcounter, 'f8', ('time', 'altitude', 'lat',))) # extinction  
        vomega_sun.append(ds.createVariable('omega_sun'+strcounter, 'f8', ('time', 'altitude', 'lat',))) # omega 
        vg_sun.append(    ds.createVariable('g_sun'    +strcounter, 'f8', ('time', 'altitude', 'lat',))) # g   

#       attributes
        vext_sun[i].units   = 'extinction coefficient of solar bands in '+desiredextinctionunits
        vomega_sun[i].units = 'single scattering albedo of solar bands'
        vg_sun[i].units     = 'asymmetry factor of solar bands'
        
#   2.d create relevant fields and units attributes for longwave
    vext_earth   = []
    vomega_earth = []
    vg_earth     = []   

    vext_earth_units   = []
    vomega_earth_units = []
    vg_earth_units     = []
 
#   loop over all LW bands
    for i in range(nearth) : 
        strcounter=str(i+1)  # starts at 1 - ... - 16
#       creating variables
        vext_earth.append(  ds.createVariable('ext_earth'  +strcounter, 'f8', ('time', 'altitude', 'lat',)))    
        vomega_earth.append(ds.createVariable('omega_earth'+strcounter, 'f8', ('time', 'altitude', 'lat',)))    
        vg_earth.append(    ds.createVariable('g_earth'    +strcounter, 'f8', ('time', 'altitude', 'lat',)))    

#       attributes
        vext_earth[i].units   = 'extinction coefficient of terrestrial bands in '+desiredextinctionunits
        vomega_earth[i].units = 'single scattering albedo of terrestrial bands'
        vg_earth[i].units     = 'asymmetry factor of terrestrial bands'
#
#   2.e global data
    origin = origindescriptionlist2ascii.origindescriptionlist2ascii(origindescriptionlist)
    ds.origin = origin
#
######################
#   3. read all data # (from benjohnson file)
######################
#
    ext_solar = assemblefield_volc_cmip7_input4mips.assemblefield_volc_cmip7_input4mips(var='ext', origindescriptionlist=origindescriptionlist, origin='benjohnson', spectrum='sw', intpmethod=intpmethod) # ext - sw
    ssa_solar = assemblefield_volc_cmip7_input4mips.assemblefield_volc_cmip7_input4mips(var='ssa', origindescriptionlist=origindescriptionlist, origin='benjohnson', spectrum='sw', intpmethod=intpmethod) # ssa - sw
    asy_solar = assemblefield_volc_cmip7_input4mips.assemblefield_volc_cmip7_input4mips(var='asy', origindescriptionlist=origindescriptionlist, origin='benjohnson', spectrum='sw', intpmethod=intpmethod) # asy - sw

    ext_earth = assemblefield_volc_cmip7_input4mips.assemblefield_volc_cmip7_input4mips(var='ext', origindescriptionlist=origindescriptionlist, origin='benjohnson', spectrum='lw', intpmethod=intpmethod) # ext - lw
    ssa_earth = assemblefield_volc_cmip7_input4mips.assemblefield_volc_cmip7_input4mips(var='ssa', origindescriptionlist=origindescriptionlist, origin='benjohnson', spectrum='lw', intpmethod=intpmethod) # ssa - lw
    asy_earth = assemblefield_volc_cmip7_input4mips.assemblefield_volc_cmip7_input4mips(var='asy', origindescriptionlist=origindescriptionlist, origin='benjohnson', spectrum='lw', intpmethod=intpmethod) # asy - lw

####################
#   4. correct nan #
####################
    ext_solar['field'][np.isnan(ext_solar['field'])] = 0
    ssa_solar['field'][np.isnan(ssa_solar['field'])] = 0
    asy_solar['field'][np.isnan(asy_solar['field'])] = 0
#
    ext_earth['field'][np.isnan(ext_earth['field'])] = 0
    ssa_earth['field'][np.isnan(ssa_earth['field'])] = 0
    asy_earth['field'][np.isnan(asy_earth['field'])] = 0
    
############################
#   5. Loop over all dates #
############################
    ntime=ext_solar['ntime']  # take one of the 6 files

    for itime in range(ntime) :  
        
        year  = ext_solar['yearlist'][itime]
        month = ext_solar['monthlist'][itime]

        vdate[itime]    = year * 10000. + month * 100. + 16. # date format in NorESM
        vdatesec[itime] = 0                                  # seconds     in NorESM  ; in CMIP6 we had it also on 0

        print('Date : ', vdate[itime])

#       loop over shortwavebands
        for i in range(nsun) :

            vext_sun[  i][itime,:,:] = ext_solar['field'][itime,:,:,i]
            vomega_sun[i][itime,:,:] = ssa_solar['field'][itime,:,:,i]
            vg_sun[    i][itime,:,:] = asy_solar['field'][itime,:,:,i]
             
#       loop over longwavebands
        for i in range(nearth) :

            vext_earth[  i][itime,:,:] = ext_earth['field'][itime,:,:,i]
            vomega_earth[i][itime,:,:] = ssa_earth['field'][itime,:,:,i]
            vg_earth[    i][itime,:,:] = asy_earth['field'][itime,:,:,i]

#

    print(nlat)
#   LATITUDES / LONGITUDES
    vlatitude[:] = ext_solar['latitude'][:] 

#   HEIGHT
    vheight[:] = ext_solar['height'][:]

#   HEIGHT_INT : in NorESM is 1-dimesional array
    vheight_int[:] = ext_solar['height_bnds'][:]

#
    ds.close()
