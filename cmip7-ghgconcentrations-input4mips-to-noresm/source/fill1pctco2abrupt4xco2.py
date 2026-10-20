import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import daysince


def fill1pctco2abrupt4xco2(D, scenario, species):
#---------------------------
    '''
    MODIFICATIONS
        (2026-10-18) : adding possibility for CMIP-abrupt2xCO2 and CMIP-abrupt0p2xCO2

    INPUT
        D : structure which contains 1850 data for all years
        scenario
        species
    
    RETURN
        D (modified)    

    CALLS
        daysince


    '''
#  
    print('+++ fill1pctco2abrupt4xco2 +++')
#
#   0. properties of original constant timeseries (1850)
#-------------------------------------------------------
    latitude = D['latitude']
    nlat     = D['nlat']
    ntime    = D['ntime']
#
#   1. year to select from original constant timeseries (1850)
#-------------------------------------------------------------
    if   ( scenario == 'CMIP-1pctco2'     ) : refyear=0
    elif ( scenario == 'CMIP-abrupt4xco2' \
        or scenario == 'CMIP-abrupt2xco2' \
        or scenario == 'CMIP-abrupt0p5xco2' ) : refyear=1850
    else :
        print('+++ fill1pctco2abrupt4xco2 +++')
        print('No scenario recognized : ', scenario)
        quit()
#
#   2. extract data from the reference year
#------------------------------------------
    isubset = ( D['timelist'] >= refyear*10000 ) * ( D['timelist'] < (refyear+1) * 10000 )
    data = D['valuelist'][isubset,:] # contains only the 1850 data
    n0,n1=data.shape

#   n0 should be 1 or 12
    if ( n0 != 1 and n0 != 12 ) : 
        print('+++ fill1pctco2series +++')
        print('No valid number of timesteps : ', n0)
        quit()

#   3. calculate global mean average of this extract[average over latitudes and time]
#-----------------------------------------------------------------------------------
#   empty weights
    weight = data * 0.

#   add latitude weighting
    for ilat in range(0,nlat) :
        weight[:,ilat] = np.cos(np.pi/180.*latitude[ilat])

#   add month length weighting
    monthlen=[31.,28.,31.,30.,31.,30.,31.,31.,30.,31.,30.,31.]
    nmonth=12
    if ( n0 == 12 ) :
        for imonth in range(0,nmonth) :
            weight[imonth,:] = weight[imonth,:]*monthlen[imonth] 

#   calculate global annual mean
    globav = np.sum(weight*data)/np.sum(weight)

#   4. loop over all times and modify the values
#-----------------------------------------------
    for itime in range(0,ntime) :

#       4.1 1pctco2    
        if ( scenario == 'CMIP-1pctco2' and species == 'co2' ) :

            refdate = 10101    # increase starts after 1 January 0001, at 00h00
            currentdate = D['timelist'][itime]
#
#           only modify if date is after 0001-01-01
            if ( refdate <= currentdate ) :

#               assume noleap year                
                days=daysince.daysince(refdate=refdate,enddate=currentdate, calendar='noleap')

                factor= ( 1.01**(float(days)/float(365)) - 1.)

                D['valuelist'][itime,:] = D['valuelist'][itime,:] + globav * factor
#
#       4.2 add the 4xco2 contribution
        elif ( scenario == 'CMIP-abrupt4xco2'   and species == 'co2' ) : D['valuelist'][itime,:] = D['valuelist'][itime,:]  + globav * 3.
#       4.3 add the 2xco2 contribution
        elif ( scenario == 'CMIP-abrupt2xco2'   and species == 'co2' ) : D['valuelist'][itime,:] = D['valuelist'][itime,:]  + globav * 1.
#       4.4 add the 0p5xco2 contribution
        elif ( scenario == 'CMIP-abrupt0p5xco2' and species == 'co2' ) : D['valuelist'][itime,:] = D['valuelist'][itime,:]  - globav * 0.5
#       
        else :
            print('fill1pctco2abrupt4xco2 : Nothing to be done')

    print('--- fill1pctco2abrupt4xco2 ---')
#   
    return D
