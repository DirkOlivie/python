import numpy as np

def yearlistmonthlist2datelist(yearlist, monthlist):
#-----------------------------
#
    '''
    INPUT
        yearlist
        monthlist

    OUTPUT
        datelist

    '''

    if ( len(yearlist) != len(monthlist) ) :
        print('+++ yearlistmonthlist2datelist +++')
        print('Length of yearlist : ', len(yearlist))
        print('Length of monthlist : ', len(monthlist))
        quit()
#   
    ntime=len(yearlist)
#
    datelist  = np.zeros(ntime, dtype='<U7')
#
    for itime in range(0,ntime) :
        datelist[itime]  = str("%4.4i"% (yearlist[itime]))+'-'+str("%2.2i"% (monthlist[itime]))
#
    return datelist
