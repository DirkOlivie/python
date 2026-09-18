import copy

import getfullsectorlist
import getspeciesinfo
import composefieldsingle


def composefield(activity, sector, species, dim, vertdist, longitude, latitude, resolution, altitude_int, year0, year1, scenario, i4mpdownload, filelocation) :
#----------------------
    '''
    INPUT
        sector : can be 'ALL' but can also be an individual sector name


    MODIFICATION
	    (2021-05-19)
		1). change in significatio of species
			before : species = original species name CMIP6 data (low level)
			now    : species = final species name in NorESM2 emission files (high level)
		2). the weighting (e.g., 0.9 for BC_N, 0.1 for BC_AX) is moved from buildemission.pro to composefield.pro (done via getspeciesinfo)
		3). species can have contribution from several species (e.g., BIGALK = butanes + pentanes + hexanes + esters + ethers)
			added call to getspeciesinfo
			addes summing over all contributions	
		4). moved unitconversion (kg/m2/s -> molecules/cm2/s) from composefieldsingle to composefield

    CALLED BY
	    buildemission
 
    CALLS
	    getfullsectorlist
        getspeciesinfo
        composefieldsingle
    '''
#------------------------------------------------------------
#
#   find all contributing sectors in case of 'ALL'
    if ( sector == 'ALL' ) : complist = getfullsectorlist.getfullsectorlist(activity=activity, scenario=scenario, i4mpdownload=i4mpdownload)
    else                   : complist = [sector] 

    ncomp=len(complist)

#   find all contributing original species
    speciesinfo=getspeciesinfo.getspeciesinfo(species=species, activity=activity)

    norig=len(speciesinfo['origspecieslist'])

#   loop over all contributing sectors ("comp" plays the role of sector
    for icomp in range(0,ncomp) :

#       loop over all contributing species      
        for iorig in range(0,norig) :

#           
            Ftmp = composefieldsingle.composefieldsingle(activity=activity, sector=complist[icomp], species=speciesinfo['origspecieslist'][iorig], dim=dim, vertdist=vertdist, year0=year0, year1=year1, longitude=longitude, latitude=latitude, resolution=resolution, altitude_int=altitude_int, scenario=scenario, i4mpdownload=i4mpdownload, filelocation=filelocation)
#
#           weight the contribution	 
            Ftmp['field'] = Ftmp['field'] * speciesinfo['origweightlist'][iorig] # weight 

#           add the new contribution to existing contribution	
            if ( icomp == 0 and iorig == 0) :
                F = copy.deepcopy(Ftmp)
            else :
                F['field'] = F['field'] + Ftmp['field']
#
#   Modify the units
    Nav = 6.022e23

#   new units :
    if ( F['units'] == 'kg m-2 s-1' ) :

        # kg   m-2   s-1
        # g    m-2   s-1
        # mole m-2   s-1 
        # mole cm-2  s-1
        # molecules cm-2 s-1
        factor  = 1.                \
                * 1.e3              \
                / speciesinfo['Mw'] \
                * 1.e-4             \
                * Nav            
#
        newunits = 'molecules cm-2 s-1'
#
    elif ( F['units'] == 'kg m-3 s-1' ) :

        # kg m-3 s-1
        # g    m-3   s-1
        # mole m-3   s-1
        # mole cm-3  s-1
        # molecules cm-2 s-1
        factor  = 1.                \
                * 1.e3              \
                / speciesinfo['Mw'] \
                * 1.e-6             \
                * Nav           
#
        newunits = 'molecules cm-3 s-1'
#
    else :
        print('+++ composefield +++')
        print('No units recognized : ', F['units'])
        quit()
#
    F['field'] = F['field'] * factor
    F['units'] = newunits
#
#   update with extra information    
    F['sector' ] = sector
    F['species'] = species
#
    return F
