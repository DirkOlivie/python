import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708ext', \
           'nco2x4.ne30pg3_tn14.noresm3_0_beta01_650dcs_4p0clubbc8_0p5dust.20250715', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext', \
           'nco2x4.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250710', \
            \
           'N1850_f19_tn14_20190621ext', \
           'NCO2x4_f19_tn14_20190624ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'b01 (1x1)', \
            'b01 (1x1, 4xCO2)', \
            'b01 (2x2)', \
            'b01 (2x2, 4xCO2)', \
            'NorESM2-LM (2x2)', \
            'NorESM2-LM (2x2, 4xCO2)']  
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,-1600+50+1,50]
#
colorlist     = [1,1,2,2,3,3]
linestylelist = [0,2,0,2,0,2]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['TREFHT','FSLNT','SWCF','LWCF','PRECT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
              'tempocn']
typevarlist=['glob']
freqtype='YEA'
#
code='n20250814_noresm2.5_4xco2cmip6'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 'AODVISdivDAYFOC'
variablelist=['AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

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
