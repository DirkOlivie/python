import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
#freqtype='seasonalcycle'
typevarlist=['glob']
description='varcommon-typevarcommon'
generalcode='n20240418_toarmip_fsst2015'


# TOA imbalance
#------------------------------------------------------------------------
#
expidlist=[ \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01', \
           \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['reference', \
            'O3-prec. 2050', \
            'O3-prec+aer. 2050', \
            'O3-clim from reference', \
            'O3-clim from O3-prec. 2050', \
            'O3-clim from O3-prec+aer. 2050']
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5]
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

# seperate variables
#-------------------------------------------------------------------------
description=''
#
variablelist=['cb_O3','cb_O3','cb_O3','ozone_columnburden','ozone_columnburden','ozone_columnburden']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code+'_rad',figlayout=figlayout,colorlist=colorlist)

variablelist=['O3_columnburden','O3_columnburden','O3_columnburden','ozone_columnburden','ozone_columnburden','ozone_columnburden']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code+'_rad',figlayout=figlayout,colorlist=colorlist)



# cb_CO2, cb_CO2_c, cb_CO2CHEM
#------------------------------------------------------------------------
#
description=''
#
expidlist=[ \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01']


#
refidlist=expidlist
#
wlist=[1.,0.]

#
legendlist=['rad. active. (ref. sim.)', \
            'chem. active. (ref. sim.)', \
            'rad. active. (pert. sim.)', \
            'chem. active. (pert. sim.)']
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,0,0]
#
colorlist=[0,1,2,4]
#
code=generalcode+'_rad'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
variablelist=['cb_CO2_c','cb_CO2CHEM','cb_CO2_c','cb_CO2CHEM']
#loopanalyseseries2.#loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CH4_c','cb_CH4CHEM','cb_CH4_c','cb_CH4CHEM']
#loopanalyseseries2.#loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_N2O_c','cb_N2OCHEM','cb_N2O_c','cb_N2OCHEM']
#loopanalyseseries2.#loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CFC11_c','cb_CFC11CHEM','cb_CFC11_c','cb_CFC11CHEM']
#loopanalyseseries2.#loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CFC12_c','cb_CFC12CHEM','cb_CFC12_c','cb_CFC12CHEM']
#loopanalyseseries2.#loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# total ozone column
#------------------------------------------------------------------------
#
description='varcommon-typevarcommon'

expidlist=[ \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01', \
           \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['reference', \
            'O3-prec. 2050', \
            'O3-prec+aer. 2050', \
            'O3-clim from reference', \
            'O3-clim from O3-prec. 2050', \
            'O3-clim from O3-prec+aer. 2050']
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5]
#
variablelist=['cb_O3']
typevarlist=['90S28S','28S28N','28N60N','60N90N']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# total ozone column
#------------------------------------------------------------------------
#
description='typevarcommon'

expidlist=[ \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01', \
            \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01', \
           \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'reference', \
            'O3-prec. 2050', \
            'O3-prec+aer. 2050', \
             \
            'O3-clim from reference', \
            'O3-clim from O3-prec. 2050', \
            'O3-clim from O3-prec+aer. 2050', \
             \
            'O3-clim from reference', \
            'O3-clim from O3-prec. 2050', \
            'O3-clim from O3-prec+aer. 2050']
#
legendlist=['(1a)','(2a)','(3a)','(1b)','(2b)','(3b)','(1b)','(2b)','(3b)']
#
smoothlist=[0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6,7,8]
#
variablelist=['cb_O3','cb_O3','cb_O3','ozone_columnburden','ozone_columnburden','ozone_columnburden','ozone_extclim_columnburden','ozone_extclim_columnburden','ozone_extclim_columnburden']
typevarlist=['']
#
code=generalcode+'_exclim'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


