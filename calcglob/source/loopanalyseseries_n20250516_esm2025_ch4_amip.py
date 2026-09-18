import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

#
typevarlist=['glob']
wlist=[1.,0.]
description='typevarcommon'
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7',title='CH'+r'$_4$'+' fluxes/rates')
freqtypelist=['YEA']
#
# 1.1 emission driven : various RATES in one figure
#--------------------------------------------------
#
nexpid=7
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506']*nexpid
refidlist=expidlist
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,2,3,4,5,6]
linestylelist=[0,0,0,0,0,0,0]
#
variablelist=['SFCH4', \
              'DF_CH4', \
               \
              'r_jch4_ab_columnburden', \
              'r_CH4_OH_columnburden', \
              'r_CL_CH4_columnburden', \
              'r_F_CH4_columnburden', \
              'r_O1D_CH4abc_columnburden']
legendlist=variablelist
code='n20250516_esm2025_ch4_amip_emisdriv_rates'
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# 1.2 concentration driven : various RATES in one figure
#-------------------------------------------------------
#
nexpid=5
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506']*nexpid
refidlist=expidlist
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[2,3,4,5,6]
linestylelist=[0,0,0,0,0]
#
variablelist=['r_jch4_ab_columnburden', \
              'r_CH4_OH_columnburden', \
              'r_CL_CH4_columnburden', \
              'r_F_CH4_columnburden', \
              'r_O1D_CH4abc_columnburden']
legendlist=variablelist
code='n20250516_esm2025_ch4_amip_concdriv_rates'
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
#
# 1.3 emis + conc driven : various RATES in one figure
#-----------------------------------------------------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
            \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506']
nexpid=len(expidlist)
refidlist=expidlist
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,2,3,4,5,6,7,2,3,4,5,6,7]
linestylelist=[0,0,0,0,0,0,0,0,2,2,2,2,2,2]
#
variablelist=['SFCH4', \
              'DF_CH4', \
               \
              'r_jch4_ab_columnburden', \
              'r_CH4_OH_columnburden', \
              'r_CL_CH4_columnburden', \
              'r_F_CH4_columnburden', \
              'r_O1D_CH4abc_columnburden', \
              'r_CH4_OH_columnburden_belowtropopause', \
               \
              'r_jch4_ab_columnburden', \
              'r_CH4_OH_columnburden', \
              'r_CL_CH4_columnburden', \
              'r_F_CH4_columnburden', \
              'r_O1D_CH4abc_columnburden', \
              'r_CH4_OH_columnburden_belowtropopause']
legendlist=variablelist
code='n20250516_esm2025_ch4_amip_emisconcdriv_rates'
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
#
# 2.
description='varcommon-typevarcommon'

# 2.1 emis-driven + conc-driven
#------------------------------
figlayout=cfiglayout.CFigLayout(title='')
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506']
legendlist=['emission-driven', \
            'concentration-driven'] 
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1]
linestylelist=[0,2]
#
variablelist=['CH4_SRF', \
              'cb_CH4', \
              'r_jch4_ab_columnburden', \
              'r_CH4_OH_columnburden', \
              'r_CL_CH4_columnburden', \
              'r_F_CH4_columnburden', \
              'r_O1D_CH4abc_columnburden',\
              'r_CH4_OH_columnburden_belowtropopause']
code='n20250516_esm2025_ch4_amip_emisconcdriv'
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 2.2 emis-driven
#----------------
figlayout=cfiglayout.CFigLayout(title='')
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506']
legendlist=['emission-driven']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0]
linestylelist=[0]
#
variablelist=['SFCH4', \
              'DF_CH4', \
              'TAU_CH4_CHMDRY', \
              'TAU_CH4_OHTROP']
code='n20250516_esm2025_ch4_amip_emisdriv'
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)





