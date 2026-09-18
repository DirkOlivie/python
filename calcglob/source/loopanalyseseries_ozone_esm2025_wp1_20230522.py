import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtypelist=['YEA']
description='varcommon'
generalcode='n20230522_esm2025_wp1'

# Full-chemistry and CMIP6 - NorESM - TREFHT, ...
#------------------------------------------------
expidlist=[ \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
            \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTfrc2_02_f09_tn14_20200427ext', \
            'NHISTfrc2_03_f09_tn14_20200519ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['full chem.', \
            'aerosol only (CMIP6)','aerosol only (CMIP6)','aerosol only (CMIP6)']
#
smoothlist=[0,0,0,0]
#            
shiftlist=[0,0,0,0]
#
colorlist=[0,1,2,3]
#
variablelist=['TREFHT']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(xrange=[1870,2015]) # legendlocation='outside1.4')
#
typevarlist=['glob']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



# Full-chemistry and CMIP6 - NorESM/CESM - TOTAL OZONE COLUMN
#-----------------------------------------------------------
expidlist=[ \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
           'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
            \
           'FCHIST_f19_mg17_20220111_test1', \
            \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'N1850frc2_f09_tn14_20191001ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['full chem. (historical)','full chem. (piControl)', \
            'CESM (2x2, fSST, historical)', \
            'aer. only CMIP6 (historical, prescribed)',
            'aer. only CMIP6 (piControl, presribed)']
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[0,1850-1, \
           0, \
           0,1850-1200]
#
colorlist=[0,1,2,3,4]
#
variablelist=['cb_O3','cb_O3', \
              'cb_O3', \
              'ozone_columnburden','ozone_columnburden']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(xrange=[1870,2015]) # legendlocation='outside1.4')
#
typevarlist=['glob','90S28SLAND']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
