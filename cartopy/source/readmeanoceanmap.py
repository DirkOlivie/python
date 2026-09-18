import getdatelist
import readsingleoceanmap

def readmeanoceanmap ( expid, var, year0, year1, season):
#------------------------------

# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)

# loop over all zonal mean
    idate=0
    for date in datelist:
        a=readsingleoceanmap.readsingleoceanmap( expid=expid, var=var, date=date)

        if ( idate == 0 ) : 
           amean=a
           amean['field'] = amean['field']    / float(ndate)
        else : 
           amean['field']    = amean['field']    + a['field']    / float(ndate)      

        idate=idate+1 
#
    return amean
