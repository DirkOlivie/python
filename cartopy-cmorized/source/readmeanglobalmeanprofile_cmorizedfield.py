import numpy as np

import averagememberaverageperiodcmorizedfield

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import lon2lonbnds
import lat2latbnds
import xlon2ilon
import xlat2ilat

def readmeanglobalmeanprofile_cmorizedfield(expid, var, year0, year1, season, region=None, xlon=None, xlat=None, verticalaxis='pressure'):
#------------------------------------------
#
    '''
    REMARK
        1) reading
        2) geographical averaging

    MODIFICATIONS
        (2022-09-07) adding possibility for regional profiles
        (2024-03-10) adding possibility of in-situ profiles (SHADOZ) : weight field is now different from 0 only in one point
        (2024-04-29) replaced readsingleh0field by readsinglefield (to allow for reading of ozone_extclim from ozone forcing file)

    CALLS
        experimentdefinition
        readsinglefield
        areafraction
        lon2lonbnds
        lat2latbnds
        xlon2ilon
        xlat2ilat
        calculate3dpressure
        calcualte3dpressbnd
        calculate3dheight
        calculate3dheightbnd

    '''
#
    print('+++ readmeanglobalmeanprofilecmorizedfield +++')
#    print('region : ', region)
#    print('xlat : ', xlat)
#    print('xlon : ', xlon)
#    print('verticalaxis : ', verticalaxis)
#    quit()

#   experiment info

    D=averagememberaverageperiodcmorizedfield.averagememberaverageperiodcmorizedfield(expid=expid, var=var, year0=year0, year1=year1, season=season)

# obtain the dimensions : 
    nlev = D['nlev']
    nlat = D['nlat']
    nlon = D['nlon']
#
# weighting dependent on region

# 
    if ( region != None) : 
        if ( 'INSITU' in region ) :           # INSITULON-3.4LAT4.7
            print('IN SITU')
            line=region.split('INSITULON')[1] #          -3.4LAT4.7
            xlon=float(line.split('LAT')[0])  #          -3.4  
            xlat=float(line.split('LAT')[1])  #                 4.7

# region 
    if ( xlon == None and xlat == None ) : 
        w = areafraction.areafraction(latitude=D['latitude'],longitude=D['longitude'],outputtype='weight',region=region)
# weighting set to 1 in in-situ location
    else :
        lonbnds = lon2lonbnds.lon2lonbnds(longitude=D['longitude']) 
        latbnds = lat2latbnds.lat2latbnds(latitude=D['latitude'])
        
        ilon = xlon2ilon.xlon2ilon(lonbnds=lonbnds, xlon=xlon)
        ilat = xlat2ilat.xlat2ilat(latbnds=latbnds, xlat=xlat)

        print('nlon = ', nlon) 
        print('nlat = ', nlat)
        print('longitude = ', D['longitude'][0], D['longitude'][-1]) 
        print('latitude  = ', D['latitude'][0], D['latitude'][-1])
        print('xlon = ', xlon)
        print('xlat = ', xlat)
        print('ilon = ', ilon)
        print('ilat = ', ilat)
#        quit()

        w=np.zeros([nlat,nlon], dtype=float)
        w[ilat,ilon] = 1.                         # only p
  
# apply weighting to variable + do summation
    field  = D['field']
    for ilev in range (nlev) : 
        field[ilev,:,:] = field[ilev,:,:] * w[:,:] / w.sum() 
#
    valuelist=np.sum(field,axis=(1,2)) # over last two dimension = lat, lon

# obtain 3d height [m] / pressure [Pa]
    if ( verticalaxis == 'pressure' ) : 

        zfield=D['pfull']
#        zbndfield=D['phalf']

        zunits='Pa'

    elif ( verticalaxis == 'height' ) :

        Z=averagememberaverageperiodcmorizedfield.averagememberaverageperiodcmorizedfield(expid=expid, var='zg', year0=year0, year1=year1, season=season)
        zfield=Z['field']

        zunits='m'

#        print('zfield : ', zfield[:,0,0])
#        quit()


    else :
        print('readmeanglobalmeanprofile_cmorizedfield : no verticalaxis recognized : '+verticalaxis)
        quit()
#
# apply weighting to height + do summation
    for ilev in range(nlev) :
        zfield[ilev,:,:] = zfield[ilev,:,:] * w[:,:] / w.sum()

    zlist=np.sum(zfield,axis=(1,2)) # over last two dimension = lat, lon
#

# apply weighting to heightbnd + do summation
#    for ilev in range(nlev+1) :
#        zbndfield[ilev,:,:] = zbndfield[ilev,:,:] * w[:,:] / w.sum()
#
#    zbndlist=np.sum(zbndfield,axis=(1,2)) # over last two dimension = lat, lon
#
#    print('zlist : ', zlist)
#    print('zunits : ', zunits)
#    quit()

# structure
    data = { 'expid'     : expid, \
             'var'       : var, \
             'region'    : region, \
             'xlon'      : xlon, \
             'xlat'      : xlat, \
             'valuelist' : valuelist, \
             'units'     : D['units'], \
             'zlist'     : zlist, \
#             'zbndlist'  : zbndlist, \
             'zunits'    : zunits, \
             'verticalaxis' : verticalaxis, \
             'year0'        : year0, \
             'year1'        : year1, \
             'season'       : season}  
#
    print('--- readmeanglobalmeanprofilecmorizedfield ---')
#    
    return data

