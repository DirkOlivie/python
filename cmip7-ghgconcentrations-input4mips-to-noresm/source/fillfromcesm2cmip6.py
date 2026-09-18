import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc
import getstandardunits


def fillfromcesm2cmip6(D, species):
#---------------------------
    '''
    INPUT
        D : structure which containin co2 
        species : 'ocs'
    
    RETURN
        D (modified)    

    CALLS
        daysince

    '''
#  
    print('+++ fillfromcesm2cmip6 +++')
#
#   final datastructure
    datelist = D['timelist']
    latitude = D['latitude']
    nlat     = D['nlat']
    ntime    = D['ntime']
#
#   cesm2cmip6 file
    filename='/datalake/NS2345K/olivie/ghgconcentrations-auxiliary/inputdata/atm/waccm/lb/LBC_17500116-20150116_CMIP6_0p5degLat_c180905.nc'

#   species
    if ( species == 'ocs' ) : finalspecies='OCS_LBC'
    else : 
        print('+++ fillfromcesm2cmip6 +++')
        print('Species not recognized : ', species)
        quit()

    datelist_cesm  = readnc.readnc('date', filename)
    valuelist_cesm = readnc.readnc(finalspecies, filename)
    latitude_cesm  = readnc.readnc('lat', filename)    

    units_cesm = getstandardunits.getstandardunits(readattributenc.readattributenc(finalspecies, filename, 'units'))    

    ntime_cesm = len(valuelist_cesm)
    nlat_cesm = len(latitude_cesm)

#   weighting original latitudes
    weight=np.zeros(nlat_cesm, dtype=float)
    for ilat in range(0,nlat_cesm) :
        weight[ilat] = np.cos(np.pi/180.*latitude_cesm[ilat])

#
    for itime in range(0,ntime) :
 #      before Jan 2015
        if ( datelist[itime] <= datelist_cesm[-1] ) :
           
            isubset = ( datelist[itime] == datelist_cesm )

            if ( sum(isubset) != 1) :
                print('+++ fillfromcesm2cmip6 +++')
                print('Number of elements in isubset : ', len(isubset))
                quit()
 
            D['valuelist'][itime,:] = np.sum(np.squeeze(valuelist_cesm[isubset,:])*weight)/np.sum(weight)
#       after Jan 2015
        else :

            D['valuelist'][itime,:] = np.sum(np.squeeze(valuelist_cesm[-1     ,:])*weight)/np.sum(weight) # in principle no squueze needed
#
    D['units'] = units_cesm
#
    return D
