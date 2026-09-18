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
import getcolor
import getlinestyle
import getmarker
import getlinearregression
import getprefix
import getstandardunits
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition


'''
    MODIFICATIONS

    INFO
        https://matplotlib.org/stable/api/markers_api.html [dots linestyle]
        https://realpython.com/numpy-scipy-pandas-correlation-python/#example-numpy-correlation-calculation [correlations in python]
        https://www.statsdirect.com/help/basics/p_values.htm [p-values]
    
    EXAMPLE OF SCATTER PLOTS WITH ERRORBARS


'''

def plotscatter(xdata,ydata,legendlist,colorlist,linestylelist,freqtypeX,freqtypeY,typevarXlist,typevarYlist,regressionlist,code,figlayout) :
#-------------------------------------------------------------------------------------------------------------------------------------------
#    
    '''
    INPUTDATA
        xdata
        ydata
        legendlist
        colorlist
        linestylelist
        freqtypeX
        freqtypeY
        typevarX
        typevarY
        regressionlist : is it participating in regression
        code
        figlayout
    '''

    print('+++ plotscatter +++')
#
    nexpid=len(xdata)

#   CHECK NUMBER OF X- AND Y-DATAPOINTS
    if ( len(xdata) != len(ydata) ) : 
        print('Number of x data sets : '+string(len(xdata)))
        print('Number of y data sets : '+string(len(ydata)))

        quit()

#   FILENAME FOR FIGURE
    filename='scatter_'+xdata[0]['variable']+'_'+typevarXlist[0]+'_'+ydata[0]['variable']+'_'+typevarYlist[0]+'_'+code

#   Title of figure can contain a), b), ...
    prefix=getprefix.getprefix(filename=filename)
#
    fig, ax = plt.subplots(figsize=figlayout.figsize,dpi=100) # figsize=[6,6]

    xlabel=getidlvar.getidlvar(xdata[0]['variable'])+' ['+getidlunits.getidlunits(xdata[0]['units'])+']' # use information from first experiment
#   ylabel=getidlvar.getidlvar(ydata[0]['variable'])+' ['+getidlunits.getidlunits(ydata[0]['units'])+']' # use information from first experiment
#   title=prefix+getidlvar.getidlvar(ydata[0]['variable'])
    title='Offset : '
    ylabel=prefix+getidlvar.getidlvar(ydata[0]['variable'])+' ['+getidlunits.getidlunits(ydata[0]['units'])+']' # use information from first experiment

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel) 
#    ax.set_title(title)                  # use first experiment to obtain units

#   plot the individual lines
#    print('x --- y --- xerr --- yerr')
    xlow =  1.e20
    xhgh = -1.e20
    ylow =  1.e20 
    yhgh = -1.e20

    xlist=np.zeros(nexpid)     
    ylist=np.zeros(nexpid)

#   INTIALISE csv file
    if ( figlayout.csvoutput == True ) :
        csvpath='/projects/NS9560K/users/olivie/csv'
        csvfile=csvpath+'/'+filename+'.csv'
        fcsv=open(csvfile,'w')
        fcsv.write('Experiment,Line,x,xerr,y,yerr')  # title line
        fcsv.write('\n')
        fcsv.write(',,'+getstandardunits.getstandardunits(units=xdata[0]['units']) \
                   +','+getstandardunits.getstandardunits(units=xdata[0]['units']) \
                   +','+getstandardunits.getstandardunits(units=ydata[0]['units']) \
                   +','+getstandardunits.getstandardunits(units=ydata[0]['units'])) # line with units
        fcsv.write('\n')

#   LOOP OVER ALL EXPERIMENTS
    for iexpid in range(0,nexpid) : 

#       ntime=len(xdata[iexpid]['timelist'])
        x=xdata[iexpid]['Ex']
        y=ydata[iexpid]['Ex']

        xerr=xdata[iexpid]['error']
        yerr=ydata[iexpid]['error']  
#
#       put error bars to zero
        xerr=xdata[iexpid]['error']*0.
        yerr=ydata[iexpid]['error']*0.


        if ( legendlist[iexpid] == '' ) : ax.errorbar(x, y, xerr=xerr, yerr=yerr,                           color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),marker=getmarker.getmarker(marker=linestylelist[iexpid]))      # label from legendlist   
        else                            : ax.errorbar(x, y, xerr=xerr, yerr=yerr, label=legendlist[iexpid], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),marker=getmarker.getmarker(marker=linestylelist[iexpid]))      # label from legendlist   

#       FOR LATER FINDING THE MIN/MAX      
        xlow=np.min([xlow,x-xerr])
        xhgh=np.max([xhgh,x+xerr])
#
        ylow=np.min([ylow,y-xerr])
        yhgh=np.max([yhgh,y+xerr])

#       FOR LATER DOING REGRESSION
        xlist[iexpid] = x
        ylist[iexpid] = y
#
#       print(legendlist[iexpid], x, y, xerr, yerr)
        
#        print(scipy.stats.pearsonr(x, y))
#        print(scipy.stats.spearmanr(x, y))
#        print(scipy.stats.kendalltau(x, y))
#
#        print(scipy.stats.linregress(x, y))  
#        print(getlinearregression.getlinearregression(x=x,y=y))   
#
#       write to csv-file
        if ( figlayout.csvoutput == True ) :

            fcsv.write(experimentdefinition.getexpidinfo(expid=xdata[iexpid]['expid'])['model'])
            fcsv.write(',')
            fcsv.write(str(linestylelist[iexpid]))
            fcsv.write(',')
            fcsv.write(str(x))
            fcsv.write(',')
            fcsv.write(str(xerr))
            fcsv.write(',')
            fcsv.write(str(y))
            fcsv.write(',')
            fcsv.write(str(yerr))
            fcsv.write('\n')

#   close csv file
    if ( figlayout.csvoutput == True ) :
        fcsv.close()

#   IMPOSE the origin to be part of it
    xlow=np.min([0.,xlow])
    xhgh=np.max([0.,xhgh])

    ylow=np.min([0.,ylow])
    yhgh=np.max([0.,yhgh])

#    x0=xlow - ( xhgh - xlow ) * 0.05
#    x1=xhgh + ( xhgh - xlow ) * 0.05 
#    y0=ylow - ( yhgh - ylow ) * 0.05
#    y1=yhgh + ( yhgh - ylow ) * 0.05 

    x0=xlow
    x1=xhgh
    y0=ylow
    y1=yhgh

    print('x0, x1, y0, y1 : ', x0, x1, y0, y1)

#    plt.xlim([x0,x1])
#    plt.ylim([y0,y1]) 
#    plt.ylim([-0.0008,0.0008]) # ne16pg3
#    plt.ylim([-0.004,0.004])   # ne30pg3

#   PLOT REGRESSION LINE
#   regr=getlinearregression.getlinearregression(x=xlist, y=ylist, imposethroughorigin=True)
#   regr=getlinearregression.getlinearregression(x=xlist, y=ylist, imposethroughorigin=True)

    regressionvaluelist=list(set(regressionlist))

    for regressionvalue in regressionvaluelist :

        if ( regressionvalue >= 0 ) :    

            regr=getlinearregression.getlinearregression(x=xlist[np.array(regressionlist)==regressionvalue], y=ylist[np.array(regressionlist)==regressionvalue], imposethroughorigin=None)

            xseq = np.linspace(xlow,xhgh,num=100)
            ax.plot(xseq, regr["alpha"] + regr["beta"] * xseq, color='tab:gray', lw=1.0, ls=getlinestyle.getlinestyle(linestyle=regressionvalue))    

            title = title+' '+str("%.3f"% (-regr["alpha"]/regr["beta"]))

    ax.set_title(title)


#   add legend
    ax.legend(fontsize=10.0)

#   PLOTS X- and Y-AXIS
    ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed')
    ax.axvline(0,lw=1.0,color='tab:gray',linestyle='dashed')

#   plot directory
#   path='/projects/NS2345K/www/people/olivie/plots/'+code
#   path='/projects/NS2345K/www/people/olivie/plots'
    path='/projects/NS9560K/users/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

#    fig.savefig(path+'/scatter_'+xdata[0]['variable']+'_'+typevarX+'_'+ydata[0]['variable']+'_'+typevarY+'_'+code+'.ps' , bbox_inches='tight')
#    fig.savefig(path+'/scatter_'+xdata[0]['variable']+'_'+typevarX+'_'+ydata[0]['variable']+'_'+typevarY+'_'+code+'.png', bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.png', bbox_inches='tight')
#
    print('--- plotscatter ---')
