import matplotlib.pyplot as plt
import numpy as np

import experimentdefinition

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlregion
import getstandardunits
import getidlunits
import getcolor
import getlinestyle
import getprefix

'''
    MODIFICATIONS

    PLOTS WITH DIFFERENT SCALES
        https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
'''

def plotzonalmeanline(datalist,legendlist,wlist,figlayout,code,horizontalaxis,colorlist=None,linestylelist=None,linewidthlist=None,ensembletypelist=None) :
#--------------------------------------------------------------
#
    '''
    INPUT
        datalist
        legendlist
        wlist : not used
        figlayout
        code : string appearing in filename of plot
        colorlist : [0,1,2,...]
        linestylelist : [0,1,0,0,...]    

    CALLED BY

    CALLS

    '''
#
    print('+++ plotzonalmeanline +++')
#
#    print('ensembletypelist : ', ensembletypelist)
#    quit()

    nexpid=len(datalist)

    print('nexpid : ', nexpid)

#   optional parameters
    if ( colorlist == None ) : colorlist = np.arange(0,nexpid)  
    if ( linestylelist == None ) : linestylelist = np.zeros(nexpid,dtype=int) # all zeros
    if ( linewidthlist == None ) : linewidthlist = np.ones(nexpid,dtype=int) # all zeros

#   use first experiment to get some information
    var=datalist[0]['variable']            # use first experiment to obtain units
    units=datalist[0]['units']
    region=datalist[0]['region']

    year0=datalist[0]['year0']
    year1=datalist[0]['year1']
    season=datalist[0]['season']

    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season # appears in name of plot


#   FILENAME FOR FIGURE
    filename='zonalmeanline_'+var+'_'+timestamp+'_'+region+'_'+horizontalaxis+figlayout.code+'_'+code

    prefix=getprefix.getprefix(filename=filename) # Figure title needs a) , b) , ...


    print('var   : ', var)
    print('units : ', units)

#   POSSIBLY CHANGE UNITS
    if ( ( var == 'O3' or var == 'ozone' or var == 'O3_SRF' or var == 'CH4_SRF' or var == 'o3_surfacelayer' ) and getstandardunits.getstandardunits(units) =='mol mol-1' ) : 
        factor=1.e+9
        newunits='ppb'
    elif ( var == 'ch4_surfacelayer' ) :
        factor   = 1.e9
        newunits = 'ppb'
    elif ( var == 'h2_surfacelayer' ) :
        factor   = 1.e9
        newunits = 'ppb'
    elif ( var == 'hus' and getstandardunits.getstandardunits(units) =='kg kg-1' ) : 
        factor=28.964/18.0153 * 1.e+6
        newunits='ppmv'
    elif ( ( var == 'PRECT' \
          or var == 'PRECC' \
          or var == 'PRECL' ) and getstandardunits.getstandardunits(units) =='m s-1' ) : 
        factor=1000 * 86400.
        newunits='mm day-1'
    else :
       factor=1.
       newunits=units   


    fig,ax =plt.subplots(figsize=[7.2,2.4],dpi=100)     
    ax.set_ylabel('['+getidlunits.getidlunits(getstandardunits.getstandardunits(newunits))+']')
    ax.set_xlabel('Latitude [deg.]') 
    ax.set_title(prefix+getidlvar.getidlvar(var=var)) #+' ['+getidlregion.getidlregion(region=region)+']')

#   LOOP OVER ALL EXPERIMENTS
    for iexpid in range(0,nexpid) : 

        if ( legendlist[iexpid] == '' ) : ax.plot(datalist[iexpid]['latitude'], factor * datalist[iexpid]['valuelist'],                           color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]),linewidth=linewidthlist[iexpid])
        else                            : ax.plot(datalist[iexpid]['latitude'], factor * datalist[iexpid]['valuelist'], label=legendlist[iexpid], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]),linewidth=linewidthlist[iexpid])

        if ( ensembletypelist[iexpid] == 'minmax' ) :
            ax.fill_between(datalist[iexpid]['latitude'], factor * datalist[iexpid]['valuelist_min'], factor * datalist[iexpid]['valuelist_max'], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme), alpha=0.2)

#
#   PLOT X- AND Y-AXIS   
#    ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed') # not needed
#    if ( var != 'T' ) : ax.axvline(0,lw=1.0,color='tab:gray',linestyle='dashed')
            
    ax.legend(fontsize=7)

#    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season
#
    print('*** plotzonalmeanline ***')
#
    if ( figlayout.plotdir == None ) : path='/projects/NS9560K/users/olivie/plots'
    else                             : path=figlayout.plotdir
#
    fig.savefig(path+'/'+filename+'.ps',  bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.png', bbox_inches='tight')
#
    plt.close(fig)






