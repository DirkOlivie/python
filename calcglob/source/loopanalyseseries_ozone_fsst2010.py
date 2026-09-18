import loopanalyseseries2

# MAIN PROGRAM

expidlist=[ \
           'FC2010climo_f19_mg17_20210204_test1', \
#          'FC2010climo_f09_mg17_20210204_test1', \
           'FC2010climo_prep_f19_20210204_test5', \
           'FC2010climo_prep_f19_20210204_test7', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test03', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test04', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test08', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test09', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test21']
#
legendlist=[ \
            'CESM2 (2x2)', \
#           'CESM2 (1x1)', \
            'CESM2 (05)', \
            'CESM2 (07)', \
            'NorESM2 (03)', \
            'NorESM2 (04)', \
            'NorESM2 (08)', \
            'NorESM2 (09)', \
            'NorESM2 (21)']
#
shiftlist=[0,0,0,0,0,0,0,0]
#
#variablelist=['FSLNT']
variablelist=['LNO_COL_PROD','cb_ISOP','cb_MTERP','SFISOP','SFMTERP', \
              'OH_surfacelayer','NO3_surfacelayer','O3_surfacelayer','HO2_surfacelayer', \
              'FSLNT']
#
typevar='glob'
freqtype='annavg'
code='trial_ozone_fsst2010'
description='varcommon'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
