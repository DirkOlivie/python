import getnextdate

def getdailydatelist(date0,date1,calendar):
#---------------------------------
    '''
    REMARK
        startdate and enddate both included in the final list

    INPUT
        date0    : string in format yyyy-mm-dd
        date1    : string in format yyyy-mm-dd
        calendar : 
    '''
    datelist=[]

    date=date0

    datelist.append(date)
    while ( date != date1 ) :
        date=getnextdate.getnextdate(date=date, calendar=calendar) 
        datelist.append(date)

    return datelist
