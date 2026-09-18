import numpy as np

import readseries
import fillstatistics
import fillmemberstatistics
import getmemberlist
import plotseries
#import massageseries

import sys
#sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
#import getparentexpidinfo
#import getexpidsplit

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents


def analyseseries_internal(expidlist, refidlist, refid2list, refid3list, wlist, shiftlist, smoothlist, variablelist, freqtype, typevarlist,dorefaverage,ensembletypelist) :
#-------------------------

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
    print(len(ensembletypelist))

    
#   I. read all experiments and do statistics     

    b_all = []
    for iexpid in range(0,nexpid) :

#       SINGLE SIMULATION
        if ( ensembletypelist[iexpid] == '' ) :

#           I.1 read experiment 
            a=readseries.readseries(expid=expidlist[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])
            a['valuelist'] = a['valuelist'] * wlist[0]
#
#           reference : always start from first year 
            if ( wlist[1] != 0. ) :

                c=readseries.readseries(expid=refidlist[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])

#               average
                if ( dorefaverage != None ) : c['valuelist'][:] = np.mean(c['valuelist'])

                a['valuelist'] = a['valuelist'] + c['valuelist'] * wlist[1]

#           reference 2 :
            if ( refid2list != None and wlist[2] != 0.)  :

                c = readseries.readseries(expid=refid2list[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])
                a['valuelist'] = a['valuelist'] + c['valuelist'] *wlist[2]

#           reference 3 :
            if ( refid3list != None and wlist[3] != 0.)  :

                c = readseries.readseries(expid=refid3list[iexpid], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])
                a['valuelist'] = a['valuelist'] + c['valuelist'] *wlist[3]

#           II. do all the statistics
            if ( freqtype == 'monthly' ) : # no statistics needed
                b_all.append(a)
            else :
                b=fillstatistics.fillstatistics(data=a, freqtype=freqtype)
                b_all.append(b)
#
#       ENSEMBLE
        else : 

#           list of all experiment members
            expmemberlist = getmemberlist.getmemberlist(expid=expidlist[iexpid])
            nexpmember=len(expmemberlist)

#           list of all reference members
            refmemberlist = getmemberlist.getmemberlist(expid=refidlist[iexpid])
            nrefmember=len(refmemberlist)

            d_all=[]
                
#           read all ensemblemembers
            for iexpmember in range(nexpmember) :
                for irefmember in range(nrefmember) :
                    a = readseries.readseries(expid = expmemberlist[iexpmember], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])                 
                    c = readseries.readseries(expid = refmemberlist[irefmember], variable=variablelist[iexpid], freqtype=freqtype, typevar=typevarlist[iexpid])                 
                    if ( dorefaverage != None ) : c['valuelist'][:] = np.mean(c['valuelist'])


                    a['valuelist'] = a['valuelist'] * wlist[0] + c['valuelist'] * wlist[1]

#                   do individual statistics
                    d=fillstatistics.fillstatistics(data=a, freqtype=freqtype)                    

                    d_all.append(d)
#
#           make ensemble statistics of     

            b = fillmemberstatistics.fillmemberstatistics(data=d_all) 

            b_all.append(b)




#           list of all reference ensemble members

#           read all reference ensemblemembers

#           make all combinations

#           for each combination make statistics

#           do the final fill


            




#   III. do all the min/max/mean/median calculations
#    estimatorlist=['mean','min','max','median','NorESM2-LM_ssp245_r1i1p1f1_gn']
#    nestimator=len(estimatorlist)
#    for iestimator in range(0,nestimator) :
#        d=fillensemblestatistics.fillensemblestatistics(data=b_all, estimator=estimatorlist[iestimator])
#
#        if iestimator==0 :
#            d_all=[d]
#        else :
#            d_all.append(d)

#  IV. do all the plotting   
    return b_all


def analyseseries(expidlist, refidlist, refid2list, refid3list, wlist, legendlist, shiftlist, smoothlist, variablelist, freqtype, typevarlist, code, figlayout,dorefaverage=None,colorlist=None,linestylelist=None,linewidthlist=None,ensembletypelist=None) :
#----------------

    '''
    INPUT
    '''

    nexpid=len(expidlist)

    print(len(expidlist))
    print(len(refidlist))
    print(len(variablelist))
    print(len(typevarlist))
    print(len(ensembletypelist))

    
#   I. read all experiments and do statistics     

    b_all = analyseseries_internal(expidlist=expidlist, refidlist=refidlist, refid2list=refid2list, refid3list=refid3list, wlist=wlist, shiftlist=shiftlist, smoothlist=smoothlist, variablelist=variablelist, freqtype=freqtype, typevarlist=typevarlist,dorefaverage=dorefaverage,ensembletypelist=ensembletypelist)

#  IV. do all the plotting   
#    print(d_all)
    plotseries.plotseries(data=b_all,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar=typevarlist[0],code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)
