import numpy as np

def year0year1_to_yearlistmonthlist(year0, year1):
#----------------------------------
#
    '''
    INPUT
        year0
        year1

    OUTPUT
        yearlist
        monthlist
    '''
#
    nyear=year1-year0+1

    if ( nyear < 1 ) : 
        print('+++ year0year1_to_yearlistmonthlist +++')
        print('Number of years not allowed : ', nyear)
        quit()

    nmonth=12
    ntime=nyear*nmonth
    yearlist  = np.zeros(ntime, dtype=int)
    monthlist = np.zeros(ntime, dtype=int)
    for itime in range(0,ntime) :
        yearlist[ itime] = year0 + itime // nmonth
        monthlist[itime] = itime % nmonth + 1
#
    return yearlist, monthlist
