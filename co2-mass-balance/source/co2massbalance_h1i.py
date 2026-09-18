import co2massbalance_h1i_generate

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import plotseries
import trimseries
import fillstatistics

def co2massbalance_h1i(expid, specieslist, legendlist, shiftlist, smoothlist, freqtypelist, code, figlayoutlist, colorlist, linestylelist):
#---------------------
#
    '''
    INPUT
        expid
        specieslist
        legendlist
        shiftlist
        smoothlist
        freqtypelist
        code
        figlayoutlist
        colorlist
        linestylelist

    CALLS
        co2massbalance_h1i_generate
        trimseries
        fillstatistics
        plotseries
    
    '''


    Rearth=6370e3    
    dir       = '/datalake/NS9560K/noresm3/cases'

#   1. read the different experiments and calculate budget
    datalist=[]
    for species in specieslist :

        tmp=co2massbalance_h1i_generate.co2massbalance_h1i_generate(expid=expid, species=species)

        datalist.append(tmp)

#   2. plot
    for freqtype in freqtypelist :

        print('DOING : ', freqtype)

#       new data
        newdatalist=[]

        for tmp in datalist:
#           trim
            if ( freqtype != 'monthly' ) :
                newdata = trimseries.trimseries(data=tmp)
            else :
                newdata = tmp

#           fill statistics
            newdata = fillstatistics.fillstatistics(data=newdata, freqtype=freqtype)

#           append
            newdatalist.append(newdata)

#       call the plotting routine
        for figlayout in figlayoutlist :            
            plotseries.plotseries(data=newdatalist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,freqtype=freqtype,typevar='XX',code=code+figlayout.ytype,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

