import numpy as np
import season2monthnamelist

def getperiodlist (timedescription):
#----------------    
    '''
    MODIFICATIONS
        (2022-09-07) : creation

    INPUT
        timedescription is of the following form :
        [year0]-[year1]-[separate]-[JAN]-[separate]
                        [average ] [FEB] [average ] 
                                   [...]
                                   [DJF]
                                   [...]
                                   [YEA]

    OUTPUT
        a list of periods
        [aaaa-bbbb-CCC,    dddd-eeee-FFF, ...] 
               |                  |   
         will be averaged  will be averaged      

    '''
# disentangle the time description   
    line=timedescription.split('-')
#
    cyear0       = line[0]                   # should be integer?
    cyear1       = line[1]                   # should be integer?
    yearmethod   = line[2]
    season       = line[3]
    seasonmethod = line[4]
#
#   contributing years
    if ( yearmethod == 'seperate' ) :              # [2000-2000, 2001-2001, ..., 2009-2009]
        year0=int(cyear0)
        year1=int(cyear1)

        yearperiodlist=[]
        for year in range(year0,year1+1) : 
            cyear=str("%4.4i"% (year))
            yearperiodlist.append(cyear+'-'+cyear)
#
    elif ( yearmethod == 'average' ) :             # [2000-2009]
        yearperiodlist=[cyear0+'-'+cyear1]           
#
    else :
        print('No yearmethod recognized : '+yearmethod)
        quit()
        

#   contributing months
    if ( seasonmethod == 'seperate' ) :            # [MAR,APR,MAY] 
        seasonperiodlist=season2monthnamelist.season2monthnamelist(season=season)

    elif ( seasonmethod == 'average' ) : 
        seasonperiodlist=[season]                   # [MAM]
#
#   combine yearperiodlist and monthperiodlist
    periodlist = []
    for yearperiod in yearperiodlist : 
        for seasonperiod in seasonperiodlist :  
            periodlist.append(yearperiod+'-'+seasonperiod)
#
    return periodlist 
