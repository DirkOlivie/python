import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. NHIST aerosol-only - how well do all historical simulations
#---------------------------------------------------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NHISTfrc2_02_f09_tn14_20200427ext', \
           'NHISTfrc2_03_f09_tn14_20200519ext']

refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'aer-only (2x2)', \
            'aer-only (2x2)', \
            'aer-only (2x2)', \
            'aer-only (1x1)', \
            'aer-only (1x1)', \
            'aer-only (1x1)']
#
smoothlist=[0,0,0,0,0,0]
colorlist=[0,0,0,1,1,1]
linestylelist=[0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0]
#
variablelist=['AOD_VISdivDAYFOC']
#
code='n20250314_navigate_volc_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 2. NHIST aerosol-only - how well do all historical simulations
#---------------------------------------------------------------
expidlist=[ \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NHISTfrc2_02_f09_tn14_20200427ext', \
           'NHISTfrc2_03_f09_tn14_20200519ext', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03']

refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'aer-only (1x1)', \
            'aer-only (1x1)', \
            'aer-only (1x1)', \
            'full-chem (1x1)']
#
smoothlist=[0,0,0,0]
colorlist=[1,1,1,2]
linestylelist=[0,0,0,0]
shiftlist=[0,0,0,0]
#
variablelist=['AOD_VISdivDAYFOC']
#
code='n20250314_navigate_volc_fullchem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 3. 
#-----------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext',    
           'NHIST_f19_tn14_20250311_test04', \
           'NHIST_f19_tn14_20250311_test05']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'aer-only (2x2)', \
            'aer-only (2x2)', \
            'aer-only (2x2)', \
            'aer-only+OCS (2x2)', \
            'aer-only+OCS+volcSO2 (2x2)']
#
smoothlist=[0,0,0,0,0]
colorlist=[0,0,0,3,4]
linestylelist=[0,0,0,0,0]
shiftlist=[0,0,0,0,0]
#
variablelist=['AOD_VISdivDAYFOC','cb_SULFATE']
#
code='n20250314_navigate_volc_aeronlyso2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# 4. 
#-----------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625ext', \
#           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
           'NHIST_f19_tn14_20250311_test04', \
           'NHIST_f19_tn14_20250311_test05']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'aer-only', \
#            'full-chem', \
            'aer-only+OCS+SO'+r'$_2$', \
            'aer-only+OCS+SO'+r'$_2$'+'(volc)']
#
smoothlist=[0,0,0]
colorlist=[0,1,2]
linestylelist=[0,0,0]
shiftlist=[0,0,0]
#
variablelist=['AOD_VISdivDAYFOC','cb_SULFATE']
#
code='n20250314_navigate_volc_all'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




