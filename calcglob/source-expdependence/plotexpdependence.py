import matplotlib.pyplot as plt
import numpy as np
import math
import os

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits
import getcolor
import getlinestyle
import getmarker

'''
    MODIFICATIONS
        (2022-09-28) : legend box outside figure
            https://towardsdatascience.com/legend-outside-the-plot-matplotlib-5d9c1caa9d31
'''

def plotexpdependence(data, freqtypelist, \
                      varlist,typevarlist,legendlist,colorlist,linestylelist, \
                      xvaluelist, xtitle, xunits, \
                      description,code,figlayout) :
#----------------------------------------------------------------------------------------------------
#    
    print('+++ plotexpdependence +++')
#
    nvar=len(data) # 
    nexpid=len(data[0]) #

#   optional parameters
    if ( colorlist == None ) : colorlist = np.zeros(nexpid,dtype=int)
    if ( linestylelist == None ) : linestylelist = np.zeros(nexpid,dtype=int) # all zeros

#   use first variable to define plots name
    variable=varlist[0]
    typevar=typevarlist[0]
    freqtype=freqtypelist[0]


#   figure size
    fig, ax = plt.subplots(figsize=[6,3],dpi=200) 

    ax.set_xlabel(xtitle+' ['+xunits+']')

    yunits=data[0][0]['units']
    ax.set_ylabel('['+getidlunits.getidlunits(units=yunits)+']') # use first experiment to obtain units
    ax.set_title(getidlvar.getidlvar(var=varlist[0]))       # use first experiment to obtain units

#   limit x-axis/y-axis range
    if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) : 
        ax.set_xlim(figlayout.xrange)

#   lin/log scale for y-axis
    if ( figlayout.ytype == 'log' ) :
        ax.set_yscale('log') 

#   plot the individual lines
    for ivar in range(0,nvar) : 
#
        y=np.zeros((nexpid),dtype='float')    
        yerr=np.zeros((nexpid),dtype='float')

        for iexpid in range(nexpid) :
            y[iexpid]    = data[ivar][iexpid]['Ex']
            yerr[iexpid] = data[ivar][iexpid]['error'] # error on mean
#
        if ( legendlist[ivar] == '' ) : ax.errorbar(xvaluelist, y, yerr=yerr,                         color=getcolor.getcolor(color=colorlist[ivar],colorscheme=figlayout.colorscheme),marker=getmarker.getmarker(marker=linestylelist[ivar]))      # label from legendlist   
        else                          : ax.errorbar(xvaluelist, y, yerr=yerr, label=legendlist[ivar], color=getcolor.getcolor(color=colorlist[ivar],colorscheme=figlayout.colorscheme),marker=getmarker.getmarker(marker=linestylelist[ivar]))      # label from legendlist

#   PLOTS X- and Y-AXIS
#    ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed')

#   LEGEND
    if ( figlayout.legendlocation == '' ) :
#       legend inside box
        ax.legend()

    elif ( figlayout.legendlocation == 'outside2.0' ) :
#       legend outside box (double size)
        pos = ax.get_position()
        ax.set_position([pos.x0, pos.y0, pos.width * 1.0, pos.height])
        ax.legend(loc='center right', bbox_to_anchor=(2.0, 0.5))

    elif ( figlayout.legendlocation == 'outside1.7' ) :
#       legend outside box (double size)
        pos = ax.get_position()
        ax.set_position([pos.x0, pos.y0, pos.width * 1.0, pos.height])
        ax.legend(loc='center right', bbox_to_anchor=(1.7, 0.5))

    elif ( figlayout.legendlocation == 'outside1.5' ) :
#       legend outside box (double size
        pos = ax.get_position()
        ax.set_position([pos.x0, pos.y0, pos.width * 1.0, pos.height])
        ax.legend(loc='center right', bbox_to_anchor=(1.5, 0.5))

    elif ( figlayout.legendlocation == 'outside1.4' ) :
#       legend outside box (double size
        pos = ax.get_position()
        ax.set_position([pos.x0, pos.y0, pos.width * 1.0, pos.height])
        ax.legend(loc='center right', bbox_to_anchor=(1.4, 0.5))


#   plot directory
#   path='/projects/NS2345K/www/people/olivie/plots/'+code
#   path='/projects/NS2345K/www/people/olivie/plots'
    path='/projects/NS9560K/users/olivie/plots'
#   path='/datalake/NS2345K/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/plotexpdependence_'+variable+'_'+typevar+'_'+freqtype+'_'+description+'_'+code+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/plotexpdependence_'+variable+'_'+typevar+'_'+freqtype+'_'+description+'_'+code+'.png', bbox_inches='tight')

    print('--- plotexpdependence ---')
