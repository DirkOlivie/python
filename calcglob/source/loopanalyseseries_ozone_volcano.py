import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol



# 1. Stratospheric aerosol (1850-2014) including CESM-chem and CESM-mam4
#-----------------------------------------------------------------------
expidlist=[ \
# Standard NorESM2-LM        
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM           
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test06', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test07', \
# CESM-chem
           'FCHIST_f19_mg17_20220111_test1', \
# CESM-MAM4
           'FHIST_f19_f19_mg17_20211015']
#
legendlist=[ \
# Standard NorESM2-LM        
           'Standard NorESM2-LM', \
# Full-chemistry NorESM2            
            'FullChem (SO2 0%/SO4 100%)', \
            'FullChem (SO2 0%/SO4 100%, 6.66LiNOx)', \
# CESM-chem
            'CESM-chem', \
# CESM-MAM4
            'CESM-MAM4']
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0]
#
code='kclim_ozone_volcano_1850-2014'
#
variablelist=['AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AODVISdn','AODVIS']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
variablelist=['cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_so4_a123','cb_so4_a123']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)


# 2. Stratospheric aerosol (1850-2014)
#-------------------------
expidlist=[ \
# Standard NorESM2-LM        
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM           
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test06', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test07']
# Full chemistry NorESM
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
#
legendlist=[ \
# Standard NorESM2-LM        
           'Standard NorESM2-LM', \
# Full-chemistry NorESM2            
            'FullChem (SO2 0%/SO4 100%)', \
            'FullChem (SO2 0%/SO4 100%, 6.66LiNOx)']
# Full-chemistry NorESM2        
#            'FullChem (SO2 100%/SO4 0%)', \
#            'FullChem (SO2 97.5%/SO4 2.5%)', \
#            'FullChem (SO2 90%/SO4 10%)', \
#            'FullChem (SO2 50%/SO4 50%)', \
#            'FullChem (SO2 0%/SO4 100%)']
#
smoothlist=[0,0,0]#,0,0,0,0,0]
#            
shiftlist=[0,0,0]#,0,0,0,0,0]
#
variablelist=['AKCXS', 'cb_SO2', 'cb_SULFATE','cb_SO4_NA','cb_SO4_A1','cb_SO4_PR','cb_SO4_AC','cb_SO4_A2','DOD550divDAYFOC','N_AER_columnburden']
variablelist=['D550_SO4']
variablelist=['SO4_A1clcoagTend','SO4_A1coagTend','SO4_A1condTend','SO4_A2_OCWclcoagTend','SO4_ACcoagTend','SO4_NAclcoagTend','SO4_NAcoagTend','SO4_NAcondTend']
variablelist=['AOD_VISdivDAYFOC']
#
code='kclim_ozone_volcano_noresmonly_1850-2014'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


# 3. Stratospheric aerosol (1970-2014)
#-------------------------
expidlist=[ \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
#
legendlist=['FullChem (SO2 100%/SO4 0%)', \
            'FullChem (SO2 97.5%/SO4 2.5%)', \
            'FullChem (SO2 95%/SO4 5%)', \
            'FullChem (SO2 90%/SO4 10%)', \
            'FullChem (SO2 80%/SO4 20%)', \
            'FullChem (SO2 50%/SO4 50%)', \
            'FullChem (SO2 0%/SO4 100%)', \
            'FullChem (SO4(na) 100%)']
#
smoothlist=[0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=['AKCXS', 'cb_SO2', 'cb_SULFATE','cb_SO4_NA','cb_SO4_A1','cb_SO4_PR','cb_SO4_AC','cb_SO4_A2','DOD550divDAYFOC','N_AER_columnburden', \
              'D550_SO4', \
              'SO4_A1clcoagTend','SO4_A1coagTend','SO4_A1condTend','SO4_A2_OCWclcoagTend','SO4_ACcoagTend','SO4_NAclcoagTend','SO4_NAcoagTend','SO4_NAcondTend', \
              'NNAT_1_columnburden','NNAT_5_columnburden'] 
#
code='kclim_ozone_volcano_noresmonly'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


# 1. AOD
#-------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
# CESM 1850-2014
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
# CESM 1970-2014 (1x1)
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem (SO2 100%)', \
            'FullChem (SO4 100%)', \
            'FullChem (SO2 50%/SO4 50%)', \
            'FullChem (SO2 97.5%/SO4 2.5%)', \
            'CESM', \
            'CESM', \
            'CESM (1x1)']
smoothlist=[0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=[ \
              'AOD_VISdivDAYFOC', \
              'DOD550divDAYFOC', \
              'DOD550divDAYFOC', \
              'DOD550divDAYFOC', \
              'DOD550divDAYFOC', \
              'AODVISdn', \
              'AODVISdn', \
              'AODVISdn']
#
code='kclim_ozone_volcano'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)


# 4.2 TOTAL SO2 emissions
#------------------------ 
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem (SO2 100%)', \
            'FullChem (SO4 100%)', \
            'FullChem (SO2 50%/SO4 50%)', \
            'FullChem (SO2 97.5%/SO4 2.5%)', \
            'CESM', \
            'CESM', \
            'CESM (1x1)']
#            
shiftlist=[0,0,0,0,0,0,0,0]
smoothlist=[0,0,0,0,0,0,0,0]
#
variablelist=['cb_SO2','cb_O3','FSDSC','EMI_SO2_TOT_noresm2','SFisoprene','SFmonoterp','cb_isoprene','cb_monoterp','FSDS','FSDSC']
#
code='kclim_ozone_volcano'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#
#
# 4.3 TOTAL SO4 load
#-------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
# CESM 1970-2014
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem', \
            'CESM', \
            'CESM', \
            'CESM (1x1)']
#            
shiftlist=[0,0,0,0,0]
smoothlist=[0,0,0,0,0]
#
variablelist=['cb_SULFATE','cb_SULFATE','cb_so4_a123','cb_so4_a123','cb_so4_a123']
#
code='kclim_ozone_fsst1850_sulfateload'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
# CESM 1970-2014 (1x1)
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem', \
            'FullChem (SO4-volc)', \
            'CESM', \
            'CESM', \
            'CESM (1x1)']
#            
shiftlist=[0,0,0,0,0,0]
smoothlist=[0,0,0,0,0,0]
#
variablelist=['cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_so4_a123','cb_so4_a123','cb_so4_a123']
#
code='kclim_ozone_fsst1850_sulfateload_so4pr'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#





# 4.3 D550_SO4
#-------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
#
legendlist=['Oslo-Aero', \
            'FullChem', \
            'FullChem (SO4-volc)']
#            
shiftlist=[0,0,0]
smoothlist=[0,0,0]
#
variablelist=['D550_SO4']
#
code='kclim_ozone_fsst1850_aodsulfate'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#


# 4.4 so4_a1, so4_a2, so4_a3
#---------------------------
expidlist=[ \
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f19_mg17_20220111_test6']
#
legendlist=['so4(a1)', \
            'so4(a2)', \
            'so4(a3)', \
            'so4(a1)', \
            'so4(a2)', \
            'so4_a3']
#            
shiftlist=[0,0,0,0,0,0]
#
variablelist=['cb_so4_a1','cb_so4_a2','cb_so4_a3','cb_so4_a1','cb_so4_a2','cb_so4_a3']
#
code='kclim_ozone_fsst1850_sulfateload'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
#
# 4.5 TOTAL SO4 load
#-------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02']
#
legendlist=['SO4(total)', \
            'SO4(NA)', \
            'SO4(PR)', \
            'SO4(A1)', \
            'SO4(A2)', \
            'SO4(AC)']
#            
shiftlist=[0,0,0,0,0,0]
#
variablelist=['cb_SULFATE','cb_SO4_NA','cb_SO4_PR','cb_SO4_A1','cb_SO4_A2','cb_SO4_AC']
#
code='kclim_ozone_fsst1850_SO4NA_SO4A1'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
#
# 4.6. stratospheric aerosol : impact of volc. SO2 versus OCS
#------------------------------------------------------------
expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test11', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test12']
#
legendlist=['SO2 + OCS', \
            'OCS', \
            'SO2']
#
variablelist=['AOD_VISdivDAYFOC', \
              'cb_O3', \
              'D550_SO4']
#            
shiftlist=[0,0,0]
#
code='kclim_ozone_fsst1850_aodstrat_so2ocs'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


# 6. aerosol burden in NFHIST
#----------------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02']
#
legendlist=['Oslo-Aero', \
            'FullChem']
#            
shiftlist=[0,0]
smoothlist=[0,0]
#
variablelist=['cb_BC','cb_OM','cb_SALT','cb_DUST','cb_SULFATE', \
              'cb_isoprene','cb_monoterp', \
              'cb_SOA_A1','cb_SOA_NA', \
              'cb_SOA_A1NA']
#
code='kclim_ozone_fsst1850_aerosol'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

# 7. Dry deposition bug in NFHIST
#--------------------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NF1850norbc_tropstratchem_f19_20220105_test05', \
# Full chemistry NorESM
           'NF1850norbc_tropstratchem_f19_20220105_test06']
#
legendlist=['FullChem', \
            'FullChem (correction)']
#            
shiftlist=[0,0]
#
variablelist=['cb_BC','cb_OM','cb_SALT','cb_DUST','cb_SULFATE']
#
code='kclim_ozone_fsst1850_depositionbug'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


# 8. aerosol burden in N1850
#---------------------------
expidlist=[ \
# Oslo-Aero (Betzy)
           'N1850_f19_tn14_20190621', \
# Full-chemistry
#           'N1850_tropstratchem_prep_f19_nt14_20211217_test03', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test05', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test06']
#           'N1850_tropstratchem_prep_f19_nt14_20211217_test07', \
#           'N1850vsls_tropstratchem_prep_f19_nt14_20220223_test01']
#
legendlist=['Oslo-Aero', \
#            'FullChem (no ocn DMS)', \
            'FullChem', \
            'FullChem (clim. O3 and strat. aer.)']
#            'FullChem (no drydep corr.)', \
#            'FullChem (ocn CHBr3)']
#            
shiftlist=[0,0,0]#,0]#,0,0]
#
variablelist=['cb_BC','cb_OM','cb_SALT','cb_DUST','cb_SULFATE', \
              'cb_isoprene','cb_monoterp', \
              'cb_SOA_A1','cb_SOA_NA', \
              'cb_SOA_A1NA']
#
variablelist=['FSDS','FSDSC']
variablelist=['SFDMS']
#
code='kclim_ozone_n1850_aerosol'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
