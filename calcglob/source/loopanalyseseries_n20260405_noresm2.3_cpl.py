import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. N1850
#-----------------------
expidlist=[ \
           'N1850_f19_tn14_20190621ext', \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
           'N1850_f19_tn14_20241127_test01', \
           'N1850_f19_tn14_20241127_test16']


#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'NorESM2-LM (2x2)', \
            'NorESM2-MM (1x1)', \
            'KeyClim-chem (1x1)', \
            'NorESM2.3 - test01 (2x2)', \
            'NorESM2.3 - test16 (2x2)']
#
smoothlist=[0,0,0,0,0]
colorlist=[0,1,2,3,4]
linestylelist=[0,0,0,0,0]
#            
shiftlist=[-1599,-1199,0,-1599,-1599]
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
code='n20260405_noresm2.3_cpl'
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
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ocean temperature
variablelist=['tempocn']
typevarlist=['glob']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
