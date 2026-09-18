import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
description='typevarcommon'
generalcode='n20240826_cesm2.5'


# 1. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid.20240822', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722', \
           'n1850mam4.ne30_tn14.hybrid.clmbgc.20240826']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hybrid (22)', \
            'CMIP6', \
            'CMIP6 [2x2]', \
            'mam4']
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,-1199,-1800,0]
#
colorlist=[0,1,2,3]
#

# tempocn
variablelist=['U10','FSLNT']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,10.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon-varcommon',code=code,figlayout=figlayout,colorlist=colorlist)

# 1. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid.20240822', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722', \
           'n1850mam4.ne30_tn14.hybrid.clmbgc.20240826']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hybrid (22)', \
            'CMIP6', \
            'CMIP6 [2x2]', \
            'mam4']
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,-1199,-1800,0]
#
colorlist=[0,1,2,3]
#

# tempocn
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,10.])
# dust emissions
variablelist=['EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','SFdst_a123']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
# dms emissions
variablelist=['minusGS_DMS','SFDMS','SFDMS','OCN_FLUX_DMS']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
# sea-salt emissions
variablelist=['EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','SFncl_a123']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
# sea-salt emissions
variablelist=['AODVIS','AOD_VIS','AOD_VIS','AODVIS']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
# sea-salt emissions
variablelist=['AODVISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AODVIS']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
