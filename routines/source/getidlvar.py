def getidlvar (var) :
#--------------------    
#
# interactive emissions from land model
    if var=='emich4land' : idlvar='CH'+r'$_4$'+' (surface emissions)'
# radiation
    elif var=='FSDS'  : idlvar='All-sky downwelling solar flux (surface)'
    elif var=='FSDSC' : idlvar='Clearsky downwelling solar flux (surface)'
    elif var=='FSNTOAC' : idlvar='Clearsky net solar flux (TOA)'
# general  
    elif var=='TREFHT' : idlvar='Surface (2m) air temperature'
    elif var=='tempocn': idlvar='Ocean temperature (volume mean)'
    elif var=='tempocn_trend': idlvar='Ocean temperature trend (volume mean)'
    elif var=='tempgaocn_trend': idlvar='Ocean temperature trend (volume mean)'
    elif var=='salngaocn' : idlvar='Ocean salinitiy (volume mean)'
    elif var=='sstgaocn' : idlvar='Sea surface temperature'
    elif var=='sssgaocn' : idlvar='Sea surface salinity'
    elif var=='voltrocn' : idlvar='Volume transport'
    elif var=='PRECT'      : idlvar='Precipitation'
    elif var=='PRECCPRECL' : idlvar='Precipitation'
    elif var=='SWCF'   : idlvar='SW cloud forcing'
    elif var=='LWCF'   : idlvar='LW cloud forcing'
    elif var=='CDNUMC' : idlvar='Cloud droplet number (column burden)'
    elif var=='U10'    : idlvar='Surface wind (10m)'
    elif var=='ICEFRAC': idlvar='Sea ice'

# column burden
    elif var=='cb_O3'  : idlvar='Ozone (column burden)'
    elif var=='cb_CH4' : idlvar='CH'+r'$_4$'+' (column burden)'
    elif var=='cb_N2O' : idlvar='N'+r'$_2$'+'O column burden'
    elif var=='cb_N2OCHEM' : idlvar='N'+r'$_2$'+'O (column burden)'
    elif var=='cb_CO'  : idlvar='CO column burden'
    elif var=='cb_NO'  : idlvar='NO column burden'
    elif var=='cb_NO2' : idlvar='NO'+r'$_2$'+' column burden'
    elif var=='cb_NH3' : idlvar='NH'+r'$_3$'+' column burden'
    elif var=='cb_SO2' : idlvar='SO'+r'$_2$'+' column burden'
    elif var=='cb_CHBR3' : idlvar='CHBr'+r'$_3$'+' (column burden)'
    elif var=='cb_DMS' : idlvar='DMS (column burden)'
    elif var=='cb_isoprene' : idlvar='Isoprene (column burden)'
    elif var=='cb_monoterp' : idlvar='Monoterp (column burden)'
    elif var=='cb_SULFATE' : idlvar='SO'+r'$_4$'+' (column burden)'
    elif var=='cb_SALT' : idlvar='Sea-salt (column burden)'
    elif var=='cb_BC' : idlvar='BC (column burden)'
    elif var=='cb_BC_AC_OCW' : idlvar='BC(ac) in cloud droplets (column burden)'
    elif var=='cb_OM' : idlvar='OM (column burden)'
    elif var=='cb_DUST' : idlvar='Dust (column burden)'

    elif var=='cb_SOA_A1' : idlvar='SOA[a1] (column burden)'
    elif var=='cb_SOA_NA' : idlvar='SOA[na] (column burden)'
    elif var=='cb_SOA_A1NA' : idlvar='SOA[a1+na] (column burden)'
#
    elif var=='cb_BC_N' : idlvar='BC(n) (column burden)'
    elif var=='cb_BC_NI' : idlvar='BC(ni) (column burden)'
    elif var=='cb_BC_A' : idlvar='BC(a) (column burden)'
    elif var=='cb_BC_AI' : idlvar='BC(ai) (column burden)'
    elif var=='cb_BC_AX' : idlvar='BC(ax) (column burden)'
    elif var=='cb_BC_AC' : idlvar='BC(ac) (column burden)'
#
    elif var=='ozone_columnburden' : idlvar='Ozone (column burden)'
    elif var=='O3_columnburden'    : idlvar='Ozone (column burden)'
    elif var=='OH_columnburden'    : idlvar='OH (column burden)'
    elif var=='HO2_columnburden'   : idlvar='HO'+r'$_2$'+' (column burden)'
#
    elif var=='CO2_columnburden'        : idlvar='CO'+r'$_2$'+' (column burden)'
    elif var=='CO2_columnburden_as_vmr' : idlvar='CO'+r'$_2$'+' (mixing ratio)'
    elif var=='CO2_columnburden_as_RF'  : idlvar='CO'+r'$_2$'+' (radiative forcing)'
#
    elif var=='ch4_columnburden'        : idlvar='CH'+r'$_4$'+' (column burden)'

# dry deposition
    elif var=='DF_CH4' : idlvar='CH'+r'$_4$ (dry deposition)'    
    elif var=='drych4' : idlvar='CH'+r'$_4$ (dry deposition)'    
    elif var=='minusdrych4' : idlvar='CH'+r'$_4$ (dry deposition)'    
#
# reactions
    elif var=='r_jch4_ab_columnburden' : idlvar='CH'+r'$_4$ (photolysis)'
    elif var=='r_CH4_OH_columnburden' : idlvar='CH'+r'$_4$ (reaction with OH)'
    elif var=='r_CL_CH4_columnburden' : idlvar='CH'+r'$_4$ (reaction with Cl)'    
    elif var=='r_F_CH4_columnburden' : idlvar='CH'+r'$_4$ (reaction with F)'    
    elif var=='r_O1D_CH4abc_columnburden' : idlvar='CH'+r'$_4$ (reaction with O'+r'$^1$'+'(D))'    

    elif var=='ch4lossoh_columnburden' : idlvar='CH'+r'$_4$ (reaction with OH)'
    elif var=='ch4losso1d_columnburden' : idlvar='CH'+r'$_4$ (reaction with O'+r'$^1$'+'(D))'
    elif var=='ch4losscl_columnburden' : idlvar='CH'+r'$_4$ (reaction with Cl)'
#
# production/loss
    elif var=='CH4_CHMP_columnburden' : idlvar='CH'+r'$_4$ (production)'
    elif var=='CH4_CHML_columnburden' : idlvar='CH'+r'$_4$ (loss)'

# surface mixing ratio
    elif var=='O3_SRF' : idlvar='O'+r'$_3$'+' (surface)'    
    elif var=='CO_SRF' : idlvar='CO (surface)'
    elif var=='H2_SRF' : idlvar='H'+r'$_2$'+' (surface)'
    elif var=='NO2_SRF' : idlvar='NO'+r'$_2$'+' (surface)'
    elif var=='NH3_SRF' : idlvar='NH'+r'$_3$'+' (surface)'
    elif var=='SO2_SRF' : idlvar='SO'+r'$_2$'+' (surface)'
    elif var=='CH4_SRF' : idlvar='CH'+r'$_4$'+' (surface)'
    elif var=='N2O_SRF' : idlvar='N'+r'$_2$'+'O (surface)'
    elif var=='CHBR3_SRF' : idlvar='CHBr'+r'$_3$'+' (surface mixing ratio)'
    elif var=='OH_SRF' : idlvar='OH (surface)'
    elif var=='DMS_SRF' : idlvar='DMS (surface)'

    elif var=='o3_surfacelayer' : idlvar='O'+r'$_3$'+' (surface)'
    elif var=='ch4_surfacelayer' : idlvar='CH'+r'$_4$'+' (surface)'

# mass mixing ratio
    elif var=='mmr_BC' : idlvar='BC'
    elif var=='mmr_OM' : idlvar='OM'
    elif var=='mmr_SULFATE' : idlvar='SO'+r'$_4$'
    elif var=='mmr_DUST' : idlvar='Dust'
    elif var=='mmr_SALT' : idlvar='Sea-salt'
    elif var=='OM_NIAIAC' : idlvar='Primary OM'
    elif var=='SOA_NAA1'  : idlvar='Secondary OM'

# concentration
    elif var=='SO2_as_concentration' : idlvar='SO'+r'$_2$'
    elif var=='mmr_SULFATE_as_concentration' : idlvar='SO'+r'$_4$'

# lifetime
    elif var=='TAU_CHBR3'    : idlvar='CHBr'+r'$_3$'+' (lifetime)'
    elif var=='TAU2_CH4'     : idlvar='CH'+r'$_4$'+' (lifetime)'
    elif var=='TAU2_N2O'     : idlvar='N'+r'$_2$'+'O (lifetime)'
    elif var=='TAU_DMS'      : idlvar='DMS'+' (lifetime)'
    elif var=='TAU_isoprene' : idlvar='Isoprene'+' (lifetime)'
    elif var=='TAU_monoterp' : idlvar='Monoterpene'+' (lifetime)'
    elif var=='TAU_BC_noresm2' : idlvar='BC'+' (lifetime)'
    elif var=='TAU_OM_noresm2' : idlvar='OM'+' (lifetime)'
    elif var=='TAU_SULFATE_noresm2' : idlvar='SO'+r'$_4$'+' (lifetime)'
    elif var=='TAU_DUST_noresm2'    : idlvar='Dust'+' (lifetime)'
    elif var=='TAU_SALT_noresm2'    : idlvar='Sea-salt'+' (lifetime)'
    elif var=='TAU_CH4_OHTROP'    : idlvar='CH'+r'$_4$'+' (lifetime from reaction with trop. OH)'
    elif var=='tau_ch4_oh'    : idlvar='CH'+r'$_4$'+' (lifetime from reaction with OH)'
    elif var=='tau_ch4_ohtrop': idlvar='CH'+r'$_4$'+' (lifetime from reaction with trop. OH)'
#
# ilevel00 and ilevel06
    elif var=='O3_layer00' : idlvar='O'+r'$_3$'+' (3.6 hPa)'
    elif var=='O3_layer06' : idlvar='O'+r'$_3$'+' (51.7 hPa)'

    elif var=='BRY_layer00' : idlvar='Br'+r'$_y$'+' (3.6 hPa)'
    elif var=='BRY_layer06' : idlvar='Br'+r'$_y$'+' (51.7 hPa)'
    elif var=='CLY_layer00' : idlvar='Cl'+r'$_y$'+' (3.6 hPa)'
    elif var=='CLY_layer06' : idlvar='Cl'+r'$_y$'+' (51.7 hPa)'
    elif var=='BRY_SUM_layer00' : idlvar='Br'+r'$_y$'+' summed (3.6 hPa)'
    elif var=='BRY_SUM_layer06' : idlvar='Br'+r'$_y$'+' summed (51.7 hPa)'
    elif var=='CLY_SUM_layer00' : idlvar='Cl'+r'$_y$'+' summed (3.6 hPa)'
    elif var=='CLY_SUM_layer06' : idlvar='Cl'+r'$_y$'+' summed (51.7 hPa)'
    elif var=='BRY_SCALED_layer00' : idlvar='Br'+r'$_y$'+' scaled (3.6 hPa)'
    elif var=='BRY_SCALED_layer06' : idlvar='Br'+r'$_y$'+' scaled (51.7 hPa)'
    elif var=='CLY_SCALED_layer00' : idlvar='Cl'+r'$_y$'+' scaled (3.6 hPa)'
    elif var=='CLY_SCALED_layer06' : idlvar='Cl'+r'$_y$'+' scaled (51.7 hPa)'
#
# surface layer
    elif var=='ozone_surfacelayer' : idlvar='O'+r'$_3$'+' (surface)'
    elif var=='O3_surfacelayer' : idlvar='O'+r'$_3$'+' (surface)'
    elif var=='OH_surfacelayer' : idlvar='OH'+' (surface)'
    elif var=='NO3_surfacelayer' : idlvar='NO'+r'$_3$'+' (surface)'
    elif var=='HO2_surfacelayer' : idlvar='HO'+r'$_2$'+' (surface)'
    elif var=='ch4_surfacelayer' : idlvar='CH'+r'$_4$'+' (surface)'
    elif var=='o3_surfacelayer' : idlvar='O'+r'$_3$'+' (surface)'

# mixing ratio
    elif var=='O3'              : idlvar='O'+r'$_3$'
    elif var=='O3_as_partpress' : idlvar='O'+r'$_3$'
    elif var=='ozone'      : idlvar='O'+r'$_3$'
    elif var=='isoprene'   : idlvar='Isoprene'
    elif var=='monoterp'   : idlvar='Monoterpene'
    elif var=='NO2'        : idlvar='NO'+r'$_2$'
    elif var=='SO2'        : idlvar='SO'+r'$_2$'
    elif var=='H2'         : idlvar='H'+r'$_2$'
    elif var=='OH_aft'     : idlvar='OH'
    elif var=='HO2_aft'    : idlvar='HO'+r'$_2$'
    elif var=='NO3_aft'    : idlvar='NO'+r'$_3$'
    elif var=='H2O2'       : idlvar='H'+r'$_2$'+'O'+r'$_2$'
    elif var=='H2SO4'      : idlvar='H'+r'$_2$'+'SO'+r'$_4$'
    elif var=='BRY'        : idlvar='Br'+r'$_y$'
    elif var=='BRY_SUM'    : idlvar='Br'+r'$_y$'+' summed'
    elif var=='BRY_SCALED' : idlvar='Br'+r'$_y$'+' scaled'
    elif var=='CLY'        : idlvar='Cl'+r'$_y$'
    elif var=='CLY_SUM'    : idlvar='Cl'+r'$_y$'+' summed'
    elif var=='CLY_SCALED' : idlvar='Cl'+r'$_y$'+' scaled'
    elif var=='CH4'        : idlvar='CH'+r'$_4$'
    elif var=='N2OCHEM'    : idlvar='N'+r'$_2$'+'O (chem)'
    elif var=='SOA_SV'     : idlvar='SOAG(SV)'
    elif var=='SOA_LV'     : idlvar='SOAG(LV)'
#
    elif var=='m_CO2_c_as_vmr' : idlvar='CO'+r'$_2$' 
    elif var=='m_CH4_c_as_vmr' : idlvar='CH'+r'$_4$' 
    elif var=='m_N2O_c_as_vmr' : idlvar='N'+r'$_2$'+'O' 
    elif var=='m_CFC11_c_as_vmr' : idlvar='CFC-11' 
    elif var=='m_CFC12_c_as_vmr' : idlvar='CFC-12' 
    elif var=='m_O3_c_as_vmr'    : idlvar='O'+r'$_3$' 
    elif var=='m_ozone_c_as_vmr'   : idlvar='O'+r'$_3$' 

# surface emissions
    elif var=='SFBC_N'     : idlvar='BC(n) (surface emissions)'
    elif var=='SFBC_AX'    : idlvar='BC(ax) (surface emissions)'
    elif var=='SFBC_NI'    : idlvar='BC(ni) (surface emissions)'
    elif var=='SFOM_NI'    : idlvar='OM(ni) (surface emissions)'
    elif var=='SFSO2'      : idlvar='SO'+r'$_2$'+' (surface emissions)'
    elif var=='SFSO4_PR'   : idlvar='SO'+r'$_4$'+'(pr) (surface emissions)'
#
    elif var=='SFCO2_FFF'  : idlvar='CO'+r'$_2$'+' emissions'
    elif var=='SFCO2_FFF_cumulative'  : idlvar='Cumulative CO'+r'$_2$'+' emissions'
#
    elif var=='SFCH4'      : idlvar='CH'+r'$_4$'+' (surface emissions)'
    elif var=='SFCO'       : idlvar='CO (surface emissions)'
    elif var=='SFNO'       : idlvar='NO (surface emissions)'
    elif var=='SFNH3'      : idlvar='NH'+r'$_3$'+' (surface emissions) [CAM]'
    elif var=='SFCHBR3'    : idlvar='CHBr'+r'$_3$'+' (surface emissions)'
    elif var=='SFisoprene' : idlvar='Isoprene (surface emissions)'
    elif var=='SFmonoterp' : idlvar='Monoterpene (surface emissions)'
    elif var=='SFDMS'      : idlvar='DMS (surface emissions)'
    elif var=='minusGS_DMS': idlvar='DMS (surface emissions)'   # temporary replacement
    elif var=='minusGS_N2O': idlvar='N'+r'$_2$'+'O (net chemical loss)'
    elif var=='SFN2O'      : idlvar='N'+r'$_2$'+'O (surface emissions)'
    elif var=='SFN2O_as_N' : idlvar='N'+r'$_2$'+'O (surface emissions, as [N])'
    elif var=='emin2oland' : idlvar='N\(_2\)O (surface emissions, as [N])'

# 3D emissions (column integrated)
    elif var=='BC_N_CMXF'     : idlvar='BC(n) (3D emissions)'
    elif var=='BC_AX_CMXF'    : idlvar='BC(ax) (3D emissions)'
    elif var=='BC_NI_CMXF'    : idlvar='BC(ni) (3D emissions)'
    elif var=='OM_NI_CMXF'    : idlvar='OM(ni) (3D emissions)'
    elif var=='SO2_CMXF'      : idlvar='SO'+r'$_2$'+' (3D emissions)'
    elif var=='SO4_PR_CMXF'   : idlvar='SO'+r'$_4$'+'(pr) (3D emissions)'
    elif var=='H2O_CMXF'      : idlvar='H'+r'$_2$'+'O(pr) (3D emissions)'
# 3D emissions (profile)
    elif var=='H2O_XFRC'      : idlvar='H'+r'$_2$'+'O(pr) (3D emissions)'
#
# total emissions
    elif var=='EMI_SO2_TOT_noresm2'  : idlvar='SO'+r'$_2$'+' (emissions)'
    elif var=='EMI_SO2SO4_as_SO2_TOT_noresm2'  : idlvar='SO'+r'$_2$'+'+SO'+'$_4$'+' (as SO'+r'$_2$'+') (emissions)'
    elif var=='EMI_SO2SO4_as_S_TOT_noresm2'    : idlvar='SO'+r'$_2$'+'+SO'+'$_4$'+' (as S) (emissions)'
    elif var=='EMI_SO2SO4_as_S_TOT_noresm2_offsetlast30yr'    : idlvar='SO'+r'$_2$'+'+SO'+'$_4$'+' (as S) (emissions)'
    elif var=='EMI_BC_TOT_noresm2'   : idlvar='BC (emissions)'
    elif var=='EMI_BC_TOT_noresm3'   : idlvar='BC (emissions)'
    elif var=='EMI_OM_TOT_noresm2'   : idlvar='OM (emissions)'
    elif var=='EMI_SALT_TOT_noresm2' : idlvar='Sea-salt (emissions)'
    elif var=='EMI_DUST_TOT_noresm2' : idlvar='Dust (emissions)'
    elif var=='WETDRY_SALT_TOT_noresm2' : idlvar='Sea-salt (dry+wet deposition)'
    elif var=='WETDRY_DUST_TOT_noresm2' : idlvar='Dust (dry+wet deposition)'
#
# lightning emissions
    elif var=='LNO_COL_PROD'          : idlvar='Lightning NO'+r'$_x$'+' (emissions, as [N])'
    elif var=='LNO_PROD_columnburden' : idlvar='Lightning NO'+r'$_x$'+' (emissions, as [N])'
    elif var=='emilnox_columnburden'  : idlvar='Lightning NO'+r'$_x$'+' (emissions, as [N])'
#
# emissions from CLM
#   CH4
    elif var=='FCH4xLANDFRAC'         : idlvar='CH'+r'$_4$'+' (surface emissions)'
#   FIRE C
    elif var=='COL_FIRE_CLOSSxLANDFRAC' : idlvar='Non-peat fire C (emissions)'
    elif var=='PFT_FIRE_CLOSSxLANDFRAC' : idlvar='Non-peat fire C (emissions)'
    elif var=='SOMC_FIRExLANDFRAC'      : idlvar='Peat fire C (emissions)'
#   N2O
    elif var=='F_N2O_DENIT_NITxLANDFRAC'        : idlvar='N'+r'$_2$'+'O (surface emissions, as [N])' # (land surface emissions, as [N])
    elif var=='F_N2O_DENIT_NITxLANDFRAC_as_N2O' : idlvar='N'+r'$_2$'+'O (land surface emissions)'
#
# deposition from CLM
    elif var=='NDEP_TO_SMINNxLANDFRAC'  : idlvar='N (land deposition) [CLM]'
    elif var=='NFERTILIZATIONxLANDFRAC' : idlvar='N (land fertilizer) [CLM]'
#
# emissions from BLOM
#   N2O
    elif var=='n2ofluxocn'        : idlvar='N'+r'$_2$'+'O (ocean emissions) [BLOM]'
#   NH3
    elif var=='nh3fluxocn'        : idlvar='NH'+r'$_3$'+' (ocean emissions) [BLOM]'
#   ndepnoyocn
    elif var=='ndepnoyocn'        : idlvar='NOy (ocean deposition) [BLOM]'
#   ndepnhxocn
    elif var=='ndepnhxocn'        : idlvar='NHx (ocean deposition) [BLOM]'

# emissions from CAM
#   N2O
    elif var=='emin2oocean'        : idlvar='N'+r'$_2$'+'O (ocean emissions) [CAM]'    
    elif var=='emin2oland_as_N2O'  : idlvar='N'+r'$_2$'+'O (land emissions) [CAM]'    
#   NH3
    elif var=='eminh3ocean'        : idlvar='NH'+r'$_3$'+' (ocean emissions) [CAM]'    
#
# depositions from CAM
    elif var=='wet_deposition_NHx_as_N'    :  idlvar='NHx (wet deposition) [CAM]'
    elif var=='dry_deposition_NHx_as_N'    :  idlvar='NHx (dry deposition) [CAM]'
    elif var=='wetdry_deposition_NHx_as_N' :  idlvar='NHx (wet+dry deposition) [CAM]'
    elif var=='wet_deposition_NOy_as_N'    :  idlvar='NOy (wet deposition) [CAM]'
    elif var=='dry_deposition_NOy_as_N'    :  idlvar='NOy (dry deposition) [CAM]'
    elif var=='wetdry_deposition_NOy_as_N' :  idlvar='NOy (wet+dry deposition) [CAM]'
    elif var=='wetdry_deposition_NHxNOy_as_N' :  idlvar='NHx+NOy (wet+dry deposition) [CAM]'
#
# radiation fluxes
    elif var=='FSLNT'  : idlvar='TOA radiative imbalance (positive downward)'
    elif var=='FSLNTC' : idlvar='Clearsky TOA radiative imbalance (positive downward)'
#
    elif var=='AOD_VISdivDAYFOC' : idlvar='AOD'
    elif var=='AODVISdivDAYFOC'  : idlvar='AOD'
    elif var=='D550_SO4' : idlvar='SO'+r'$_4$'+' AOD (550 nm)'
    elif var=='D550_SSdivDAYFOC' : idlvar='Sea-salt AOD (550 nm)'
#
# CLDTOT
    elif var=='CLDTOT' : idlvar='Vertically-integrated total cloud'
    elif var=='CLDHGH' : idlvar='Vertically-integrated high cloud'
    elif var=='CLDMED' : idlvar='Vertically-integrated mid-level cloud'
    elif var=='CLDLOW' : idlvar='Vertically-integrated low cloud'
#
    elif var=='NUMICE_columnburden' : idlvar='Ice crystal number (column burden)'
    elif var=='NUMLIQ_columnburden' : idlvar='Liquid cloud droplet number (column burden)'
#
    elif var=='TGCLDIWP' : idlvar='Ice cloud water path'
    elif var=='TGCLDLWP' : idlvar='Liquid cloud water path'
#
#   volcanic SO2 emissions CMIP7 input4MIPs
    elif var=='utsvolcemis' : idlvar='Volcanic SO'+r'$_2$'+' emissions'
    elif var=='height'      : idlvar='Height'
    elif var=='ext_sun'     : idlvar='Extinction'

# OCEAN
    elif var=='mmflxdmax26.0Nocn' : idlvar='AMOC at 26.0N'
#
# CF names
    elif var=='emich4'   : idlvar='CH'+r'$_4$'+' (surface emissions)'
    elif var=='hus'       : idlvar='Specific humidity'
    elif var=='ta'        : idlvar='Temperature'
    elif var=='tasmaxmin' : idlvar='Daily temperature range'
    elif var=='pr'        : idlvar='Precipitation'
    elif var=='tas'       : idlvar='Surface air temperature'
    elif var=='cl'        : idlvar='Cloud fraction'
    elif var=='clt'       : idlvar='Total cloud cover'
    elif var=='ch4'       : idlvar='CH'+r'$_4$'
    elif var=='o3'        : idlvar='Ozone'
    elif var=='o3_as_partpress' : idlvar='Ozone [part. press.]'
    elif var=='toz'       : idlvar='Total ozone column'
    elif var=='minusrsutcloud'     : idlvar='TOA SW (AS - CS) ERF'
    elif var=='minusrlutcloud'     : idlvar='TOA LW (AS - CS) ERF'
    elif var=='minusrsutrlutcloud' : idlvar='TOA SW+LW (AS - CS) ERF'
#
    else : idlvar=var

    return idlvar
