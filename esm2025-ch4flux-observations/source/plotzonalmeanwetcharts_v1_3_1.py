import readwetcharts_v1_3_1
import convertdata2zonalmeantimeseries    

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/linezonal/source')
import fillzonalmeanstatistics
import plotzonalmeanline

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


def plotzonalmeanwetcharts2_v1_3_1(expidlist, typevar, season, figlayout, code):
#---------------------------------
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
        tmp = convertdata2zonalmeantimeseries.convertdata2zonalmeantimeseries(data=raw, region=typevar)
#
#       do statistics
        b = fillzonalmeanstatistics.fillzonalmeanstatistics(data=tmp, season=season)

#       append data           
        data.append(b)
        legendlist.append(str(raw['expid']))
        colorlist.append(iexpid)

#
#   PLOT THE DATA
    shiftlist  = [0] * nexpid
    smoothlist = [0] * nexpid
    linestylelist = [0] * nexpid
    linewidthlist = [1] * nexpid
    ensembletypelist = [''] * nexpid

    plotzonalmeanline.plotzonalmeanline(datalist=data,legendlist=legendlist,wlist=[1.,0.], figlayout=figlayout, code=code, horizontalaxis='', colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist, ensembletypelist=ensembletypelist)
#
#
def plotzonalmeanwetcharts_v1_3_1():
#-----------------------------
#
# extended ensemble 
    figlayout=cfiglayout.CFigLayout(plotdir='/scratch/olivie/code/python/esm2025-ch4flux-observations/plots')   
    code='wetcharts-v1.3.1'  
    typevar='glob'
    season='YEA'

    expidlist=['1913', '1914', '1923', '1924', '1933', '1934', \
               '2913', '2914', '2923', '2924', '2933', '2934', \
               '3913', '3914', '3923', '3924', '3933', '3934']
#               '1913-1914-1923-1924-1933-1934']

    plotzonalmeanwetcharts2_v1_3_1(expidlist=expidlist, typevar=typevar, season=season, figlayout=figlayout, code=code)

if  __name__ == '__main__':
    plotzonalmeanwetcharts_v1_3_1()
