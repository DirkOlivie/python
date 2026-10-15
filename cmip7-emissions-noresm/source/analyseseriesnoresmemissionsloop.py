import analyseseriesnoresmemissionsloop2
'''
    REAMRK !!!!!!
        No '.nc' at the end of the file

    CALLS
        analysenoresmemissionsloop2

'''
freqtype='YEA'


if ( False ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260105/individual/hist'

    gridlist=['1.9x2.5','ne16pg3']
#   gridlist=['0.9x1.25','ne30pg3']

    for grid in gridlist :

        filenamelist=[ \
              'emissions_cmip7_noresm3_BC_AX_airALL_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_BC_AX_anthroprofENEIND_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_BC_AX_anthrosurfAGRTRADOMSOLWSTSHP_surface_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_BC_N_airALL_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_BC_N_anthroprofENEIND_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_BC_N_anthrosurfAGRTRADOMSOLWSTSHP_surface_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_BC_NI_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1849-2025_'+grid+'_DRES-CMIP-BB4CMIP7-2-0_version20260105', \
              'emissions_cmip7_noresm3_OM_NI_airALL_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_OM_NI_anthroprofENEIND_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_OM_NI_anthrosurfAGRTRADOMSOLWSTSHP_surface_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_OM_NI_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1849-2025_'+grid+'_DRES-CMIP-BB4CMIP7-2-0_version20260105', \
              'emissions_cmip7_noresm3_SO2_airALL_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_SO2_anthroprofENEIND_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_SO2_anthrosurfAGRTRADOMSOLWSTSHP_surface_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_SO2_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1849-2025_'+grid+'_DRES-CMIP-BB4CMIP7-2-0_version20260105', \
              'emissions_cmip7_noresm3_SO2_volcCONTEXPL_vertical_1849-2025_'+grid+'_AeroCom2006_version20260105', \
              'emissions_cmip7_noresm3_SO4_PR_airALL_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_SO4_PR_anthroprofENEIND_vertical_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_SO4_PR_anthrosurfAGRTRADOMSOLWSTSHP_surface_1849-2025_'+grid+'_CEDS-CMIP-2025-04-18_version20260105', \
              'emissions_cmip7_noresm3_SO4_PR_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1849-2025_'+grid+'_DRES-CMIP-BB4CMIP7-2-0_version20260105', \
              'emissions_cmip7_noresm3_SO4_PR_volcCONTEXPL_vertical_1849-2025_'+grid+'_AeroCom2006_version20260105']

        analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory+'/'+grid,filenamelist=filenamelist,freqtype=freqtype)


if ( False ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20250620/individual/hist'

    filenamelist=[ \
            'emissions_cmip7_noresm3_BC_AX_airALL_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_BC_AX_anthroprofENEIND_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_BC_AX_anthrosurfAGRTRADOMSOLWSTSHP_surface_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_BC_N_airALL_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_BC_N_anthroprofENEIND_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_BC_N_anthrosurfAGRTRADOMSOLWSTSHP_surface_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_BC_NI_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_OM_NI_airALL_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_OM_NI_anthroprofENEIND_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_OM_NI_anthrosurfAGRTRADOMSOLWSTSHP_surface_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_OM_NI_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO2_airALL_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO2_anthroprofENEIND_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO2_anthrosurfAGRTRADOMSOLWSTSHP_surface_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO2_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO2_volcCONTEXPL_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO4_PR_airALL_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO4_PR_anthroprofENEIND_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO4_PR_anthrosurfAGRTRADOMSOLWSTSHP_surface_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO4_PR_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1995-2025_1.9x2.5_version20250620', \
            'emissions_cmip7_noresm3_SO4_PR_volcCONTEXPL_vertical_1995-2025_1.9x2.5_version20250620']

    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)


if ( False ) :
    directory='/scratch/olivie/noresm-inputdata/atm/cam/chem/emis/cmip6_emissions_version20180512'

    filenamelist=[ \
            'emissions_cmip6_noresm2_BC_AX_airALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_BC_AX_anthroprofALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_BC_AX_anthrosurfALL_surface_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_BC_N_airALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_BC_N_anthroprofALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_BC_N_anthrosurfALL_surface_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_BC_NI_bbALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_OM_NI_airALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_OM_NI_anthroprofALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_OM_NI_anthrosurfALL_surface_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_OM_NI_bbALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO2_airALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO2_anthroprofALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO2_anthrosurfALL_surface_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO2_bbALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO2_volcALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO4_PR_airALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO4_PR_anthroprofALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO4_PR_anthrosurfALL_surface_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO4_PR_bbALL_vertical_1849-2015_1.9x2.5_version20180512', \
            'emissions_cmip6_noresm2_SO4_PR_volcALL_vertical_1849-2015_1.9x2.5_version20180512']

    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)

#   HYway
if ( False ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260207/individual/hist/1.9x2.5'

    filenamelist=[ \
            'emissions_hyway_noresm2_H2_anthrosurfALL_surface_1849-2020_1.9x2.5_GFDL_version20260207', \
            'emissions_hyway_noresm2_H2_oceanALL_surface_1849-2020_1.9x2.5_GFDL_version20260207', \
            'emissions_hyway_noresm2_H2_soilALL_surface_1849-2020_1.9x2.5_GFDL_version20260207', \
             \
            'emissions_ceds_v2021_04_21_noresm2_H2_bbsurfALL_surface_1997-2020_1.9x2.5_version20250313']

    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)

if ( False ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260820/individual/CMIP/1.9x2.5'

    filenamelist=[ \
            'emissions_cmip7_noresm3_S_volcstratclimALL_vertical_1850_1.9x2.5_UOEXETER-CMIP-2-2-1_version20260820']

    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)

if ( False ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260927/individual/histclimo/1.9x2.5'

    filenamelist=[
            'emissions_cmip7_noresm3_BC_airALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BC_anthroprofALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BC_anthrosurfALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BC_bbALL_vertical_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_BENZENE_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BENZENE_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_BIGALK_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BIGALK_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_BIGENE_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BIGENE_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H2_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H2_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H4_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H4_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H5OH_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H5OH_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H6_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H6_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C3H6_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C3H6_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C3H8_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C3H8_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH2O_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH2O_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3CHO_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3CHO_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3CN_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3CN_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3COCH3_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3COCH3_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3COCHO_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3COOH_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3COOH_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3OH_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3OH_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CO_airALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CO_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CO_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_DMS_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_GLYALD_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_H2_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_HCN_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_HCN_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_HCOOH_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_HCOOH_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_ISOP_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_MEK_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_MEK_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_MTERP_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_NH3_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_NH3_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_NO2_airALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_NO_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_NO_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_OC_airALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_OC_anthroprofALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_OC_anthrosurfALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_OC_bbALL_vertical_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_S_airALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_S_anthroprofALL_vertical_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_S_anthrosurfALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_S_bbALL_vertical_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_S_volcALL_vertical_histclimo_1850-2023_1.9x2.5_Aerocom2006_version20260927', \
            'emissions_cmip7_noresm3_S_volcstratclim1850-2021ALL_vertical_histclimo_1850-2023_1.9x2.5_UOEXETER-CMIP-2-2-1_version20260927', \
            'emissions_cmip7_noresm3_TOLUENE_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_TOLUENE_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_XYLENES_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_XYLENES_bbsurfALL_surface_histclimo_1850-2023_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927']


    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)

if ( True ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260927/individual/historical/1.9x2.5'

    filenamelist=[
            'emissions_cmip7_noresm3_BC_airALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BC_anthroprofALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BC_anthrosurfALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BC_bbALL_vertical_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_BENZENE_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BENZENE_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_BIGALK_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BIGALK_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_BIGENE_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_BIGENE_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H2_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H2_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H4_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H4_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H5OH_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H5OH_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C2H6_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C2H6_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C3H6_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C3H6_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_C3H8_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_C3H8_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH2O_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH2O_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3CHO_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3CHO_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3CN_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3CN_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3COCH3_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3COCH3_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3COCHO_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3COOH_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3COOH_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CH3OH_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CH3OH_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_CO_airALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CO_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_CO_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_DMS_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_GLYALD_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_H2_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_HCN_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_HCN_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_HCOOH_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_HCOOH_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_ISOP_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_MEK_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_MEK_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_MTERP_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_NH3_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_NH3_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_NO2_airALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_NO_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_NO_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_OC_airALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_OC_anthroprofALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_OC_anthrosurfALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_OC_bbALL_vertical_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_S_airALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_S_anthroprofALL_vertical_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_S_anthrosurfALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_S_bbALL_vertical_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_S_volcALL_vertical_historical_1998-2002_1.9x2.5_Aerocom2006_version20260927', \
            'emissions_cmip7_noresm3_TOLUENE_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_TOLUENE_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927', \
            'emissions_cmip7_noresm3_XYLENES_anthrosurfgasALL_surface_historical_1998-2002_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927', \
            'emissions_cmip7_noresm3_XYLENES_bbsurfALL_surface_historical_1998-2002_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260927']

    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)
