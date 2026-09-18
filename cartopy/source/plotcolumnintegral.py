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

def plotcolumnintegral(expid, var, year0, year1, season, data, figlayout):

#   title
    title=getidlvar.getidlvar(var=var)

    if ( figlayout.title == '' ) :
        title=title				
    else :
        title=figlayout.title			
  
#   get standard units
    units=getstandardunits.getstandardunits(units=data['units'])

#   units [convert kg[O3]/m2 -> DU[O3]/m2]
    units, factor = getfinalunits.getfinalunits(var='column_'+var, units=units)
    z = data['z']*factor 
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

    x=data['lons']
    y=data['lats']
#
    # Add colourful filled contours.
    cmap='RdYlBu_r'
#   cmap='YlGnBu'
    gamma=1 # linear
    if ( figlayout.contour_levels_type == 'imposed' ) : 
        levels,gamma=getlevels.getlevels(var='column_'+var, units=units, spacing='non-linear')
        filled_c = ax.contourf(x, y, z, levels, cmap=cmap, norm=colors.PowerNorm(gamma=gamma), transform=ccrs.PlateCarree())
    elif ( figlayout.contour_levels_type == 'free' ) :
        filled_c = ax.contourf(x, y, z, cmap=cmap, transform=ccrs.PlateCarree())

    # And black line contours.
    line_c = ax.contour(x, y, z, levels=filled_c.levels,
                        colors=['black'],
                        transform=ccrs.PlateCarree())

    # Uncomment to make the line contours invisible.
    # plt.setp(line_c.collections, visible=False)

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
    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season

    fig.savefig('/projects/NS2345K/www/people/olivie/plots/columnintegral_'+var+'_'+expid+'_'+timestamp+figlayout.code+'.png', bbox_inches='tight')
    fig.savefig('/projects/NS2345K/www/people/olivie/plots/columnintegral_'+var+'_'+expid+'_'+timestamp+figlayout.code+'.ps' , bbox_inches='tight')

    plt.close("all")
