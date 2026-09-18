import getfinalexpidinfo
import getrealmlist
import cmorize_internal

def cmorize(expid,var,freqfile,version,filenameformat,prodlossunits,overwrite=False) :
#------------------------------------------------
    '''
    INPUT
        expid
        var
        freqfile
        version
        filenameformat
        prodlossunits
        overwrite

    CALLS
        getrealmlist
        cmorize_internal

    MODIFICATIONS
        (2024-05-24) no_overwrite 

    '''

#   Not used so commented out [2025-10-21]
#   finalexpidinfo=getfinalexpidinfo.getfinalexpidinfo(expid=expid)
#    freqfile=finalexpidinfo['freqfile']
#
#   attributes for variable
    realmlist=getrealmlist.getrealmlist(var=var, freqfile=freqfile)

#   no loop     
    for realm in realmlist:
        cmorize_internal.cmorize_internal(expid=expid, var=var, freqfile=freqfile, realm=realm, version=version, filenameformat=filenameformat, prodlossunits=prodlossunits, overwrite=overwrite)
