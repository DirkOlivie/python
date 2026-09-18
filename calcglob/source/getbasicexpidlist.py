def getbasicexpidlist ( expid ) :
#---------------------
    '''
    MODIFICATIONS
        (2022-08-30) : creation

    '''    
# CMIP6 [1x1]
#   piControl
    if ( expid == 'N1850frc2_f09_tn14_20191001ext' ) : readexpidlist=['N1850frc2_f09_tn14_20191001', \
                                                                      'N1850frc2_f09_tn14_20191012', \
                                                                      'N1850frc2_f09_tn14_20191113'] # piControl [1200-1699]
    elif ( expid == 'N1850frc2_f09_tn14_20191001len165' ) : readexpidlist=['N1850frc2_f09_tn14_20191001',
                                                                           'N1850frc2_f09_tn14_20191012len65'] # piControl [1200-1364]
#   abrupt-4xCO2
    elif ( expid == 'NCO2x4frc2_f09_tn14_20191008ext' ) : readexpidlist=['NCO2x4frc2_f09_tn14_20191008', \
                                                                         'NCO2x4frc2_f09_tn14_20191028'] # abrupt-4xCO2
#   1pctCO2
    elif ( expid == 'N1PCTfrc2_f09_tn14_20191008ext' ) : readexpidlist=['N1PCTfrc2_f09_tn14_20191008', \
                                                                        'N1PCTfrc2_f09_tn14_20191028'] # 1pct-CO2
#   historical
    elif ( expid == 'NHISTfrc2_f09_tn14_20191001ext' ) : readexpidlist=['NHISTfrc2_f09_tn14_20191001', \
                                                                        'NHISTfrc2_f09_tn14_20191025']
    elif ( expid == 'NHISTfrc2_02_f09_tn14_20200427ext' ) : readexpidlist=['NHISTfrc2_02_f09_tn14_20200427', \
                                                                           'NHISTfrc2_02_f09_tn14_20200519']
    elif ( expid == 'NHISTfrc2_03_f09_tn14_20200519ext' ) : readexpidlist=['NHISTfrc2_03_f09_tn14_20200519', \
                                                                           'NHISTfrc2_03_f09_tn14_20200619']
#
# CMIP6 [2x2]
#   piControl
    elif ( expid == 'N1850_f19_tn14_20190621ext' ) : readexpidlist=['N1850_f19_tn14_20190621', \
                                                                    'N1850_f19_tn14_20190722', \
                                                                    'N1850_f19_tn14_20190802'] # piControl
#   abrupt-4xCO2
    elif ( expid == 'NCO2x4_f19_tn14_20190624ext' ) : readexpidlist=['NCO2x4_f19_tn14_20190624', \
                                                                     'NCO2x4_f19_tn14_20190705', \
                                                                     'NCO2x4_f19_tn14_20190724'] # abrupt-4xCO2
#   1pctCO2
    elif ( expid == 'N1PCT_f19_tn14_20190626ext') : readexpidlist=['N1PCT_f19_tn14_20190626', \
                                                                   'N1PCT_f19_tn14_20190712'] # 1pct-CO2
#   historical
    elif ( expid == 'NHIST_f19_tn14_20190625ext' )    : readexpidlist=['NHIST_f19_tn14_20190625'   ,'NHIST_f19_tn14_20190710']
    elif ( expid == 'NHIST_02_f19_tn14_20190801ext' ) : readexpidlist=['NHIST_02_f19_tn14_20190801','NHIST_02_f19_tn14_20190813']
    elif ( expid == 'NHIST_03_f19_tn14_20190801ext' ) : readexpidlist=['NHIST_03_f19_tn14_20190801','NHIST_03_f19_tn14_20190813']
#    damip - natonly
    elif ( expid == 'N1850natonly_f19_tn14_20190805ext' ) : readexpidlist=['N1850natonly_f19_tn14_20190805','N1850natonly_f19_tn14_20190815']
#    damip - aeroxidonly
    elif ( expid == 'N1850aeroxidonly_f19_tn14_20190805ext' ) : readexpidlist=['N1850aeroxidonly_f19_tn14_20190805','N1850aeroxidonly_f19_tn14_20190815']
#
# FULL CHEMISTRY
    elif ( expid == 'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02_from1860' ) : readexpidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02']
    elif ( expid == 'FCHIST_f19_mg17_20220111_test1_from1860' ) : readexpidlist=['FCHIST_f19_mg17_20220111_test1']
#
# IMBALANCE CICERO
    elif ( expid == 'NFHISTnorpddmsbc_01_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_01_f19_mg17_20230110','NFSSP245norpddmsbc_01_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_02_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_02_f19_mg17_20230110','NFSSP245norpddmsbc_02_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_03_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_03_f19_mg17_20230110','NFSSP245norpddmsbc_03_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_04_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_04_f19_mg17_20230110','NFSSP245norpddmsbc_04_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_05_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_05_f19_mg17_20230110','NFSSP245norpddmsbc_05_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_06_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_06_f19_mg17_20230110','NFSSP245norpddmsbc_06_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_aer2000_01_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_aer2000_01_f19_mg17_20230110','NFSSP245norpddmsbc_aer2000_01_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_aer2000_02_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_aer2000_02_f19_mg17_20230110','NFSSP245norpddmsbc_aer2000_02_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_aer2000_03_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_aer2000_03_f19_mg17_20230110','NFSSP245norpddmsbc_aer2000_03_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_aer2000_04_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_aer2000_04_f19_mg17_20230110','NFSSP245norpddmsbc_aer2000_04_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_aer2000_05_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_aer2000_05_f19_mg17_20230110','NFSSP245norpddmsbc_aer2000_05_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_aer2000_06_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_aer2000_06_f19_mg17_20230110','NFSSP245norpddmsbc_aer2000_06_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_anthro2000_01_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_anthro2000_01_f19_mg17_20230110','NFSSP245norpddmsbc_anthro2000_01_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_anthro2000_02_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_anthro2000_02_f19_mg17_20230110','NFSSP245norpddmsbc_anthro2000_02_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_anthro2000_03_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_anthro2000_03_f19_mg17_20230110','NFSSP245norpddmsbc_anthro2000_03_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_anthro2000_04_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_anthro2000_04_f19_mg17_20230110','NFSSP245norpddmsbc_anthro2000_04_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_anthro2000_05_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_anthro2000_05_f19_mg17_20230110','NFSSP245norpddmsbc_anthro2000_05_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_anthro2000_06_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_anthro2000_06_f19_mg17_20230110','NFSSP245norpddmsbc_anthro2000_06_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_all2000_01_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_all2000_01_f19_mg17_20230110','NFSSP245norpddmsbc_all2000_01_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_all2000_02_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_all2000_02_f19_mg17_20230110','NFSSP245norpddmsbc_all2000_02_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_all2000_03_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_all2000_03_f19_mg17_20230110','NFSSP245norpddmsbc_all2000_03_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_all2000_04_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_all2000_04_f19_mg17_20230110','NFSSP245norpddmsbc_all2000_04_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_all2000_05_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_all2000_05_f19_mg17_20230110','NFSSP245norpddmsbc_all2000_05_f19_mg17_20230110']
    elif ( expid == 'NFHISTnorpddmsbc_all2000_06_f19_mg17_20230110ext' ) : readexpidlist=['NFHISTnorpddmsbc_all2000_06_f19_mg17_20230110','NFSSP245norpddmsbc_all2000_06_f19_mg17_20230110']
#
# KEYCLIM - WP6
#   elif ( expid == 'histssp585' )           : readexpidlist=['NHISTfrc2_f09_tn14_20191001','NHISTfrc2_f09_tn14_20191025','NSSP585frc2_f09_tn14_20191105'] # reference
#   elif ( expid == 'histssp585' )           : readexpidlist=['NHISTfrc2_f09_tn14_20200718','NSSP585frc2_f09_tn14_20191105'] # reference
    elif ( expid == 'histssp585' )           : readexpidlist=['NHISTfrc2_f09_tn14_20200718','NSSP585frc2_f09_tn14_20200919'] # reference
    elif ( expid == 'histssp370-piAerOxid' ) : readexpidlist=['NHISTpiaeroxid_f09_tn14_keyClim20201217','NSSP370piaeroxid_f09_tn14_keyClim20210210']
    elif ( expid == 'histssp585-piAerOxid' ) : readexpidlist=['NHISTpiaeroxid_f09_tn14_keyClim20201217','NSSP585piaeroxid_f09_tn14_keyClim_20230705']
    elif ( expid == 'histssp585-eddy' )      : readexpidlist=['NHISTfrc2_historical_Eddy_KeyCLim','NHISTfrc2_histeddy2_KeyCLim','NSSP585frc2_Eddy_KeyCLIM']
    elif ( expid == 'histssp585-iceSheet3' ) : readexpidlist=['NHISTfrc2G_f09_tn14_gl4_SMB1_celo','NSSP585frc2G_f09_tn14_gl4_SMB1_celo']
    elif ( expid == 'histssp585-cloud2' )    : readexpidlist=['NHISTfrc2_f09_tn14_cloudxpice_220629','NSSP585frc2_f09_tn14_cloudxpice_220819']
    elif ( expid == 'histssp585-ozone' )     : readexpidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03','NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01']
    elif ( expid == 'histssp585-snow' )      : readexpidlist=['NHIST_hist_snow_KeyClim','NSSP585_snow_KeyClim']
#
# KEYCLIM - Bromo-08
    elif ( expid == 'NHISTfrc2_f19_tn14_bromo_08_r1850ext'   ) : readexpidlist=['NHISTfrc2_f19_tn14_bromo_08_r1850','NHISTfrc2_f19_tn14_bromo_08_r1870','NHISTfrc2_f19_tn14_bromo_08_r1990']
    elif ( expid == 'NSSP585frc2_f19_tn14_bromo_08_r2015ext' ) : readexpidlist=['NSSP585frc2_f19_tn14_bromo_08_r2015','NSSP585frc2_f19_tn14_bromo_08_r2080']
#
# CAMS-VSLS - Michael Gauss
    elif ( expid == 'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03' ) : readexpidlist=['NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim03','NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03']
#
# METHANE-MIP
    elif ( expid == 'NHISTSSP245_tropstratchem_01_f19_tn14_r2000_s01_20241118' ) : readexpidlist=['NHIST_tropstratchem_01_f19_tn14_r2000_s01_20241118','NSSP245_tropstratchem_01_f19_tn14_s01_20241118']
    elif ( expid == 'NHISTSSP245_tropstratchem_02_f19_tn14_r2000_s01_20241118' ) : readexpidlist=['NHIST_tropstratchem_02_f19_tn14_r2000_s01_20241118','NSSP245_tropstratchem_02_f19_tn14_s01_20241118']
    elif ( expid == 'NHISTSSP245_tropstratchem_03_f19_tn14_r2000_s01_20241118' ) : readexpidlist=['NHIST_tropstratchem_03_f19_tn14_r2000_s01_20241118','NSSP245_tropstratchem_03_f19_tn14_s01_20241118']
    elif ( expid == 'NHISTSSP245_tropstratchem_04_f19_tn14_r2000_s01_20241118' ) : readexpidlist=['NHIST_tropstratchem_04_f19_tn14_r2000_s01_20241118','NSSP245_tropstratchem_04_f19_tn14_s01_20241118']
    elif ( expid == 'NHISTSSP245_tropstratchem_05_f19_tn14_r2000_s01_20241118' ) : readexpidlist=['NHIST_tropstratchem_05_f19_tn14_r2000_s01_20241118','NSSP245_tropstratchem_05_f19_tn14_s01_20241118']
    elif ( expid == 'NHISTSSP245_tropstratchem_06_f19_tn14_r2000_s01_20241118' ) : readexpidlist=['NHIST_tropstratchem_06_f19_tn14_r2000_s01_20241118','NSSP245_tropstratchem_06_f19_tn14_s01_20241118']
#    
# HYWAY 
    elif ( expid == 'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521' ) : readexpidlist=['NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521','NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_20250521']
    elif ( expid == 'NFHISTSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521' ) : readexpidlist=['NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521','NFSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_20250521']
#
# IMPOSE - JÖRG
    elif ( expid =='N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316pre' )      : readexpidlist=['N1850frc2esm_ZECMIP_B3_f19_tn14_20200316'   ,'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316'     ]
    elif ( expid =='N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224pre' ) : readexpidlist=['N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224','N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224']
    elif ( expid =='N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224pre' ) : readexpidlist=['N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224','N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224']
#
# NAVIGATE
#   30S-30N (too weak forcing)
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250730pre'    ) : readexpidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250721','N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250730']

#   30S-30N
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730pre'    ) : readexpidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721'   ,'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730']
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730pre' ) : readexpidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721','N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730']
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730pre' ) : readexpidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721','N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730']
#   15N-60N
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01apre' ) : readexpidlist=[ 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01', 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01a']
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02apre' ) : readexpidlist=[ 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02', 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02a']
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03apre' ) : readexpidlist=[ 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03', 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03a']
#   60S-15S
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens01apre' ) : readexpidlist = [ 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens01','N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens01a']
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02apre' ) : readexpidlist = [ 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02','N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens02a']
    elif ( expid == 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens03apre' ) : readexpidlist = [ 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens03','N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens03a']
#
# SSP5-3.4 - JÖRG
    elif ( expid == 'NSSP534frc2esm_f19_tn14_20230106ext' ) : readexpidlist=['NSSP534frc2esm_f19_tn14_20230106','NSSP534frc2esmext_f19_tn14_20230510']

# NORESM3.0-beta01 piControl
    elif ( expid == 'n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708ext' ) : readexpidlist=['n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708','n1850.ne30_tn14.nor3_b01-cplhist-noLU.20250716','n1850.ne30_tn14.nor3_b01-noLU_yr101.20250729']
    elif ( expid == 'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext' ) : readexpidlist=['n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708','n1850.ne16pg3_tn14.nor3_b01-cplhist.20250716','n1850.ne16pg3_tn14.nor3_b01.20250731']
#
# NORESM3.0-beta03 piControl
    elif ( expid == 'n1850.ne16_tn14.nor3_b03-rc3.20250925ext' ) : readexpidlist=['n1850.ne16_tn14.nor3_b03-rc3.20250925','n1850.ne16_tn14.nor3_b03-rc3_yr0031.20250928']

# ELSE
    else : readexpidlist = [expid]

#   return    
    return readexpidlist
