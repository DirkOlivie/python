def getbasicvarcomponents(var, expid):
#------------------------
    '''
    MODIFICATIONS
        (2022-06-22) added 
        (2025-11-30) correction for as N2O : I used 14./44 instead of 28./44 
        (2026-04-15) adding input argument expid
    '''
#    print('gevarcomponents : var = ',var)

# default value
    if   ( var== 'ICEFRAC_as_fraction')          : componentlist=['ICEFRAC'] ; weightlist=[1.]
    elif ( var== 'diagsumheatlndocn' )           : componentlist=['diagsumheatlnd','diagsumheatocn'] ; weightlist=[1.,1.]  
    elif ( var== 'diagsumheatice' )              : componentlist=['diagsumheatice_nh','diagsumheatice_sh'] ; weightlist=[1.,1.]  
    elif ( var== 'diagsumheatocnice' )           : componentlist=['diagsumheatocn','diagsumheatice_nh','diagsumheatice_sh'] ; weightlist=[1.,1.,1.]  
    elif ( var== 'diagsumheatlndocnice' )        : componentlist=['diagsumheatlnd','diagsumheatocn','diagsumheatice_nh','diagsumheatice_sh'] ; weightlist=[1.,1.,1.,1.]  
    elif ( var== 'diagsumheatlndocniceglc' )     : componentlist=['diagsumheatlnd','diagsumheatocn','diagsumheatice_nh','diagsumheatice_sh','diagsumheatglc'] ; weightlist=[1.,1.,1.,1.,1.]  
    elif ( var== 'diagsumheatlndrofocniceglc' )  : componentlist=['diagsumheatlnd','diagsumheatrof','diagsumheatocn','diagsumheatice_nh','diagsumheatice_sh','diagsumheatglc'] ; weightlist=[1.,1.,1.,1.,1.,1.]  
    elif ( var== 'diagsumheatsumoffline' )       : componentlist=['diagsumheatatm','diagsumheatlnd','diagsumheatrof','diagsumheatocn','diagsumheatice_nh','diagsumheatice_sh','diagsumheatglc'] ; weightlist=[1.,1.,1.,1.,1.,1.,1.]  
    elif ( var=='rsutcloud' )                    : componentlist=['rsut','rsutcs']  ; weightlist=[1.,-1.]
    elif ( var=='rlutcloud' )                    : componentlist=['rlut','rlutcs']  ; weightlist=[1.,-1.] 
    elif ( var=='minusrsutcloud' )               : componentlist=['rsut','rsutcs']  ; weightlist=[-1.,1.]   
    elif ( var=='minusrlutcloud' )               : componentlist=['rlut','rlutcs']  ; weightlist=[-1.,1.] 
    elif ( var=='minusrsutrlutcloud' )           : componentlist=['rsut','rsutcs','rlut','rlutcs'] ; weightlist=[-1.,1.,-1.,1.] 
    elif ( var=='minusrsut' )                    : componentlist=['rsut']  ; weightlist=[-1.]
    elif ( var=='minusrlut' )                    : componentlist=['rlut']  ; weightlist=[-1.]
    elif ( var=='minusrsutcs' )                  : componentlist=['rsutcs']  ; weightlist=[-1.]
    elif ( var=='minusrlutcs' )                  : componentlist=['rlutcs']  ; weightlist=[-1.]

# new aerosolfree radiation diagnostics
    elif ( var=='rsdt_noresm3' )                 : componentlist=['FSNTOA','FSUTOA'] ; weightlist=[1.,1.]
#
    elif ( var=='rsut_noresm3' )                 : componentlist=['FSUTOA'  ] ; weightlist=[1.]
    elif ( var=='rsutaf_noresm3' )               : componentlist=['FSUTOAAF'] ; weightlist=[1.]
    elif ( var=='rsutcs_noresm3' )               : componentlist=['SOLIN','FSNTOAC'] ; weightlist=[1.,-1.]
    elif ( var=='rsutcsaf_noresm3' )             : componentlist=['SOLIN','FSNTOACAF'] ; weightlist=[1.,-1.]

    elif ( var=='rlut_noresm3' )                 : componentlist=['FSNTOA'   ,'FSNT'    ,'FLNT'    ] ; weightlist=[1.,-1.,1.]
    elif ( var=='rlutaf_noresm3' )               : componentlist=['FSNTOAAF' ,'FSNTAF'  ,'FLNTAF'  ] ; weightlist=[1.,-1.,1.]
    elif ( var=='rlutcs_noresm3' )               : componentlist=['FSNTOAC'  ,'FSNTC'   ,'FLNTC'   ] ; weightlist=[1.,-1.,1.]
    elif ( var=='rlutcsaf_noresm3' )             : componentlist=['FSNTOACAF','FSNTCAF' ,'FLNTCAF' ] ; weightlist=[1.,-1.,1.]

    elif ( var=='direct_ERF_noresm3' )           : componentlist=['direct_ERF_SW_noresm3','direct_ERF_LW_noresm3'] ; weightlist=[1.,1.]
    elif ( var=='cloud_ERF_noresm3' )            : componentlist=['cloud_ERF_SW_noresm3','cloud_ERF_LW_noresm3']   ; weightlist=[1.,1.]
    elif ( var=='surfalb_ERF_noresm3' )          : componentlist=['surfalb_ERF_SW_noresm3','surfalb_ERF_LW_noresm3']   ; weightlist=[1.,1.]
    elif ( var=='ERF_noresm3' )                  : componentlist=['ERF_SW_noresm3','ERF_LW_noresm3']   ; weightlist=[1.,1.] 

    elif ( var=='direct_ERF_SW_noresm3' )        : componentlist=['rsdt_noresm3','rsut_noresm3','rsdt_noresm3','rsutaf_noresm3'                                  ] ; weightlist=[1.,-1.,-1., 1.]
    elif ( var=='cloud_ERF_SW_noresm3' )         : componentlist=[                              'rsdt_noresm3','rsutaf_noresm3','rsdt_noresm3','rsutcsaf_noresm3'] ; weightlist=[        1.,-1.,-1., 1.]
    elif ( var=='surfalb_ERF_SW_noresm3')        : componentlist=[                                                              'rsdt_noresm3','rsutcsaf_noresm3'] ; weightlist=[                1.,-1.]
    elif ( var=='ERF_SW_noresm3')                : componentlist=['rsdt_noresm3','rsut_noresm3'                                                                  ] ; weightlist=[1.,-1.] 

    elif ( var=='direct_ERF_LW_noresm3' )        : componentlist=['rlut_noresm3','rlutaf_noresm3'                   ] ; weightlist=[-1., 1.    ]
    elif ( var=='cloud_ERF_LW_noresm3' )         : componentlist=[               'rlutaf_noresm3','rlutcsaf_noresm3'] ; weightlist=[    -1., 1.]
    elif ( var=='surfalb_ERF_LW_noresm3' )       : componentlist=[                                'rlutcsaf_noresm3'] ; weightlist=[        -1.]
    elif ( var=='ERF_LW_noresm3' )               : componentlist=['rlut_noresm3'                                    ] ; weightlist=[-1.        ]


#   SW ERF    
    elif ( var=='minusWD_SO2' )                  : componentlist=['WD_SO2']  ; weightlist=[-1.]

    elif ( var=='minusdrych4' )                  : componentlist=['drych4']  ; weightlist=[-1.]

#   elif (var=='PRECT' )                         : componentlist = ['PRECC','PRECL']                                                    ; weightlist=[1.,1.]
    elif (var=='PRECCPRECL' )                         : componentlist = ['PRECC','PRECL']                                                    ; weightlist=[1.,1.]

    elif ( var=='OM_NIAIAC' )                    : componentlist = ['OM_NI','OM_AI','OM_AC']                                            ; weightlist=[1.,1.,1.]
    elif ( var=='SOA_NAA1' )                     : componentlist = ['SOA_NA','SOA_A1']                                                  ; weightlist=[1.,1.]

    elif ( var=='so4_a123')                      : componentlist = ['so4_a1','so4_a2','so4_a3']                                         ; weightlist=[1.,1.,1.]
    elif ( var=='bc_a14')                        : componentlist = ['bc_a1','bc_a4']                                              ; weightlist=[1.,1.]
    elif ( var=='pom_a14')                       : componentlist = ['pom_a1','pom_a4']                                            ; weightlist=[1.,1.]
    elif ( var=='soa_a12')                       : componentlist = ['soa_a1','soa_a2']                                            ; weightlist=[1.,1.]
    elif ( var=='dst_a123')                      : componentlist = ['dst_a1','dst_a2','dst_a3']                                ; weightlist=[1.,1.,1.]
    elif ( var=='ncl_a123')                      : componentlist = ['ncl_a1','ncl_a2','ncl_a3']                                ; weightlist=[1.,1.,1.]
    elif ( var=='cb_bc_a14')                     : componentlist = ['cb_bc_a1','cb_bc_a4']                                              ; weightlist=[1.,1.]
    elif ( var=='cb_pom_a14')                    : componentlist = ['cb_pom_a1','cb_pom_a4']                                            ; weightlist=[1.,1.]
    elif ( var=='cb_so4_a123')                   : componentlist = ['cb_so4_a1','cb_so4_a2','cb_so4_a3']                                ; weightlist=[1.,1.,1.]
    elif ( var=='cb_dst_a123')                   : componentlist = ['cb_dst_a1','cb_dst_a2','cb_dst_a3']                                ; weightlist=[1.,1.,1.]
    elif ( var=='cb_ncl_a123')                   : componentlist = ['cb_ncl_a1','cb_ncl_a2','cb_ncl_a3']                                ; weightlist=[1.,1.,1.]
    elif ( var=='cb_soa12345_a12')               : componentlist = ['cb_soa1_a1','cb_soa2_a1','cb_soa3_a1','cb_soa4_a1','cb_soa5_a1', \
                                                                    'cb_soa1_a2','cb_soa2_a2','cb_soa3_a2','cb_soa4_a2','cb_soa5_a2']   ; weightlist=[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]
    elif ( var=='cb_pom_a14_soa12345_a12')       : componentlist = ['cb_pom_a1','cb_pom_a4', \
                                                                    'cb_soa1_a1','cb_soa2_a1','cb_soa3_a1','cb_soa4_a1','cb_soa5_a1', \
                                                                    'cb_soa1_a2','cb_soa2_a2','cb_soa3_a2','cb_soa4_a2','cb_soa5_a2']   ; weightlist=[1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]
    elif ( var=='so4_a123_columnburden')         : componentlist = ['so4_a1_columnburden','so4_a2_columnburden','so4_a3_columnburden']                                         ; weightlist=[1.,1.,1.]
    elif ( var=='bc_a14_columnburden'  )         : componentlist = ['bc_a1_columnburden','bc_a4_columnburden']                                              ; weightlist=[1.,1.]
    elif ( var=='pom_a14_columnburden' )         : componentlist = ['pom_a1_columnburden','pom_a4_columnburden']                                            ; weightlist=[1.,1.]
    elif ( var=='soa_a12_columnburden' )         : componentlist = ['soa_a1_columnburden','soa_a2_columnburden']                                            ; weightlist=[1.,1.]
    elif ( var=='pom_a14_soa_a12_columnburden' ) : componentlist = ['pom_a1_columnburden','pom_a4_columnburden','soa_a1_columnburden','soa_a2_columnburden']                                            ; weightlist=[1.,1.,1.,1.]
    elif ( var=='dst_a123_columnburden')         : componentlist = ['dst_a1_columnburden','dst_a2_columnburden','dst_a3_columnburden']                                ; weightlist=[1.,1.,1.]
    elif ( var=='ncl_a123_columnburden')         : componentlist = ['ncl_a1_columnburden','ncl_a2_columnburden','ncl_a3_columnburden']                                ; weightlist=[1.,1.,1.]

    elif ( var=='SFdst_a123')                    : componentlist = ['SFdst_a1','SFdst_a2','SFdst_a3']                                ; weightlist=[1.,1.,1.]
    elif ( var=='SFncl_a123')                    : componentlist = ['SFncl_a1','SFncl_a2','SFncl_a3']                                ; weightlist=[1.,1.,1.]

    elif ( var=='EMI_OM_TOT_noresm2')            : componentlist = [         'SFOM_NI'                      ,'OM_NI_CMXF'             ] ; weightlist=[1.,1.]
    elif ( var=='EMI_BC_TOT_noresm2')            : componentlist = ['SFBC_N','SFBC_NI','SFBC_AX','BC_N_CMXF','BC_NI_CMXF','BC_AX_CMXF'] ; weightlist=[1.,1.,1.,1.,1.,1.]
    elif ( var=='EMI_BC_TOT_noresm3')            : componentlist = ['SFBC_N',          'SFBC_AX','BC_N_CMXF','BC_NI_CMXF','BC_AX_CMXF'] ; weightlist=[1.,   1.,1.,1.,1.]
    elif ( var=='EMI_SO2_TOT_noresm2')           : componentlist = ['SFSO2','SO2_CMXF']                                                 ; weightlist=[1.,1.]
    elif ( var=='EMI_SO4_TOT_noresm2')           : componentlist = ['SFSO4_PR','SO4_PR_CMXF']                                           ; weightlist=[1.,1.]
    elif ( var=='EMI_SO2SO4_as_SO2_TOT_noresm2') : componentlist = ['SFSO2','SO2_CMXF','SFSO4_PR','SO4_PR_CMXF']                        ; weightlist=[1.,1.,64./98.,64./98.]
    elif ( var=='EMI_SO2SO4_as_S_TOT_noresm2')   : componentlist = ['SFSO2','SO2_CMXF','SFSO4_PR','SO4_PR_CMXF']                        ; weightlist=[0.5,0.5,0.5*64./98.,0.5*64./98.]
    elif ( var=='EMI_DUST_TOT_noresm2')          : componentlist = ['SFDST_A2','SFDST_A3']                                              ; weightlist=[1.,1.]
    elif ( var=='EMI_SALT_TOT_noresm2')          : componentlist = ['SFSS_A1','SFSS_A2','SFSS_A3']                                      ; weightlist=[1.,1.,1.]
    elif ( var=='EMI_CO_TOT_noresm2')            : componentlist = ['SFCO','CO_CMXF']                                                   ; weightlist=[1.,1.]
    elif ( var=='EMI_NO_TOT_noresm2')            : componentlist = ['SFNO','NO_CMXF']                                                   ; weightlist=[1.,1.]
    elif ( var=='EMI_NO2_TOT_noresm2')           : componentlist = ['SFNO2','NO2_CMXF']                                                 ; weightlist=[1.,1.]
#   cesm2
    elif ( var=='EMI_SO2SO4_as_SO2_TOT_cesm2') : componentlist = ['SFSO2','SO2_CMXF','SFso4_a1','SFso4_a2','SFso4_a3','so4_a1_CMXF','so4_a2_CMXF'] ; weightlist=[1.,1.,64./115.,64./115.,64./115.,64./115.,64./115.]
    elif ( var=='EMI_SO4_TOT_cesm2') : componentlist = ['SFso4_a1','SFso4_a2','so4_a1_CLXF','so4_a2_CLXF'] ; weightlist=[1.,1.,1.,1.]

    elif ( var=='FSLNS')                         : componentlist = ['FSNS','FLNS']              ; weightlist=[1.,-1.]
    elif ( var=='FSLNT')                         : componentlist = ['FSNT','FLNT']              ; weightlist=[1.,-1.]
    elif ( var=='FSLNTC')                        : componentlist = ['FSNTC','FLNTC']            ; weightlist=[1.,-1.]
    elif ( var=='FSLNT_spAer')                   : componentlist = ['FSNT_SP2','FLNT']          ; weightlist=[1.,-1.]
    elif ( var=='cb_SOA_A1NA')                   : componentlist = ['cb_SOA_A1','cb_SOA_NA']    ; weightlist=[1.,1.]
    elif ( var=='SOA_A1NA_columnburden')         : componentlist = ['SOA_A1_columnburden','SOA_NA_columnburden']    ; weightlist=[1.,1.]
    elif ( var=='TREFMXMNAV' )                   : componentlist = ['TREFMXAV','TREFMNAV']      ; weightlist=[1.,-1.]             
    elif ( var=='minusFLNT')                     : componentlist = ['FLNT']                     ; weightlist=[-1.]
    elif ( var=='minusFLNTC')                    : componentlist = ['FLNTC']                    ; weightlist=[-1.]
    elif ( var=='LHFLXSHFLXFSNSFLNS')            : componentlist = ['LHFLX','SHFLX','FSNS','FLNS'] ; weightlist=[1.,1.,-1.,1.] # energy flux positive going into the atmosphere
# 
    elif ( var=='VCONC0105_columnburden') : componentlist = ['VCONC01_columnburden','VCONC05_columnburden']        ; weightlist=[1.,1.]
#
#   NHx/NOY dry/wet deposition in 
    elif ( var=='wetdry_deposition_NHx_as_N') : componentlist = ['wet_deposition_NHx_as_N','dry_deposition_NHx_as_N'] ; weightlist=[1.,1.]
    elif ( var=='wetdry_deposition_NOy_as_N') : componentlist = ['wet_deposition_NOy_as_N','dry_deposition_NOy_as_N'] ; weightlist=[1.,1.]
    elif ( var=='wetdry_deposition_NHxNOy_as_N') : componentlist = ['wet_deposition_NHx_as_N','dry_deposition_NHx_as_N','wet_deposition_NOy_as_N','dry_deposition_NOy_as_N'] ; weightlist=[1.,1.,1.,1.]
#
#   SAD surface area density    
#   cesm
    elif ( var=='sad_cesm2_dry_a1234' ) : componentlist = ['sad_cesm2_dry_a1','sad_cesm2_dry_a2','sad_cesm2_dry_a3','sad_cesm2_dry_a4'] ; weightlist=[1.,1.,1.,1.]
    elif ( var=='sad_cesm2_wet_a1234' ) : componentlist = ['sad_cesm2_wet_a1','sad_cesm2_wet_a2','sad_cesm2_wet_a3','sad_cesm2_wet_a4'] ; weightlist=[1.,1.,1.,1.]
#   noresm    
    elif ( var=='sad_noresm2_dry_m01020405' ) : componentlist = ['sad_noresm2_dry_m01','sad_noresm2_dry_m02','sad_noresm2_dry_m04','sad_noresm2_dry_m05',] ; weightlist=[1.,1.,1.,1.]
#
#   CESM number concentrations
    elif ( var=='num_a1234' ) : componentlist = ['num_a1','num_a2','num_a3','num_a4'] ; weightlist=[1.,1.,1.,1.]
    elif ( var=='num_a1234_as_concentration' ) : componentlist = ['num_a1_as_concentration','num_a2_as_concentration','num_a3_as_concentration','num_a4_as_concentration'] ; weightlist=[1.,1.,1.,1.]
#
#   CHEMISTRY
#   n2o
    elif ( var=='minusGS_N2O' )    : componentlist=['GS_N2O']     ; weightlist=[ -1.]
#   dms
    elif ( var=='minusGS_DMS' )    : componentlist=['GS_DMS']     ; weightlist=[ -1.]
#   chbr3
    elif ( var=='minusGS_CHBR3' )  : componentlist=['GS_CHBR3']     ; weightlist=[ -1.]
    elif ( var=='r_jchbr3_CHBR3_OH_columnburden' ) : componentlist=['r_jchbr3_columnburden','r_CHBR3_OH_columnburden'] ; weightlist=[1.,1.]
#   ch4
    elif ( var=='r_O1D_CH4abc' )              : componentlist=['r_O1D_CH4a','r_O1D_CH4b','r_O1D_CH4c'] ; weightlist=[1.,1.,1.]
    elif ( var=='r_O1D_CH4abc_columnburden' ) : componentlist=['r_O1D_CH4a_columnburden','r_O1D_CH4b_columnburden','r_O1D_CH4c_columnburden'] ; weightlist=[1.,1.,1.]
    elif ( var=='r_jch4_ab_columnburden'    ) : componentlist=['r_jch4_a_columnburden','r_jch4_b_columnburden'] ; weightlist=[1.,1.]

    elif ( var=='CHLDRY_CH4_TOT_noresm2' ) : 
                                             componentlist=['DF_CH4', \
                                                            'r_CH4_OH_columnburden','r_CL_CH4_columnburden','r_F_CH4_columnburden', \
                                                            'r_O1D_CH4a_columnburden','r_O1D_CH4b_columnburden','r_O1D_CH4c_columnburden', \
                                                            'r_jch4_a_columnburden','r_jch4_b_columnburden']
                                             weightlist=[1., \
                                                         1.,1.,1., \
                                                         1.,1.,1., \
                                                         1.,1.]
    elif ( var == 'r_CH4_OH_O1D_CH4abc_columnburden_abovetropopause' ) : 
                                                                         componentlist=['r_CH4_OH_columnburden_abovetropopause', \
                                                                                        'r_O1D_CH4a_columnburden_abovetropopause', \
                                                                                        'r_O1D_CH4b_columnburden_abovetropopause', \
                                                                                        'r_O1D_CH4c_columnburden_abovetropopause'] 
                                                                         weightlist=[1.,1.,1.,1.]
    elif ( var == 'r_CH4_OH_O1D_CH4abc_CL_CH4_columnburden_abovetropopause' ) : 
                                                                         componentlist=['r_CH4_OH_columnburden_abovetropopause', \
                                                                                        'r_O1D_CH4a_columnburden_abovetropopause', \
                                                                                        'r_O1D_CH4b_columnburden_abovetropopause', \
                                                                                        'r_O1D_CH4c_columnburden_abovetropopause', \
                                                                                        'r_CL_CH4_columnburden_abovetropopause'] 
                                                                         weightlist=[1.,1.,1.,1.,1,]
#   (CNRM)
    elif ( var == 'ch4lossoh_ch4losso1d_ch4losscl_columnburden_abovetropopause' ) : 
                                                                         componentlist=['ch4lossoh_columnburden_abovetropopause', \
                                                                                        'ch4losso1d_columnburden_abovetropopause', \
                                                                                        'ch4losscl_columnburden_abovetropopause']
                                                                         weightlist = [1.,1.,1.]

#   ch2o (formaldehyde)
    elif ( var=='CHLWETDRY_CH2O_TOT_noresm2' ) :
                                                componentlist=['CH2O_CHML_columnburden','WD_CH2O','DF_CH2O']
                                                weightlist   =[ 1.                     , -1.    , 1.       ]  
    elif ( var=='CHPEMI_CH2O_TOT_noresm2' ) :
                                                componentlist=['CH2O_CHMP_columnburden','SFCH2O']
                                                weightlist   =[1.                      , 1.     ]

#   CO2_columnburden 
    elif ( var=='CO2_columnburden_as_vmr' ) : componentlist=['CO2_columnburden'] ; weightlist=[1.]
    elif ( var=='CO2_columnburden_as_RF'  ) : componentlist=['CO2_columnburden'] ; weightlist=[1.]

#   inteactive CO2
    elif ( var=='TMCO2_FFFLNDOCN' ) : componentlist=['TMCO2_FFF','TMCO2_LND','TMCO2_OCN'] ; weightlist=[1.,1.,1.]
    elif ( var=='SFCO2_FFFLNDOCN' ) : componentlist=['SFCO2_FFF','SFCO2_LND','SFCO2_OCN'] ; weightlist=[1.,1.,1.]

    elif ( var=='TMCO2_FFF_offset_minus_SFCO2_FFF_cumulative' ) : componentlist=['TMCO2_FFF_offset','SFCO2_FFF_cumulative'] ; weightlist=[1.,-1.]
    elif ( var=='TMCO2_LND_offset_minus_SFCO2_LND_cumulative' ) : componentlist=['TMCO2_LND_offset','SFCO2_LND_cumulative'] ; weightlist=[1.,-1.]
    elif ( var=='TMCO2_OCN_offset_minus_SFCO2_OCN_cumulative' ) : componentlist=['TMCO2_OCN_offset','SFCO2_OCN_cumulative'] ; weightlist=[1.,-1.]
    elif ( var=='TMCO2_FFFLNDOCN_offset_minus_SFCO2_FFFLNDOCN_cumulative' ) : componentlist=['TMCO2_FFFLNDOCN_offset','SFCO2_FFFLNDOCN_cumulative'] ; weightlist=[1.,-1.]
    elif ( var=='TMCO2_offset_minus_SFCO2_cumulative' ) : componentlist=['TMCO2_offset','SFCO2_cumulative'] ; weightlist=[1.,-1.]

    elif ( var=='SFCO2_ac_CO2_columnburden'           ) : componentlist=['SFCO2','ac_CO2_columnburden'] ; weightlist=[1.,1.]
    elif ( var=='SFCO2_FFF_ac_CO2_columnburden'       ) : componentlist=['SFCO2_FFF','ac_CO2_columnburden'] ; weightlist=[1.,1.]
    elif ( var=='SFCO2_FFFLNDOCN_ac_CO2_columnburden' ) : componentlist=['SFCO2_FFF','SFCO2_LND','SFCO2_OCN','ac_CO2_columnburden'] ; weightlist=[1.,1.,1.,1.]

    elif ( var=='SFCO2_LND_minus_FCO2xLANDFRAC'       ) : componentlist=['SFCO2_LND','FCO2xLANDFRAC'] ; weightlist=[1.,-1.]  
    elif ( var=='FCO2xLANDFRAC_minus_SFCO2_LND'       ) : componentlist=['FCO2xLANDFRAC','SFCO2_LND'] ; weightlist=[1.,-1.]  

#   CO2 as [C]
    elif ( var=='SFCO2_FFF_as_C' ) : componentlist=['SFCO2_FFF'] ; weightlist=[12.01/44.009]

#   CanESM5 : CH4 emissions
    elif ( var=='emich4_canesm5' ) : componentlist=['emiach4corr','emibbch4','emiotherch4','wetlandCH4prod'] ; weightlist=[1.,1.,1.,1.] 

#                                          
#   GHAN ERF SPLIT
#   sw toa
    elif ( var=='direct_ERF_SW_noresm2' )  : componentlist=['FSNT','FSNT_DRF']     ; weightlist=[ 1.,-1.]
    elif ( var=='cloud_ERF_SW_noresm2' )   : componentlist=['FSNT_DRF','FSNTCDRF'] ; weightlist=[ 1.,-1.]
    elif ( var=='surfalb_ERF_SW_noresm2' ) : componentlist=['FSNTCDRF']            ; weightlist=[ 1.]    
#   lw toa   
    elif ( var=='direct_ERF_LW_noresm2' )  : componentlist=['FLNT','FLNT_DRF']     ; weightlist=[-1., 1.]
    elif ( var=='cloud_ERF_LW_noresm2' )   : componentlist=['FLNT_DRF','FLNTCDRF'] ; weightlist=[-1., 1.]
    elif ( var=='surfalb_ERF_LW_noresm2' ) : componentlist=['FLNTCDRF']            ; weightlist=[-1.]    
#   sw+lw toa
    elif ( var=='direct_ERF_noresm2' )     : componentlist=['FSNT','FSNT_DRF'    ,'FLNT','FLNT_DRF']     ; weightlist=[ 1.,-1.,-1., 1.]
    elif ( var=='cloud_ERF_noresm2' )      : componentlist=['FSNT_DRF','FSNTCDRF','FLNT_DRF','FLNTCDRF'] ; weightlist=[ 1.,-1.,-1., 1.]
    elif ( var=='surfalb_ERF_noresm2' )    : componentlist=['FSNTCDRF'           ,'FLNTCDRF']            ; weightlist=[ 1.    ,-1.    ]
#   sw surface    
    elif ( var=='direct_ERFsurf_SW_noresm2' )  : componentlist=['FSNS','FSNS_DRF']     ; weightlist=[ 1.,-1.]
    elif ( var=='cloud_ERFsurf_SW_noresm2' )   : componentlist=['FSNS_DRF','FSNSCDRF'] ; weightlist=[ 1.,-1.]
    elif ( var=='surfalb_ERFsurf_SW_noresm2' ) : componentlist=['FSNSCDRF']            ; weightlist=[ 1.]
#   lw surface
    elif ( var=='direct_ERFsurf_LW_noresm2' )  : componentlist=['FLNS','FLNS_DRF']     ; weightlist=[-1., 1.]
    elif ( var=='cloud_ERFsurf_LW_noresm2' )   : componentlist=['FLNS_DRF','FLNSCDRF'] ; weightlist=[-1., 1.]
    elif ( var=='surfalb_ERFsurf_LW_noresm2' ) : componentlist=['FLNSCDRF']            ; weightlist=[-1.]
#   sw+lw surface
    elif ( var=='direct_ERFsurf_noresm2' )     : componentlist=['FSNS','FSNS_DRF'    ,'FLNS','FLNS_DRF']     ; weightlist=[ 1.,-1.,-1., 1.]
    elif ( var=='cloud_ERFsurf_noresm2' )      : componentlist=['FSNS_DRF','FSNSCDRF','FLNS_DRF','FLNSCDRF'] ; weightlist=[ 1.,-1.,-1., 1.]
    elif ( var=='surfalb_ERFsurf_noresm2' )    : componentlist=['FSNSCDRF'           ,'FLNSCDRF']            ; weightlist=[ 1.    ,-1.    ]
#   some strange combinations of Alf
    elif ( var=='FSNT_minus_FSNTCDRF' ) : componentlist=['FSNT','FSNTCDRF'] ; weightlist=[1.,-1.]
    elif ( var=='FSNS_minus_FSNSCDRF' ) : componentlist=['FSNS','FSNSCDRF'] ; weightlist=[1.,-1.]
#
#   GHAN ERF SPLIT for SP-AEROSOL
    elif ( var=='direct_ERF_SW_spAer_noresm2' ) : componentlist=['FSNT_SP2','FSNT_DRF']     ; weightlist=[ 1.,-1.]
    elif ( var=='direct_ERF_spAer_noresm2' )    : componentlist=['FSNT_SP2','FSNT_DRF'    ,'FLNT','FLNT_DRF']     ; weightlist=[ 1.,-1.,-1., 1.]    
#   toa
    elif ( var=='FSNT_SP2_minus_FSNT_SP'  ) : componentlist=['FSNT_SP2','FSNT_SP']     ; weightlist=[ 1.,-1.]
    elif ( var=='FSNT_SP3_minus_FSNT_SP2' ) : componentlist=['FSNT_SP3','FSNT_SP2']    ; weightlist=[ 1.,-1.]
    elif ( var=='FSNT_SP3_minus_FSNT_SP'  ) : componentlist=['FSNT_SP3','FSNT_SP']     ; weightlist=[ 1.,-1.]
#   surface
    elif ( var=='FSNS_SP2_minus_FSNS_SP'  ) : componentlist=['FSNS_SP2','FSNS_SP']     ; weightlist=[ 1.,-1.]
    elif ( var=='FSNS_SP3_minus_FSNS_SP2' ) : componentlist=['FSNS_SP3','FSNS_SP2']    ; weightlist=[ 1.,-1.]
    elif ( var=='FSNS_SP3_minus_FSNS_SP'  ) : componentlist=['FSNS_SP3','FSNS_SP']     ; weightlist=[ 1.,-1.]

#   TOTAL BROMINE
    elif ( var == 'BRY_SUM' )         : componentlist=['BR','BRCL','BRO','BRONO2','HBR','HOBR'] ; weightlist=[1.,1.,1.,1.,1.,1.]
    elif ( var == 'BRY_SUM_layer00' ) : componentlist=['BR_layer00','BRCL_layer00','BRO_layer00','BRONO2_layer00','HBR_layer00','HOBR_layer00'] ; weightlist=[1.,1.,1.,1.,1.,1.]
    elif ( var == 'BRY_SUM_layer06' ) : componentlist=['BR_layer06','BRCL_layer06','BRO_layer06','BRONO2_layer06','HBR_layer06','HOBR_layer06'] ; weightlist=[1.,1.,1.,1.,1.,1.]
#
    elif ( var == 'BRY_SCALED' )         : componentlist = ['BRY'] ; weightlist = [99.716850/79.904] # MW(BRy)/MW(BR)
    elif ( var == 'BRY_SCALED_layer00' ) : componentlist = ['BRY_layer00'] ; weightlist = [99.716850/79.904] # MW(BRy)/MW(BR)
    elif ( var == 'BRY_SCALED_layer06' ) : componentlist = ['BRY_layer06'] ; weightlist = [99.716850/79.904] # MW(BRy)/MW(BR)
#   TOTAL CHLORINE
    elif ( var == 'CLY_SUM' ) : componentlist=['CL','CLO','HOCL','CL2','CL2O2','OCLO','HCL','CLONO2'] ; weightlist=[1.,1.,1.,1.,1.,1.,1.,1.]
    elif ( var == 'CLY_SUM_layer00' ) : componentlist=['CL_layer00','CLO_layer00','HOCL_layer00','CL2_layer00','CL2O2_layer00','OCLO_layer00','HCL_layer00','CLONO2_layer00'] ; weightlist=[1.,1.,1.,2.,2.,1.,1.,1.]
    elif ( var == 'CLY_SUM_layer06' ) : componentlist=['CL_layer06','CLO_layer06','HOCL_layer06','CL2_layer06','CL2O2_layer06','OCLO_layer06','HCL_layer06','CLONO2_layer06'] ; weightlist=[1.,1.,1.,2.,2.,1.,1.,1.]
#
    elif ( var == 'CLY_SCALED' )         : componentlist = ['CLY'] ; weightlist = [100.916850/35.4527] # MW(CLy)/MW(CL)
    elif ( var == 'CLY_SCALED_layer00' ) : componentlist = ['CLY_layer00'] ; weightlist = [100.916850/35.4527] # MW(CLy)/MW(CL)
    elif ( var == 'CLY_SCALED_layer06' ) : componentlist = ['CLY_layer06'] ; weightlist = [100.916850/35.4527] # MW(CLy)/MW(CL)
#   
#   CESM mass concentrations
    elif ( var=='ncl_a1a2a3' ) : componentlist = ['ncl_a1','ncl_a2','ncl_a3'] ; weightlist=[1.,1.,1.]
    elif ( var=='bc_a1a4' )    : componentlist = ['bc_a1','bc_a4'] ; weightlist=[1.,1.]

#   CESM : diameter -> radius (dry)
    elif ( var=='rgnum1')              : componentlist = ['dgnum1']                   ; weightlist=[0.5] 
    elif ( var=='rgnum2')              : componentlist = ['dgnum2']                   ; weightlist=[0.5] 
    elif ( var=='rgnum3')              : componentlist = ['dgnum3']                   ; weightlist=[0.5] 
    elif ( var=='rgnum4')              : componentlist = ['dgnum4']                   ; weightlist=[0.5] 
#   CESM : diameter -> radius (wet)
    elif ( var=='rgnumwet1')           : componentlist = ['dgnumwet1']                ; weightlist=[0.5] 
    elif ( var=='rgnumwet2')           : componentlist = ['dgnumwet2']                ; weightlist=[0.5] 
    elif ( var=='rgnumwet3')           : componentlist = ['dgnumwet3']                ; weightlist=[0.5] 
    elif ( var=='rgnumwet4')           : componentlist = ['dgnumwet4']                ; weightlist=[0.5] 
#   ESGF - CMIP6
    elif ( var=='tasmaxmin')           : componentlist = ['tasmax','tasmin']                ; weightlist=[1.,-1.]
#
#   nitrogen budget
    elif ( var=='SFNH3_as_N')          : componentlist = ['SFNH3'] ; weightlist=[14./17.]
    elif ( var=='SFNH4_as_N')          : componentlist = ['SFNH4'] ; weightlist=[14./18.]
    elif ( var=='WD_NH3_as_N')          : componentlist = ['WD_NH3'] ; weightlist=[14./17.]
    elif ( var=='WD_NH4_as_N')          : componentlist = ['WD_NH4'] ; weightlist=[14./18.]
    elif ( var=='DF_NH3_as_N')          : componentlist = ['DF_NH3'] ; weightlist=[14./17.]
    elif ( var=='DF_NH4_as_N')          : componentlist = ['DF_NH4'] ; weightlist=[14./18.]
#
#   nitrogen from land model
    elif ( var=='F_N2O_DENIT_NITxLANDFRAC')        : componentlist = ['F_N2O_DENITxLANDFRAC','F_N2O_NITxLANDFRAC'] ; weightlist=[1.,1.]
    elif ( var=='F_N2O_DENIT_NITxLANDFRAC_as_N2O') : componentlist = ['F_N2O_DENITxLANDFRAC','F_N2O_NITxLANDFRAC'] ; weightlist=[44./28., 44./28.] # weightlist=[44./14. , 44./14.] (until 2025-11-30)
    elif ( var=='FN2OxLANDFRAC_as_N2O')            : componentlist = ['FN2OxLANDFRAC']                             ; weightlist=[44./28.]          # weightlist=[44./14.]
#   nitrogren im CAM
    elif ( var=='emin2oland_as_N2O')               : componentlist = ['emin2oland']                                ; weightlist=[44./28.]          # [44./14.] 
    elif ( var=='emin2oocean_as_N')                : componentlist = ['emin2oocean']                               ; weightlist=[28./44.]          # [44./14.] 
    elif ( var=='SFN2O_as_N')                      : componentlist = ['SFN2O']                                     ; weightlist=[28./44.]          # [14./44.] 
#
#   wet + dry deposition
#   dust : wet + dry 
    elif ( var=='WETDRY_DUST_TOT_noresm2') : 
                                             componentlist=['DST_A2DDF','DST_A2_OCWDDF','DST_A2SFWET','DST_A2_OCWSFWET', \
                                                            'DST_A3DDF','DST_A3_OCWDDF','DST_A3SFWET','DST_A3_OCWSFWET'] 
                                             weightlist=[1.,1.,-1.,-1., \
                                                         1.,1.,-1.,-1.]
#   dust : wet
    elif ( var=='WET_DUST_TOT_noresm2') : 
                                          componentlist=['DST_A2SFWET','DST_A2_OCWSFWET', \
                                                         'DST_A3SFWET','DST_A3_OCWSFWET']
                                          weightlist=[-1.,-1., \
                                                      -1.,-1.]
#   dust : dry
    elif ( var=='DRY_DUST_TOT_noresm2') : 
                                          componentlist=['DST_A2DDF','DST_A2_OCWDDF', \
                                                         'DST_A3DDF','DST_A3_OCWDDF'] 
                                          weightlist=[1.,1., \
                                                      1.,1.] 

#   salt : wet + dry
    elif ( var=='WETDRY_SALT_TOT_noresm2') : 
                                             componentlist=['SS_A1DDF','SS_A1_OCWDDF','SS_A1SFWET','SS_A1_OCWSFWET', \
                                                            'SS_A2DDF','SS_A2_OCWDDF','SS_A2SFWET','SS_A2_OCWSFWET', \
                                                            'SS_A3DDF','SS_A3_OCWDDF','SS_A3SFWET','SS_A3_OCWSFWET']
                                             weightlist=[1.,1.,-1.,-1., \
                                                         1.,1.,-1.,-1., \
                                                         1.,1.,-1.,-1.]
#    salt : wet     
    elif ( var=='WET_SALT_TOT_noresm2' ) : 
                                           componentlist=['SS_A1SFWET','SS_A1_OCWSFWET', \
                                                          'SS_A2SFWET','SS_A2_OCWSFWET', \
                                                          'SS_A3SFWET','SS_A3_OCWSFWET']
                                           weightlist=[-1.,-1., \
                                                       -1.,-1., \
                                                       -1.,-1.]
#    salt : dry
    elif ( var=='DRY_SALT_TOT_noresm2' ) : 
                                           componentlist=['SS_A1DDF','SS_A1_OCWDDF', \
                                                          'SS_A2DDF','SS_A2_OCWDDF', \
                                                          'SS_A3DDF','SS_A3_OCWDDF']
                                           weightlist=[1.,1., \
                                                       1.,1., \
                                                       1.,1.]

#    BC : wet + dry
    elif ( var=='WETDRY_BC_TOT_noresm2' ) : 
                                            componentlist=['BC_NDDF' ,'BC_N_OCWDDF' ,'BC_NSFWET' ,'BC_N_OCWSFWET' , \
                                                           'BC_ADDF' ,'BC_A_OCWDDF' ,'BC_ASFWET' ,'BC_A_OCWSFWET' , \
                                                           'BC_NIDDF','BC_NI_OCWDDF','BC_NISFWET','BC_NI_OCWSFWET', \
                                                           'BC_AIDDF','BC_AI_OCWDDF','BC_AISFWET','BC_AI_OCWSFWET', \
                                                           'BC_AXDDF'               ,'BC_AXSFWET'                 , \
                                                           'BC_ACDDF','BC_AC_OCWDDF','BC_ACSFWET','BC_AC_OCWSFWET']
                                            weightlist=[1.,1.,-1.,-1., \
                                                        1.,1.,-1.,-1., \
                                                        1.,1.,-1.,-1., \
                                                        1.,1.,-1.,-1., \
                                                        1.,   -1.,     \
                                                        1.,1.,-1.,-1.]
#    BC : wet
    elif ( var=='WET_BC_TOT_noresm2' ) : 
                                         componentlist=[ 'BC_NSFWET', 'BC_N_OCWSFWET', \
                                                         'BC_ASFWET', 'BC_A_OCWSFWET', \
                                                        'BC_NISFWET','BC_NI_OCWSFWET', \
                                                        'BC_AISFWET','BC_AI_OCWSFWET', \
                                                        'BC_AXSFWET'                 , \
                                                        'BC_ACSFWET','BC_AC_OCWSFWET']
                                         weightlist=[-1.,-1.,\
                                                     -1.,-1.,\
                                                     -1.,-1.,\
                                                     -1.,-1.,\
                                                     -1.,    \
                                                     -1.,-1.] 
#    BC : dry
    elif ( var=='DRY_BC_TOT_noresm2' ) : 
                                         componentlist=['BC_NDDF' ,'BC_N_OCWDDF' , \
                                                        'BC_ADDF' ,'BC_A_OCWDDF' , \
                                                        'BC_NIDDF','BC_NI_OCWDDF', \
                                                        'BC_AIDDF','BC_AI_OCWDDF', \
                                                        'BC_AXDDF'               , \
                                                        'BC_ACDDF','BC_AC_OCWDDF']
                                         weightlist=[1.,1., \
                                                     1.,1., \
                                                     1.,1., \
                                                     1.,1., \
                                                     1.,    \
                                                     1.,1.] 

#    OM : wet + dry
    elif ( var=='WETDRY_OM_TOT_noresm2' ) : 
                                            componentlist=['OM_NIDDF','OM_NI_OCWDDF','OM_NISFWET','OM_NI_OCWSFWET', \
                                                           'OM_AIDDF','OM_AI_OCWDDF','OM_AISFWET','OM_AI_OCWSFWET', \
                                                           'OM_ACDDF','OM_AC_OCWDDF','OM_ACSFWET','OM_AC_OCWSFWET']
                                            weightlist=[1.,1.,-1.,-1., \
                                                        1.,1.,-1.,-1., \
                                                        1.,1.,-1.,-1.]
#    OM : wet
    elif ( var=='WET_OM_TOT_noresm2' ) : 
                                         componentlist=['OM_NISFWET','OM_NI_OCWSFWET', \
                                                        'OM_AISFWET','OM_AI_OCWSFWET', \
                                                        'OM_ACSFWET','OM_AC_OCWSFWET']
                                         weightlist=[-1.,-1., \
                                                     -1.,-1., \
                                                     -1.,-1.]
#    OM : dry
    elif ( var=='DRY_OM_TOT_noresm2' ) : 
                                         componentlist=['OM_NIDDF','OM_NI_OCWDDF', \
                                                        'OM_AIDDF','OM_AI_OCWDDF', \
                                                        'OM_ACDDF','OM_AC_OCWDDF']
                                         weightlist=[1.,1., \
                                                     1.,1., \
                                                     1.,1.]

#    OM + SOA : wet + dry
    elif ( var=='WETDRY_OM_SOA_TOT_noresm2' ) : 
                                                componentlist=[ 'OM_NIDDF', 'OM_NI_OCWDDF', 'OM_NISFWET', 'OM_NI_OCWSFWET', \
                                                                'OM_AIDDF', 'OM_AI_OCWDDF', 'OM_AISFWET', 'OM_AI_OCWSFWET', \
                                                                'OM_ACDDF', 'OM_AC_OCWDDF', 'OM_ACSFWET', 'OM_AC_OCWSFWET', \
                                                               'SOA_NADDF','SOA_NA_OCWDDF','SOA_NASFWET','SOA_NA_OCWSFWET', \
                                                               'SOA_A1DDF','SOA_A1_OCWDDF','SOA_A1SFWET','SOA_A1_OCWSFWET']
                                                weightlist=[1.,1.,-1.,-1., \
                                                            1.,1.,-1.,-1., \
                                                            1.,1.,-1.,-1., \
                                                            1.,1.,-1.,-1., \
                                                            1.,1.,-1.,-1.] 
#    OM + SOA : wet
    elif ( var=='WET_OM_SOA_TOT_noresm2' ) : 
                                             componentlist=[ 'OM_NISFWET', 'OM_NI_OCWSFWET', \
                                                             'OM_AISFWET', 'OM_AI_OCWSFWET', \
                                                             'OM_ACSFWET', 'OM_AC_OCWSFWET', \
                                                            'SOA_NASFWET','SOA_NA_OCWSFWET', \
                                                            'SOA_A1SFWET','SOA_A1_OCWSFWET']
                                             weightlist=[-1.,-1., \
                                                         -1.,-1., \
                                                         -1.,-1., \
                                                         -1.,-1., \
                                                         -1.,-1.]
#    OM + SOA : dry
    elif ( var=='DRY_OM_SOA_TOT_noresm2' ) : 
                                             componentlist=[ 'OM_NIDDF', 'OM_NI_OCWDDF', \
                                                             'OM_AIDDF', 'OM_AI_OCWDDF', \
                                                             'OM_ACDDF', 'OM_AC_OCWDDF', \
                                                            'SOA_NADDF','SOA_NA_OCWDDF', \
                                                            'SOA_A1DDF','SOA_A1_OCWDDF']
                                             weightlist=[1.,1., \
                                                         1.,1., \
                                                         1.,1., \
                                                         1.,1., \
                                                         1.,1.]
#    OM only : wet+dry
    elif ( var=='WETDRY_POA_TOT_noresm2' ) : 
                                             componentlist=['OM_NIDDF','OM_NI_OCWDDF','OM_NISFWET','OM_NI_OCWSFWET', \
                                                            'OM_AIDDF','OM_AI_OCWDDF','OM_AISFWET','OM_AI_OCWSFWET', \
                                                            'OM_ACDDF','OM_AC_OCWDDF','OM_ACSFWET','OM_AC_OCWSFWET']
                                             weightlist=[1.,1.,-1.,-1., \
                                                         1.,1.,-1.,-1., \
                                                         1.,1.,-1.,-1.] 
#   SOA only : wet+dry
    elif ( var=='WETDRY_SOA_TOT_noresm2' ) : 
                                             componentlist=['SOA_NADDF','SOA_NA_OCWDDF','SOA_NASFWET','SOA_NA_OCWSFWET', \
                                                            'SOA_A1DDF','SOA_A1_OCWDDF','SOA_A1SFWET','SOA_A1_OCWSFWET']
                                             weightlist=[1.,1.,-1.,-1., \
                                                         1.,1.,-1.,-1.]
#    SULFATE : wet + dry 
    elif ( var=='WETDRY_SULFATE_TOT_noresm2' ) : 
                                                 componentlist=['SO4_NADDF','SO4_NA_OCWDDF','SO4_NASFWET','SO4_NA_OCWSFWET', \
                                                                'SO4_PRDDF','SO4_PR_OCWDDF','SO4_PRSFWET','SO4_PR_OCWSFWET', \
                                                                'SO4_A1DDF','SO4_A1_OCWDDF','SO4_A1SFWET','SO4_A1_OCWSFWET', \
                                                                'SO4_A2DDF','SO4_A2_OCWDDF','SO4_A2SFWET','SO4_A2_OCWSFWET', \
                                                                'SO4_ACDDF','SO4_AC_OCWDDF','SO4_ACSFWET','SO4_AC_OCWSFWET']
                                                 weightlist=[1.,1.,-1.,-1.,\
                                                             1.,1.,-1.,-1.,\
                                                             1.,1.,-1.,-1.,\
                                                             1.,1.,-1.,-1.,\
                                                             1.,1.,-1.,-1.]
    elif ( var=='WET_SULFATE_TOT_noresm2' ) : 
                                              componentlist=['SO4_NASFWET','SO4_NA_OCWSFWET', \
                                                             'SO4_PRSFWET','SO4_PR_OCWSFWET', \
                                                             'SO4_A1SFWET','SO4_A1_OCWSFWET', \
                                                             'SO4_A2SFWET','SO4_A2_OCWSFWET', \
                                                             'SO4_ACSFWET','SO4_AC_OCWSFWET']
                                              weightlist=[-1.,-1., \
                                                          -1.,-1., \
                                                          -1.,-1., \
                                                          -1.,-1., \
                                                          -1.,-1.]
    elif ( var=='DRY_SULFATE_TOT_noresm2' ) : 
                                              componentlist=['SO4_NADDF','SO4_NA_OCWDDF', \
                                                             'SO4_PRDDF','SO4_PR_OCWDDF', \
                                                             'SO4_A1DDF','SO4_A1_OCWDDF', \
                                                             'SO4_A2DDF','SO4_A2_OCWDDF', \
                                                             'SO4_ACDDF','SO4_AC_OCWDDF']
                                              weightlist=[1.,1., \
                                                          1.,1., \
                                                          1.,1., \
                                                          1.,1., \
                                                          1.,1.]
#    AMMONIUM
    elif ( var=='WETDRY_AMMONIUM_TOT_noresm2' ) : 
                                                  componentlist=['NH4_A1DDF','NH4_A1_OCWDDF','NH4_A1SFWET','NH4_A1_OCWSFWET']
                                                  weightlist=[1.,1.,-1.,-1.]
#    NITRATE
    elif ( var=='WETDRY_NITRATE_TOT_noresm2' ) : 
                                                 componentlist=['NO3_A1DDF' ,'NO3_A1_OCWDDF' ,'NO3_A1SFWET' ,'NO3_A1_OCWSFWET', \
                                                                'NO3_DSTDDF','NO3_DST_OCWDDF','NO3_DSTSFWET','NO3_DST_OCWSFWET', \
                                                                'NO3_SSDDF' ,'NO3_SS_OCWDDF' ,'NO3_SSSFWET' ,'NO3_SS_OCWSFWET']
                                                 weightlist=[1.,1.,-1.,-1., \
                                                             1.,1.,-1.,-1., \
                                                             1.,1.,-1.,-1.]
#    SOA
    elif ( var=='WETDRY_SOA_TOT_noresm2' ) : 
                                        componentlist=['SOA_NADDF','SOA_NA_OCWDDF','SOA_NASFWET','SOA_NA_OCWSFWET', \
                                                       'SOA_A1DDF','SOA_A1_OCWDDF','SOA_A1SFWET','SOA_A1_OCWSFWET']
                                        weightlist=[1.,1.,-1.,-1., \
                                                    1.,1.,-1.,-1.]
#
#   NORESM3
    elif ( var=='wetdry_BC' )      : componentlist=['wet_BC'     ,'dry_BC']      ; weightlist   =[1.,1.]
    elif ( var=='wetdry_OM' )      : componentlist=['wet_OM'     ,'dry_OM']      ; weightlist   =[1.,1.]
    elif ( var=='wetdry_SULFATE' ) : componentlist=['wet_SULFATE','dry_SULFATE'] ; weightlist   =[1.,1.]
    elif ( var=='wetdry_DUST' )    : componentlist=['wet_DUST'   ,'dry_DUST']    ; weightlist   =[1.,1.]
    elif ( var=='wetdry_SALT' )    : componentlist=['wet_SALT'   ,'dry_SALT']    ; weightlist   =[1.,1.]

#   MAM4
    elif ( var=='WETDRY_bc_a14_TOT_cesm2') : 
                                        componentlist=['bc_a1DDF','bc_a4DDF','bc_a1SFWET','bc_a4SFWET','bc_c1SFWET','bc_c4SFWET']
                                        weightlist   =[1.,1.,-1.,-1.,-1.,-1.]
    elif ( var=='WETDRY_pom_a14_TOT_cesm2') :
                                        componentlist=['pom_a1DDF','pom_a4DDF','pom_a1SFWET','pom_a4SFWET','pom_c1SFWET','pom_c4SFWET']
                                        weightlist   =[1.,1.,-1.,-1.,-1.,-1.]
    elif ( var=='WETDRY_so4_a123_TOT_cesm2') :
                                        componentlist=['so4_a1DDF','so4_a2DDF','so4_a3DDF','so4_a1SFWET','so4_a2SFWET','so4_a3SFWET','so4_c1SFWET','so4_c2SFWET','so4_c3SFWET']
                                        weightlist   =[1.,1.,1.,-1.,-1.,-1.,-1.,-1.,-1.]
    elif ( var=='WETDRY_ncl_a123_TOT_cesm2') :
                                        componentlist=['ncl_a1DDF','ncl_a2DDF','ncl_a3DDF','ncl_a1SFWET','ncl_a2SFWET','ncl_a3SFWET','ncl_c1SFWET','ncl_c2SFWET','ncl_c3SFWET']
                                        weightlist   =[1.,1.,1.,-1.,-1.,-1.,-1.,-1.,-1.]
    elif ( var=='WETDRY_dst_a123_TOT_cesm2') :
                                        componentlist=['dst_a1DDF','dst_a2DDF','dst_a3DDF','dst_a1SFWET','dst_a2SFWET','dst_a3SFWET','dst_c1SFWET','dst_c2SFWET','dst_c3SFWET']
                                        weightlist   =[1.,1.,1.,-1.,-1.,-1.,-1.,-1.,-1.]
#
    elif ( var=='voltrocn' ) :
        if ( \
#            ne30pg3 
             expid == 'n1850.ne16pg3_tn14.noresm3_0_beta11.CAMtuning.20260224' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta12.lamult_reduction.20260314' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta12.ndiff_surface_align.20260317' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_drydep_oldBLOM.2026-04-17' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_oldBLO_oldBLOMv32.2026-04-17' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11.OcnTune2026-04-19' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta13.Run11.2026-04-15' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-04-24' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-05-04' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.Olivia.2026-05-05' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12_ATMtune.Olivia.2026-05-10' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12_ATMtune2.Olivia.2026-05-12' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.c8_4p55.Olivia.2026-05-13' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.Olivia.2026-05-18' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.4p95' \

#            ne30pg16
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta12a-run1_yr001_olivia.20260313' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run4_yr061.20260429' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run5_yr076.20260504' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run7_yr101.20260508' \
            \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run6_yr001.20260505' \
            \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run10_yr101.20260513' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run12_yr101.20260516' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta14-run13_yr101.20260521' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta15-run12_yr151.cplhist.20260529' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta18.20260530' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta18.20260606' \
          or expid == 'n1850.ne30pg3_tn14.noresm3_0_beta18.egc_1p5.20260612' \
            \
          or expid == 'N1850.n30b23MM.i496.20260815' \
          or expid == 'N1850.n30b23MM.506.20260821' \
          or expid == 'N1850.MM.nor30b23.509.20260901' \
          or expid == 'N1850.MM.nor30b24.515.20260908' \
          or expid == 'N1850.MM.nor30b24.520.20260913' \
            \
          or expid == 'n1850GaxgGHG.LM.nor30b25.526.redout.20260928' \
          or expid == 'n1850GaxgGHG.LM.nor30b25.528.20260928' \
            \
          or expid == 'n1850esmGaxgGHG.LM.n30b25.20260928' \
          or expid == 'n1850esmGaxgGHG.LM.n30b25.529.20261002' \
            \
          or expid == 'n1850GHGGaxg.LM.nor30b27.002.20261016' \
          or expid == 'n1850esmGHGGaxg.LM.nor30b27.003.20261024' \
          or expid == 'n1850esmGHGGaxg.LM.nor30b27.001.20261016' \
            \
          or expid == 'n1850Gg.ne16pg3_tn14_gl4.noresm3_0_beta16.Run13.Olivia.2026-05-18_pseudo_hybrid' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14.Olivia.2026-05-28' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A.Olivia.2026-06-01' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A2.Olivia.2026-06-03' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-B.Olivia.2026-06-03' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-C.Olivia.2026-06-04' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-D.Olivia.2026-06-04' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F.Olivia.2026-06-05' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-G.Olivia.2026-06-06' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-H.Olivia.2026-06-08' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-I.Olivia.2026-06-08' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F_blom_cv_1p2.2026-06-12' \
            \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15.Olivia.2026-06-08' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-B.Olivia.2026-06-11' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-C.Olivia.2026-06-15' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-D.Olivia.2026-06-17' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-E.Olivia.2026-06-18' \
            \
          or expid == 'nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07' \
          or expid == 'n1850esm.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07' \
          or expid == 'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09' \
            \
          or expid == 'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_ksno04.Olivia.2026-06-23' \
          or expid == 'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_ksno02.Olivia.2026-06-23' \
          or expid == 'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnwfall100.Olivia.2026-06-23' \
          or expid == 'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnw075.Olivia.2026-06-23' \
          or expid == 'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnwfall300.Olivia.2026-06-23' \
          or expid == 'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_phiimushy45.Olivia.2026-06-23'
            \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta20.Run15-F.Olivia.2026-06-22' \
            \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta20.470.ref461.20260626' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta20.473.ref461.20260630' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta20.474.ref461.20260630' \
            \
          or expid == 'n1pctCO2.ne16pg3_tn14.beta20.2026-06-12' \
          or expid == 'n1pctCO2-RAD.ne16pg3_tn14.beta20.2026-06-24' \
            \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.476.2026-07-03' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.i478.2026-07-06' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.i480.2026-07-16' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260717' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.i482.2026-07-23' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260723' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.cmeps-latent-heat-bugfix.2026-07-23' \
          or expid == 'n1850.ne16pg3_tn14.noresm3_0_beta21.coare-const-i380.2026-07-27' \
            \
          or expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.i486.2026-07-31' \
          or expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2.20260730' \
          or expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.i489.2026-08-06' \
          or expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2_cplhist.20260806' \
          or expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2.20260811' \
          or expid=='n1850Gaxg.ne16pg3_tn14_ais8gris4.noresm3_0_beta22.492.ref490.20260811' \
            \
          or expid=='nhist.ne16pg3_tn14.noresm3_0_beta22.i491.2026-08-10' \
            \
          or expid=='n1850Gaxg.n30b23LM.498.20260815' \
          or expid=='n1850Gaxg.n30b23LM.502.20260818' \
            \
          or expid=='n1850.LM.n30b22.507.GAaxg.20260820' \
          or expid=='n1850.LM.n30b22.507.GAaxg_lnd_ic.20260820' \
          or expid=='n1850.LM.n30b23.507.GAaxg.20260820' \
          or expid=='n1850.LM.n30b23.507.GAaxg_lnd_ic.20260820' \
          or expid=='n1850.LM.n30b23.507.woGAaxg.20260820' \
          or expid=='n1850.LM.n30b23.507.woGAaxg_lnd_ic.20260820' \
            \
          or expid=='n1850esmGaxg.n30b23LM.XYZ.20260820' \
          or expid=='n1850esmGaxg.n30b23LM.508.20260824' \
            \
          or expid=='n1850Gaxg.LM.n30b24.511.betzy.20260904' \
          or expid=='n1850GaxgGHG.LM.n30b24.511.betzy.20260904' \
          or expid=='n1850Gaxg.LM.n30b24.516.20260909' \
          or expid=='n1850GaxgGHG.LM.n30b24.516.20260909' \
          or expid=='n1850GaxgGHG.LM.n30b24.517.20260911' \
          or expid=='n1850GaxgGHG.LM.n30b24.517.branch.20260913' \
          or expid=='n1850GaxgGHG.LM.nor30b24.525.20260923' \
            \
          or expid=='n1850GHG.MM.nor30b25.527.20260928' \
          or expid=='n1850GHG.MM.nor30b25.527.redout.20260929' \
           ) : componentlist=['masstrocn']; weightlist=[1.]
        else : componentlist=[var]; weightlist=[1.]            

    else : componentlist = [var] ; weightlist=[1.]
# 
# PRINT
#   print('getvarcomponents.py : componentlist = ', componentlist)
#
# CHECK LENGTH OF ARRAYS
    if ( len(componentlist) != len(weightlist) ) : 
        print('getvarcomponents : different size of arrays')
        quit()

    return componentlist, weightlist


def unravelvarcomponents(componentlist, weightlist, expid):
#-----------------------
    '''


    '''

    if ( len(componentlist) != len(weightlist) ) :
        print('+++ unravelvarcomponents +++')
        print('Different size for componentlist and weightlist : ', len(componentlist), len(weightlist))
        quit()    

    n = len(componentlist)

    newcomponentlist=[]
    newweightlist=[]

    for i in range(n) :

#       apply basic search on one element
        var=componentlist[i]
        weight=weightlist[i]

        tmpcomponentlist, tmpweightlist= getbasicvarcomponents(var=var, expid=expid)

#       apply multiplication of weights
        m = len(tmpweightlist)
        for j in range(m) :
            tmpweightlist[j] = tmpweightlist[j] * weight        

#       concatenate extended information
        newcomponentlist = newcomponentlist + tmpcomponentlist # concatenation of lists !
        newweightlist = newweightlist + tmpweightlist          # concatenation of lists !   

#       if list has grown : apply routine again        
        if ( newcomponentlist != componentlist ) : 
            newcomponentlist, newweightlist = unravelvarcomponents(componentlist=newcomponentlist, weightlist=newweightlist, expid=expid)

    return newcomponentlist, newweightlist



def getvarcomponents(var, expid=None):
#-------------------
    '''


    '''
    componentlist, weightlist=unravelvarcomponents(componentlist=[var], weightlist=[1.], expid=expid)

    return componentlist, weightlist
