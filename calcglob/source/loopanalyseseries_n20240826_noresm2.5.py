import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
description='varcommon-typevarcommon'
generalcode='n20240826_noresm2.5'


# 1.a NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
           'n1850.ne30_tn14.hybrid.20240801', \
           'n1850.ne30_tn14.hybrid_coare.20240801', \
           'n1850.ne30_tn14.hybrid.20240808', \
           'n1850.ne30_tn14.hybrid.20240822', \
           'n1850.ne30_tn14.hybrid_fatessp.20241111', \
           'n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241219', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['isopycnic', \
            'hybrid (01)', \
            'hybrid-coare', \
            'hybrid (08)', \
            'hybrid (22)', \
            '20241111', \
            '20241204', \
            '', \
            'CMIP6', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,70,-1199,-1800]
#
colorlist=[0,1,2,4,3,5,6,6,7,8]
#

# tempocn
variablelist=['SWCF','LWCF', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT',\
              'cb_DMS', \
              'U10', \
              'SFisoprene','SFmonoterp', \
              'EMI_SALT_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_SO2_TOT_noresm2','EMI_SO4_TOT_noresm2', \
              'EMI_BC_TOT_noresm3', \
              'EMI_OM_TOT_noresm2', \
              'TREFHT', \
              'FSLNT','FSNTOAC','FSDSC']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.4',colorscheme='keyclim-wp6', xrange=[0.,130.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
# 1.b NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
           'n1850.ne30_tn14.hybrid.20240801', \
           'n1850.ne30_tn14.hybrid_coare.20240801', \
           'n1850.ne30_tn14.hybrid.20240808', \
           'n1850.ne30_tn14.hybrid.20240822', \
           'n1850.ne30_tn14.hybrid_fatessp.20241111', \
           'n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['isopycnic', \
            'hybrid (01)', \
            'hybrid-coare', \
            'hybrid (08)', \
            'hybrid (22)', \
            '20241111', \
            '20241204', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,-1800]
#
colorlist=[0,1,2,4,3,5,6,8]
#

# tempocn
variablelist=['AQSO4_H2O2','AQSO4_O3']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,130.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
# 2. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
           'n1850.ne30_tn14.hybrid.20240801', \
           'n1850.ne30_tn14.hybrid_coare.20240801', \
           'n1850.ne30_tn14.hybrid.20240808', \
           'n1850.ne30_tn14.hybrid.20240822', \
           'n1850.ne30_tn14.hybrid_fatessp.20241111', \
           'n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241219', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['isopycnic', \
            'hybrid (01)', \
            'hybrid-coare', \
            'hybrid (08)', \
            'hybrid (22)', \
            '20241111', \
            '20241204', \
            '', \
            'CMIP6', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,70,-1199,-1800]
#
colorlist=[0,1,2,4,3,5,6,6,7,8]
#

# tempocn
variablelist=['U10', \
              'TREFHT']
typevarlist=['LAND','SEA']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,130.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
# NORESM2.5 [minusGS_DMS] and NORESM2 [SFDMS]
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
           'n1850.ne30_tn14.hybrid.20240801', \
           'n1850.ne30_tn14.hybrid_coare.20240801', \
           'n1850.ne30_tn14.hybrid.20240808', \
           'n1850.ne30_tn14.hybrid.20240822', \
           'n1850.ne30_tn14.hybrid_fatessp.20241111', \
           'n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241219', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['isopycnic', \
            'hybrid (01)', \
            'hybrid-coare', \
            'hybrid (08)', \
            'hybrid (22)', \
            '20241111', \
            '20241204', \
            '', \
            'CMIP6', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,70,-1199,-1800]
#
colorlist=[0,1,2,4,3,5,6,6,7,8]
#

typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,130.])
#
variablelist=['minusGS_DMS','minusGS_DMS','minusGS_DMS','minusGS_DMS','minusGS_DMS','minusGS_DMS','minusGS_DMS','SFDMS','SFDMS','SFDMS']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist)


variablelist=['AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AOD_VISdivDAYFOC','AOD_VISdivDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist)


# NORESM2.5 and NORESM2 [2x2]
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
           'n1850.ne30_tn14.hybrid.20240801', \
           'n1850.ne30_tn14.hybrid_coare.20240801', \
           'n1850.ne30_tn14.hybrid.20240808', \
           'n1850.ne30_tn14.hybrid.20240822', \
           'n1850.ne30_tn14.hybrid_fatessp.20241111', \
           'n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['isopycnic', \
            'hybrid (01)', \
            'hybrid-coare', \
            'hybrid (08)', \
            'hybrid (22)', \
            '20241111', \
            '20241204', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,-1800]
#
colorlist=[0,1,2,4,3,5,6,7]
#

variablelist=['TAU_BC_noresm2','TAU_OM_noresm2','TAU_SULFATE_noresm2','TAU_DUST_noresm2','TAU_SALT_noresm2', \
              'WETDRY_DUST_TOT_noresm2','WETDRY_SALT_TOT_noresm2']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,130.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# NORESM2 [CMIP6] to check SFDMS and minusGS_DMS 
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'N1850_f19_tn14_20190722', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['SFDMS (20241204)', \
            'minusGS_DMS (20241204)', \
            'SFDMS (CMIP6, 2x2)', \
            'minusGS_DMS (CMIP6, 2x2)'] 
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,-1800,-1800]
#
colorlist=[0,1,2,3]
#

variablelist=['SFDMS','minusGS_DMS','SFDMS','minusGS_DMS']
typevarlist=['glob']
#
code=generalcode+'_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist)



