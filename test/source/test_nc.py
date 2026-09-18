from netCDF4 import Dataset
#
dir='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260105/individual/hist/1.9x2.5'
filename=dir+'/emissions_cmip7_noresm3_BC_N_anthroprofENEIND_vertical_1849-2025_1.9x2.5_CEDS-CMIP-2025-04-18_version20260105.nc'

dir='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260105/individual/hist/ne16pg3'
filename=dir+'/emissions_cmip7_noresm3_BC_N_anthroprofENEIND_vertical_1849-2025_ne16pg3_CEDS-CMIP-2025-04-18_version20260105.nc'

nc_fid = Dataset(filename, 'r')

# list of all variables in file
varkeylist = nc_fid.variables.keys()
print('varkeylist : ', varkeylist)

for varkey in varkeylist :
    varid = nc_fid.variables[varkey]
    
    dimnamelist = varid.dimensions
    dimsizelist = varid.shape

    print('dimensions : ', dimnamelist)
    print('shape      : ', dimsizelist)




#varitemlist = nc_fid.variables.items()
#print('varitemlist : ', varitemlist)


# dimensions in file
dimkeylist = nc_fid.dimensions.keys()
print('dimkeylist : ', dimkeylist)

for dimkey in dimkeylist :
    dimid = nc_fid.dimensions[dimkey]

    print('size : ', dimid.size)



nc_fid.close
