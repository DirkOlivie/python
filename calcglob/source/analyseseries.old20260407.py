import numpy as np

import readseries
import fillstatistics
import fillensemblestatistics
import plotseries
import massageseries

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getparentexpidinfo
import getexpidsplit

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents


def analyseseries(expidlist, refidlist, refid2list, refid3list, wlist, legendlist, shiftlist, smoothlist, variablelist, freqtype, typevarlist, code, figlayout,dorefaverage=None,colorlist=None,linestylelist=None) :
#----------------

    '''
    INPUT
        expid='FC2010climo_f19_20210204_test1'
        variable='cb_O3'
        freqtype='annavg'
        typevar='glob'
    '''

    nexpid=len(expidlist)

    print(len(expidlist))
    print(len(refidlist))
    print(len(variablelist))
    print(len(typevarlist))

    
#   I. read all experiments     
    for iexpid in range(0,nexpid) :

        a=readseries.readseries(expid=expidlist[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])
        a['valuelist'] = a['valuelist'] * wlist[0]
#

#       if ( wlist[1] != 0. ) : 
        if ( 0. == 1. ) :


            if ( ( expidlist[iexpid] == 'NorESM2-LM_ssp245_r1i1p1f1_gn' or expidlist[iexpid] == 'NorESM2-MM_ssp245_r1i1p1f1_gn' )
             and ( variablelist[iexpid] == 'tasmin' or variablelist[iexpid] == 'tasmax' or variablelist[iexpid] == 'tasmaxmin' ) ) :
                freqfile='daily'  

            else : 
                freqfile='monthly'

#           look for corresponding information only in first component : tasmaxmin = tasmax - tasmin -> only look into tasmax
            complist, weightlist = getvarcomponents.getvarcomponents(var=variablelist[iexpid])

            historicalinfo=getparentexpidinfo.getparentexpidinfo(expid=expidlist[iexpid], var=complist[0], freqfile=freqfile)       # historical <-- ssp245
            piControlinfo=getparentexpidinfo.getparentexpidinfo(expid=historicalinfo['expid'], var=complist[0], freqfile=freqfile)  # piControl <-- historical
#
            print('piControlinfo[branchyear]')
            print(piControlinfo['branchyear'])

            c=readseries.readseries(expid=piControlinfo['expid'], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid]) # read raw piControl

            print('+++ a +++')
            print(a['ntime'])
            print(a['yearlist'][0])

            print('+++ c +++')
            print(c['ntime'])
            print(c['yearlist'][0])

            c=massageseries.massageseries(data=c,year0=piControlinfo['branchyear']+165,nyear=a['ntime']/12)                          # historical branch-off point + 165 year
#
            print('+++ c +++')
            print(c['ntime'])
            print(c['yearlist'][0])

            a['valuelist'] = a['valuelist'] - c['valuelist']
#
#       reference : always start from first year 
        if ( wlist[1] != 0. ) :

            c=readseries.readseries(expid=refidlist[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])

#           average
            if ( dorefaverage != None ) : c['valuelist'][:] = np.mean(c['valuelist'])

            print(len(c['yearlist'])) 

#            c=massageseries.massageseries(data=c,year0=c['yearlist'][0],nyear=a['ntime']/12)  # for DUNCAN
#           c=massageseries.massageseries(data=c,year0=c['yearlist'][1300],nyear=a['ntime']/12)  

            a['valuelist'] = a['valuelist'] + c['valuelist'] * wlist[1]

#       reference 2 :
        if ( refid2list != None and wlist[2] != 0.)  :

            c = readseries.readseries(expid=refid2list[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])
            a['valuelist'] = a['valuelist'] + c['valuelist'] *wlist[2]

#       reference 3 :
        if ( refid3list != None and wlist[3] != 0.)  :

            c = readseries.readseries(expid=refid3list[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])
            a['valuelist'] = a['valuelist'] + c['valuelist'] *wlist[3]

#

#       all piControl should be plotted from same starting point (=0); now spans from year 1 to year 5000
#        splitinfo=getexpidsplit.getexpidsplit(expidlist[iexpid])
#
#        model=splitinfo['model']
#        scenario=splitinfo['scenario']
#        realisation=splitinfo['realisation']
#        grid=splitinfo['grid']
#
#        if ( scenario == 'piControl' ) : 
#            a['yearlist'][:] = a['yearlist'][:] - a['yearlist'][0] 
#        i0=(2010-1850)*12
#        i1=(2249-1850+1)*12
#
#        a['valuelist'][:] = a['valuelist'][:] - np.mean(a['valuelist'][i0:i1])

        if iexpid==0 :
            a_all=[a]
        else :
            a_all.append(a)
#
#   II. do all the statistics
    if ( freqtype == 'monthly' ) : # no statistics needed
        b_all = a_all

    else :
        for iexpid in range(0,nexpid) :
            b=fillstatistics.fillstatistics(data=a_all[iexpid], freqtype=freqtype)

            if iexpid==0 :
                b_all=[b]
            else :
                b_all.append(b)
#
#   III. do all the min/max/mean/median calculations
    estimatorlist=['mean','min','max','median','NorESM2-LM_ssp245_r1i1p1f1_gn']
    nestimator=len(estimatorlist)
    for iestimator in range(0,nestimator) :
        d=fillensemblestatistics.fillensemblestatistics(data=b_all, estimator=estimatorlist[iestimator])

        if iestimator==0 :
            d_all=[d]
        else :
            d_all.append(d)

#  IV. do all the plotting   
    print(d_all)
    plotseries.plotseries(data=b_all,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar=typevarlist[0],code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

#   V.plot min/max/mean/...
#    plotseries.plotseries(data=d_all,legendlist=estimatorlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar=typevar,code=code+'ensemblemean')
