import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[1000.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[1350.,1700.])
figlayout=cfiglayout.CFigLayout(xrange=[1530.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[ 925.,1800.])
figlayout=cfiglayout.CFigLayout(xrange=[1450.,1650.])
figlayout=cfiglayout.CFigLayout(xrange=[1476.,1485.])


# GLOBAL MEAN : COLUMN BURDEN, SURFACE CONCENTRATION
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850esmGaxg.n30b23LM.508.20260824', \
           'n1850esmGaxgGHG.LM.n30b24.20260916']  
#
legendlist=[ \
            'b23 (#507)', \
            'b24 (GHG)'] 
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0]
shiftlist=[0,0]
colorlist     =   [0,1]
linestylelist =   [2,2]
linewidthlist =   [1,1]

#
# tempocn
description='typevarcommon-varcommon'
variablelist=[\
              'CO2_surfacelayer', \
              'TMCO2']  
typevarlist=['glob']
freqtype='monthly'
#
code='n20260903_noresm2.5_picontrol_co2'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)


# NH, TROPICS, SH : COLUMN BURDEN, SURFACE CONCENTRATION
#------------------------------------------------------------------------
#
expidlist= \
           ['n1850esmGaxg.n30b23LM.508.20260824']*3 \
          +['n1850esmGaxgGHG.LM.n30b24.20260916']*3 \
#
legendlist=[ \
            'b23 (#507, NH)', \
            'b23 (#507, tropics)', \
            'b23 (#507, SH)', \
            'b24 (GHG, NH)', \
            'b24 (GHG, tropics)', \
            'b24 (GHG, SH)'] 
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0]
colorlist     =   [0,0,0,1,1,1]
linestylelist =   [0,1,2,0,1,2]
linewidthlist =   [1,1,1,1,1,1]

#
# tempocn
description='varcommon'
variablelist=[\
              'CO2_surfacelayer', \
              'TMCO2']  
typevarlist=['NH','28S28N','SH','NH','28S28N','SH']
freqtype='monthly'
#
code='n20260903_noresm2.5_picontrol_co2_zonal'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)


# NH, TROPICS, SH : COLUMN BURDEN, SURFACE CONCENTRATION
#------------------------------------------------------------------------
#
expidlist= \
          ['n1850esmGaxgGHG.LM.n30b24.20260916']*3
#
legendlist=[ \
            'b24 (GHG, NH)', \
            'b24 (GHG, tropics)', \
            'b24 (GHG, SH)'] 
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0,0]
shiftlist=[0,0,0]
colorlist     =   [1,1,1]
linestylelist =   [0,1,2]
linewidthlist =   [1,1,1]

#
# tempocn
description='varcommon'
variablelist=[\
              'CO2_surfacelayer', \
              'TMCO2']  
typevarlist=['NH','28S28N','SH']
freqtype='monthly'
#
code='n20260903_noresm2.5_picontrol_co2_zonal_ghgonly'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)


# GLOBAL EMISSIONS
#------------------------------------------------------------------------
#
expidlist= \
          ['n1850esmGaxgGHG.LM.n30b24.20260916']*4
#
legendlist=[ \
            'b24 (GHG) - total', \
            'b24 (GHG) - land', \
            'b24 (GHG) - ocean', \
            'b24 (GHG) - fossil fuel']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
colorlist     =   [0,1,2,3]
linestylelist =   [2,2,2,2]
linewidthlist =   [1,1,1,1]

#
# tempocn
description='typevarcommon'
variablelist=[\
              'SFCO2','SFCO2_LND','SFCO2_OCN','SFCO2_FFF']  
typevarlist=['']
freqtype='monthly'
#
code='n20260903_noresm2.5_picontrol_co2_speciated'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)




