import readspectrumseries

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import plotseries


def analysespectrumseries(setlist, legendlist, shiftlist, smoothlist, freqtype, code, figlayout, colorlist, linestylelist):
#------------------------
    '''
    INPUT
        setlist
        colorlist

    RETURN

    '''
    nset = len(setlist)

# read series
    data=[]

    for set in setlist :

        tmp = readspectrumseries.readspectrumseries(var=set['var'], origin=set['origin'], wvlresolution=set['wvlresolution'], freqtype=freqtype)
        data.append(tmp)

# plotseries
    plotseries.plotseries(data=data,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar='XX',code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
