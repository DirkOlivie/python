import numpy as np
import math
from netCDF4 import Dataset

import experimentdefinition
import oceanareafraction

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import getstandardunitname

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname


def readsingleglobalmeanoceanprofile(expid, var, date, region=None, xlon=None, xlat=None, verticalaxis='pressure'):
#-----------------------------------
#
    '''
    REMARK

    MODIFICATIONS

    CALLS

    '''
#
    print('+++ readsingleglobalmeanoceanprofile +++')
    print('date : '+date)
#
#   find basic expid : such that period corresponds
    basicexpid=getbasicexpidname.getbasicexpidname(expid=expid,date=date)

#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=basicexpid)
    subdir=expidinfo['subdir']
    cexpid=expidinfo['cexpid'] # experiment you read (can be different from experiment you write)

    camversion='cam'

#   ocean model
    if ( cexpid == 'N1850_f19_tn14_20190621' \
      or cexpid == 'N1850_f19_tn14_20190722' \
      or cexpid == 'N1850_f19_tn14_20190802' ) : 
        oceanmodel='micom'
    else :
        oceanmodel='blom'


#   reading some grid information
    nc_f='/datalake/NS2345K/olivie/inputdata/ocn/blom/grid/grid_tnx1v4_20170622.nc'
    nc_fid= Dataset(nc_f, 'r')
    parea=np.nan_to_num(np.array(nc_fid.variables['parea'][:]))  # area [m2]
    pmask=np.nan_to_num(np.array(nc_fid.variables['pmask'][:]))  # mask [0 or 1]
    plat=np.array(nc_fid.variables['plat'][:])  # latitudes
    plon=np.array(nc_fid.variables['plon'][:])  # longitudes
    nc_fid.close

    np.place(parea, parea > 1.e20, [0.]) 

    parea[:,-1]=0. # because nreg = 2

#   weighting dependent on region
    w=oceanareafraction.oceanareafraction(plat=plat,plon=plon,parea=parea,outputtype='weight',region=region)



#   reading data from file
    print('subdir : ', subdir)
    nc_f=subdir+'/'+cexpid+'/ocn/hist/'+cexpid+'.'+oceanmodel+'.hm.'+date+'.nc'
    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')

# read field + units
    field=np.squeeze(np.nan_to_num(np.array(nc_fid.variables[var][:]))) # removes dimensions with size = 1 
    units=nc_fid.variables[var].units
    fillvalue=nc_fid.variables[var]._FillValue
    np.place(field,field > 1.e20, [0.]) # put fill values on 0.

# standardize unit name
    units=getstandardunitname.getstandardunitname(units)

#   read 1-dimesional depth information
    depth=np.array(nc_fid.variables['depth'][:]) # depth
    depth_bnds=np.array(nc_fid.variables['depth_bnds'][:]) # depth_bnds
    units_depth=nc_fid.variables['depth'].units

#   read dzlvl information
    dz=np.squeeze(np.nan_to_num(np.array(nc_fid.variables['dzlvl'][:]))) # use this as weighting factor
    np.place(dz,dz > 1.e20, [0.])

    nc_fid.close  # close netcdf file

#   dimensions
    nlev, nlat, nlon = field.shape

#   zbnds
    zbndlist=np.zeros((nlev+1))
    zbndlist[0:nlev]=depth_bnds[0:nlev,0]
    zbndlist[nlev]=depth_bnds[nlev-1,1]

#   calculate profile
    valuelist  = np.zeros((nlev), dtype=float)
    weightlist = np.zeros((nlev), dtype=float)

    for ilev in range(nlev) :
        valuelist[ilev]  = np.sum(field[ilev,:,:]*dz[ilev,:,:]*parea*pmask*w)
        weightlist[ilev] = np.sum(                dz[ilev,:,:]*parea*pmask*w)
#
#   
    valuelist=valuelist/weightlist
#
#
# structure
    data = { 'expid'     : expid, \
             'var'       : var, \
             'region'    : region, \
             'xlon'      : xlon, \
             'xlat'      : xlat, \
             'valuelist' : valuelist, \
             'units'     : units, \
             'zlist'     : depth, \
             'zbndlist'  : zbndlist, \
             'zunits'    : units_depth, \
             'verticalaxis' : verticalaxis}  
#
    print('--- readsingleglobalmeanprofile ---')
#    
    return data

