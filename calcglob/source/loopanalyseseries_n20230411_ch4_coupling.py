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
expidlist=['N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02', \
           'N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test04', \
           'N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test05', \
           'N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test06', \
           'N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test07']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=['TAU2_CH4', \
              'TREFHT','FSLNT', \
              'cb_CH4', \
              'LNO_COL_PROD','LNO_PROD_columnburden', \
              'GS_CH4','TAU2_CH4', \
              'cb_O3','OH_columnburden', \
              'ch4vmr','co2vmr','n2ovmr']
#             'tempocn']
#             'CH4_SURF_DIFF_SAT','CH4_SURF_DIFF_UNSAT','CH4_SURF_EBUL_SAT','CH4_SURF_EBUL_UNSAT','CH4_SURF_AERE_SAT','CH4_SURF_AERE_UNSAT']
#legendlist=['test02','test04','test05','test06']
legendlist=['(1)','(2)','(3)','(4)','(5)']
#
code='n20230411_ch4_coupling'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# ONE VARIABLES (for 2 experiments : test02 and test07)
#------------------------------------------------------
#
description='varcommon-typevarcommon'
#
expidlist=['N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02', \
           'N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test07']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
colorlist=[1,0]
#
variablelist=['TAU2_CH4', \
              'TREFHT','FSLNT', \
              'cb_CH4', \
              'LNO_COL_PROD','LNO_PROD_columnburden', \
              'GS_CH4','TAU2_CH4', \
              'cb_O3','OH_columnburden', \
              'ch4vmr','co2vmr','n2ovmr', \
              'CH4_SRF']
#             'tempocn']
#             'CH4_SURF_DIFF_SAT','CH4_SURF_DIFF_UNSAT','CH4_SURF_EBUL_SAT','CH4_SURF_EBUL_UNSAT','CH4_SURF_AERE_SAT','CH4_SURF_AERE_UNSAT']
#legendlist=['test02','test04','test05','test06']
legendlist=['prescribed surf. conc',\
            'interactive emissions']
#
code='n20230411_ch4_coupling_test02test07'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# ONE VARIABLES (for 1 experiments : test07)
#------------------------------------------------------
#
description='varcommon-typevarcommon'
#
expidlist=['N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test07']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0]
#            
shiftlist=[0]
#
colorlist=[0]
#
variablelist=['TAU2_CH4', \
              'TREFHT','FSLNT', \
              'cb_CH4', \
              'LNO_COL_PROD','LNO_PROD_columnburden', \
              'GS_CH4','TAU2_CH4', \
              'cb_O3','OH_columnburden', \
              'ch4vmr','co2vmr','n2ovmr', \
              'emich4land']
#             'tempocn']
#             'CH4_SURF_DIFF_SAT','CH4_SURF_DIFF_UNSAT','CH4_SURF_EBUL_SAT','CH4_SURF_EBUL_UNSAT','CH4_SURF_AERE_SAT','CH4_SURF_AERE_UNSAT']
#legendlist=['test02','test04','test05','test06']
legendlist=['interactive emissions']
#
code='n20230411_ch4_coupling_test07'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)








# 2.a COMPARE ONE VARIABLES - 11-year running average
#-------------------------
#variablelist=['FCH4xLANDFRAC','SFCH4','emich4land']
#smoothlist=[5,5]
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



# 1. COMPARE TWO VARIABLES
#-------------------------
#
description='typevarcommon'
#
expidlist=['N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02', \
           'N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
colorlist=[0,1]
#
variablelist=['FCH4','emich4land']
legendlist=variablelist
#
code='n20230411_ch4_coupling'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
