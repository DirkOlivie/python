import os
import glob

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import season2monthnumberlist


def getsondelist(station,year0=1800,year1=3000,season='YEA'):
#------------------
    '''
    MODIFICATIONS
        (2024-02-19)

    INPUT
        station
        year0
        year1
        season

    RETURN
        list of sondes
    '''
 
    monthlist=season2monthnumberlist.season2monthnumberlist(season=season)
 
    dir='/projects/NS9560K/users/olivie/observations/shadoz/v20240209/'+station

    entrylist = os.listdir(dir)
#   entrylist = glob.glob(dir+'/*')

    sondelist = [] # empty list

    for entry in entrylist :
#
#        print(entry[-4:])

        if ( entry[-4:] == '.dat' ) : # only take files with '.dat' extension 

#           split filename
            line=entry.split('_')   # e.g. costarica_20080611T14_SHADOZV06.dat
                                   #      costarica_20130913T12_SHADOZV06_corr.dat
          
            timestamp = line[1]     # 20080611T14
            year  = int(timestamp[0:4])  
            month = int(timestamp[4:6])
            day   = int(timestamp[6:8])
#
#           print(year,month,day)


            if ( year0 <= year and year <= year1 ) :
                if ( month in monthlist ) : 
                    sondelist.append(entry) 

    print(sondelist)

    return sondelist
