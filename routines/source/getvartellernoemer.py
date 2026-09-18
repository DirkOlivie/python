def getvartellernoemer(var):
#---------------------------
    '''
    MODIFICATIONS
	(2022-03-17) creation

    '''

# default value
#   lifetime GAS PHASE
    if   ( var=='TAU_CHBR3' )               : des={'dofraction':1, 'teller':'cb_CHBR3', 'noemer':'SFCHBR3',  'f' :  365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU2_CHBR3' )              : des={'dofraction':1, 'teller':'cb_CHBR3', 'noemer':'GS_CHBR3', 'f' : -365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_CHBR3_from_jchbr3' )   : des={'dofraction':1, 'teller':'cb_CHBR3', 'noemer':'r_jchbr3_columnburden',    'f' :  365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_CHBR3_from_CHBR3_OH' ) : des={'dofraction':1, 'teller':'cb_CHBR3', 'noemer':'r_CHBR3_OH_columnburden',  'f' :  365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_DMS' )                 : des={'dofraction':1, 'teller':'cb_DMS'  , 'noemer':'SFDMS'  , 'f' : 365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_isoprene' )            : des={'dofraction':1, 'teller':'cb_isoprene'  , 'noemer':'SFisoprene'  , 'f' : 365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_monoterp' )            : des={'dofraction':1, 'teller':'cb_monoterp'  , 'noemer':'SFmonoterp'  , 'f' : 365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_SOA_SV' )              : des={'dofraction':1, 'teller':'cb_SOA_SV'  , 'noemer':'GS_SOA_SV', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1 
    elif ( var=='TAU_SOA_LV' )     : des={'dofraction':1, 'teller':'cb_SOA_LV'  , 'noemer':'GS_SOA_LV', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1

    elif ( var=='TAU2_CH4' )   : des={'dofraction':1, 'teller':'cb_CH4', 'noemer':'GS_CH4', 'f' : -1.0, 'newunits':'year'} # yr-1 -> yr-1
    elif ( var=='TAU2_N2O' )   : des={'dofraction':1, 'teller':'cb_N2O', 'noemer':'GS_N2O', 'f' : -1.0, 'newunits':'year'} # yr-1 -> yr-1
    elif ( var=='TAU2_OCS' )   : des={'dofraction':1, 'teller':'cb_OCS', 'noemer':'GS_OCS', 'f' : -1.0, 'newunits':'year'} # yr-1 -> yr-1
    elif ( var=='TAU2_SF6' )   : des={'dofraction':1, 'teller':'cb_SF6', 'noemer':'GS_SF6', 'f' : -1.0, 'newunits':'year'} # yr-1 -> yr-1
#
#   lifetime CH2O
    elif ( var=='TAU_CH2O' )    : des={'dofraction':1, 'teller':'cb_CH2O', 'noemer':'CHPEMI_CH2O_TOT_noresm2', 'f' : 365.25, 'newunits':'day'}    # Production-based 
    elif ( var=='TAU2_CH2O' )   : des={'dofraction':1, 'teller':'cb_CH2O', 'noemer':'CHLWETDRY_CH2O_TOT_noresm2', 'f' : 365.25, 'newunits':'day'} # Loss-based

#   lifetime CH4
    elif ( var=='TAU_CH4_OHTROP' ) : des={'dofraction':1, 'teller':'cb_CH4', 'noemer':'r_CH4_OH_columnburden_belowtropopause', 'f' : +1.0, 'newunits':'year'} # yr-1 -> yr-1   
    elif ( var=='TAU_CH4_CHMDRY' ) : des={'dofraction':1, 'teller':'cb_CH4', 'noemer':'CHMDRY_CH4_TOT_noresm2'               , 'f' : +1.0, 'newunits':'year'}
    elif ( var=='TAU_CH4_CHML'   ) : des={'dofraction':1, 'teller':'cb_CH4', 'noemer':'CH4_CHML_columnburden'                , 'f' : +1.0, 'newunits':'year'}
    elif ( var=='tau_ch4_oh'     ) : des={'dofraction':1, 'teller':'ch4_columnburden', 'noemer':'ch4lossoh_columnburden', 'f' : +1.0, 'newunits':'year'} # yr-1 -> yr-1  
    elif ( var=='tau_ch4_ohtrop' ) : des={'dofraction':1, 'teller':'ch4_columnburden', 'noemer':'ch4lossoh_columnburden_belowtropopause', 'f' : +1.0, 'newunits':'year'} # yr-1 -> yr-1  
    elif ( var=='tau_ch4_lossch4_trop' ) : des={'dofraction':1, 'teller':'ch4_columnburden', 'noemer':'lossch4_columnburden_belowtropopause', 'f' : +1.0, 'newunits':'year'} # yr-1 -> yr-1  
#
#   lifetime AEROSOL
#   noresm2
    elif ( var=='TAU_DUST_noresm2' )        : des={'dofraction':1, 'teller':'cb_DUST'    , 'noemer':'WETDRY_DUST_TOT_noresm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_SALT_noresm2' )       : des={'dofraction':1, 'teller':'cb_SALT'    , 'noemer':'WETDRY_SALT_TOT_noresm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_BC_noresm2' )         : des={'dofraction':1, 'teller':'cb_BC'      , 'noemer':'WETDRY_BC_TOT_noresm2'    , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_OM_noresm2' )         : des={'dofraction':1, 'teller':'cb_OM'      , 'noemer':'WETDRY_OM_SOA_TOT_noresm2', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1 
    elif ( var=='TAU_SULFATE_noresm2' )    : des={'dofraction':1, 'teller':'cb_SULFATE' , 'noemer':'WETDRY_SULFATE_TOT_noresm2','f':365.25, 'newunits':'day'} # yr-1 -> day-1

    elif ( var=='TAU_POA_noresm2' )        : des={'dofraction':1, 'teller':'cb_POA_noresm2', 'noemer':'WETDRY_POA_TOT_noresm2', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1 
    elif ( var=='TAU_SOA_noresm2' )        : des={'dofraction':1, 'teller':'cb_SOA_noresm2', 'noemer':'WETDRY_SOA_TOT_noresm2', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1 

    elif ( var=='TAUWET_DUST_noresm2' )    : des={'dofraction':1, 'teller':'cb_DUST'    , 'noemer':'WET_DUST_TOT_noresm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAUWET_SALT_noresm2' )    : des={'dofraction':1, 'teller':'cb_SALT'    , 'noemer':'WET_SALT_TOT_noresm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAUWET_BC_noresm2' )      : des={'dofraction':1, 'teller':'cb_BC'      , 'noemer':'WET_BC_TOT_noresm2'    , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAUWET_OM_noresm2' )      : des={'dofraction':1, 'teller':'cb_OM'      , 'noemer':'WET_OM_SOA_TOT_noresm2', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1 
    elif ( var=='TAUWET_SULFATE_noresm2' ) : des={'dofraction':1, 'teller':'cb_SULFATE' , 'noemer':'WET_SULFATE_TOT_noresm2','f':365.25, 'newunits':'day'} # yr-1 -> day-1

    elif ( var=='TAUDRY_DUST_noresm2' )    : des={'dofraction':1, 'teller':'cb_DUST'    , 'noemer':'DRY_DUST_TOT_noresm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAUDRY_SALT_noresm2' )    : des={'dofraction':1, 'teller':'cb_SALT'    , 'noemer':'DRY_SALT_TOT_noresm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAUDRY_BC_noresm2' )      : des={'dofraction':1, 'teller':'cb_BC'      , 'noemer':'DRY_BC_TOT_noresm2'    , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAUDRY_OM_noresm2' )      : des={'dofraction':1, 'teller':'cb_OM'      , 'noemer':'DRY_OM_SOA_TOT_noresm2', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1 
    elif ( var=='TAUDRY_SULFATE_noresm2' ) : des={'dofraction':1, 'teller':'cb_SULFATE' , 'noemer':'DRY_SULFATE_TOT_noresm2','f':365.25, 'newunits':'day'} # yr-1 -> day-1
#   noresm3
    elif ( var=='tau_BC_noresm3' )      : des={'dofraction':1, 'teller':'cb_BC'      , 'noemer':'wetdry_BC'     , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='tau_OM_noresm3' )      : des={'dofraction':1, 'teller':'cb_OM'      , 'noemer':'wetdry_OM'     , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='tau_SULFATE_noresm3' ) : des={'dofraction':1, 'teller':'cb_SULFATE' , 'noemer':'wetdry_SULFATE', 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='tau_DUST_noresm3' )    : des={'dofraction':1, 'teller':'cb_DUST'    , 'noemer':'wetdry_DUST'   , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='tau_SALT_noresm3' )    : des={'dofraction':1, 'teller':'cb_SALT'    , 'noemer':'wetdry_SALT'   , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1

#   lifetime AEROSOL CESM2/CESM3
    elif ( var=='TAU_dst_a123_cesm2' )        : des={'dofraction':1, 'teller':'dst_a123_columnburden'    , 'noemer':'WETDRY_dst_a123_TOT_cesm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_ncl_a123_cesm2' )        : des={'dofraction':1, 'teller':'ncl_a123_columnburden'    , 'noemer':'WETDRY_ncl_a123_TOT_cesm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_so4_a123_cesm2' )        : des={'dofraction':1, 'teller':'so4_a123_columnburden'    , 'noemer':'WETDRY_so4_a123_TOT_cesm2'  , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_pom_a14_cesm2'  )        : des={'dofraction':1, 'teller':'pom_a14_columnburden'     , 'noemer':'WETDRY_pom_a14_TOT_cesm2'   , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1
    elif ( var=='TAU_bc_a14_cesm2'  )         : des={'dofraction':1, 'teller':'bc_a14_columnburden'      , 'noemer':'WETDRY_bc_a14_TOT_cesm2'    , 'f':365.25, 'newunits':'day'} # yr-1 -> day-1

#   optical depth
    elif ( var == 'DOD550weightDAYFOC' )   : des={'dofraction':1, 'teller':'DOD550',   'noemer':'DAYFOC',  'f' : 1., 'newunits':''}
    elif ( var == 'AOD_VISweightDAYFOC' )  : des={'dofraction':1, 'teller':'AOD_VIS',  'noemer':'DAYFOC',  'f' : 1., 'newunits':''}
    elif ( var == 'AODVVOLCweightDAYFOC' ) : des={'dofraction':1, 'teller':'AODVVOLC', 'noemer':'DAYFOC',  'f' : 1., 'newunits':''}
    elif ( var == 'ABSVVOLCweightDAYFOC' ) : des={'dofraction':1, 'teller':'ABSVVOLC', 'noemer':'DAYFOC',  'f' : 1., 'newunits':''}
#   MODIS optical depth
    elif ( var == 'TAUWMODISweightCLWMODIS') : des={'dofraction':1, 'teller':'TAUWMODIS', 'noemer':'CLWMODIS',  'f' : 1., 'newunits':''}
    elif ( var == 'TAUIMODISweightCLIMODIS') : des={'dofraction':1, 'teller':'TAUIMODIS', 'noemer':'CLIMODIS',  'f' : 1., 'newunits':''}
    elif ( var == 'TAUTMODISweightCLTMODIS') : des={'dofraction':1, 'teller':'TAUTMODIS', 'noemer':'CLTMODIS',  'f' : 1., 'newunits':''}
#   else
    else                         : des={'dofraction':0, 'teller':var}
# 
    return des
