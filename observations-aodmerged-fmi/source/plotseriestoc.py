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

def plotseriestoc(expidlist, xdiff, vartype, code, data, colorlist, linestylelist, legendlist, dolegendlist, figlayout) :
#----------------
#
    print('+++ plotseriestoc +++')
#
#       
    nexpid=len(expidlist)

    var=data[0]['var']

    fig,ax =plt.subplots()     
#
    ax.set_xlabel('Time [year]')
    ax.set_ylabel('[DU]')
    ax.set_title('Total ozone column')
#
    for iexpid in range (0,nexpid) :
#
        x=data[iexpid]['timelist'] 

        if   ( vartype == 'var'  ) : y=data[iexpid]['valuelist']
        elif ( vartype == 'mask' ) : y=data[iexpid]['masklist']
        else : 
            print('No vartype recognized : ', vartype)
            quit()

        ax.plot(x, y, label=getidlregion.getidlregion(legendlist[iexpid]), color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme), linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid],linestylescheme='default'))

    ax.legend()
#
    path='/projects/NS9560K/users/olivie/plots/toccopernicus'
    path='/datalake/NS2345K/olivie/plots/toccopernicus'
#
    fig.savefig(path+'/toccopernicus_'+var+'_'+vartype+'_'+code+'.ps',  bbox_inches='tight')
    fig.savefig(path+'/toccopernicus_'+var+'_'+vartype+'_'+code+'.png', bbox_inches='tight')
