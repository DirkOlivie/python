import matplotlib.pyplot as plt
import numpy as np
import math
import os
import scipy.stats

#from sklearn.linear_model import LinearRegression

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits
import getlinearregression
import getcolor

'''
    MODIFICATIONS

    INFO
        https://matplotlib.org/stable/api/markers_api.html [dots linestyle]
        https://realpython.com/numpy-scipy-pandas-correlation-python/#example-numpy-correlation-calculation [correlations in python]
        https://www.statsdirect.com/help/basics/p_values.htm [p-values]

'''

def plotscatterseries(xdata,ydata,freqtypeX,freqtypeY,typevarX,typevarY,legendlist,colorlist,dolinearregressionlist,description,figlayout,code) :
#--------------------
    '''
    INPUT
        xdata : list of dictionaries; dictionary contains 'variable', 'timelist', 'valuelist', 'units'
        ydate : list of dictionaries; dictionary contains 'variable', 'timelist', 'valuelist', 'units'
        freqtypeX : NOT USED
        freqtypeY : NOT USED
        typevarX  : used in filename for plotting
        typevarY  : used in filename for plotting
        legendlist
        colorlist
        dolinearregressionlist : NOT USED
        description : NOT USED
        code 

    MODIFICATIONS
        (2026-09-11) added figlayout

    '''
#    
    print('+++ plotscatterseries +++')
#
    nexpid=len(xdata)

    if ( len(xdata) != len(ydata) ) : 
        print('Number of x data sets : '+string(len(xdata)))
        print('Number of y data sets : '+string(len(ydata)))

        quit()
#
    print(xdata[0]['variable'])
    print(ydata[0]['variable'])
#
#   fig, ax = plt.subplots(figsize=[8,4],dpi=100)
    fig, ax = plt.subplots(figsize=[6,4],dpi=100)

    xlabel=getidlvar.getidlvar(xdata[0]['variable'])+' ['+getidlunits.getidlunits(xdata[0]['units'])+']' # use information from first experiment
    ylabel=getidlvar.getidlvar(ydata[0]['variable'])+' ['+getidlunits.getidlunits(ydata[0]['units'])+']' # use information from first experiment

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel) 
#    ax.set_title('What can I put here ...')                  # use first experiment to obtain units

#   plot the individual lines
    for iexpid in range(0,nexpid) : 

        ntime=len(xdata[iexpid]['timelist'])
        x=xdata[iexpid]['valuelist']
        y=ydata[iexpid]['valuelist']
#
#        ax.plot(x, y, label=legendlist[iexpid], marker='o')      # label from legendlist   
        ax.scatter(x, y, label=legendlist[iexpid], marker='o', color=getcolor.getcolor(color=colorlist[iexpid]), s=20)      # label from legendlist   
#      
        print(legendlist[iexpid])
        
        print(scipy.stats.pearsonr(x, y))
        print(scipy.stats.spearmanr(x, y))
        print(scipy.stats.kendalltau(x, y))
#
        print(scipy.stats.linregress(x, y))  
        print(getlinearregression.getlinearregression(x=x,y=y))   
#
#       plot regression line
        regr=getlinearregression.getlinearregression(x=x, y=y, imposethroughorigin=None)
        
        xlow=np.min(x)
        xhgh=np.max(x)
        
        xseq = np.linspace(xlow,xhgh,num=100)

#        ax.plot(xseq, regr["alpha"] + regr["beta"] * xseq, lw=1.0, color=getcolor.getcolor(color=colorlist[iexpid]))

#   add legend
    ax.legend()
#
#   lin/log scale for y-axis
    if ( figlayout.xtype == 'log' ) :
        ax.set_xscale('log')
    if ( figlayout.ytype == 'log' ) :
        ax.set_yscale('log')

#   PLOT 1:1 line
#    ax.plot([xlow,xhgh],[xlow,xhgh],color='tab:gray',linestyle='dashed')


#   PLOTS X- and Y-AXIS
#    ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed')
#    ax.axvline(0,lw=1.0,color='tab:gray',linestyle='dashed')

#   plot directory
    if ( figlayout.plotdir == None ) :
#        path='/projects/NS2345K/www/people/olivie/plots/'+code
#       path='/projects/NS2345K/www/people/olivie/plots'
        path='/projects/NS9560K/users/olivie/plots'
    else :
        path=figlayout.plotdir

    if  not os.path.isdir(path) : os.mkdir(path)

    filename='scatterseries_'+xdata[0]['variable']+'_'+typevarX+'_'+ydata[0]['variable']+'_'+typevarY+'_x'+figlayout.xtype+'_y'+figlayout.ytype+'_'+code

    fig.savefig(path+'/'+filename+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.png', bbox_inches='tight')
#
    print('--- plotscatterseries ---')
