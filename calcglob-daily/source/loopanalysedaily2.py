import analysedaily

import sys 
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getdailydatelist

def loopanalysedaily2(varlist, expid, directory, date0, date1, calendar, code):
#--------------------

    datelist=getidailydatelist.getdailydatelist(date0=date0, date1=date1, calendar=calendar)

    print(datelist)

    for var in varlist :

        analysedaily.analysedaily(var=var, expid=expid, directory=directory, datelist=datelist, calendar=calendar, code=code)
