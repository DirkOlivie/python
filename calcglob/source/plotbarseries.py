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
import getprefix
import getstandardunits

sys.path.insert(0,'/nird/home/olivie/code/python/hadcrut/source')
import gethadcrut


'''
    MODIFICATIONS
	(2022-03-01) : plotting value_seasonavg (instead of value_annavg)
	(2022-03-01) : need surface area to convert Tg[O3] to DU[O3] if regional domains are used
	(2022-03-07) : added possibility for funning average (smoothlist)
        (2022-05   ) : writes out data for Duncan in /nird/home/olivie/output/duncan/
        (2022-07-07) : allows to plot raw monthly data
        (2022-09-28) : legend box outside figure
            https://towardsdatascience.com/legend-outside-the-plot-matplotlib-5d9c1caa9d31
        (2022-10-21) : adding x-range limit (figlayout)
        (2022-10-24) : only treating values within x-range limit
        (2025-01-14) : adding linestylelist
        (2025-06-25) : adding zero line
'''

def plotbarseries_internal (ax,data,legendlist,shiftlist,freqtype,code,figlayout,colorlist,linestylelist,linewidthlist) :
#----------------------
#    
    print('+++ plotbarseries_internal +++')
#
#   number of experiments
    nexpid=len(data)

#   optional parameters
    if ( colorlist        == None ) : colorlist = np.zeros(nexpid,dtype=int)
    if ( linestylelist    == None ) : linestylelist = np.zeros(nexpid,dtype=int) # all zeros
    if ( linewidthlist    == None ) : linewidthlist = np.ones(nexpid,dtype=int) # all zeros

#   scaling : factorlist and newunitslist
    factorlist=np.zeros(nexpid,dtype=float)
    newunitslist=['']*nexpid

    for iexpid in range(0,nexpid) :
        units=getstandardunits.getstandardunits(data[iexpid]['units'])
        variable=data[iexpid]['variable']
        areaglob=data[iexpid]['areaglob']
        area    =data[iexpid]['area']

        # Tg[CO2] -> Pg[C]
        if ( variable in ['TMCO2_offset','TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset', \
                          'SFCO2_cumulative','SFCO2_FFF_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_cumulative', \
                          'TMCO2_FFF_offset_minus_SFCO2_FFF_cumulative','TMCO2_LND_offset_minus_SFCO2_LND_cumulative','TMCO2_OCN_offset_minus_SFCO2_OCN_cumulative','TMCO2_FFFLNDOCN_offset_minus_SFCO2_FFFLNDOCN_cumulative','TMCO2_offset_minus_SFCO2_cumulative'] \
            and units == 'Tg' ) :
            factorlist[iexpid] = 1.e-3 * 12. / ( 12. + 2. * 16.)
            newunitslist[iexpid] = 'Pg(C)'
        # Tg[CO2]/yr -> Pg[C]/yr
        elif ( variable in ['SFCO2','SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN'] \
            and units == 'Tg yr-1' ) :
            factorlist[iexpid] = 1.e-3 * 12. / ( 12. + 2. * 16.)
            newunitslist[iexpid] = 'Pg(C) yr-1'
        elif ( variable in ['FCO2xLANDFRAC_minus_SFCO2_LND'] \
            and units == 'Tg yr-1' ) :
            factorlist[iexpid] = 1.e-3 / 12.
            newunitslist[iexpid] = 'Pg(CO2) month-1'
        elif ( variable in ['CO2_columnburden_as_vmr'] \
            and units == 'mol mol-1' ) :
            factorlist[iexpid] = 1.e6
            newunitslist[iexpid] = 'ppm'
        elif ( ( variable == 'cb_O3'  \
            or variable == 'ozone_columnburden' \
            or variable == 'O3_columnburden' ) and ( units == 'Tg' ) ) : 
            factorlist[iexpid] = 1.e9 / ( 4. * math.pi *6.37e6 * 6.37e6) * 1. / 2.1415e-5 * areaglob / area
            newunitslist[iexpid]='DU'
        elif ( variable == 'toz' and units == 'm' ) :
            factorlist[iexpid]=1.e5  # m --(x1000)-> mm -> --(x100)--> 0.01mm
            newunitslist[iexpid]='DU' 
        elif ( variable == 'pr' and units == 'Tg yr-1' ) :
            factorlist[iexpid] = 1.e9 / ( 4. * math.pi *6.37e6 * 6.37e6) / 365. * areaglob / area
            newunitslist[iexpid]='mm day-1'
        elif ( variable == 'ch4_surfacelayer' \
            or variable == 'CH4_SRF' ) :
            factorlist[iexpid]   = 1.e9
            newunitslist[iexpid] = 'ppb'
        elif ( variable == 'o3_surfacelayer' ) :
            factorlist[iexpid]   = 1.e9
            newunitslist[iexpid] = 'ppb'
        elif ( variable == 'N2O_SRF' ) :
            factorlist[iexpid]   = 1.e9
            newunitslist[iexpid] = 'ppb'
        elif ( ( variable == 'BRY_layer00' \
              or variable == 'BRY_layer06' \
              or variable == 'BRY_SUM_layer00' \
              or variable == 'BRY_SUM_layer06' \
              or variable == 'BRY_SCALED_layer00' \
              or variable == 'BRY_SCALED_layer06' \
              ) and units == 'mol mol-1' ) :
            factorlist[iexpid]   = 1.e12 
            newunitslist[iexpid] = 'ppt'
        elif ( ( variable == 'CLY_layer00' \
              or variable == 'CLY_layer06' \
              or variable == 'CLY_SUM_layer00' \
              or variable == 'CLY_SUM_layer06' \
              or variable == 'CLY_SCALED_layer00' \
              or variable == 'CLY_SCALED_layer06' \
            ) and units == 'mol mol-1' ) :
            factorlist[iexpid]   = 1.e9 
            newunitslist[iexpid] = 'ppb'
        elif ( variable == 'mmflxdmax26.0Nocn' \
            or variable == 'voltrocn' ) :
            factorlist[iexpid]   =1.e-9 
            newunitslist[iexpid] = 'Sv'
#        elif ( variable == 'ICEFRAC' ) :
#            factorlist[iexpid]=area*1.e-6   # fraction -> m2 -> km2
#            newunitslist[iexpid]='km2'
        elif ( variable == 'ICEFRAC' ) :
            factorlist[iexpid]=area*1.e-12   # fraction -> m2 -> 1e6km2
            newunitslist[iexpid]='1e6km2'
        elif ( variable == 'CLDTOT' and units == 'fraction' ) : 
            factorlist[iexpid]=100.
            newunitslist[iexpid]='%'
        elif ( variable == 'utsvolcemis' and units == 'kg' ) :
            factorlist[iexpid]=1.e-9
            newunitslist[iexpid]='Tg'
        else : 
            factorlist[iexpid] = 1.                                                         
            newunitslist[iexpid]=units  
#
    newunits=newunitslist[0]
    variable=data[0]['variable']    

#   filename
    filename=variable+'_'+freqtype+'_'+code

    prefix=getprefix.getprefix(filename=filename)

#   preparation for writing out all data

#   x-label
    if ( figlayout.xlabel == None ) : ax.set_xlabel('Time [yr]')   # x-axis label default
    else                            : ax.set_xlabel(figlayout.xlabel)

#   y-label
    ax.set_ylabel('['+getidlunits.getidlunits(units=newunits)+']') # y-axis label
#
#   title
    if ( figlayout.title != '' ) : 
        title=figlayout.title        
    else :
        title=getidlvar.getidlvar(var=variable) #+ ' ['+freqtype+'] ['+typevar+']'                       # title

#   region in title
    if ( figlayout.regionintitle ) : title=title #+' ['+getidlregion.getidlregion(region=typevar)+']'   # add region to title

    ax.set_title(prefix+title)                                            # 

#   limit x-axis/y-axis range
    if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) : 
        ax.set_xlim(figlayout.xrange)

#   lin/log scale for y-axis
    if ( figlayout.xtype == 'log' ) :
        ax.set_xscale('log') 
    if ( figlayout.ytype == 'log' ) : 
        ax.set_yscale('log')

#   initialize minimum and maximum
    ymin = 1.e36
    ymax =-1.e36

#   plot individual lines
    for iexpid in range(0,nexpid) : 

        factor=factorlist[iexpid]

        ntime=len(data[iexpid]['timelist'])

#       valuelist and timelist
#       ----------------------
        x=data[iexpid]['timelist'] + shiftlist[iexpid] 
        y=data[iexpid]['valuelist']

#       only work on subset that fall with xrange
#       -----------------------------------------
        if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) :
            iset0 = ( x >= figlayout.xrange[0] ) # array of booleans
            iset1 = ( x <= figlayout.xrange[1] ) # array of booleans
            iset = iset0 * iset1

            x = x[iset]
            y = y[iset]

            ntime = len(x) 

        values = y
        n0=0                         # plot all points
        n1=ntime                     # plot all points

#       only plot if subset length different from 0
        if ( n0 < n1 ) : 

            if ( legendlist[iexpid] == '' ) : ax.bar(x[n0:n1], factor*values[n0:n1],                                                color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]),width=linewidthlist[iexpid])      # label from legendlist
            else                            : ax.bar(x[n0:n1], factor*values[n0:n1], label=getidlvar.getidlvar(legendlist[iexpid]), color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]),width=linewidthlist[iexpid])      # label from legendlist   

#
#   legend inside box
    ax.legend(fontsize=6)  # 6 # 7 # 9 

#
#   Y range
    if ( figlayout.yrange != [-1.,-1.] ) :
        plt.ylim([figlayout.yrange[0],figlayout.yrange[1]])

    print('--- plotbarseries_internal ---')


def plotbarseries(data,legendlist,shiftlist,freqtype,code,figlayout,colorlist,linestylelist,linewidthlist) :
#-------------------------------------------------------------------------------------------------------------------------------------------
#
    '''
    CALLS 
        plotbarseries_internal

    '''
    
    print('+++ plotbarseries +++')
#
    fig, ax = plt.subplots(figsize=[6,3],dpi=400)
#
    plotbarseries_internal(ax=ax,data=data,legendlist=legendlist,shiftlist=shiftlist,freqtype=freqtype,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)

#   filename
    variable=data[0]['variable']
    filename=variable+'_'+freqtype+'_'+'y'+figlayout.ytype+'_'+code

#   plot directory
    if ( figlayout.plotdir == None ) :
        path='/projects/NS9560K/users/olivie/plots'
    else : 
        path=figlayout.plotdir

    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/'+filename+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.png', bbox_inches='tight')

    print('--- plotbarseries ---')
