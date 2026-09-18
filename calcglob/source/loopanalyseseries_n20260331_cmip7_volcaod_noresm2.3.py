import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
code='n20260331_cmip7_volcaod_noresm2.3'
figlayout=cfiglayout.CFigLayout()



# I. IMPOSE SIMULATIONS + TEST SIMULATIONS
#-----------------------

expidlist=[ \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip6', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7wghtavg', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone']
#
refidlist=[ \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone']
wlist=[1.,-1.]
legendlist=[ \
            'CMIP6', \
            'CMIP7', \
            'CMIP7-weighted', \
            'none']
#
smoothlist=[0,0,0,0]
colorlist=[0,1,2,3]
linestylelist=[0,0,0,0]
shiftlist=[0,0,0,0]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['AOD_VISdivDAYFOC', \
#             'DOD550divDAYFOC', \      
              'AODVVOLCdivDAYFOC', \
              'ABSVVOLCdivDAYFOC', \
              'FSDS','FSDSC', \
              'FSNT','FSNTC', \
              'FLNT','FLNTC', \
              'FSLNT','FSLNTC'] 
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
