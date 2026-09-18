import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon'
generalcode='n20231107_keyclim_erf'


# I. ALL VARIABLES 2014
#######################
#
expidlist=[ \
            'NF1850frc2norbc_aer2014_f09_20200108', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug01', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug02', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug03', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug04', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug05', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug06']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['N1024 (fram)', \
            'N1024', \
            'N1024 (corr.)', \
            'N1075 (Eddy, piAerOxid-SSP585)', \
            'N1536 (IceSheet)', \
            'N1728 (Reference)', \
            'N1792 (Cloud, Snow, Ozone, piAerOxid)']
#
legendlist=['N1024 (fram)', \
            'N1024', \
            'N1024 (corr.)', \
            'N1075 (Eddy, piAO585)', \
            'N1536 (IceSheet)', \
            'N1728 (Reference)', \
            'N1792 (Cl, Sn, Oz, piO)']
#
smoothlist=[0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6]
#

# tempocn no PRECT
variablelist=[ \
            'FSNT','FLNT','FSLNT', \
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
              'N_AER_columnburden', \
              'cb_BC_AC_OCW', \
              'CCN_B', \
              'D550_BCdivDAYFOC','D550_POMdivDAYFOC','D550_SO4divDAYFOC', ]
#
code=generalcode+'_2014'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# ALL VARIABLES 1850
#-------------------
#
expidlist=[ \
            'NF1850frc2norbc_f09_20200108', \
            'NF1850frc2norbc_f09_20231029_pesbug01', \
            'NF1850frc2norbc_f09_20231029_pesbug02', \
            'NF1850frc2norbc_f09_20231029_pesbug03', \
            'NF1850frc2norbc_f09_20231029_pesbug04', \
            'NF1850frc2norbc_f09_20231029_pesbug05', \
            'NF1850frc2norbc_f09_20231029_pesbug06']
#
code=generalcode+'_1850'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# II. WITHOUT FRAM wrong CCN1, CCN2, CCN3, ..., CCN7
####################################################


# ALL VARIABLES 2014
#-------------------
#
expidlist=[ \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug01', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug02', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug03', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug04', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug05', \
            'NF1850frc2norbc_aer2014_f09_20231029_pesbug06']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['N1024', \
            'N1024 (corr.)', \
            'N1075 (Eddy, piAerOxid-SSP585)', \
            'N1536 (IceSheet)', \
            'N1728 (Reference)', \
            'N1792 (Cloud, Snow, Ozone, piAerOxid)']
#
legendlist=['N1024', \
            'N1024 (corr.)', \
            'N1075 (Eddy, piAO585)', \
            'N1536 (IceSheet)', \
            'N1728 (Reference)', \
            'N1792 (Cl, Sn, Oz, piO)']
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0]
#
colorlist=[1,2,3,4,5,6]
#

# tempocn no PRECT
variablelist=[ \
              'CCN1_columnburden','CCN2_columnburden','CCN3_columnburden','CCN4_columnburden','CCN5_columnburden','CCN6_columnburden','CCN7_columnburden']
#
code=generalcode+'_2014'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# ALL VARIABLES 1850
#-------------------
#
expidlist=[ \
            'NF1850frc2norbc_f09_20231029_pesbug01', \
            'NF1850frc2norbc_f09_20231029_pesbug02', \
            'NF1850frc2norbc_f09_20231029_pesbug03', \
            'NF1850frc2norbc_f09_20231029_pesbug04', \
            'NF1850frc2norbc_f09_20231029_pesbug05', \
            'NF1850frc2norbc_f09_20231029_pesbug06']
#
code=generalcode+'_1850'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



