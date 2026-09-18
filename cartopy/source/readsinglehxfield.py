import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import datetime
import glob
import time

import experimentdefinition

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname


def readsinglehxfield( expid, var, date, hx, dhx):
#--------------------
    '''
    INPUT
        expid
        var
        date : yyyy-mm-dd-hh:mm:ss
        hx : 'h1', 'h2', ...
        dhx : -000000, -10800, ...

    CALLS
        getbasixexpidname
        getexpidinfo

    REMARK

'''
    print('+++ readsinglehxfield +++')
    print('date : '+date)
    print('var  : '+var)
##
#   extract year/month/day/hour/minute/second from date
    line=date.split('-')    # split yyyy-mm-dd-hh:mm:ss
    year  = int(line[0])    # convert string (yyyy) into integer
    month = int(line[1])     
    day   = int(line[2])

    timeline=line[3].split(':')
    hour   = int(timeline[0])  # hour
    minute = int(timeline[1])  # minute
    second = int(timeline[2])  # second

#   
#   get basice expid
    if ( month == 1 and day == 1 and hour == 0) :
        testdate=str("%4.4i"% (year-1))+'-12'
    else :
        testdate=line[0]+'-'+line[1]

    basicexpid=getbasicexpidname.getbasicexpidname(expid=expid, date=testdate) # date : yyyy-mm
    
#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=basicexpid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid'] # experiment you read (can be different from experiment you write)
    model=expidinfo['model']

#   h1 filename list
    dt    = datetime.datetime(year,month,day,hour)
    dtnum = nc.date2num(dt,'days since 2000-01-01 00:00:00',calendar='gregorian')
    dtnum = dtnum-3./24.  # remove 3 hours
    dt    = nc.num2date(dtnum,'days since 2000-01-01 00:00:00',calendar='gregorian')

    testyear  = str("%4.4i"% (dt.year))
    testmonth = str("%2.2i"% (dt.month))
    testday   = str("%2.2i"% (dt.day))
    testdate  = testyear+'-'+testmonth+'-'+testday
     
    filelist=glob.glob(subdir+'/'+cexpid+'/atm/hist/'+cexpid+'*'+hx+'*'+testdate+'*'+dhx+'.nc')
    filelist.sort()

#   read from first file
    nc_f=filelist[0]
##    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')
    
    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
#
    units=nc_fid.variables[var].units
    nlat=len(lats)
    nlon=len(lons)
#
    hyam=np.array(nc_fid.variables['hyam'][:]) # hyam
    hybm=np.array(nc_fid.variables['hybm'][:]) # hybm
    hyai=np.array(nc_fid.variables['hyai'][:]) # hyam
    hybi=np.array(nc_fid.variables['hybi'][:]) # hybm
#
    nlev = len(hyam)
# 
    nc_fid.close
#
#   loop over all files
    found=False 

    ifile=0
    while ( not found) : 

        print('Searching : ', ifile, filelist[ifile])
        nc_fid= Dataset(filelist[ifile], 'r') # loop over all file via ifile

        time          = nc_fid.variables['time'][:]  
        time_bnds     = nc_fid.variables['time_bnds'][:]
        time_units    = nc_fid.variables['time'].units
        time_calendar = nc_fid.variables['time'].calendar

#       the time you are looking fore
        numt=nc.date2num(datetime.datetime(year,month,day,hour), time_units, calendar=time_calendar)  # beginpoint 
#        numt0=nc.date2num(datetime.datetime(year,month,day,hour), time_units, calendar=time_calendar)  # beginpoint 
#        numt1=numt0+1 

        ntime=len(time)

        for itime in range(0,ntime) :

 #           numx0=time_bnds[itime,0]
 #           numx1=time_bnds[itime,1]
            numx=time[itime]

#            print('numt0 = ',numt0)
#            print('numt1 = ',numt1)

#            print('numx0 = ',numx0)
#            print('numx1 = ',numx1)

#           if ( numt0 == numx0 and numt1 == numx1 ) :
            if ( numt == numx ) :

                print(filelist[ifile])  

                field=np.squeeze(np.array(nc_fid.variables[var][:]))    # extract correct variable
                ndim = field.ndim

                if ( ndim == 4 ) :
                    ps=np.squeeze(np.array(nc_fid.variables['PS'][:]))
                    p0=np.array(nc_fid.variables['P0'][:]) # reference pressure 
                    units_p0=nc_fid.variables['P0'].units
                    units_ps=nc_fid.variables['PS'].units


                if ( ndim == 3 ) : 
                    field=field[itime,:,:]                                 # extract correct time
                elif ( ndim == 4 ) : 
                    field=field[itime,:,:,:]
                    ps=ps[itime,:,:]
                else :
                    print('+++ readsinglehxfield +++')
                    print('No dimension recognized')
                    quit()

                found=True

        nc_fid.close

        ifile=ifile+1 # go to next file
#
#   data        
    ndim=field.ndim
    
    data = { 'field'     : field, \
             'longitude' : lons, \
             'latitude'  : lats, \
             'nlon'      : nlon, \
             'nlat'      : nlat, \
             'units'     : units}  
    if ( ndim == 3) :
        data.update({
             'p0'        : p0, \
             'ps'        : ps, \
             'hyai'      : hyai, \
             'hybi'      : hybi, \
             'hyam'      : hyam, \
             'hybm'      : hybm, \
             'units_ps'  : units_ps, \
             'units_p0'  : units_p0, \
             'nlev'      : nlev})
#  
    print(var)
    print(field.ndim) 
    print(field.shape)
    print('--- readsinglehxfield ---')
# 
    return data    
