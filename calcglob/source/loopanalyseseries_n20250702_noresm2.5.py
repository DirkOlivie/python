import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513', \
           'n1850.ne30_tn14.noresm3_0_alpha07.20250628', \
           'n1850.ne30_tn14.noresm3_0_beta01.20250629', \
           'n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh.20250630', \
           'n1850.ne16pg3_tn14.noresm3_0_alpha07.20250701', \
           'n1850.ne16pg3_tn14.noresm3_0_beta01.20250701', \
           'n1850.ne16pg3_tn14.noresm3_0_beta01.20250704']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['a03b', \
            'a07', \
            'b01', \
            'b01 (no LH)', \
            'a07 (2x2)', \
            'b01 (2x2)', \
            'b01 (2x2, sip)']
#
smoothlist=[0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0]
#
colorlist     = [0,1,2,3,1,2,2]
linestylelist = [0,0,0,0,2,2,1]
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
code='n20250702_noresm2.5'
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
