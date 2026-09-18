import matplotlib.pyplot as plt
import os

import convertdata2histogram

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits

'''
    MODIFICATIONS
'''

def plotdistributionhistogram(data,legendlist,figlayout,code) :
#----------------------------
# 
    '''
    INPUT
        data is a structure containing the different experiments

    '''

    print('+++ plotdistributionhistogram +++')
#
    nexpid=len(data)

    variable=data[0]['variable']            # use first experiment to obtain units
    units=data[0]['units']
#
#    fig,ax =plt.subplots()     
    fig, ax = plt.subplots(figsize=[8,4],dpi=100)

    ax.set_xlabel(getidlvar.getidlvar(var=variable)+' ['+getidlunits.getidlunits(units=units)+']') # use first experiment to obtain units
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')                  # use first experiment to obtain units
#
#   plot the individual lines
    for iexpid in range(0,nexpid) : 

        tmp=convertdata2histogram.convertdata2histogram(data=data[iexpid]) 

        ax.plot(tmp['xlist'], tmp['valuelist'],  label=legendlist[iexpid])      # label from legendlist   
   
        print(legendlist[iexpid])

    ax.legend()

#   plot x-axis
#    ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed')
    if ( figlayout.ytype == 'log' ) :
        ax.set_yscale('log')

#   plot directory
#   path='/projects/NS2345K/www/people/olivie/plots/'+code
#   path='/projects/NS2345K/www/people/olivie/plots'
#   path='/datalake/NS2345K/olivie/plots'
    path='/projects/NS9560K/users/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/distributionhistogram_'+data[0]['variable']+'_'+figlayout.code+'_'+code+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/distributionhistogram_'+data[0]['variable']+'_'+figlayout.code+'_'+code+'.png', bbox_inches='tight')

    print('--- plotdistributionhistogram ---')
