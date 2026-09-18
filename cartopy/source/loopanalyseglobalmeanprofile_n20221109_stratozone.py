import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard')

#   1. NorESM2 - full chemistry : with/without volcanic aerosol (all 1992)
#-----------------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
#    varlist=['SAD_SULFC','SAD_SULFC','SAD_SULFC','SAD_SULFC']
#    varlist=['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE']
#    varlist=['N_AER','N_AER','N_AER','N_AER']
    varlist=['SAD_SULFC','mmr_SULFATE','N_AER']
    varlist=['N_AER']
    varlist=['mmr_SULFATE']
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO']
    varlist=['H2SO4M_C']
    year0list=[1992,1992,1992,1992,1992]
    year1list=[1992,1992,1992,1992,1992]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['(2x2) 1992','(2x2) 1992 - no volc.','(1x1) 1992','(1x1) 1992 - no volc.','(2x2) 1992 - SO4(na)']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20221109_stratozone_noresm2_all1992'
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
#   2.1 NorESM2 - full chemistry : compare 1992/1990
#----------------------------------------------------
#    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
#               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
#               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18', \
#               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
#               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
#               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18']
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test20', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test22', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test24', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test20', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test22', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test24']
#    varlist=['SAD_SULFC','SAD_SULFC','SAD_SULFC','SAD_SULFC']
#    varlist=['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE']
#    varlist=['N_AER','N_AER','N_AER','N_AER']
    varlist=['SAD_SULFC','mmr_SULFATE','N_AER']
    varlist=['N_AER']
    varlist=['mmr_SULFATE']
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO']
    varlist=['SAD_AERO']
    varlist=['mmr_SULFATE']
#   varlist=['H2SO4M_C']
#    varlist=['sad_noresm2_dry_m01','sad_noresm2_dry_m02','sad_noresm2_dry_m04','sad_noresm2_dry_m05']
#    varlist=['sad_noresm2_dry_m01020405']
#    varlist=['NCONC01','NCONC02','NCONC04','NCONC05']
#    varlist=['N_AER']
    year0list=[1992,1992,1992,1992,1990,1990,1990,1990]
    year1list=[1992,1992,1992,1992,1990,1990,1990,1990]
#   seasonlist=['YEA','YEA','YEA','YEA']
    seasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL']
    legendlist=['(2x2) 1992','(2x2) 1992','(2x2) 1992','(2x2) 1992','(2x2) 1990','(2x2) 1990','(2x2) 1990','(1x1) 1990']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20221109_stratozone_noresm2_1992_1990'
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
#   2.2 NorESM2 - full chemistry : compare 1992/1990
#----------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08']
    varlist=['NCONC01','NCONC02','NCONC04','NCONC05','N_AER','NCONC01','NCONC02','NCONC04','NCONC05','N_AER']
    year0list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990]
    year1list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990]
#   seasonlist=['YEA','YEA','YEA','YEA']
    seasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL']
    legendlist=['(m1) 1992','(m2) 1992','(m4) 1992','(m5) 1992','(all) 1992','(m1) 1990','(m2) 1990','(m4) 1990','(m5) 1990','(all) 1990']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description=''
    code='n20221109_stratozone_comparison_noresm2_1992_1990'
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
#   3.1 CESM2 - full chemistry : compare 1992/1990
#------------------------------
    expidlist=['FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test6', \
               'FCHIST_f09_mg17_20220111_test7', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test6', \
               'FCHIST_f09_mg17_20220111_test7']
#    varlist=['SAD_SULFC','SAD_SULFC','SAD_SULFC','SAD_SULFC']
#    varlist=['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE']
#    varlist=['N_AER','N_AER','N_AER','N_AER']
    varlist=['SAD_SULFC']
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO']
    varlist=['H2SO4M_C']
#   varlist=['sad_cesm2_dry_a1','sad_cesm2_dry_a2','sad_cesm2_dry_a3','sad_cesm2_dry_a4']
    varlist=['sad_cesm2_dry_a1234']
#    varlist=['num_a1234_as_concentration']
#    varlist=['num_a1234']
    varlist=['SAD_AERO']
    varlist=['sad_cesm2_dry_a1234']
    varlist=['sad_cesm2_wet_a1234']
    varlist=['so4_a123']
    year0list=[1992,1992,1992,1990,1990,1990]
    year1list=[1992,1992,1992,1990,1990,1990]
#   seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    seasonlist=['JUL','JUL','JUL','JUL','JUL','JUL']
    legendlist=['(2x2) 1992','(2x2) 1992','(1x1) 1992','(2x2) 1990','(2x2) 1990','(1x1) 1990']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20221109_stratozone_cesm2_1992_1990'
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
#   3.2 CESM2 - full chemistry : compare 1992/1990
#------------------------------
    expidlist=['FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1']
    varlist=['sad_cesm2_dry_a1','sad_cesm2_dry_a2','sad_cesm2_dry_a3','sad_cesm2_dry_a4','sad_cesm2_dry_a1234', \
             'sad_cesm2_dry_a1','sad_cesm2_dry_a2','sad_cesm2_dry_a3','sad_cesm2_dry_a4','sad_cesm2_dry_a1234']
    year0list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990]
    year1list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990]
#   seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    seasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL']
    legendlist=['(a1) 1992','(a2) 1992','(a3) 1992','(a4) 1992','(a1-4) 1992','(a1) 1990','(a2) 1990','(a3) 1990','(a4) 1990','(a1-4) 1990']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description=''
    code='n20221109_stratozone_cesm2_comparison_1992_1990'
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
    expidlist=['FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test1']
#    varlist=['num_a1','num_a2','num_a3','num_a4','num_a1','num_a2','num_a3','num_a4']
#    varlist=['num_c1','num_c2','num_c3','num_c4','num_c1','num_c2','num_c3','num_c4']
    varlist=['num_a1_as_concentration','num_a2_as_concentration','num_a3_as_concentration','num_a4_as_concentration','num_a1234_as_concentration','num_a1_as_concentration','num_a2_as_concentration','num_a3_as_concentration','num_a4_as_concentration','num_a1234_as_concentration']
    year0list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990]
    year1list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990]
#   seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    seasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL']
    legendlist=['(a1) 1992','(a2) 1992','(a3) 1992','(a4) 1992','(a1-4) 1992','(a1) 1990','(a2) 1990','(a3) 1990','(a4) 1990','(a1-4) 1992',]
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description=''
    code='n20221109_stratozone_cesm2_comparison_1992_1990'
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
    

#   4. NorESM2 and CESM2 - full chemistry : compare 1992/1990
#----------------------------------------- 
    expidlist=[ \
#               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
#               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test20', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test22', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test24', \
#               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
#               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test20', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test22', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test24', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test6', \
               'FCHIST_f09_mg17_20220111_test7', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f19_mg17_20220111_test6', \
               'FCHIST_f09_mg17_20220111_test7']
    varlist=['SAD_AERO']
#    year0list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990,1992,1992,1992,1990,1990,1990]
#    year1list=[1992,1992,1992,1992,1992,1990,1990,1990,1990,1990,1992,1992,1992,1990,1990,1990]
    year0list=[1992,1992,1992,1992,1990,1990,1990,1990,1992,1992,1992,1990,1990,1990]
    year1list=[1992,1992,1992,1992,1990,1990,1990,1990,1992,1992,1992,1990,1990,1990]
#   seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    seasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL','JUL']#,'JUL','JUL','JUL','JUL']
    legendlist=['NorESM (2x2) 1992','NorESM (1x1) 1992','NorESM (2x2) 1992','NorESM (2x2) 1992','NorESM (2x2) 1992','NorESM (2x2) 1990','NorESM (1x1) 1990','NorESM (2x2) 1990','NorESM (2x2) 1990','NorESM (2x2) 1990','CESM (2x2) 1992','CESM (2x2) 1992','CESM (1x1) 1992','CESM (2x2) 1990','CESM (2x2) 1990','CESM (1x1) 1990']
    legendlist=['NorESM (2x2) 1992','NorESM (2x2) 1992','NorESM (2x2) 1992','NorESM (2x2) 1992','NorESM (2x2) 1990','NorESM (2x2) 1990','NorESM (2x2) 1990','NorESM (2x2) 1990','CESM (2x2) 1992','CESM (2x2) 1992','CESM (1x1) 1992','CESM (2x2) 1990','CESM (2x2) 1990','CESM (1x1) 1990']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20221109_stratozone_noresm2cesm2_1992_1990'
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
#   5. NorESM2 - full chemistry - NF2010 - some sensitivity runs 
#---------------------------------------------------------------
    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test11', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test12', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test19', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test13', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test14', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test15', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test16', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test08']
    varlist=['SAD_SULFC']
#  varlist=['mmr_SULFATE']
#   varlist=['SAD_AERO']
    year0list=[6,6,6,6,6,6,6,6,6]
    year1list=[10,10,10,10,10,10,10,10,10]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['Reference','no volc. SO2','no OCS', 'no volc. SO2 - no OCS','Only mode 1', 'Only mode 2', 'Only mode 4', 'Only mode 5', 'Mode 1, 2, 4, 5, 12, 14']
    regionlist=['glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20221109_stratozone_noresm2_NF2010'
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
#
#   6. CESM2 - FC2010 - some sensitivity runs
#--------------------------------------------
    expidlist=['FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test6', \
               'FC2010climo_prep_f19_20210204_test7', \
               'FC2010climo_prep_f19_20210204_test9', \
               'FC2010climo_prep_f19_20210204_test10', \
               'FC2010climo_prep_f19_20210204_test11', \
               'FC2010climo_prep_f19_20210204_test12', \
               'FC2010climo_prep_f19_20210204_test13', \
               'FC2010climo_prep_f19_20210204_test14', \
               'FC2010climo_prep_f19_20210204_test17']
    varlist=['SAD_SULFC']
#    varlist=['so4_a123']
#   varlist=['SAD_AERO']
    year0list=[6,6,6,6,6,6,6,6,6,6]
    year1list=[10,10,10,10,10,10,10,10,10,10]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['Test 5 : reference', \
                'Test 6 : photodissociation', \
                'Test 7 : no trop. het. reactions', \
                'Test 9 : two CESM2.2 corrections', \
                'Test 10 : no NH4 creation', \
                'Test 11 : no volc. emis.', \
                'Test 12 : no MAMH2SO4', \
                'Test 13 : no volc. emis. - no OCS', \
                'Test 14 : extra output', \
                'Test 17 : no OCS']
    regionlist=['glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20221109_stratozone_cesm2_FC2010'
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description,code=code)
#
    print('--- loopanalyseglobalmeanprofile ---')
#
if __name__ == '__main__':
    main()
