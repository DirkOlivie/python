import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtypelist=['YEA']
description='varcommon'
generalcode='n20230420_kclim_ozone_vsls_hist'


# Full-chemistry historical/piControl - NorESM coupled and CESM fSST - TREFHT, cb_O3
#-----------------------------------------------------------------------------------
#
expidlist=[ \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
            'FCHIST_f19_mg17_20220111_test1']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hist 01','hist 02', 'hist 03', 'piControl 12','piControl 14','CESM (2x2, fSST)']
#
smoothlist=[0,0,0,0,0,0]
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,1850-1,1850-1,0]
#
colorlist=[0,1,2,3,4,5]
#
variablelist=['TREFHT','cb_O3']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# Full-chemistry historical/piControl - NorESM - optical depth
#------------------------------------------------------------
#
expidlist=[ \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14',]
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hist 01','hist 02', 'piControl 12','piControl 14']
#
smoothlist=[0,0,0,0]
smoothlist=[5,5,5,5]
#            
shiftlist=[0,0,1850-1,1850-1]
#
colorlist=[0,1,2,3,4]
#
variablelist=['DOD550divDAYFOC','D550_SO4']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# Full-chemistry and CMIP6 - NorESM - tempocn
#--------------------------------------------
expidlist=[ \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01_from1880', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
            \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTfrc2_02_f09_tn14_20200427ext', \
            'NHISTfrc2_03_f09_tn14_20200519ext', \
            'N1850frc2_f09_tn14_20191001', \
            \
            'NHIST_f19_tn14_20190625ext', \
            'NHIST_02_f19_tn14_20190801ext', \
            'NHIST_03_f19_tn14_20190801', \
            'N1850_f19_tn14_20190621']

#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hist 01','hist 02','piControl 12','piControl 14', \
            'hist CMIP6','hist CMIP6','hist CMIP6','piControl CMIP6', \
            'hist CMIP6 2x2','hist CMIP6 2x2','hist CMIP6 2x2','piControl CMIP6 2x2']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,1850-1,1850-1,0,0,0,1850-1200,0,0,0,1850-1600]
#
colorlist=[0,1,2,3, \
           4,4,4,5, \
           6,6,6,7]
#
variablelist=['tempocn']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
#for freqtype in freqtypelist : 
#    for typevar in typevarlist : 
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# Full-chemistry and CMIP6 - NorESM - TREFHT, ...
#------------------------------------------------
expidlist=[ \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
            \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTfrc2_02_f09_tn14_20200427ext', \
            'NHISTfrc2_03_f09_tn14_20200519ext', \
            'N1850frc2_f09_tn14_20191001', \
            \
            'NHIST_f19_tn14_20190625ext', \
            'NHIST_02_f19_tn14_20190801ext', \
            'NHIST_03_f19_tn14_20190801', \
            'N1850_f19_tn14_20190621']

#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hist 01','hist 02','hist03','piControl 12','piControl 14', \
            'hist CMIP6','hist CMIP6','hist CMIP6','piControl CMIP6', \
            'hist CMIP6 2x2','hist CMIP6 2x2','hist CMIP6 2x2','piControl CMIP6 2x2']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,1850-1,1850-1,0,0,0,1850-1200,0,0,0,1850-1600]
#
colorlist=[0,1,2,3,4, \
           5,5,5,6, \
           7,7,7,8]
#
variablelist=['TREFHT','cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
                       'EMI_OM_TOT_noresm2','emi_BC_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.4')
#
typevarlist=['glob']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



# Full-chemistry and CMIP6 - NorESM/CESM - TOTAL OZONE COLUMN
#-----------------------------------------------------------
expidlist=[ \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
           'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12', \
           'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
            \
           'FCHIST_f19_mg17_20220111_test1', \
            \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NHISTfrc2_02_f09_tn14_20200427ext', \
           'NHISTfrc2_03_f09_tn14_20200519ext', \
           'N1850frc2_f09_tn14_20191001', \
            \
           'NHIST_f19_tn14_20190710', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801', \
           'N1850_f19_tn14_20190722']           
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hist 01','hist 02','hist 03','piControl 12','piControl 14', \
            'CESM (2x2, fSST)', \
            'hist CMIP6','hist CMIP6','hist CMIP6','piControl CMIP6', \
            'hist CMIP6 2x2','hist CMIP6 2x2','hist CMIP6 2x2','piControl CMIP6 2x2']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,1850-1,1850-1, \
           0, \
           0,0,0,1850-1200, \
           0,0,0,1850-1800]
#
colorlist=[0,1,2,3,4, \
           5, \
           6,6,6,7, \
           8,8,8,9]
#
variablelist=['cb_O3','cb_O3','cb_O3','cb_O3','cb_O3', \
              'cb_O3', \
              'ozone_columnburden','ozone_columnburden','ozone_columnburden','ozone_columnburden', \
              'ozone_columnburden','ozone_columnburden','ozone_columnburden','ozone_columnburden']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.4')
#
typevarlist=['glob','90S28SLAND']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
