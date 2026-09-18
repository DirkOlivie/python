import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# stratospheric aerosol

# 1. full-chemistry compared with CMIP6 (3 ensemble members)
#-----------------------------------------------------------
expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NHISTfrc2_02_f09_tn14_20200427ext', \
           'NHISTfrc2_03_f09_tn14_20200519ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['full chem.','aerosol only','aerosol only','aerosol only']
#
smoothlist=[0,0,0,0]
#            
shiftlist=[0,0,0,0]
#
variablelist=['TREFHT','AOD_VISdivDAYFOC','cb_BC','cb_DUST','cb_OM','cb_SULFATE','cb_SALT','SWCF']
#
code='n20221210_esm2025_fullchem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 2. full-chemistry compared with CMIP6 (member with AeroCom output)
#-------------------------------------------------------------------
expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
           'NHISTfrc2_f09_tn14_20200718'] 
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['full chem.','aerosol only']
#
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
variablelist=['D550_BCdivDAYFOC','D550_DUdivDAYFOC','D550_POMdivDAYFOC','D550_SO4divDAYFOC','D550_SSdivDAYFOC']
#
code='n20221210_esm2025_fullchem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 3. full-chemistry only
#-----------------------
expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['full chem. (NorESM2)', 'full chem. (CESM2-CAM-chem)']
#
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
variablelist=['cb_O3']
#
code='n20221210_esm2025_fullchem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['90S28SLAND']
freqtypelist=['SON']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
