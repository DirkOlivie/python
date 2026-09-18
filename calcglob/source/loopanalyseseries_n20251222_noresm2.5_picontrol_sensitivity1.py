import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout(xrange=[230.,300.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.clubb_c_k10h.20260112', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.combined_176.20260112', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.combined_176.20260119', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.hetfrz_dust_scalfac.20260112', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.zmconv_c0_lnd.20260112', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.zmconv_c0_lnd_ocn.20260112', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.zmconv_c0_lnd_ocn.20260119']
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
             \
            'b09 (2x2)', \
             \
            'b09 (2x2, clubb_c_k10h)', \
            'b09 (2x2, combined_176)', \
            'b09 (2x2, combined_176)', \
            'b09 (2x2, hetfrz_dust_scalfac)', \
            'b09 (2x2, zmconv_c0_lnd)', \
            'b09 (2x2, zmconv_c0_lnd_ocn)', \
            'b09 (2x2, zmconv_c0_lnd_ocn)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0, 0,0,0,0,0,0,0]
#
shiftlist=[-1199,-1599, 0, 0,0,0,0,0,0,0]
#
colorlist     =   [0,1, 2, 3,4,5,6,7,8,9]
linestylelist =   [2,0, 0, 0,0,0,0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['SOLIN', \
              'FSDS','FSDSC', \
              'PRECC','PRECL', \
              'TREFHT','QREFHT','LHFLX','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
              'tempocn','sssgaocn','sstgaocn','salngaocn', \
              'cb_DMS','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT']
#             'AODVISdivDAYFOC'
typevarlist=['glob']
freqtype='YEA'
#
code='n20251222_noresm2.5_picontrol_sensitivity1'
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

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# AOD 
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablelist=[\
#             'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC', \
              'AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']


loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
