import glueseries
import fillfromcesm2cmip6

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-ghgconcentrations-input4mips/source')
import constructseries
import constructseries_1850placeholder

#
def assembleseries(scenario, timeresolution, region, species, source, fixedvalue, i4mpdownload):
#------------------------
    '''
    MODIFICATION
	    (2019-11-14) : added possibility of using hist+scenario
	    (2020-07-01) : added possibility of covid scenarios
	    (2020-07-17) : modified version3.0 -> version4.0 for covid scenarios
	    (2020-07-20) : added hsit_ssp245_amap_CMIP6
	    (2023-07-27) : added hist_ssp245_forces_CLE
		               added hist_ssp245_forces_MFR
		               added hist_ssp245_forces_LOW	
        (2026-10-18) : added possibility for 'CMIP-abrupt0p5xco2' and 'CMIP-abrupt2xco2'

    INPUT
	    scenario
	    timeresolution : 'monthly' | 'annual'
	    region
	    species
	    i4mpdownload

    REMARK 
	    This function calls itself for period covering historical plus scenarion

    CALLED BY
	    composeries

    CALLS
        constructseries_1850placeholder
	    assembleseries CALLS ITSELF !!
        glueseries
	    constructseries
	    constructforcesseries
	    constructcovidseries
	    biascorrectseries
    '''
#--------------------------------------------------------------------------------------------
#
#   OPTION I : 1pctCO2 or abrupt4xco2
    if ( scenario == 'CMIP-1pctco2' \
      or scenario == 'CMIP-abrupt4xco2' \
      or scenario == 'CMIP-abrupt2xco2' \
      or scenario == 'CMIP-abrupt0p5xco2' ) :

        S = constructseries_1850placeholder.constructseries_1850placeholder(scenario=scenario, timeresolution=timeresolution, region=region, species=species,i4mpdownload=i4mpdownload)

#   OPTION II : splitting historical+scenario
    elif ( scenario == 'hist_ScenarioMIP_UoM-AIM-ssp370-1-2-1' ) : 
        line = scenario.split('_')
        print('Scenario (before split) : ', scenario)
        print('Scenario 1 : ', line[0])
        print('Scenario 2 : ', line[1])
#
        S0=assembleseries.assembleseries(scenario=line[0], timeresolution=timeresolution, region=region, species=species, source=source, fixedvalue=fixedvalue, i4mpdownload=i4mpdownload) # history part
        S1=assembleseries.assembleseries(scenario=line[1], timeresolution=timeresolution, region=region, species=species, source=source, fixedvalue=fixedvalue, i4mpdownload=i4mpdownload) # scenario part
#
        S = glueseries.glueseries(S0=S0, S1=S1)
#
#   OPTION III : use co2 for non-existing input4MIPs data : H2, CH2BR2 (fixed)
    elif ( source == 'fixedvalue' ) :

        S = assembleseries(scenario=scenario, timeresolution=timeresolution, region=region, species='co2', source='standard', fixedvalue=None, i4mpdownload=i4mpdownload) # read co2
        S['valuelist'][:,:] = fixedvalue                                                                                                                                  # impose values   
        S['units'] = 'mol mol-1'                                                                                                                                          # impose units

#   OPTION IV : use co2 for non-existing input4MIPs data : OCS (cesm2cmip6)
    elif ( source == 'cesm2-cmip6' ) :

        S = assembleseries(scenario=scenario, timeresolution=timeresolution, region=region, species='co2', source='standard', fixedvalue=None, i4mpdownload=i4mpdownload) # read co2       
        S = fillfromcesm2cmip6.fillfromcesm2cmip6(D=S, species=species)                                                                                                   # impose values 

#   OPTION V : treat single period (historical or scenario)
    elif ( source == 'standard' ) :
#
        print('scenario = ', scenario)
        print('species = ', species)

        S = constructseries.constructseries(scenario=scenario, timeresolution=timeresolution, region=region, species=species,i4mpdownload=i4mpdownload)
#
#   OPTION VI 
    else :
        print('+++ assembleseries +++')
        print('No choice recognized ...')
        quit()

    return S
