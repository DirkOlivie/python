import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')

import readnc
import readattributenc
#import checknan
import year0year1_to_yearlistmonthlist
import getstandardunits
import getconversionfactorunits

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


def readwetcharts_v1_3_1(expid) :
#-----------------------
    '''
    MODIFICATIONS
        (2023-11-21) added species : 'ch4' in RETURN structure  

    ARGUMENTS
        expid : name of experiment (4 digits)
    '''
#
    year0=2001 ; year1=2019

#
    nmonth=12
    nyear=year1-year0+1
    ntime=nmonth*nyear    
#
    expid_as_integer=int(expid)    # 4 digits

# loop over all years
    for iyear in range(nyear) :
        year=year0+iyear

        cyear=str("%4.4i"% (year))
        filename='/datalake/NS2345K/olivie/methane/WETCHARTS1.3.1/WetCHARTs_v1_3_1_'+cyear+'.nc'
#
#       only the first year
        if ( iyear == 0 ) :
            longitude = readnc.readnc('lon',filename)
            latitude  = readnc.readnc('lat',filename)
            timelist_file  = readnc.readnc('time',filename)
            expidlist = readnc.readnc('model',filename) # read modellist
            
            iexpid = list(expidlist).index(expid_as_integer)
 
            nlon = len(longitude)
            nlat = len(latitude)
            ntime_file  = len(timelist_file)
            nexpid  = len(expidlist)

            if ( ntime_file != nmonth ) :
                print('+++ readwetcharts_v1_3_1 +++')
                print('ntime_file, ntime : ', ntime_file, ntime)
                quit()

#           new field : will contain all years and months
            field = np.zeros((nyear*nmonth,nlat,nlon),dtype=float)

#       read the data
        tmp  = readnc.readnc('wetland_CH4_emissions', filename)

#       check for nan
        tmp = np.where(np.isnan(tmp), 0., tmp)

#       fill the annual data
        field[iyear*nmonth:(iyear+1)*nmonth,:,:] = tmp[iexpid,:,:,:]


#       read the units
        units = readattributenc.readattributenc('wetland_CH4_emissions', filename, 'units')
#        if ( units != 'mg m-2 d-1' ) : 
#            print('+++ readwetcharts_v1_3_1 +++')
#            print('Units not recognized : ', units)
#            quit()

#       standard writing of units
        units = getstandardunits.getstandardunits(units=units)

#       units I would like to have
        finalunits='kg m-2 s-1'        
        factor = getconversionfactorunits.getconversionfactorunits(origunits=units, finalunits=finalunits)
#
#        for imonth in range(nmonth) :
#            print(iyear,imonth,np.max(tmp[imodel,imonth,:,:]))

#        for itime in range(ntime) :
#            print(itime, np.max(field[itime,:,:]))


#   apply factor for final units
    field=field*factor    
#
#   check for nan : there are nans (checked on 2026-04-25)
#    field = np.where(np.isnan(field), 0., field)

#   area
    area=areafraction.areafraction(latitude=latitude, longitude=longitude, outputtype='area') # m2

#   make final time series
    yearlist, monthlist = year0year1_to_yearlistmonthlist.year0year1_to_yearlistmonthlist(year0=year0,year1=year1)
    decimalyearlist = np.zeros(ntime, dtype=float)
    for itime in range(ntime) :
        decimalyearlist[itime] = float(yearlist[itime]) + ( float(monthlist[itime])-0.5 ) / float(nmonth)

#   structure
    data = { 'variable'  : 'ch4', \
             'expid'     : expid, \
             'fileorigin': 'wetcharts_v1.3.1', \
             'field'     : field, \
             'units'     : finalunits, \
             'area'      : area, \
             'areaunits' : 'm2', \
             'longitude' : longitude, \
             'latitude'  : latitude, \
             'yearlist'  : yearlist, \
             'monthlist' : monthlist, \
             'timelist'  : decimalyearlist, \
             'freqtype'  : 'monthly', \
             'ntime'     : nyear*nmonth}
#  
#    for itime in range(ntime) :
#        print(itime, np.max(field[itime,:,:]))
#
#    quit()
 
    return data
