import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'NF1850norbc_tropstratchem_f19_f19_20241127_test01', \
           'NF1850norbc_tropstratchem_f19_f19_20241127_test01_bis', \
           'NF1850norbc_tropstratchem_f19_f19_20241127_test16_bis', \
           'NF1850norbc_tropstratchem_f19_f19_t00_20260829', \
           'NF1850norbc_tropstratchem_f19_f19_t01_20260829', \
           'NF1850norbc_tropstratchem_f19_f19_t02_20260829']     
#
legendlist=[ \
            'NorESM2.3 (original tuning)', \
            'NorESM2.3 (original tuning, rerun)', \
            'NorESM2.3 (final tuning)', \
            'NorESM2.3 (final tuning, newer codebase)', \
            'NorESM2.3 (final tuning, newer codebase) - CMIP7 solar/GHGs', \
            'NorESM2.3 (final tuning, newer codebase) - CMIP7 solar/GHGs/emissions']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0]
colorlist     =   [0,1,2,3,4,5]
linestylelist =   [0,2,0,2,0,0]
linewidthlist =   [1,1,1,1,1,1]

#
# tempocn
description='typevarcommon-varcommon'
variablelist=[\
              'cb_O3',\
              'OH_columnburden', \
              'HO2_columnburden', \
              'NO3_columnburden', \
              'O3_columnburden', \
              \
              'NO_CMXF', \
              'NO2_CMXF', \
              \
              'OH_surfacelayer', \
              'HO2_surfacelayer', \
              'NO3_surfacelayer', \
              'O3_surfacelayer']

typevarlist=['glob']
freqtype='YEA'
#
code='n20260905_noresm2.3_cmip7_forcing'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)
