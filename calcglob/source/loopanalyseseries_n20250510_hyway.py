import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


description='varcommon-typevarcommon'
generalcode='n20250510_hyway'
figlayout=cfiglayout.CFigLayout(legendlocation='')
typevarlist=['glob']
freqtype='YEA'

# 1. METHANEMIP + HYWAY
#------------------------------------------------------------------------
#
expidlist=[ \
           'NHISTSSP245_tropstratchem_01_f19_tn14_r2000_s01_20241118', \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
# 
           'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep1p0_s01_hyway_20260315', \
           'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep0p7_s01_hyway_20260315', \
#
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep1p0_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p7_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p65_s01_hyway_20260403', \
#
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4x1p1_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_h2plus100tg_s01_hyway_20260403', \
#           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr1850_h2emi_h2dep0p75_s01_hyway_20260403', \
#
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4emi_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4emi_h2plus100tg_s01_hyway_20260403']        
#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[\
            'fully-coupled', \
            'HYway (ssp2-4.5)', \
            'HYway (ssp5-8.5)', \
#
            'HYway (emi - 1.0 dv)', \
            'HYway (emi - 0.7 dv)', \
#
            'HYway (ctrl - 1.0 dv)', \
            'HYway (ctrl - 0.75 dv)', \
            'HYway (ctrl - 0.7 dv)', \
            'HYway (ctrl - 0.65 dv)', \
#            
            'HYway (CH4+10%)', \
            'HYway (H2+100Tg/yr)', \
#            'HYway (1850)', \
#
            'HYway (CH4emi)', \
            'HYway (CH4emi,H2+100Tg/yr)']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0,0]#,0]
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0,0]#,0]
colorlist=[0,1,2,3,4,3,5,4,6,7,8,9,10]#,11]
linestylelist=[0,0,0,0,0,2,2,2,2,0,0,1,1]#,1]

variablelist=[ \
              'CH4_SRF','O3_SRF','H2_SRF', 'CO2_SRF','SFISOP','TREFHT']
#              'EMI_SALT_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_SO2_TOT_noresm2','EMI_SO4_TOT_noresm2', \
 #             'EMI_BC_TOT_noresm3','EMI_BC_TOT_noresm2', \
 #             'EMI_OM_TOT_noresm2', \
 #             'SFBC_N','BC_NI_CMXF', \
 #             'SFSO2','SO2_CMXF']
#
code=generalcode
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# 2. HYWAY ONLY
#------------------------------------------------------------------------
#
expidlist=[ \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
#
           'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep1p0_s01_hyway_20260315', \
           'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep0p7_s01_hyway_20260315']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[\
            'HYway (ssp2-4.5)', \
            'HYway (ssp5-8.5)', \
            'HYway (emi - 1.0 dv)', \
            'HYway (emi - 0.7 dv)']
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
colorlist=[1,2,3,4]
variablelist=['SFCH2O','CH2O_CHML_columnburden','CH2O_CHMP_columnburden','DF_CH2O','WD_CH2O','cb_CH2O','GS_CH2O','LNO_COL_PROD','TAU_CH4_CHML','CH4_CHML_columnburden','cb_CH4']
code=generalcode
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



#
# 3. HYWAY ONLY
#------------------------------------------------------------------------
#
expidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep1p0_s01_hyway_20260315', \
           'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep0p7_s01_hyway_20260315', \
#       
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep1p0_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p7_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p65_s01_hyway_20260403', \
#
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4x1p1_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_h2plus100tg_s01_hyway_20260403', \
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr1850_h2emi_h2dep0p75_s01_hyway_20260403']

refidlist=expidlist
wlist=[1.,0.]
legendlist=[\
            'HYway (emi - 1.0 dv)', \
            'HYway (emi - 0.7 dv)', \
#
            'HYway (ctrl - 1.0 dv)', \
            'HYway (ctrl - 0.75 dv)', \
            'HYway (ctrl - 0.7 dv)', \
            'HYway (ctrl - 0.65 dv)', \
#
     
            'HYway (CH4+10%)', \
            'HYway (H2+100Tg/yr)', \
            'HYway (1850)']

smoothlist=[0,0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0,0]
colorlist=[3,4,3,5,4,6,7,8,9]
linestylelist=[0,0,2,2,2,2,0,0,0]
variablelist=['SFH2','DF_H2']
code=generalcode
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




description='typevarcommon'
# 4. HYWAY ONLY
#------------------------------------------------------------------------
#
expidlist=[ \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[\
            'tau1 (ssp2-4.5)', \
            'tau2 (ssp2-4.5)', \
            'tau1 (ssp5-8.5)', \
            'tau2 (ssp5-8.5)']
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
colorlist=[1,2,3,4]
variablelist=['TAU_CH2O','TAU2_CH2O','TAU_CH2O','TAU2_CH2O']
code=generalcode
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 5. HYWAY
#----------------------------------
#
description='varcommon-typevarcommon'

# emih2
variablelist=['emih2']
expidlist=['CESM2-v212_hyway_transient2010s_r1', \
           'EC-Earth3-AerChem_hyway_transient2010s_r1']
#           'UKESM1-0-LL_hyway_transient2010s_r1']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['CESM2', \
            'EC-Earth3']
#            'UKESM1-0-LL']
smoothlist=[0,0]
shiftlist=[0,0]
colorlist=[0,1]
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# dryh2
variablelist=['dryh2']
expidlist=['CESM2-v212_hyway_transient2010s_r1', \
           'EC-Earth3-AerChem_hyway_transient2010s_r1', \
           'EMAC-DLR_hyway_transient2010s_r2', \
           'LMDZ-INCA_hyway_transient2010s_r1', \
           'OsloCTM3v1-2_hyway_transient2010s_r1', \
           'UKESM1-0-LL_hyway_transient2010s_r1']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['CESM2', \
            'EC-Earth3', \
            'EMAC-DLR', \
            'LMDZ-INCA', \
            'OsloCTM3v1-2', \
            'UKESM1-0-LL']
smoothlist=[0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0]
colorlist=[0,1,2,3,4,5]
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)




