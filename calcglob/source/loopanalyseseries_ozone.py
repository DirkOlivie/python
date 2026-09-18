import analyseseries

def loopanalyseseries2(expidlist,legendlist,variablelist,typevar,freqtype,code) :

    for variable in variablelist :
        analyseseries.analyseseries(expidlist=expidlist,legendlist=legendlist,variable=variable,typevar=typevar,freqtype=freqtype,code=code)
  

# MAIN PROGRAM

expidlist=['FC2010climo_f19_20210204_test1', \
           'FC2010climo_f19_mg17_20210204_test1', \
           'FC2010climo_f09_mg17_20210204_test1', \
            \
           'FC2010climo_prep_f19_20210204_test5', \
           'FC2010climo_prep_f19_20210204_test6', \
            \
#          'NF1850norbc_tropstratchem_f19_20210331_test14', \
#           'NF1850norbc_tropstratchem_f19_20210517_test01', \
#           'NF1850norbc_tropstratchem_f19_20210517_test02', \
#           'NF1850norbc_tropstratchem_f19_20210517_test03', \
#           'NF1850norbc_tropstratchem_f19_20210517_test04', \
#           'NF1850norbc_tropstratchem_f19_20210517_test05', \
           'NF1850norbc_tropstratchem_f19_20210517_test06', \
           'NF1850norbc_tropstratchem_f19_20210517_test08', \
           'NF1850norbc_tropstratchem_f19_20210517_test09', \
           'NF1850norbc_tropstratchem_f19_20210517_test10', \
           'NF1850norbc_tropstratchem_f19_20210517_test11', \
           'NF1850norbc_tropstratchem_f19_20210517_test12', \
            \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test01', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test03', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test04', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test05'] 
#expidlist=['NF1850norbc_tropstratchem_f19_20210331_test14','NF1850norbc_tropstratchem_f19_20210331_test14']
#expidlist=['FC2010climo_f19_20210204_test1','FC2010climo_f19_20210204_test1']
legendlist=['CESM2 (cam-chem)', \
            'CESM2 (cam-chem, mg17)', 
            'CESM2 (cam-chem, mg17, 1x1)', \

            'CESM2 (modif. chemistry)',
            'CESM2 (modif. chemistry + modif phot.)',
#            'NorESM2 (full chemistry)', \
#            'NorESM2 test1', \
#            'NorESM2 test2', \
#            'NorESM2 test3', \
#            'NorESM2 test4', \
#            'NorESM2 test5', \
             'NorESM2 test6', \
             'NorESM2 test8', \
             'NorESM2 test9', \
             'NorESM2 test10', \
             'NorESM2 test11', \
             'NorESM2 test12', \
              \
             'NorESM2_2010test1', \
             'NorESM2_2010test3', \
             'NorESM2_2010test4', \
             'NorESM2_2010test5']  
#            
expidlist=['FC2010climo_f19_20210204_test1', \
           'FC2010climo_f19_mg17_20210204_test1', \
           'FC2010climo_f09_mg17_20210204_test1', \
            \
           'FC2010climo_prep_f19_20210204_test5', \
            \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test06', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test07']
#   
legendlist=['CESM2 (cam-chem)', \
            'CESM2 (cam-chem, mg17)',
            'CESM2 (cam-chem, mg17, 1x1)', \
             \
            'CESM2 (modif. chemistry)', \
             \
            'NorESM2 (test06)', \
            'NorESM2 (test07)']
# 
expidlist=['FC2010climo_prep_f19_20210204_test5', \
            \
           'NF1850norbc_tropstratchem_f19_20210517_test01', \
           'NF1850norbc_tropstratchem_f19_20210517_test02', \
           'NF1850norbc_tropstratchem_f19_20210517_test03', \
           'NF1850norbc_tropstratchem_f19_20210517_test04', \
           'NF1850norbc_tropstratchem_f19_20210517_test05', \
           'NF1850norbc_tropstratchem_f19_20210517_test06', \
           'NF1850norbc_tropstratchem_f19_20210517_test08', \
           'NF1850norbc_tropstratchem_f19_20210517_test09', \
           'NF1850norbc_tropstratchem_f19_20210517_test10', \
           'NF1850norbc_tropstratchem_f19_20210517_test11', \
           'NF1850norbc_tropstratchem_f19_20210517_test12', \
            \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test07'] 
#
legendlist=['CESM2', \
             \
            'NorESM2 (test 01)', \
            'NorESM2 (test 02)', \
            'NorESM2 (test 03)', \
            'NorESM2 (test 04)', \
            'NorESM2 (test 05)', \
            'NorESM2 (test 06)', \
            'NorESM2 (test 08)', \
            'NorESM2 (test 09)', \
            'NorESM2 (test 10)', \
            'NorESM2 (test 11)', \
            'NorESM2 (test 12)', \
             \
            'NorESM2']
#
##############################################################################
#
expidlist=['FC2010climo_f09_mg17_20210204_test1', \
           'FC2010climo_f19_20210204_test1', \
           'FC2010climo_prep_f19_20210204_test7', \
           'FC2010climo_prep_f19_20210204_test9', \
            \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test08', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test09', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test13', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test14', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test15', \
           'NF2010norpddmsbc_tropstratchem_f19_20210517_test16']
legendlist=['CESM2 (1x1)', \
            'CESM2', \
            'CESM2 (no trop. het. chem.)', \
            'CESM2 (cesm2.2 correction)', \
            'NorESM2', \
            'NorESM2 (no trop. het. chem.)', \
            'NorESM2 (only mode 1, 2, 4, 5)', \
            'NorESM2 (only mode 1)', \
            'NorESM2 (only mode 2)', \
            'NorESM2 (only mode 4)', \
            'NorESM2 (only mode 5)']  
#
variablelist=['cb_O3','cb_CH4','cb_N2O','cb_CO','cb_NO','cb_NO2','cb_SO2', \
              'SFCO','SFNO','SFNO2', \
              'SFDMS','SFNH3','SFSO2','SO2_CMXF','EMI_SO2_TOT_noresm2', \
              'FSLNT','TREFHT', \
              'O3_SRF','CO_SRF','SO2_SRF','NO2_SRF','CH4_SRF','N2O_SRF','OH_SRF','H2O_SRF','NO_SRF', \
              'cb_NH3', 'DF_NH3', 'WD_NH3',   'SFNH3', \
              'cb_NH4', 'DF_NH4', 'WD_NH4',   'SFNH4', \
              'cb_NDEP',       'WD_NDEP',  'SFNDEP', \
              'cb_NHDEP',      'WD_NHDEP', 'SFNHDEP']

#variablelist=['CLDTOT','CLDLOW','CLDMED','CLDHGH','CLDLIQ','CLDICE']

# NO_SRF
variablelist=['OH_SRF'] #,'CO_SRF']
#
#variablelist=['H2O_SRF']
#variablelist=['OH_SRF']
#variablelist=['SFISOP','SFMTERP']
#variablelist=['MEG_BCARY','MEG_BIGALK','MEG_BIGENE','MEG_C2H4','MEG_C2H5OH','MEG_C2H6', \
#              'MEG_C3H6','MEG_C3H8','MEG_CH2O','MEG_CH3CHO','MEG_CH3COCH3','MEG_CH3COOH', \
#              'MEG_CH3OH','MEG_CO','MEG_HCN','MEG_HCOOH','MEG_ISOP','MEG_MTERP','MEG_TOLUENE']
# 
#variablelist=['TREFHT']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='trial'
#
loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,code=code)
