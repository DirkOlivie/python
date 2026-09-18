import numpy as np

def getlevels(var, units, spacing=''):
#------------    


    print('+++ getlevels +++')
    print('spacing = ' + spacing)
    print('var = ' + var)
    print('--- getlevels ---')


# default value
    gamma=1.

    if   ( var=='cb_O3'        and units=='DU'): levels=[150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450]
    elif ( var=='column_O3'    and units=='DU'): levels=[150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450]
    elif ( var=='column_ozone' and units=='DU'): levels=[150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450]
#
#   aerosol burden
    elif ( var=='cb_SOA_A1' ) : 
                                levels=levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*5.e-6
                                if ( spacing=='xdiff' ) : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-6; gamma=1.

#
#   volcanic extinction
    elif ( var == 'BVISVOLC' \
        or var == 'ext' \
        or var == 'ext_sun' \
        or var == 'ext_earth' ) : levels = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.])*1.e-4 ; gamma=1

#   aerosol optical depth
    elif ( var == 'AOD_VIS' \
        or var == 'AODVIS' \
        or var == 'D550_SO4' \
        or var == 'column_EXT_MODE01_AeroTab_NCONC' \
        or var == 'column_EXT_MODE01_AeroTab_NCONC_RELHUM' \
        or var == 'column_EXT_MODE01_AeroTab_NCONC_SPEHUM' \
        or var == 'column_EXT_MODE05_AeroTab_NCONC' \
        or var == 'column_EXT_MODE05_AeroTab_NCONC_RELHUM' \
        or var == 'column_EXT_MODE05_AeroTab_NCONC_SPEHUM') : 
#                                                             levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.]) * 1.e-2 ; gamma=0.2
                                                             levels=np.array([1.,2.,5.,10.,20.,50.,100.]) * 1.e-2 ; gamma=0.2
#                                                             levels=np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]) * 1.e-1 ; gamma=1.
                                                             if ( spacing=='xdiff') : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*0.05 ; gamma=1.   
#
#   aerosol number concentration (column integrated)
    elif ( var == 'column_NCONC01' \
        or var == 'column_NCONC02' \
        or var == 'column_NCONC03' \
        or var == 'column_NCONC04' \
        or var == 'column_NCONC05' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.]) *1.e10 ; gamma=0.2
#
#   aerosol volume concentration (column integrated)
    elif ( var == 'column_VCONC01' \
        or var == 'column_VCONC02' \
        or var == 'column_VCONC03' \
        or var == 'column_VCONC04' \
        or var == 'column_VCONC05' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.]) *1.e-11 ; gamma=0.2
#
#   aerosol number concentration (column integrated)
    elif ( var == 'NCONC01' \
        or var == 'NCONC02' \
        or var == 'NCONC03' \
        or var == 'NCONC04' \
        or var == 'NCONC05' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.]) *1.e3 ; gamma=0.2
#
#   aerosol volume concentration (column integrated)
    elif ( var == 'VCONC01' \
        or var == 'VCONC02' \
        or var == 'VCONC03' \
        or var == 'VCONC04' \
        or var == 'VCONC05' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.]) *1.e-15 ; gamma=0.2
#
#   aerosol surface area
    elif (var == 'SAD_AERO' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-12 ; gamma=0.2
    elif (var == 'SAD_ICE' )  : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-12 ; gamma=0.2
    elif (var == 'SAD_LNAT' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-12 ; gamma=0.2
    elif (var == 'SAD_SULFC' ): levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-12 ; gamma=0.2
    elif (var == 'SAD_TROP' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-12 ; gamma=0.2

    elif (var == 'REFF_AERO' ): levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-8 ; gamma=0.2
    elif (var == 'REFF_AERO' ): levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.])*1.e-6 

    elif (var == 'H2SO4M_C' ): levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-8 ; gamma=0.2
    elif (var == 'H2SO4' )   : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-16 ; gamma=0.2
#
#   precipitation
    elif (var == 'PRECT' ) : 
                              if ( spacing=='xdiff' ) : levels=np.array([-2.4,-2.0,-1.6,-1.2,-0.8,-0.4,0.,0.4,0.8,1.2,1.6,2.0,2.4]) ; gamma=1.
                              else                    : levels=np.array([0.,2.,4.,6.,8.,10.,12.,14.]) ; gamma=1.   
#   cloud droplet number (column integrated)
    elif (var == 'CDNUMC' ) : 
                              if ( spacing=='xdiff' ) : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e10; gamma=1.
                              elif ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e8 ; gamma=0.2   
#
#   CCN1, CCN2, ...
    elif (var == 'column_N_AER') : levels=np.array([0.,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2])*1.e13 ; gamma=1.
#
#   emissions
    elif ( var=='EMI_DUST_TOT_noresm2' \
        or var=='SFdst_a123') :
#                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])/10.*1.e-7 ; gamma=1.
#                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])/1000.*1.e-7 ; gamma=0.2
                                                            levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])/1000.*1.e-7 ; gamma=0.2

    elif ( var=='EMI_BC_TOT_noresm2' ) :
                                 levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-16; gamma=0.2

    elif ( var=='EMI_OM_TOT_noresm2' \
        or var=='EMI_SO2SO4_as_SO2_TOT_noresm2' ) :
                                 levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15; gamma=0.2


#   3D concentrations
    elif ( var=='SO2_as_concentration' )   : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*2.e-10 ; gamma=1.
    elif ( var=='mmr_SULFATE_as_concentration' )   : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*2.e-9 ; gamma=1.


#   3D mixing ratios
    elif ( var=='CO' )    : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-8
    elif ( var=='SOA_SV' or \
           var=='SOA_LV' ) : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-14 ; gamma=0.2
    elif ( var=='NO2' ) : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-11 ; gamma=0.2
    elif ( var=='N2O5' ) : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.])*1.e-13 ; gamma=0.2
    elif ( var=='OCS' ) : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.])*1.e-15 ; gamma=0.2
    elif ( var=='SO2' )   : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.])*1.e-12 ; gamma=0.2
    elif ( var=='NH3' )   : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.])*1.e-12 ; gamma=0.2
    elif ( var=='NH4' )   : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.])*1.e-12 ; gamma=0.2
    elif ( var=='HO2' )   :
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15 ; gamma=0.2
    elif ( var=='OH' \
        or var=='OH_bef' \
        or var=='OH_aft' ) :
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15 ; gamma=0.2
    elif ( var=='NO3' \
        or var=='NO3_bef' \
        or var=='NO3_aft' ) :
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15 ; gamma=0.2
    elif ( var=='O1D' )   : 
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.,1000000.,2000000.,5000000.,10000000.,20000000.,50000000.,100000000.,200000000.,500000000.])*1.e-23 ; gamma=0.2

    elif ( var=='CH4' )   : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-7*2.

    elif ( var=='O3' \
        or var=='ozone' )    :
                            if ( spacing=='xdiff' ) : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-7 ; gamma=1.
                            else                    : levels=np.array([0.,0.1,0.2,0.4,0.5,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-6                                           ; gamma=1.
#                            if ( spacing =='')            : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-6                                           ; gamma=1.
#                            elif ( spacing=='non-linear') : levels=np.array([10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,200.,500.,1000.,2000.,5000.,10000.])*1.e-9 ; gamma=0.2
    elif ( var=='BRY' \
        or var=='BRY_SUM' \
        or var=='BRY_SCALED' ) : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*2*1.e-12
    elif ( var=='CLY' \
        or var=='CLY_SUM' \
        or var=='CLY_SCALED') : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.])*1.e-10
#
    elif ( var=='so4_a123' \
        or var=='mmr_SULFATE' \
        or var=='so4_a1' or var=='so4_a2' or var=='so4_a3' \
        or var=='soa_a1' or var=='soa_a2' \
        or var=='SO4_A1' or var=='SO4_A2' or var=='SO4_NA' or var=='SO4_PR' or var=='SO4_AC' \
        or var=='bc_a1' ) :
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-9 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.])*1.e-12 ; gamma=0.2
                             if ( spacing=='xdiff' )     : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-7; gamma=1.
#
#   radius
    elif ( var=='NMR01'     or var=='NMR05' \
        or var=='dgnum1'    or var=='dgnum2'    or var=='dgnum3'    or var=='dgnum4' \
        or var=='dgnumwet1' or var=='dgnumwet2' or var=='dgnumwet3' or var=='dgnumwet4' \
        or var=='rgnum1'    or var=='rgnum2'    or var=='rgnum3'    or var=='rgnum4' \
        or var=='rgnumwet1' or var=='rgnumwet2' or var=='rgnumwet3' or var=='rgnumwet4' ) :
                                                            levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.])*1.e-8 ; gamma=1.
#                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-8 ; gamma=1.
#                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.])*1.e-12 ; gamma=0.2
                             

    elif ( var=='BC_AC_OCWclcoagTend') :
                              if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                              if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-17 ; gamma=0.2


#   surface concentrations
    elif ( ( var=='O3_SRF' or var=='O3_surfacelayer' ) and units=='mol mol-1')  : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-9
    elif ( ( var=='O3_SRF' \
          or var=='O3_surfacelayer' \
          or var=='vmro3_1000hPa' \
          or var=='vmro3_925hPa' \
          or var=='vmro3_850hPa' \
          or var=='vmro3_800hPa' \
          or var=='vmro3_700hPa' \
          or var=='vmro3_600hPa' \
          or var=='vmro3_500hPa' ) and units=='ppb')  : levels=np.array([0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.,85.,90.,95.,100.])
    elif ( var=='NO3_SRF' \
        or var=='NO3_surfacelayer' \
        or var=='NO3_bef_surfacelayer' \
        or var=='NO3_aft_surfacelayer' ) :
                              if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                              if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-17 ; gamma=0.2
    elif ( var=='OH_SRF'\
        or var=='OH_surfacelayer' \
        or var=='OH_bef_surfacelayer' \
        or var=='OH_aft_surfacelayer' )   :
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-18 ; gamma=0.2
    elif ( var=='HO2_SRF' \
        or var=='HO2_surfacelayer' ) :
                             if ( spacing=='')           : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-12 ; gamma=1.
                             if ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-16 ; gamma=0.2
    elif ( var=='CO_SRF' )  : 
                              if ( spacing=='')             : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-8 ; gamma=1.
                              elif ( spacing=='non-linear') : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-8   ; gamma=0.2
    elif ( var=='NO_SRF' ) : 
                              if ( spacing=='')             : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-11 ; gamma=1.
                              elif (spacing=='non-linear' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-11   ; gamma=0.2   

    elif ( var=='NO2_SRF' ) : 
                              if ( spacing=='')             : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-11 ; gamma=1.
                              elif (spacing=='non-linear' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-11   ; gamma=0.2   

    elif ( var=='SO2_SRF' ) : 
                              if ( spacing=='')             : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-12 ; gamma=1.
                              elif (spacing=='non-linear' ) : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-12   ; gamma=0.2
#
#   surface emissions
    elif ( var=='SFDMS' )  :
                              if ( spacing=='' ) : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.])*1.e-13 ; gamma=1.
                              if ( spacing=='non-linear' ) : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.])*1.e-13 ; gamma=1.
                              if ( spacing=='xdiff' ) : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*2.e-13; gamma=1.                              
                              if ( spacing=='xdiff-non-linear' ) : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*2.e-13; gamma=1.                              
    elif ( var=='SFCHBR3' )  :
                                                                    levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-15 ; gamma=1.
    elif ( var=='SFisoprene' or var=='MEG_isoprene' )  :
                              if ( spacing=='')                   : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-15 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15   ; gamma=0.2
                              elif ( spacing=='xdiff' )           : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-11; gamma=1.
                              elif ( spacing=='xdiff-non-linear') : levels=np.array([-1000.,-500.,-200.,-100.,-50.,-20.,-10.,-5.,-2.,-1.,1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-12 ; gamma=1. 
    elif ( var=='SFmonoterp' )  :
                              if ( spacing=='')                   : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-15 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15   ; gamma=0.2 
                              elif ( spacing=='xdiff' )           : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-11; gamma=1.
                              elif ( spacing=='xdiff-non-linear') : levels=np.array([-1000.,-500.,-200.,-100.,-50.,-20.,-10.,-5.,-2.,-1.,1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-12 ; gamma=1.
    elif ( var=='emich4land' or var=='FCH4' ) :
                              if ( spacing=='')                   : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*2.e-11 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-14   ; gamma=0.2
#
#   CLM variables
    elif ( var=='FSNO' )  :
                              if ( spacing=='')             : levels=np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]) ; gamma=1.
                              elif ( spacing=='xdiff')      : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*0.2 ; gamma=1.
    elif ( var=='TLAI' )  :
                              if ( spacing=='')             : levels=np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*5. ; gamma=1.
                              elif ( spacing=='xdiff')      : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*2. ; gamma=1.
    elif ( var=='TSA' )  :
                              if ( spacing=='')             : levels=np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*5. ; gamma=1.
                              elif ( spacing=='xdiff')      : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*5. ; gamma=1.
    elif ( var=='NPP' )  :
                              if ( spacing=='')                   : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-15 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15   ; gamma=0.2
                              elif ( spacing=='xdiff' )           : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e-6; gamma=1.
                              elif ( spacing=='xdiff-non-linear') : levels=np.array([-1000.,-500.,-200.,-100.,-50.,-20.,-10.,-5.,-2.,-1.,1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-12 ; gamma=1.
    elif ( var=='SOILWATER_10CM' )  :
                              if ( spacing=='')                   : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])*1.e-15 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-15   ; gamma=0.2
                              elif ( spacing=='xdiff' )           : levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*2.; gamma=1.
                              elif ( spacing=='xdiff-non-linear') : levels=np.array([-1000.,-500.,-200.,-100.,-50.,-20.,-10.,-5.,-2.,-1.,1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.])*1.e-12 ; gamma=1.
#
#   SPAERO ERF
    elif ( var=='FSNT_SP2_minus_FSNT_SP' ) : levels=np.array([-5.,-2.,-1.,-0.5,-0.25,-0.125,0.,0.125,0.25,0.5,1.,2.,5.]) ; gamma=1
    elif ( var=='FSNT_SP3_minus_FSNT_SP2' \
        or var=='FSNT_SP3_minus_FSNT_SP'  \
        or var=='FSNS_SP2_minus_FSNS_SP'  \
        or var=='FSNS_SP3_minus_FSNS_SP2' \
        or var=='FSNS_SP3_minus_FSNS_SP' ) : levels=np.array([-20.,-10.,-5.,-3.,-1.,-0.5,0.,0.5,1.,3.,5.,10.,20.]) ; gamma=1            
#
    elif ( var=='FSLNT' \
        or var=='FSLNTC' \
        or var=='FSDS' \
        or var=='FSDSC' \
        or var=='direct_ERF_noresm2' \
        or var=='cloud_ERF_noresm2' \
        or var=='surfalb_ERF_noresm2' ) : 
                        levels=np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*0.1; gamma=1.
                        levels=np.array([-15.,-12.,-9.,-6.,-3.,0.,3.,6.,9.,12.,15.])/3.; gamma=1.
#    elif ( var=='FSLNT' ) : levels=np.array([-20.,-15.,-10.,-6.,-3.,-1.,1.,3.,6.,10.,15.,20.]); gamma=1.
#
#   PHOTOLYSIS RATES
    elif ( var=='jchbr3' )  : levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.])*1.e-8 ; gamma=0.2

#   METEOROLOGICAL VALUES
    elif ( var=='T' or 
           var=='TREFHT' or 
           var=='TREFMXAV' or 
           var=='TREFMNAV' ) : 
                              if ( spacing=='')                   : levels=np.array([-90.,-80.,-70.,-60.,-50.,-40.,-30.,-20.,-10.,0.,10.,20.,30.]) ; gamma=1.
#                             elif ( spacing=='xdiff')            : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*5. ; gamma=1. 
                              elif ( spacing=='xdiff')            : levels=np.array([-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.]) ; gamma=1. 
                              elif ( spacing=='non-linear')       : levels=np.array([-90.,-80.,-70.,-60.,-50.,-40.,-30.,-20.,-10.,0.,10.,20.,30.]) ; gamma=1. 
    elif ( var=='TREFMXMNAV' or
           var=='tasmaxmin' ) : levels = np.array([-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.]) ; gamma=1
    elif ( var=='SWCF' ) :    
                              if ( spacing=='')             : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.]) ; gamma=1.
                              elif ( spacing=='xdiff')      : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*2. ; gamma=1. 

    elif ( var=='CLOUD' \
        or var=='CLOUDCOVER_CLUBB' \
        or var=='CLOUDFRAC_CLUBB' \
        or var=='CONCLD' \
        or var=='CLDTOT' \
        or var=='CLDHGH' \
        or var=='CLDMED' \
        or var=='CLDLOW' ) :    
                              if ( spacing=='')             : levels=np.array([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.]) * 0.01 ; gamma=1.
                              elif ( spacing=='xdiff')      : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*0.05 ; gamma=1.
    elif ( var=='U10' ) : levels = np.array([0.,2.,4.,6.,8.,10.,12.,14.]) ; gamma=1

    elif ( var=='PHIS' ) : 
                           if ( spacing=='' \
                             or spacing=='non-linear')   : levels=np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.]) * 5000 ; gamma=1.
                           elif ( spacing=='xdiff')      : levels=np.array([-1.5,-1.4,-1.3,-1.2,-1.1,-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5])*3000 ; gamma=1.


#   OCEAN VALUES 
    elif ( var=='SST' or
           var=='sst' ) :
                              if ( spacing=='')                   : levels=np.array([-5.,0.,5.,10.,15.,20.,25.,30.,35.]) ; gamma=1.
#                             elif ( spacing=='xdiff')            : levels=np.array([-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])*5. ; gamma=1. 
                              elif ( spacing=='xdiff')            : levels=np.array([-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.]) * 0.5 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([-90.,-80.,-70.,-60.,-50.,-40.,-30.,-20.,-10.,0.,10.,20.,30.]) ; gamma=1.

    elif ( var=='oceanheat_columnburden' ) :
                              if ( spacing=='')                   : levels=np.array([-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])*1.e+13 ; gamma=1.
                              elif ( spacing=='xdiff')            : levels=np.array([-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.]) * 0.25 * 1.e+13 ; gamma=1.
                              elif ( spacing=='non-linear')       : levels=np.array([-90.,-80.,-70.,-60.,-50.,-40.,-30.,-20.,-10.,0.,10.,20.,30.]) ; gamma=1.

#
    elif ( 'emiss' in var ) :
#            levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-17; gamma=0.2
            levels=np.array([1.,2.,5.,10.,20.,50.,100.,200.,500.,1000.,2000.,5000.,10000.,20000.,50000.,100000.,200000.,500000.])*1.e-10; gamma=0.2
            
    else : 
        levels = [0,1,2,3,4,5,6,7,8,9,10]
#       levels = np.array([-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.]) ; gamma=1
        levels = np.array([-10.,-9.,-8.,-7.,-6.,-5.,-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]) ; gamma=1

    print('+++ getlevels +++')
    print(var)
    print(spacing)
    print(levels)

    return levels, gamma


