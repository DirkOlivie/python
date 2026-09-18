import analysetopography

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


# analysetopographyloop

figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
figlayoutlist=[figlayout0,figlayout1]

topodir='/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo'

# NE30PG3
# 1.1) ne30pg3 (given by Øyvind)
setopofile=topodir+'/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_greenlndantarcsgh30fac2.50_20250828.nc'
#setopofile=topodir+'/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_20240720.nc' # PHIS differs by 1.e-9 with the other file
fvtopofile=topodir+'/fv_0.9x1.25_nc3000_Nsw042_Nrs008_Co060_Fi001_ZR_sgh30_24km_GRNL_c170103.nc'
regridweightfile='/scratch/olivie/noresm-inputdata/cpl/gridmaps/ne30pg3/map_ne30pg3_TO_fv0.9x1.25_blin.240826.nc'  # bilinear
code='1x1_blin'
analysetopography.analysetopography(setopofile=setopofile, fvtopofile=fvtopofile, regridweightfile=regridweightfile, figlayoutlist=figlayoutlist, code=code)

# 1.2) ne30pg3 (given by Øyvind)
regridweightfile='/scratch/olivie/noresm-inputdata/cpl/gridmaps/ne30pg3/map_ne30pg3_TO_fv0.9x1.25_aave.240826.nc' # aave - first order conservative
code='1x1_aave'
analysetopography.analysetopography(setopofile=setopofile, fvtopofile=fvtopofile, regridweightfile=regridweightfile, figlayoutlist=figlayoutlist, code=code)


# NE16PG3
# 2) ne16pg3 
setopofile=topodir+'/se/ne16pg3_gmted2010_modis_bedmachine_nc3000_Laplace0200_20230202.nc'
fvtopofile=topodir+'/fv_1.9x2.5_nc3000_Nsw084_Nrs016_Co120_Fi001_ZR_061116.nc'
regridweightfile='/datalake/NS9560K/diagnostics/land_xesmf_diag_data/map_ne16pg3_to_1.9x2.5_nomask_scripgrids_c250425.nc'  # marit - first order conservative
code='2x2_aave'
analysetopography.analysetopography(setopofile=setopofile, fvtopofile=fvtopofile, regridweightfile=regridweightfile, figlayoutlist=figlayoutlist, code=code)
