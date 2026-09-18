import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()

code='n20260422_noresm2.5_hist_so2oh'

# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'nhist.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250716', \
           'nhist.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716', \
            \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2', \
            \
#           'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225', \
            \
           'NHISTfrc2_123_f09_tn14_20191001ext', \
#           'NHISTfrc2_f09_tn14_20191001ext', \
#           'NHISTfrc2_02_f09_tn14_20200427ext', \
#           'NHISTfrc2_03_f09_tn14_20200519ext', \
            \
           'NHIST_123_f19_tn14_20190625ext']
#           'NHIST_f19_tn14_20190625ext', \
#           'NHIST_02_f19_tn14_20190801ext', \
#           'NHIST_03_f19_tn14_20190801ext']  
#
refidlist=expidlist
#
ensembletypelist=['minmax']*6
#
wlist=[1.,0.]
#
legendlist=[ \
            'b01 (1x1, tuned)', \
            'b01 (2x2, tuned)', \
            'b09 (2x2)', \
            'b09 (2x2, SO2+OH)', \
#            'b11 (2x2, CO2 emi)', \
            'NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)']  
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0]
#
colorlist     = [0,1,2,3,4,5]
linestylelist = [2,0,0,0,0,2]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['TREFHT','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
#            'tempocn','sssgaocn','sstgaocn', \
              'SO2_SRF', \
              'TREFHT']
#'AODVISdivDAYFOC'

typevarlist=['glob','LAND']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)


# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# AMOC
freqtype='YEA'
typevarlist=['glob','atlarc']
variablelist=['mmflxdmax26.0Nocn']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# AOD 
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablelist=[\
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
