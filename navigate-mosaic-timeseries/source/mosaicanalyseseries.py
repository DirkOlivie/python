import mosaicplotseries

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import analyseseries

def mosaicanalyseseries(expiddescriptionlist,suptitle,code,ncol):
#---------------------
    '''
    INPUT
        expiddescriptionlist
        var
        suptitle
        addcolorbar
        code

    CALLED BY
        mosaicanalyseloop2
    
    CALLS
        readmeanmap
        finditcz   
        mosaicplot 

    '''

    datalist = []

#   read the data
    for D in expiddescriptionlist : 

        expdata = analyseseries.analyseseries_internal(expidlist=D['expidlist'], refidlist=D['refidlist'], refid2list=None, refid3list=None, wlist=D['wlist'], shiftlist=D['shiftlist'], smoothlist=D['smoothlist'], variablelist=D['variablelist'], freqtype=D['freqtype'], typevarlist=D['typevarlist'], dorefaverage=D['dorefaverage'], ensembletypelist=D['ensembletypelist'])

        datalist.append(expdata)

#   plot the data
    mosaicplotseries.mosaicplotseries(expiddescriptionlist=expiddescriptionlist, datalist=datalist, suptitle=suptitle, code=code, ncol=ncol)
