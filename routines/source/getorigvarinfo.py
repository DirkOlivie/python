def getorigvarinfo(var) :
#--------------------------------
    '''
    INPUT
	    var 

    MODIFICATIONS
	(2025-05-18)    
        Extracted from netcdf_atmospher_exp_var and made into function

    '''
#   default variables
    varorig=None
    method=None
    varweight=None

#   some variables are derived
#   column burden 
    if (   var == 'ozone_columnburden' )      : varorig='ozone'   ; method='columnintegration'
    elif ( var == 'ozone_extclim_columnburden' ) : varorig='ozone_extclim'   ; method='columnintegration'
    elif ( var == 'CH4_columnburden' )        : varorig='CH4'     ; method='columnintegration'
    elif ( var == 'O3_columnburden' )         : varorig='O3'      ; method='columnintegration'
    elif ( var == 'OH_columnburden' )         : varorig='OH'      ; method='columnintegration'
    elif ( var == 'HO2_columnburden' )        : varorig='HO2'     ; method='columnintegration'
    elif ( var == 'N_AER_columnburden')       : varorig='N_AER'   ; method='columnintegration'
    elif ( var == 'LNO_PROD_columnburden')    : varorig='LNO_PROD'; method='columnintegration'
    elif ( var == 'mmr_SULFATE_columnburden') : varorig='mmr_SULFATE'; method='columnintegration'
    elif ( var == 'CLDLIQ_columnburden')      : varorig='CLDLIQ'  ; method='columnintegration'
    elif ( var == 'CLDICE_columnburden')      : varorig='CLDICE'  ; method='columnintegration'
    elif ( var == 'NUMLIQ_columnburden')      : varorig='NUMLIQ'  ; method='columnintegration'
    elif ( var == 'NUMICE_columnburden')      : varorig='NUMICE'  ; method='columnintegration'
    elif ( var == 'Q_columnburden')           : varorig='Q'       ; method='columnintegration'
#
    elif ( var == 'CCN1_columnburden')        : varorig='CCN1'  ; method='columnintegration'
    elif ( var == 'CCN2_columnburden')        : varorig='CCN2'  ; method='columnintegration'
    elif ( var == 'CCN3_columnburden')        : varorig='CCN3'  ; method='columnintegration'
    elif ( var == 'CCN4_columnburden')        : varorig='CCN4'  ; method='columnintegration'
    elif ( var == 'CCN5_columnburden')        : varorig='CCN5'  ; method='columnintegration'
    elif ( var == 'CCN6_columnburden')        : varorig='CCN6'  ; method='columnintegration'
    elif ( var == 'CCN7_columnburden')        : varorig='CCN7'  ; method='columnintegration'
#
    elif ( var == 'SAD_SULFC_columnburden' )  : varorig='SAD_SULFC' ; method='columnintegration'
    elif ( var == 'SAD_AERO_columnburden' )   : varorig='SAD_AERO'  ; method='columnintegration'
    elif ( var == 'SAD_ICE_columnburden' )    : varorig='SAD_ICE'   ; method='columnintegration'
    elif ( var == 'SAD_LNAT_columnburden' )   : varorig='SAD_LNAT'  ; method='columnintegration'
    elif ( var == 'SAD_TROP_columnburden' )   : varorig='SAD_TROP'  ; method='columnintegration'
#
    elif ( var == 'NNAT_0_columnburden')      : varorig='NNAT_0'  ; method='columnintegration'
    elif ( var == 'NNAT_1_columnburden')      : varorig='NNAT_1'  ; method='columnintegration'
    elif ( var == 'NNAT_2_columnburden')      : varorig='NNAT_2'  ; method='columnintegration'
    elif ( var == 'NNAT_4_columnburden')      : varorig='NNAT_4'  ; method='columnintegration'
    elif ( var == 'NNAT_5_columnburden')      : varorig='NNAT_5'  ; method='columnintegration'
    elif ( var == 'NNAT_6_columnburden')      : varorig='NNAT_6'  ; method='columnintegration'
    elif ( var == 'NNAT_7_columnburden')      : varorig='NNAT_7'  ; method='columnintegration'
    elif ( var == 'NNAT_8_columnburden')      : varorig='NNAT_8'  ; method='columnintegration'
    elif ( var == 'NNAT_9_columnburden')      : varorig='NNAT_9'  ; method='columnintegration'
    elif ( var == 'NNAT_10_columnburden')     : varorig='NNAT_10' ; method='columnintegration'
    elif ( var == 'NNAT_11_columnburden')     : varorig='NNAT_11' ; method='columnintegration'
    elif ( var == 'NNAT_12_columnburden')     : varorig='NNAT_12' ; method='columnintegration'
    elif ( var == 'NNAT_14_columnburden')     : varorig='NNAT_14' ; method='columnintegration'
#
    elif ( var == 'NCONC01_columnburden')     : varorig='NCONC01' ; method='columnintegration'
    elif ( var == 'NCONC02_columnburden')     : varorig='NCONC02' ; method='columnintegration'
    elif ( var == 'NCONC03_columnburden')     : varorig='NCONC03' ; method='columnintegration'
    elif ( var == 'NCONC04_columnburden')     : varorig='NCONC04' ; method='columnintegration'
    elif ( var == 'NCONC05_columnburden')     : varorig='NCONC05' ; method='columnintegration'
    elif ( var == 'NCONC06_columnburden')     : varorig='NCONC06' ; method='columnintegration'
    elif ( var == 'NCONC07_columnburden')     : varorig='NCONC07' ; method='columnintegration'
    elif ( var == 'NCONC08_columnburden')     : varorig='NCONC08' ; method='columnintegration'
    elif ( var == 'NCONC09_columnburden')     : varorig='NCONC09' ; method='columnintegration'
    elif ( var == 'NCONC10_columnburden')     : varorig='NCONC10' ; method='columnintegration'
    elif ( var == 'NCONC11_columnburden')     : varorig='NCONC11' ; method='columnintegration'
    elif ( var == 'NCONC12_columnburden')     : varorig='NCONC12' ; method='columnintegration'
    elif ( var == 'NCONC13_columnburden')     : varorig='NCONC13' ; method='columnintegration'
    elif ( var == 'NCONC14_columnburden')     : varorig='NCONC14' ; method='columnintegration'
#
    elif ( var == 'VCONC01_columnburden')     : varorig='VCONC01' ; method='columnintegration'
    elif ( var == 'VCONC02_columnburden')     : varorig='VCONC02' ; method='columnintegration'
    elif ( var == 'VCONC03_columnburden')     : varorig='VCONC03' ; method='columnintegration'
    elif ( var == 'VCONC04_columnburden')     : varorig='VCONC04' ; method='columnintegration'
    elif ( var == 'VCONC05_columnburden')     : varorig='VCONC05' ; method='columnintegration'
    elif ( var == 'VCONC06_columnburden')     : varorig='VCONC06' ; method='columnintegration'
    elif ( var == 'VCONC07_columnburden')     : varorig='VCONC07' ; method='columnintegration'
    elif ( var == 'VCONC08_columnburden')     : varorig='VCONC08' ; method='columnintegration'
    elif ( var == 'VCONC09_columnburden')     : varorig='VCONC09' ; method='columnintegration'
    elif ( var == 'VCONC10_columnburden')     : varorig='VCONC10' ; method='columnintegration'
    elif ( var == 'VCONC11_columnburden')     : varorig='VCONC11' ; method='columnintegration'
    elif ( var == 'VCONC12_columnburden')     : varorig='VCONC12' ; method='columnintegration'
    elif ( var == 'VCONC13_columnburden')     : varorig='VCONC13' ; method='columnintegration'
    elif ( var == 'VCONC14_columnburden')     : varorig='VCONC14' ; method='columnintegration'
#
    elif ( var == 'NMR01_NCONC01_weightedcolumnburden') : varorig='NMR01' ; varweight='NCONC01' ; method='weightedcolumnintegration'
    elif ( var == 'NMR05_NCONC05_weightedcolumnburden') : varorig='NMR05' ; varweight='NCONC05' ; method='weightedcolumnintegration'

    elif ( var == 'NMR01_VCONC01_weightedcolumnburden') : varorig='NMR01' ; varweight='VCONC01' ; method='weightedcolumnintegration'
    elif ( var == 'NMR05_VCONC05_weightedcolumnburden') : varorig='NMR05' ; varweight='VCONC05' ; method='weightedcolumnintegration'

#   (extinction) -> (AOD)
    elif ( var == 'BETOTVIS_columnburden')    : varorig='BETOTVIS' ; method='columnintegration' #    [1/km]   -> integrated should give AOD
    elif ( var == 'BVISVOLC_columnburden')    : varorig='BVISVOLC' ; method='columnintegration' #    [1/km]
    elif ( var == 'EC550AER_columnburden')    : varorig='EC550AER' ; method='columnintegration' #    [m-1]   -> integrated should give AOD
    elif ( var == 'EC550BC_columnburden')     : varorig='EC550BC'  ; method='columnintegration' #     [m-1]
    elif ( var == 'EC550DU_columnburden')     : varorig='EC550DU'  ; method='columnintegration' #     [m-1]
    elif ( var == 'EC550POM_columnburden')    : varorig='EC550POM' ; method='columnintegration' #   [m-1]
    elif ( var == 'EC550SO4_columnburden')    : varorig='EC550SO4' ; method='columnintegration' #    [m-1]
    elif ( var == 'EC550SS_columnburden')     : varorig='EC550SS'  ; method='columnintegration' #     [m-1]
    elif ( var == 'ECDRY440_columnburden')    : varorig='ECDRY440' ; method='columnintegration' #    [m-1]
    elif ( var == 'ECDRY870_columnburden')    : varorig='ECDRY870' ; method='columnintegration' #   [m-1]
    elif ( var == 'ECDRYAER_columnburden')    : varorig='ECDRYAER' ; method='columnintegration' #    [m-1]   -> to be compared with
    elif ( var == 'ECDRYLT1_columnburden')    : varorig='ECDRYLT1' ; method='columnintegration' #    [m-1]
    elif ( var == 'EXTVIS_columnburden')      : varorig='EXTVIS'   ; method='columnintegration' #      [1/km]
#
#   reaction production rates [VSLS]
    elif ( var == 'r_jchbr3_columnburden')    : varorig='r_jchbr3'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_CHBR3_OH_columnburden')  : varorig='r_CHBR3_OH' ; method='columnintegration' # [molecules/cm3/s]
    elif ( var == 'r_DMS_OHa_columnburden')   : varorig='r_DMS_OHa'  ; method='columnintegration' # [molecules/cm3/s]
    elif ( var == 'r_DMS_OH_columnburden')    : varorig='r_DMS_OH'   ; method='columnintegration' # [molecules/cm3/s]
    elif ( var == 'r_DMS_NO3_columnburden')   : varorig='r_DMS_NO3'  ; method='columnintegration' # [molecules/cm3/s]
#
#   reaction production rates [CH4]
    elif ( var == 'r_jch4_a_columnburden')    : varorig='r_jch4_a'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_jch4_b_columnburden')    : varorig='r_jch4_b'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_CH4_OH_columnburden')    : varorig='r_CH4_OH'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_CL_CH4_columnburden')    : varorig='r_CL_CH4'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_F_CH4_columnburden')     : varorig='r_F_CH4'    ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4a_columnburden')  : varorig='r_O1D_CH4a' ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4b_columnburden')  : varorig='r_O1D_CH4b' ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4c_columnburden')  : varorig='r_O1D_CH4c' ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'CH4_CHMP_columnburden')    : varorig='CH4_CHMP'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'CH4_CHML_columnburden')    : varorig='CH4_CHML'   ; method='columnintegration'  # [molecules/cm3/s]
#
    elif ( var == 'r_jch4_a_columnburden_belowtropopause')    : varorig='r_jch4_a'   ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_jch4_b_columnburden_belowtropopause')    : varorig='r_jch4_b'   ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_CH4_OH_columnburden_belowtropopause')    : varorig='r_CH4_OH'   ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_CL_CH4_columnburden_belowtropopause')    : varorig='r_CL_CH4'   ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_F_CH4_columnburden_belowtropopause')     : varorig='r_F_CH4'    ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4a_columnburden_belowtropopause')  : varorig='r_O1D_CH4a' ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4b_columnburden_belowtropopause')  : varorig='r_O1D_CH4b' ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4c_columnburden_belowtropopause')  : varorig='r_O1D_CH4c' ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'CH4_CHMP_columnburden_belowtropopause')    : varorig='CH4_CHMP'   ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
    elif ( var == 'CH4_CHML_columnburden_belowtropopause')    : varorig='CH4_CHML'   ; method='columnintegration_belowtropopause'  # [molecules/cm3/s]
#
    elif ( var == 'r_jch4_a_columnburden_abovetropopause')    : varorig='r_jch4_a'   ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_jch4_b_columnburden_abovetropopause')    : varorig='r_jch4_b'   ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_CH4_OH_columnburden_abovetropopause')    : varorig='r_CH4_OH'   ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_CL_CH4_columnburden_abovetropopause')    : varorig='r_CL_CH4'   ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_F_CH4_columnburden_abovetropopause')     : varorig='r_F_CH4'    ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4a_columnburden_abovetropopause')  : varorig='r_O1D_CH4a' ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4b_columnburden_abovetropopause')  : varorig='r_O1D_CH4b' ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'r_O1D_CH4c_columnburden_abovetropopause')  : varorig='r_O1D_CH4c' ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'CH4_CHMP_columnburden_abovetropopause')    : varorig='CH4_CHMP'   ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
    elif ( var == 'CH4_CHML_columnburden_abovetropopause')    : varorig='CH4_CHML'   ; method='columnintegration_abovetropopause'  # [molecules/cm3/s]
#
#   CH2O (formaldehyde)
    elif ( var == 'CH2O_CHMP_columnburden')    : varorig='CH2O_CHMP'   ; method='columnintegration'  # [molecules/cm3/s]
    elif ( var == 'CH2O_CHML_columnburden')    : varorig='CH2O_CHML'   ; method='columnintegration'  # [molecules/cm3/s]

#   mam4
    elif ( var == 'sum_BC_columnburden')    : varorig='sum_BC'   ; method='columnintegration' 
    elif ( var == 'sum_DST_columnburden')   : varorig='sum_DST'   ; method='columnintegration' 
    elif ( var == 'sum_OM_columnburden')    : varorig='sum_OM'   ; method='columnintegration'
    elif ( var == 'sum_SO4_columnburden')   : varorig='sum_SO4'   ; method='columnintegration'
    elif ( var == 'sum_SOA_columnburden')   : varorig='sum_SOA'   ; method='columnintegration'
    elif ( var == 'sum_SS_columnburden')    : varorig='sum_SS'   ; method='columnintegration'
#
    elif ( var == 'bc_a1_columnburden')    : varorig='bc_a1'   ; method='columnintegration'
    elif ( var == 'bc_a4_columnburden')    : varorig='bc_a4'   ; method='columnintegration'
    elif ( var == 'pom_a1_columnburden')    : varorig='pom_a1'   ; method='columnintegration'
    elif ( var == 'pom_a4_columnburden')    : varorig='pom_a4'   ; method='columnintegration'
    elif ( var == 'so4_a1_columnburden')    : varorig='so4_a1'   ; method='columnintegration'
    elif ( var == 'so4_a2_columnburden')    : varorig='so4_a2'   ; method='columnintegration'
    elif ( var == 'so4_a3_columnburden')    : varorig='so4_a3'   ; method='columnintegration'
    elif ( var == 'dst_a1_columnburden')    : varorig='dst_a1'   ; method='columnintegration'
    elif ( var == 'dst_a2_columnburden')    : varorig='dst_a2'   ; method='columnintegration'
    elif ( var == 'dst_a3_columnburden')    : varorig='dst_a3'   ; method='columnintegration'
    elif ( var == 'ncl_a1_columnburden')    : varorig='ncl_a1'   ; method='columnintegration'
    elif ( var == 'ncl_a2_columnburden')    : varorig='ncl_a2'   ; method='columnintegration'
    elif ( var == 'ncl_a3_columnburden')    : varorig='ncl_a3'   ; method='columnintegration'
    elif ( var == 'soa_a1_columnburden')    : varorig='soa_a1'   ; method='columnintegration'
    elif ( var == 'soa_a2_columnburden')    : varorig='soa_a2'   ; method='columnintegration'
#
#   interactive CO2 cycle
    elif ( var == 'CO2_columnburden'     ) : varorig = 'CO2'     ; method='columnintegration'    
    elif ( var == 'CO2_FFF_columnburden' ) : varorig = 'CO2_FFF' ; method='columnintegration'    
    elif ( var == 'CO2_LND_columnburden' ) : varorig = 'CO2_LND' ; method='columnintegration'    
    elif ( var == 'CO2_OCN_columnburden' ) : varorig = 'CO2_OCN' ; method='columnintegration'    
#
    elif ( var == 'CO2_columnburden_dry'     ) : varorig = 'CO2'     ; method='columnintegration_dry'    
    elif ( var == 'CO2_FFF_columnburden_dry' ) : varorig = 'CO2_FFF' ; method='columnintegration_dry'    
    elif ( var == 'CO2_LND_columnburden_dry' ) : varorig = 'CO2_LND' ; method='columnintegration_dry'    
    elif ( var == 'CO2_OCN_columnburden_dry' ) : varorig = 'CO2_OCN' ; method='columnintegration_dry'    
#
#   column burden above 100 hpa
    elif ( var == 'mmr_SULFATE_columnburden_above100hPa' )    : varorig='mmr_SULFATE'   ; method='columnintegration_above100hPa'
#
#   column integration in troposphere/stratosphere
    elif ( var == 'O3_columnburden_belowtropopause' ) : varorig='O3' ; method='columnintegration_belowtropopause'  # tropospheric column
    elif ( var == 'O3_columnburden_abovetropopause' ) : varorig='O3' ; method='columnintegration_abovetropopause'  # stratospheric column
    elif ( var == 'ozone_columnburden_belowtropopause' ) : varorig='ozone' ; method='columnintegration_belowtropopause'  # tropospheric column
    elif ( var == 'ozone_columnburden_abovetropopause' ) : varorig='ozone' ; method='columnintegration_abovetropopause'  # stratospheric column
#   
#   surface layer oxidants
    elif ( var == 'NO3_bef_surfacelayer' )    : varorig='NO3_bef' ; method='surfaceextraction' 
    elif ( var == 'NO3_aft_surfacelayer' )    : varorig='NO3_aft' ; method='surfaceextraction' 
    elif ( var == 'NO3_surfacelayer' )        : varorig='NO3'     ; method='surfaceextraction' 
    elif ( var == 'OH_bef_surfacelayer' )     : varorig='OH_bef'  ; method='surfaceextraction' 
    elif ( var == 'OH_aft_surfacelayer' )     : varorig='OH_aft'  ; method='surfaceextraction' 
    elif ( var == 'OH_surfacelayer' )         : varorig='OH'      ; method='surfaceextraction' 
    elif ( var == 'HO2_surfacelayer' )        : varorig='HO2'     ; method='surfaceextraction' 
    elif ( var == 'O3_surfacelayer' )         : varorig='O3'      ; method='surfaceextraction'
#   surface layer ozone
    elif ( var == 'ozone_surfacelayer' )      : varorig='ozone'   ; method='surfaceextraction'
#   surface layer GHGs
    elif ( var == 'CO2_surfacelayer' )        : varorig='CO2'     ; method='surfaceextraction' 
    elif ( var == 'CH4_surfacelayer' )        : varorig='CH4'     ; method='surfaceextraction' 
    elif ( var == 'N2O_surfacelayer' )        : varorig='N2O'     ; method='surfaceextraction' 
    elif ( var == 'CFC11_surfacelayer' )      : varorig='CFC11'   ; method='surfaceextraction' 
    elif ( var == 'CFC12_surfacelayer' )      : varorig='CFC12'   ; method='surfaceextraction' 
#
    elif ( var == 'DMS_surfacelayer' )        : varorig='DMS'     ; method='surfaceextraction' 
    elif ( var == 'SO2_surfacelayer' )        : varorig='SO2'     ; method='surfaceextraction' 
    elif ( var == 'CHBR3_surfacelayer' )      : varorig='CHBR3'   ; method='surfaceextraction' 
#
# CMORIZED
#   surface field
    elif ( var == 'ch4_surfacelayer'       )  : varorig='ch4'        ; method='surfaceextraction'
    elif ( var == 'h2_surfacelayer'        )  : varorig='h2'         ; method='surfaceextraction'
    elif ( var == 'o3_surfacelayer'        )  : varorig='o3'         ; method='surfaceextraction'
    elif ( var == 'co_surfacelayer'        )  : varorig='co'         ; method='surfaceextraction'
    elif ( var == 'oh_surfacelayer'        )  : varorig='oh'         ; method='surfaceextraction'

#   column bruden using no field
    elif ( var == 'emilnox_columnburden'   )  : varorig='emilnox'    ; method='columnintegration' 

#   column burden using pressure field
    elif ( var == 'ch4_columnburden'       )  : varorig='ch4'        ; method='columnintegration'
    elif ( var == 'co_columnburden'        )  : varorig='co'         ; method='columnintegration'
    elif ( var == 'oh_columnburden'        )  : varorig='oh'         ; method='columnintegration'
    elif ( var == 'o3_columnburden'        )  : varorig='o3'         ; method='columnintegration'
#
    elif ( var == 'ch4lossoh_columnburden' )  : varorig='ch4lossoh'  ; method='columnintegration'
    elif ( var == 'ch4losscl_columnburden' )  : varorig='ch4losscl'  ; method='columnintegration'
    elif ( var == 'ch4losso1d_columnburden' ) : varorig='ch4losso1d' ; method='columnintegration'
    elif ( var == 'lossch4_columnburden' )    : varorig='lossch4'    ; method='columnintegration'
#
    elif ( var == 'lossco_columnburden' )     : varorig='lossco'     ; method='columnintegration'
#
    elif ( var == 'ch4lossoh_columnburden_abovetropopause'  ) : varorig='ch4lossoh'  ; method='columnintegration_abovetropopause'
    elif ( var == 'ch4losscl_columnburden_abovetropopause'  ) : varorig='ch4losscl'  ; method='columnintegration_abovetropopause'
    elif ( var == 'ch4losso1d_columnburden_abovetropopause' ) : varorig='ch4losso1d' ; method='columnintegration_abovetropopause'
#
    elif ( var == 'ch4lossoh_columnburden_belowtropopause' )  : varorig='ch4lossoh' ; method='columnintegration_belowtropopause'
    elif ( var == 'lossch4_columnburden_belowtropopause' )    : varorig='lossch4'   ; method='columnintegration_belowtropopause'

#   column burden using airmass field
    elif ( var == 'ch4_columnburdenfromairmass'       )  : varorig='ch4'       ; method='columnintegrationfromairmass'
    elif ( var == 'o3_columnburdenfromairmass'       )  : varorig='o3'       ; method='columnintegrationfromairmass'

#   column burden using volume field
    elif ( var == 'lossch4_columnburdenfromvolume' )    : varorig='lossch4'    ; method='columnintegrationfromvolume'    
#
    elif ( '_layer' in var) : 
        line    = var.split('_layer')    # O3_layer06
        ilayer  = int(line[1])            # will give layer number
        varorig = line[0]               # original variable name
        method  = 'layerextraction'        # method
#        
    else                                      : varorig=var     ; method=''


#   structure
    data={ 'varorig'   : varorig, \
           'varweight' : varweight, \
           'method'    : method}
           
#   return
    return  data
