import numpy as np

import getfinalexpidinfo
import aerocomize_internal

def aerocomize(expid,var,version,filetype,freqfile,overwrite=False) :
#-------------
    '''
    INPUT
        expid
        var
        overwrite

    CALLS
        getfinalexpidinfo
        aerocomize_internal

    MODIFICATIONS
        (2024-05-24) no_overwrite 

    '''

    finalexpidinfo=getfinalexpidinfo.getfinalexpidinfo(expid=expid)
    year0=finalexpidinfo['year0']
    year1=finalexpidinfo['year1']
#
    if ( filetype == 'one-year-per-file' ) :  

#        list of all years to be done
         yearlist=np.arange(year0,year1+1,dtype=int)

#        loop over all years    
         for year in yearlist:
             aerocomize_internal.aerocomize_internal(expid=expid, var=var, year0=year, year1=year, version=version, freqfile=freqfile, overwrite=overwrite)
#
    elif ( filetype == 'all-years-in-one-file' ) :

         aerocomize_internal.aerocomize_internal(expid=expid, var=var, year0=year0, year1=year1, version=version, freqfile=freqfile, overwrite=overwrite) 
#
    else :
        print('No filetype recognized : ', filetype)
        quit()

