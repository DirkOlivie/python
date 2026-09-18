from netCDF4 import Dataset
import numpy as np

file='/nird/datalake/NS9560K/noresm3/input4mips/cmip7/DRES-CMIP-BB4CMIP7-2-0/BCpercentageAGRI_input4MIPs_emissions_CMIP_DRES-CMIP-BB4CMIP7-2-0_gn_175001-202312.nc'

itime0=0
itime1=359

nc_fid= Dataset(file, 'r')
tmppercentage=np.array(nc_fid.variables['BCpercentageAGRI'][itime0:itime1+1,:,:])    # data
nc_fid.close

print(np.mean(tmppercentage))
