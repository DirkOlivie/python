import readmeanzonalmean
import plotzonalmean

def analysezonalmean (expid, refid, wlist, var, year0, year1, refyear0, refyear1, season, figlayoutlist, code) :
#-------------------    

# read all the data 
    expdata = readmeanzonalmean.readmeanzonalmean(expid, var, year0, year1, season)

    if ( wlist[1] != 0. ) :
        refdata = readmeanzonalmean.readmeanzonalmean(refid, var, refyear0, refyear1, season)
    else :
        refdata = expdata # just to have something

# plot the zonal mean
    for figlayout in figlayoutlist :

        plotzonalmean.plotzonalmean(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, season=season, expdata=expdata, refdata=refdata, figlayout=figlayout, code=code)
