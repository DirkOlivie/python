import loopanalyseseries2

# MAIN PROGRAM
expidlist=['FCHIST_f09_mg17_20220111_test2', \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test3', \
           'FCHIST_f09_mg17_20220111_test4', \
           'FCHIST_f19_mg17_20220111_test5', \
            \
           'FCHIST_f09_f09_mg17_20211217_test01', \
           'FCHIST_f19_f19_mg17_20211217_test02', \
           'FCHIST_f19_f19_mg17_20211217_test03', \
            \
           'FCHIST_f09_f09_mg17_20220202_test01', \
           'FCHIST_f19_f19_mg17_20220202_test02'] 
#
legendlist=['CESM2 (1x1, NorESMhub)', \
            'CESM2 (2x2, NorESMhub)', \
            'CESM2 (2x2, no cam/src/NorESM)', \
            'CESM2 (1x1, no cam/src/NorESM)', \
            'CESM2 (2x2, NorESMhub, lightning)', \
             \
            'CESM2.1.3 (1x1)', \
            'CESM2.1.3 (2x2)', \
            'CESM2.1.3 (2x2, unscaled CESM2.1.0)', \
             \
            'CESM2.1.0 (1x1)', \
            'CESM2.1.0 (2x2)']
#
shiftlist=[-1849,-1849,-1849,-1849,-1849,-1849,-1849,-1849,-1849,-1849]
#
variablelist=['LNO_PROD_columnburden','LNO_COL_PROD', \
              'FSLNT', \
              'cb_isoprene','cb_monoterp','SFisoprene','SFmonoterp', \
              'TREFHT', \
              'OH_surfacelayer','O3_surfacelayer','NO3_surfacelayer','HO2_surfacelayer', \
              'SFDMS']
#variablelist=['EMI_SO2_TOT_noresm2','SFSO2']
#variablelist=['LNO_PROD_columnburden','LNO_COL_PROD']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst_cesm'
description='varcommon'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
