import plotexpdependence

import numpy as np

import sys

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import readseries
import shortenseries
import fillstatistics

def analyseexpdependence(expidlist,refidlist, \
                         expyear0list,expyear1list,refyear0list,refyear1list,seasonlist, \
                         wlist, \
                         varlist,typevarlist,legendlist,colorlist,linestylelist, \
                         xvaluelist, xtitle, xunits, \
                         description,code,figlayout) :
#-----------------------

    '''
    MODIFICATIONS
        (2025-02-05) creation

    INPUT
    '''

    print('+++ analyseexpdependence +++')
    print('varlist : ', varlist)
    print('typevarlist : ', typevarlist)

    nexpid=len(expidlist)
    nvar=len(varlist)


    data=[]

# read all variables
    for ivar in range(0,nvar) :
        
        vardata=[]

        for iexpid in range(0,nexpid) :

#           exp
            expdata=shortenseries.shortenseries(data=readseries.readseries(expid=expidlist[iexpid], variable=varlist[ivar], typevar=typevarlist[ivar]), year0=expyear0list[iexpid],year1=expyear1list[iexpid])
#   
#           ref
            refdata=shortenseries.shortenseries(data=readseries.readseries(expid=refidlist[iexpid], variable=varlist[ivar], typevar=typevarlist[ivar]), year0=refyear0list[iexpid],year1=refyear1list[iexpid])

            expdata['valuelist'] = wlist[0] * expdata['valuelist'] \
                                 + wlist[1] * refdata['valuelist']
#       
            stat = fillstatistics.fillstatistics(data=expdata, freqtype=seasonlist[iexpid]) # season information is used


            vardata.append(stat) # all different experiments are gathered

        data.append(vardata)   
#
# do all the plotting   
    plotexpdependence.plotexpdependence(data=data, freqtypelist=seasonlist, \
                                        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
                                        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
                                        description=description,code=code,figlayout=figlayout)
