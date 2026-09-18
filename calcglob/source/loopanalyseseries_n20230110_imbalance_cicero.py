import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

# imbalance cicero

# 1. NEW CEDS simulations
#------------------------
expidlist=['NFHISTnorpddmsbc_01_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_02_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_03_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_04_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_05_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_06_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_aer2000_01_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_aer2000_02_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_aer2000_03_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_aer2000_04_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_aer2000_05_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_aer2000_06_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_anthro2000_01_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_anthro2000_02_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_anthro2000_03_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_anthro2000_04_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_anthro2000_05_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_anthro2000_06_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_all2000_01_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_all2000_02_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_all2000_03_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_all2000_04_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_all2000_05_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_all2000_06_f19_mg17_20230110ext']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['ref 1', 'ref 2','ref 3','ref 4', 'ref 5','ref 6', \
            'aer 1', 'aer 2','aer 3','aer 4', 'aer 5','aer 6', \
            'anthro 1', 'anthro 2','anthro 3','anthro 4', 'anthro 5','anthro 6', \
            'all 1', 'all 2','all 3','all 4', 'all 5','all 6']
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
colorlist=['b','b','b','b','b','b','g','g','g','g','g','g','r','r','r','r','r','r','c','c','c','c','c','c']
variablelist=['EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_BC_TOT_noresm2','EMI_OM_TOT_noresm2','H2O_CMXF', \
              'FSLNT','SWCF','CDNUMC', \
              'co2vmr','ch4vmr','n2ovmr','f11vmr','f12vmr']
#             'PRECT']
code='n20230110_imbalance_cicero'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
description='varcommon'
#
#for freqtype in freqtypelist : 
#    for typevar in typevarlist : 
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 2. COMPARISON with CMIP6 historical simulations
#------------------------
expidlist=['NHIST_f19_tn14_20190710', \
           'NFHISTnorpddmsbc_01_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_02_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_03_f19_mg17_20230110ext']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['cmip6','new ceds 1', 'new ceds 2','new ceds 3']
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
variablelist=['EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_BC_TOT_noresm2','EMI_OM_TOT_noresm2','H2O_CMXF',\
              'FSLNT','SWCF', \
              'co2vmr','ch4vmr','n2ovmr','f11vmr','f12vmr']
code='n20230110_imbalance_cicero_ceds_vs_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob','US','CHN','EUR']
freqtypelist=['YEA']
#
description='varcommon'
#
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)



# 3. COMPARISON with CMIP6 historical + SSP245 + SSP simulations
#------------------------
expidlist=['NHIST_f19_tn14_20190710', \
           'NFHISTnorpddmsbc_01_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_02_f19_mg17_20230110ext', \
           'NFHISTnorpddmsbc_03_f19_mg17_20230110ext', \
           'NSSP126frc2_f19_tn14_20191014', \
           'NSSP245frc2_f19_tn14_20191014', \
           'NSSP370frc2_f19_tn14_20191014', \
           'NSSP585frc2_f19_tn14_20191014']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['cmip6','new ceds 1', 'new ceds 2','new ceds 3','ssp126','ssp245','ssp370','ssp585']
smoothlist=[0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0]
variablelist=['EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_BC_TOT_noresm2','EMI_OM_TOT_noresm2']
variablelist=['TREFHT']
code='n20230110_imbalance_cicero_ceds_vs_cmip6_ssp'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
description='varcommon'
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)



