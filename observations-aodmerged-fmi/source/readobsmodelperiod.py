import numpy as np

#import readobsmonth_aodmergedfmi
import readobsmonth_toccopernicus
import readobsmonth_aodmergedfmi
import readmodelmonth
import interpolatemodelperiod
import modifymask

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getfinalunits

sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import getbasicexpidname

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy-cmorized/source')
import readallcmorizedfield

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition


def readobsmodelperiod(expid, var, year0, year1):
#--------------------------  
    '''
    REMARK
        model results are interpolated to the observational grid

    INPUT
        expid
        var
        year0
        year1
 
    RETURN
        structure containing 
               var
               field[nlon x nlat x ntime]

    CALLED BY
        getseries
               
    CALLS
        readobsmonth_toccopernicus  [sets field=0 and mask=0 if field value is not finite]
        readmodelmonth
        interpolatemodelperiod
        modifymask
        getfinalunits
    '''
#---------------------------------------------------------
#
    print('+++ readobsmodelperiod +++')
    print('expid : ', expid)

    nmonth=12
    nyear=year1-year0+1

    ntime=nyear*nmonth # total time points

#   Check dataformat : rawnoresm or cmorized
                                                                
    if ( expid != 'aodmergedfmi' and expid != 'toccopernicus' ) :
        basicexpid = getbasicexpidname.getbasicexpidname(expid=expid,date=str(year0)+'-01') 
        expidinfo  = experimentdefinition.getexpidinfo(expid=basicexpid)
        dataformat = expidinfo['dataformat'] # rawnoresm or cmorized    
        project    = expidinfo['project']
    else :
        dataformat = None

#   Option 1 for : aodmergedfmi, toccopernicus, rawnoresm data
    if ( expid == 'aodmergedfmi' \
      or expid == 'toccopernicus'  \
      or dataformat == 'rawnoresm' ) : 

        itime=0
        for iyear in range(0,nyear): 
            for imonth in range(0,nmonth):

                year  = year0  + iyear
                month = imonth + 1

                if   ( expid == 'aodmergedfmi'  ) : tmp = readobsmonth_aodmergedfmi.readobsmonth_aodmergedfmi(  var=var, year=year, month=month) # read observations 1 month
                elif ( expid == 'toccopernicus' ) : tmp = readobsmonth_toccopernicus.readobsmonth_toccopernicus(var=var, year=year, month=month) # read observations 1 month
                elif ( dataformat == 'rawnoresm' ) : tmp = readmodelmonth.readmodelmonth(           expid=expid, var=var, year=year, month=month) # read model 1 month  
                else :
                    print('+++ readobsmodelperiod +++')
                    print('No choice recognized')
                    quit()

                if ( iyear == 0 and imonth == 0 ) :

                    nlon=len(tmp['longitude'])
                    nlat=len(tmp['latitude'])

#                   make empty 3D structure 
                    field = np.zeros([ntime,nlat,nlon],dtype=float)
                    mask  = np.zeros([ntime,nlat,nlon],dtype=float)

#                   make empty 1D structure (for time)
                    yearlist=np.zeros(ntime,dtype=int)
                    monthlist=np.zeros(ntime,dtype=int)
                    timelist=np.zeros(ntime,dtype=float) # decimalyearlist

                field[itime,:,:] = tmp['field']
                mask[itime,:,:]  = tmp['mask']
                yearlist[ itime] = year
                monthlist[itime] = month
                timelist[ itime] = float(year) + ( float(imonth) + 0.5 ) / float(nmonth) # decimalyearlist

                itime = itime + 1
#
#   Option 2 for : cmorized data
    elif ( dataformat == 'cmorized' ) :
        if (var == 'toc' ) : 
            cvar='o3_columnburden'
        else :
            print('+++ readobsmodelperiod +++')
            print('No dataformat recognized : ', dataformat)
            quit()

        tmp = readallcmorizedfield.readallcmorizedfield( expid=expid, var=cvar, year0=year0, year1=year1, project=project)
        
        field     = tmp['field']
        mask      = tmp['field'] * 0. + 1.
        yearlist  = tmp['yearlist']
        monthlist = tmp['monthlist']
        timelist  = yearlist + ( monthlist - 0.5 ) / float(nmonth)

#   No option recognized
    else :
        print('No dataformat recognized : ', dataformat)
        quit()


#   return data structure
    data = {'var'       : var, \
            'units'     : tmp['units'], \
            'field'     : field, \
            'mask'      : mask, \
            'longitude' : tmp['longitude'] , \
            'latitude'  : tmp['latitude'], \
            'yearlist'  : yearlist, \
            'monthlist' : monthlist, \
            'timelist'  : timelist, \
            'ntime'     : ntime}

#   interpolate model to standard observational grid (so not for obsevations)
    if ( expid != 'aodmergedfmi' \
    and expid != 'toccopernicus' ) :
        data=interpolatemodelperiod.interpolatemodelperiod(data=data)                 # to observational grid
        data=modifymask.modifymask(data=data,var=var,year0=year0,year1=year1) # to mask of original grid (exclude points whcich have not been observed)
# 
#   standardize units
    newunits,factor=getfinalunits.getfinalunits(var=data['var'], units=data['units'])
    data['field'] = data['field']*factor
    data['units'] = newunits

    return data
