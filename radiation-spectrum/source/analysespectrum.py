import readspectrum
import plotspectrum

def analysespectrum(setlist, legendlist, shiftlist, smoothlist, code, figlayout, colorlist, linestylelist):
#------------------
    '''
    INPUT
        setlist
        legendlist
        shiftlist
        smoothlist
        code
        figlayout
        colorlist
        linestylelist

    CALLS
        plotspectrum        

    '''
    nset = len(setlist)

# read series
    data=[]

    for set in setlist :

        tmp = readspectrum.readspectrum(var=set['var'], origin=set['origin'], wvlresolution=set['wvlresolution'], year0=set['year0'], year1=set['year1'], temperature=set['temperature'], prefactor=set['prefactor'])
        data.append(tmp)

# plotseries
    plotspectrum.plotspectrum(data=data,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
