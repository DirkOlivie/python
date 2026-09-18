import numpy as np

import intplev

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

#
def intpfieldirregular(infield, latin, latout, lonin, lonout, regridversion, irreggridversion, levinbd=None, levoutbd=None, extrapolate=None):
#---------------------
    '''
    REMARK 

    INPUT
        infield
        outfield
        latinbd   : the latitudinal boundaries
        latoutbd  
        loninbd   : the longitudinal boundaries
        lonoutbd
        levinbd     : NEEDED if 3-dim field
        levoutbd    : NEEDED if 3-dim field
        extrapolate

    CALLS
        readnc
        intplev

    '''
#
#   original field dimensions
    if ( infield.ndim == 3 ) : 
        ntime, nlat0, nlon0 = infield.shape
    elif ( infield.ndim == 4 ) :
        ntime, nlev0, nlat0, nlon0 = infield.shape
    else :
        print('+++ intpfieldirregular +++')
        print('No dimension of input field recognized (should be 3 or 4) : ', infield.ndim)
        quit()    
#
#   final field dimensions
    if ( len(latout) != len(lonout) ) :
        print('+++ intpfieldirregular +++')
        print('Sized of longitudes and latitudes differ : ', len(latout), len(lonout))
        quit()
    else :    
        ncol=len(latout)
#
#   find correct weight file
#   a) recognize inputgrid
    dlat=str(180./float(nlat0))
    dlon=str(360./float(nlon0))
#   
    if (latin[0] < 0. ) : 
        lat0='minus'+str(np.abs(latin[0]))
    else : 
        lat0='plus'+str(np.abs(latin[0]))                

#
    if (lonin[0] < 0. ) : 
        lon0='minus'+str(np.abs(lonin[0]))
    else : 
        lon0='plus'+str(np.abs(lonin[0]))
#
#   b) recgonize outputgrid
    if ( len(latout) == 13824 and len(lonout) == 13824 ) :
        gridout='ne16pg3'            
    elif ( len(latout) == 48600 and len(lonout) == 48600 ) :
        gridout='ne30pg3'            
    else :
        print('+++ intpfieldirregular +++')
        print('No output grid recognized : ', len(latout), len(lonout))
        quit()

    dir='/datalake/NS2345K/olivie/emissions-auxiliary/esmf/weights'
    if   ( gridout == 'ne16pg3' ) :
        weightfile=dir+'/WEIGHT_lat'+dlat+'xlon'+dlon+'_lon0'+lon0+'_lat0'+lat0+'_scrip_v20251011_TO_'+gridout+'_ESMFmesh_cdf5_'+irreggridversion+'_'+regridversion+'.nc'
    elif ( gridout == 'ne30pg3' ) :
#       weightfile=dir+'/WEIGHT_lat'+dlat+'xlon'+dlon+'_lon0'+lon0+'_lat0'+lat0+'_scrip_v20251011_TO_'+gridout+'_scrip_170611_VERSION20251018.nc'
        weightfile=dir+'/WEIGHT_lat'+dlat+'xlon'+dlon+'_lon0'+lon0+'_lat0'+lat0+'_scrip_v20251011_TO_'+gridout+'_ESMFmesh_cdf5_'+irreggridversion+'_'+regridversion+'.nc'
    else : 
        print('+++ intpfieldirregular +++')
        print('No output grid recognized : ', gridout)
        quit()
#
#   read weights from file : col/row/s have same dimensions
    col = readnc.readnc('col', weightfile) - 1 # should start at 0 !!
    row = readnc.readnc('row', weightfile) - 1 # should start at 0 !!
    S   = readnc.readnc('S'  , weightfile)

    print('+++ intpirregular +++')

    print('Min, max col : ' , np.min(col), np.max(col))
    print('Min, max row : ' , np.min(col), np.max(row))


#   2D case
    if ( infield.ndim == 3 ) :
#
#       horizontal interpolation
        outfield=np.zeros((ntime,ncol),dtype=float)

        for i in range(0,len(S)) :
            outfield[:,row[i]] = outfield[:,row[i]] + S[i] * infield[:, col[i] // nlon0,  col[i] % nlon0] 
    
#   3D case
    elif ( infield.ndim == 4 ) :  

#       final grid
        nlev1=len(levoutbd)-1

        ptlev, wtlev = intplev.intplev(levinbd=levinbd, levoutbd=levoutbd, extrapolate=extrapolate)
#
#       1) interpolation along vertical
        afield=np.zeros((ntime,nlev1,nlat0,nlon0),dtype=float)
        for ilev1 in range(0,nlev1) :
            nlev=ptlev[ilev1,0] # first value gives number of levels that contribute
            for ilev in range(1,nlev+1) :
                ilev0=ptlev[ilev1,ilev]
                wlev=wtlev[ilev1,ilev]
                afield[:,ilev1,:,:] = afield[:,ilev1,:,:] + infield[:,ilev0,:,:] * wlev
    
#       2) interpolation geographical
        outfield=np.zeros((ntime,nlev1,ncol),dtype=float)
        for i in range(0,len(S)) :
            outfield[:,:,row[i]] = outfield[:,:,row[i]] + S[i] * afield[:,:, col[i] // nlon0, col[i] % nlon0 ] # SHOULDN'T THIS BE "a" INSTEAD OF "infield"
#
    else :
        print('Combination of levinbd and levoutb not allowe : ')
        quit()

    print('--- intpirregular ---')

    return outfield
