import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

#
typevarlist=['glob']
#
# ONE VARIABLES (for 5 experiments)
#----------------------------------
#
description='varcommon-typevarcommon'
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_f19_20250416_test01', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_nodfch4_s01_20250416', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_1xdfch4_s01_20250416', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_0.05xdfch4_s01_20250416', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_20xdfch4_s01_20250416']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[-19,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=[ \
              'TAU2_CH4', \
#              'TREFHT','FSLNT', \
              'cb_CH4', \
#              'LNO_COL_PROD','LNO_PROD_columnburden', \
              'GS_CH4', \
              'cb_O3','OH_columnburden', \
              'ch4vmr','co2vmr','n2ovmr', \
              'CH4_SRF']
#             'tempocn']
#             'CH4_SURF_DIFF_SAT','CH4_SURF_DIFF_UNSAT','CH4_SURF_EBUL_SAT','CH4_SURF_EBUL_UNSAT','CH4_SURF_AERE_SAT','CH4_SURF_AERE_UNSAT']
#legendlist=['test02','test04','test05','test06']
legendlist=['(1979)', \
            'no CH4 drydep', \
            '1x CH4 drydep', \
            '0.05x CH4 drydep', \
            '20x CH4 drydep']
#
code='n20250418_esm2025_ch4_amip'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
# ONE VARIABLES (for 4 experiments)
#----------------------------------
#
description='varcommon-typevarcommon'
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_f19_20250416_test01', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_1xdfch4_s01_20250416', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_0.05xdfch4_s01_20250416', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_20xdfch4_s01_20250416']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0]
#            
shiftlist=[-19,0,0,0]
#
colorlist=[0,2,3,4]
#
variablelist=['DF_CH4']
legendlist=['(1979)', \
            '1x CH4 drydep', \
            '0.05x CH4 drydep', \
            '20x CH4 drydep']
#
code='n20250418_esm2025_ch4_amip'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
