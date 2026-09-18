import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

#
typevarlist=['glob']
wlist=[1.,0.]
description='typevarcommon'
figlayout=cfiglayout.CFigLayout()
freqtypelist=['YEA']
#
# 1.1 emission driven : various RATES in one figure
#--------------------------------------------------
#
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,1]
linestylelist=[0,2,0]
#
variablegrouplist=[['ch4_surfacelayer','CH4_SRF','CH4_SRF'], \
                   ['o3_surfacelayer','O3_SRF','O3_SRF']]
legendlist=['CNRM-ESM2-1 (emi-driven)', \
            'NorESM2-LM-C (conc-driven)', \
            'NorESM2-LM-C (emi-driven)']
code='n20250526_esm2025_ch4_amip_multimodel'

for variablelist in variablegrouplist :
    for freqtype in freqtypelist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




