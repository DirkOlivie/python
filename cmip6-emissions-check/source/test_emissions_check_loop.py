import test_emissions_check

#
# AIM
#   calculating global means of emissions fikes    
#
# CESM emission files [1x1]
#
filelist=['/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015/emissions-cmip6_NH3_other_surface_1750-2015_0.9x1.25_c20170322.nc', \
          '/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015/emissions-cmip6_NH3_anthro_surface_1750-2015_0.9x1.25_c20170608.nc', \
          '/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015/emissions-cmip6_NH3_bb_surface_1750-2015_0.9x1.25_c20170322.nc']
code='cesm2_nh3'

test_emissions_check.test_emissions_check(filelist=filelist, sectorsum='individual', code=code)
#
# NorESM emission files [2x2]
filelist=['/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015_2deg/emissions-cmip6_NH3_other_surface_1750-2015_1.9x2.5_c20170322.nc', \
          '/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/cmip6_emissions_version20211124/emissions_cmip6_noresm2_NH3_anthrosurfgasALL_surface_1849-2015_1.9x2.5_version20211124.nc', \
          '/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/cmip6_emissions_version20211124/emissions_cmip6_noresm2_NH3_bbsurfALL_surface_1849-2015_1.9x2.5_version20211124.nc']
code='noresm2_nh3'

test_emissions_check.test_emissions_check(filelist=filelist, sectorsum='individual', code=code)
