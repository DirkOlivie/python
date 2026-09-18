import getmonthlength

def daysince(refdate, enddate, calendar):
#------------
    '''
    CORRECTION
        (2023-07-27) year ne 1800 OR year ne  1900 : OR should be AND

    MODIFICATIONS
        (2018-05-12) added 1800 as a non-leap year
        (2021-04-18) added calendartype
                       'gregorian' (default) : includes leap years
                       'noleap'              : includes no leap years
        (2023-07-26) added 1700 as a non-leap year

    INPUT
        refdate : yyyymmdd (integer)
        enddate : yyyymmdd (integer)
        calendartype=

    RETURN
        number of days since refdate
    '''
#----------------------------------------------------------
#    
#    print('+++ daysince +++')
#
    if ( calendar != 'gregorian' and calendar != 'noleap' ) :
        print('+++ daysince +++')
        print('No calendar recognized : ', calendar)
        quit()

    refyear  =   refdate // 10000
    refmonth = ( refdate // 100 ) % 100
    refday   =   refdate % 100
#
    endyear  =   enddate // 10000
    endmonth = ( enddate // 100 ) % 100
    endday   =   enddate % 100
#
    year  = refyear
    month = refmonth
    day   = refday
#
    diff=0
#
    while ( ( year != endyear ) or ( month != endmonth ) or (day != endday ) ) :
#        print(year,month,day)
#       current monthlength
        monthlen = getmonthlength.getmonthlength(year=year, month=month, calendar=calendar)
#
#       try to step by 1 month if on 1st of month
        if ( ( year != endyear ) and (day == 1) ) :

#           step
            diff=diff+monthlen # step by 1 month
#           
#           new date
            month=month+1      # go to next month

#           check writing of next date
            if ( month > 12 ) :
                month = 1
                year = year +1

        else :

#           step
            diff=diff+1

#           new date
            day=day+1          # go to next day

#           check writing of next date
            if ( day > monthlen) :
                day = 1
                month = month +1
                if ( month > 12 ) :
                    month = 1
                    year = year +1
#
#    print('--- daysince ---')
#
    return diff

