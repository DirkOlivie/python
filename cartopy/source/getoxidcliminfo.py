def getoxidcliminfo (expid) :
#------------------
    '''
    AIM
        give information on which oxidant climatology had been used for specific experiment

    '''
    dir='/scratch/olivie/noresm-inputdata/atm/cam/tracer_cnst'

#   cmip6 fsst
    if (   expid == 'NF1850norbc_f19_20191025' )      : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850
    elif ( expid == 'NF1850norbc_f19_20191025len30' ) : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850
    elif ( expid == 'NF1850frc2norbc_f09_20200108')   : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850
#   cmip6 cpl
    elif ( expid == 'N1850_f19_tn14_20190621')        : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850
    elif ( expid == 'N1850_f19_tn14_20190722')        : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850
    elif ( expid == 'N1850_f19_tn14_20190802')        : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850
#   bromoform
    elif ( expid == 'N1850frc2_f19_tn14_bromo_08')    : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850


#   betzy
    elif ( expid == 'NF1850norbc_f19_20201226')       : filename=dir+'/tracer_cnst_WACCM6_halons_3DmonthlyL70_1850climoCMIP6piControl001_y21-50avg_c180802.nc' ; method='cyclical' ; cycleyear=1850  
#
#   HISTORICAL 
    elif ( expid == 'NFHISTnorbc_f19_20191107')         : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
#   2x2
    elif ( expid == 'NHIST_f19_tn14_20190625')          : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHIST_f19_tn14_20190710')          : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHIST_02_f19_tn14_20190801')       : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHIST_02_f19_tn14_20190813')       : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHIST_03_f19_tn14_20190801')       : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHIST_03_f19_tn14_20190813')       : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
#   2x2 bromoform
    elif ( expid == 'NHISTfrc2_f19_tn14_bromo_08')     : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1

#   1x1
    elif ( expid == 'NHISTfrc2_f09_tn14_20191001')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHISTfrc2_f09_tn14_20191001')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1 
    elif ( expid == 'NHISTfrc2_f09_tn14_20191025')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHISTfrc2_02_f09_tn14_20200427')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1 
    elif ( expid == 'NHISTfrc2_02_f09_tn14_20200519')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1 
    elif ( expid == 'NHISTfrc2_03_f09_tn14_20200519')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1 
    elif ( expid == 'NHISTfrc2_03_f09_tn14_20200619')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1 
    elif ( expid == 'NHISTfrc2_f09_tn14_20200718')    : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1 
#   1x1 KeyCLIM WP6 HISTORICAL
    elif ( expid == 'NHISTpiaeroxid_f09_tn14_keyClim20201217' ) : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHISTfrc2_historical_Eddy_KeyCLim')        : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHISTfrc2_histeddy2_KeyCLim')              : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHISTfrc2G_f09_tn14_gl4_SMB1_celo')        : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHISTfrc2_f09_tn14_cloudxpice_220629')     : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NHIST_hist_snow_KeyClim')                  : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2015_CMIP6ensAvg_c180927.nc'; method='interp_missing_months' ; cycleyear=-1
#
#   SSP126
#   2x2 bromoform
    elif ( expid == 'NSSP126frc2_f19_tn14_bromo_08' ) : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP1-2.6_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
#
#   SSP370
#   1x1 KeyCLIM WP6 SSP370
    elif ( expid == 'NSSP370piaeroxid_f09_tn14_keyClim20210210' ) : filename=dir+'/tracer_cnst_halons_3D_L70_1849-2101_CMIP6ensAvg_SSP3-7.0_c190403.nc'; method='interp_missing_months' ; cycleyear=-1
#
#   SSP585
#   2x2
    elif ( expid == 'NSSP585frc2_f19_tn14_20191014' ) : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
#   2x2 bromoform
    elif ( expid == 'NSSP585frc2_f19_tn14_bromo_08' ) : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
#   1x1    
    elif ( expid == 'NSSP585frc2_f09_tn14_20191105' ) : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NSSP585frc2_f09_tn14_20200919' ) : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
#
#   1x1 KeyCLIM WP6 SSP585
    elif ( expid == 'NSSP585piaeroxid_f09_tn14_keyClim_20230705' ): filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NSSP585frc2_Eddy_KeyCLIM' )                  : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NSSP585frc2G_f09_tn14_gl4_SMB1_celo' )       : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NSSP585frc2_f09_tn14_cloudxpice_220819' )    : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1
    elif ( expid == 'NSSP585_snow_KeyClim' )                      : filename=dir+'/tracer_cnst_halons_3D_L70_2014-2101_CMIP6-SSP5-8.5_c190307.nc'; method='interp_missing_months' ; cycleyear=-1

    info={'filename'  : filename, \
          'method'    : method, \
          'cycleyear' : cycleyear}

    return info
