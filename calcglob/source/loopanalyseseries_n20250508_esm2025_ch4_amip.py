import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

#
typevarlist=['glob']
#
# DF_CH4
#----------------------------------
#
description='varcommon-typevarcommon'
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s02_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s03_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506'] 
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0]
#            
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#
variablelist=['DF_CH4']
legendlist=['CH4 drydep x 0.00', \
            'CH4 drydep x 0.05', \
            'CH4 drydep x 0.05']
#
code='n20250508_esm2025_ch4_amip'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
# cb_CH4, CH4_SRF
#----------------------------------
#
description='varcommon-typevarcommon'
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s02_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s03_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506'] 
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0]
#            
shiftlist=[0,0,0,0]
#
colorlist=[0,1,2,3]
#
variablelist=['cb_CH4','CH4_SRF']
legendlist=['no CH4 drydep', \
            'CH4 drydep x 0.00', \
            'CH4 drydep x 0.05', \
            'CH4 drydep x 0.05']
#
code='n20250508_esm2025_ch4_amip'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
