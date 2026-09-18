import os, sys

sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getexpidsplit
import getparentexpidinfo

import concatenatenetcdf

def loopconcatenatenetcdf2(expidlist,varlist) :
#--------------------------------------------

    for expid in expidlist :
        for var in varlist :
#
#           extract model name            
            expidsplitinfo=getexpidsplit.getexpidsplit(expid=expid)
            model=expidsplitinfo['model']

#           frequency of original data
            if ( ( model == 'NorESM2-LM' \
                or model == 'NorESM2-MM' ) and \
                   ( var == 'tasmin' \
                  or var == 'tasmax' ) ) :
                freqfile = 'daily'
            else :
                freqfile = 'monthly'
#
#           experiment ssp245 (some models run up to 2500)            
            concatenatenetcdf.concatenatenetcdf(expid=expid,var=var,freqfile=freqfile,yearrange=[-10000,2100])

#           find the corresponding piControl period
            historicalinfo=getparentexpidinfo.getparentexpidinfo(expid=expid, var=var, freqfile=freqfile)       # historical <-- ssp245
            piControlinfo=getparentexpidinfo.getparentexpidinfo(expid=historicalinfo['expid'], var=var, freqfile=freqfile)  # piControl <-- historical

            year0=piControlinfo['branchyear']+165
#
            concatenatenetcdf.concatenatenetcdf(expid=piControlinfo['expid'],var=var,freqfile=freqfile,yearrange=[year0,year0+85])   
