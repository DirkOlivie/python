import analysemapnoresmemissionsloop2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

'''
    REAMRK !!!!!!
        No '.nc' at the end of the file

    CALLS
        analysenoresmemissionsloop2

'''

def main():
#----------
#
    plotdir='/scratch/olivie/code/python/cmip7-emissions-noresm/data/output'
#
    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed', plotdir=plotdir)
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free', plotdir=plotdir)
    figlayoutlist=[figlayout0,figlayout1]
#
#   CMIP7 emissions
    if ( False ) :
#
        directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260105/individual/hist'
#
        gridlist=['ne16pg3','1.9x2.5','ne30pg3','0.9x1.25']
        code='trial'

        periodlist=['2000-2023-YEA']

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

            analysemapnoresmemissionsloop2.analysemapnoresmemissionsloop2(directory=directory+'/'+grid,filenamelist=filenamelist,periodlist=periodlist, figlayoutlist=figlayoutlist, code=code)
#
#   Stratospheric volcanic emissions
    if ( True ) :
#
        directory='/scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260820/individual/CMIP/1.9x2.5'
#    
        code='trial'

        periodlist=['1850-1850-YEA']

        filenamelist=[ \
            'emissions_cmip7_noresm3_S_volcstratclimALL_vertical_1850_1.9x2.5_UOEXETER-CMIP-2-2-1_version20260820']

        analysemapnoresmemissionsloop2.analysemapnoresmemissionsloop2(directory=directory,filenamelist=filenamelist,periodlist=periodlist, figlayoutlist=figlayoutlist, code=code)

if __name__ == '__main__':
    main()
