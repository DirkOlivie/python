import getfinalexpidinfo
import getrealmlist
import cmorize_internal

def cmorize(expid,var,overwrite=True) :
#------------------------------------------------
    '''
    INPUT
        expid
        var
        overwrite

    MODIFICATIONS
        (2024-05-24) no_overwrite 

    '''

    finalexpidinfo=getfinalexpidinfo.getfinalexpidinfo(expid=expid)
    freqfile=finalexpidinfo['freqfile']
#
#   attributes for variable
    realmlist=getrealmlist.getrealmlist(var=var, freqfile=freqfile)
    
    for realm in realmlist:
        cmorize_internal.cmorize_internal(expid=expid, var=var, realm=realm, overwrite=overwrite)
