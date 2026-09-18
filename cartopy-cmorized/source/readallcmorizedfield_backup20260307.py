import glob
import numpy as np
from netCDF4 import Dataset

import sys
#sys.path.insert(0,'/nird/home/olivie/scripts-python')
#import experimentdefinition

sys.path.insert(0,'/nird/home/olivie/scripts-python-cmip6-v2')
import getrawdirectory
import getperiodlist
import getrealm
import getvertcoordinfo
import getexpidsplit

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import calculate4dpressure
import hybnds2hy
import interp1d
import getlenintervaloverlap
import readnc
import getstandardunits

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

def readallcmorizedfield( expid, var, year0, year1, project=None):
########################
#
    '''
    REMARK
        contains corrections for EMAC
        cl :    is in 0-1 with units "-"
                should be 0-100 with units "%"
        cl : in the filename 'cl_corrected'

    INPUT
        expid
        var
        year0 : first year to be read
        year1 : last year to be read

    CALLS
        readallcmorizedfield [calls recursively itself]
        getexpidsplit
#        getexpidinfo
        getvertcoordinfo
        getrawdirectory
        getrealm
        getperiodlist
        calculate4dpressure

    MODIFCICATION 
        (2025-01-28)
        (2025-05-25) 
            extension to surface layer
            extension to column burden

    '''
#
#   constants
    Rair  = 287.058
    Mwair =  28.97    # this should be Mwair !!!!!
    Nav   =   6.022e23

    print('+++ readallcmorizedfield +++')
    print('var      : ', var)
    print('year0    : ', year0)
    print('year1    : ', year1)
#
###########################
#   Ozone  partial pressure
##########################
    if ( var == 'o3_as_partpress' ) :

        data = readallcmorizedfield( expid=expid, var='o3', year0=year0, year1=year1, project=project )

        data['field'] = data['field']*data['pfull'] # partial pressure = vmr * pressure
        data['units'] = 'Pa'   
#
################################
#   Extract surface layer values
################################
    elif ( var == 'ch4_surfacelayer' \
        or var == 'co_surfacelayer' \
        or var == 'h2_surfacelayer' \
        or var == 'o3_surfacelayer' \
        or var == 'oh_surfacelayer' ) :

        print('PASSING HERE ...')

#       split
        line=var.split('_')
        varorig=line[0]        

#       read original field
        origdata=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull
#        
        nlev=origdata['nlev']
        pfull=origdata['pfull']
        print(pfull.shape)
        if ( np.max(pfull[:,0,:,:]) >= np.max(pfull[:,nlev-1,:,:]) ) : isurface=0
        else : isurface=nlev-1
#
        data = { 'field'     : np.squeeze(origdata['field'][:,isurface,:,:]), \
                 'longitude' : origdata['longitude'], \
                 'latitude'  : origdata['latitude'], \
                 'nlon'      : origdata['nlon'], \
                 'nlat'      : origdata['nlat'], \
                 'nlev'      : 0, \
                 'units'     : origdata['units'], \
                 'yearlist'  : origdata['yearlist'], \
                 'monthlist' : origdata['monthlist'], \
                 'datelist'  : origdata['datelist'], \
                 'ntime'     : origdata['ntime']}
#
###################################
#   columnburden using volume (not just layer thickness but whole 3D volume
###################################
    elif ( var == 'lossch4_columnburdenfromvolume' ) :
#
#       derived var info
        if   ( var == 'lossch4_columnburdenfromvolume'                       ) : varorig='lossch4'        ; Mw=16.0406 ; limit=''
        else :
            print('No var recognized : ', var)
            quit()

#       read original field (always)
        OD=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull
        field = OD['field']

        nlon = OD['nlon']
        nlat = OD['nlat']
        nlev = OD['nlev']
        ntime = OD['ntime']
        units = OD['units']

        area = areafraction.areafraction(latitude=OD['latitude'], longitude=OD['longitude'], outputtype='area') 

#       read airmass (always)
        VOLUME=readallcmorizedfield( expid=expid, var='volume', year0=year0, year1=year1, project=project)

#
#       column integration
        column = np.zeros((OD['ntime'], OD['nlat'], OD['nlon']), dtype=float)

#       
        for ilev in range(nlev) :

            dv = VOLUME['field'][:,ilev,:,:] / area[:,:]

            units = getstandardunits.getstandardunits(units=units)

            if   ( units=='m-3'                ) : column = column + dv * field[:,ilev,:,:]                         ; newunits = 'm-2'
            elif ( units=='cm-3'               ) : column = column + dv * field[:,ilev,:,:] *1.e6                   ; newunits = 'm-2'
            elif ( units=='cm-2 cm-3'          ) : column = column + dv * field[:,ilev,:,:] *1.e6                   ; newunits = 'cm-2 m-2'
            elif ( units=='molecules cm-3 s-1' ) : column = column + dv * field[:,ilev,:,:] *1.e6 * Mw *1.e-3 / Nav ; newunits = 'kg m-2 s-1'
            elif ( units=='mol m-3 s-1'        ) : column = column + dv * field[:,ilev,:,:]       * Mw *1.e-3       ; newunits = 'kg m-2 s-1'
            elif ( units=='kg m-3 s-1'         ) : column = column + dv * field[:,ilev,:,:]                         ; newunits = 'kg m-2 s-1'
            else :
                print('columnintegration : Unit not recognized : '+units)
                quit()


#       Generating return data
        data = { 'field'     : column, \
                 'longitude' : OD['longitude'], \
                 'latitude'  : OD['latitude'], \
                 'nlon'      : OD['nlon'], \
                 'nlat'      : OD['nlat'], \
                 'nlev'      : 0, \
                 'units'     : newunits, \
                 'yearlist'  : OD['yearlist'], \
                 'monthlist' : OD['monthlist'], \
                 'datelist'  : OD['datelist'], \
                 'ntime'     : OD['ntime']}

#
###################################
#   columnburden using airmass
###################################
    elif ( var == 'ch4_columnburdenfromairmass' \
        or var == 'o3_columnburdenfromairmass' ) :
#
#       derived var info
        if   ( var == 'ch4_columnburdenfromairmass'                       ) : varorig='ch4'        ; Mw=16.0406 ; limit=''
        elif ( var == 'o3_columnburdenfromairmass'                        ) : varorig='o3'         ; Mw=47.9982 ; limit=''   
        else :
            print('No var recognized : ', var)
            quit()

#       read original field (always)
        OD=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull
        field = OD['field']

        nlon = OD['nlon']
        nlat = OD['nlat']
        nlev = OD['nlev']
        ntime = OD['ntime']
        units = OD['units']

#       read airmass (always)
        AIRMASS=readallcmorizedfield( expid=expid, var='airmass', year0=year0, year1=year1, project=project)
#
#       column integration
        column = np.zeros((OD['ntime'], OD['nlat'], OD['nlon']), dtype=float)

#       
        for ilev in range(nlev) :

            dm = AIRMASS['field'][:,ilev,:,:]

            units = getstandardunits.getstandardunits(units=units)

            if   ( units=='mol mol-1'          ) : column = column + dm * field[:,ilev,:,:] * Mw / Mwair                         ; newunits = 'kg m-2'
            elif ( units=='kg kg-1'            ) : column = column + dm * field[:,ilev,:,:]                                      ; newunits = 'kg m-2'
            elif ( units=='kg-1'               ) : column = column + dm * field[:,ilev,:,:]                                      ; newunits = 'm-2'
            elif ( units=='m-3'                ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = 'm-2'
            elif ( units=='cm-3'               ) : column = column + dm * field[:,ilev,:,:] / density    *1.e6                   ; newunits = 'm-2'
            elif ( units=='cm-2 cm-3'          ) : column = column + dm * field[:,ilev,:,:] / density    *1.e6                   ; newunits = 'cm-2 m-2'
            elif ( units=='molecules cm-3 s-1' ) : column = column + dm * field[:,ilev,:,:] / density    *1.e6 * Mw *1.e-3 / Nav ; newunits = 'kg m-2 s-1'
            elif ( units=='mol m-3 s-1'        ) : column = column + dm * field[:,ilev,:,:] / density          * Mw *1.e-3       ; newunits = 'kg m-2 s-1'
            elif ( units=='kg m-3 s-1'         ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = 'kg m-2 s-1'
            elif ( units=='m-1'                ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = ''
            elif ( units=='km-1'               ) : column = column + dm * field[:,ilev,:,:] / density * 1.e-3                    ; newunits = ''
            elif ( units=='m3 m-3'             ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = 'm3 m-2'
            else :
                print('columnintegration : Unit not recognized : '+units)
                quit()


#       Generating return data
        data = { 'field'     : column, \
                 'longitude' : OD['longitude'], \
                 'latitude'  : OD['latitude'], \
                 'nlon'      : OD['nlon'], \
                 'nlat'      : OD['nlat'], \
                 'nlev'      : 0, \
                 'units'     : newunits, \
                 'yearlist'  : OD['yearlist'], \
                 'monthlist' : OD['monthlist'], \
                 'datelist'  : OD['datelist'], \
                 'ntime'     : OD['ntime']}

#
###################################
#   columnburden using pressure
###################################
    elif ( var == 'ch4_columnburden' \
           \
        or var == 'ch4lossoh_columnburden' \
        or var == 'ch4losscl_columnburden' \
        or var == 'ch4losso1d_columnburden' \
        or var == 'lossch4_columnburden' \
           \
        or var == 'ch4lossoh_columnburden_abovetropopause' \
        or var == 'ch4losscl_columnburden_abovetropopause' \
        or var == 'ch4losso1d_columnburden_abovetropopause' \
           \
        or var == 'ch4lossoh_columnburden_belowtropopause' \
        or var == 'lossch4_columnburden_belowtropopause' \
           \
        or var == 'co_columnburden' \
        or var == 'oh_columnburden' \
        or var == 'o3_columnburden' \
           \
        or var == 'emilnox_columnburden' ) :
#
#       derived var info
        if   ( var == 'ch4_columnburden'                       ) : varorig='ch4'        ; Mw=16.0406 ; limit=''
        elif ( var == 'ch4lossoh_columnburden'                 ) : varorig='ch4lossoh'  ; Mw=16.0406 ; limit=''
        elif ( var == 'ch4losscl_columnburden'                 ) : varorig='ch4losscl'  ; Mw=16.0406 ; limit=''
        elif ( var == 'ch4losso1d_columnburden'                ) : varorig='ch4losso1d' ; Mw=16.0406 ; limit=''
        elif ( var == 'lossch4_columnburden'                   ) : varorig='lossch4'    ; Mw=16.0406 ; limit=''
#
        elif ( var == 'ch4lossoh_columnburden_abovetropopause' ) : varorig='ch4lossoh'  ; Mw=16.0406 ; limit='abovetropopause'
        elif ( var == 'ch4losscl_columnburden_abovetropopause' ) : varorig='ch4losscl'  ; Mw=16.0406 ; limit='abovetropopause'
        elif ( var == 'ch4losso1d_columnburden_abovetropopause') : varorig='ch4losso1d' ; Mw=16.0406 ; limit='abovetropopause'
#
        elif ( var == 'ch4lossoh_columnburden_belowtropopause' ) : varorig='ch4lossoh'  ; Mw=16.0406 ; limit='belowtropopause'
        elif ( var == 'lossch4_columnburden_belowtropopause'   ) : varorig='lossch4'    ; Mw=16.0406 ; limit='belowtropopause'

        elif ( var == 'co_columnburden'                        ) : varorig='co'         ; Mw=28.0104 ; limit=''

        elif ( var == 'oh_columnburden'                        ) : varorig='oh'         ; Mw=17.0068 ; limit=''   

        elif ( var == 'o3_columnburden'                        ) : varorig='o3'         ; Mw=47.9982 ; limit=''   

        elif ( var == 'emilnox_columnburden'                   ) : varorig='emilnox'    ; Mw=14.006740 ; limit=''    # molar weight of N

        else :
            print('No var recognized : ', var)
            quit()

#       read original field (always)
        OD=readallcmorizedfield( expid=expid, var=varorig, year0=year0, year1=year1, project=project) # will include pfull
        field = OD['field']

        nlon = OD['nlon']
        nlat = OD['nlat']
        nlev = OD['nlev']
        ntime = OD['ntime']
        units = OD['units']

#       read temperature (always)
        T=readallcmorizedfield( expid=expid, var='ta', year0=year0, year1=year1, project=project)
        nlev0=T['nlev'] # original number of levels
#
        print('nlev  : ', nlev )
        print('nlev0 : ', nlev0)
        print('var   : ', var)

        if ( nlev0 == nlev) : 
            t3d=T['field']
        else :                # temperature is, e.g., p19 field

            print ('BEFORE TOPOGRAPHY CORRECTION')
            print('#levels : ', nlev0)
            print('minimum temperature : ', np.min(T['field']))
            print('maximum temperature : ', np.max(T['field']))

#           print('START CORRECTION FOR VALUES BELOW TOPOGRAPHY')
#           loop over original levels (p19 levels)
            for ilev in range(T['nlev']-2,-1,-1) :
                print(ilev, np.max(T['field'][:,ilev,:,:]))
                T['field'][:,ilev,:,:] = np.where(T['field'][:,ilev,:,:] > 1.e10, T['field'][:,ilev+1,:,:],T['field'][:,ilev,:,:])
                print(ilev, np.max(T['field'][:,ilev,:,:]))

            print ('AFTER TOPOGRAPHY CORRECTION')
            print('minimum temperature : ', np.min(T['field']))
            print('maximum temperature : ', np.max(T['field']))
#
#           extrapolate value to 0 hPa and 1200 hPa
            ntime0=T['ntime']
            nlat0=T['nlat']
            nlon0=T['nlon']

            nlev0=nlev0+2  # increase number of levels by two

            Ttmp     = np.zeros((OD['ntime'], nlev0, OD['nlat'], OD['nlon']), dtype=float)
            Pfulltmp = np.zeros((OD['ntime'], nlev0, OD['nlat'], OD['nlon']), dtype=float)        

            Ttmp[:,1:nlev0-1,:,:] = T['field'][:,:,:,:] 
            print('Pfulltmp.shape : ', Pfulltmp.shape)
            print('T[pfull].shape : ', T['pfull'].shape)

            Pfulltmp[:,1:nlev0-1,:,:] = T['pfull'][:,:,:,:]

            Ttmp[:,0      ,:,:] = T['field'][:,0      ,:,:]
            Ttmp[:,nlev0-1,:,:] = T['field'][:,nlev0-3,:,:] 


            if (   np.mean(Pfulltmp[:,1      ,:,:]) >= 90000. \
             and   np.mean(Pfulltmp[:,nlev0-2,:,:]) <= 10000.) : Pfulltmp[:,0      ,:,:] = 120000. ; Pfulltmp[:,nlev0-1,:,:] = 0. ; 
                                                        
            elif ( np.mean(Pfulltmp[:,nlev0-2,:,:]) >= 90000. \
             and   np.mean(Pfulltmp[:,1      ,:,:]) <= 10000.) : Pfulltmp[:,nlev0-1,:,:] = 120000. ; Pfulltmp[:,0,:,:] = 0.                                 ;   
            else :
                print('Pressure at bottom and top level seem out of range ...')
                print('Level 1       : ', np.mean(Pfulltmp[:,1      ,:,:])) 
                print('Level nlev0-2 : ', np.mean(Pfulltmp[:,nlev0-2,:,:]))
                quit()

            T['field'] = Ttmp
            T['pfull'] = Pfulltmp
            T['nlev']  = nlev0

            print ('AFTER EXTRAPOLATION')
            print('minimum temperature : ', np.min(T['field']))
            print('maximum temperature : ', np.max(T['field']))

#           interpolate temperature to level grid (from p19)
            t3d=np.zeros((OD['ntime'], OD['nlev'], OD['nlat'], OD['nlon']), dtype=float)

#        print('START INTERPOLATION')
#        for itime in range(OD['ntime']) :
#            print('itime : ', itime)
#            for ilat in range(0,OD['nlat']) :
#                for ilon in range(0,OD['nlon']) :
#                   correct T-profile for 1e+19
#                    t1d=T['field'][itime,:,ilat,ilon]
#                    for ilev in range(T['nlev']-1,-1,-1) :
#                        if ( t1d[ilev] > 1.e10 ) : t1d[ilev] = t1d[ilev+1]
#                   interpolate
#                    t3d[itime,:,ilat,ilon] = interp1d.interp1d(x=T['pfull'][itime,:,ilat,ilon], \
#                                                               fx=t1d[:], \
#                                                               y=OD['pfull'][itime,:,ilat,ilon])
#        print('END INTERPOLATION') 

            print('START INTERPOLATION')
            for ilev in range(nlev) : # loop over final levels
                p = OD['pfull'][:,ilev,:,:]
                for ilev0 in range (nlev0-1) : # loop over initial levels
                    pa=T['pfull'][:,ilev0,:,:]    
                    pb=T['pfull'][:,ilev0+1,:,:]

                    pmin=np.minimum(pa,pb)
                    pmax=np.maximum(pa,pb)

                    isubset = ( p >= pmin ) * ( p <= pmax )

                    t3d[:,ilev,:,:] = np.where(isubset,   (pb-p)/ (pb -pa)*T['field'][:,ilev0,:,:] + (p-pa)/ (pb -pa)*T['field'][:,ilev0+1,:,:], t3d[:,ilev,:,:])
                    alpha=(pb-p)/ (pb -pa)
                    beta=(p-pa)/ (pb -pa)  
#                if ( np.any(isubset) ) : 
#                    print('ilev, ilev0 : ', ilev, ilev0)
#                    print('alpha : ', np.min(alpha[isubset]), np.max(alpha[isubset]))
#                    print('beta  : ', np.min(beta[isubset]), np.max(beta[isubset]))
#                    print('alpha+beta : ', np.min(alpha[isubset]+beta[isubset]), np.max(alpha[isubset]+beta[isubset]))
#                    if ( np.min(alpha[isubset]+beta[isubset]) != 1. or np.max(alpha[isubset]+beta[isubset]) != 1 ) :
#                        print('Not ok ...')
#                        quit()            
#                    if ( np.min(alpha[isubset]) < 0. \
#                      or np.max(alpha[isubset]) > 1. \
#                      or np.min(beta[isubset]) < 0. \
#                      or np.max(beta[isubset]) > 1. ) :
#                        rint('Not ok ... 2')          
#                        quit()   
                                                    
        print('Max : ', np.max(t3d))
        print('Min : ', np.min(t3d))

        print('Max : ', np.max(T['field']))
        print('Min : ', np.min(T['field']))

        print('END INTERPOLATION')
#        quit()

#        print('START INTERPOLATION')
#        for itime in range(OD['ntime']) :
#            print('itime : ', itime)
#            for ilat in range(0,OD['nlat']) :
#                for ilon in range(0,OD['nlon']) :
##                   correct T-profile for 1e+19
#                    t1d=T['field'][itime,:,ilat,ilon]
#                    for ilev in range(T['nlev']-1,-1,-1) :
#                        if ( t1d[ilev] > 1.e10 ) : t1d[ilev] = t1d[ilev+1]
#                   interpolate
#                    t3d[itime,:,ilat,ilon] = interp1d.interp1d(x=T['pfull'][itime,:,ilat,ilon], \
#                                                               fx=t1d[:], \
#                                                               y=OD['pfull'][itime,:,ilat,ilon])
#        print('END INTERPOLATION') 
#            
#       read tropopause pressure
        if ( limit == 'belowtropopause' \
          or limit == 'abovetropopause' ) :
            ptp=readallcmorizedfield( expid=expid, var='ptp', year0=year0, year1=year1, project=project)
            ptrop=ptp['field']

#       column integration
        column = np.zeros((OD['ntime'], OD['nlat'], OD['nlon']), dtype=float)

#       
        for ilev in range(nlev) :

            pressure = OD['pfull'][:,ilev,:,:]          # mid-level pressure
            density  = pressure / Rair / t3d[:,ilev,:,:] # density                         

#           airmass
            dm = abs( OD['phalf'][:,ilev+1,:,:] - OD['phalf'][:,ilev,:,:] ) / 9.81    # dm = dp / g

#           how much does level contributes
            w = np.zeros( ( ntime, nlat, nlon ) )

            print('START WEIGHTING')           
            if ( limit == '' ) : w[:,:,:] = 1.
            elif ( limit == 'above100hPa' ) :
                plim = 10000.
                for itime in range(ntime) :
                    print('itime : ', itime)
                    for ilat in range(nlat) :
                        for ilon in range(nlon) :
                            pa   = OD['phalf'][itime,ilev  ,ilat,ilon]# pressure at ilev interface
                            pb   = OD['phalf'][itime,ilev+1,ilat,ilon]# pressure at ilev+1 interface
                            pmin = np.amin([pa,pb])                                  # minimum of boundary pressures
                            pmax = np.amax([pa,pb])                                  # maximum of boundary pressures
                            w[itime,ilat,ilon] = np.amin([1.,np.amax([0., (pmax-plim) / (pmax-pmin) ])])
            elif ( limit == 'belowtropopause' \
                or limit == 'abovetropopause' ) :

                pa   = OD['phalf'][:,ilev  ,:,:]# pressure at ilev interface
                pb   = OD['phalf'][:,ilev+1,:,:]# pressure at ilev+1 interface 
                pmin = np.minimum(pa,pb)      # pointwise minimum of two arrays 
                pmax = np.maximum(pa,pb)      # pointwise maximum of two arrays

                if (   limit == 'belowtropopause' ) : w = (np.maximum(pmax,ptrop)-np.maximum(pmin,ptrop))/(pmax-pmin)
                elif ( limit == 'abovetropopause' ) : w = (np.minimum(pmax,ptrop)-np.minimum(pmin,ptrop))/(pmax-pmin) 
                else :
                    print('No limit recognized : ', limit)
                    quit()


            else :
                print('No limit recognized : ', limit)
                quit()

            print('END WEIGHTING')

#           combination
            dm = dm * w

            units = getstandardunits.getstandardunits(units=units)

            if   ( units=='mol mol-1'          ) : column = column + dm * field[:,ilev,:,:] * Mw / Mwair                         ; newunits = 'kg m-2'
            elif ( units=='kg kg-1'            ) : column = column + dm * field[:,ilev,:,:]                                      ; newunits = 'kg m-2'
            elif ( units=='kg-1'               ) : column = column + dm * field[:,ilev,:,:]                                      ; newunits = 'm-2'
            elif ( units=='m-3'                ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = 'm-2'
            elif ( units=='cm-3'               ) : column = column + dm * field[:,ilev,:,:] / density    *1.e6                   ; newunits = 'm-2'
            elif ( units=='cm-2 cm-3'          ) : column = column + dm * field[:,ilev,:,:] / density    *1.e6                   ; newunits = 'cm-2 m-2'
            elif ( units=='molecules cm-3 s-1' ) : column = column + dm * field[:,ilev,:,:] / density    *1.e6 * Mw *1.e-3 / Nav ; newunits = 'kg m-2 s-1'
            elif ( units=='mol m-3 s-1'        ) : column = column + dm * field[:,ilev,:,:] / density          * Mw *1.e-3       ; newunits = 'kg m-2 s-1'
            elif ( units=='kg m-3 s-1'         ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = 'kg m-2 s-1'
            elif ( units=='m-1'                ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = ''
            elif ( units=='km-1'               ) : column = column + dm * field[:,ilev,:,:] / density * 1.e-3                    ; newunits = ''
            elif ( units=='m3 m-3'             ) : column = column + dm * field[:,ilev,:,:] / density                            ; newunits = 'm3 m-2'
            elif ( units=='mol m-2 s-1'        ) : column = column +      field[:,ilev,:,:]                    * Mw *1.e-3       ; newunits = 'kg m-2 s-1'
            else :
                print('columnintegration : Unit not recognized : '+units)
                quit()


#       Generating return data
        data = { 'field'     : column, \
                 'longitude' : OD['longitude'], \
                 'latitude'  : OD['latitude'], \
                 'nlon'      : OD['nlon'], \
                 'nlat'      : OD['nlat'], \
                 'nlev'      : 0, \
                 'units'     : newunits, \
                 'yearlist'  : OD['yearlist'], \
                 'monthlist' : OD['monthlist'], \
                 'datelist'  : OD['datelist'], \
                 'ntime'     : OD['ntime']}

#
############
#   Standard
############
    else :
#
        nmonth=12
#
        expidsplitinfo=getexpidsplit.getexpidsplit(expid=expid,project=project)
        model=expidsplitinfo['model']        

#       vertical coordinfo
        vinfo = getvertcoordinfo.getvertcoordinfo(model=model, project=project)
        vtype = vinfo['vtype']
        cp0   = vinfo['cp0']
        cps   = vinfo['cps']
        chyam = vinfo['chyam']       # nlev
        chybm = vinfo['chybm']
        chyai = vinfo['chyai']       # nlev +1  
        chybi = vinfo['chybi']
        chyabnds = vinfo['chyabnds'] # nlev x2
        chybbnds = vinfo['chybbnds']
        clev     = vinfo['clev']     # name of vertical coordinate
        psorigin=vinfo['psorigin']
        pfullorigin = vinfo['pfullorigin']
        phalforigin = vinfo['phalforigin']

#       directory
        directory=getrawdirectory.getrawdirectory(expid=expid,var=var,project=project,freqfile='monthly')
        realm=getrealm.getrealm(var=var,freqfile='monthly',model=model)

#       list of all files with correct variable 
        fvar = var
        if ( model == 'DLR-EMAC' and var == 'cl' ) : fvar='cl_corrected'

        if ( project == 'hyway' ) : 
            regex=fvar+'_monthly_*[0-9].nc'
        else :
            regex=fvar+'_'+realm+'_*[0-9].nc'
        filelist=glob.glob(directory+'/'+regex)
        filelist.sort()

#       list of all periods
        periodlist=getperiodlist.getperiodlist(expid, var, project, freqfile='monthly')

#       loop over all periods and read all the files which have at least a partial overlap
        first=True

        for iperiod in range(0,periodlist['nperiod']) :

            period=periodlist['periodlist'][iperiod]
            year0file=periodlist['year0list'][iperiod]
            year1file=periodlist['year1list'][iperiod]

            if ( year0 <= year1file and year1 >= year0file ) :

#               read netcdf file
                if ( project == 'hyway' ) :
                    regex=fvar+'_monthly_*'+period+'.nc'
                else :
                    regex=fvar+'_'+realm+'_*'+period+'.nc'
                filelist=glob.glob(directory+'/'+regex)

                if ( len(filelist) != 1 ) :
                    print('Expected only 1 file in list')
                    print('filelist : ', filelist)

                nc_f=filelist[0]

                print(nc_f)
                nc_fid= Dataset(nc_f, 'r')
    
# reading actual field
                tmpfieldlist=np.squeeze(np.array(nc_fid.variables[var][:]))
                if ( model == 'DLR-EMAC' and var == 'cl' ) :
                    tmpfieldlist=tmpfieldlist*100.

# only for first file
                if ( first ) :   

                    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
                    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
                    if ( model == 'CNRM-ESM2-1' and var == 'emich4' ) :
                        lats = lats[:,0]
                        lons = lons[0,:]

                    if ( model == 'DLR-EMAC' and var == 'cl' ) : 
                        units='%'
                    elif ( model == 'CESM2' and var == 'cl' ) :
                        units='%'
                    elif ( model == 'CESM2' and var == 'ta' ) :
                        units='K'
                    elif ( model == 'CESM2' and var == 'o3' ) :
                        units='mol mol-1'
                    elif ( model == 'CESM2' and var == 'hus' ) :
                        units='kg kg-1'
                    elif ( model == 'OsloCTM3v1-2' and ( var == 'ps' or var == 'pfull' or var == 'zg' or var == 'airmass' or var == 'lossch4') ) :
                        units=nc_fid.variables[var].unit # no "s"
                    elif ( model == 'CNRM-ESM2-1' and var == 'emich4' ) :
                        units='kg m-2 s-1'                  
                    else : 
                        print('model : ', model)
                        print('var   : ', var)

                        units=nc_fid.variables[var].units

                        if ( model == 'UKESM1-0-LL' and var == 'emilnox' and units == 'mol s-1' ) : 
                            units = 'mol m-2 s-1' 

                    ndim=tmpfieldlist.ndim
                    nlat=len(lats)
                    nlon=len(lons)

                    dimensions = nc_fid.variables[var].dimensions   # ('MT', 'Depth', 'Y', 'X')
                    shape = nc_fid.variables[var].shape             # (1, 10, 850, 712) 

# 3d fields
                    if ( ndim == 4 ) :

# distinguish between model levels (lev as coordinate) and 19 pressure levels
                        if ( clev in dimensions ) : # model levels


                            if ( model == 'EC-Earth3-AerChem' ) :
                                lev_dim = nc_fid.dimensions[clev]
                                nlev = lev_dim.size                                
                            else : 
                                levs=np.array(nc_fid.variables[clev][:]) # model levels 
                                nlev=len(levs)

                            # p0
                            if ( cp0   != '' ) : 
                                if ( model == 'CESM2-v212' ) :
                                    p0 = readnc.readnc(cp0, '/projects/NS11106K/HYway/modelling_repository/CESM2-v212/transient2010s/airmass_monthly_CESM2-v212_hyway_transient2010s_r1_201001-201912.nc')
                                else :
                                    p0   = np.array(nc_fid.variables[cp0][:])   
                            else               : p0   = 1. 
                            # hyam / hybm
                            if ( chyam != '' ) : hyam = np.array(nc_fid.variables[chyam][:]) # hyam
                            if ( chybm != '' ) : hybm = np.array(nc_fid.variables[chybm][:]) # hybm
                            # hyai / hybi
                            if ( chyai != '' ) :
                                if ( model == 'OsloCTM3v1-2' ) :                                     
                                    hyai = readnc.readnc(chyai,'/projects/NS11106K/HYway/modelling_repository/OsloCTM3v1-2/transient2010s/o3_monthly_OsloCTM3v1-2_hyway_transient2010s_r1_201001-201012.nc')
                                    hyai = hyai[0,:] * 100.
                                else : 
                                    hyai = np.array(nc_fid.variables[chyai][:]) # hyai

                            if ( chybi != '' ) :
                                if ( model == 'OsloCTM3v1-2' ) : 
                                    hybi = readnc.readnc(chybi,'/projects/NS11106K/HYway/modelling_repository/OsloCTM3v1-2/transient2010s/o3_monthly_OsloCTM3v1-2_hyway_transient2010s_r1_201001-201012.nc')
                                    hybi = hybi[0,:]
                                else :
                                    hybi = np.array(nc_fid.variables[chybi][:]) # hybi
                                    
                            # hyabnds / hybbnds
                            if ( chyabnds != '' ) : 
                                hyabnds = np.array(nc_fid.variables[chyabnds][:]) # hyabnds
                                hyai = hybnds2hy.hybnds2hy(hyabnds)
                            if ( chybbnds != '' ) : 
                                hybbnds = np.array(nc_fid.variables[chybbnds][:]) # hybbnds
                                hybi = hybnds2hy.hybnds2hy(hybbnds)    

                            # units_ps
                            if ( cps   != '' and psorigin == 'included' ) : units_ps = nc_fid.variables[cps].units      # units of surface pressure

                        elif ( 'plev' in dimensions ) : # 19 pressure levels

                            levs=np.array(nc_fid.variables['plev'][:])   # 19 pressure levels
                            nlev=len(levs) 
                            print(model)
                            if ( model == 'NorESM2-LM' \
                              or model == 'CESM2' ) :
                                units_plev='Pa'
                            else : 
                                units_plev = nc_fid.variables['plev'].units  # units of 19 pressure levels

                        else :
                            print('+++ readallcmorizedfield (1) +++')
                            print('No vertical dimension recognized')
                            quit()
#
# reading surface pressure field
                if ( ndim == 4 and vtype == 'hybrpress' and clev in dimensions and psorigin == 'included' ) : tmppslist=np.squeeze(np.array(nc_fid.variables['ps'][:]))

# generating timefield
                ntime=(year1file-year0file+1)*nmonth

                tmpyearlist  = np.zeros((ntime), dtype=int)
                tmpmonthlist = np.zeros((ntime), dtype=int)
                tmpdatelist  = np.zeros((ntime), dtype='<U7')   # strings of max 7 characters !!!
                for itime in range(0,ntime):
                    year = year0file + itime // nmonth
                    month = itime%nmonth + 1 # module

                    tmpyearlist[itime]  = year
                    tmpmonthlist[itime] = month
        
                    cyear=str("%4.4i"% (year))
                    cmonth= str("%2.2i"% (month))

                    tmpdatelist[itime] = cyear+'-'+cmonth

                nc_fid.close # close file
#
#               concatenate 
                if ( first ) : # create the new arrays
                    fieldlist = tmpfieldlist
                    if ( ndim == 4 and vtype == 'hybrpress' and clev in dimensions and psorigin == 'included' ) : pslist = tmppslist # ps
                    yearlist  = tmpyearlist
                    monthlist = tmpmonthlist
                    datelist  = tmpdatelist
                else :         # concatenate to the arrays
                    fieldlist = np.concatenate( (fieldlist,tmpfieldlist), axis=0 ) 
                    if ( ndim == 4 and vtype == 'hybrpress' and clev in dimensions and psorigin == 'included' ) : pslist=np.concatenate( (pslist,tmppslist), axis=0 ) # ps
                    yearlist  = np.concatenate(  (yearlist,tmpyearlist)           )
                    monthlist = np.concatenate( (monthlist,tmpmonthlist)         )
                    datelist  = np.concatenate(( datelist,tmpdatelist)            )

                first = False

#       number of times
        ntime=len(datelist)

#       data selection between year0 and year1
        isubset = ( yearlist >= year0 ) * ( yearlist <= year1)

#       reduce extent of the field
        if (   ndim == 3 ) : 
            fieldlist = fieldlist[isubset,:,:]           # fiedlist
        elif ( ndim == 4 ) :
            fieldlist = fieldlist[isubset,:,:,:]
            print('DOING FIELD REDUCTION') 
            print('var : ', var)
            print('dimensions : ', dimensions)
            print('vtype : ', vtype)
 
            if ( ( var != 'phalf' and var != 'pfull' ) \
             and ( clev in dimensions ) \
             and ( vtype == 'hybrpress') \
             and ( psorigin == 'included' ) ) :  
                pslist = pslist[isubset,:,:]          
                print('DOING PS REDUCTION') 

#
        if ( ndim == 4 and vtype == 'hybrpress' and clev in dimensions and psorigin == 'external' ) :
            ps=readallcmorizedfield( expid=expid, var='ps',year0=year0, year1=year1, project=project)
            pslist   = ps['field']
            units_ps = ps['units']

#   read also phalf and pfull / calculate from ps  
        if ( ndim == 4 and ( var != 'phalf' and var != 'pfull' ) ) : 

#           model levels
            if ( clev in dimensions ) :

#               height coordinate # UKESM
                if ( vtype == 'hybrheight' ) :  
#                   pfull
                    pfull=readallcmorizedfield( expid=expid, var='pfull',year0=year0, year1=year1, project=project)   # read directly pfull-field
                    field_pfull=pfull['field']
                    units_pfull=pfull['units']                    
#                   phalf
#                   2026-03-15 : HYway commented out        
#                    phalf=readallcmorizedfield( expid=expid, var='phalf',year0=year0, year1=year1, project=project)
#                    field_phalf=phalf['field']
#                    units_phalf=phalf['units']
#               pressure coordinate # NorESM, CESM, OsloCTM3
                elif (vtype == 'hybrpress' ) :                    
#                   pfull
                    if ( pfullorigin == 'ps-based' ) :
                        field_pfull=calculate4dpressure.calculate4dpressure(p0=p0,ps=pslist,hya=hyam,hyb=hybm)  # calculate pfull-field based on ps # before ps = pslist                 
                        units_pfull=units_ps
                    elif ( pfullorigin == 'self' ) :
                        pfull=readallcmorizedfield( expid=expid, var='pfull',year0=year0, year1=year1, project=project)   # read directly pfull-field
                        field_pfull=pfull['field']
                        units_pfull=pfull['units']
                    else :
                        print('pfull not retrieved')

#                   phalf
                    if ( phalforigin == 'ps-based' ) :
                        field_phalf=calculate4dpressure.calculate4dpressure(p0=p0,ps=pslist,hya=hyai,hyb=hybi)  # calculate pfull-field based on ps # before ps = pslist
                        units_phalf=units_ps
                    elif ( phalforigin == 'psbased' ) : 
                        phalf=readallcmorizedfield( expid=expid, var='phalf',year0=year0, year1=year1, project=project)
                        field_phalf=phalf['field']
                        units_phalf=phalf['units']
                    else :
                        print('phalf not retrieved')

                else :
                    print('No vtype recognized : ', vtype)
                    quit() 

#           19 pressure levels
            elif ( 'plev' in dimensions ) : 
                field_pfull=np.zeros((ntime,nlev,nlat,nlon),dtype=float)
                for ilev in range(nlev) :
                    field_pfull[:,ilev,:,:] = levs[ilev]

                field_pfull = field_pfull[isubset,:,:,:]

                units_pfull=units_plev
            else : 
                print('+++ readallcmorizedfield (2) +++')
                print('No vertical dimension recognized')
                quit()

#       reduce extend of yearlist/monthlist/datelist
        yearlist = yearlist[isubset]                                      # yearlist
        monthlist = monthlist[isubset]                                    # monthlist
        datelist= datelist[isubset]                                       # datelist  

#       Generating return data 
        data = { 'field'     : fieldlist, \
                 'longitude' : lons, \
                 'latitude'  : lats, \
                 'nlon'      : nlon, \
                 'nlat'      : nlat, \
                 'nlev'      : 0, \
                 'units'     : units, \
                 'yearlist'  : yearlist, \
                 'monthlist' : monthlist, \
                 'datelist'  : datelist, \
                 'ntime'     : len(datelist)}
#       in case of 4d data
        if  ( ndim == 4 ) : 
            data.update({'nlev'      : nlev})

#       in case of 4d data (not 'phalf', not 'pfull')    
        if ( ndim == 4 and ( var != 'phalf' and var != 'pfull' ) ) :

#           pfull
            data.update({ \
#               'pfull'     : field_pfull[isubset,:,:,:], \ # isubset selection not anymore neededd
                'pfull'     : field_pfull[:,:,:,:], \
                'units_pfull' : units_pfull})

#           phalf            
            if ( clev in dimensions and phalforigin != '' ) : # not to be done if plev19
                data.update({ \
##                   'phalf'     : field_phalf[isubset,:,:,:], \ # isubset selection not anymore needed
                    'phalf'     : field_phalf[:,:,:,:], \
                    'units_phalf' : units_phalf})
#  
#        if ( var == 'o3' and model == 'OsloCTM3v1-2' ) :
#            print('+++ readallcmorizedfield +++')
#            print('field : ', data['field'][0,:,0,0])
#            print('phalf : ', data['phalf'][0,:,0,0])
#            quit()
 
    print('--- readallcmorizedfield ---')
# 
    return data    
