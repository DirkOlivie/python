import sys

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import getdatelist
#import readsingleglobalmeanprofile
import readmeanglobalmeanprofile


def readmodelprofile( expid, year0, year1, season, var, xlon, xlat, verticalaxis):
#--------------------
    '''
    MODIFICATIONS
        (204-02-21) creation

    CALLS
        getdatelist
        readsingleglobalmeanprofile

    '''
# 
    print('+++ readmodelprofile +++')    

# get sondelist
    datelist=getdatelist.getdatelist(year0=year0, year1=year1, season=season)

# make average sonde
    datalist=[]

# read all individual sondes
    for date in datelist :
        print('Start reading model : '+date)

#       TRADITIONAL METHOD       
#       read one single month [for NorESM output type]
#        data= readsingleglobalmeanprofile.readsingleglobalmeanprofile(expid=expid, date=date, var=var, xlon=xlon, xlat=xlat, verticalaxis=verticalaxis)

#       NEW METHOD
        line=date.split('-')
        year=int(line[0])
        month=line[1]
        if   ( month == '01' ) : season = 'JAN'
        elif ( month == '02' ) : season = 'FEB' 
        elif ( month == '03' ) : season = 'MAR'
        elif ( month == '04' ) : season = 'APR'
        elif ( month == '05' ) : season = 'MAY'
        elif ( month == '06' ) : season = 'JUN'
        elif ( month == '07' ) : season = 'JUL'
        elif ( month == '08' ) : season = 'AUG'
        elif ( month == '09' ) : season = 'SEP'
        elif ( month == '10' ) : season = 'OCT'
        elif ( month == '11' ) : season = 'NOV'
        elif ( month == '12' ) : season = 'DEC'
        else : 
            print('No month recognized : ', month)
            quit() 
#    
        data = readmeanglobalmeanprofile.readmeanglobalmeanprofile(expid=expid, var=var, year0=year, year1=year, season=season, xlon=xlon, xlat=xlat, verticalaxis=verticalaxis)
#
#        print(data['zlist'])
#        print(data['zunits'])
#        quit()


        datalist.append(data)

# return the data
    return datalist
