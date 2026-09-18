import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()
figlayoutlog=cfiglayout.CFigLayout(ytype='log')


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850.ne30_tn14.noresm3_0_alpha03d.20250528', \
           'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            '03d', \
            '03d (ghg)']
#
smoothlist=[0,0]
#
shiftlist=[0,0]
#
colorlist=[0,1]
linestylelist=[0,0]
#

# annual
description='typevarcommon-varcommon'
variablelist=['FSLNT','SWCF','LWCF','TREFHT','PRECT', \
              'CLDLOW','CLDMED','CLDHGH','CLDTOT'] 
typevarlist=['glob']
freqtype='YEA'
#
code='n20250611_noresm2.5_ghg'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# monthtly
variablelist=['cb_BC_AX']
freqtype='monthly'
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayoutlog,colorlist=colorlist,linestylelist=linestylelist)
