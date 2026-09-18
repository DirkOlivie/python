import getmonthlength

def getpreviousdate(date,calendar):
#--------------
    '''
    INPUT
        date : yyyy-mm-dd
        calendar
    '''
#
    line=date.split('-')
#
    if (len(line) != 3 ) :
        print('Date not in correct yyyy-mm-dd format : ', date)
        quit()
#
    year=int(line[0])
    month=int(line[1])
    day=int(line[2])

#   nexdate   
    day=day-1

    if ( day < 1 ) :  
        month=month-1    
        if ( month < 1 ) : 
           year=year-1
           month=12            
        day=getmonthlength.getmonthlength(year=year,month=month,calendar=calendar)

    previousdate=str("%4.4i"% (year))+'-'+str("%2.2i"% (month))+'-'+str("%2.2i"% (day))

    return previousdate
