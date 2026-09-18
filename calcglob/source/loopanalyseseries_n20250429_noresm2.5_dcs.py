import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
figlayout=cfiglayout.CFigLayout(xrange=[0.,60.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[\
           'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408', \
           'n1850.ne30_tn14.hybrid_fates-nocomp_spinup.3.0a02.20250415']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM3 (3.0a02, DCS=500/600)', \
            'NorESM3 (3.0a02, DCS=600)']
#
smoothlist=[0,0]
#
shiftlist=[0,0]
#
colorlist=[0,1]
linestylelist=[0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['NUMICE_columnburden']
typevarlist=['glob']
#
code='n20250429_noresm2.5_cesm3_dcs'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

