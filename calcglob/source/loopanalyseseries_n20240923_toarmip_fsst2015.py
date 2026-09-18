import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
#freqtype='seasonalcycle'
typevarlist=['glob']
description='varcommon-typevarcommon'
generalcode='n20240923_toarmip_fsst2015'


# TOA imbalance
#------------------------------------------------------------------------
#
expidlist=[ \
#           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
#           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
#           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01', \
           \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[\
#            'reference', \
#            'O3-prec. 2050', \
#            'O3-prec+aer. 2050', \
            'O3-clim from reference', \
            'O3-clim from O3-prec. 2050', \
            'O3-clim from O3-prec+aer. 2050']
#
smoothlist=[0,0,0]#,0,0,0]
#
shiftlist=[0,0,0]#,0,0,0]
#
colorlist=[0,1,2]#,3,4,5]
#
variablelist=['FSLNT','cb_O3','cb_NO2','OH_columnburden','HO2_columnburden','TREFHT','TS', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'LNO_COL_PROD','LNO_PROD_columnburden', \
              'cb_CH4CHEM','cb_N2OCHEM', \
              'cb_CO','cb_NO','cb_NO2', \
              'NO_SRF','NO2_SRF','N2O5_SRF','HNO3_SRF']
#
variablelist=['CLDTOT']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


