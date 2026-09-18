import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# 1. fSST TOA imbalance
#----------------------
expidlist=['NF1850norbc_f19_20191025len30', \
           'NF1850norbc_f19_20201226', \
           'NF1850norbc_tropstratchem_f19_20220105_test05', \
           'NF1850norbc_tropstratchem_f19_20220105_test08', \
           'NF1850norbc_tropstratchem_reduced_f19_20220105_test02', \
           'NF1850norbc_tropstratchem_reduced_f19_20220105_test03', \
           'NF1850norbc_tropstratchem_reduced_f19_20220105_test05', \
           'NF1850norbc_tropstratchem_reduced_f19_20220105_test07', \
           'NF1850norbc_tropstratchem_reduced_f19_20220105_test09']
#
#legendlist=['NorESM2 (OsloAero, 2x2)', \
#            'NorESM2 (OsloAero, 2x2)', \
#            'NorESM2 (FullChem, 2x2)', \
#            'NorESM2 (FullChem, 2x2, sigma, 5.5 lightning)', \
#            'NorESM2 (FullChem, 2x2, reduced-02)', \
#            'NorESM2 (FullChem, 2x2, reduced-03, no OCS)', \
#            'NorESM2 (FullChem, 2x2, reduced-05, no OCS, 6.66 lightning)', \
#            'NorESM2 (FullChem, 2x2, reduced-07)', \
#            'NorESM2 (FullChem, 2x2, reduced-09)']
#
legendlist=['NorESM2 (OsloAero)', \
            'NorESM2 (OsloAero)', \
            'NorESM2 (FullChem 05)', \
            'NorESM2 (FullChem 08)', \
            'NorESM2 (FullChem r02)', \
            'NorESM2 (FullChem r03)', \
            'NorESM2 (FullChem r05)', \
            'NorESM2 (FullChem r07)', \
            'NorESM2 (FullChem r09)']

shiftlist=[0,0,0,0,0,0,0,0,0]
#smoothlist=[5,5,5,5]
smoothlist=[1,1,1,1,1,1,1,1,1]
#
variablelist=['AOD_VISdivDAYFOC','FSLNT','FLNT','FSNT','SWCF','LWCF','CLDTOT','CLDMED','CLDHGH','CLDLOW','FSDS','FSDSC','CDNUMC','CLDLIQ','CLDICE', \
              'cb_DUST','cb_SALT','cb_SULFATE','cb_BC','cb_OM', \
              'cb_SOA_A1','cb_SOA_NA', \
              'cb_SOA_SV','cb_SOA_LV', \
              'cb_isoprene','cb_monoterp', \
#              'NO3_surfacelayer','OH_surfacelayer','O3_surfacelayer','HO2_surfacelayer', \
              'TAU_DMS','TAU_isoprene','TAU_monoterp', \
              'AOD_VISdivDAYFOC', \
#              'CLDLIQ_columnburden','CLDICE_columnburden', \
              'SFisoprene','SFmonoterp', \
              'FSLNT']
#
variablelist=['FSLNT']
#
code='kclim_ozone_fsst1850_imbalancequest'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

# 2. coupled TOA imbalance
#-------------------------
expidlist=['N1850_f19_tn14_20190621', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test07', \
#           'N1850_tropstratchem_prep_f19_nt14_20211217_test06', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test05']
#
legendlist=['NorESM2 (OsloAero, 2x2)', \
            'NorESM2 (FullChem, 2x2)', \
#            'NorESM2 (FullChem, 2x2, dep.corr., prescr. O3 + strat. aer.)', \
            'NorESM2 (FullChem, 2x2, dep. corr.)']

shiftlist=[-1599,0,0]
smoothlist=[5,5,5]
#
variablelist=['FSLNT','SFDMS','cb_SULFATE','cb_OM','AOD_VISdivDAYFOC','FSDSC','SWCF']
#
code='kclim_ozone_cpl1850_imbalancequest'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

# 3. oyvind
#---------
expidlist=['NF1850norbc_aer2014_f19_f19_20210530', \
           'NF1850norbc_aer2014_f19_f19_20210530_vd']
legendlist=['NorESM2', \
            'NorESM2 (sigma corr.)']
shiftlist=[0,0]
smoothlist=[5,5]
#
variablelist=['cb_DUST','cb_SALT','cb_SULFATE','cb_BC','cb_OM','FSLNT']
#
code='kclim_ozone_fsst1850_imbalancequest_oyvind'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

