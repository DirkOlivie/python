from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys
#import datetime

#import modifyunitsfield
#import correctnanfield
import interpolatefield
#import transposefield

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-volcaod-input4mips/source')
import getstandardunits
import readfield_volc_cmip7_input4mips

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import bndstwodim2bnds

def buildvolcaod(inputperiod,outputperiod,inputversion,outputversion, desiredheightunits,desiredextinctionunits,wvl_interpolation_type, var_weighting_type, overwrite) :
#---------------
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
        inputperiod
        outputperiod
        inputversion           : 'UOEXETER-CMIP-1-2-0' | ...
        outputversion
        desiredheightunits
        desiredextinctionunits
        wvl_interpolation_type : constant | blackbody
        var_weighting_type     : NOT YET USED
        overwrite              : False | True

    CALLED BY
       loopvolc2 

    CALLS
        getstandardunits
        readfield_volc_cmip7_input4mips
        interpolatefield

    MODIFICATIONS
        (2025-01-15) creation
        (2026-10-28) readfield_volc_cmip7_input4mips needs extra inputargument 'origin' 

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
    path = '/scratch/olivie/code/python/cmip7-volcaod-input4mips-to-noresm/data/output'
    if  not os.path.isdir(path) : os.makedirs(path)
#
#   1.a reading some information from CMIP7 input4MIPs file : lat, lat_bnds, height, height_bnds
#-----------------------------------------------------------
    nc_f='/datalake/NS9560K/noresm3/input4mips/cmip7/'+inputversion+'/asy_input4MIPs_aerosolProperties_CMIP_'+inputversion+'_gnz_'+inputperiod+'.nc'

    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')

#   latitude    
    latitude        = np.array(nc_fid.variables['lat'][:])       # lat
    latitude_units  =          nc_fid.variables['lat'].units     # units
    latitude_bnds   = np.array(nc_fid.variables['lat_bnds'][:])  # lat_bnds

#   height/altitude
    height       = np.array(nc_fid.variables['height'][:])      # height 
    height_units =          nc_fid.variables['height'].units    # units
    height_bnds  = np.array(nc_fid.variables['height_bnds'][:]) # height_bnds

    nc_fid.close

#   number of latitudes and numpber of levels in input data
    nlat=len(latitude)
    nheight=len(height)
#
#   1.b reading some information from CMIP6 input4MIPs file
#----------------------------------------------------------
#   wl1_sun, wl2_sun, wl1_earth, wl2_earth
#   nc_f='/scratch/olivie/noresm-inputdata/atm/cam/volc/CMIP_CAM6_radiation_v3.nc'
    nc_f='/nird/datalake/NS2345K/olivie/volcaod-auxiliary/inputdata/atm/cam/volc/CMIP_CAM6_radiation_v3.nc'

    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')

#   shortwave in NorESM 
#   lower bounds 
    wl1_sun       =                          np.array(nc_fid.variables['wl1_sun'][:])
    wl1_sun_units = getstandardunits.getstandardunits(nc_fid.variables['wl1_sun'].units)  # will be something like ower boundary of wavelength of solar band in um
#   upper bounds
    wl2_sun       =                          np.array(nc_fid.variables['wl2_sun'][:])
    wl2_sun_units = getstandardunits.getstandardunits(nc_fid.variables['wl2_sun'].units)
#
#   longwave in NorESM
#   lower bounds
    wl1_earth       =                          np.array(nc_fid.variables['wl1_earth'][:])
    wl1_earth_units = getstandardunits.getstandardunits(nc_fid.variables['wl1_earth'].units)
#   upper bounds
    wl2_earth       =                          np.array(nc_fid.variables['wl2_earth'][:])
    wl2_earth_units = getstandardunits.getstandardunits(nc_fid.variables['wl2_earth'].units)
#
    nc_fid.close

#   number of wavelength bands in NorESM2
    nsun  =len(wl1_sun)
    nearth=len(wl1_earth)
#
#   check that all 4 wavelength units are equal
    if ( wl1_sun_units != wl2_sun_units  \
      or wl1_sun_units != wl1_earth_units \
      or wl1_sun_units != wl2_earth_units ) :
        print('+++ volc_internal +++')
        print('Different units for wavelengths : ', wl1_sun_units, wl2_sun_units, wl1_earth_units, wl1_earth_units)
        quit()
    
#   the wavelength units from the NorESM file
    wavelength_units=wl1_sun_units

#   make 1-dimensional arrays
#   earth
#    wvl_bnds_sun         = np.zeros((nsun+1), dtype=float)
#    wvl_bnds_sun[0:nsun] = wl1_sun[0:nsun  ]
#    wvl_bnds_sun[  nsun] = wl2_sun[  nsun-1]
    wvl_bnds_sun = bndstwodim2bnds.bndstwodim2bnds(lowerbnds=wl1_sun,upperbnds=wl2_sun)

#   sun
#    wvl_bnds_earth           = np.zeros((nearth+1), dtype=float)
#    wvl_bnds_earth[0:nearth] = wl1_earth[0:nearth  ]
#    wvl_bnds_earth[  nearth] = wl2_earth[  nearth-1]
    wvl_bnds_earth = bndstwodim2bnds.bndstwodim2bnds(lowerbnds=wl1_earth,upperbnds=wl2_earth)

#######################
#   2. create one new file #
#######################
#    
    fn=path+'/'+inputversion+'_'+outputperiod+'_WVLWEIGHT'+wvl_interpolation_type+'_'+outputversion+'.nc'
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
######################
#   3. read all data # NO DISTICNCTION BETWEEN SW AND LW
######################

    ext = readfield_volc_cmip7_input4mips.readfield_volc_cmip7_input4mips(var='ext',mipversion=inputversion,period=inputperiod,origin='input4mips') # extinction
    ssa = readfield_volc_cmip7_input4mips.readfield_volc_cmip7_input4mips(var='ssa',mipversion=inputversion,period=inputperiod,origin='input4mips') # single scattering albedo - omega
    asy = readfield_volc_cmip7_input4mips.readfield_volc_cmip7_input4mips(var='asy',mipversion=inputversion,period=inputperiod,origin='input4mips') # assymetrie               - g

#####################
#   4. modify units # NOT NEEDED ANYMORE - ALREADY DONE DURING READING
#####################
#
#   modify height units (to desiredheightunits) and variable units
#    ext = modifyunitsfield.modifyunitsfield(data=ext, desiredheightunits=desiredheightunits, desiredfieldunits=desiredextinctionunits,desiredwavelengthunits=wavelength_units)
#    ssa = modifyunitsfield.modifyunitsfield(data=ssa, desiredheightunits=desiredheightunits,                                          desiredwavelengthunits=wavelength_units)
#    asy = modifyunitsfield.modifyunitsfield(data=asy, desiredheightunits=desiredheightunits,                                          desiredwavelengthunits=wavelength_units)

####################
#   5. correct nan # NOT NEEDED ANYMORE - ALREADY DONE DURING READING
####################

#    ext = correctnanfield.correctnanfield(data=ext)
#    ssa = correctnanfield.correctnanfield(data=ssa)
#    asy = correctnanfield.correctnanfield(data=asy)

#########################################
#   5. interpolate to NorESM wavelength #
#########################################
#   5.a solar radiation : to the NorESM bands (wl1_sun and wl2_sun)
    ext_solar=interpolatefield.interpolatefield(origdata=ext,wavelength_bnds=wvl_bnds_sun,wavelength_units=wavelength_units, wvl_interpolation_type=wvl_interpolation_type, wvl_group_type='SW')
    ssa_solar=interpolatefield.interpolatefield(origdata=ssa,wavelength_bnds=wvl_bnds_sun,wavelength_units=wavelength_units, wvl_interpolation_type=wvl_interpolation_type, wvl_group_type='SW')
    asy_solar=interpolatefield.interpolatefield(origdata=asy,wavelength_bnds=wvl_bnds_sun,wavelength_units=wavelength_units, wvl_interpolation_type=wvl_interpolation_type, wvl_group_type='SW')

#   5.b terrestrial radiation : to the NorESM bands (wl1_earth an wl2_earth)
    ext_earth=interpolatefield.interpolatefield(origdata=ext,wavelength_bnds=wvl_bnds_earth,wavelength_units=wavelength_units, wvl_interpolation_type=wvl_interpolation_type, wvl_group_type='LW')
    ssa_earth=interpolatefield.interpolatefield(origdata=ssa,wavelength_bnds=wvl_bnds_earth,wavelength_units=wavelength_units, wvl_interpolation_type=wvl_interpolation_type, wvl_group_type='LW')
    asy_earth=interpolatefield.interpolatefield(origdata=asy,wavelength_bnds=wvl_bnds_earth,wavelength_units=wavelength_units, wvl_interpolation_type=wvl_interpolation_type, wvl_group_type='LW')


####################################################
#   6. transpose : interchange height and latitude #
####################################################
    
#    ext_solar=transposefield.transposefield(data=ext_solar)
#    ssa_solar=transposefield.transposefield(data=ssa_solar)
#    asy_solar=transposefield.transposefield(data=asy_solar)

#    ext_earth=transposefield.transposefield(data=ext_earth)
#    ssa_earth=transposefield.transposefield(data=ssa_earth)
#    asy_earth=transposefield.transposefield(data=asy_earth)


############################
#   7. Loop over all dates #
############################
    ntime=ext_solar['ntime']  # take one of the 6 files

    for itime in range(ntime) :  
        
        year  = ext_solar['yearlist'][itime]
        month = ext_solar['monthlist'][itime]

        vdate[itime] = year * 10000. + month * 100. + 16. # date format in NorESM
        vdatesec[itime]=0                                 # seconds     in NorESM  

        print('Date : ', vdate[itime])

#       loop over shortwavebands
        for i in range(nsun) :

#            print('Solar : ', i)

            vext_sun[  i][itime,:,:] = ext_solar['field'][itime,:,:,i]
            vomega_sun[i][itime,:,:] = ssa_solar['field'][itime,:,:,i]
            vg_sun[    i][itime,:,:] = asy_solar['field'][itime,:,:,i]
             
#       loop over longwavebands
        for i in range(nearth) :

#            print('Earth : ', i)

            vext_earth[  i][itime,:,:] = ext_earth['field'][itime,:,:,i]
            vomega_earth[i][itime,:,:] = ssa_earth['field'][itime,:,:,i]
            vg_earth[    i][itime,:,:] = asy_earth['field'][itime,:,:,i]


#       fille the time
#      date = datetime.datetime(year, month, 15)
#        timelist[itime] = nc.date2num(date, time_units, calendar=calendar)

#    times[0:ntime] = timelist[0:ntime]
#
#    value.units=D['units']    

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
