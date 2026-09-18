import copy

import insitureadsingle

def insituread(expid, variable, xlon, xlat):
#-------------

# get experiment info
    if ( variable == 'SULFATE_SRF' ) : complist=['SO4_A1_SRF','SO4_A2_SRF','SO4_AC_SRF','SO4_NA_SRF','SO4_PR_SRF']
    else : complist = [variable]

#   
    for comp in complist :
        tmp = insitureadsingle.insitureadsingle(expid=expid, variable=comp, xlon=xlon, xlat=xlat) 

        if ( comp == complist[0] ) : 
            data=copy.deepcopy(tmp)
        else :
            data['valuelist'] = data['valuelist'] + tmp['valuelist']
#
    data['variable'] = variable
#
    return data
