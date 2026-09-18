import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtypelist=['YEA']
description='varcommon-typevarcommon'
generalcode='n20230908_kl_seminar'

# CIMP6-only : 1x1 historical
#--------------------------------------------------------------------
expidlist=[ \
#           'NHIST_f19_tn14_20190625ext', \
#           'NHIST_02_f19_tn14_20190801ext', \
#           'NHIST_03_f19_tn14_20190801ext', \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NHISTfrc2_02_f09_tn14_20200427ext', \
           'NHISTfrc2_03_f09_tn14_20200519ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2 (mem. 1)', \
            'NorESM2 (mem. 2)', \
            'NorESM2 (mem. 3)']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,0,0]
#
variablelist=['TREFHT']
#
code=generalcode+'_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2015])
#
typevarlist=['glob']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# CIMP6-only : 1x1 historical + SSP585
#--------------------------------------------------------------------
expidlist=[ \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NSSP585frc2_f09_tn14_20191105']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2 (historical)', \
            'NorESM2 (ssp5-8.5)']
#
smoothlist=[0,0]
#
shiftlist=[0,0]
#
colorlist=[0,1]
#
variablelist=['SFisoprene','SFmonoterp','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFDMS']
#
code=generalcode+'_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2100])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# CIMP6-only : 2x2 damip
#--------------------------------------------------------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
           \
           'N1850aeroxidonly_f19_tn14_20190805ext', \
           'N1850aeroxidonly_02_f19_tn14_20190909', \
           'N1850aeroxidonly_03_f19_tn14_20190913', \
           \
           'N1850ghgonly_f19_tn14_20190712', \
           'N1850ghgonly_02_f19_tn14_20190909', \
           'N1850ghgonly_03_f19_tn14_20190913', \
           \
           'N1850natonly_f19_tn14_20190805ext', \
           'N1850natonly_02_f19_tn14_20190909', \
           'N1850natonly_03_f19_tn14_20190913']        
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2 (all forcings)', \
            '', \
            '', \
            'NorESM2 (only aerosol)', \
            '', \
            '',
            'NorESM2 (only ghg)', \
            '', \
            '',
            'NorESM2 (only natural)', \
            '', \
            ''] 
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,0,0,1,1,1,2,2,2,3,3,3]
#
variablelist=['TREFHT']
#
code=generalcode+'_cmip6_damip'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2015])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# CIMP6-only : fsst - nat-only
#--------------------------------------------------------------------
expidlist=['NFHISTnorpibc_natonly_f19_20191208', \
           'NFHISTnorpibc_natonly_02_f19_20200118', \
           'NFHISTnorpibc_natonly_03_f19_20200118']
#
refidlist=['NF1850norbc_f19_20191025len165', \
           'NF1850norbc_f19_20191025len165', \
           'NF1850norbc_f19_20191025len165']
#
wlist=[1.,-1.]
#
legendlist=['NorESM2 (mem. 1)', \
            'NorESM2 (mem. 2)', \
            'NorESM2 (mem. 3)']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#
variablelist=['FSLNT']
#
code=generalcode+'_cmip6_fhist_natonly'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2015])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)




# TOA imbalance, ocean temperature in N1850 : CMIP6 versusu full-chem
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
shiftlist=[-1200+1,0]
#
colorlist=[0,1]
#
variablelist=['FSLNT','tempocn']
#
code=generalcode+'_piControl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[0,500])
#
#typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# TREFHT PRECT SWCF LWCF SFisoprene SFmonoterp : CMIP6 versus full-chem
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
              'cb_SOA_NA','cb_SOA_A1','cb_SOA_A1NA','cb_OM','SFDMS']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# TREFHT PRECT SWCF LWCF SFisoprene SFmonoterp : CMIP6 versus full-chem
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20200718', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)' ]
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#
variablelist=['D550_DUdivDAYFOC','D550_SSdivDAYFOC','D550_POMdivDAYFOC']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# FSDSC : comparison with CESM
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
variablelist=['FSDSC','SFisoprene','SFmonoterp','cb_isoprene','cb_monoterp','TAU_DMS','TAU_isoprene','TAU_monoterp']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1855,2055])
#
typevar='glob'
freqtype='YEA'
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# LNO_COL_PROD
#----------------------------------------------------------------------
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
variablelist=['LNO_COL_PROD','CO_SRF','NO2_SRF']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1855,2055])
#
typevar='glob'
freqtype='YEA'
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# OZONE COLUMN : comparison with CESM
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
              'cb_O3','cb_O3','cb_O3','cb_O3'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1855,2055])
#
typevar='glob'
freqtype='YEA'
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
typevar='90S28SLAND'
freqtype='SON'
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)

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
variablelist=['AOD_VISdivDAYFOC', 'AOD_VISdivDAYFOC', 'AOD_VISdivDAYFOC', \
              'AODVISdn', 'AODVISdn'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)

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
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

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
variablelist=['SO2_SRF','DMS_SRF','H2SO4_SRF', \
              'O3_surfacelayer','HO2_surfacelayer','NO3_surfacelayer','OH_surfacelayer', \
              'EMI_SO2_TOT_noresm2']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevarlist=['glob']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

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
variablelist=['ozone_surfacelayer','O3_SRF','O3_SRF','O3_SRF','O3_SRF'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevar='glob'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# ozone_surfacelayer/O3_SRF
#----------------------------------------------------------------------
variablelist=['OH_bef_surfacelayer','OH_SRF','OH_SRF','OH_SRF','OH_SRF']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_DUST / cb_dst_a123
#----------------------------------------------------------------------
variablelist=['cb_DUST','cb_DUST','cb_DUST','cb_dst_a123','cb_dst_a123']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_SALT / cb_ncl_a123
#----------------------------------------------------------------------
variablelist=['cb_SALT','cb_SALT','cb_SALT','cb_ncl_a123','cb_ncl_a123']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_SULFATE / cb_so4_a123
#----------------------------------------------------------------------
variablelist=['cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_so4_a123','cb_so4_a123']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_SOA_A1NA / cb_soa12345_a12
#----------------------------------------------------------------------
variablelist=['cb_SOA_A1NA','cb_SOA_A1NA','cb_SOA_A1NA','cb_soa12345_a12','cb_soa12345_a12']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_BC / cb_bc_a14
#----------------------------------------------------------------------
variablelist=['cb_BC','cb_BC','cb_BC','cb_bc_a14','cb_bc_a14']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_OM / cb_pom_a14
#----------------------------------------------------------------------
variablelist=['cb_OM','cb_OM','cb_OM','cb_pom_a14_soa12345_a12','cb_pom_a14_soa12345_a12']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_DUST / cb_dst_a123
#----------------------------------------------------------------------
#
expidlist=[ \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01', \
            'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2-chem', \
            'NorESM2-chem (ssp585)', \
            'CESM2-chem']
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,0,0]
#
colorlist=[0,1,2,4]
#
variablelist=['cb_DUST','cb_DUST','cb_DUST','cb_dst_a123']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1850,2055])
#
typevar='glob'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
# EMI_DUST_TOT_noresm2 / SFdst_a123
#----------------------------------------------------------------------
variablelist=['EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','SFdst_a123']
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
