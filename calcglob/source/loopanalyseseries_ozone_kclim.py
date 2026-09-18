import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# 1. fSST TOA imbalance
#----------------------
expidlist=['NF1850norbc_f19_20191025len30', \
           'NF1850frc2norbc_f09_20200108', \
           'NF1850norbc_tropstratchem_f19_20220105_test03', \
           'NF1850norbc_tropstratchem_f19_20220105_test04', \
           'NF1850norbc_tropstratchem_f19_20220105_test05', \
           'NF1850norbc_tropstratchem_f19_20220105_test06', \
           'NF1850norbc_tropstratchem_f09_20220105_test07', \
           'NF1850norbc_tropstratchem_f19_20220105_test08']

legendlist=['NorESM2 (OsloAero, 2x2)', \
            'NorESM2 (OsloAero, 1x1)', \
            'NorESM2 (FullChem, 2x2, 3)', \
            'NorESM2 (FullChem, 2x2, 4)', \
            'NorESM2 (FullChem, 2x2)', \
            'NorESM2 (FullChem, 2x2, sigma)', \
            'NorESM2 (FullChem, 1x1, sigma)', \
            'NorESM2 (FullChem, 2x2, sigma, 5.5 lightning)']
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=['FSLNT']
#
code='kclim_ozone_fsst1850_toaimbalance'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

# 2. coupled TOA imbalance
#-------------------------
expidlist=['N1850_f19_tn14_20190621', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test05', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test06', \
           'N1850_tropstratchem_prep_f19_nt14_20211217_test07']
#          'N1850vsls_tropstratchem_prep_f19_nt14_20220223_test01']

legendlist=['NorESM2 (OsloAero, 2x2)', \
            'NorESM2 (OsloAero, 1x1)', \
            'NorESM2 (FullChem, 2x2, dep.corr.)', \
            'NorESM2 (FullChem, 2x2, dep.corr., prescr. O3 + strat. aer.)', \
            'NorESM2 (FullChem, 2x2)']
#           'NorESM2 (FullChem, 2x2, sigma, ocean CHBr3)']
           
shiftlist=[-1599,-1199,0,0,0]
smoothlist=[5,5,5,5,5]
#
variablelist=['FSLNT','SFDMS','cb_SULFATE','cb_OM']
#
code='kclim_ozone_cpl1850_toaimbalance'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)

# 3. Ozone impact from CHBr3 x 0.0, CHBr3 x 1.0, CHBr3 x 2.0
#-----------------------------------------------------------
expidlist=['NF1850norbc_tropstratchem_f19_20220105_test09', \
           'NF1850norbc_tropstratchem_f19_20220105_test06', \
           'NF1850norbc_tropstratchem_f19_20220105_test10']

legendlist=['NorESM2 (FullChem, 2x2, sigma, CHBr3 = 0.0ppt)', \
            'NorESM2 (FullChem, 2x2, sigma, CHBr3 = 1.0ppt)', \
            'NorESM2 (FullChem, 2x2, sigma, CHBr3 = 2.0ppt)']
shiftlist=[0,0,0]
smoothlist=[0,0,0]
#
variablelist=['FSLNT','cb_O3','CHBR3_SRF']
#
code='kclim_ozone_fsst1850_chbr3'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)



# 3.bis 
expidlist=['N1850frc2_f19_tn14_bromo_07', \
           'N1850vsls_tropstratchem_prep_f19_nt14_20220223_test01', \
           'N1850vsls_tropstratchem_prep_f19_nt14_20220223_test02']

legendlist=['OsloAero + ocean CHBr3', \
            'FullChem + ocean CHBr3', \
            'FullChem + ocean CHBr3']

shiftlist=[0,0,0]
smoothlist=[0,0,0]
#
variablelist=['CHBR3_SRF','SFCHBR3']
#
code='kclim_ozone_cpl1850_chbr3'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)




# 4. stratospheric aerosol
# 4.1 AOD without emissions in SO4(PR)
#-------------------------------------- 
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
#           'NFHISTnorbc_f19_20191107', \
#           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
#           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
#           'FCHIST_f19_mg17_20220111_test6', \
# CESM 1970-2014          
           'FCHIST_f09_mg17_20220111_test7']
#           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero (DOD550divDAYFOC)', \
#            'Oslo-Aero (AODVVOLCdivDAYFOC)', \
#            'Oslo-Aero (AOD_VISdivDAYFOC)', \
            'FullChem (DOD550divDAYFOC)', \
#            'FullChem (AOD_VISdivDAYFOC)', \
            'CESM (AODVISdn)', \
#            'CESM (AODVISstdn)', \
            'CESM (AODVISdn)', \
#            'CESM (AODVISstdn)', \
            'CESM (AODVISdn)']
#            'CESM (AODVISstdn)']
#legendlist=['','','','','','','','','','','']              
#            
shiftlist=[0,0,0,0,0]#,0,0,0,0,0,0]
smoothlist=[0,0,0,0,0]#,0,0,0,0,0,0]
#
variablelist=['DOD550divDAYFOC', \
#              'AODVVOLCdivDAYFOC', \
#              'AOD_VISdivDAYFOC', \
              'DOD550divDAYFOC', \
#              'AOD_VISdivDAYFOC', \
              'AODVISdn', \
#              'AODVISstdn', \
              'AODVISdn', \
#              'AODVISstdn', \
              'AODVISdn']
#              'AODVISstdn']
#
code='kclim_ozone_fsst1850_aodstrat'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)

# 4.2 AOD - with emission correction in SO4_PR
#---------------------------------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
#           'NFHISTnorbc_f19_20191107', \
#           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
#           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
#           'FCHIST_f19_mg17_20220111_test6',\
# CESM 1970-2014 (1x1)
           'FCHIST_f09_mg17_20220111_test7']
#           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
#            'Oslo-Aero (AODVVOLCdivDAYFOC)', \
#            'Oslo-Aero (AOD_VISdivDAYFOC)', \
            'FullChem', \
#            'FullChem (AOD_VISdivDAYFOC)', \
            'FullChem (SO4-volc)', \
#            'FullChem (AOD_VISdivDAYFOC, SO4-volc)', \
            'CESM', \
#            'CESM (AODVISstdn)', \
            'CESM', \
#            'CESM (AODVISstdn)', \
            'CESM (1x1)']
#            'CESM (AODVISstdn)']
#legendlist=['','','','','','','','','','','','','']              
smoothlist=[0,0,0,0,0,0]#,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0]#,0,0,0,0,0,0,0]
#
variablelist=[ \
#              'DOD550divDAYFOC', \
#              'AODVVOLCdivDAYFOC', \
              'AOD_VISdivDAYFOC', \
              'DOD550divDAYFOC', \
#              'AOD_VISdivDAYFOC', \
              'DOD550divDAYFOC', \
#              'AOD_VISdivDAYFOC', \
              'AODVISdn', \
#              'AODVISstdn', \
              'AODVISdn', \
#              'AODVISstdn', \
              'AODVISdn']
#              'AODVISstdn']
#
code='kclim_ozone_fsst1850_aodstrat_so4pr'
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
# CESM 1850-1869
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem', \
            'FullChem (SO4-volc)', \
            'CESM', \
            'CESM',
            'CESM (1x1)']
#            
shiftlist=[0,0,0,0,0,0]
smoothlist=[0,0,0,0,0,0]
#
variablelist=['cb_O3','FSDSC','EMI_SO2_TOT_noresm2','SFisoprene','SFmonoterp','cb_isoprene','cb_monoterp','FSDS','FSDSC']
#
code='kclim_ozone_fsst1850_aodstrat'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=['cb_O3'],typevar='90S28SLAND',freqtype='SON',description=description,code=code)
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=['cb_O3'],typevar='90S28SLAND',freqtype='SEP',description=description,code=code)
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=['cb_O3'],typevar='90S28SLAND',freqtype='OCT',description=description,code=code)
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=['cb_O3'],typevar='90S28SLAND',freqtype='NOV',description=description,code=code)
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
#           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
#
refidlist=expidlist
# 
wlist=[1.,0.]
#
legendlist=[\
#            'Oslo-Aero', \
            'SO'+r'$_4$'+'(na) (100 %)', \
            'SO'+r'$_2$'+' (100 %), SO'+r'$_4$'+'(pr)(0 %)', \
            'SO'+r'$_2$'+' (97.5 %), SO'+r'$_4$'+'(pr)(2.5 %)', \
            'SO'+r'$_2$'+' (95 %), SO'+r'$_4$'+'(pr)(5 %)', \
            'SO'+r'$_2$'+' (90 %), SO'+r'$_4$'+'(pr)(10 %)', \
            'SO'+r'$_2$'+' (80 %), SO'+r'$_4$'+'(pr)(20 %)', \
            'SO'+r'$_2$'+' (50 %), SO'+r'$_4$'+'(pr)(50 %)', \
            'SO'+r'$_2$'+' (0 %), SO'+r'$_4$'+'(pr)(100 %)']
#            
shiftlist=[0,0,0,0,0,0,0,0]#,0]
smoothlist=[0,0,0,0,0,0,0,0]#,0]
#
variablelist=['D550_SO4','AOD_VISdivDAYFOC','DOD550divDAYFOC']
variablelist=['EXTVIS_columnburden']
#
code='kclim_ozone_fsst1850_aodsulfate'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
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
