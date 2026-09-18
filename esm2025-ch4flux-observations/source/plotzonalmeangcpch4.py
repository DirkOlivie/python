import readgcpch4
import convertdata2zonalmeantimeseries    

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/linezonal/source')
import fillzonalmeanstatistics
import plotzonalmeanline

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


def plotzonalmeangcpch42(expidlist, legendlist, typevar, season, colorlist, linestylelist, figlayout, code):
#-----------------------
    '''
    MODIFICATIONS
    '''

    nexpid=len(expidlist)

#   READ ALL THE DATA
#    legendlist=[]
#    colorlist=[]
    data=[]
    for iexpid in range(nexpid) :
        expid=expidlist[iexpid]
#
#       read raw model data
        raw = readgcpch4.readgcpch4(expid=expid)
#
#       convert to timeseries
        tmp = convertdata2zonalmeantimeseries.convertdata2zonalmeantimeseries(data=raw, region=typevar)
#
#       do statistics
        b = fillzonalmeanstatistics.fillzonalmeanstatistics(data=tmp, season=season)

#       append data           
        data.append(b)
#        legendlist.append(str(raw['expid']))
#        colorlist.append(iexpid)

#
#   PLOT THE DATA
    shiftlist  = [0] * nexpid
    smoothlist = [0] * nexpid
#    linestylelist = [0] * nexpid
    linewidthlist = [1] * nexpid
    ensembletypelist = [''] * nexpid

    plotzonalmeanline.plotzonalmeanline(datalist=data,legendlist=legendlist,wlist=[1.,0.], figlayout=figlayout, code=code, horizontalaxis='', colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist, ensembletypelist=ensembletypelist)
#
#
def plotzonalmeangcpch4():
#----------------------
#
# extended ensemble 
    figlayout=cfiglayout.CFigLayout(plotdir='/scratch/olivie/code/python/esm2025-ch4flux-observations/plots')   
    code='gcp-ch4'  
    typevar='glob'
    season='YEA'

    expidlist = [\
                  'CLASSIC_CRU', \
                  'CLASSIC_GSWP3', \
                  'ELM_CRU', \
                  'ELM_GSWP3', \
                  'ISAM_CRU', \
                  'ISAM_GSWP3', \
                  'JSBACH_CRU', \
                  'JSBACH_GSWP3', \
                  'JULES_CRU', \
                  'JULES_GSWP3', \
                  'LPJ-MPI_CRU', \
                  'LPJ-MPI_GSWP3', \
                  'LPJ-wsl_CRU', \
                  'LPJ-wsl_GSWP3', \
                  'LPX-Bern_CRU', \
                  'LPX-Bern_GSWP3', \
                  'ORCHIDEE_CRU', \
                  'ORCHIDEE_GSWP3', \
                  'SDGVM_CRU', \
                  'SDGVM_GSWP3', \
                  'VISIT_CRU', \
                  'VISIT_GSWP3']

    legendlist = [\
                  'CLASSIC','', \
                  'ELM','', \
                  'ISAM','', \
                  'JSBACH','', \
                  'JULES','', \
                  'LPJ-MPI','', \
                  'LPJ-wsl','', \
                  'LPX-Bern','', \
                  'ORCHIDEE','', \
                  'SDGVM','', \
                  'VISIT','']

    colorlist=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
    linestylelist=[0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2]

    plotzonalmeangcpch42(expidlist=expidlist, legendlist=legendlist, typevar=typevar, season=season, colorlist=colorlist, linestylelist=linestylelist, figlayout=figlayout, code=code)

if  __name__ == '__main__':
    plotzonalmeangcpch4()
