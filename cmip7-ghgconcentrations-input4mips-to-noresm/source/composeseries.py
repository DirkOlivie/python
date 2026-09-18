import numpy as np

import assembleseries
import fill1pctco2abrupt4xco2
import fillfromcesm2cmip6

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-ghgconcentrations-input4mips/source')
import getemptydata 

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import interp1d


def composeseries(scenario, yearrange, species, source, fixedvalue, timeresolution, region, latitude, i4mpdownload):
#----------------
    ''' 
    AIM
	    getting timeseries of GHGs
	    history  : do possibly correction for year 2023 (take 2022 values)
	    scenario : do possibly correction for year ... (take ... values)
	    units are kept as in original time series
        does zonal interpolation

    REMARK
	    if year = 2023 and scenario = 'CMIP' --> takes year 2022 values

    INPUT
	    scenario       : 'CMIP' | 'ScenarioMIP' | 'CMIP-1pctco2' | 'CMIP-abrupt4xco2'
	    yearrange      : 2-elementa array : [year0, year1]
	    species        : 'co2', 'ch4', ... (GHG name as in original input4MIPs NetCDF file)
        source         : 'standard' | 'fixedvalue' ! 'cesm2cmip6' 
	    timeresolution : 'monthly' | 'annual'
	    region         : 'GLOBAL', 'ZONAL', 'NH', 'SH', ...                                 [original resolution]
        latitude       : desired latitudes                                                  [final resolution]
	    i4mpdownload  

    RETURN
	    structure containing
		    timelist  :
		    valuelist :
		    ntime
		    name
		    unit		
 
    CALLED BY
	    buildconcentration

    CALLS 
	    assembleseries
	    getemptydata
        interp1d [interpolation over the latitudes]
    '''
#----------------------------------------------------------------
#
    print('+++ composeseries +++')
#
#   I. read original series (the original period can be longer than what is actually wanted)
#--------------------------
    if ( species != '-' ) :
        S = assembleseries.assembleseries(scenario=scenario, timeresolution=timeresolution, region=region, species=species, source=source, fixedvalue=fixedvalue, i4mpdownload=i4mpdownload) # ORIGINAL SERIES
        print, np.min(S['valuelist']), np.max(S['valuelist'])
#
    print('Original latitudes')
    print('latitudes              : ', S['latitude'])
    print('ntime                  : ', S['ntime'])
    print('orignal values (shape) : ', S['valuelist'].shape)
    print('original units         : ', S['units'])

#   II. generate new series and fill latitudes and times
#-------------------------------------------------------
#   range
    year0=yearrange[0]
    year1=yearrange[1]

    nyear = year1 - year0 +1

#   timeresolution (is the same in the reading and final file)
    if   ( timeresolution == 'annual'  ) : nmonth = 1
    elif ( timeresolution == 'monthly' ) : nmonth = 12 
    else :
        print('No timeresolution recognized : ', timeresolution)
        quit()

#   Final datastructure (with desired time range, with desired latitudinal timeresolution)
    nlat=len(latitude)
    F=getemptydata.getemptydata(ntimemax=nyear*nmonth,nlatmax=nlat,timestamp='date')

#   Fill the latitudes in the structure 
    F['latitude'][:]=latitude[:]
    F['nlat'] = len(F['latitude'][:])

#   fill the dates in the structure
    itime=0
    for year in range(year0,year1+1) :
        for month in range(1,nmonth+1) :
            if (   timeresolution == 'annual'  ) : F['timelist'][itime] = year * 10000 +     7 * 100 +  2  # 2nd of July      
            elif ( timeresolution == 'monthly' ) : 
                if ( month == 2 ) : middleday = 15
                else              : middleday = 16

                F['timelist'][itime] = year * 10000 + month * 100 + middleday # middle of each month
            else :
                print('No timeresolution recognized : ', timeresolution)
                quit()
      
            itime = itime+1
#
    ntime=itime

#   III. Compare the dates in original and final series : find correspondence + latitude interpolation
#--------------------------------------------------------
    if ( species != '-' ) :
#       loop over all times
        for itime in range(0,ntime) :
#
#           check whether year is equal to 2023 and scenario is 'CMIP' -> take 2022 
            year = F['timelist'][itime] // 10000 # integer division
            if ( year == 2023 and ( scenario == 'CMIP' and i4mpdownload == 'CR-CMIP-1-0-0' ) ) :
                time = F['timelist'][itime] - 10000  # go one year back    
            else :
                time= F['timelist'][itime]

#           select in original timeseries where data is equal
            isubset = ( S['timelist'] == time )

#           select corresponding time and do interpolation         
            F['valuelist'][itime,:] = interp1d.interp1d(x=S['latitude'], fx=np.squeeze(S['valuelist'][isubset,:], axis=0), y=F['latitude']) # squeezing was necessary
#        
        F['name']  = S['name']
        F['units'] = S['units']
        F['ntime'] = ntime
#
    else : # species = '-'
#
        F['valuelist'][:,:] =  0. # put the field on zero
        F['name']           = '-' # species
        F['units']          = 'unitless'
        F['ntime']          = ntime
#

#   IV. Do 4xCO2 and 1pctCO2 [should be done on final interpolated fields]
#---------------------------
    if ( scenario == 'CMIP-1pctco2' \
      or scenario == 'CMIP-abrupt4xco2' ) :
        F = fill1pctco2abrupt4xco2.fill1pctco2abrupt4xco2(D=F, scenario=scenario, species=species)    

    else :
        print('Nothing to be done')

#   returns structure
    return F
