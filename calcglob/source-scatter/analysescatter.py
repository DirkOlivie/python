import plotscatter

import numpy as np

import sys

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import readseries
import shortenseries
import fillstatistics

#sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
#import getparentexpidinfo
#import getexpidsplit

#sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
#import getvarcomponents


def analysescatter(expXlist,refXlist,refX2list,refX3list,expXyear0list,expXyear1list,refXyear0list,refXyear1list,seasonXlist,wXlist,varXlist,typevarXlist, \
                   expYlist,refYlist,refY2list,refY3list,expYyear0list,expYyear1list,refYyear0list,refYyear1list,seasonYlist,wYlist,varYlist,typevarYlist, \
                   legendlist,colorlist,linestylelist,regressionlist,code,figlayout) :
#-----------------------

    '''
    MODIFICATIONS
        (2024-10-27) creation

    INPUT
    '''

    nexpid=len(expXlist)

    xdata=[] # seperate elements will be statistical information of each exeperiment
    ydata=[] 

#    print('expXlist : ', expXlist)
#    print('varXlist : ', varXlist)
#    print('typevarXlist : ', typevarXlist)
#    print('expXyear0list : ', expXyear0list)
#    print('expXyear1list : ', expXyear1list)

# read all experiments     
    for iexpid in range(0,nexpid) :

#       X-VALUES
#       exp
        expX=shortenseries.shortenseries(data=readseries.readseries(expid=expXlist[iexpid], variable=varXlist[iexpid], typevar=typevarXlist[iexpid]), year0=expXyear0list[iexpid],year1=expXyear1list[iexpid])
#   
#       ref
        refX=shortenseries.shortenseries(data=readseries.readseries(expid=refXlist[iexpid], variable=varXlist[iexpid], typevar=typevarXlist[iexpid]), year0=refXyear0list[iexpid],year1=refXyear1list[iexpid])
        expX['valuelist'] = wXlist[0] * expX['valuelist'] \
                          + wXlist[1] * refX['valuelist']
#       
#       ref2    
        if ( refX2list != None and wXlist[2] != 0. ) :
            refid=refX2list[iexpid]
            if ( refid != '' ) : 
                refX=shortenseries.shortenseries(data=readseries.readseries(expid=refid, variable=varXlist[iexpid], typevar=typevarXlist[iexpid]), year0=expXyear0list[iexpid],year1=expXyear1list[iexpid]) 
                expX['valuelist'] = expX['valuelist'] \
                                  + refX['valuelist'] * wXlist[2]

#       ref3    
        if ( refX3list != None and wXlist[3] != 0. ) :
            refid=refX3list[iexpid]
            if ( refid != '' ) :
                refX=shortenseries.shortenseries(data=readseries.readseries(expid=refid, variable=varXlist[iexpid], typevar=typevarXlist[iexpid]), year0=expXyear0list[iexpid],year1=expXyear1list[iexpid])           
                expX['valuelist'] = expX['valuelist'] \
                                  + refX['valuelist'] * wXlist[3]

        statX = fillstatistics.fillstatistics(data=expX, freqtype=seasonXlist[iexpid]) # season information is used

#       Y-VALUES
#       exp
        expY=shortenseries.shortenseries(data=readseries.readseries(expid=expYlist[iexpid], variable=varYlist[iexpid], typevar=typevarYlist[iexpid]), year0=expYyear0list[iexpid],year1=expYyear1list[iexpid])
#       ref
        refY=shortenseries.shortenseries(data=readseries.readseries(expid=refYlist[iexpid], variable=varYlist[iexpid], typevar=typevarYlist[iexpid]), year0=refYyear0list[iexpid],year1=refYyear1list[iexpid])
        expY['valuelist'] = wYlist[0] * expY['valuelist'] \
                          + wYlist[1] * refY['valuelist']
#
#       ref2
        if ( refY2list != None and wYlist[2] != 0. ) :
            refid=refY2list[iexpid]
            if ( refid != '' ) :
                refY=shortenseries.shortenseries(data=readseries.readseries(expid=refid, variable=varYlist[iexpid], typevar=typevarYlist[iexpid]), year0=expYyear0list[iexpid],year1=expYyear1list[iexpid])           
                expY['valuelist'] = expY['valuelist'] \
                                  + refY['valuelist'] * wYlist[2]

#       ref3    
        if ( refY3list != None and wYlist[3] != 0. ) :
            refid=refY3list[iexpid]
            if ( refid != '' ) :
                refY=shortenseries.shortenseries(data=readseries.readseries(expid=refid, variable=varYlist[iexpid], typevar=typevarYlist[iexpid]), year0=expYyear0list[iexpid],year1=expYyear1list[iexpid])
                expY['valuelist'] = expY['valuelist'] \
                                  + refY['valuelist'] * wYlist[3]

#
        statY = fillstatistics.fillstatistics(data=expY, freqtype=seasonYlist[iexpid]) # season information is used

        xdata.append(statX)
        ydata.append(statY)
#
# do all the plotting   
    plotscatter.plotscatter(xdata=xdata,ydata=ydata,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,freqtypeX=seasonXlist[0],freqtypeY=seasonYlist[0],typevarXlist=typevarXlist,typevarYlist=typevarYlist,regressionlist=regressionlist,code=code,figlayout=figlayout)
