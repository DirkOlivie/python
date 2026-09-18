import mosaicplot

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import readmeanmap

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import finditcz

def mosaicanalyse(expiddescriptionlist,var,suptitle,addcolorbar,code):
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

    lon0=0. # 180.

    nexpid = len(expiddescriptionlist)

    datalist = []

    expitczlist = []
    refitczlist = []

#   read the data
    for D in expiddescriptionlist : 

        w=D['wlist']

        expdata = readmeanmap.readmeanmap(expid=D['expid'], var=var, year0=D['year0'], year1=D['year1'], season=D['season'])
        expitcz = finditcz.finditcz(data=expdata,lon0=lon0)


#        if ( w[0] != 1. or w[1] != 0.) :
        refdata = readmeanmap.readmeanmap(expid=D['refid'], var=var, year0=D['year0'], year1=D['year1'], season=D['season'])
        refitcz = finditcz.finditcz(data=refdata, lon0=lon0)

        expdata['field'] = D['wlist'][0] * expdata['field'] + D['wlist'][1] * refdata['field']

        datalist.append(expdata)

        expitczlist.append(expitcz)
        refitczlist.append(refitcz)


#   plot the data
    mosaicplot.mosaicplot(expiddescriptionlist=expiddescriptionlist, var=var, datalist=datalist, expitczlist=expitczlist, refitczlist=refitczlist, suptitle=suptitle, addcolorbar=addcolorbar, code=code)
