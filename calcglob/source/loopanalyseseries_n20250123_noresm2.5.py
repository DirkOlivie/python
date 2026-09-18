import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
description='varcommon-typevarcommon'
generalcode='n20250123_noresm2.5'


# 1.a NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241219', \
           'n1850.ne30_tn14.hybrid_wavparam_fatessp.20241226', \
           'nf2000_ne30pg3_ne30pg3_mtn14_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.dcs600_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.coare_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.clubbc8cesm121_20250124', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['20241204', \
            '', \
            '20241226 (wave)', \
            'nf2000 (clm)', \
            'nf2000', \
            'nf2000 (dcs=600)', \
            'nf2000 (coare)', \
            'nf2000 (clubb-C8=121)', \
            'CMIP6 [1x1]', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,70,0,0,0,0,0,0,-1199,-1800]
#
colorlist=[0,0,1,2,3,4,5,6,7,8]
linestylelist=[0,0,0,0,0,0,0,0,2,2]
#

# tempocn
variablelist=['PRECT', \
              'SFDMS', \
              'SWCF','LWCF', \
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
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.4',colorscheme='keyclim-wp6', xrange=[0.,200.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# 1.b NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_wavparam_fatessp.20241226', \
           'nf2000_ne30pg3_ne30pg3_mtn14_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.dcs600_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.coare_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.clubbc8cesm121_20250124', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['20241204', \
            '20241226 (wave)', \
            'nf2000 (clm)', \
            'nf2000', \
            'nf2000 (dcs=600)', \
            'nf2000 (coare)', \
            'nf2000 (clubb-C8=121)', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,-1800]
#
colorlist=[0,1,2,3,4,5,6,8]
#
linestylelist=[0,0,0,0,0,0,0,2]

# tempocn
variablelist=['AQSO4_H2O2','AQSO4_O3']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,200.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# 2. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241219', \
           'n1850.ne30_tn14.hybrid_wavparam_fatessp.20241226', \
           'nf2000_ne30pg3_ne30pg3_mtn14_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.dcs600_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.coare_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.clubbc8cesm121_20250124', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['20241204', \
            '', \
            '20241226 (wave)', \
            'nf2000 (clm)', \
            'nf2000', \
            'nf2000 (dcs=600)', \
            'nf2000 (coare)', \
            'nf2000 (clubb-C8=121)', \
            'CMIP6 [1x1]', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,70,0,0,0,0,0,0,-1199,-1800]
#
colorlist=[0,0,1,2,3,4,5,6,7,8]
#
linestylelist=[0,0,0,0,0,0,0,0,2,2]

# tempocn
variablelist=['U10', \
              'TREFHT']
typevarlist=['LAND','SEA']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,200.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#

# NORESM2.5 [minusGS_DMS] and NORESM2 [SFDMS]
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_fatessp.20241219', \
           'n1850.ne30_tn14.hybrid_wavparam_fatessp.20241226', \
           'nf2000_ne30pg3_ne30pg3_mtn14_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.dcs600_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.coare_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.clubbc8cesm121_20250124', \
           'N1850frc2_f09_tn14_20191001', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['20241204', \
            '', \
            '20241226 (wave)', \
            'nf2000 (clm)', \
            'nf2000', \
            'nf2000 (dcs=600)', \
            'nf2000 (coare)', \
            'nf2000 (clubb-C8=121)', \
            'CMIP6 [1x1]', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,70,0,0,0,0,0,0,-1199,-1800]
#
colorlist=[0,0,1,2,3,4,5,6,7,8]
#
linestylelist=[0,0,0,0,0,0,0,0,2,2]

typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,200.])
#
variablelist=['AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




# NORESM2.5 and NORESM2 [2x2]
#------------------------------------------------------------------------
#
expidlist=['n1850.ne30_tn14.hybrid_fatessp.20241204', \
           'n1850.ne30_tn14.hybrid_wavparam_fatessp.20241226', \
           'nf2000_ne30pg3_ne30pg3_mtn14_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp_20250120', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.dcs600_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.coare_20250124', \
           'nf2000_ne30pg3_ne30pg3_mtn14.fatessp.clubbc8cesm121_20250124', \
           'N1850_f19_tn14_20190722']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['20241204', \
            '20241226 (wave)', \
            'nf2000 (clm)', \
            'nf2000', \
            'nf2000 (dcs=600)', \
            'nf2000 (coare)', \
            'nf2000 (clubb-C8=121)', \
            'CMIP6 [2x2]']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,-1800]
#
colorlist=[0,1,2,3,4,5,6,8]
#
linestylelist=[0,0,0,0,0,0,2,2]


variablelist=['TAU_BC_noresm2','TAU_OM_noresm2','TAU_SULFATE_noresm2','TAU_DUST_noresm2','TAU_SALT_noresm2', \
              'WETDRY_DUST_TOT_noresm2','WETDRY_SALT_TOT_noresm2']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6', xrange=[0.,200.])
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


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
linestylelist=[0,0,0,0]

variablelist=['SFDMS','minusGS_DMS','SFDMS','minusGS_DMS']
typevarlist=['glob']
#
code=generalcode+'_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



