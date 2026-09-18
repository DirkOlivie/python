from netCDF4 import Dataset
import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import gridmanipulation
import intplon
import intplat


def interpolatemodelperiod(data):
#------------------------------  
    '''
    AIM
        interpolate (model) data to observational grid

    INPUT 
        data structure containing
            var     
            field    
            mask    
            longitude 
            latitude 
            yearlist 
            monthlist
            timelist
            ntime

    RETURN
        data structure containing (same as input structure)
            ...
            mask : is everywhere put to 1 (even after interpolation is model data defined everywhere)
            ...

    CALLED BY
        readobsmodelperiod
               
    CALLS
        lon2lonbnds
        lat2latbnds
        readnc
        readobsmonth
        readmodelmonth
    '''
#---------------------------------------------------------
#   use shortname
    D=data

#   original grid
    lonbnds0=gridmanipulation.lon2lonbnds(longitude=D['longitude'])
    latbnds0=gridmanipulation.lat2latbnds(latitude=D['latitude'])
    nlon0=len(D['longitude'])
    nlat0=len(D['latitude'])

#   read final grid from observation file (1995) 
    if ( data['var'] == 'toc' ) : 
        nc_f='/projects/NS9560K/users/olivie/observations/toccopernicus/v20240209/197901-C3S-L4_OZONE-O3_PRODUCTS-MSR-ASSIM-ALG-MONTHLY-v0023.nc'
        clat='latitude'
        clon='longitude'
    elif ( data['var'] == 'od550aer' ) :
        nc_f='/projects/NS9560K/users/olivie/observations/aodmerged-fmi/FMI_SAT_AOD-MERGED-L3_Ver1.0_Column_od550aer_1995_monthly.nc'
        clat='lat'
        clon='lon'
    else :
        print('No variable recognized : ', data['var'])
        quit()
    nc_fid= Dataset(nc_f, 'r') # open NetCDF file
    latitude1=np.array(nc_fid.variables[clat][:])  # latitudes
    longitude1=np.array(nc_fid.variables[clon][:])  # longitudes
    nc_fid.close # close NetCDF file

    lonbnds1=gridmanipulation.lon2lonbnds(longitude=longitude1)
    latbnds1=gridmanipulation.lat2latbnds(latitude=latitude1)
    nlon1=len(longitude1)
    nlat1=len(latitude1)

#   interpolate 
    print('preparing ptlon, wtlon')
    ptlon, wtlon = intplon.intplon(loninbd=lonbnds0, lonoutbd=lonbnds1)
    print('preparing ptlat, wtlat')
    ptlat, wtlat = intplat.intplat(latinbd=latbnds0, latoutbd=latbnds1)

#
#   1) interpolation along latitude
    a=np.zeros((D['ntime'],nlat1,nlon0), dtype=float)
    for ilat1 in range(0,nlat1) :
        nlat=ptlat[ilat1,0]                  # first value gives number of latitudes that contribute
        for ilat in range(1,nlat+1) :
            ilat0=ptlat[ilat1,ilat]
            wlat=wtlat[ilat1,ilat]
            a[:,ilat1,:]=a[:,ilat1,:]+D['field'][:,ilat0,:]*wlat

#   2) interpolation along longitude
    outfield=np.zeros((D['ntime'],nlat1,nlon1), dtype=float)
    for ilon1 in range(0,nlon1) :
        nlon=ptlon[ilon1,0]                 # first value gives number of longitudes that contribute
        for ilon in range(1,nlon+1) : 
            ilon0=ptlon[ilon1,ilon]
            wlon=wtlon[ilon1,ilon]
            outfield[:,:,ilon1]=outfield[:,:,ilon1]+a[:,:,ilon0]*wlon

#
    mask=outfield[:,:,:] * 0. + 1.

    outdata = {'var'             : D['var'], \
               'field'           : outfield, \
               'units'           : D['units'], \
               'mask'            : mask, \
               'longitude'       : longitude1, \
               'latitude'        : latitude1, \
               'yearlist'        : D['yearlist'], \
               'monthlist'       : D['monthlist'], \
               'timelist'        : D['timelist'], \
               'ntime'           : D['ntime']}
#
    return outdata
