import cmorize

def loopcmorize2(expidlist,varlist,freqfilelist,version,filenameformat,prodlossunits,overwrite=True) :
#---------------
    '''
    CALLED BY 
        loopcmorize

    CALLS
        cmorize
    '''
    for expid in expidlist :
        for var in varlist :
            for freqfile in freqfilelist :
#
                cmorize.cmorize(expid=expid,var=var,freqfile=freqfile,version=version,filenameformat=filenameformat,prodlossunits=prodlossunits,overwrite=overwrite)   
