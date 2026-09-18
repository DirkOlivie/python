import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. N1850
#-----------------------
expidlist=[ \
           'NHIST_123_f19_tn14_20190625ext', \
#           'NHIST_02_f19_tn14_20190801ext', \
#           'NHIST_03_f19_tn14_20190801ext', \
           'NHISTfrc2_123_f09_tn14_20191001ext', \
#           'NHISTfrc2_02_f09_tn14_20200427ext', \
#           'NHISTfrc2_03_f09_tn14_20200519ext', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
           'NHIST_tropstratchem_f09_tn14_20250917_1975_2014']
#
refidlist=expidlist
#
ensembletypelist=['minmax','minmax','','']


wlist=[1.,0.]
#
legendlist=[ \
            'NorESM2-LM (2x2)', \
            'NorESM2-MM (1x1)', \
            'KeyClim-chem (1x1)', \
            'NorESM2.3 (1x1, Eli)']
#
smoothlist=[0,0,0,0]
colorlist=[0,1,2,3]
linestylelist=[0,0,0,0]
#            
shiftlist=[0,0,0,0]
#
variablelist=['PRECT','TREFHT','U10', \
              'EMI_DUST_TOT_noresm2', 'EMI_SALT_TOT_noresm2', \
              'cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
#             'DOD550divDAYFOC', \
              'AOD_VISdivDAYFOC']
#
#              'cb_SOA_A1NA', \
#              'TGCLDLWP','TGCLDIWP', 'TREFHT', \
#              'U10', \
#              'CDNUMC','NUMICE_columnburden','NUMLIQ_columnburden','N_AER_columnburden', \
#              'SFisoprene','SFmonoterp', \
#              'SFDMS','TREFHT','SWCF','LWCF','FSLNT', \
#              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
#              'cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
#              'ICEFRAC']
#variablelist=['TREFHT','LWP','IWP']
#
code='n20260405_noresm2.3_cpl_hist'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
#typevarlist=['glob','NHLAND','SHSEA','SH','NH','SHLAND','NHSEA']
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# ocean temperature
#variablelist=['tempocn']
#typevarlist=['glob']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
