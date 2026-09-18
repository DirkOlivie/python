import readmeanmap
import plotmap
import cfiglayout

def analysemap (expid, refid, wlist, var, year0, year1, refyear0, refyear1, season, figlayoutlist, code) :
#-------------

# read all the data 
    expdata = readmeanmap.readmeanmap(expid, var, year0, year1, season)

    if ( wlist[1] != 0. ) :

#        if ( refid == 'N1850_f19_tn14_20190621' ) :
#            year0corr= 1791  # 1800
#            year1corr= 1800
#        else :
#            year0corr=year0
#            year1corr=year1
#        
#        refdata = readmeanmap.readmeanmap(refid, var, year0corr, year1corr, season)

        refdata = readmeanmap.readmeanmap(refid, var, refyear0, refyear1, season)
    else :
        refdata = expdata # just to have something

# plot the zonal mean
    
    for figlayout in figlayoutlist : 
 
#       figlayout=cfiglayout.CFigLayout(contour_levels_type=figlayout,code=figlayout)             

        plotmap.plotmap(expid=expid, refid=refid, var=var, wlist=wlist, year0=year0, year1=year1,  season=season, expdata=expdata, refdata=refdata, figlayout=figlayout, code=code)
