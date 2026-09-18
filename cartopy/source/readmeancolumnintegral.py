import getdatelist
import readsinglecolumnintegral

def readmeancolumnintegral ( expid, var, year0, year1, season):

# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)

# loop over all zonal mean
    idate=0
    for date in datelist:
        a=readsinglecolumnintegral.readsinglecolumnintegral( expid=expid, var=var, date=date)

        if ( idate == 0 ) : 
           amean=a
           amean['lats'] = amean['lats'] / float(ndate)
           amean['lons'] = amean['lons'] / float(ndate)
           amean['z']    = amean['z']    / float(ndate)
        else : 
           amean['lats'] = amean['lats'] + a['lats'] / float(ndate)
           amean['lons'] = amean['lons'] + a['lons'] / float(ndate)
           amean['z']    = amean['z']    + a['z']    / float(ndate)      

        idate=idate+1 
#
    return amean
