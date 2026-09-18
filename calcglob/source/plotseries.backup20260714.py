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

def plotseries(data,legendlist,shiftlist,smoothlist,freqtype,typevar,code,figlayout,colorlist=None,linestylelist=None,ensembletypelist=None) :
#-------------------------------------------------------------------------------------------------------------------------------------------
#    
    print('+++ plotseries +++')
#
    nexpid=len(data)

#   optional parameters
    if ( colorlist == None ) : colorlist = np.zeros(nexpid,dtype=int)
    if ( linestylelist == None ) : linestylelist = np.zeros(nexpid,dtype=int) # all zeros
    if ( ensembletypelist == None ) : ensembletypelist = ['']*nexpid

    variable=data[0]['variable']            # use first experiment to obtain variable name
    units=data[0]['units']                  # use first experiment to obtain units 

    areaglob=data[0]['areaglob']
    area    =data[0]['area'] 

    print(variable+'XXX')
    print(units+'XXX')

    
    factorlist=np.zeros(nexpid,dtype=float)
    newunitslist=['']*nexpid

    for iexpid in range(0,nexpid) :
        units=getstandardunits.getstandardunits(data[iexpid]['units'])
        variable=data[iexpid]['variable']

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
        else : 
            factorlist[iexpid] = 1.                                                         
            newunitslist[iexpid]=units  
#
    newunits=newunitslist[0]
    variable=data[0]['variable']    

#   filename
    filename=variable+'_'+typevar+'_'+freqtype+'_'+code

    prefix=getprefix.getprefix(filename=filename)

#   preparation for writing out all data
    asciifilename='/nird/home/olivie/output/duncan/'+variable+'_'+typevar+'_'+freqtype+'_'+code+'.txt'
    f=open(asciifilename,'w')

#    fig,ax =plt.subplots()     
#   fig, ax = plt.subplots(figsize=[8,4],dpi=100) # standard upto 2023-05-23
    fig, ax = plt.subplots(figsize=[6,3],dpi=200) 

    ax.set_xlabel('Time [yr]')                                     # x-axis label 
    ax.set_ylabel('['+getidlunits.getidlunits(units=newunits)+']') # y-axis label
#
#   title
    if ( figlayout.title != '' ) : 
        title=figlayout.title        
    else :
        title=getidlvar.getidlvar(var=variable) + ' ['+freqtype+'] ['+typevar+']'                       # title

#   region in title
    if ( figlayout.regionintitle ) : title=title+' ['+getidlregion.getidlregion(region=typevar)+']'   # add region to title
    ax.set_title(prefix+title)                                            # 

#   limit x-axis/y-axis range
    if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) : 
        ax.set_xlim(figlayout.xrange)

#   lin/log scale for y-axis
    if ( figlayout.xtype == 'log' ) :
        ax.set_yscale('log') 
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

        if ( ensembletypelist[iexpid] == 'minmax' ) : 
            y_min=data[iexpid]['valuelist_min']
            y_max=data[iexpid]['valuelist_max']

#
#       only work on subset that fall with xrange
#       -----------------------------------------
        if ( figlayout.xrange[0] != -1 or figlayout.xrange[1] != -1) :
            iset0 = ( x >= figlayout.xrange[0] ) # array of booleans
            iset1 = ( x <= figlayout.xrange[1] ) # array of booleans
            iset = iset0 * iset1

            x = x[iset]
            y = y[iset]

            if ( ensembletypelist[iexpid] == 'minmax' ) :
                y_min = y_min[iset]
                y_max = y_max[iset]

            ntime = len(x) 

#       running average
#       ---------------
        if ( smoothlist[iexpid] > 0 ) :      

            values=np.zeros(ntime,dtype=float)    

            if ( ensembletypelist[iexpid] == 'minmax' ) :
                values_min=np.zeros(ntime,dtype=float)
                values_max=np.zeros(ntime,dtype=float)

            for itime in range(0,ntime) :

                actuallen=min([smoothlist[iexpid], itime, ntime-1-itime])             

#               squared running average
                values[itime]=sum(y[itime-actuallen:itime+actuallen+1]) / float(2*actuallen+1)  
                if ( ensembletypelist[iexpid] == 'minmax' ) :
                   values_min[itime]=sum(y_min[itime-actuallen:itime+actuallen+1]) / float(2*actuallen+1)
                   values_max[itime]=sum(y_max[itime-actuallen:itime+actuallen+1]) / float(2*actuallen+1) 

            n0=smoothlist[iexpid]        # do not plot first points
            n1=ntime-smoothlist[iexpid]  # do not plot last points

        else :
       
            values = y
            if ( ensembletypelist[iexpid] == 'minmax' ) :
                values_min = y_min
                values_max = y_max

            n0=0                         # plot all points
            n1=ntime                     # plot all points

#       only plot if subset length different from 0
        if ( n0 < n1 ) : 

            if ( legendlist[iexpid] == '' ) : ax.plot(x[n0:n1], factor*values[n0:n1],                                                color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]),linewidth=1.0)      # label from legendlist
            else                            : ax.plot(x[n0:n1], factor*values[n0:n1], label=getidlvar.getidlvar(legendlist[iexpid]), color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]),linewidth=1.0)      # label from legendlist   

            if ( ensembletypelist[iexpid] == 'minmax' ) :
                ax.fill_between(x[n0:n1], factor*values_min[n0:n1], factor*values_max[n0:n1], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme), alpha=0.2)


            ymintmp=min(factor*values[n0:n1])
            ymaxtmp=max(factor*values[n0:n1])

            ymin=min([ymin,ymintmp])
            ymax=max([ymax,ymaxtmp])    

#           writing to file 
            f.write('VAR=')
            f.write(data[iexpid]['variable'])
            f.write('\n')    
            f.write('EXPID=')
            f.write(legendlist[iexpid])
            f.write('\n')
            for itime in range(n0,n1-n0) :
                f.write(str("%4.4i"% (x[itime])))
                f.write(' ')
                f.write(str("%13.6e"% (factor*values[itime])))
                f.write('\n')  

#   HadCrut5
    if ( variable == 'TREFHT' and 0 == 1 ) : 
        hcdata = gethadcrut.gethadcrut()
#       mean over 1850-1899 period    
        boolarr = ( hcdata['yearlist'] >= 1850 ) * ( hcdata['yearlist'] < 1900 )

        hcmean=np.mean(hcdata['valuelist'][boolarr])


        expidmeanlist=[]  

        for iexpid in range(0,nexpid) :        
            boolarr = ( data[iexpid]['timelist'] >= 1850 ) * ( data[iexpid]['timelist'] < 1900 )
            expidmean=np.mean(data[iexpid]['valuelist'][boolarr])

            expidmeanlist.append(expidmean)

        expidmeanlist=np.array(expidmeanlist)
        
        expidmean=np.mean(expidmeanlist) 
        
        print('expidmean : ', expidmean)
        print('hcmean    : ', hcmean)

        ax.plot(hcdata['yearlist'],hcdata['valuelist'] + expidmean - hcmean  , color=getcolor.getcolor(color=1,colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=0))



        print(iset)

#
    if ( figlayout.legendlocation == '' ) :
#       legend inside box
        ax.legend(fontsize=6)  # 6 # 7 # 9 

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
#    if ( ymin*ymax < 0. or min([abs(ymin),abs(ymax)]) / max([abs(ymin),abs(ymax)]) < 0.2 ) :
#        ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed')

    if (figlayout.axhline != None ) :
        for ypos in figlayout.axhline :
            ax.axhline(ypos,lw=1.0,color='tab:gray',linestyle='dashed')

    if (figlayout.axvline != None ) :
        for xpos in figlayout.axvline :
            ax.axvline(xpos,lw=1.0,color='tab:gray',linestyle='dashed')

#    ax.axhspan(ymin=1.5, ymax=2., color='lightblue', alpha=0.5)


#   plot directory
#   path='/projects/NS2345K/www/people/olivie/plots/'+code
#   path='/projects/NS2345K/www/people/olivie/plots'

    if ( figlayout.plotdir == None ) :
        path='/projects/NS9560K/users/olivie/plots'
    else : 
        path=figlayout.plotdir

#   path='/datalake/NS2345K/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/'+filename+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.png', bbox_inches='tight')

#   ascii file output
    f.close()

    print('--- plotseries ---')
