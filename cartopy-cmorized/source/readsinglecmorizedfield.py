import glob
import numpy as np
from netCDF4 import Dataset

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getrawdirectory
import getperiodlist
import getrealm



'''
REMARK
        tempeatures [K] -> converted to [] : NOT ANYMORE
        conversion : molecules cm-3 -> mol mol-1

MODIFCICATION 
        (2022-07-11) : no conversion of temperature from [K] to [C]
        (2023-10-20) : introduced possibility for basic experimentname
'''


def readsinglecmorizedfield( expid, var, date):
###########################
#
    print('+++ readsinglecmorizedfield +++')
    print('date : '+date)
    print('var  : '+var)
    print('--- readsinglecmorizedfield ---')
#
#   split    
    line=date.split('-')
    year=int(line[0])
    month=int(line[1])

#   obtain the project
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    project=expidinfo['project']

#   directory
    directory=getrawdirectory.getrawdirectory(expid=expid,var=var,project=project,freqfile='monthly')
    realm=getrealm.getrealm(var=var,freqfile='monthly')

# list of all files   
    filelist=glob.glob(directory+'/'+var+'_'+realm+'_*[0-9].nc')
    filelist.sort()

# list of all periods
    nmonth=12

    periodlist=getperiodlist.getperiodlist(expid, var, project, freqfile='monthly')
    for iperiod in range(0,periodlist['nperiod']) :
        print(iperiod,periodlist['year0list'][iperiod])

        if ( periodlist['year0list'][iperiod] <= year 
        and  periodlist['year1list'][iperiod] >= year ) : 
            iperiodfound=iperiod                                           # period
            itime = ( year - periodlist['year0list'][iperiod] ) * nmonth + month-1          

    period=periodlist['periodlist'][iperiodfound]

#   read netcdfi file
    filelist=glob.glob(directory+'/'+var+'_'+realm+'_*'+period+'.nc')
    nc_f=filelist[0]

    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')
    
    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
    print('... before ...')
    field=np.squeeze(np.array(nc_fid.variables[var][:]))
    print('... after ...')
    units=nc_fid.variables[var].units
    ndim=field.ndim
    nlat=len(lats)
    nlon=len(lons)

    if ( ndim==4 ) :
        
        levs=np.array(nc_fid.variables['lat'][:]) # levels 
        nlev=len(levs)

    nc_fid.close
#
#   select correct month
    if   ( ndim == 3 ) : field = field[itime,:,:]
    elif ( ndim == 4) : field = field[itime,:,:,:]
    else :
        print('No ndim recognized : '+ndim)
        quit()

#   read also phalf and pfull    
    if ( ndim==4 and ( var != 'phalf' and var != 'pfull' ) ) : 
                       
        pfull=readsinglecmorizedfield( expid=expid, var='pfull', date=date)
        phalf=readsinglecmorizedfield( expid=expid, var='phalf', date=date)
  
#   data            
    data = { 'field'     : field, \
             'longitude' : lons, \
             'latitude'  : lats, \
             'nlon'      : nlon, \
             'nlat'      : nlat, \
             'units'     : units}  
#   in case of 4d data
    if( ndim == 4 ) : 
        data.update({'nlev'      : nlev})

#   in case of 4d data (not 'phalf', not 'pfull')    
    if ( ndim == 4 and ( var != 'phalf'and var != 'pfull' )) :
        data.update({   
             'pfull'     : pfull['field'], \
             'phalf'     : phalf['field'], \
             'units_pfull' : pfull['units'],\
             'units_phalf' : phalf['units']})
#   
    print('--- readsinglecmorizedfield ---')
# 
    return data    
