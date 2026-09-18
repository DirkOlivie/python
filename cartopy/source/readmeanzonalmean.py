import getdatelist
import readsinglezonalmean

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents

def readmeanzonalmean ( expid, var, year0, year1, season):
#--------------------
#
# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)
#
# get the componentlist
    complist, weightlist = getvarcomponents.getvarcomponents(var=var)
    ncomp=len(complist)

# loop over all zonal mean
    idate=0
    for date in datelist:

        icomp=0 
        for comp in complist :  
            weight=weightlist[icomp]

            a=readsinglezonalmean.readsinglezonalmean( expid=expid, var=comp, date=date)

            if ( idate == 0 and icomp==0 ) : 
                amean=a
                amean['x'] = amean['x'] / float(ndate) / float(ncomp)  # latitude
                amean['y'] = amean['y'] / float(ndate) / float(ncomp)  # altitude
                amean['z'] = amean['z'] / float(ndate) * weight        # actual field
            else : 
                amean['x'] = amean['x'] + a['x'] / float(ndate) / float(ncomp) # latitude
                amean['y'] = amean['y'] + a['y'] / float(ndate) / float(ncomp) # altitude
                amean['z'] = amean['z'] + a['z'] / float(ndate) * weight       # actual field

            icomp=icomp+1
             
        idate=idate+1 
#
    return amean
