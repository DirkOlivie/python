import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import datetime
import glob

import experimentdefinition

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname


'''
REMARK
        tempeatures [K] -> converted to [] : NOT ANYMORE
        conversion : molecules cm-3 -> mol mol-1

MODIFCICATION 
        (2022-07-11) : no conversion of temperature from [K] to [C]
        (2023-10-20) : introduced possibility for basic experimentname
'''


def readsingleh1field( expid, var, date):
#####################
    print('+++ readsingleh1field +++')
    print('date : '+date)
    print('var  : '+var)
    print('--- readsingleh1field ---')
##
#   extract date from year
    line=date.split('-')    # split yyyy-mm
    year=int(line[0])       # convert string (yyyy) into integer
    month=int(line[1])
    day=int(line[2])

#   get basice expid
    basicexpid=getbasicexpidname.getbasicexpidname(expid=expid, date=line[0]+'-'+line[1]) # date : yyyy-mm
    
#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=basicexpid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid'] # experiment you read (can be different from experiment you write)
    model=expidinfo['model']

#   h1 filename list
    filelist=glob.glob(subdir+'/'+cexpid+'/atm/hist/'+cexpid+'*h1*00000.nc')
    filelist.sort()

#   read from first file
    nc_f=filelist[0]
##    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')
    
    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes

#        field=np.squeeze(np.array(nc_fid.variables[var][:]))
 
    units=nc_fid.variables[var].units
    nlat=len(lats)
    nlon=len(lons)
# 
    nc_fid.close
#
#   loop over all files
    found=False 

    ifile=0
    while ( not found) : 

#        print(filelist[ifile])

        nc_fid= Dataset(filelist[ifile], 'r') 

        time=nc_fid.variables['time'][:]  
        time_bnds=nc_fid.variables['time_bnds'][:]
        time_units=nc_fid.variables['time'].units
        time_calendar=nc_fid.variables['time'].calendar

        numt0=nc.date2num(datetime.datetime(year,month,day), time_units, calendar=time_calendar)  # beginpoint 
        numt1=numt0+1 

#        print('numt0 = ',numt0)
#        print('numt1 = ',numt1)



        ntime=len(time)

        for itime in range(0,ntime) :

            numx0=time_bnds[itime,0]
            numx1=time_bnds[itime,1]

#            print('numt0 = ',numt0)
#            print('numt1 = ',numt1)

#            print('numx0 = ',numx0)
#            print('numx1 = ',numx1)

            if ( numt0 == numx0 and numt1 == numx1 ) :

               print(filelist[ifile])  

               field=np.squeeze(np.array(nc_fid.variables[var][:]))    # extract correct variable
               field=field[itime,:,:]                                 # extract correct time

               found=True

        nc_fid.close

        ifile=ifile+1
#
#   data            
    data = { 'field'     : field, \
             'longitude' : lons, \
             'latitude'  : lats, \
             'nlon'      : nlon, \
             'nlat'      : nlat, \
             'units'     : units}  
#   
    print('--- readsingleh1field ---')
# 
    return data    
