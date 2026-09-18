import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout(xrange=[1850,2100])

code='n20260211_noresm2.5_hist'

# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'nhist.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250716', \
           'nhist.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716', \
            \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
            \
#           'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225', \
            \
           'nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07', \
           'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09', \
            \
           'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_ksno04.Olivia.2026-06-23', \
           'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_ksno02.Olivia.2026-06-23', \
           'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnwfall100.Olivia.2026-06-23', \
           'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnw075.Olivia.2026-06-23', \
           'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnwfall300.Olivia.2026-06-23', \
           'nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_phiimushy45.Olivia.2026-06-23', \
            \
           'NHISTfrc2_12_f09_tn14_20191001ext', \
#           'NHISTfrc2_02_f09_tn14_20200427ext', \
            \
           'NHIST_123_f19_tn14_20190625ext']
#           'NHIST_02_f19_tn14_20190801ext', \
#           'NHIST_03_f19_tn14_20190801ext']  
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'b01 (1x1, tuned)', \
            'b01 (2x2, tuned)', \
            'b09 (2x2)', \
#            'b11 (2x2, CO2 emi)', \
            'b19 (2x2)', \
            'b19 (2x2, CO2 emi)', \
#
            'b19 (2x2, ksno04)', \
            'b19 (2x2, ksno02)', \
            'b19 (2x2, rsnwfall100)', \
            'b19 (2x2, rsnw075)', \
            'b19 (2x2, rsnwfall300)', \
            'b19 (2x2, phiimushy45)', \
#
            'NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)']  
#
ensembletypelist=['','','','','','','','','','','','minmax','minmax']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#
colorlist     = [0,1,2, 3,4, 5,6,7,8,9,10, 11,12]
linestylelist = [2,0,0, 0,0, 0,0,0,0,0,0 , 2 ,0 ]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['FSDS', \
              'TREFHT','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
              'tempocn','sssgaocn','sstgaocn']
variablelist=['QREFHT','LHFLX','salngaocn','TREFHT']
#'AODVISdivDAYFOC'

typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# TREFHT 60N90N
freqtype='YEA'
typevarlist=['60N90N']
variablelist=['TREFHT']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

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

# AOD 
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablelist=[\
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
