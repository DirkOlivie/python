import getdatelist
import readsingleoceancolumnintegral

def readmeanoceancolumnintegral ( expid, var, year0, year1, season):
#------------------------------

# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)

# loop over all zonal mean
    idate=0
    for date in datelist:
        a=readsingleoceancolumnintegral.readsingleoceancolumnintegral( expid=expid, var=var, date=date)

        if ( idate == 0 ) : 
           amean=a
           amean['field'] = amean['field']    / float(ndate)
           amean['depth'] = amean['depth']    / float(ndate)
        else : 
           amean['field']    = amean['field']    + a['field']    / float(ndate)      
           amean['depth']    = amean['depth']    + a['depth']    / float(ndate)      

        idate=idate+1 
#
    return amean
