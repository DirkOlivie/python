import generateseriesnoresmemissions

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import plotseries


def plotseriesnoresmemissions(filelist, prefactorlist, legendlist, shiftlist, smoothlist, freqtype, code, figlayout, colorlist, linestylelist):
#----------------------------
    '''
    INPUT
        filelist      : list of list !!
        prefactorlist : list of list !!
        legendlist
        shiftlist
        smoothlist
        freqtype
        code
        figlayout
        colorlist
        linestylelist

    RETURN

    CALLS
        generateseriesnorsmemissions
        plotseries

    '''
    nset = len(filelist)

# read series
    data=[]

    for iset in range(nset) :

#       filelist[iset] and prefactorlist[iset] are still lists !!
        tmp = generateseriesnoresmemissions.generateseriesnoresmemissions(filelist=filelist[iset], prefactorlist=prefactorlist[iset], freqtype=freqtype)
        data.append(tmp)

# plotseries
    plotseries.plotseries(data=data,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar='XX',code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
