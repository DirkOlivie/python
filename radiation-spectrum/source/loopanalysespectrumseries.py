import loopanalysespectrumseries2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#----------

figlayout=cfiglayout.CFigLayout()

setlist=[ {'var': 'TSI', 'origin' : 'ClimateDataRecord', 'wvlresolution' : 'standard'} ]
legendlist=['ClimateDataRecord']
freqtype='YEA'
shiftlist=[0]
smoothlist=[0]
colorlist=[0]
linestylelist=[0]
code='n20251026_tsi'

loopanalysespectrumseries2.loopanalysespectrumseries2(setlist=setlist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtype=freqtype, code=code, figlayout=figlayout, colorlist=colorlist, linestylelist=linestylelist)
