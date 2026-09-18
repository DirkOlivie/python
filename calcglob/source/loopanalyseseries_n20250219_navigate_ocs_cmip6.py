import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. N1850
#-----------------------
expidlist=[ \
           'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
           'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'piControl', \
            'historical', \
            'ssp5-8.4']
#
smoothlist=[0,0,0]
colorlist=[0,1,2]
linestylelist=[0,0,0]
shiftlist=[+1849-60,0,0]
#
variablelist=['GS_OCS','cb_OCS','OCS_SRF','TAU2_OCS','DF_OCS','WD_OCS', \
              'TAU2_CH4','GS_CH4', \
              'TAU2_SF6']
#
code='n20250219_navigate_ocs_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
