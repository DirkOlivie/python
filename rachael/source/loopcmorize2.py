import cmorize

def loopcmorize2(expidlist,varlist,overwrite=True) :
#---------------------------------------------------

    for expid in expidlist :
        for var in varlist :
#
            cmorize.cmorize(expid=expid,var=var,overwrite=overwrite)   
