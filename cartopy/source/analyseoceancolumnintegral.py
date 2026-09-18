import readmeanoceancolumnintegral
import interp_blom_to_cam
#import plotoceancolumnintegral

def analyseoceancolumnintegral (expid, refid, wlist, var, year0, year1, season, figlayoutlist, code) :
#-----------------------------

# read all the data 
    expdata = readmeanoceancolumnintegral.readmeanoceancolumnintegral(expid, var, year0, year1, season)
    expdata = interp_blom_to_cam.interp_blom_to_cam(blomdata=expdata,grid='f19')


    if ( wlist[1] != 0. ) :
        refdata = readmeanoceancolumnintegral.readmeanoceancolumnintegral(refid, var, year0, year1, season)
        refdata = interp_blom_to_cam.interp_blom_to_cam(blomdata=refdata,grid='f19')

    else : 
        refdata = expdata   # just DUMMY needed  
 
#
# integrate to cam grid


# plot the zonal map

#    for figlayout in figlayoutlist :

#        plotoceancolumnintegral.plotoceancolumnintegral(expid=expid, refid=refid, wlist=wlist, var=var, year0=year0, year1=year1, season=season, expdata=expdata, refdata=refdata, figlayout=figlayout, code=code)
