import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon'
generalcode='n20230801_keyclim_wp6'


# ALL VARIABLES (except ozone)
#------------------------------------------------------------------------
#
expidlist=[ \
           'histssp585', \
           'histssp585-cloud2', \
           'histssp585-eddy', \
           'histssp585-iceSheet3', \
           'histssp585-ozone', \
           'histssp585-snow', \
           'histssp585-piAerOxid', \
           'histssp370-piAerOxid']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Cloud', \
            'Eddy', \
            'IceSheet', \
            'Ozone', \
            'Snow', \
            'piAerOxid', \
            ''] 
#
#smoothlist=[0,0,0,0,0,0,0,0]
smoothlist=[5,5,5,5,5,5,5,5]
#
shiftlist=[0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6,6]
#

# tempocn
variablelist=['tempocn', \
#              'TREFHT','PRECT','SWCF','LWCF','PRECT','U10', \
#              'SFDMS','SFisoprene','SFmonoterp', \
#              'cb_DMS','cb_SO2','cb_H2SO4','cb_isoprene','cb_monoterp', \
#              'EMI_BC_TOT_noresm2','EMI_OM_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SO2_TOT_noresm2', \
#              'SFSS_A1','SFSS_A2','SFSS_A3', \
#              'cb_SULFATE','cb_DUST','cb_SALT','cb_BC','cb_OM', \
#              'cb_BC_N','cb_BC_NI','cb_BC_A','cb_BC_AI','cb_BC_AX','cb_BC_AC', \
#              'cb_OM_NI','cb_OM_AI','cb_OM_AC','cb_SOA_NA','cb_SOA_A1', \
#              'cb_SO4_A1','cb_SO4_A2','cb_SO4_AC','cb_SO4_NA','cb_SO4_PR', \
#              'SFBC_N','SFBC_NI','SFBC_AX', \
#              'SFOM_NI', \
#              'TAU_DMS','TAU_isoprene','TAU_monoterp', \
#              'DRY_SULFATE_TOT_noresm2','DRY_DUST_TOT_noresm2','DRY_SALT_TOT_noresm2','DRY_BC_TOT_noresm2','DRY_OM_TOT_noresm2', \
#              'WET_SULFATE_TOT_noresm2','WET_DUST_TOT_noresm2','WET_SALT_TOT_noresm2','WET_BC_TOT_noresm2','WET_OM_TOT_noresm2', \
#              'TAU_SULFATE_noresm2','TAU_DUST_noresm2','TAU_SALT_noresm2','TAU_BC_noresm2','TAU_OM_noresm2', \
#              'BC_NclcoagTend','BC_AclcoagTend','BC_NIclcoagTend','BC_AIclcoagTend','BC_AXclcoagTend','BC_AC_OCWclcoagTend', \
#              'OM_AC_OCWclcoagTend', \
#              'SO4_NAclcoagTend','SO4_A1clcoagTend','SO4_A2_OCWclcoagTend', \
#              'CDNUMC','CCN_B','CCN1_columnburden','CCN2_columnburden','CCN3_columnburden', \
#              'AOD_VISdivDAYFOC', \
              'cb_BC_AC_OCW', \
              'N_AER_columnburden'] 
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#
# SAME WITHOUT OZONE :
#--------------------------------------------------------------------
#
expidlist=[ \
           'histssp585', \
           'histssp585-cloud2', \
           'histssp585-eddy', \
           'histssp585-iceSheet3', \
           'histssp585-snow', \
           'histssp585-piAerOxid', \
           'histssp370-piAerOxid']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Cloud', \
            'Eddy', \
            'IceSheet', \
            'Snow', \
            'piAerOxid', \
            ''] 
#
smoothlist=[0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,5,6,6]
#
code=generalcode+'_without_ozone'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#
# SAME WITHOUT OZONE & CLOUD:
#--------------------------------------------------------------------
#
expidlist=[ \
           'histssp585', \
           'histssp585-eddy', \
           'histssp585-iceSheet3', \
           'histssp585-snow', \
           'histssp585-piAerOxid', \
           'histssp370-piAerOxid']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Eddy', \
            'IceSheet', \
            'Snow', \
            'piAerOxid', \
            '']
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0]
#
colorlist=[0,2,3,5,6,6]
#
code=generalcode+'_without_ozone_cloud'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#



# TOTAL OZONE COLUMN
#------------------------------------------------------------------------
#
expidlist=['histssp585', \
           'histssp585-cloud2', \
           'histssp585-eddy', \
           'histssp585-iceSheet3', \
           'histssp585-ozone', \
           'histssp585-snow', \
           'histssp585-piAerOxid', \
           'histssp370-piAerOxid']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Cloud', \
            'Eddy', \
            'IceSheet', \
            'Ozone', \
            'Snow', \
            'piAerOxid', \
            '']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6,6]
#
variablelist=['ozone_columnburden','ozone_columnburden','ozone_columnburden','ozone_columnburden','cb_O3','ozone_columnburden','ozone_columnburden','ozone_columnburden']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
#
# O3_surfacelayer, OH_surfacelayer, NO3_surfacelayer, HO2_surfacelayer
#---------------------------------------------------------------------
#
expidlist=['histssp585', \
           'histssp585-ozone']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=expidlist
#
smoothlist=[0,0]
#
shiftlist=[0,0]
#
colorlist=[0,5]
#
#variablelist=['O3_surfacelayer','O3_SRF']
variablelist=['NO3_bef_surfacelayer','NO3_SRF']
variablelist=['OH_bef_surfacelayer','OH_SRF']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
#
