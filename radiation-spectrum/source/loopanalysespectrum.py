import loopanalysespectrum2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#----------

#figlayout=cfiglayout.CFigLayout(xrange=[0,2000])
figlayout=cfiglayout.CFigLayout(xtype='log', ytype='log')

setlist=[ {'var': 'SSI' , 'origin' : 'ClimateDataRecord', 'wvlresolution' : 'standard', 'year0' : 1850, 'year1' : 2021, 'temperature': 5777, 'prefactor' : None}, \
          {'var': 'SSI' , 'origin' : 'AeroTab'          , 'wvlresolution' : None      , 'year0' : None, 'year1' : None, 'temperature': 5777, 'prefactor' : None}, \
          {'var': 'BBI' , 'origin' : 'SP2006'           , 'wvlresolution' : None      , 'year0' : None, 'year1' : None, 'temperature': 5777, 'prefactor' : 1./47000.}  \
          ]
        
legendlist=['CDR', 'AeroTab','Black body']
shiftlist=[0,0,0]
smoothlist=[0,0,0]
colorlist=[0,1,2]
linestylelist=[0,0,0]
code='n20251026_volc_spectrum'

loopanalysespectrum2.loopanalysespectrum2(setlist=setlist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, code=code, figlayout=figlayout, colorlist=colorlist, linestylelist=linestylelist)
