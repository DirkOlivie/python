import readgiemsmc

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import fillstatistics
import plotseries

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

sys.path.insert(0,'/nird/home/olivie/code/python/esm2025-ch4flux-observations/source')
import convertdata2globalmeantimeseries

def plotseriesgiemsmc2(varlist, legendlist, colorlist, linestylelist, typevar, freqtype, figlayout, code):
#--------------------
    '''
    MODIFICATIONS
    '''
#
#   READ ALL THE DATA
    data=[]

    nvar = len(varlist)

    for ivar in range(nvar) :
        var=varlist[ivar]
#
#       read raw model data
        raw = readgiemsmc.readgiemsmc(variable=var)
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
    shiftlist  = [0] * nvar
    smoothlist = [0] * nvar
    ensembletypelist = [''] * nvar

    plotseries.plotseries(data=data,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar=typevar,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
#
#
def plotseriesgiemsmc():
#--------------------
#
# extended ensemble 
    figlayout=cfiglayout.CFigLayout(plotdir='/scratch/olivie/code/python/esm2025-wetlandfraction-observations/plots')   
    code='giems-mc'  
    typevar='glob'

#   variables with annual + monthly data
    varlist = ['inund_sat_wetland_frac','inund_sat_peat_wetland_frac']
    legendlist = varlist
    colorlist=[0,1]
    linestylelist=[0,0]
#
    plotseriesgiemsmc2(varlist=varlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='monthly'      , figlayout=figlayout, code=code)
    plotseriesgiemsmc2(varlist=varlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='YEA'          , figlayout=figlayout, code=code)
    plotseriesgiemsmc2(varlist=varlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='seasonalcycle', figlayout=figlayout, code=code)
#
#   variables with one seasonal cycle
    varlist = ['rice_irri_frac','rice_rainfed_frac']
    legendlist = varlist
    colorlist=[0,1]
    linestylelist=[0,0]
#
    plotseriesgiemsmc2(varlist=varlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='monthly'      , figlayout=figlayout, code=code)
    plotseriesgiemsmc2(varlist=varlist, legendlist=legendlist, colorlist=colorlist, linestylelist=linestylelist, typevar=typevar, freqtype='seasonalcycle', figlayout=figlayout, code=code)
#
if  __name__ == '__main__':
    plotseriesgiemsmc()
