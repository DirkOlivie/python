import getbasicexpidlist

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def getbasicexpidname ( expid, date ) :
#--------------------
    '''
    MODIFICATIONS
        (2023-10-20) : creation

    INPUT
        expid  : 
        date   : yyyy-mm

    RETURNS
        one experiment name for which the year corresponds

    CALLS
        getbasicexpidlist
        getexpidinfo (experimentdefinition.py)

    '''    

#   get whole experiment list    
    expidlist=getbasicexpidlist.getbasicexpidlist(expid=expid)
    nexpid=len(expidlist)

    print('EXPIDLIST : ',expidlist)

#   extract date from year
    line=date.split('-')    # split yyyy-mm
    year=int(line[0])       # convert string (yyyy) into integer


    basicexpid=''
#   loop over all experiments : last one which agrees will be retained
    for testexpid in expidlist : 
        expidinfo=experimentdefinition.getexpidinfo(expid=testexpid)
        if ( expidinfo['year0'] <= year \
         and expidinfo['year1'] >= year) : basicexpid=testexpid

        
#   check        
    if ( basicexpid == '' ) : 
        print('*** No corresponding experiment found (getbasicexpidname.py) ***')
        print('Experiment : ', expid)
        print('Year : ', year)
        print('Experimentlist : ', expidlist)
        quit()

#   return    
    return basicexpid
