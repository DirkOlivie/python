import numpy as np

import readzonalseries
import fillzonalseriesstatistics
import plotzonalseries

def analysezonalseries (expid, refid, wlist, var, typevar, year0, year1, refyear0, refyear1, freqtype, season, dorefyearaverage, description, code, figlayoutlist) :
#---------------------
    '''
    INPUT
        ...
        year0
        year1
        ...

    CALLS
        readzonalseries
        fillzonalseriesstatistics : converts it to the right average ...
        plotzonalseries

    '''

# 1. read all the data 
    expdata = readzonalseries.readzonalseries(expid=expid, variable=var, typevar=typevar, year0=year0, year1=year1)

    if ( wlist[1] != 0. ) :
        refdata = readzonalseries.readzonalseries(refid, variable=var, typevar=typevar, year0=refyear0, year1=refyear1)

        if ( dorefyearaverage ) : 
            nlat=refdata['nlat']
            ntime=refdata['ntime']

            newvaluelist=np.zeros((ntime,nlat),dtype=float)

            nmonth=12
            for imonth in range(nmonth) :
                newvaluelist[imonth::nmonth,:] = np.mean(refdata['valuelist'][imonth::nmonth,:], axis=0)

            refdata['valuelist'] = newvaluelist

            print(newvaluelist[6,:])

    else :
        refdata = expdata # just to have something

#
# 2. add/substract/compare the two datasets 
    data = expdata
    data['valuelist'] = expdata['valuelist'] * wlist[0] \
                      + refdata['valuelist'] * wlist[1]
#
# 3. do all the statistics
    newdata = fillzonalseriesstatistics.fillzonalseriesstatistics(data=data, freqtype=freqtype, season=season)

#   plot the zonal mean
    for figlayout in figlayoutlist :

        plotzonalseries.plotzonalseries(expid=expid, refid=refid, wlist=wlist, var=var, typevar=typevar, year0=year0, year1=year1, freqtype=freqtype, season=season, data=newdata, code=code, figlayout=figlayout)
