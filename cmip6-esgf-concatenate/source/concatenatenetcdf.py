from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np
import math
import os, sys
import datetime

sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getperiodlist
import getrealm
import getexpidsplit
import getrawdirectory
import getlonname
import getlatname

import concatenatenetcdf

def concatenatenetcdf(expid,var,freqfile,yearrange) :
#------------------------------------------------
    '''
    INPUT


    '''



    ntimemax=500


#   try to extract model / scenario / realisation
    expidsplitinfo=getexpidsplit.getexpidsplit(expid=expid)
    model=expidsplitinfo['model']
    scenario=expidsplitinfo['scenario']
    realisation=expidsplitinfo['realisation']
    grid=expidsplitinfo['grid']
#
    print('+++ concatenatenetcdf +++')
    print('expid    : '+expid)
    print('model    : '+model)
    print('var      : '+var)
    print('freqfile : '+freqfile)
    print('--- concatenatenetcdf ---')

# making output directory
#   path = "/nird/home/olivie/output/netcdf-concatenate-cmip6"    # in home to directory : 2022-05-06
    path = "/nird/home/olivie/output/netcdf-concatenate-cmip6-v2" # in home to directory : 2022-08-22
    if  not os.path.isdir(path) : os.mkdir(path)

# try to extract all the periods :
    periodlistinfo=getperiodlist.getperiodlist(expid=expid, var=var, freqfile=freqfile)
    nperiod=periodlistinfo['nperiod']
    year0=periodlistinfo['year0']
    year1=periodlistinfo['year1']
#
    if ( nperiod == 0 ) : return
#
    lastperiod=periodlistinfo['periodlist'][nperiod-1]
#
    print('lastperiod : ')
    print(str(lastperiod))
    print('model : ')
    print(str(model))
    print('scenario : ')
    print(str(scenario))
    print('realisation : ')
    print(str(realisation))
    print('grid : ')
    print(str(grid))

    realm=getrealm.getrealm(var=var, freqfile=freqfile)

    directory=getrawdirectory.getrawdirectory(expid=expid, var=var, freqfile=freqfile)

    nc_f=directory+'/'+var+'_'+realm+'_'+model+'_'+scenario+'_'+realisation+'_'+grid+'_'+lastperiod+'.nc'

    if ( os.path.getsize(nc_f) == 0 ) : return # empty file

    nc_fid= Dataset(nc_f, 'r')                 # open file

    latslist=np.array(nc_fid.variables[getlatname.getlatname(model=model)][:])  # latitudes
    lonslist=np.array(nc_fid.variables[getlonname.getlonname(model=model)][:])  # longitude

    nlon = len(lonslist)
    nlat = len(latslist)

# attributes time
    time_bounds        = nc_fid.variables['time'].bounds
    time_units         = nc_fid.variables['time'].units
    time_calendar      = nc_fid.variables['time'].calendar
    time_axis          = nc_fid.variables['time'].axis
#   time_long_name     = nc_fid.variables['time'].long_name
    time_standard_name = nc_fid.variables['time'].standard_name

# attributes lat  
#   lat_bounds        = nc_fid.variables[getlatname.getlatname(model=model)].bounds 
#  lat_units         = nc_fid.variables[getlatname.getlatname(model=model)].units
    lat_axis          = nc_fid.variables[getlatname.getlatname(model=model)].axis
#   lat_long_name     = nc_fid.variables[getlatname.getlatname(model=model)].long_name
    lat_standard_name = nc_fid.variables[getlatname.getlatname(model=model)].standard_name

# attributes lon
#    lon_bounds        = nc_fid.variables[getlonname.getlonname(model=model)].bounds 
    lon_units         = nc_fid.variables[getlonname.getlonname(model=model)].units
    lon_axis          = nc_fid.variables[getlonname.getlonname(model=model)].axis
#   lon_long_name     = nc_fid.variables[getlonname.getlonname(model=model)].long_name
    lon_standard_name = nc_fid.variables[getlonname.getlonname(model=model)].standard_name
#
# attributes variable
    var_standard_name = nc_fid.variables[var].standard_name 
    var_long_name     = nc_fid.variables[var].long_name 
#   var_comment       = nc_fid.variables[var].comment
    var_units         = nc_fid.variables[var].units
#    var_original_name = nc_fid.variables[var].original_name
    var_cell_methods  = nc_fid.variables[var].cell_methods
    var_cell_measures = nc_fid.variables[var].cell_measures
#   var_history       = nc_fid.variables[var].history
#   var_coordinates   = nc_fid.variables[var].coordinates
    var_missing_value = nc_fid.variables[var].missing_value
    var__FillValue    = nc_fid.variables[var]._FillValue
#
    calendar=nc_fid.variables['time'].calendar # e.g., 'standard', 'gregorian', 'proleptic_gregorian', 'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'
#
# global attributes
    globattr_Conventions = nc_fid.Conventions
    globattr_activity_id = nc_fid.activity_id
    globattr_branch_method = nc_fid.branch_method
#    globattr_branch_time = nc_fid.branch_time
    globattr_branch_time_in_child = nc_fid.branch_time_in_child
    globattr_branch_time_in_parent = nc_fid.branch_time_in_parent
#    globattr_contact = nc_fid.contact
    globattr_creation_date = nc_fid.creation_date
    globattr_data_specs_version = nc_fid.data_specs_version
    globattr_experiment =nc_fid.experiment
    globattr_experiment_id = nc_fid.experiment_id
    globattr_external_variables = nc_fid.external_variables
    globattr_forcing_index = nc_fid.forcing_index
    globattr_frequency = nc_fid.frequency
    globattr_further_info_url = nc_fid.further_info_url
    globattr_grid = nc_fid.grid
    globattr_grid_label = nc_fid.grid_label
#   globattr_history = nc_fid.history
    globattr_initialization_index = nc_fid.initialization_index
    globattr_institution = nc_fid.institution
    globattr_institution_id = nc_fid.institution_id
    globattr_mip_era = nc_fid.mip_era
#    globattr_model_id = nc_fid.model_id
    globattr_nominal_resolution = nc_fid.nominal_resolution
    globattr_parent_activity_id = nc_fid.parent_activity_id
    globattr_parent_experiment_id = nc_fid.parent_experiment_id
    globattr_parent_mip_era = nc_fid.parent_mip_era
    globattr_parent_source_id = nc_fid.parent_source_id
#   parent_sub_experiment_id = nc_fid.parent_sub_experiment
    globattr_parent_time_units = nc_fid.parent_time_units
    globattr_parent_variant_label = nc_fid.parent_variant_label
    globattr_physics_index = nc_fid.physics_index
    globattr_product = nc_fid.product
    globattr_realization_index = nc_fid.realization_index
    globattr_realm = nc_fid.realm
#   globattr_run_variant = nc_fid.run_variant
    globattr_source = nc_fid.source
    globattr_source_id = nc_fid.source_id
    globattr_source_type = nc_fid.source_type
    globattr_sub_experiment = nc_fid.sub_experiment
    globattr_sub_experiment_id = nc_fid.sub_experiment_id
    globattr_table_id = nc_fid.table_id
#   globattr_table_info = nc_fid.table_info
#   globattr_title = nc_fid.title
    globattr_variable_id = nc_fid.variable_id
    globattr_variant_label = nc_fid.variant_label
    globattr_license = nc_fid.license
#   globattr_cmor_version = nc_fid.cmor_version
    globattr_tracking_id = nc_fid.tracking_id

    nc_fid.close

    iyear=0
    ncontr=0
    currentyear=-1
    tmpfld = np.zeros( ( nlat , nlon ) , dtype=float)
    fld = np.zeros( ( ntimemax, nlat , nlon ) , dtype=float)
    yearlist = np.zeros ( (ntimemax) , dtype=int)

    for iperiod in range(0,nperiod) : 

        period=periodlistinfo['periodlist'][iperiod]
# reading netcdf file
        nc_f=directory+'/'+var+'_'+realm+'_'+model+'_'+scenario+'_'+realisation+'_'+grid+'_'+period+'.nc'

        nc_fid= Dataset(nc_f, 'r')                               # open the file -> gets an "ID"
        fieldall=np.squeeze(np.array(nc_fid.variables[var][:])) # extract the 3D field
        print(fieldall[0:10,0,0])
        units=nc_fid.variables[var].units                       # extract the units
        times=np.squeeze(np.array(nc_fid.variables['time'][:]))
        time_units=nc_fid.variables['time'].units                # time units : since ....
        calendar=nc_fid.variables['time'].calendar               # calendar
        nc_fid.close 

        ntime=len(times)

        for itime in range(0,ntime) : 

# find date
            date=nc.num2date(times[itime],time_units,calendar=calendar)

            if ( date.year >= yearrange[0] \
             and date.year <= yearrange[1] ) :       

                yyyy = str("%4.4i"% (date.year))
                mm   = str("%4.4i"% (date.month))
                dd   = str("%4.4i"% (date.day))

                print(yyyy+' '+mm+' '+dd)

# adding or averaging
                if ( date.year == currentyear or currentyear == -1 ) :
                    tmpfld=tmpfld+fieldall[itime,:,:]   # add up the field
                    ncontr=ncontr+1
                    currentyear = date.year
                else :
# write down former year                
                    fld[iyear,:,:]=tmpfld/float(ncontr) # divide to get avearage
                    yearlist[iyear]=currentyear
# start                                  
                    tmpfld=fieldall[itime,:,:]          # get first field
                    ncontr=1.                           
                    currentyear=date.year
                    iyear=iyear+1

                print(currentyear)
#
# adding last sample if something left in the buffer
    if ( ncontr != 0 ) : 
        fld[iyear,:,:]=tmpfld/float(ncontr) # divide to get avearage
        yearlist[iyear]=currentyear

    nyear=iyear+1
#
#######################
# create one new file #
#######################

    period=str("%4.4i"% (max([year0,yearrange[0]])))+'-'+str("%4.4i"% (min([year1,yearrange[1]])))
    realm='Ayr'
#    
    fn=path+'/'+var+'_'+realm+'_'+model+'_'+scenario+'_'+realisation+'_'+grid+'_'+period+'.nc'
#   ds = nc.Dataset(fn, 'w', format='NETCDF4')
    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   create dimensions
    time = ds.createDimension('time', None)
    lat = ds.createDimension('lat', nlat)
    lon = ds.createDimension('lon', nlon)

#   create variables
    times = ds.createVariable('time', 'f4', ('time',))
    lats = ds.createVariable('lat', 'f4', ('lat',))
    lons = ds.createVariable('lon', 'f4', ('lon',))
    value = ds.createVariable(var, 'f4', ('time', 'lat', 'lon',), fill_value=var__FillValue)

#   variable attributes
#    value.units = 'Unknown'                                            # attribute
#    lats.units = 'Degree North'
#    times.units = 'Days since whatever time ...'

# attributes time
    times.bounds        = time_bounds
    times.units         = time_units
    times.calendar      = time_calendar
    times.axis          = time_axis
#   times.long_name     = time_long_name
    times.standard_name = time_standard_name

# attributes lat  
#   lats.bounds        = lat_bounds 
#  lats.units         = lat_units
    lats.axis          = lat_axis
#   lats.long_name     = lat_long_name
    lats.standard_name = lat_standard_name

# attributes lon
#    lons.bounds        = lon_bounds 
    lons.units         = lon_units
    lons.axis          = lon_axis
#   lons.long_name     = lon_long_name
    lons.standard_name = lon_standard_name
#
# attributes variable
    value.standard_name = var_standard_name
    value.long_name     = var_long_name
#   value.comment       = var_comment
    value.units         = var_units
#    value.original_name = var_original_name
    value.cell_methods  = var_cell_methods
    value.cell_measures = var_cell_measures
#   value.history       = var_history
#   value.coordinates   = var_coordinates
    value.missing_value = var_missing_value
#    value._FillValue    = var__FillValue  # should be done during creation of value
#
# GLOBAL ATTRIBUTES


#
    ds.description = 'Trying global attribute'
    ds.source_id = 'Trying global attribute'
    ds.brol = 'Trying global attribute'

# global attributes
    ds.Conventions = globattr_Conventions
    ds.activity_id = globattr_activity_id
    ds.branch_method = globattr_branch_method
#    ds.branch_time = globattr_branch_time
    ds.branch_time_in_child = globattr_branch_time_in_child
    ds.branch_time_in_parent = globattr_branch_time_in_parent
#    ds.contact = globattr_contact
    ds.creation_date = globattr_creation_date
    ds.data_specs_version = globattr_data_specs_version
    ds.experiment =globattr_experiment
    ds.experiment_id = globattr_experiment_id
    ds.external_variables = globattr_external_variables
    ds.forcing_index = globattr_forcing_index
    ds.frequency = globattr_frequency
    ds.further_info_url = globattr_further_info_url
    ds.grid = globattr_grid
    ds.grid_label = globattr_grid_label
#   ds.history = globattr_history
    ds.initialization_index = globattr_initialization_index
    ds.institution = globattr_institution
    ds.institution_id = globattr_institution_id
    ds.mip_era = globattr_mip_era
#    ds.model_id = globattr_model_id
    ds.nominal_resolution = globattr_nominal_resolution
    ds.parent_activity_id = globattr_parent_activity_id
    ds.parent_experiment_id = globattr_parent_experiment_id
    ds.parent_mip_era = globattr_parent_mip_era
    ds.parent_source_id = globattr_parent_source_id
#   parent_sub_experiment_id = globattr_parent_sub_experiment
    ds.parent_time_units = globattr_parent_time_units
    ds.parent_variant_label = globattr_parent_variant_label
    ds.physics_index = globattr_physics_index
    ds.product = globattr_product
    ds.realization_index = globattr_realization_index
    ds.realm = globattr_realm
#   ds.run_variant = globattr_run_variant
    ds.source = globattr_source
    ds.source_id = globattr_source_id
    ds.source_type = globattr_source_type
    ds.sub_experiment = globattr_sub_experiment
    ds.sub_experiment_id = globattr_sub_experiment_id
    ds.table_id = globattr_table_id
#   ds.table_info = globattr_table_info
#   ds.title = globattr_title
    ds.variable_id = globattr_variable_id
    ds.variant_label = globattr_variant_label
    ds.license = globattr_license
#   ds.cmor_version = globattr_cmor_version
    ds.tracking_id = globattr_tracking_id

#
#   ADDING VALUES FOR TIME 1
    value[0:nyear,:,:] = fld[0:nyear,:,:]

#
#   DATES
    timelist=np.zeros( (nyear) ) 
    for iyear in range(0,nyear) : 
        date = datetime.datetime(yearlist[iyear], 7, 1)
        timelist[iyear] = nc.date2num(date, time_units, calendar=calendar)

    times[0:nyear] = timelist[0:nyear]

#
#   LATITUDES / LONGITUDES
    lats[0:nlat] = latslist[0:nlat]
    lons[0:nlon] = lonslist[0:nlon] 

    ds.close()
