import loopanalyseseries2

# MAIN PROGRAM

expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test11', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test12']
legendlist=['NorESM2', \
            'NorESM2 (no strat. SO2)', \
            'NorESM2 (no strat. OCS)']
shiftlist=[0,0,0]
#
variablelist=['CDNUMC','N_AER']

#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst'
description='varcommon'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


expidlist=['NF1850norbc_f19_20191025len30', \
           'NF1850frc2norbc_f09_20200108', \
           'NF1850norbc_tropstratchem_f19_20220105_test01', \
           'NF1850norbc_tropstratchem_f09_20220105_test02', \
           'NF1850norbc_tropstratchem_f19_20220105_test03', \
           'NF1850norbc_tropstratchem_f19_20220105_test05', \
           'NF1850norbc_tropstratchem_f19_20220105_test06', \
           'NF1850norbc_tropstratchem_f09_20220105_test07', \
           'FCHIST_f09_f09_mg17_20211217_test01', \
           'FCHIST_f19_f19_mg17_20211217_test02', \
           'FCHIST_f19_f19_mg17_20211217_test03', \
           'FCHIST_f09_mg17_20220111_test2', \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_f19_mg17_20220202_test02'] 

legendlist=['NorESM2 (OsloAero, 2x2)', \
            'NorESM2 (OsloAero, 1x1)', \
            'NorESM2 (full chem. 1)', \
            'NorESM2 (full chem. 2, 1x1)', \
            'NorESM2 (full chem. 3)', \
            'NorESM2 (full chem. 5)', \
            'NorESM2 (full chem. 6)', \
            'NorESM2 (full chem. 7, 1x1)', \
            'CESM2 (historical, 1x1, CESM2.1.3)', \
            'CESM2 (historical, CESM2.1.3)', \
            'CESM2 (historical, CESM2.1.3, old)', \
            'CESM2 (historical, 1x1)', \
            'CESM2 (historical)', \
            'CESM2 (historical, CESM2.1.0)']
shiftlist=[0,0,0,0,0,0,0,0,-1849,-1849,-1849,-1849,-1849,-1849]
#
variablelist=['FSLNT', \
              'cb_isoprene','cb_monoterp','SFisoprene','SFmonoterp', \
              'TREFHT', \
              'OH_surfacelayer','O3_surfacelayer','NO3_surfacelayer','HO2_surfacelayer', \
              'SFDMS']
variablelist=['EMI_SO2_TOT_noresm2','SFSO2']
#variablelist=['FSNT','FLNT']
#variablelist=['SFDMS']
#variablelist=['FSLNT']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst'
description='varcommon'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

expidlist=['NF1850norbc_tropstratchem_f19_20220105_test05', \
           'NF1850norbc_tropstratchem_f19_20220105_test06', \
           'NF1850norbc_tropstratchem_f09_20220105_test07', \
           'FCHIST_f09_f09_mg17_20211217_test01', \
           'FCHIST_f19_f19_mg17_20211217_test02', \
           'FCHIST_f19_f19_mg17_20211217_test03', \
           'FCHIST_f09_mg17_20220111_test2', \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_f19_mg17_20220202_test02']
           

legendlist=['NorESM2 (full chem. 5)', \
            'NorESM2 (full chem. 6)', \
            'NorESM2 (full chem. 7, 1x1)', \
            'CESM2 (historical, 1x1, CESM2.1.3)', \
            'CESM2 (historical, CESM2.1.3)', \
            'CESM2 (historical, CESM2.1.3, old)', \
            'CESM2 (historical, 1x1)', \
            'CESM2 (historical)', \
            'CESM2 (historical, CESM2.1.0)']
shiftlist=[0,0,0,-1849,-1849,-1849,-1849,-1849,-1849]
#
variablelist=['LNO_PROD_columnburden','LNO_COL_PROD']
#variablelist=['FSNT','FLNT']
#variablelist=['SFDMS']
#variablelist=['FSLNT']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst'
description='varcommon'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


expidlist=['NF1850norbc_f19_20191025len30', \
           'NF1850frc2norbc_f09_20200108', \
           'NF1850norbc_tropstratchem_f19_20220105_test01', \
           'NF1850norbc_tropstratchem_f09_20220105_test02', \
           'NF1850norbc_tropstratchem_f19_20220105_test03', \
           'NF1850norbc_tropstratchem_f19_20220105_test05']
legendlist=['NorESM2 (OsloAero, 2x2)', \
            'NorESM2 (OsloAero, 1x1)', \
            'NorESM2 (full chem. 1)', \
            'NorESM2 (full chem. 2)', \
            'NorESM2 (full chem. 3)', \
            'NorESM2 (full chem. 5)']
shiftlist=[0,0,0,0,0,0]
#
variablelist=['AODVVOLCdivDAYFOC','ABSVVOLCdivDAYFOC',
              'cb_SULFATE','cb_DUST','cb_SALT','cb_OM','cb_BC','cb_DMS', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'cb_O3']
#variablelist=['FSNT','FLNT']
#variablelist=['SFDMS']
#variablelist=['FSLNT']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst'
description='varcommon'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


expidlist=['FC2010climo_prep_f19_20210204_test5', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
           'NF1850norbc_tropstratchem_f19_20220105_test01']
#          'NF1850norbc_f19_20191025len30']  
legendlist=['CESM2 (full chem 2010)', \
            'NorESM2 (full chem 2010)', \
            'NorESM2 (full chem 1850)']
#           'NorESM2 (1850)'  ]
shiftlist=[0,0,0]#,0]
#
variablelist=['SFisoprene','SFmonoterp','cb_isoprene','cb_monoterp']
variablelist=['OH_SRF','O3_SRF','NO3_SRF']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst'
description='varcommon'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

