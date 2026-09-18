import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

# imbalance cicero

# 1. simulation with OPOM output for EMEP
#----------------------------------------
expidlist=['NFHISTnorpddmsbcsdyn_standard_opom_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_standard_opom_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_standard_opom_f09_mg17_20210226']
refidlist=expidlist
wlist=[1.,0.]
smoothlist=[0,0,0]       
shiftlist=[0,0,0]
variablelist=['SFDMS','emidmsocean','emipomocean']
legendlist=variablelist
code='n20231107_opom_emep'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
description=''
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
