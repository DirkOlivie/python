def getorigfilename(species, resolution): 
#--------------------
    '''



    '''
#   directory
    if   ( resolution == '0.9x1.25' ) : dir='/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015'
    elif ( resolution == '1.9x2.5'  ) : dir='/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/CMIP6_emissions_1750_2015_2deg'
    else :
        print('+++ getorigfilename +++')
        print('No resolution recognized : ', resolution)
        quit()
#
#   filename
    if ( species == 'E90' ) : filename=dir+'/emissions_E90global_surface_1750-2100_0.9x1.25_c20170322.nc'
    else                    : filename=dir+'/emissions-cmip6_'+species+'_other_surface_1750-2015_'+resolution+'_c20170322.nc'
#
    return filename
