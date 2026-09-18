import numpy as np
import math

import getcmorvarcomponents
import convert3dplev19
import convert3dzlev20
import convert3dcolumn
import convert2dpfull
import convert2dphalf
import convert2dheightdelta
import readsinglefieldgeneral

import os, sys

import copy

#sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
#import readsinglefieldgeneral

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getconversionfactorunits
import getstandardunits

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

def obtainfield(expid,var,year,month,day,hour,desiredunits,cdim,freqfile) :
#--------------
    '''
    AIM 
        For one specific year and month

    INPUT
        expid
        var
        year
        month
        day hour
        desiredunits
        cdim : '2d', '3d', '3d-plev''

    RETURNS structure
        

    CALLED BY
        cmorize_internal

    CALLS
        getcmorvarcomponents    : returns clist,wlist,cnoemer,action
        readsinglefieldgeneralgeneral :[ 
        getstandardunits
        convert3dplev19    : 3d model levels -> 3d press levels
        convert3dzlev20    : 3d model levels -> 3d height levels
        convert3dcolumn    : 3d model -> 2d
        convertd2pfull            
        convert2dphalf
        getconversionfactorunits

    MODIFICATION
        (2025-05-21) extension to zlev20 (altitude)
        (2026-02-07) added input variables : day and hour

    '''

    print('+++ obtainfield +++')

#   1. FIND THE DATE
    cyear=str("%4.4i"% (year))
    cmonth=str("%2.2i"% (month))
    if ( freqfile == 'monthly' \
      or freqfile == 'fixed' ) :
        date=cyear+'-'+cmonth    # yyyy-mm
    elif ( freqfile== '3hourly') :
        cday=str("%2.2i"% (day))
        chour=str("%2.2i"% (hour))
        date=cyear+'-'+cmonth+'-'+cday+'-'+chour+':00:00'
    else :
        print('+++ obtainfield +++')
        print('No date recognized')
        quit()    


#   2. READ ORIGINAL DATA 
#   2.1 contributing fields
    clist,wlist,cnoemer,action = getcmorvarcomponents.getcmorvarcomponents(var=var) # contains final units
    ncomp=len(clist)

#   2.2 teller : add up contributions
    for icomp in range(0,ncomp) :

#       read component
        tmp=readsinglefieldgeneral.readsinglefieldgeneral(expid, clist[icomp], date) # contains original units

#       initialization of total field
        if ( icomp== 0 ) :
            data=copy.deepcopy(tmp)
            ndim=data['field'].ndim
            if   ( ndim == 2 ) : data['field'][:,:] = 0.
            elif ( ndim == 3 ) : data['field'][:,:,:] = 0.
            else :
                print('No # dimensions recognized : ', ndim)
                quit()

#       check whether all units are the same
        if ( tmp['units'] != data['units'] ) : 
            print('Components have different units')
            print('Up to now : ', data['units'])
            print('Latest contribution : ', tmp['units'])
            print('All components : ', clist)
            print('Latest component : ', clist[icomp])
            quit()

#       add the component contribution
        data['field'] = data['field'] + tmp['field'] * wlist[icomp]
#           
#   2.3 noemer : division if needed 
    if ( cnoemer != None ) :

        tmp=readsinglefieldgeneral.readsinglefieldgeneral(expid, cnoemer, date) 

#       data['field'] = np.where( tmp['field'] >= 0., data['field'] / tmp['field'], 0.) 
        data['field'] =  data['field'] / ( tmp['field'] + 1.e-10 ) 

#   2.4 check standard writing of units
    data['units'] = getstandardunits.getstandardunits(units=data['units'])

#   3. POSSIBLE CONVERSIONS
#   3.1 conversion to plev19
    if ( cdim == '3d-plev19' ) : 
        data = convert3dplev19.convert3dplev19(data=data) 

#   3.2 conversion to zlev20
    if ( cdim == '3d-zlev20' ) :
        zdata = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'Z3', date)   # geopotential height [m] 
        data = convert3dzlev20.convert3dzlev20(data=data, zdata=zdata)        

#   3.2 convert to column burden
    if ( action == 'columnintegrate' ) :
        ptropdata = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'TROP_P', date)                   # read PTROP
        tdata     = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'T'     , date)                   # read T 
        data = convert3dcolumn.convert3dcolumn(data=data, ptropdata=ptropdata, tdata=tdata, var=var) 

#
#   3.3 surface pressure to pfull
    if ( action == 'expand' and var == 'pfull' ) :
#       tdata = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'T'     , date)   # to have all the hyai, ... data
        tdata = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'O3'     , date)  # only to have all the hyai, ... data
        data  = convert2dpfull.convert2dpfull(psdata=data, tdata=tdata,var=var)

#   3.4 surface pressure to phalf
    if ( action == 'expand' and var == 'phalf' ) :
        tdata = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'T'     , date)  # to have all the hyai, ... data
        data  = convert2dphalf.convert2dphalf(psdata=data, tdata=tdata,var=var)

#   3.5 volume
    if ( action == 'special' and var == 'volume' ) :
        tdata = readsinglefieldgeneral.readsinglefieldgeneral(expid, 'T'     , date)  # to have all the hyai, ... data        
        data = convert2dheightdelta.convert2dheightdelta(psdata=data, tdata=tdata,var=var) # heightdelta [in m]

#        print('DELTA HEIGHT MEAN : ', np.mean(data['field'], axis=(1,2)))

        area = areafraction.areafraction(longitude=data['longitude'], latitude=data['latitude'], outputtype='area') # area [in m2]
#
        for ilev in range(data['nlev']) :               
            data['field'][ilev,:,:] = data['field'][ilev,:,:] * area 

        data['units'] = 'm3'

#        print('TOTAL AREA   : ', np.sum(area))
#        print('TOTAL VOLUME : ', np.sum(data['field']))
#        print('MEAN HEIGHT  : ', np.sum(data['field'])/(4.*math.pi*6370e3*6370e3))
#        quit()

#
    print('... here ...')     

#   4. GO TO DESIRED UNITS
#   check units
    factor = getconversionfactorunits.getconversionfactorunits(origunits=data['units'],finalunits=desiredunits,var=var)
    data['field'] = data['field'] * factor
    data['units'] = desiredunits
#
    return data
