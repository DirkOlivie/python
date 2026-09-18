import checkdifftopography

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


topodir='/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo'

# NE30PG3
# ne30pg3 : two versions
file0=topodir+'/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_greenlndantarcsgh30fac2.50_20250828.nc'
file1=topodir+'/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_20240720.nc'
checkdifftopography.checkdifftopography(file0=file0, file1=file1)
