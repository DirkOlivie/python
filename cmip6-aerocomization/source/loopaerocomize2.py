import aerocomize

def loopaerocomize2(expidlist,varlist,version,filetype,freqfile, overwrite=True) :
#------------------

    for expid in expidlist :
        for var in varlist :
#
            aerocomize.aerocomize(expid=expid,var=var,version=version,filetype=filetype,freqfile=freqfile,overwrite=overwrite)   
