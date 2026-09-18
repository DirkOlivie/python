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

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import plotseries


def mosaicplotseries(expiddescriptionlist, datalist, suptitle, code, ncol) :
#-------------------
    '''
    INPUT
        expiddescriptionlist
        var
        datalist
        suptitle
        code
    '''
#
    ndescription=len(expiddescriptionlist)

    # Define a layout with named panels
    nrow = ( ndescription - 1 ) // ncol +1
    fig = plt.figure(figsize=(5*ncol, 2*nrow), dpi=300) # 10,4 used to be 8,5 (before 2026-06-29)
    gs = fig.add_gridspec(nrow, ncol)

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
    for idescription in range(ndescription) : 
        
        ax = fig.add_subplot(gs[idescription // ncol , idescription % ncol])
        
        plotseries.plotseries_internal(ax=ax, \
                                       data=datalist[idescription], \
                                       legendlist=expiddescriptionlist[idescription]['legendlist'], \
                                       shiftlist =expiddescriptionlist[idescription]['shiftlist'], \
                                       smoothlist=expiddescriptionlist[idescription]['smoothlist'], \
                                       freqtype  =expiddescriptionlist[idescription]['freqtype'], \
                                       typevar   =expiddescriptionlist[idescription]['typevarlist'][0], \
                                       code=code, \
                                       figlayout       =expiddescriptionlist[idescription]['figlayout'], \
                                       colorlist       =expiddescriptionlist[idescription]['colorlist'], \
                                       linestylelist   =expiddescriptionlist[idescription]['linestylelist'], \
                                       ensembletypelist=expiddescriptionlist[idescription]['ensembletypelist'])

    if ( suptitle != '' ) :
        fig.suptitle('Precipitation change', fontsize=16)

    plt.tight_layout()

    path='/datalake/NS2345K/olivie/plots'

    fig.savefig(path+'/mosaicseries'+code+'.ps')#, bbox_inches='tight')
    fig.savefig(path+'/mosaicseries'+code+'.png')#, bbox_inches='tight')
