import numpy as np

import readobsmodelperiod


import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

def getseries(expid, refid, xdiff, region, var, year0, year1):
#------------
    '''
    INPUT
        expid
        refid
        xdiff  : abs | diffabs | rmse | correlation 
        region : global | LAND | SEA | 28S28N | NHSEA | SHSEA
        var    : od55aer | od550aer_unc | od550aer-coverage
        year0
        year1

    REMARK
       always take areafraction : crescendo.aerocom.aodmergedfmi
       because all fields are interpolated to that resolution (and mask) anyway

       var1 = !VALUES.F_NaN
       PRINT, var1.IsNaN( )

    CALLED BY
       analyseseries

    CALLS
       readobsmodelperiod
       areafraction

    MODIFIATIONS
       (2024-02-13) distinction between od550aer and toc for reading land-sea mask
    '''
#------------------------------------------------------------------------------------------------------
#
#   1. read 2d fields [also models on observation grid from FMI, 180x360]
#   read expid data
    E = readobsmodelperiod.readobsmodelperiod(expid=expid, var=var, year0=year0, year1=year1) # contains field and mask; if model, is already interpolated to observation grid
#   read refid data
    if ( xdiff == 'diffabs' \
      or xdiff == 'correlation' \
      or xdiff == 'rmse' ) :

        R = readobsmodelperiod.readobsmodelperiod(expid=refid, var=var, year0=year0, year1=year1) # contains field and mask 


    ntime=E['ntime']

    valuelist=np.zeros(ntime,dtype=float)
    masklist =np.zeros(ntime,dtype=float)

#   average - extract - land - ocean - ... 
    longitude=E['longitude']
    latitude=E['latitude']

#   2. obtain weight 
#  case var of
#    'od550aer' : fileorigin='crescendo.aerocom.aodmergedfmi'
#    'toc'      : fileorigin='crescendo.aerocom.toccopernicus'
#  endcase

    weight=areafraction.areafraction(latitude=latitude, longitude=longitude, outputtype='weight', region=region)
#
#   3. compare every single monght
    for itime in range(0,ntime) :

#   1. averaged value

#       normalized weights   
        w = weight * E['mask'][itime,:,:] # combine weight (~grid size, correct region) x weight (where data exists or not)
        w = w / np.sum(w)                 # renormalize the new weight

#       value of experiments     
        if ( xdiff == 'abs') : 
            teller=np.sum( E['field'][itime,:,:] * w )                                              # summed over all grid points with correct weight
            noemer=np.sum(                      w )

#       value of experiments minus references    
        elif ( xdiff == 'diffabs' ) : 
            teller=np.sum( ( E['field'][itime,:,:] - R['field'][itime,:,:] ) * w )
            noemer=np.sum(                                                     w )
               
#       rmse
        elif ( xdiff == 'rmse' ) :
            teller=np.sqrt( np.sum ( ( E['field'][itime,:,:] - R['field'][itime,:,:] )^2 * w ) )
            noemer=np.sqrt( np.sum (                                                       w ) )

#       correlation
        elif ( xdiff == 'correlation' ) :
            Ex = np.sum (   E['field'][itime,:,:]                                             * w )
            Ey = np.sum (                                      R['field'][itime,:,:]          * w )
            Exx= np.sum ( ( E['field'][itime,:,:] - Ex )^2                                    * w )
            Eyy= np.sum (                                    ( R['field'][itime,:,:] - Ey )^2 * w )
            Exy= np.sum ( ( E['field'][itime,:,:] - Ex )   * ( R['field'][itime,:,:] - Ey )   * w )

            teller= Exy
            noemer= sqrt( Exx * Eyy )

        if ( noemer != 0. ) :
            valuelist[itime] = teller / noemer
        else :
            valuelist[itime] = float('nan')

#   2. mask [will indicated % of area that actullay contributed : is less than 100% due to missing values in observations]

#    global total mask
        teller_mask = np.sum ( weight * E['mask'][itime,:,:] ) # all points that are in correct region AND where data is available        
        noemer_mask = np.sum ( weight                        ) # all points that are in correct region

        if ( noemer_mask != 0. ) :
            masklist[itime] = teller_mask / noemer_mask
        else : 
            masklist[itime] = 0.

        print, 'valuelist[itime] : ', valuelist[itime]
#
# return data
    data = { 'var'             : var, \
             'units'           : E['units'], \
             'region'          : region, \
             'valuelist'       : valuelist, \
             'masklist'        : masklist, \
             'yearlist'        : E['yearlist'], \
             'monthlist'       : E['monthlist'], \
             'timelist' : E['timelist'], \
             'ntime'           : ntime }
#
    return data
