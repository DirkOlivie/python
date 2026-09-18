import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon'
generalcode='n20231026_noresm2.5_refactor'


# ALL VARIABLES (except ozone)
#------------------------------------------------------------------------
#
expidlist=[ \
            'NF2000oslo.f19_f19_mtn14.2', \
            'NF2000oslo.f19_f19_mtn14.3', \
            'NF2000oslo.f19_f19_mtn14.3.bug'] 
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['mtn14.2', \
            'mtn14.3', \
            'mtn14.3.bug']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#

# tempocn no PRECT
variablelist=[ \
            'AOD_VISdivDAYFOC', \
              'TREFHT','SWCF','LWCF','U10', \
#              'SFDMS','SFisoprene','SFmonoterp', \
#              'cb_DMS','cb_SO2','cb_H2SO4','cb_isoprene','cb_monoterp', \
#              'EMI_BC_TOT_noresm2','EMI_OM_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SO2_TOT_noresm2', \
#              'SFSS_A1','SFSS_A2','SFSS_A3', \
              'cb_SULFATE','cb_DUST','cb_SALT','cb_BC','cb_OM', \
              'cb_BC_N','cb_BC_NI','cb_BC_A','cb_BC_AI','cb_BC_AX','cb_BC_AC', \
              'cb_OM_NI','cb_OM_AI','cb_OM_AC','cb_SOA_NA','cb_SOA_A1', \
              'cb_SO4_A1','cb_SO4_A2','cb_SO4_AC','cb_SO4_NA','cb_SO4_PR', \
#              'SFBC_N','SFBC_NI','SFBC_AX', \
#              'SFOM_NI', \
#              'TAU_DMS','TAU_isoprene','TAU_monoterp', \
#              'DRY_SULFATE_TOT_noresm2','DRY_DUST_TOT_noresm2','DRY_SALT_TOT_noresm2','DRY_BC_TOT_noresm2','DRY_OM_TOT_noresm2', \
#              'WET_SULFATE_TOT_noresm2','WET_DUST_TOT_noresm2','WET_SALT_TOT_noresm2','WET_BC_TOT_noresm2','WET_OM_TOT_noresm2', \
              'TAU_SULFATE_noresm2','TAU_DUST_noresm2','TAU_SALT_noresm2','TAU_BC_noresm2','TAU_OM_noresm2', \
              'BC_NclcoagTend','BC_AclcoagTend','BC_NIclcoagTend','BC_AIclcoagTend','BC_AXclcoagTend','BC_AC_OCWclcoagTend', \
              'OM_AC_OCWclcoagTend', \
              'SO4_NAclcoagTend','SO4_A1clcoagTend','SO4_A2_OCWclcoagTend', \
              'CDNUMC','CCN1_columnburden','CCN2_columnburden','CCN3_columnburden','CCN4_columnburden','CCN5_columnburden','CCN6_columnburden','CCN7_columnburden', \
              'N_AER_columnburden']
#              'cb_BC_AC_OCW'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
