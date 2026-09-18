import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol

# 1. IMPACT FROM LIGHTNING ON SURFACE OZONE
#------------------------------------------
expidlist=[ \
# Reference
           'NF1850norbc_tropstratchem_f19_20220105_test06', \
# Lightning production *5.5
           'NF1850norbc_tropstratchem_f19_20220105_test08']
#
legendlist=['Standard', \
            'Increased NOx']
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
variablelist=['LNO_PROD_columnburden','LNO_COL_PROD','O3_SRF']
#
code='kclim_ozone_esm2025_wp1'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

# 2. IMPACT FROM HETEROGENEOUS CHEMISTRY ON SURFACE OZONE
#--------------------------------------------------------
expidlist=[ \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test13', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test14', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test15', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test16']
#
legendlist=['Mode 1+2+4+5', \
            'Mode 1', \
            'Mode 2', \
            'Mode 4', \
            'Mode 5']
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0]
#
variablelist=['NO2_SRF','O3_SRF']
#
code='kclim_ozone_esm2025_wp1_hetreac'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

