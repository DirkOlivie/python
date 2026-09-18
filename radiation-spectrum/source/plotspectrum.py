import matplotlib.pyplot as plt
import numpy as np
import math
import os

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits
import getidlregion
import getcolor
import getlinestyle

sys.path.insert(0,'/nird/home/olivie/code/python/hadcrut/source')
import gethadcrut


'''
    MODIFICATIONS
	(2025-10-01) : 
'''

def plotspectrum(data,legendlist,shiftlist,smoothlist,code,figlayout,colorlist=None,linestylelist=None) :
#----------------------------------------------------------------------------------------------------
#    
    print('+++ plotspectrum +++')
#
    nexpid=len(data)

#   optional parameters
    if ( colorlist == None ) : colorlist = np.zeros(nexpid,dtype=int)
    if ( linestylelist == None ) : linestylelist = np.zeros(nexpid,dtype=int) # all zeros

    variable=data[0]['variable']            # use first experiment to obtain variable name
    units=data[0]['units']                  # use first experiment to obtain units 

    factor=1.
    newunits=units


#    fig,ax =plt.subplots()     
#   fig, ax = plt.subplots(figsize=[8,4],dpi=100) # standard upto 2023-05-23
    fig, ax = plt.subplots(figsize=[6,3],dpi=200) 

    ax.set_xlabel('Spectrum ['+data[0]['wavelength_units']+']')                                     # x-axis label 
    ax.set_ylabel('['+getidlunits.getidlunits(units=newunits)+']') # y-axis label
#
#   title
    if ( figlayout.title != '' ) : 
        title=figlayout.title        
    else :
        title=getidlvar.getidlvar(var=variable)                       # title

#   limit x-axis/y-axis range
    if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) : 
        ax.set_xlim(figlayout.xrange)

#   lin/log scale for y-axis
    if ( figlayout.xtype == 'log' ) :
        ax.set_xscale('log') 
    if ( figlayout.ytype == 'log' ) :
        ax.set_yscale('log') 

#   plot the individual lines
    ymin = 1.e36
    ymax =-1.e36

    for iexpid in range(0,nexpid) : 

        nwvl=len(data[iexpid]['wavelength'])
        x=data[iexpid]['wavelength'] + shiftlist[iexpid]
        y=data[iexpid]['valuelist']
#
#       only work on subset 
        if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) :
            iset0 = ( x >= figlayout.xrange[0] ) # array of booleans
            iset1 = ( x <= figlayout.xrange[1] ) # array of booleans
            iset = iset0 * iset1

            x = x[iset]
            y = y[iset]
            nwvl = len(x) 

#       running average
        if ( smoothlist[iexpid] > 0 ) :      

            values=np.zeros(nwvl,dtype=float)    

            for iwvl in range(0,nwvl) :

                actuallen=min([smoothlist[iexpid], iwvl, nwvl-1-iwvl])             

#               squared running average
                values[iwvl]=sum(y[iwvl-actuallen:iwvl+actuallen+1]) / float(2*actuallen+1)  

            n0=smoothlist[iexpid]        # do not plot first points
            n1=nwvl-smoothlist[iexpid]  # do not plot last points

        else :
       
            values = y
            n0=0                         # plot all points
            n1=nwvl                      # plot all points

#
        if ( legendlist[iexpid] == '' ) : ax.plot(x[n0:n1], factor*values[n0:n1],                                                color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))      # label from legendlist
        else                            : ax.plot(x[n0:n1], factor*values[n0:n1], label=getidlvar.getidlvar(legendlist[iexpid]), color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))      # label from legendlist   

        ymintmp=min(factor*values[n0:n1])
        ymaxtmp=max(factor*values[n0:n1])

        ymin=min([ymin,ymintmp])
        ymax=max([ymax,ymaxtmp])    

#
    if ( figlayout.legendlocation == '' ) :
#       legend inside box
        ax.legend(fontsize=6)  # 7 # 9 

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

#   PLOTS X- and Y-AXIS
    if ( ymin*ymax < 0. or min([abs(ymin),abs(ymax)]) / max([abs(ymin),abs(ymax)]) < 0.2 ) :
        ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed')

    path='/projects/NS9560K/users/olivie/plots'
#   path='/datalake/NS2345K/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/'+variable+'_'+code+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/'+variable+'_'+code+'.png', bbox_inches='tight')

    print('--- plotseries ---')
