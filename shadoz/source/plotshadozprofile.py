import matplotlib.pyplot as plt
import numpy as np

import getfullstationname

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlregion
import getcolor
import getlinestyle

'''
    MODIFICATIONS
        (2023-10-20) Adding colorlist and colorscheme

'''

def plotshadozprofile(var,station,modeldatalist,legendlist,obsdata,figlayout,code,verticalaxis,season,colorlist=None) :
#--------------------
#
    print('+++ plotshadozprofile +++')
#
    linewidth_model=1
    linewidth_obs=3
#
    nexpid=len(modeldatalist)
    nobs=len(obsdata)
    print(nobs)
#    print(obsdata)

    year0=0
    year1=0

#   optional parameters
#   if ( colorlist == None ) : colorlist = np.zeros(nexpid,dtype=int) # all zeros
#    if ( colorlist == None ) : colorlist = np.arange(0,nexpid)  

#   use first experiment to get some information
#    var=datalist[0]['var']            # use first experiment to obtain units
#    units=datalist[0]['units']
#    region=datalist[0]['region']
#    verticalaxis=datalist[0]['verticalaxis']

#    year0=datalist[0]['year0']
#    year1=datalist[0]['year1']
#    season=datalist[0]['season']

#    if ( var == 'O3' or var == 'ozone' and units =='mol/mol' ) : 
#        factor=1.e+6
#        newunits='ppm'
#    else :
#       factor=1.
#       newunits=units   

    fig,ax =plt.subplots(figsize=figlayout.figsize)     
#   ax.set_ylabel('Pressure [Pa]')
#    ax.set_xlabel('['+newunits+']') # use first experiment to obtain units
#   ax.set_title(getidlvar.getidlvar(var=variable))                  # use first experiment to obtain units
#    ax.set_title(getidlvar.getidlvar(var))                                           # use first experiment to obtain units
#    ax.set_title(getidlvar.getidlvar(var=var)+' ['+getidlregion.getidlregion(region=region)+']')


#    printing individual profiles
#    for iobs in range(0,nobs) :
#        ax.plot(obsdata[iobs]['ylist'][:],obsdata[iobs]['xlist'][:], color=getcolor.getcolor(color=iobs,colorscheme=figlayout.colorscheme))


#    printing min, max, mean, median, ...
    ax.plot(obsdata['ymin'   ][:],obsdata['xlist'][:], label='min (obs)'   , color=getcolor.getcolor(color=0,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=1), linewidth=1)
    ax.plot(obsdata['yq25'   ][:],obsdata['xlist'][:], label='q25 (obs)'   , color=getcolor.getcolor(color=0,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=2), linewidth=1)
    ax.plot(obsdata['ymedian'][:],obsdata['xlist'][:], label='median (obs)', color=getcolor.getcolor(color=0,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=0), linewidth=linewidth_obs)
#   ax.plot(obsdata['ymean'  ][:],obsdata['xlist'][:], label='mean (obs)'  , color=getcolor.getcolor(color=3,colorscheme=figlayout.colorscheme))
    ax.plot(obsdata['yq75'   ][:],obsdata['xlist'][:], label='q75 (obs)'   , color=getcolor.getcolor(color=0,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=2), linewidth=1)
    ax.plot(obsdata['ymax'   ][:],obsdata['xlist'][:], label='max (obs)'   , color=getcolor.getcolor(color=0,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=1), linewidth=1)

    for iexpid in range(0,nexpid) : 

        print('Legend : ', legendlist[iexpid])
        print('xlist : ', modeldatalist[iexpid]['xlist'])

        ax.plot(modeldatalist[iexpid]['ymean'], modeldatalist[iexpid]['xlist'], label=legendlist[iexpid], color=getcolor.getcolor(color=1+iexpid,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=0), linewidth=linewidth_model)
#       ax.plot(modeldatalist[iexpid]['ymean']*1000., modeldatalist[iexpid]['xlist']/1000., label=legendlist[iexpid], color=getcolor.getcolor(color=3+iexpid,colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=0), linewidth=3.0)
#       if ( legendlist[iexpid] == '' ) : ax.plot(factor * datalist[iexpid]['valuelist'], datalist[iexpid]['zlist'],                           color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme))
#       else                            : ax.plot(factor * datalist[iexpid]['valuelist'], datalist[iexpid]['zlist'], label=legendlist[iexpid], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme))
#
    ax.legend()
#
    ax.set_title(getfullstationname.getfullstationname(station=station)+' ['+season+']')

    ax.set_xlabel('['+obsdata['yunit']+']')

#   to have log-scale on x-axis
#    if (wlist[1] == 0. ) : ax.set_xscale('log')

    if ( verticalaxis == 'pressure' ) :
        ax.set_ylabel('Pressure [Pa]')
        ax.set_yscale('log')

#        plt.ylim([100000.,1.])
        plt.ylim([1000.,1.])
#       plt.ylim([100000.,100.])
#       plt.ylim([100000.,5000.])

    elif ( verticalaxis == 'height' ) : 
        ax.set_ylabel('Height [km]')
        plt.ylim([0.,40.])

    else :
         print('No verticalaxis recognized : '+verticalaxis)
         quit()

    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season
    timestamp=season
#
#   path='/projects/NS9560K/users/olivie/plots/shadoz'
    path='/datalake/NS2345K/olivie/plots/shadoz'
#
    fig.savefig(path+'/shadozprofile_'+var+'_'+timestamp+'_'+station+'_'+verticalaxis+figlayout.code+'_'+code+'.ps',  bbox_inches='tight')
    fig.savefig(path+'/shadozprofile_'+var+'_'+timestamp+'_'+station+'_'+verticalaxis+figlayout.code+'_'+code+'.png', bbox_inches='tight')
