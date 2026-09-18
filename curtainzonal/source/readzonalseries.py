import re
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getvarcomponents
import readsinglezonalseries

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getmemberlist


def readzonalseries (expid=None, variable=None, typevar=None, year0=None, year1=None) :
#------------------
#
    '''
    REMARK
        reads everything - not for a specific season yet

    INPUT
        expid
        variable
        typevar
        year0
        year1

    CALLS
        readsinglezonalseries

    MODIFICATIONS
	    (2021-04-05) : creation
        (2025-12-02) : extension to memberlist
    '''

    complist, weightlist = getvarcomponents.getvarcomponents(var=variable)
    ncomp=len(complist)


    memberlist = getmemberlist.getmemberlist(expid=expid)
    nmember=len(memberlist)


#   loop over all component contributions    
    for icomp in range(ncomp) :
        
        comp   = complist[icomp]
        weight = weightlist[icomp]

#       loop over all members
        for imember in range(nmember) :

            member = memberlist[imember]

            tmp = readsinglezonalseries.readsinglezonalseries(expid=member, variable=comp, typevar=typevar, year0=year0, year1=year1)  

            if ( icomp== 0 and imember== 0) : 

                data=tmp
                data['valuelist'] =                     tmp['valuelist'] * weight / float(nmember)

            else :

                data['valuelist'] = data['valuelist'] + tmp['valuelist'] * weight / float(nmember)

    data['variable'] = variable
#
#
    return data
