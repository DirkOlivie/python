import glob
import numpy as np

import getdiagvaluelistsinglefile

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def getdiagvaluelist(expid, freqtype, budgettype, component, variable):
#-------------------

    expidinfo = experimentdefinition.getexpidinfo(expid=expid)
    year0  = expidinfo['year0']
    year1  = expidinfo['year1']
    subdir = expidinfo['subdir']
    cexpid = expidinfo['cexpid'] # experiment you read (can be different from experiment you write)
    cdir   = expidinfo['cdir']
    
    directory=subdir+'/'+cdir+'/logs'

    regex='diags.log.*'

    filelist=glob.glob(directory+'/'+regex)
    filelist.sort()

    a_all = {}

    for file in filelist:

        a=getdiagvaluelistsinglefile.getdiagvaluelistsinglefile(filename=file, freqtype=freqtype, budgettype=budgettype, component=component, variable=variable)

        print(a)

        for key, value in a.items()  :

            a_all[key] = value
   
    print(a_all)
 
    n=len(a_all)
#
    yearlist=np.zeros(n, dtype=int)    
    monthlist=np.zeros(n, dtype=int)
    valuelist=np.zeros(n, dtype=float)
    units='W m-2'
 
    i=0
    for key,value in a_all.items() :
          
        date=int(key)
        year = date // 10000
        month = ( date % 10000 ) // 100

#       go to previous month
        month=month-1
        if ( month < 1 ) : month=12 ; year=year-1

        yearlist[i] = year
        monthlist[i] = month
        valuelist[i] = float(value)

        i=i+1

    ntime=i

#    print(yearlist)
#    print(monthlist)
##    print(valuelist)

    data = { 'valuelist' : valuelist, \
             'monthlist' : monthlist, \
             'yearlist'  : yearlist, \
             'units'     : units, \
             'ntime'     : ntime}

    return data
    

