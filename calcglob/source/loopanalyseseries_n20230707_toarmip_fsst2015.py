import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
freqtype='seasonalcycle'
typevar='glob'
description='varcommon'
generalcode='n20230707_toarmip_fsst2015'


# TOA imbalance
#------------------------------------------------------------------------
#
expidlist=[ \
           'NF1850norbc_tropstratchem_f19_20230515_test01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20230605_sim01', \
            \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['piClim-control (1850)', \
            'reference (2015)', \
            'all emissions (2050)', \
            'reference (2015)', \
            'ozone precursors (2050)', \
            'reference (2015) - presc. O3']
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5]
#
variablelist=['FSLNT','cb_O3','cb_NO2','OH_columnburden','HO2_columnburden','TREFHT','TS', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'LNO_COL_PROD','LNO_PROD_columnburden']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# seperate variables
#-------------------------------------------------------------------------
#
description=''
variablelist=['cb_CH4','cb_CH4CHEM','cb_CH4CHEM','cb_CH4CHEM','cb_CH4CHEM','cb_CH4CHEM']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

variablelist=['cb_N2O','cb_N2OCHEM','cb_N2OCHEM','cb_N2OCHEM','cb_N2OCHEM','cb_N2OCHEM']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


variablelist=['cb_O3','cb_O3','cb_O3','cb_O3','cb_O3','ozone_columnburden']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code+'_rad',figlayout=figlayout,colorlist=colorlist)

variablelist=['O3_columnburden','O3_columnburden','O3_columnburden','O3_columnburden','O3_columnburden','ozone_columnburden']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code+'_rad',figlayout=figlayout,colorlist=colorlist)



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
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CH4_c','cb_CH4CHEM','cb_CH4_c','cb_CH4CHEM']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_N2O_c','cb_N2OCHEM','cb_N2O_c','cb_N2OCHEM']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CFC11_c','cb_CFC11CHEM','cb_CFC11_c','cb_CFC11CHEM']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CFC12_c','cb_CFC12CHEM','cb_CFC12_c','cb_CFC12CHEM']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
