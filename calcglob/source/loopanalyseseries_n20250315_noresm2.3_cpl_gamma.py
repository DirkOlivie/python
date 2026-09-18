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
           'N1850_f19_tn14_20231204_test11', \
           'N1850_f19_tn14_20231204_test12', \
            \
           'N1850_f19_tn14_20241127_test04', \
           'N1850_f19_tn14_20241127_test02', \
           'N1850_f19_tn14_20241127_test08', \
           'N1850_f19_tn14_20241127_test07', \
           'N1850_f19_tn14_20241127_test03', \
           'N1850_f19_tn14_20241127_test01', \
            \
           'N1850_tropstratchem_f19_tn14_20241127_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'noresm2 (CMIP6)', \
            'noresm2.1', \
            'noresm2.1 + SH/TS', \
            \
            'noresm2.3 (gamma=0.294)', \
            'noresm2.3 (gamma=0.284)', \
            'noresm2.3 (gamma=0.278)', \
            'noresm2.3 (gamma=0.276)', \
            'noresm2.3 (gamma=0.274)', \
            'noresm2.3', \
            \
            'noresm2.3 (full chem.)']
#
smoothlist=[5,5,5,5,5,5,5,5,5,5]
colorlist=[0,1,2,3,4,5,6,7,8,9]
linestylelist=[2,2,2,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0]
#
variablelist=['PRECT', \
              'cb_SOA_A1NA', \
              'TGCLDLWP','TGCLDIWP', 'TREFHT', \
              'U10', \
              'CDNUMC','NUMICE_columnburden','NUMLIQ_columnburden','N_AER_columnburden', \
              'SFisoprene','SFmonoterp', \
              'SFDMS','TREFHT','SWCF','LWCF','FSLNT', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
              'ICEFRAC']
#variablelist=['TREFHT','LWP','IWP']
#
code='n20250315_noresm2.3_cpl_gamma'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob','NH','SH']
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

# ocean amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['glob','atlarc']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
