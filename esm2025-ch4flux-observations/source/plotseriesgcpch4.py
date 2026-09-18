import readgcpch4
import convertdata2globalmeantimeseries    

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import fillstatistics
import plotseries

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


def plotseriesgcpch42(expidlist, legendlist, colorlist, linestylelist, typevar, freqtype, figlayout, code):
#--------------------
    '''
    MODIFICATIONS
    '''
#
#   READ ALL THE DATA
    data=[]

    nexpid = len(expidlist)

    for iexpid in range(nexpid) :
        expid=expidlist[iexpid]
#
#       read raw model data
        raw = readgcpch4.readgcpch4(expid=expid)
#
#       convert to timeseries
        tmp = convertdata2globalmeantimeseries.convertdata2globalmeantimeseries(data=raw)
#
#       do statistics
        b = fillstatistics.fillstatistics(data=tmp, freqtype=freqtype)

#       append data           
        data.append(b)

#
#   PLOT THE DATA
    shiftlist  = [0] * nexpid
    smoothlist = [0] * nexpid
    ensembletypelist = [''] * nexpid

    plotseries.plotseries(data=data,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar=typevar,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
#
#
def plotseriesgcpch4():
#-------------------
#
# extended ensemble 
    figlayout=cfiglayout.CFigLayout(plotdir='/scratch/olivie/code/python/esm2025-ch4flux-observations/plots')   
    code='gcp-ch4'  
    typevar='glob'
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
#
    plotseriesgcpch42(expidlist=expidlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='monthly'      , figlayout=figlayout, code=code)
    plotseriesgcpch42(expidlist=expidlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='YEA'          , figlayout=figlayout, code=code)
    plotseriesgcpch42(expidlist=expidlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='seasonalcycle', figlayout=figlayout, code=code)
#
if  __name__ == '__main__':
    plotseriesgcpch4()
