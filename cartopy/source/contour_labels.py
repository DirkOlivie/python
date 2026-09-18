"""
Contour labels
--------------

An example of adding contour labels to matplotlib contours.

"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from cartopy.examples.waves import sample_data


def main():
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
    x, y, z = sample_data((20, 40))
    z = z * -1.5 * y

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
