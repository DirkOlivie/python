def getozonecliminfo (expid) :
#-------------------
    '''
    AIM
        give information on which ozone climatology had been used for specific experiment

    MODIFICATIONS
        (2024-04-26) creation

    '''
    dir='/scratch/olivie/noresm-inputdata/atm/cam/ozone_strataero'

#   toar experiments
    if   ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01' )     : filename=dir+'/O3.NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01.average.0021-0040.nc' ; method='cyclical' ; cycleyear=2015
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01' )     : filename=dir+'/O3.NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01.average.0021-0040.nc' ; method='cyclical' ; cycleyear=2015
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01' ) : filename=dir+'/O3.NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01.average.0021-0040.nc' ; method='cyclical' ; cycleyear=2015

    info={'filename'  : filename, \
          'method'    : method, \
          'cycleyear' : cycleyear}

    return info
