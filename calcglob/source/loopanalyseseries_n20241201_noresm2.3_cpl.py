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
#           'N1850_f19_tn14_20231204_test05', \
            \
#           'N1850_f19_tn14_20231204_test15', \
#           'N1850_f19_tn14_20231204_test16', \
#           'N1850_f19_tn14_20231204_test14', \
#           'N1850_f19_tn14_20231204_test17', \
            \
#           'N1850_f19_tn14_20231204_test13', \
#           'N1850_f19_tn14_20231204_test03', \
           'N1850_f19_tn14_20231204_test11', \
           'N1850_f19_tn14_20231204_test12', \
            \
           'N1850_f19_tn14_20241127_test01', \
           'N1850_f19_tn14_20241127_test02', \
           'N1850_f19_tn14_20241127_test03', \
           'N1850_f19_tn14_20241127_test04', \
           'N1850_f19_tn14_20241127_test05', \
           'N1850_f19_tn14_20241127_test06', \
           'N1850_f19_tn14_20241127_test07', \
           'N1850_f19_tn14_20241127_test08', \
           'N1850_f19_tn14_20241127_test11', \
           'N1850_f19_tn14_20241127_test12', \
           'N1850_f19_tn14_20241127_test13', \
           'N1850_f19_tn14_20241127_test14', \
           'N1850_f19_tn14_20241127_test15', \
           'N1850_f19_tn14_20241127_test16', \
           'N1850_tropstratchem_f19_tn14_20241127_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'noresm2 (CMIP6)', \
#            'noresm2.1 (no CAM corr.)', \
             \
#            'noresm2.1 (only ice-delimiter corr.)', \
#            'noresm2.1 (only het. freez. corr.)', \
#            'noresm2.1 (only koagsub corr.)', \
#            'noresm2.1 (only dry dep. corr.)', \
             \
#            'noresm2.1 (no koagsub corr.)', \
#            'noresm2.1 (no ice-delimiter corr.)', \
            'noresm2.1', \
            'noresm2.1 + SH/TS', \
            \
            'noresm2.3', \
            'noresm2.3 (gamma=0.284)', \
            'noresm2.3 (gamma=0.274)', \
            'noresm2.3 (gamma=0.294)', \
            'noresm2.3 (old soa-yield)', \
            'noresm2.3 (SI)', \
            'noresm2.3 (gamma=0.276)', \
            'noresm2.3 (gamma=0.278)', \
            'noresm2.3 (SI, 0.0125 SY)', \
            'noresm2.3 (SI, 0.0250 SY)', \
            'noresm2.3 (hetfrz_aer_scalfac=1)', \
            'noresm2.3 (hetfrz_aer_scalfac=1, SI)', \
            'noresm2.3 (hetfrz_aer_scalfac=1, SI, 0.0125 SY)', \
            'noresm2.3 (hetfrz_aer_scalfac=1, SI, 0.0125 SY)', \
            'noresm2.3 (full chem.)']
#            'noresm2.1 + SH/TS']
#
#smoothlist=[0]#,0,0,0]
#smoothlist=[0,0,0,0,0,0,0,0,0,0]
smoothlist=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
#smoothlist=[10,10,10,10,10,10,10,10]
#
#colorlist=[0,1,7,8,4,5,6,2,3,9,10]
colorlist=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
linestylelist=[2,2,2,0,3,3,3,0,0,3,3,0,0,0,0,0,0,1]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#-1200+1600]#,-1+1600]
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
code='n20241201_noresm2.3_cpl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
#typevarlist=['glob','NHLAND','SHSEA','SH','NH','SHLAND','NHSEA']
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
