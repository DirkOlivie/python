import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits
import getfinalunits
import getlevels
import getstandardunits

def plotmaplog(expid, refid, wlist, var, year0, year1, season, expdata, refdata, figlayout, code):
#-------------
#   title
    title=getidlvar.getidlvar(var=var)

    if ( figlayout.title == '' ) :
        title=title				
    else :
        title=figlayout.title			
  
#   get standard units
    units=getstandardunits.getstandardunits(units=expdata['units'])

#   convert units to more human values
#   units [convert kg[O3]/m2 -> DU[O3]/m2]
#                  mol/mol[O3] -> ppb[O3] 
#                  m s-1 -> mm day-1        : PRECT  
    units, factor = getfinalunits.getfinalunits(var=var, units=units)
#   
    if ( wlist[1] != 0. ) : 
        z = ( expdata['field'] * wlist[0] + refdata['field'] * wlist[1] ) * factor 
    else :
        z =   expdata['field'] * wlist[0]                             * factor
#		      
    fig = plt.figure(figsize=[10,10],dpi=100) # figsize [inches]

    # Setup a global EckertIII map with faint coastlines.
    # ax = fig.add_subplot(1, 1, 1, projection=ccrs.EckertIII()) # EckertIII did not exist
#    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=180))
    ax.set_global()
    ax.set_title(title)
    ax.set_xlabel('Longitude [deg]') # did not happen
    ax.set_ylabel('Latitude [deg]')  # did not happen
    ax.coastlines('110m', alpha=0.5) # 0.1 -> 0.5

    x=expdata['longitude']
    y=expdata['latitude']
#
    # Add colourful filled contours.
#    levels=[1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]*1.e-7
    if ( wlist[1] == 0. ) :
        cmap='RdYlBu_r'
    else :
        cmap='coolwarm'
#        cmap='hsv'
#   cmap='YlGnBu'
    gamma=1 # linear

    print('figlayout.contour_levels_type : ')
    print(figlayout.contour_levels_type)

    if ( figlayout.contour_levels_type == 'imposed' ) : 
#        levels=np.arange(0,50.e-9,5.e-9)
        if ( wlist[1] != 0. ) : spacing='xdiff' 
        else                  : spacing='non-linear'
        levels,gamma=getlevels.getlevels(var=var, units=units, spacing=spacing)

        filled_c = ax.contourf(x, y, z, cmap=cmap, norm=colors.logNorm(vmin=1.e-16, vmax=1.e10), transform=ccrs.PlateCarree())
#       filled_c = ax.contourf(x, y, z, levels, cmap=cmap, norm=colors.PowerNorm(gamma=gamma), transform=ccrs.PlateCarree())
#       filled_c = ax.contourf(x, y, z, levels, cmap=cmap, norm=colors.SymLogNorm(linthresh=0.03,linscale=0.03,vmin=np.amin(levels),vmax=np.amax(levels),base=10), transform=ccrs.PlateCarree())
    elif ( figlayout.contour_levels_type == 'free' ) :
        filled_c = ax.contourf(x, y, z, cmap=cmap, transform=ccrs.PlateCarree())

    if ( wlist[1] ==  0. or 
         wlist[1] == -1. ) :

   # And black line contours.
        line_c = ax.contour(x, y, z, levels=filled_c.levels,
                            colors=['black'],
                            transform=ccrs.PlateCarree())
    #   Comment to make the line contours   visible.
    # Uncomment to make the line contours invisible.
        plt.setp(line_c.collections, visible=False)

    # Add a colorbar for the filled contour.
        fig.colorbar(filled_c, orientation='horizontal', label=getidlunits.getidlunits(units), aspect=40, shrink=0.8)

    # Use the line contours to place contour labels.
        ax.clabel(
            line_c,  # Typically best results when labelling line contours.
            colors=['black'],
            manual=False,  # Automatic placement vs manual placement.
            inline=True,  # Cut the line where the label will be placed.
            fmt=' {:9.1e} '.format,  # Labes as integers, with some extra space.
        )

    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

#    ax.fill([0,20,20,0,0],[0,0,30,30,0])
   
#    plt.text(0,0,'New York')


    # plt.show()
    #plt.show()
    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season

    if ( wlist[1] != 0. ) : expidrefid=expid+'_'+refid
    else                  : expidrefid=expid

#   dir='/projects/NS2345K/www/people/olivie/plots'

    if ( figlayout.plotdir == None ) : dir='/datalake/NS2345K/olivie/plots'
    else                             : dir=figlayout.plotdir

    fig.savefig(dir+'/map_'+var+'_'+expidrefid+'_'+timestamp+figlayout.code+'_'+code+'.png', bbox_inches='tight')
    fig.savefig(dir+'/map_'+var+'_'+expidrefid+'_'+timestamp+figlayout.code+'_'+code+'.ps' , bbox_inches='tight')

    plt.close("all")
