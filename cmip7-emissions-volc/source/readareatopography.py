import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc



def readareatopography(grid, variable, filelocation):
#---------------------
    '''


    INPUT
        grid         : 
        variable     : 'topography' | 'area' 
        filelocation :

    RETURN
        orography [in units of m]        
        area      [in untis of m2]

    MODIFICATIONS
        (2025-10-18) Extension to irregular SE grids        
        (2026-01-16) adding argument : filelocation

    '''
#    
#    dir='/nird/datalake/NS2345K/olivie/emissions-auxiliary/inputdata/atm/cam/topo'
#    fncar_1x1 = dir+'/fv_0.9x1.25_nc3000_Nsw042_Nrs008_Co060_Fi001_ZR_sgh30_24km_GRNL_c170103.nc'
#    fncar_2x2 = dir+'/fv_1.9x2.5_nc3000_Nsw084_Nrs016_Co120_Fi001_ZR_061116.nc'
#    fncar_ne30pg3 = dir+'/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_20240720.nc' : contains area in radians^2 (however it says "m")
#    fncar_ne16pg3 = dir+'/se/ne16pg3_gmted2010_modis_bedmachine_nc3000_Laplace0200_20230202.nc'        : contains area in radians^2 (however it says "m") 
#
#    if   ( origin == '0.9x1.25' ) : filename = fncar_1x1
#    elif ( origin == '1.9x2.5'  ) : filename = fncar_2x2
#    elif ( origin == 'ne30pg3'  ) : filename = fncar_ne30pg3
#    elif ( origin == 'ne16pg3'  ) : filename = fncar_ne16pg3
#    else : 
#        print('Origin not recognized = ', origin)
#        quit() 
    filename=filelocation.topofile(grid=grid)
#
    g=9.81
    Rearth = 6370e+3
#
    if ( variable == 'topography' ) : data = 1. / g          * readnc.readnc('PHIS', filename)
    elif ( variable == 'area')      : data = Rearth * Rearth * readnc.readnc('area', filename) # conversion radians^2 -> m2
    else : 
        print('Origin not recognized = ', origin)
        quit()
#
    return data
