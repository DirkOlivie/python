import plotscatterseries

import sys

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import readseries
import shortenseries
import fitconstantseries
import fillstatistics

sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getparentexpidinfo
import getexpidsplit

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents


def analysescatterseries(expXlist,refXlist,expXyear0list,expXyear1list,refXyear0list,refXyear1list,seasonXlist,wXlist,varX,typevarX, \
                         expYlist,refYlist,expYyear0list,expYyear1list,refYyear0list,refYyear1list,seasonYlist,wYlist,varY,typevarY, \
                         legendlist,colorlist,dolinearregressionlist, \
                         description,code) :
#-----------------------

    '''
    INPUT
    '''

    nexpid=len(expXlist)

    xdata=[]
    ydata=[]

# read all experiments     
    for iexpid in range(0,nexpid) :

#       x-values
        expX=shortenseries.shortenseries(data=readseries.readseries(expid=expXlist[iexpid], variable=varX, typevar=typevarX), year0=expXyear0list[iexpid],year1=expXyear1list[iexpid])
        refX=shortenseries.shortenseries(data=readseries.readseries(expid=refXlist[iexpid], variable=varX, typevar=typevarX), year0=refXyear0list[iexpid],year1=refXyear1list[iexpid])
        refX=fitconstantseries.fitconstantseries(data=refX)

        expX['valuelist'] = wXlist[0] * expX['valuelist'] \
                          + wXlist[1] * refX['valuelist']
        statX = fillstatistics.fillstatistics(data=expX, freqtype=seasonXlist[iexpid])

#       y-values
        expY=shortenseries.shortenseries(data=readseries.readseries(expid=expYlist[iexpid], variable=varY, typevar=typevarY), year0=expYyear0list[iexpid],year1=expYyear1list[iexpid])
        refY=shortenseries.shortenseries(data=readseries.readseries(expid=refYlist[iexpid], variable=varY, typevar=typevarY), year0=refYyear0list[iexpid],year1=refYyear1list[iexpid])
        refY=fitconstantseries.fitconstantseries(data=refY)
        expY['valuelist'] = wYlist[0] * expY['valuelist'] \
                          + wYlist[1] * refY['valuelist']
        statY = fillstatistics.fillstatistics(data=expY, freqtype=seasonYlist[iexpid])

        xdata.append(statX)
        ydata.append(statY)
#
# do all the plotting   
    plotscatterseries.plotscatterseries(xdata=xdata,ydata=ydata,freqtypeX=seasonXlist[0],freqtypeY=seasonYlist[0],typevarX=typevarX,typevarY=typevarY, \
                                        legendlist=legendlist,colorlist=colorlist,dolinearregressionlist=dolinearregressionlist,\
                                        description=description,code=code)
