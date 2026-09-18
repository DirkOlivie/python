import netCDF4 as nc

import creategrid

def createscripfile(grid, version):
#------------------
    '''
    REAMRK on NetCDF4 type
    https://unidata.github.io/netcdf4-python/

    Specifier   Datatype 	            Old typecodes
    'f4' 	    32-bit floating point 	'f'
    'f8' 	    64-bit floating point 	'd'
    'i4' 	    32-bit signed integer 	'i' 'l'
    'i2' 	    16-bit signed integer 	'h' 's'
    'i8' 	    64-bit signed integer 	
    'i1' 	    8-bit signed integer 	'b' 'B'
    'u1' 	    8-bit unsigned integer 	
    'u2' 	    16-bit unsigned integer 	
    'u4' 	    32-bit unsigned integer 	
    'u8' 	    64-bit unsigned integer 	
    'S1' 	    single-character string 'c'

    CALLED BY
        loopcreategrid

    CALLS
        creategrid

    MODIFICATIONS
        (2026-01-07) : s_grid_area : 'i2' -> 'f8' (was 0 in output files)

    '''
    
#   test
    D=creategrid.creategrid(grid=grid)

#   create new file
    fn='/scratch/olivie/code/python/cmip7-esmf/data/output/'+grid+'_scrip_'+version+'.nc'
    ds = nc.Dataset(fn, 'w', format='NETCDF3_CLASSIC')

#   dimensions
    grid_size    = ds.createDimension('grid_size',    D['nsize'])
    grid_corners = ds.createDimension('grid_corners', D['ncorners'])     # 4
    grid_rank    = ds.createDimension('grid_rank',    D['nrank'])        # e.g., 144, 96
#
#   variables
    s_grid_center_lat = ds.createVariable('grid_center_lat','f8',('grid_size',))
    s_grid_center_lon = ds.createVariable('grid_center_lon','f8',('grid_size',))
    s_grid_corner_lat = ds.createVariable('grid_corner_lat','f8',('grid_size', 'grid_corners',))
    s_grid_corner_lon = ds.createVariable('grid_corner_lon','f8',('grid_size', 'grid_corners',))
    s_grid_dims       = ds.createVariable('grid_dims'      ,'i2',('grid_rank',))
    s_grid_imask      = ds.createVariable('grid_imask'     ,'i2',('grid_size',))
    s_grid_area       = ds.createVariable('grid_area'      ,'f8',('grid_size',))
#
#   attributes
    s_grid_center_lat.units = "degrees"
    s_grid_center_lon.units = "degrees"
    s_grid_corner_lat.units = "degrees"
    s_grid_corner_lon.units = "degrees"
    s_grid_imask.units      = "unitless"
    s_grid_area.units       = "square radians"
#
#   global attributes
    ds.title = 'TEST'
    ds.creation_date = 'TEST'
    ds.history = 'TEST'
#
#   fill values
    s_grid_center_lat[:]   = D['grid_center_lat'][:]
    s_grid_center_lon[:]   = D['grid_center_lon'][:]
    s_grid_corner_lat[:,:] = D['grid_corner_lat'][:,:]
    s_grid_corner_lon[:,:] = D['grid_corner_lon'][:,:]
    s_grid_dims[:]         = D['grid_dims'][:]
    s_grid_imask[:]        = D['grid_imask'][:]
    s_grid_area[:]         = D['grid_area'][:]
#
#   close file
    ds.close()
