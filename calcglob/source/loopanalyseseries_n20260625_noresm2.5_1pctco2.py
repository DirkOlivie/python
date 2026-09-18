import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()

code='n20260625_noresm2.5_1pctco2'

# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
            'n1pctCO2.ne16pg3_tn14.beta20.2026-06-12', \
            'n1pctCO2-RAD.ne16pg3_tn14.beta20.2026-06-24', \
            'N1PCT_f19_tn14_20190626', \
            'N1PCTfrc2_f09_tn14_20191008']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'b20 (2x2)', \
            'b20 (2x2, RAD)', \
            'NorESM2-LM (1x1)', \
            'NorESM2-MM (2x2)']  
#
ensembletypelist=['','','','']
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,0,0]
#
colorlist     = [0,1,2,3]
linestylelist = [0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['TREFHT','PRECT','ICEFRAC','FSLNT']

typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)


# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# AMOC
freqtype='YEA'
typevarlist=['glob','atlarc']
variablelist=['mmflxdmax26.0Nocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
