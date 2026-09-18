import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708ext', \
           'nhist.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250716', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext', \
           'nhist.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['b01-tuned n1850 (1x1)', \
            'b01-tuned nhist (1x1)', \
            'b01-tuned n1850 (2x2)', \
            'b01-tuned nhist (2x2)']  
#
smoothlist=[0,0,0,0]
#
shiftlist=[1850-50-1,0,1850-50-1,0]
#
colorlist     = [0,1,2,3]
linestylelist = [1,0,1,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['TREFHT','FSLNT','SWCF','LWCF','PRECT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','AODVISdivDAYFOC','SFisoprene','SFmonoterp','U10', \
              'tempocn']
typevarlist=['glob']
freqtype='YEA'
#
code='n20250709_noresm2.5_hist'
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
