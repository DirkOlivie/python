import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()
code='n20260329_noresm2.5_cmip7frc'


# 1. CMIP6 (kjetil) , CMIP6 (Dirk) , CMIP7 , CMIP7 + GHG
#------------------------------------------------------------------------
#
expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
           'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['CMIP6', \
            'CMIP6 (+output)', \
            'CMIP7', \
            'GHG+CMIP7']
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
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['TREFHT','FSLNT','SWCF','LWCF','PRECT', \
              'SFDMS', 'SFSO2', 'SFisoprene','SFmonoterp',
              'EMI_BC_TOT_noresm2', 'EMI_OM_TOT_noresm2', 'EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2', \
              'AODVISdivDAYFOC',
              'U10', \
              'tempocn']
typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


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
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
#
# 2. Volcanicd AOD
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
           'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'CMIP6 (+output)', \
            'CMIP7', \
            'GHG+CMIP7']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist     = [1,2,3]
linestylelist = [0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['AODVVOLCdivDAYFOC']
typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# 3. CMIP7+GHG : surfacelayer
#-----------------------------------
expidlist=[ \
           'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'GHG+CMIP7']
#
smoothlist=[0]
#
shiftlist=[0]
#
colorlist     = [3]
linestylelist = [0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['CO2_surfacelayer','CH4_surfacelayer','N2O_surfacelayer','CFC11_surfacelayer','CFC12_surfacelayer']
typevarlist=['glob']
freqtype='seasonalcycle'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
