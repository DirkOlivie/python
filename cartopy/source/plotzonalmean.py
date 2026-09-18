import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
import matplotlib.colors as colors

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getfinalunits
import getlevels
import getstandardunits

def plotzonalmean(expid, refid, wlist, var, year0, year1, season, expdata, refdata, figlayout, code):
#----------------
    '''
    MODIFICATIONS
        (2025-10-26) adding use of y_units to distinguish between pressure and height coordinates

    '''
# title
    title=getidlvar.getidlvar(var=var)

    if ( figlayout.title == '' ) :
        title=title
    else :
        title=figlayout.title

#  units
    units=getstandardunits.getstandardunits(units=expdata['units'])

#   convert units to more human values
#   units [convert kg[O3]/m2 -> DU[O3]/m2]
#                  mol/mol[O3] -> ppb[O3]  
    units, factor = getfinalunits.getfinalunits(var=var, units=units)
#   
    if ( wlist[1] != 0. ) :
        z = ( expdata['z'] * wlist[0] + refdata['z'] * wlist[1] ) * factor
    else :
        z =   expdata['z'] * wlist[0] * factor

    fig =  plt.figure(figsize=[10,10],dpi=100)

#   pressure vertical coorinate logarithmic
    if ( expdata['y_units'] == 'Pa' ) :
        ax = fig.add_subplot(1, 1, 1, ylim=(100000,100),yscale='log')
        ax.set_ylabel('Pressure [Pa]')
    elif (expdata['y_units'] == 'km' ) :
        ax = fig.add_subplot(1, 1, 1, ylim=(0,40))
        ax.set_ylabel('Height [km]')
    elif (expdata['y_units'] == 'm' ) :
        ax = fig.add_subplot(1, 1, 1, ylim=(0,40000))
        ax.set_ylabel('Height [m]')
    else :
        print('+++ plotzonalmean +++')
        print('No y_units recognized : ', expdata['y_units'])
        quit()

#   km vertical coordinate linear
#   ax = fig.add_subplot(1, 1, 1, ylim=(0,40))


#    ax.set_title(r'O$_3$')
    ax.set_title(title)

    x=expdata['x']
    y=expdata['y']

# impose contourlevels : viridis = standard colourmap
    cmap='RdYlBu_r'
#   cmap='YlGnBu'
    gamma=1 # linear
    if ( figlayout.contour_levels_type == 'imposed' ) :
#        levels=np.arange(0,50.e-9,5.e-9)
#       levels, gamma=getlevels.getlevels(var=var, units=units, spacing='non-linear')
        if ( wlist[1] != 0. ) : spacing='xdiff'
        else                  : spacing='non-linear'
        levels, gamma=getlevels.getlevels(var=var, units=units, spacing=spacing)
        print('gamma : ', gamma)
        filled_c = ax.contourf(x, y, z, levels, cmap=cmap, norm=colors.PowerNorm(gamma=gamma))
#       filled_c = ax.contourf(x, y, z, levels, colors=['red','green','blue','yellow'])
    elif ( figlayout.contour_levels_type == 'free' ) :
        filled_c = ax.contourf(x, y, z, cmap=cmap, norm=colors.PowerNorm(gamma=gamma))



#   v = np.arange(0,1.e-5,1.e-6) # (start, stop, step) 
#    v = np.arange(0,1.e-8,1.e-9)
#v=np.array([0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0])*1.e-9

#   filled_c = ax.contourf(data['x'], data['y'], data['z'])
#   filled_c = ax.contourf(data['x'], data['y'], z, v)
    #filled_c = ax.contourf(x, y, z, v)

    # And black line contours.
    line_c = ax.contour(x, y, z, levels=filled_c.levels, colors=['black'])



    # Add a colorbar for the filled contour.
    #fig.colorbar(filled_c, orientation='horizontal', label=units, aspect=40, shrink=0.8)
    fig.colorbar(filled_c, orientation='horizontal', aspect=40, shrink=1.0, format='%9.1e')

    # Use the line contours to place contour labels.
    ax.clabel(
        line_c,  # Typically best results when labelling line contours.
        colors=['black'],
        manual=False,  # Automatic placement vs manual placement.
        inline=True,  # Cut the line where the label will be placed.
        fmt=' {:.2e} '.format,  # Labes as integers, with some extra space.
    )

    #plt.show()
    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season

    if ( wlist[1] != 0. ) : expidrefid=expid+'_'+refid
    else                  : expidrefid=expid

    path='/projects/NS9560K/users/olivie/plots'

#   fig.savefig('/projects/NS2345K/www/people/olivie/plots/zonalmean_'+var+'_'+expid+'_'+timestamp+figlayout.code+'.'+figlayout.filetype, bbox_inches='tight')
    fig.savefig(path+'/zonalmean_'+var+'_'+expidrefid+'_'+timestamp+figlayout.code+'_'+code+'.ps', bbox_inches='tight')
    fig.savefig(path+'/zonalmean_'+var+'_'+expidrefid+'_'+timestamp+figlayout.code+'_'+code+'.png', bbox_inches='tight')

    plt.close("all")
