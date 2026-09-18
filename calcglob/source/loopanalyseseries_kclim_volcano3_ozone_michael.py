import loopanalyseseries2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

typevarlist=['glob','90S28SLAND','90S28S','28S28N','28N60N','60N90N']
#freqtype='annavg'
freqtype='YEA'
#freqtype='monthly'
description='varcommon'
#xrange=[1990,1995]
xrange=[1980,2014]

figlayout=cfiglayout.CFigLayout(xrange=xrange, legendlocation='outside1.4')

# 1 degree
#---------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test12', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test13', \
            \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'no volcanic emis.', \
            'SO2 100%/SO4 0%', \
            'SO2 90%/SO4 10%', \
            'SO2 0%/SO4 100%', \
             \
            'CESM 2x2', \
            'CESM 2x2', \
            'CESM 1x1']
smoothlist=[0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0]
code='kclim_ozone_volcano_michael_f09'
#
variablelist=['cb_O3','O3_layer06']
for typevar in typevarlist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)


# 2 degree
#---------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test12', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
            \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]

legendlist=[ \
            'no volcanic emis.', \
            'SO2 100%/SO4 0%', \
            'SO2 97.5%/SO4 2.5%', \
            'SO2 95%/SO4 5%', \
            'SO2 90%/SO4 10%', \
            'SO2 80%/SO4 20%', \
            'SO2 50%/SO4 50%', \
            'SO2 0%/SO4 100%', \
            'SO2 0%/SO4 100% (na)', \
             \
            'CESM 2x2', \
            'CESM 2x2', \
            'CESM 1x1']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
code='kclim_ozone_volcano_michael_f19'
#
variablelist=['cb_O3','O3_layer06']
for typevar in typevarlist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 3. temperature evolution
#-------------------------
#
xrange=[1970,2015]
figlayout=cfiglayout.CFigLayout(xrange=xrange)
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
            \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['f19', \
            'f19 - no volc. emis.', \
            'f09', \
            'f09 - no volc. emis.', \
            'f19 - cesm', \
            'f19 - cesm', \
            'f09 - cesm']
#

smoothlist=[0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0]
#
code='kclim_ozone_volcano_michael_f19'
#
variablelist=['TREFHT']
#
typevarlist=['glob','SEA']
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
