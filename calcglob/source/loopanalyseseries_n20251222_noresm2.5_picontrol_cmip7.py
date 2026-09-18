import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[800.,900.])

code='n20251222_noresm2.5_picontrol_cmip7'
#
# 1. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
           'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
legendlist=[ \
            'b12 (2x2, #365)', \
            'b12 (2x2, ref)', \
            'b12 (2x2, cmip7)', \
            'b12 (2x2, ghg+cmip7)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
colorlist     =   [0,1,2,3]
linestylelist =   [0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=[\
              'SOLIN', \
              'FSDS','FSDSC', \
              'PRECC','PRECL', \
              'TREFHT','QREFHT','LHFLX','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
              'tempocn','sssgaocn','sstgaocn','salngaocn', \
              'cb_DMS','cb_SO2','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'AODVISdivDAYFOC']
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

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 2. 
#------------------------------------------------------------------------
#
expidlist=[ \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
           'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
legendlist=[ \
            'b12 (2x2, ref)', \
            'b12 (2x2, cmip7)', \
            'b12 (2x2, ghg+cmip7)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0]
shiftlist=[0,0,0]
colorlist     =   [1,2,3]
linestylelist =   [0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=[\
              'SFBC_N','SFBC_AX','SFBC_NI', \
              'SFOM_NI', \
              'SFSO2','SFSO4_PR', \
              'BC_N_CMXF','BC_AX_CMXF','BC_NI_CMXF', \
              'OM_NI_CMXF', \
              'SO2_CMXF','SO4_PR_CMXF', \
              'H2O_CMXF', \
              'AODVVOLCdivDAYFOC', 'ABSVVOLCdivDAYFOC', \
              'DOD550divDAYFOC', \
              'EMI_BC_TOT_noresm2', 'EMI_OM_TOT_noresm2','EMI_SO2_TOT_noresm2','EMI_SO4_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2', 'EMI_DUST_TOT_noresm2', 'EMI_SALT_TOT_noresm2', \
              'TAU_DMS','TAU_isoprene','TAU_monoterp','TAU_SOA_SV','TAU_SOA_LV', \
              'TAU_BC_noresm2','TAU_OM_noresm2','TAU_SULFATE_noresm2','TAU_DUST_noresm2','TAU_SALT_noresm2']
               
typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
