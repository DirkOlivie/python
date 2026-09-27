import netCDF4 as nc

import readnc
import readattributenc

def readdatesnc(filename):
#--------------
    '''
    MODIFICATIONS
        (2026-09-25) creation
    '''
    print('filename : ', filename)

#   READ TIME
    timelist = readnc.readnc('time', filename)

#   READ CALENDAR
    calendar = readattributenc.readattributenc('time', filename, 'calendar')

#   READ TIME_UNITS
    time_units = readattributenc.readattributenc('time', filename, 'units')

#   TIME + CALENDAR + TIME_UNITS -> DATETIME   
    datelist=[]
    for i in range(len(timelist)) :
        datetime = nc.num2date(timelist[i], time_units, calendar=calendar)
        
        cyear=str(datetime.year)
        cmonth=str(datetime.month)
        cday=str(datetime.day) 

        datelist.append(cyear+'-'+cmonth+'-'+cday)

    return datelist
