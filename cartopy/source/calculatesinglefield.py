import numpy as np
from netCDF4 import Dataset

import experimentdefinition
import readsingleh0field

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/aerotabread/source')
import readaerotable
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import goffgratch_svp_water

'''
REMARK

'''


def calculatesinglefield( expid, var, date):
########################    
    '''
    MODIFICATIONS
        (2022-07-05) : creation     
    '''
#
#  wavelength bands 
#       CAM5    bands           AeroTab bands
#       14      3.846 12.195    14
#       1       3.077 3.846     13
#       2       2.500 3.077     12
#       3       2.150 2.500     11
#       4       1.942 2.150     10
#       5       1.626 1.942     9
#       6       1.299 1.626     8
#       7       1.242 1.299     7
#       8       0.778 1.242     6
#       9       0.625 0.778     5
#       10      0.442 0.625     4
#       11      0.345 0.442     3
#       12      0.263 0.345     2
#       13      0.200 0.263     1
#
#
#  So for 0.442 0.625 wavelength-band : choose iband=3
#
#----------------------------------------------------------------
#
    print('+++ calculatesinglefield +++')
    print('date : '+date)
#
#
    Mh2o    = 18.01
    Mdryair = 28.97 

#   choose 0.442-0.625 wavelength band
    iband = 3

#   experiment info
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
#
    if   ( var == 'EXT_MODE01_AeroTab_NCONC_RELHUM' ) : mode='01' ; shortfilename='kcomp1.out' ; version='AeroTab_8jun17' ; dorelhum=1 ; dospehum=0
    elif ( var == 'EXT_MODE01_AeroTab_NCONC_SPEHUM' ) : mode='01' ; shortfilename='kcomp1.out' ; version='AeroTab_8jun17' ; dorelhum=0 ; dospehum=1
    elif ( var == 'EXT_MODE01_AeroTab_NCONC'        ) : mode='01' ; shortfilename='kcomp1.out' ; version='AeroTab_8jun17' ; dorelhum=0 ; dospehum=0
    elif ( var == 'EXT_MODE05_AeroTab_NCONC_RELHUM' ) : mode='05' ; shortfilename='kcomp5.out' ; version='AeroTab_8jun17' ; dorelhum=1 ; dospehum=0
    elif ( var == 'EXT_MODE05_AeroTab_NCONC_SPEHUM' ) : mode='05' ; shortfilename='kcomp5.out' ; version='AeroTab_8jun17' ; dorelhum=0 ; dospehum=1
    elif ( var == 'EXT_MODE05_AeroTab_NCONC' )        : mode='05' ; shortfilename='kcomp5.out' ; version='AeroTab_8jun17' ; dorelhum=0 ; dospehum=0
#
#   obtain number concentration : units = [#/m3] 
    nconc = readsingleh0field.readsingleh0field(expid=expid,var='NCONC'+mode,date=date)

#   dimensions
    nlev, nlat, nlon = nconc['field'].shape


#   obtain relative humidity [percent, and can be larger than 100%]
    if ( dorelhum == 1 ) :
        relhum = readsingleh0field.readsingleh0field(expid=expid,var='RELHUM',date=date)
#   obtain specific humidity, and convert to relative humidity         
    elif (dospehum == 1 ) : 
        q = readsingleh0field.readsingleh0field(expid=expid,var='Q',date=date) # specific humidity         
        t = readsingleh0field.readsingleh0field(expid=expid,var='T',date=date) # temperature

        qsat=np.zeros([nlev,nlat,nlon])
         
        epsilon=Mh2o / Mdryair

        for ilev in range(0,nlev) :
            for ilat in range(0,nlat) :
                for ilon in range(0,nlon) :
                    
                    psat = goffgratch_svp_water.goffgratch_svp_water(t=t['field'][ilev,ilat,ilon])    # saturation pressure
                    p    = t['hyam'][ilev] * t['p0'] + t['hybm'][ilev] * t['ps'][ilat,ilon]           # mid-level pressure
                    qsat[ilev,ilat,ilon] =  psat * epsilon / ( p - ( 1. - epsilon ) * psat )

        relhum=q                                                         # initialize the structure
        relhum['field'][:,:,:] = q['field'][:,:,:] / qsat[:,:,:] * 100. 
        relhum['units'] = '%'

#   obtain AeroTab table : units is [km-1] for concentration of 1 [1/cm3] (see heading inside AeroTab files)
    table = readaerotable.readaerotable(version=version, shortfilename=shortfilename)

    print(relhum['units'])
    print(nconc['units'])        
    print(table['units'])

    iposrelh = table['dimnamelist'].index('relh')    # which position is "relative humidity" 
    iposiband = table['dimnamelist'].index('iband')  # which position is "wavelength"

    nrelh= table['dimsizelist'][iposrelh]            # how many x-values for "relativel humidity" 
    xrelhlist = table['xvaluelist'][iposrelh,0:nrelh] # x-values for "relative humidity" : 0-1 [fraction]

    print(iposrelh)
    print(iposiband)

#
    ext=np.zeros([nlev,nlat,nlon])

    for ilev in range(0,nlev) :
        for ilat in range(0,nlat) : 
            for ilon in range(0,nlon) :


                if ( dorelhum == 1 or dospehum == 1 ) :  

#                   convert relative humidity : from 0-100 [%] to 0-1 [fraction]
                    xrelh=np.amin([99.5,relhum['field'][ilev,ilat,ilon]]) / 100.  # conversion 0-100 to 0-1, and limit maximum value to 0.995

#                   find index of relative humidity interval
                    irelhfound=-1
                    for irelh in range(0,nrelh-1) : 
                        if ( xrelhlist[irelh] <= xrelh and xrelh <= xrelhlist[irelh+1] ) : irelhfound=irelh

#                   lowerbound and upperbound of interval 
                    x0 = xrelhlist[irelhfound]
                    x1 = xrelhlist[irelhfound+1]

#                   find corresponding y-values                                        
                    if (table['ndim'] == 5 and iposrelh==1) : 
                        y0=table['bext'][iband,irelhfound  ,0,0,0]
                        y1=table['bext'][iband,irelhfound+1,0,0,0]
                    elif (table['ndim'] == 6 and iposrelh==1) : 
                        y0=table['bext'][iband,irelhfound  ,0,0,0,0]
                        y1=table['bext'][iband,irelhfound+1,0,0,0,0]
                    else : 
                        print('Not recognized ndim or iposrelh')                   
                        quit()                                               

#                   interpolation  
                    y = ( y0 * (x1 -xrelh ) + y1 * (xrelh - x0) ) / ( x1 - x0 )

                elif ( dorelhum == 0 and dospehum == 0 ) :

#                   find corresponding y-values                                        
                    if (table['ndim'] == 5 and iposrelh==1) :
                        y=table['bext'][iband,0,0,0,0]
                    elif (table['ndim'] == 6 and iposrelh==1) : 
                        y=table['bext'][iband,0,0,0,0,0]
                    else :
                        print('Not recognized ndim or iposrelh')
                        quit()

#               fill the array
                ext[ilev,ilat,ilon] = y * nconc['field'][ilev,ilat,ilon] * 1.e-6

#   units
    units='km-1'
#
#   create structure
    data = { 'field'     : ext, \
             'longitude' : nconc['longitude'], \
             'latitude'  : nconc['latitude'], \
             'nlon'      : nconc['nlon'], \
             'nlat'      : nconc['nlat'], \
             'units'     : units, \
             'p0'        : nconc['p0'], \
             'ps'        : nconc['ps'], \
             'hyai'      : nconc['hyai'], \
             'hybi'      : nconc['hybi'], \
             'hyam'      : nconc['hyam'], \
             'hybm'      : nconc['hybm'], \
             'units_ps'  : nconc['units_ps'], \
             'units_p0'  : nconc['units_p0'], \
             'nlev'      : nconc['nlev']}
#
    print('MIN - MAX')
    print(np.amin(ext))
    print(np.amax(ext))
    print('--- calculatesinglefield ---')
#
    return data
