import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['N1850_f19_tn14_20190621', \
           'NHIST_f19_tn14_20190625ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['n1850 (2x2)', \
            'nhist (2x2)']
#
smoothlist=[0,0]
#
shiftlist=[250,0]
#
colorlist     = [0,1]
linestylelist = [0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['AODVVOLCdivDAYFOC','ABSVVOLCdivDAYFOC','BVISVOLC_columnburden']
typevarlist=['glob']
freqtype='YEA'
#
code='n20251026_volc'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
