import numpy as np

def getdatelist (year0, year1, season):
#--------------    
    '''
    MODIFICATIONS

    '''

    if   ( season == 'JAN' ) : monthlist=['01']
    elif ( season == 'FEB' ) : monthlist=['02']
    elif ( season == 'MAR' ) : monthlist=['03']
    elif ( season == 'APR' ) : monthlist=['04']
    elif ( season == 'MAY' ) : monthlist=['05']
    elif ( season == 'JUN' ) : monthlist=['06']
    elif ( season == 'JUL' ) : monthlist=['07']
    elif ( season == 'AUG' ) : monthlist=['08']
    elif ( season == 'SEP' ) : monthlist=['09']
    elif ( season == 'OCT' ) : monthlist=['10']
    elif ( season == 'NOV' ) : monthlist=['11']
    elif ( season == 'DEC' ) : monthlist=['12']
    elif ( season == 'DJF' ) : monthlist=['01','02','12']
    elif ( season == 'MAM' ) : monthlist=['03','04','05']
    elif ( season == 'JJA' ) : monthlist=['06','07','08']
    elif ( season == 'SON' ) : monthlist=['09','10','11']
    elif ( season == 'YEA' ) : monthlist=['01','02','03','04','05','06','07','08','09','10','11','12']
    else : 
        print('+++ getdatelist +++')
        print('No season recognized : ', season)
        quit()

#    print('year0 : ', year0)
#    print('year1 : ', year1)
#    print('season : ', season)

    yearlist=np.arange(year0, year1+1, 1)

    datelist=[]

    for year in yearlist :
        for month in monthlist :
#
            datelist.append(str("%4.4i"% (year))+'-'+month)

    return datelist
