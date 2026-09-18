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

if ( True ) :
    directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260820/individual/CMIP/1.9x2.5'

    filenamelist=[ \
            'emissions_cmip7_noresm3_S_volcstratclimALL_vertical_1850_1.9x2.5_UOEXETER-CMIP-2-2-1_version20260820']

    analyseseriesnoresmemissionsloop2.analyseseriesnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,freqtype=freqtype)

