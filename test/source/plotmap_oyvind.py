from netCDF4 import Dataset

import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getfinalunits
import getlevels
import getstandardunits

def main() :
#-----------
# 
#   read the netcdf file
    nc_f='/projects/NS2345K/noresm/cases/N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12/atm/hist/N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12.cam.h0.0120-12.nc'
    nc_fid= Dataset(nc_f, 'r')
    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
    field=np.squeeze(np.array(nc_fid.variables['TREFHT'][:])) # TRFHT
    nc_fid.close

#   title
    title='Geographical distribution'

# 
    units='K'
#		      
    fig = plt.figure(figsize=[10,10],dpi=100) # figsize [inches]

    # Setup a global EckertIII map with faint coastlines.
    # ax = fig.add_subplot(1, 1, 1, projection=ccrs.EckertIII()) # EckertIII did not exist
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))
    ax.set_global()
    ax.set_title(title)
    ax.set_xlabel('Longitude [deg]') # did not happen
    ax.set_ylabel('Latitude [deg]')  # did not happen
    ax.coastlines('110m', alpha=0.5) # 0.1 -> 0.5

    x=lons
    y=lats
    z=field
#    
    cmap='RdYlBu_r'
    cmap='coolwarm'
#   cmap='YlGnBu'
    gamma=1 # linear

    contour_levels_type = 'imposed'
    contour_levels_type = 'free'

    if ( contour_levels_type == 'imposed' ) : 

        levels=np.arange(250,350,5)
        gamma=1

        filled_c = ax.contourf(x, y, z, levels, cmap=cmap, norm=colors.PowerNorm(gamma=gamma), transform=ccrs.PlateCarree())

    elif ( contour_levels_type == 'free' ) :
        filled_c = ax.contourf(x, y, z, cmap=cmap, transform=ccrs.PlateCarree())

   # And black line contours.
    line_c = ax.contour(x, y, z, levels=filled_c.levels,
                        colors=['black'],
                        transform=ccrs.PlateCarree())
    # Uncomment to make the line contours invisible.
    plt.setp(line_c.collections, visible=False)

    # Add a colorbar for the filled contour.
    fig.colorbar(filled_c, orientation='horizontal', label=units, aspect=40, shrink=0.8)

    # Use the line contours to place contour labels.
    ax.clabel(
        line_c,  # Typically best results when labelling line contours.
        colors=['black'],
        manual=False,  # Automatic placement vs manual placement.
        inline=True,  # Cut the line where the label will be placed.
        fmt=' {:9.1e} '.format,  # Labes as integers, with some extra space.
    )

    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

    # plt.show()
    #plt.show()


    fig.savefig('/projects/NS2345K/www/people/olivie/plots/map_oyvind.png', bbox_inches='tight')
    fig.savefig('/projects/NS2345K/www/people/olivie/plots/map_oyvind.ps' , bbox_inches='tight')

    plt.close("all")

    #
if __name__ == '__main__':
    main()
