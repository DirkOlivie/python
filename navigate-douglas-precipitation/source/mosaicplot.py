import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from matplotlib import colors

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits
import getidlunits

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


def mosaicplot(expiddescriptionlist, var, datalist, expitczlist, refitczlist, suptitle, addcolorbar, code) :
#-------------
    '''
    INPUT
        expiddescriptionlist
        var
        datalist
        expitczlist
        refitczlist
        suptitle
        code
    '''
#
#    if ( code == 'CDR' ) : titlesuffix = 'CDR'
#    elif ( code == 'CDRSAITR' ) : titlesuffix = 'CDR + SAI(TR)'
#    elif ( code == 'CDRSAINH' ) : titlesuffix = 'CDR + SAI(NH)'
#    elif ( code == 'CDRSAISH' ) : titlesuffix = 'CDR + SAI(SH)'
#    else :
#        print('+++ mosaicplot +++')
#        print('code not recognized')
#        quit()

    nexpid=len(datalist)

    # Define a layout with named panels
    fig = plt.figure(figsize=(10, 3.5 * nexpid // 2)) # 10,4 used to be 8,5 (before 2026-06-29)
    gs = fig.add_gridspec(nexpid // 2 * 3 + 1, 2)

#    norm = colors.Normalize(vmin=-5e-8, vmax=5e-8)

    levels=np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])*0.1*3 #5.e-8

#
#   Set the base font size for all elements
    plt.rcParams.update({'font.size': 8})

#   Alternatively, set specific elements globally
#    plt.rcParams.update({
#    'axes.titlesize': 20,
#    'axes.labelsize': 16,
#    'xtick.labelsize': 12,
#    'ytick.labelsize': 12,
#    'legend.fontsize': 10})
#    You can view all available parameters using print(plt.rcParams.keys()).
#
#   # modify units
    for iexpid in range(nexpid) :
        units=getstandardunits.getstandardunits(datalist[iexpid]['units'])

        if ( var == 'PRECT' and units == 'm s-1' ) :
            factor=86400*1000  # s-1 -> day-1, m -> mm
            newunits='mm day-1'
        else :
            factor = 1
            newunits=units        

        datalist[iexpid]['field'] = datalist[iexpid]['field'] * factor
        datalist[iexpid]['units'] = newunits
#
#   calculate global total
    globavglist=[]
    for iexpid in range(nexpid) :   
        weight=areafraction.areafraction(longitude=datalist[iexpid]['longitude'], latitude=datalist[iexpid]['latitude'])        
        globavg=np.mean(weight*datalist[iexpid]['field'])/np.mean(weight)    
        globavglist.append(globavg)

    # values
    for iexpid in range(nexpid) :
        print(iexpid, np.min(datalist[iexpid]['field']),np.max(datalist[iexpid]['field']))

    # loop over all figures
    for iexpid in range(nexpid) : 
#       I. map 
        ax = fig.add_subplot(gs[iexpid // 2 * 3 :  iexpid // 2 * 3 + 2 , iexpid % 2], projection=ccrs.PlateCarree(central_longitude=180))
        ax.coastlines()
        ax.set_title(expiddescriptionlist[iexpid]['legend']+' '+str("%.2f"% (globavglist[iexpid]))+' '+getidlunits.getidlunits(newunits))
#        ax.set_extent([-180, 180, -50, 50])
        ax.set_extent([0,359.99, -60, 60])
        x=datalist[iexpid]['longitude']
        y=datalist[iexpid]['latitude']

        filled_c = ax.contourf(x,y,datalist[iexpid]['field'],levels,transform=ccrs.PlateCarree(), cmap='BrBG')#, extent=[0,360, -50,50]) #extent=[-180, 180, -50, 50]

#       gridlines
        gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
        gl.top_labels = False   # Disable top labels
        gl.right_labels = False # Disable right labels

#       plot ITCZ
        ax.plot(expitczlist[iexpid]['x'], expitczlist[iexpid]['y'], color='blue', linewidth=0.5, transform=ccrs.Geodetic()) # marker = 'o'
        
#       II. ITCZ shift
        ax_shift = fig.add_subplot(gs[iexpid // 2 * 3 + 2 , iexpid % 2])
#        ax_shift.plot(expitczlist[iexpid]['x'], expitczlist[iexpid]['y'] - refitczlist[iexpid]['y'])
        ax_shift.fill_between(expitczlist[iexpid]['x'], np.maximum(expitczlist[iexpid]['y'] - refitczlist[iexpid]['y'],0.), expitczlist[iexpid]['y'] - expitczlist[iexpid]['y'],color='red')
        ax_shift.fill_between(expitczlist[iexpid]['x'], np.minimum(expitczlist[iexpid]['y'] - refitczlist[iexpid]['y'],0.), expitczlist[iexpid]['y'] - expitczlist[iexpid]['y'],color='blue')
        ax_shift.plot(expitczlist[iexpid]['x'], expitczlist[iexpid]['y'] - refitczlist[iexpid]['y'], color = 'black', linewidth=0.5)
        ax_shift.set_xlim(0,360) #)(-180.,180.)
        ax_shift.set_ylim(-2.,2.)
        ax_shift.set_xlabel('Longitude')
        ax_shift.set_ylabel('Latitude')
        ax_shift.set_xticks([0,60,120,180,240,300,360])
        ax_shift.set_xticklabels(['0'+r'$\degree$','60'+r'$\degree$'+'E','120'+r'$\degree$'+'E','180'+r'$\degree$','120'+r'$\degree$'+'W','60'+r'$\degree$'+'W','0'+r'$\degree$']) ##([-180,-120,-60,0,60,120,180])




    if ( suptitle != '' ) :
        fig.suptitle('Precipitation change', fontsize=16)

    if (addcolorbar != None ) :
        cax = fig.add_axes([0.12, 0.12 / float(nexpid // 2) , 0.76, 0.03 / float(nexpid // 2)]) # left bottom with height [0.12, 0.12, 0.76, 0.03] before 2026-06-29
        fig.colorbar(filled_c, cax=cax, orientation='horizontal',extend='both', label=r'$\Delta$'+'Precipitation ['+getidlunits.getidlunits(newunits)+']')

    plt.tight_layout()

    path='/datalake/NS2345K/olivie/plots'

    fig.savefig(path+'/mosaic'+code+'.ps')#, bbox_inches='tight')
    fig.savefig(path+'/mosaic'+code+'.png')#, bbox_inches='tight')
