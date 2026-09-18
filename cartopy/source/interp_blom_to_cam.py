import numpy as np
from netCDF4 import Dataset

def interp_blom_to_cam ( blomdata, grid ) :
#---------------------
    '''
    INPUT
        blomfield
        grid      : desired CAM grid



    '''
#   I.a information on CAM grid : longitudes and latitudes
    if   ( grid == 'f09' ) : nc_f='/projects/NS9560K/noresm/cases/NSSP245frc2_03_f09_tn14_20200630/atm/hist/NSSP245frc2_03_f09_tn14_20200630.cam.h0.2019-12.nc'
    elif ( grid == 'f19' ) : nc_f='/datalake/NS9560K/noresm/cases/N1850_f19_tn14_20231204_test04/atm/hist/N1850_f19_tn14_20231204_test04.cam.h0.1699-12.nc'
    else                   : 
        print('No grid recognized : '+grid)
        quit()  
 #                              
    nc_fid= Dataset(nc_f, 'r') # only reading
    lat=np.array(nc_fid.variables['lat'][:])  # latitudes
    lon=np.array(nc_fid.variables['lon'][:])  # longitudes
    nc_fid.close

    nlat=len(lat)
    nlon=len(lon)

#   I.b information on BLOM grid
    gridversion='tnx1v4' # NorESM2
#   gridversion='gx1v6'  # NorESM1  
    nc_f='/projects/NS2345K/diagnostics/noresm/packages/BLOM_DIAG/grid_files/'+gridversion+'/grid.nc'
#
    nc_fid= Dataset(nc_f, 'r') # only reading
    parea=np.nan_to_num(np.array(nc_fid.variables['parea'][:]))  # area
    pmask=np.nan_to_num(np.array(nc_fid.variables['pmask'][:]))  # mask
    plat=np.array(nc_fid.variables['plat'][:])  # latitudes
    plon=np.array(nc_fid.variables['plon'][:])  # longitudes
    nc_fid.close

#   I.c file with interpolate weights
    if   ( grid == 'f09' ) : nc_f='/scratch/olivie/noresm-inputdata/cpl/cpl6/map_'+gridversion+'_to_fv0.9x1.25_aave_da_170609.nc'
    elif ( grid == 'f19' ) : nc_f='/scratch/olivie/noresm-inputdata/cpl/cpl6/map_'+gridversion+'_to_fv1.9x2.5_aave_da_170609.nc'
    else                   : 
        print('No grid recognized : '+grid)
        quit()

    nc_fid= Dataset(nc_f, 'r') # only reading 
#   source grid "a" : micom grid
    xc_a=np.array(nc_fid.variables['xc_a'][:])
    yc_a=np.array(nc_fid.variables['yc_a'][:])
#   destination grid "b" : cam grid
    xc_b=np.array(nc_fid.variables['xc_b'][:])
    yc_b=np.array(nc_fid.variables['yc_b'][:])
#   weights
    col=np.array(nc_fid.variables['col'][:])
    row=np.array(nc_fid.variables['row'][:])
    s=np.array(nc_fid.variables['S'][:])
#   frac_b
    frac_b=np.array(nc_fid.variables['frac_b'][:]) # fraction of CAM grid point covered by ocean grid points
    nc_fid.close

    nw=len(s)


#   II. do interpolation
    camfield      = np.zeros( (nlat,nlon) )
    weight        = np.zeros( (nlat,nlon) )
    weight_frac_b = np.zeros( (nlat,nlon) )


    for iw in range(nw) : 
#       1-d grid
        i_a=col[iw]
        i_b=row[iw]
#       source (micom)
        ilon0 = (i_a-1) %  360   # don't forget -1
        ilat0 = (i_a-1) // 360   #
#       destination (cam)
        ilon1 = (i_b-1) %  nlon  # don't forget -1
        ilat1 = (i_b-1) // nlon
#
#       print(ilon0, ilat0, ilon1, ilat1, s[iw])

#       accumulate
        camfield[ilat1,ilon1] = camfield[ilat1,ilon1] + blomdata['field'][ilat0,ilon0] * s[iw]
        weight[  ilat1,ilon1] = weight[  ilat1,ilon1] +                                  s[iw]
#
#       print, i_b, size(frac_b)
        weight_frac_b[ilat1,ilon1]     = frac_b[i_b-1]
#  
#   III. return structure
    newdata={ 'field'     : camfield, \
              'longitude' : lon, \
              'latitude'  : lat, \
              'units'     : blomdata['units'] } 
#
    return newdata
