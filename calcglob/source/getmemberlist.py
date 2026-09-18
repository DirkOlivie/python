def getmemberlist ( expid ) :
#----------------------------
    '''
    MODIFICATIONS
        (2024-11-25) creation    
        (2025-12-02) adding ZECMIP-IMPOSE simulations

    '''
#   CESM2 - TOARMIP
    if (   expid == 'CESM2_pdClim-control_r1r2i1p1f1_gn'               ) : memberlist = ['CESM2_pdClim-control_r1i1p1f1_gn','CESM2_pdClim-control_r2i1p1f1_gn']
    elif ( expid == 'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn'      ) : memberlist = ['CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn','CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn']
    elif ( expid == 'CESM2_pdClim-fixO3_r1r2i1p1f1_gn'                 ) : memberlist = ['CESM2_pdClim-fixO3_r1i1p1f1_gn','CESM2_pdClim-fixO3_r2i1p1f1_gn']
    elif ( expid == 'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn' ) : memberlist = ['CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn','CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn']
    elif ( expid == 'CESM2_pdClim-2050ssp370fODS-radO3_r1r2i1p1f1_gn'  ) : memberlist = ['CESM2_pdClim-2050ssp370fODS-radO3_r1i1p1f1_gn','CESM2_pdClim-2050ssp370fODS-radO3_r2i1p1f1_gn']
#
#   METHANE MIP
    elif ( expid == 'NHISTSSP245_tropstratchem_123456_f19_tn14_r2000_s01_20241118' ) : memberlist = ['NHISTSSP245_tropstratchem_01_f19_tn14_r2000_s01_20241118', \
                                                                                                     'NHISTSSP245_tropstratchem_02_f19_tn14_r2000_s01_20241118', \
                                                                                                     'NHISTSSP245_tropstratchem_03_f19_tn14_r2000_s01_20241118', \
                                                                                                     'NHISTSSP245_tropstratchem_04_f19_tn14_r2000_s01_20241118', \
                                                                                                     'NHISTSSP245_tropstratchem_05_f19_tn14_r2000_s01_20241118', \
                                                                                                     'NHISTSSP245_tropstratchem_06_f19_tn14_r2000_s01_20241118']
    elif ( expid == 'NSSP245TECH_tropstratchem_123456_f19_tn14_s01_20241118'       ) : memberlist = ['NSSP245TECH_tropstratchem_01_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245TECH_tropstratchem_02_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245TECH_tropstratchem_03_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245TECH_tropstratchem_04_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245TECH_tropstratchem_05_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245TECH_tropstratchem_06_f19_tn14_s01_20241118']
    elif ( expid == 'NSSP245AMBI_tropstratchem_123456_f19_tn14_s01_20241118'       ) : memberlist = ['NSSP245AMBI_tropstratchem_01_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245AMBI_tropstratchem_02_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245AMBI_tropstratchem_03_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245AMBI_tropstratchem_04_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245AMBI_tropstratchem_05_f19_tn14_s01_20241118', \
                                                                                                     'NSSP245AMBI_tropstratchem_06_f19_tn14_s01_20241118']
#
#   ZECMIP - IMPOSE
#   a) 2000 Tg[C] - 1850-2249
    elif ( expid == 'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316' ) : memberlist = ['N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
                                                                                     'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
                                                                                     'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224']
#   b) 1500 Tg[C] - 1850-2249
    elif ( expid == 'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316' ) : memberlist = ['N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
                                                                                     'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
                                                                                     'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224']
#   c) 2000-500 Tg[C] - 1950--2249
    elif ( expid == 'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316' ) : memberlist = ['N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316', \
                                                                                      'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224', \
                                                                                      'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224']    
#      2000-500 Tg[C] - 1850-2249
    elif ( expid == 'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316pre' ) : memberlist = ['N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316pre', \
                                                                                         'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224pre', \
                                                                                         'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224pre']    
#      2000-500 Tg[C] - 1850-2249 [only member 2 and 3]     
    elif ( expid == 'N1850frc2esm_IMPOSE_C1a_23_f19_tn14_20200316pre' ) : memberlist = ['N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224pre', \
                                                                                         'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224pre']    
#   NAVIGATE
#   30S-30N
#   a) 1850-1949
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721len100', \
                                                                                                            'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721', \
                                                                                                            'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721']
#    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721', \
#                                                                                                            'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721', \
#                                                                                                            'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721']
#   b) 1950-2249
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730', \
                                                                                                            'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730', \
                                                                                                            'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730']
#   c) 1850-2249 (combination)
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730pre', \
                                                                                                               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730pre', \
                                                                                                               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730pre']
#   15N-60N
#   a) 1850-1949
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01', \
                                                                                                                      'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02', \
                                                                                                                      'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03']
#   b) 1950-2249
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123a' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01a', \
                                                                                                                       'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02a', \
                                                                                                                       'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03a']
#   c) 1850-2249
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01apre', \
                                                                                                                          'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02apre', \
                                                                                                                          'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03apre']
#   60S-15S
#   a) 1850-1949 
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens123' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens01', \
                                                                                                                      'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02', \
                                                                                                                      'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens03'] 
#   b) 1950-2249 
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123a' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens01a', \
                                                                                                                       'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens02a', \
                                                                                                                       'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens03a'] 
#   c) 1850-2249 
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre' ) : memberlist = ['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens01apre', \
                                                                                                                          'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02apre', \
                                                                                                                          'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens03apre'] 
#
#   CMIP6 HISTORICAL 
#   2x2
    elif ( expid == 'NHIST_123_f19_tn14_20190625ext' ) : memberlist=['NHIST_f19_tn14_20190625ext', \
                                                                     'NHIST_02_f19_tn14_20190801ext', \
                                                                     'NHIST_03_f19_tn14_20190801ext']
#   1x1
    elif ( expid == 'NHISTfrc2_123_f09_tn14_20191001ext' ) : memberlist=['NHISTfrc2_f09_tn14_20191001ext', \
                                                                         'NHISTfrc2_02_f09_tn14_20200427ext', \
                                                                         'NHISTfrc2_03_f09_tn14_20200519ext']

    elif ( expid == 'NHISTfrc2_12_f09_tn14_20191001ext' ) : memberlist=['NHISTfrc2_f09_tn14_20191001ext', \
                                                                        'NHISTfrc2_02_f09_tn14_20200427ext']
#
#   CMIP6 SSP SCENARIOS
    elif ( expid == 'NSSP245frc2_123_f19_tn14_20191014' ) : memberlist= ['NSSP245frc2_f19_tn14_20191014', \
                                                                         'NSSP245frc2_02_f19_tn14_20191014', \
                                                                         'NSSP245frc2_03_f19_tn14_20191014']
    elif ( expid == 'NSSP370frc2_123_f19_tn14_20191014' ) : memberlist = ['NSSP370frc2_f19_tn14_20191014', \
                                                                          'NSSP370frc2_02_f19_tn14_20191118', \
                                                                          'NSSP370frc2_03_f19_tn14_20191118'] 
#
    else : memberlist = [expid]

    return memberlist

