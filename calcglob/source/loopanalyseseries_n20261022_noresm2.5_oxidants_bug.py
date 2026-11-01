import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850GHGGaxg.LM.nor30b27.002.20261016', \
           'n1850GHGGaxg.LM.nor30b27.002.20261022.oxidtest']
#
legendlist=['old', \
            'new']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0]
shiftlist=[0,0]
colorlist     =   [0,1]
linestylelist =   [0,0]
linewidthlist =   [2,2]

#
# tempocn
description='typevarcommon-varcommon'
variablelist=[\
              'cb_SULFATE', \
              'isoprene_surfacelayer', \
              'DMS_surfacelayer', \
              'SO2_surfacelayer', \
              'AODVISdivDAYFOC']
typevarlist=['glob','SEA','LAND','NAM','SAM','NAF','SAF','SA','EA','IND','AUS','NEUR','SEUR','EUR','MED','USW','USE','US','CHN','CHNW','CHNE']
#
code='n20261022_noresm2.5_oxidants_bug'
#
figlayout=cfiglayout.CFigLayout(xrange=[-5,55])
freqtype='YEA'
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)
#
figlayout=cfiglayout.CFigLayout()
freqtype='seasonalcycle'
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)
#
figlayout=cfiglayout.CFigLayout(xrange=[-5,55])
variablelist=['tempocn']
typevarlist=['glob']
freqtype='YEA'
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)
