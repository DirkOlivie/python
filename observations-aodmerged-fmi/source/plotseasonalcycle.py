import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getcolor
import getlinestyle
import getidlregion

'''
    MODIFICATIONS
        (2023-10-20) Adding colorlist and colorscheme

'''

def plotseasonalcycle(expidlist, xdiff, vartype, code, data, colorlist, linestylelist, legendlist, dolegendlist, figlayout) :
#--------------------
#
    print('+++ plotseasonalcycle +++')
#
#       
    nexpid=len(expidlist)
#
    var=data[0]['var']
#
    fig,ax =plt.subplots()     
#
    ax.set_xlabel('Time [month]')
    ax.set_ylabel('[DU]')
    ax.set_title('Total ozone column')
#
    for iexpid in range (0,nexpid) :
#
        x=data[iexpid]['timelist'] 
#
        y=data[iexpid]['Ex']
#
        ax.plot(x, y, label=getidlregion.getidlregion(legendlist[iexpid]), color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid],linestylescheme='default'))
#
    ax.legend()
#
    path='/projects/NS9560K/users/olivie/plots/toccopernicus'
    path='/datalake/NS2345K/olivie/plots/toccopernicus'
#
    fig.savefig(path+'/toccopernicus_'+var+'_'+vartype+'_'+code+'_seasonal_cycle.ps',  bbox_inches='tight')
    fig.savefig(path+'/toccopernicus_'+var+'_'+vartype+'_'+code+'_seasonal_cycle.png', bbox_inches='tight')
