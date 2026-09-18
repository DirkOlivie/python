import getdatelist
import readsinglemap

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getmemberlist

def readmeanmap ( expid, var, year0, year1, season):
#--------------
    '''
    MODIFICATIONS
        (2025-12-14) : extension to memberlist

    INPUT
        expid
        var
        year0
        year1
        season

    CALLS
        getdatelist
        getvarcomponents
        getmemberlist
        readsinglemap
    '''
#
# get the datelist
    datelist=getdatelist.getdatelist(year0=year0,year1=year1,season=season)
    ndate=len(datelist)
    print('datelist = ')
    print(datelist)
    print(year0)
    print(year1)

# get the componentlist
    complist, weightlist = getvarcomponents.getvarcomponents(var=var)
    ncomp=len(complist)

# get memberlist 
    memberlist = getmemberlist.getmemberlist(expid=expid)    
    nmember=len(memberlist)

# loop over all zonal mean
    for idate in range(ndate) :
        date = datelist[idate]

        for icomp in range(ncomp) :
            comp   = complist[icomp]
            weight = weightlist[icomp]

            for imember in range(nmember) :
                member = memberlist[imember]
                
                a=readsinglemap.readsinglemap( expid=member, var=comp, date=date)

                if ( idate == 0 and icomp == 0 and imember == 0 ) : 
                    amean=a
                    amean['latitude']  = amean['latitude']  / float(ndate) / float(ncomp) / float(nmember) # latitudes
                    amean['longitude'] = amean['longitude'] / float(ndate) / float(ncomp) / float(nmember) # longitues
                    amean['field']     = amean['field']     / float(ndate) * weight       / float(nmember) # actual field
                else : 
                    amean['latitude']  = amean['latitude']  + a['latitude']  / float(ndate) / float(ncomp) / float(nmember) # latitudes
                    amean['longitude'] = amean['longitude'] + a['longitude'] / float(ndate) / float(ncomp) / float(nmember) # longitudes
                    amean['field']     = amean['field']     + a['field']     / float(ndate) * weight       / float(nmember) # actual field       
#
    return amean
