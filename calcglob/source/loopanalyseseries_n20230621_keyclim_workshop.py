import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtypelist=['YEA']
description='varcommon'
generalcode='n20230621_keyclim_workshop'


# TOA imbalance, ocean temperature
#----------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem']
#
smoothlist=[0,0]
#
shiftlist=[1850-1200,1850-1]
#
colorlist=[0,1]
#
variablelist=['FSLNT','tempocn']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2015])
#
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# TREFHT PRECT SWCF LWCF SFisoprene SFmonoterp
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTfrc2_02_f09_tn14_20200427ext', \
            'NHISTfrc2_03_f09_tn14_20200519ext', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            '', \
            '', 
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)' ]
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[0,0,0,0,0]
#
colorlist=[0,0,0,1,2]
#
variablelist=['tempocn', \
              'TREFHT','PRECT','SWCF','LWCF', \
              'CDNUMC', \
              'cb_DUST','cb_SALT','cb_SULFATE','cb_OM','cb_BC', \
              'SFisoprene','SFmonoterp','SFDMS']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# OZONE COLUMN
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'FCHIST_f19_mg17_20220111_test1_from1860', \
            'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)', \
            'CESM2-chem (2x2)', \
            'CESM2-chem'] 
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[0,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=['ozone_columnburden', \
              'cb_O3','cb_O3','cb_O3'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1855,2055])
#
typevar='glob'
freqtype='YEA'
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
typevar='90S28SLAND'
freqtype='SON'
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)

# AOD
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'FCHIST_f19_mg17_20220111_test1_from1860', \
            'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)', \
            'CESM2-chem (2x2)', \
            'CESM2-chem'] 
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[0,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=['AOD_VISdivDAYFOC', 'AOD_VISdivDAYFOC', \
              'AODVISdn', 'AODVISdn'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)

# O3_SRF NO2_SRF CO_SRF OH_SRF [only full-chemistry diagnostics]
#---------------------------------------------------------------
#
expidlist=[ \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'FCHIST_f19_mg17_20220111_test1_from1860', \
            'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2-chem', \
            'NorESM2-chem (ssp585)', \
            'CESM2-chem (2x2)', \
            'CESM2-chem'] 
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,0,0]
#
colorlist=[1,2,3,4]
#
variablelist=['O3_SRF','CO_SRF','NO2_SRF','OH_SRF', \
              'EMI_CO_TOT_noresm2','EMI_NO_TOT_noresm2','EMI_NO2_TOT_noresm2', \
              'CLY_SCALED_layer00','BRY_SCALED_layer00', \
              'CLY_SCALED_layer06','BRY_SCALED_layer06']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# SO2_SRF DMS_SRF
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'FCHIST_f19_mg17_20220111_test1_from1860', \
            'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)', \
            'CESM2-chem (2x2)', \
            'CESM2-chem'] 
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[0,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=['SO2_SRF','DMS_SRF', \
              'O3_surfacelayer','HO2_surfacelayer','NO3_surfacelayer','OH_surfacelayer', \
              'EMI_SO2_TOT_noresm2']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# ozone_surfacelayer/O3_SRF
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'FCHIST_f19_mg17_20220111_test1_from1860', \
            'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)', \
            'CESM2-chem (2x2)', \
            'CESM2-chem'] 
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[0,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=['ozone_surfacelayer','O3_SRF','O3_SRF','O3_SRF'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevar='glob'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# ozone_surfacelayer/O3_SRF
#----------------------------------------------------------------------
variablelist=['OH_bef_surfacelayer','OH_SRF','OH_SRF','OH_SRF']
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
