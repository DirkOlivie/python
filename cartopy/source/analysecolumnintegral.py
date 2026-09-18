import readmeancolumnintegral
import plotcolumnintegral

def analysecolumnintegral (expid, var, year0, year1, season, figlayoutlist) :
#------------------------

# read all the data 
    data = readmeancolumnintegral.readmeancolumnintegral(expid, var, year0, year1, season)

# plot the zonal mean

    for figlayout in figlayoutlist :

        plotcolumnintegral.plotcolumnintegral(expid=expid, var=var, year0=year0, year1=year1, season=season, data=data, figlayout=figlayout)
