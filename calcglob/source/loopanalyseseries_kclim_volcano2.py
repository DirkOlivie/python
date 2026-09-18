import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
freqtype='monthly'
description='varcommon'



# 1 degree
#----------------------------------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test12', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['SO2 (100%)','SO2 (90%)','SO4 (10 %), SO4 (100 %)', \
            'SO2 (100%)','SO2 (90%)','SO4 (10 %), SO4 (100 %)']
smoothlist=[0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0]
code='kclim_ozone_volcano_aerotab_f09'
#
variablelist=['cb_SULFATE','AOD_VISdivDAYFOC','DOD550divDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)




# OBTAINING VOLCANIC EMISSION TOTAL
#----------------------------------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['NMR01_NCONC01 (0%)'  ,'NMR01_VCONC01 (0%)'  ,'NMR05_NCONC05 (0%)'  ,'NMR05_VCONC05 (0%)',\
            'NMR01_NCONC01 (100%)','NMR01_VCONC01 (100%)','NMR05_NCONC05 (100%)','NMR05_VCONC05 (100%)']
smoothlist=[0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0]
code='kclim_ozone_volcano_aerotab'
#
variablelist=['NMR01_NCONC01_weightedcolumnburden','NMR01_VCONC01_weightedcolumnburden','NMR05_NCONC05_weightedcolumnburden','NMR05_VCONC05_weightedcolumnburden',\
              'NMR01_NCONC01_weightedcolumnburden','NMR01_VCONC01_weightedcolumnburden','NMR05_NCONC05_weightedcolumnburden','NMR05_VCONC05_weightedcolumnburden']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)



expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08']
refidlist=expidlist
variablelist=['cb_SO4_NA','cb_SO4_A1','cb_SO4_PR','cb_SO4_AC','cb_SO2']
legendlist=variablelist
smoothlist=[0,0,0,0,0]
shiftlist=[0,0,0,0,0]
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)


expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
refidlist=expidlist
variablelist=['VCONC01_columnburden','VCONC05_columnburden','VCONC01_columnburden','VCONC05_columnburden']
legendlist=variablelist
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)


expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
refidlist=expidlist
variablelist=['D550_SO4','D550_SO4']
legendlist=variablelist
smoothlist=[0,0]
shiftlist=[0,0]
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)




# OBTAINING VOLCANIC EMISSION TOTAL
#----------------------------------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['']
smoothlist=[0]
shiftlist=[0]
code='kclim_ozone_volcano_aerotab'
#
variablelist=['SO4_NA_CMXF']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)


# OTHER VARIABLES
#----------------
#
expidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test12', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
#
refidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13']
#
wlist=[1.,-1.]

legendlist=[ \
            'SO2 100%/SO4 0%', \
            'SO2 97.5%/SO4 2.5%', \
            'SO2 95%/SO4 5%', \
            'SO2 90%/SO4 10%', \
            'SO2 80%/SO4 20%', \
            'SO2 50%/SO4 50%', \
            'SO2 0%/SO4 100%', \
            'SO2 0%/SO4 100% (na)']
#
smoothlist=[0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
code='kclim_ozone_volcano_aerotab'
#
variablelist=['SO4_NAcondTend','SO4_NAcoagTend','SO4_A1condTend','SO4_A1coagTend','SO4_ACcoagTend']
variablelist=['VCONC01_columnburden','VCONC05_columnburden']
variablelist=['cb_SULFATE','AOD_VISdivDAYFOC','DOD550divDAYFOC','cb_SO4_A2','cb_H2SO4']
variablelist=['VCONC01_columnburden','VCONC02_columnburden','VCONC04_columnburden','VCONC05_columnburden','VCONC06_columnburden','VCONC07_columnburden','VCONC08_columnburden','VCONC09_columnburden','VCONC10_columnburden','VCONC12_columnburden','VCONC14_columnburden','WD_SO2','SF_SO2']
#variablelist=['AOD_VISdivDAYFOC','cb_SO4_AC','cb_SO4_A1','cb_SO4_NA', 'cb_SO4_PR','D550_SO4','cb_SULFATE','NCONC01_columnburden','NCONC05_columnburden','cb_SO2']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
