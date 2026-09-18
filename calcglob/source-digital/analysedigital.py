import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/tableglob/source')
import gettablevalue
import plotdigital

def analysedigital (expidlist,refidlist,wlist,xlist,expyear0list,expyear1list,expseasonlist,refyear0list,refyear1list,refseasonlist,legendlist,varlist,typevar,code) :
#-----------------    
    ''' 
    MODIFICATIONS
	(2022-07-12) : creation
    '''
#
#    
    nexpid=len(expidlist)
    nvar=len(varlist)
#
#   fill table
    valuelist=np.zeros((nexpid, nvar))
    unitslist = ['']*nvar # empty array
        
    for iexpid in range(0,nexpid) :   

        expid=expidlist[iexpid]
        refid=refidlist[iexpid]

        for ivar in range(0,nvar) :  

            ttt, units = gettablevalue.gettablevalue(var=varlist[ivar], expid=expidlist[iexpid], year0=expyear0list[iexpid], year1=expyear1list[iexpid],season=expseasonlist[iexpid])
            valuelist[iexpid,ivar] = ttt * wlist[0]

            if ( wlist[1] != 0. ) :

                ttt, units = gettablevalue.gettablevalue(var=varlist[ivar], expid=refidlist[iexpid], year0=refyear0list[iexpid], year1=refyear1list[iexpid],season=refseasonlist[iexpid])
                valuelist[iexpid] = valuelist[iexpid] + ttt * wlist[1]

            unitslist[ivar] = units

    print(valuelist)

#   plotdigital
    plotdigital.plotdigital(varlist=varlist, valuelist=valuelist, xlist=xlist, legendlist=legendlist, unitslist=unitslist, code=code)
