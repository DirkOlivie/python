import loopanalyseseries2


# MAIN PROGRAM
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test01', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorbc_f19_20191107']

legendlist=['NorESM2 (full chem. 1)', \
            'NorESM2 (full chem. 2)', \
            'NorESM2 (OsloAero)']
shiftlist=[0,0,0]
#
variablelist=['AODVVOLCdivDAYFOC','ABSVVOLCdivDAYFOC', \
              'AOD_VISdivDAYFOC', \
              'cb_O3']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst_hist'
description='varcommon'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)



# MAIN PROGRAM
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test01', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02']

legendlist=['NorESM2 (full chem. 1)', \
            'NorESM2 (full chem. 2)']
shiftlist=[0,0]
#
variablelist=['FSLNT', \
              'cb_isoprene','cb_monoterp', \
              'TREFHT', \
#              'OH_surfacelayer','O3_surfacelayer','NO3_surfacelayer', \
              'AODVVOLCdivDAYFOC','ABSVVOLCdivDAYFOC', \
              'cb_SULFATE','cb_DUST','cb_SALT','cb_OM','cb_BC','cb_DMS', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'cb_O3', \
              'EMI_SO2_TOT_noresm2','SO2_CMXF', \
              'AOD_VISdivDAYFOC']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst_hist'
description='varcommon'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02']

legendlist=['NorESM2 (full chem. 2)']
shiftlist=[0,0]
#
variablelist=['LNO_COL_PROD','LNO_PROD_columnburden']
#variablelist=['OH_surfacelayer','NO3_surfacelayer','O3_surfacelayer']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial_ozone_fsst_hist'
description='varcommon'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)



