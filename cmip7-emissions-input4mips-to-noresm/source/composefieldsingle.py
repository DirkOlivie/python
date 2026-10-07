import intpstandard
import intpaircraft
import intpvolcano
import intpvolcstratclim
import expandfield

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-input4mips/source')
import readfield

#
def composefieldsingle(activity, sector, species, dim, vertdist, year0, year1, longitude, latitude, resolution, altitude_int, scenario, i4mpdownload, filelocation):
#---------------------
    '''
    INPUT
        ...
        sector : should be one specific sector (cannot be 'ALL')


    MODIFICATION
	    (2021-05-14) extension of the molecular weights
        (2021-05-15) extension to 'bbsurf'
	    (2021-09-02) added 'anthrosurfgas'
        (2025-10-18) removed 

    REMARK

     INPUT
	    activity :
        sector   :
	    species  : original species name (as used in input4MIPs
	    dim      :
        vertdist : 
        year0    :
        year1    :
        longitude  :
        latitude   :
        resolution :
        altitude_int
        scenario
        i4mpdownload :
        filelocation

    CALLED BY
	    composefield
 
    CALLS
	    readfield
    	intpstandard
	    intpaircraft
	    intpvolcano
        intpvolcstratclim
	    expandfield
    '''
#---------------------
#   0. ALL not allowed as sector
    if ( sector == 'ALL' ) :
        print('+++ composefieldsingle +++')        
        print('Sector ALL not allowed : ', sector)
        quit()
    
#   1. read in the original field (except for volcanic)
    if ( activity != 'volc' \
     and activity != 'volcstratclim1850-2021' \
     and activity != 'volcstratclim1750-2023' ) :

#       subcategories       
        if   ( activity == 'anthrosurf'   ) : F=readfield.readfield(activity='anthro', sector=sector, species=species, year0=year0, year1=year1, scenario=scenario, i4mpdownload=i4mpdownload)
        elif ( activity == 'anthroprof'   ) : F=readfield.readfield(activity='anthro', sector=sector, species=species, year0=year0, year1=year1, scenario=scenario, i4mpdownload=i4mpdownload)
        elif ( activity == 'anthrosurfgas') : F=readfield.readfield(activity='anthro', sector=sector, species=species, year0=year0, year1=year1, scenario=scenario, i4mpdownload=i4mpdownload)
        elif ( activity == 'bbsurf'       ) : F=readfield.readfield(activity='bb'    , sector=sector, species=species, year0=year0, year1=year1, scenario=scenario, i4mpdownload=i4mpdownload)
#       standard categarories
        else                                : F=readfield.readfield(activity=activity, sector=sector, species=species, year0=year0, year1=year1, scenario=scenario, i4mpdownload=i4mpdownload) 

#   2. interpolate to the new grid
#   2-dim 
    if ( dim == '2-dim') :
#
        F=intpstandard.intpstandard(D=F, longitude=longitude, latitude=latitude, resolution=resolution, filelocation=filelocation) #, altitude_int=altitude_int) #???? altitude_int possibly not needed?
#
#   3-dim
    elif ( dim == '3-dim' ) :

        if (   activity == 'air'           ) : F = intpaircraft.intpaircraft(D=F,      longitude=longitude, latitude=latitude, resolution=resolution, levbnds=altitude_int, filelocation=filelocation)
        elif ( activity == 'volc'          ) : F = intpvolcano.intpvolcano(            longitude=longitude, latitude=latitude, resolution=resolution, levbnds=altitude_int, sector=sector, species=species, year0=year0, year1=year1,                            filelocation=filelocation)
        elif ( activity == 'volcstratclim1850-2021' \
            or activity == 'volcstratclim1750-2023' ) : 
                                               F = intpvolcstratclim.intpvolcstratclim(activity=activity, longitude=longitude, latitude=latitude, resolution=resolution, levbnds=altitude_int, sector=sector, species=species, year0=year0, year1=year1, i4mpdownload=i4mpdownload, filelocation=filelocation)
        elif ( vertdist == 'surface-to-profile' ) :
#           expand field : 2dim -> 3dim ; kg m-2 s-1 -> kg m-3 s-1
                                                    F = expandfield.expandfield( D=F, sector=sector, activity=activity)               
                                                    F = intpstandard.intpstandard(D=F, longitude=longitude, latitude=latitude, resolution=resolution, altitude_int=altitude_int, filelocation=filelocation) 
#
        elif ( vertdist == 'profile-to-profile' ) : F = intpstandard.intpstandard(D=F, longitude=longitude, latitude=latitude, resolution=resolution, altitude_int=altitude_int, filelocation=filelocation)
        else :
            print('No vertdist recognized : ', vertdist)
            quit()            
    
    else :
        print('No dim recognized : ', dim)
        quit()
#
    return F
