import getsondelist
import sondelist2frequency
import frequencytransformation

import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getcolor

'''
    MODIFICATIONS
        (2023-10-20) Adding colorlist and colorscheme

'''

def plotobservationfrequency(stationlist, representationtype, figlayout) :
#---------------------------
#
    print('+++ plotobservationfrequency +++')
#
#       
    nstation=len(stationlist)

    fig,ax =plt.subplots()     

    for istation in range (0,nstation) :
#
        station=stationlist[istation]
#
#       read sondelist
        sondelist=getsondelist.getsondelist(station = station)

#       convert to frequencylist
        tmp=sondelist2frequency.sondelist2frequency(sondelist=sondelist)

#       convert to desired representationtype
        data=frequencytransformation.frequencytransformation(D=tmp, representationtype=representationtype) 

        ax.plot(data['timelist'], data['valuelist'], label=station, color=getcolor.getcolor(color=istation,colorscheme=figlayout.colorscheme))

    ax.legend()
#
    path='/projects/NS9560K/users/olivie/plots/shadoz'
#
    fig.savefig(path+'/shadozfrequency_'+representationtype+'.ps',  bbox_inches='tight')
    fig.savefig(path+'/shadozfrequency_'+representationtype+'.png', bbox_inches='tight')
