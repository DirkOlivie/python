import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc

import getorigfilename
import checkfield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc
import readglobalattributenc
import readvariablenamesnc
import daysince


#
def builde90(species, resolution, period, version, overwrite):
#-----------
    '''
    REMARK

    AIM 

    INPUT
        species
        resolution
        period
        version
        overwrite : True | False

    CALLED BY
	    buildoxidantsloop2

    CALLS
	    readnc
 	    daysince
   ''' 
#
    nmonth=12
#
#   I. PERIOD
#------------
#   period -> yearlist
    if ( period == 'histclimo' ) : yearlist=[                    1850,1860,1870,1880,1890,1900, \
                                             1910,1920,1930,1940,1950,1960,1970,1980,1990,2000, \
                                             2010,2020,2023] 
    else : 
        print('+++ builde90 +++')
        print('No period recognized : ', period)
        quit()
#
    nyear = len(yearlist)
#
#   II. READ FROM 
#-----------------
    filename = getorigfilename.getorigfilename(species=species, resolution=resolution)
    print('Reading file : ', filename)


#   fixed fields/variables
    latitude  = readnc.readnc('lat' ,filename)
    longitude = readnc.readnc('lon' ,filename)

#   dimensions
    nlat = len(latitude)
    nlon = len(longitude)

#    if   ( nlat == 96  and nlon == 144 and resolution == '1.9x2.5'  ) : print('ok')    
#    elif ( nlat == 192 and nlon == 288 and resolution == '0.9x1.25' ) : print('ok')
#    else :
#        print('+++ builde90 +++')
#        print('No resolution recognized with nlat and nlon : ', nlat, nlon, resolution)
#        quit()

#   time date
    origdatelist=readnc.readnc('date' ,filename)
    origtimelist=readnc.readnc('time' ,filename)

    origntime = len(origtimelist)

    if ( origntime % nmonth != 0 ) :
        print('+++ builde90 +++')
        print('#time is not a multiple of 12')
        quit()

    origdaymonthlist =   origdatelist % 10000

    origdaylist = origdatelist % 100

    print('origdaylist : ', origdaylist)

    if ( min(origdaylist) != max(origdaylist) ) :
        print('+++ builde90 +++')
        print('Not all days are equal in original dataset : ', origdaylist)
        quit()



#   III. TIME
#------------

    nyear = len(yearlist)
    year0 = yearlist[0]       # first element
    year1 = yearlist[-1]      # last element 
  
    date    = np.zeros(nyear*nmonth,dtype=int)  # integer  

    for iyear in range(0,nyear) :
        year=yearlist[iyear]
        date[   iyear*nmonth:(iyear+1)*nmonth] = origdaymonthlist[0:nmonth] + 10000 * year

    ntime = nyear * nmonth
#
    print('datelist : ', date)

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
    fshort='emissions-cmip6_'+species+'_other_surface_'+period+'_'+cperiod+'_'+resolution+'_c20170322_'+version+'.nc'

##############
#   New file #
##############

#   create new directory
    outdir='/scratch/olivie/code/python/cmip7-e90-cesm-to-noresm/data/output/'+version+'/'+period+'/'+resolution
    if  not os.path.isdir(outdir) : os.makedirs(outdir)

#   create new NetCDF file
    fn = outdir+'/'+fshort
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
    londimid = ds.createDimension('lon', nlon)
    latdimid = ds.createDimension('lat', nlat)

#   time
    timedimid = ds.createDimension('time', None)

######################
#   Define variables #
######################
# 
#   horizontal
    latid  = ds.createVariable('lat' , 'f4', ('lat',))
    lonid  = ds.createVariable('lon' , 'f4', ('lon',))

#   time
    timeid = ds.createVariable('time', 'f4', ('time',))
    dateid = ds.createVariable('date'   , 'i4', ('time',))
#
#   name of emissions will be name of sector
    sectorlist=readvariablenamesnc.readvariablenamesnc(filename=filename,ndim=3) # all 3-dimesional fields (time, latitude, longitude)
    nsector = len(sectorlist)

    sectoridlist=[]
    for sector in sectorlist :
        sectoridlist.append(ds.createVariable(sector,'f4', ('time', 'lat', 'lon',), fill_value=1.e+20))
# 
################
#   ATTRIBUTES #
################
#   latitude
    latid.long_name     = readattributenc.readattributenc('lat',filename,'long_name')
    latid.units         = readattributenc.readattributenc('lat',filename,'units')

#   longitude
    lonid.long_name     = readattributenc.readattributenc('lon',filename,'long_name')
    lonid.units         = readattributenc.readattributenc('lon',filename,'units')

#   sector   
    for isector in range(0,nsector) :         
        
        sectoridlist[isector].units            = readattributenc.readattributenc(sectorlist[isector], filename, 'units') # take units from first contributing component
        sectoridlist[isector].long_name        = readattributenc.readattributenc(sectorlist[isector], filename, 'long_name')
        sectoridlist[isector].molecular_weight = readattributenc.readattributenc(sectorlist[isector], filename, 'molecular_weight')
        
#   time 
    calendar   = readattributenc.readattributenc('time',filename,'calendar')
    time_units = readattributenc.readattributenc('time',filename,'units')

    if ( time_units == "days since 1750-01-01 00:00:00" ) : refdate=17500101
    else : 
        print('+++ builde90 +++')
        print('No time_units recognized : ', time_units)
        quit()

    timeid.units= time_units
    timeid.calendar = calendar

#   date
    dateid.units = readattributenc.readattributenc('date',filename,'units')
    dateid.long_name  = readattributenc.readattributenc('date',filename,'long_name')


##################
#   WRITE FIELDS #
##################
#
#   FIXED FIELDS / VARIABLES
    latid[0:nlat] = latitude[ 0:nlat]
    lonid[0:nlon] = longitude[0:nlon]
#
#   
    print('yearlist      : ', yearlist)
    
    nmonth=12

#   loop over all sectors
    for isector in range(0,nsector) :

        print('sector : ', sectorlist[isector])

#       retries the whole timeseries
        F = readnc.readnc(sectorlist[isector], filename)

#       check that all years are equal in original data
        checkfield.checkfield(field=F)

#       loop over all years
        for iyear in range(0,nyear) :
                
            print('iyear : ', iyear)            

#           always put fist year of original data set (all years are equal)
            sectoridlist[isector][iyear*nmonth:(iyear+1)*nmonth,0:nlat,0:nlon] = F[0:nmonth,0:nlat,0:nlon]

#
#   loop over all dates
    print('calculating dates : ', ntime)
    for itime in range(0,ntime) :
        print('date : ', date[itime])
        dateid[itime] = date[itime]
        timeid[itime] = daysince.daysince(refdate=refdate,enddate=date[itime], calendar=calendar)

#
#   global attributes
    ds.data_title = readglobalattributenc.readglobalattributenc(filename,'data_title')
    ds.molecular_weight = readglobalattributenc.readglobalattributenc(filename,'molecular_weight')
    ds.data_creator = readglobalattributenc.readglobalattributenc(filename,'data_creator')
    ds.data_summary = readglobalattributenc.readglobalattributenc(filename,'data_summary')
    ds.cesm_contact = readglobalattributenc.readglobalattributenc(filename,'cesm_contact')
    ds.creation_date = readglobalattributenc.readglobalattributenc(filename,'creation_date')
    ds.update_date = readglobalattributenc.readglobalattributenc(filename,'update_date')
    if ( species != 'E90' ) : ds.history = readglobalattributenc.readglobalattributenc(filename,'history')
    ds.data_script = readglobalattributenc.readglobalattributenc(filename,'data_script')
    if ( species != 'E90' ) : ds.data_source_url = readglobalattributenc.readglobalattributenc(filename,'data_source_url')
    if ( species != 'E90' ) : ds.data_reference = readglobalattributenc.readglobalattributenc(filename,'data_reference')
#   
    ds.close()

