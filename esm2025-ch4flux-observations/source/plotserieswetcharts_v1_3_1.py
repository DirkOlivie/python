import readwetcharts_v1_3_1
import convertdata2globalmeantimeseries    

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import fillstatistics
import plotseries

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


def plotserieswetcharts2_v1_3_1(expidlist, typevar, freqtype, figlayout, code):
#------------------------------
    '''
    MODIFICATIONS
    '''

    nexpid=len(expidlist)

#   READ ALL THE DATA
    legendlist=[]
    colorlist=[]
    data=[]
    for iexpid in range(nexpid) :
        expid=expidlist[iexpid]
#
#       read raw model data
        raw = readwetcharts_v1_3_1.readwetcharts_v1_3_1(expid=expid)
#
#       convert to timeseries
        tmp = convertdata2globalmeantimeseries.convertdata2globalmeantimeseries(data=raw)
#
#       do statistics
        b = fillstatistics.fillstatistics(data=tmp, freqtype=freqtype)

#       append data           
        data.append(b)
        legendlist.append(str(raw['expid']))
        colorlist.append(iexpid)

#
#   PLOT THE DATA
    shiftlist  = [0] * nexpid
    smoothlist = [0] * nexpid
    linestylelist = [0] * nexpid
    ensembletypelist = [''] * nexpid

    plotseries.plotseries(data=data,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar=typevar,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
#
#
def plotserieswetcharts_v1_3_1():
#-----------------------------
#
# extended ensemble 
    figlayout=cfiglayout.CFigLayout(plotdir='/scratch/olivie/code/python/esm2025-ch4flux-observations/plots')   
    code='wetcharts-v1.3.1'  
    typevar='glob'

    expidlist=['1913', '1914', '1923', '1924', '1933', '1934', \
               '2913', '2914', '2923', '2924', '2933', '2934', \
               '3913', '3914', '3923', '3924', '3933', '3934']

    plotserieswetcharts2_v1_3_1(expidlist=expidlist, typevar=typevar, freqtype='monthly', figlayout=figlayout, code=code)
    plotserieswetcharts2_v1_3_1(expidlist=expidlist, typevar=typevar, freqtype='YEA', figlayout=figlayout,code=code)
    plotserieswetcharts2_v1_3_1(expidlist=expidlist, typevar=typevar, freqtype='seasonalcycle', figlayout=figlayout,code=code)

if  __name__ == '__main__':
    plotserieswetcharts_v1_3_1()
