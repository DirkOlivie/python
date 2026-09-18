import numpy as np

import getperiodlist
import readmeancolumnintegral
import readmeanlayer
import readmeanmap

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lat2latbnds
import lon2lonbnds
import readnc
import intpfieldregular



def readdistribution ( expid, var, typevar, timedescription, finalresolution ):
#-------------------
#
    '''
    INPUT
        expid
        var : CHBR3 / CHBR3_columnburden / CHBR3_surfacelayer / CHBR3_secondsurfacelayer
        typevar : '' / 'glob' / 'SEA'
        timedescription : 

    '''
# get the periodlist
    periodlist=getperiodlist.getperiodlist(timedescription=timedescription)
    nperiod=len(periodlist)

# loop over all periods
    for iperiod in range(0,nperiod) :
       
        period=periodlist[iperiod] # xxxx-yyyy-SSS

        line=period.split('-')
        year0=int(line[0])      # conversion string -> integer
        year1=int(line[1])      # conversion string -> integer 
        season=line[2]

# read the data for individual period (currently only for 2dim fields)
        if ( "_columnburden" in var ) :
            varorig=var.split("_columnburden")[0]
            tmp=readmeancolumnintegral.readmeancolumnintegral(expid=expid, var=varorig, year0=year0, year1=year1, season=season) 
        elif ( "_surfacelayer" in var ) : 
            varorig=var.split("_surfacelayer")[0]
            tmp=readmeanlayer.readmeanlayer(expid=expid, var=varorig, year0=year0, year1=year1, season=season, clayer='surfacelayer')
        elif ( "_secondsurfacelayer" in var ) :      
            varorig=var.split("_secondsurfacelayer")[0]
            tmp=readmeanlayer.readmeanlayer(expid=expid, var=varorig, year0=year0, year1=year1, season=season, clayer='secondsurfacelayer')
        elif ( "_thirdsurfacelayer" in var ) :      
            varorig=var.split("_thirdsurfacelayer")[0]
            tmp=readmeanlayer.readmeanlayer(expid=expid, var=varorig, year0=year0, year1=year1, season=season, clayer='thirdsurfacelayer')
        else : 
            tmp=readmeanmap.readmeanmap(expid=expid, var=var, year0=year0, year1=year1, season=season)
#
# possible weighting
#       read also LANDFRAC
        landfrac=readmeanmap.readmeanmap(expid=expid, var='LANDFRAC', year0=year0, year1=year1, season=season)

#       read also ICEFRAC : WRONG - READS ALSO LANDFRAC - BUT NOT USED
        icefrac=readmeanmap.readmeanmap(expid=expid, var='LANDFRAC', year0=year0, year1=year1, season=season)    
#              
#       areafraction (as a weight)
        areaweight=areafraction.areafraction(latitude=tmp['latitude'],longitude=tmp['longitude'],outputtype='weight', landfraction=landfrac['field'], region=typevar)

# create and fill the final empty array 
        if ( iperiod == 0 ) :
           nlat,nlon = tmp['field'].shape
           field=np.zeros([nperiod,nlat,nlon])
           weight=np.zeros([nperiod,nlat,nlon])

        field[iperiod,:,:]  = tmp['field']
        weight[iperiod,:,:] = areaweight[:,:] # but can be more complicated (including icefra or 
#
# interpolate to new resolution
    if ( finalresolution == 'orig' ) :
        newfield = field
        newweight = weight
    else :
        if   (  finalresolution == '2x2' ) : 
            year=291
            expid='n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.2025-10-29'    
        elif ( finalresolution == '1x1' ) : 
            year=1
            expid='n1850.ne30_tn14.noresm3_0_beta04-run1_yr001.20251103'
        else :
            print('+++ readdistribution +++')
            print('No final resolution recognized : ', finalresolution)
            quit()
#       
#       final grid
        landfrac=readmeanmap.readmeanmap(expid=expid, var='LANDFRAC', year0=year, year1=year, season='YEA')
        latitude2=landfrac['latitude']
        longitude2=landfrac['longitude']
        latoutbnds = lat2latbnds.lat2latbnds(latitude2)
        lonoutbnds = lon2lonbnds.lon2lonbnds(longitude2)
        nlat2=len(latitude2)
        nlon2=len(longitude2)
#
#       original grid
        latinbnds = lat2latbnds.lat2latbnds(tmp['latitude'])
        loninbnds = lon2lonbnds.lon2lonbnds(tmp['longitude'])
#
#       interpolation
        newfield=intpfieldregular.intpfieldregular(infield=field, latinbd=latinbnds, latoutbd=latoutbnds, loninbd=loninbnds, lonoutbd=lonoutbnds)
#
#       weight
        newweight = np.zeros([nperiod,nlat2,nlon2])
        ttt=areafraction.areafraction(latitude=latitude2,longitude=longitude2,outputtype='weight', landfraction=landfrac['field'], region=typevar)
        for iperiod in range(0,nperiod) :
            newweight[iperiod,:,:] = ttt[:,:]

#   return data
    data={'field'      : newfield, \
          'weight'     : newweight, \
          'periodlist' : periodlist, \
          'variable'   : var, \
          'units'      : tmp['units']}
#
    return data
