import getdatelist
import readsingleglobalmeanprofile

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents

def readmeanglobalmeanprofile_rawnoresm ( expid, var, year0, year1, season, verticalaxis, region=None, xlon=None, xlat=None):
#--------------------------------------
    '''
    MODIFICATIONS
        (2022-11-18) extension until components
        (2025-10-04) adding xlon and xlat, and default for region

    CALLS
        getdatelist
        getvarcomponents
        readsingleglobalmeanprofile
    '''
    print('+++ readmeanglobalmeanprofile +++')
#
# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)

#
# get the componentlist
    complist, weightlist = getvarcomponents.getvarcomponents(var=var)
    ncomp=len(complist)

# loop over all dates and components
    idate=0
    for date in datelist:

        icomp=0
        for comp in complist :
            weight=weightlist[icomp]

            a=readsingleglobalmeanprofile.readsingleglobalmeanprofile( expid=expid, var=comp, date=date, region=region, xlon=xlon, xlat=xlat, verticalaxis=verticalaxis)

            if ( idate == 0 and icomp == 0) : 
                amean=a

                amean['zlist']     = amean['zlist']     / float(ndate) / float(ncomp) # height
                amean['valuelist'] = amean['valuelist'] / float(ndate) * weight       # actual field
            else : 
                amean['zlist']     = amean['zlist']     + a['zlist']     / float(ndate) / float(ncomp) # height
                amean['valuelist'] = amean['valuelist'] + a['valuelist'] / float(ndate) * weight       # actual field     

            icomp=icomp+1 

        idate=idate+1 

# add begin year, end year and season information          
    amean['year0'] = year0
    amean['year1'] = year1
    amean['season'] = season
    amean['var'] = var
#
    print('--- readmeanglobalmeanprofile ---')
#
    return amean
