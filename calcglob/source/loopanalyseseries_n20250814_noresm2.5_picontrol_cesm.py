import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout(xrange=[0.,300.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513', \
            \
           'n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708ext', \
           'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext', \
            \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
           'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152', \
           'b.e30_beta06.B1850C_LTso.ne30_t232_wgx3.192', \
            \
           'n1850.ne16_tn14.noresm3_0_beta02-run1_yr001.20250825']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['a03b (1x1)', \
            'b01 (1x1, tuned)', \
            'b01 (2x2, tuned)', \
            'NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
            'CESM3 (1x1, 152)', \
            'CESM3 (1x1, 192)', \
            'b02 (2x2)']
          
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,-1199,-1599,280,280,0]
#
colorlist     = [0,1,2,3,4,5,6,7]
linestylelist = [0,0,2,0,2,0,0,2]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['FSDS', 'FSDSC', \
              'TREFHT','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
#              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp',
              'U10']
#              'tempocn','sssgaocn','sstgaocn']
#             'AODVISdivDAYFOC'
typevarlist=['glob']
freqtype='YEA'
#
code='n20250814_noresm2.5_picontrol_cesm'
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
variablelist=['AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC', \
              'AODVISdivDAYFOC']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

#
variablegrouplist=[['SFDMS','SFDMS','SFDMS','SFDMS','SFDMS','OCN_FLUX_DMS','OCN_FLUX_DMS','SFDMS'], \
                   ['EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','SFdst_a123','SFdst_a123','EMI_DUST_TOT_noresm2'], \
                   ['EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','SFncl_a123','SFncl_a123','EMI_SALT_TOT_noresm2']]
for variablelist in variablegrouplist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
