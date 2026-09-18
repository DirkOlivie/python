import matplotlib.pyplot as plt
import numpy as np
import math
import os

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits

'''
    MODIFICATIONS
        (2022-07-12) plotdigital
'''

def plotdigital(valuelist,varlist,xlist, unitslist,legendlist,code) :
#------------------------------------------------------------------
#    
    print('+++ plotdigital +++')
#
    nvar=len(varlist)
    nx=len(xlist)    

    fig, ax = plt.subplots(figsize=[8,4],dpi=100)

    ax.set_xlabel('Fraction')
    ax.set_ylabel('['+getidlunits.getidlunits(units=unitslist[0])+']') # use first experiment to obtain units
#   ax.set_title(getidlvar.getidlvar(var=varlist[0]))             # use first experiment to obtain var name

#   plot the individual lines
    for ivar in range(0,nvar) :
        ax.plot(xlist, valuelist[:,ivar],label=getidlvar.getidlvar(var=varlist[ivar]))      # label from legendlist   

#   ax.set_xticks(xlist,legendlist)
    ax.set_xticks(xlist)
#    ax.xticks(xlist,labels)

    plt.legend()

#   plt.show()


#   plot directory
#   path='/projects/NS2345K/www/people/olivie/plots/'+code
    path='/projects/NS2345K/www/people/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/digital_'+varlist[0]+'_'+code+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/digital_'+varlist[0]+'_'+code+'.png', bbox_inches='tight')

    print('--- plotdigital ---')
