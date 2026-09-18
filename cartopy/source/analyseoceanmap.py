import readmeanoceanmap
import plotmap
import interp_blom_to_cam
import cfiglayout

def analyseoceanmap (expid, refid, wlist, var, year0, year1, season, figlayoutlist, code) :
#------------------

# read all the data 
    expdata = readmeanoceanmap.readmeanoceanmap(expid, var, year0, year1, season)
    expdata = interp_blom_to_cam.interp_blom_to_cam(blomdata=expdata,grid='f19')

# read the reference data
    if ( wlist[1] != 0. ) :
        refdata = readmeanoceanmap.readmeanoceanmap(refid, var, year0, year1, season)
        refdata = interp_blom_to_cam.interp_blom_to_cam(blomdata=refdata,grid='f19')
    else :
        refdata = expdata # just to have something

# plot the zonal mean
    
    for figlayout in figlayoutlist : 
 
#       figlayout=cfiglayout.CFigLayout(contour_levels_type=figlayout,code=figlayout)             

        plotmap.plotmap(expid=expid, refid=refid, var=var, wlist=wlist, year0=year0, year1=year1, season=season, expdata=expdata, refdata=refdata, figlayout=figlayout, code=code)
