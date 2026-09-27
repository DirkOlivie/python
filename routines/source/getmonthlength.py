def getmonthlength(year, month, calendar) :
#-----------------
    '''
    INPUT   
        year
        month
        calendar : 'gregorian' | 'no_leap' | '365_day'    

    MODIFICATIONS
        (2024-09-25) Creation
        (2026-05-22) Removed default for calendar : was '', and added test (only 'gregorian' and 'noleap' allowed)

    '''
#
    if ( calendar != 'gregorian' and calendar != 'noleap' and calendar != '365_day' ) :
        print('+++ getmonthlength +++')
        print('No calendar recognized : ', noleap)
        quit()
#
    monthlengthlist=[31,28,31,30,31,30,31,31,30,31,30,31]
#
#   modify february length  
    if ( month == 2 and calendar == 'gregorian' ) :
        if (   ( year % 400 == 0 ) \
          or ( ( year % 4 == 0   ) and ( year % 100 != 0 ) ) ) : monthlengthlist[1] = 29
#
#   extract the correct month
    monthlength = monthlengthlist[month-1]  

    return monthlength
