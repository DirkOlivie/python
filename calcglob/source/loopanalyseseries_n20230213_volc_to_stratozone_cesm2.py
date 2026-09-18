import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# stratospheric aerosol

# 1. CESM-only historical
#------------------------
expidlist=['FCHIST_f19_mg17_20220111_test1',
           'FCHIST_f19_mg17_20220111_test6',
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['2x2', \
            '2x2', \
            '1x1']
#
smoothlist=[0,0,0]
#            
shiftlist=[0,0,0]
#
variablelist=['cb_O3','cb_so4_a123','cb_OCS','cb_SO2','EMI_SO2SO4_as_SO2_TOT_cesm2']
#
code='n20230213_volc_to_stratozone_cesm2_hist'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 2. CESM-only 2010-climo : perturbation simulations
#---------------------------------------------------
expidlist=['FC2010climo_prep_f19_20210204_test5',
           'FC2010climo_prep_f19_20210204_test11',
           'FC2010climo_prep_f19_20210204_test17',
           'FC2010climo_prep_f19_20210204_test13',
           'FC2010climo_prep_f19_20210204_test9']

#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['reference', \
            'no volc.', \
            'no ocs', \
            'no volc., no ocs', \
            'cesm2.2']
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0]
#
variablelist=['cb_O3','cb_so4_a123','cb_OCS','cb_SO2','EMI_SO2SO4_as_SO2_TOT_cesm2']
#
code='n20230213_volc_to_stratozone_cesm2_climo2010'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

