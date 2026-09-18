"""
Contour labels
--------------

An example of adding contour labels to matplotlib contours.

"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from netCDF4 import Dataset
import numpy as np

#from cartopy.examples.waves import sample_data


def main():

    cexpid='FC2010climo_f19_20210204_test1'
    var='cb_O3'
    var='O3_SRF'
    var='NO2_SRF'
    var='TREFHT'
    year=7
    month=10

#   cexpid='NHIST_f19_tn14_20190710'
#   var='ozone'
#   year=2000
#   month=6

    camversion='cam'

# read different fields : temperature, pressure, ozone, hyai, hybi
    yyyy = str("%4.4i"% (year))
    mm = str("%2.2i"% (month))
    nc_f='/projects/NS2345K/noresm/olivie/vsls/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.h0.'+yyyy+'-'+mm+'.nc'
#   nc_f='/projects/NS9560K/noresm/cases/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.h0.'+yyyy+'-'+mm+'.nc'

    nc_fid= Dataset(nc_f, 'r')

    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
    field=np.squeeze(np.array(nc_fid.variables[var][:]))

    fig = plt.figure(figsize=[10,10],dpi=100) # figsize [inches]

    # Setup a global EckertIII map with faint coastlines.
    # ax = fig.add_subplot(1, 1, 1, projection=ccrs.EckertIII()) # EckertIII did not exist
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=-90))
    ax.set_global()
    ax.set_title('Overview map')
    ax.set_xlabel('Longitude [deg]') # did not happen
    ax.set_ylabel('Latitude [deg]')  # did not happen
    ax.coastlines('110m', alpha=0.5) # 0.1 -> 0.5

    # Use the waves example to provide some sample data, but make it
    # more dependent on y for more interesting contours.
    #x, y, z = sample_data((20, 40))
    #z = z * -1.5 * y

    x=lons
    y=lats
    z=field

    # Add colourful filled contours.
    filled_c = ax.contourf(x, y, z, transform=ccrs.PlateCarree())

    # And black line contours.
    line_c = ax.contour(x, y, z, levels=filled_c.levels,
                        colors=['black'],
                        transform=ccrs.PlateCarree())

    # Uncomment to make the line contours invisible.
    # plt.setp(line_c.collections, visible=False)

    # Add a colorbar for the filled contour.
    fig.colorbar(filled_c, orientation='horizontal', label='Whatever Units ...', aspect=40, shrink=0.8)

    # Use the line contours to place contour labels.
    ax.clabel(
        line_c,  # Typically best results when labelling line contours.
        colors=['black'],
        manual=False,  # Automatic placement vs manual placement.
        inline=True,  # Cut the line where the label will be placed.
        fmt=' {:.0f} '.format,  # Labes as integers, with some extra space.
    )

    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

    # plt.show()
    fig.savefig('/projects/NS2345K/www/people/olivie/plots/cartopy.png')

if __name__ == '__main__':
    main()
