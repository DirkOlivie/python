def getexpidinfo (expid) :
#---------------
    '''
    MODIFICATION
	    (2014-05-23) : included 00N30N, 30N60N, 60N90N
        (2014-10-30) : included LAND, SEA
 	    (2015-01-05) : included Monsoon areas
	    (2017-05-02) : added EURHTAP1, EURHTAP2
    '''
    basedir='/projects/NS2345K/noresm/cases'
    basedirns2345k='/projects/NS2345K/noresm/cases'
    basedirns9560k='/projects/NS9560K/noresm/cases'
    basedirns9252k='/projects/NS9252K/noresm/cases'
#   basedirfram='/projects/NS2345K/FRAM/noresm/cases'
    basedirfram='/tos-project1/NS2345Ktmp/FRAM/noresm/cases' # 2019-04-16 (see sigma2 - opslog)
    basedirsnapshot='/projects/NS2345K/.snapshots/Tuesday-15-Jan-2019/noresm/cases'
    basedirnatsens='/projects/NS2345K/noresm/olivie/natural-sensitivity'
    basedirns2345kvsls='/projects/NS2345K/noresm/olivie/vsls'
    basedirns2345kozone='/projects/NS2345K/noresm/olivie/ozone'
    lakedirns2345kozone='/datalake/NS2345K/olivie/noresm/cases-group/ozone'
    basedirns2345kaerocom='/projects/NS2345K/noresm/olivie/aerocom'
    basedirns2345knoresm22='/projects/NS2345K/noresm/olivie/noresm2.2'
    basedirns2345kemissionmip='/projects/NS2345K/noresm/olivie/emissionmip'
    basedirns2345kmmppecloud='/projects/NS2345K/noresm/olivie/mmppe-cloud'
    oyvindsns2345kmmppecloud='/projects/NS2345K/oyvinds/mmppe-cloud'
    basedirns2345kimbalancemip='/projects/NS2345K/noresm/olivie/imbalancemip'
    basedirns2345kesm2025ozone='/projects/NS2345K/noresm/olivie/esm2025-ozone'
    lakedirns2345kesm2025ozone='/datalake/NS2345K/olivie/noresm/cases-group/esm2025-ozone'
    basedirns2345koyvind='/projects/NS2345K/oyvinds/cases'
    basedirns9252kheiko='/projects/NS9252K/users/heig/NorESM/archive'
    basedirns9560kn2otest='/projects/NS9560K/users/olivie/noresm/cases/n2o-tests'
    lakedirns2345kn2otest='/datalake/NS2345K/olivie/noresm/cases-group/n2o-tests'
    basedirns9560kn2olandtest='/projects/NS9560K/users/olivie/noresm/cases/n2o-land-tests'
    lakedirns2345kn2olandtest='/datalake/NS2345K/olivie/noresm/cases-group/n2o-land-tests'
    basedirns9560kch4test='/projects/NS9560K/users/olivie/noresm/cases/ch4-tests'
    lakedirns2345kesm2025ch4='/datalake/NS2345K/olivie/noresm/cases-group/esm2025-ch4'
    lakedirns2345khyway='/datalake/NS2345K/olivie/noresm/cases-group/hyway'
    basedirns9560kimbalancemip='/projects/NS9560K/users/olivie/noresm/cases/imbalancemip'
    basedirns9560ktoarmip='/projects/NS9560K/users/olivie/noresm/cases/toarmip'
    lakedirns2345ktoarmip='/datalake/NS2345K/olivie/noresm/cases-group/toarmip'
    lakedirns2345kmethanemip='/datalake/NS2345K/olivie/noresm/cases-group/methanemip'
    lakedirns2345cmip7volcaodnoresm23='/datalake/NS2345K/olivie/noresm/cases-group/cmip7-volcaod-noresm2.3'
    basedirns9560kbromo='/projects/NS9560K/users/olivie/noresm/cases/bromoform'
    basedirns9560krefactor='/projects/NS9560K/users/olivie/noresm/cases/refactor'
    basedirns9560kkeyclimerf='/projects/NS9560K/users/olivie/noresm/cases/keyclim-erf'
    basedirns9560kingvild='/projects/NS9560K/users/ingvisau'
    lakedirns9560k='/datalake/NS9560K/noresm/cases'
    lakedirns9252k='/datalake/NS9252K/cases'
    lakedirns2345knoresm21performance='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.1-performance'
    lakedirns2345knoresm23test='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.3-test'
    lakedirns9560knoresm23='/datalake/NS9560K/noresm2.3/cases'
    lakedirns2345knoresm25test='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.5-test'
    lakedirns2345kcamsvsls='/datalake/NS2345K/olivie/noresm/cases-group/cams-vsls'
    lakedirns2345knavigate='/datalake/NS2345K/olivie/noresm/cases-group/navigate'
    basedirns9560kcamsvsls='/projects/NS9560K/users/olivie/noresm/cases/cams-vsls'
    lakedirns9560knoresm3='/datalake/NS9560K/noresm3/cases'
    lakedirns9560knoresm='/datalake/NS9560K/noresm/cases'
    lakedirns9560koyvind='/datalake/NS9560K/oyvinds/cases'
    lakedirns2345kesm2025oyvind='/datalake/NS2345K/oyvinds/casesESM2025'
    basedirns10054kimpose='/projects/NS10054K/IMPOSE_idealized'
    lakedirns1002k='/datalake/NS1002K/noresm/cases'
    basedirns9560knoresm3='/projects/NS9560K/noresm3/cases'
    basedirns11106k='/projects/NS11106K/HYway/modelling_repository'
    basedirns2980k='/projects/NS2980K/jmaerz/archive'
    lakedirns2980k='/datalake/NS2980K/users/jmaerz/simulations/archive'
    lakedirns2345kovewh='/nird/datalake/NS2345K/ovewh/PPE-BASELINE'
    basedirns1004kelihho='/nird/datapeak/NS1004K/elihho'
    lakedirns9560kmpet='/nird/datalake/NS9560K/mpet/archive'
    lakedirns11118knoresm3='/datalake/NS11118K/noresm3/cases'
    lakedirns11118knoresm23='/datalake/NS11118K/noresm2.3/cases'
    scratchdir='/scratch/olivie/noresm/cases'    
    esgfdir='/projects/NS9252K/CMIP6'
    #
    # Default variables
    cdir=None
    expidshort=None

    # noresm1 (official) : 4xco2 and picontrol
    if   expid=='N18504XAERCN_f19_g16_01' : des={'year0' :  1, 'year1' : 150, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # 4xCO2
    elif expid=='NAER1850CNOC_f19_g16_03' : des={'year0' :  1, 'year1' : 299, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}      
    elif expid=='NAER1850CNOC_f19_g16_04' : des={'year0' :300, 'year1' : 599, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}      
    elif expid=='NAER1850CNOC_f19_g16_05' : des={'year0' :600, 'year1' : 699, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}      
#   elif expid=='NAER1850CNOC_f19_g16_06' : des={'year0' :700, 'year1' : 849, 'model' : 'NorESM1', 'subdir' : basedirsnapshot, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 1200     
    elif expid=='NAER1850CNOC_f19_g16_06' : des={'year0' :700, 'year1' :1200, 'model' : 'NorESM1', 'subdir' : basedirsnapshot, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 1200     
    #
    # noresm1 (anonymous) : picontrl and 4xco2
    elif expid=='N1850AERCN_f19_g16_161015'       : des={'year0' : 631, 'year1' : 780, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # 601
    elif expid=='N1850AERCN_4XCO2_f19_g16'        : des={'year0' : 631, 'year1' : 780, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # noresm1-happi : 1x1 degree !!!!
    elif expid=='N1850AERCN_f09_g16_01'     : des={'year0' : 930, 'year1' :1079, 'model' : 'NorESM1', 'subdir' : '../../../NS9082K/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850AERCN4XCO2_f09_16_01' : des={'year0' : 930, 'year1' :1079, 'model' : 'NorESM1', 'subdir' : '../../../NS9082K/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # noresm1-happi SLAB OCEAN : 1x1 degree !!!
    elif expid=='N1Happi_som_1850_02'       : des={'year0' : 26, 'year1' :130, 'model' : 'NorESM1', 'subdir' : '../../../NS9082K/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1Happi_som_1850_4XCO2_01' : des={'year0' : 26, 'year1' :130, 'model' : 'NorESM1', 'subdir' : '../../../NS9082K/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # noresm1 historical
    elif expid=='N20TRAERCN_f19_g16_01' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N20TRAERCN_f19_g16_02' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N20TRAERCN_f19_g16_03' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N20TRAERCN_f19_g16_06' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N20TRAERCN_f19_g16_07' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    #
    # noresm-happi historical
    elif expid=='N20TRAERCN_f09_g16_happi01' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : '/scratch/olivie/noresm-happi', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}    
    elif expid=='N20TRAERCN_f09_g16_happi02' : des={'year0' : 1990, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : '/scratch/olivie/noresm-happi', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}    
    elif expid=='N20TRAERCN_f09_g16_happi03' : des={'year0' : 1990, 'year1' : 2005, 'model' : 'NorESM1', 'subdir' : '/scratch/olivie/noresm-happi', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}    
    # 
    # beta-05
    elif expid=='CESM2B5_NFPTAERO60f09_gamma0p238_AMCORRallc1' : des={'year0' : 1, 'year1' :  7, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60f09_gamma0p238_AMCORRallc2' : des={'year0' : 1, 'year1' :  7, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60f09_gamma0p238_AMCORR'      : des={'year0' : 1, 'year1' :  6, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60f09_gamma0p238'             : des={'year0' : 1, 'year1' :  6, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}

    #-- no access on nird      
    elif expid=='CESM2B5_NFPTAERO60_f09'             : des='not known'
    elif expid=='CESM2B5_NFPTAERO60_f19_c0_lnd0p045' : des='not known'
    elif expid=='CESM2B5_NFPTAERO60_f19_c0_ocn0p045' : des='not known'
    elif expid=='CESM2B5_NFPTAERO60_f19'             : des='not known'
    #-- no access on nird

    elif expid=='CESM2B5_NFPTAERO60_gamma0p238_AMCORRallc1' : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60_gamma0p238_AMCORRallc2' : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60_gamma0p238_AMCORRallc3' : des={'year0' : 1, 'year1' :  7, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60_gamma0p238_AMCORR'      : des={'year0' : 1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='CESM2B5_NFPTAERO60_gamma0p238'             : des={'year0' : 1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}

    # beta-06 - spinup simulations - Oyvind/Alok
    elif expid=='B1850_f09_g17_1'                  : des={'year0' : 1, 'year1' :  50, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # SIM1
    elif expid=='N1850P_f09_g17_191017_cmip6emis'  : des={'year0' : 1, 'year1' :  50, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # SIM2 cb_SO2
    elif expid=='B1850_f09_g17_thomas'             : des={'year0' : 1, 'year1' :  50, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # SIM3
    elif expid=='N1850_f19_tn14_191017'            : des={'year0' : 1, 'year1' : 100, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # SIM4 cb_SO2
    elif expid=='N1850_f09_tn14_191017'            : des={'year0' : 1, 'year1' :  75, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} #      cb_SO2 
    elif expid=='N1850OCBDRD_f09_tn14'             : des={'year0' : 1, 'year1' :  50, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # SIM5
    elif expid=='N1850C53CLM45L32_f19_tn11_191017' : des={'year0' : 1, 'year1' : 200, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # SIM6 cb_SO2, SO2, SO2_SRF nothing else
    elif expid=='N1850C53CLM45L32_f09_tn11_191017' : des={'year0' : 1, 'year1' : 110, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} #      cb_SO2, SO2, SO2_SRF nothing else
    # beta-06 - historical simulations -Dirk
    elif expid=='B06T10_NHIST_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    elif expid=='B06T11_N1850_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    elif expid=='B06T12_NHIST_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    elif expid=='B06T15_BHIST'          : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} #
    elif expid=='B06T16_N1850_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    elif expid=='B06T17_B1850'          : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} #
    elif expid=='B06T18_NHIST_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    elif expid=='B06T19_N1850_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} #
    elif expid=='B06T20_NHIST_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    elif expid=='B06T23_NHIST_f19_tn14' : des={'year0' : 1850, 'year1' : 2005, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # cb_SO2
    # sandbox-227 - Oyvind    
    elif expid=='B1850_f09_g17_r227_050118_newoutclm' : des={'year0' :    1, 'year1' :   50, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    # sandbox-227 - Dirk 
    elif expid=='SB227T39_N1850_f09_tn14' : des={'year0' :    1, 'year1' :   50, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f09_tn14_r227T40'  : des={'year0' :    1, 'year1' :  150, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_f09_tn14_r227T50'  : des={'year0' : 1850, 'year1' : 1924, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f09_tn14_r227T60'  : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f09_tn14_r227T61'  : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f09_tn14_r227T64'  : des={'year0' :    1, 'year1' :    6, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # history_aerosol = true, 3D emissions output

    elif expid=='N1850_f09_tn14_r227T66'  : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # 1850 emissions version20171122
    elif expid=='N1850_f09_tn14_r227T67'  : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # 2000 emissions version20171122
    elif expid=='N1850_f09_tn14_r227T68'  : des={'year0' :    1, 'year1' :    8, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # 1850 emissions version20180330
    elif expid=='N1850_f19_tn14_r227T69'  : des={'year0' :    1, 'year1' :    5, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # 1850 emissions version20180330, 2x2
    elif expid=='N1850_f09_tn14_r227T70'  : des={'year0' :    1, 'year1' :    4, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} # 1850 emissions version20180330
    # johan
    elif expid=='B1850_f09_tn14_230218'  : des={'year0' :    1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f09_tn14_230218'  : des={'year0' :    1, 'year1' :  200, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # ada 
    elif expid=='N1850_f19_tn14_r227_ctrl' : des={'year0' :    1, 'year1' :  360, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # sandbox-227 - Jerry Tjiputra
    elif expid=='N1850OCECO_f09_tn14_r227T40B'  : des={'year0' :    1, 'year1' :  220, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # sandbox-265 - Ada
    elif expid=='F1850_f09_f09_r227DOM_ctrl'  : des={'year0' :    6, 'year1' :   20, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} 
    elif expid=='F1850_f09_f09_r227DOM_2dust' : des={'year0' :    6, 'year1' :   20, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} 
    elif expid=='F1850_f09_f09_r227DOM_2ssa'  : des={'year0' :    6, 'year1' :   20, 'model' : 'NorESM2', 'chem' : '', 'project' : ''} 
    elif expid=='F2000_f09_f09_r227test01'    : des={'year0' :    6, 'year1' :   15, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    # sandbox-265 - Ada - AerChemMIP
    elif expid=='N1850_4xCO2_f19_tn14_r265_ctrl_20180411' : des={'year0' : 1   , 'year1' : 200 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f19_tn14_r265_ctrl_20180411'       : des={'year0' : 1   , 'year1' : 200 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_2DMS_f19_f19_r265_20180412'       : des={'year0' : 1   , 'year1' :  30 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_2DST_f19_f19_r265_20180412'       : des={'year0' : 1   , 'year1' :  30 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_2SSA_f19_f19_r265_20180412'       : des={'year0' : 1   , 'year1' :  30 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_2VOC_f19_f19_r265_20180412'       : des={'year0' : 1   , 'year1' :  30 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_4xCO2_f19_f19_r265_20180412'      : des={'year0' : 1   , 'year1' :  30 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_CTRL_f19_f19_r265_20180412'       : des={'year0' : 1   , 'year1' :  30 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_f19_tn14_r265_20180420'            : des={'year0' : 1850, 'year1' :2005 , 'model' : 'NorESM2', 'subdir' : 'AerChemMIP/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # sandbox-265 Alf
    elif expid=='F2000ERF'   : des={'year0' :    3, 'year1' :   10, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    elif expid=='NF2000PIERF' : des={'year0' :    3, 'year1' :   10, 'model' : 'NorESM2', 'chem' : '', 'project' : ''}
    # cesm2.0 (June 2018)
    elif expid=='N1850OCBDRDDMS_f09_tn14_noresm-dev-06062018_R1' : des={'year0' :    1, 'year1' :   4, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # cesm2.0 : sensitivy tests - Dirk
    # 1x1
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04'             : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04_gam27'       : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04_gam27_dcs4'  : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04_emiPI'       : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04_emiPI_oxiPI' : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04_dms71'       : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # 2x2
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05'                  : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_gam27'            : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_gam27_dcs4'       : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_emiPI'            : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_emiPI_oxiPI'      : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_dms71'            : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_oxiCMIP5'         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_emiPI_oxiCMIP5'   : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_emiPI_oxiPICMIP5' : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_ch4OFF'           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_cosp_convorg'     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05_omssdms'          : des={'year0' :    1, 'year1' :    2, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # 2x2 (correction)
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05b_emiPI_oxiPI'     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05b_emiPI_oxiCMIP5'  : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05b_emiPI_oxiPICMIP5': des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05b_omssdms'         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04c'                 : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05c'                 : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # without preprocessor
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05d_gam27'           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05d_gam27_dcs4'      : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f19_f19_mg17_vljGT05d_dms71'           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04d_gam27'           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF2000climo_f09_f09_mg17_vljGT04d_dms71'           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # ZM 1x1 : sensitivity tests - Thomas
    # on fram
    elif expid=='f09F2k_OD_ZMtests_ctrl' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_nolnd': des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_org'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_tdk'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_tht0' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
#   elif expid=='f09F2k_OD_ZMtests_tht1' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # problem in radiation
    elif expid=='f09F2k_OD_ZMtests_thtdk': des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # on vilje 
    #elif expid=='f09F2k_OD_ZMtests_nolnd_vlj' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #elif expid=='f09F2k_OD_ZMtests_thto'      : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_nolnd_copy': des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/on_vilje/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_thto'      : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/on_vilje/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
#
    elif expid=='f09F2k_OD_ZMtests_thtnc'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_thtdh'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_thtdi'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_thtdj'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_nlnd1'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_nlnd2'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
# 
    elif expid=='f09F2k_OD_ZMtests_refnc'    : des={'year0' :    1, 'year1' :   3, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} 
    elif expid=='f09F2k_OD_ZMtests_refncAlf' : des={'year0' :    1, 'year1' :   2, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} 
#
    elif expid=='f09F2k_OD_ZMtests_djlo_ref'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_dct'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_d2t'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_d2rt' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
#
    elif expid=='f09F2k_OD_ZMtests_djlo_gamdcs_d2rct' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_gamdcs_d2rt'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_gamdcs_d2t'   : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_gamdcs_dt'    : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_gamdcs_ref'   : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
#
    elif expid=='f09F2k_OD_ZMtests_djlo_ssltomx2_dt'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm-djlo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_ssltx2_d2rct' : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm-djlo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_ssltx2_d2rt'  : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm-djlo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_djlo_ssltx2_dt'    : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2', 'subdir' : '../olivie/zm-djlo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
#
# Thomas August/September 2018
    elif expid=='f09F2k_ncar'                : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_OD_ZMtests_rfnc'     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/on_fram/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_OD_ZMtests_rfncp'    : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_OD_ZMtests_2rnc'     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_rfos'     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/on_fram/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='f09F2k_OD_ZMtests_2rosc1'   : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_2rosc1_adj'          : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F_2rosc1_adj_p'          : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_OD_ZMtests_2osc1d'   : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_OD_ZMtests_2rosc1d'  : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_2rosc1d_adj'         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_2rosc1d_adjdcs'      : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F2k_OD_ZMtests_2rosc1dd' : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
    elif expid=='f09F_2rosc1dp'              : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : '../thomas/ZM/expts/out/BugFix/'+expid+'/atm/hist', 'chem' : '', 'project' : ''} # ok
#
    # cesm2.0 (June 2018 - Alok)
    elif expid=='N1850OCBDRDDMS_f19_tn14_noresm-dev-22062018_Original' : des={'year0' :    1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_noresm-dev-22062018_Original' : des={'year0' :    1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_noresm-dev-22062018_clubb_gamma_coef_.27_micro_mg_dcs_400.D-6' : des={'year0' :    1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_noresm-dev-22062018_clubb_gamma_coef_.27_micro_mg_dcs_400.D-6' : des={'year0' :    1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_CGC.27_mgd400.D-6_to_branch'      : des={'year0' :    16, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # not good - still used HAMMOC emissions
    elif expid=='N1850OCBDRDDMS_f09_tn14_CGC.27_mgd400.D-6_to_branch'      : des={'year0' :    16, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # probably not good - still used HAMMOC emissions
    elif expid=='N1850OCBDRDDMS_f19_tn14_CGC.27_mgd400.D-6_to_branch_Lana' : des={'year0' :    16, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_CGC.27_mgd400.D-6_to_branch_Lana' : des={'year0' :    16, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_standard_to_branch'               : des={'year0' :    16, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # 24-hourly coupling
    elif expid=='N1850OCBDRDDMS_f19_tn14_doublesalt'                       : des={'year0' :     1, 'year1' :  195, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_doublesalt'                       : des={'year0' :     1, 'year1' :  210, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_CGC.23_mgd400.D-6'                : des={'year0' :     1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_CGC.23_mgd400.D-6'                : des={'year0' :     1, 'year1' :   60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # cesm2.0 (June 2018 - Dirk) B1850
    elif expid=='GT18_B1850_f09_g17' : des={'year0' :    1, 'year1' :  61, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='GT21_B1850_f09_g17' : des={'year0' :    1, 'year1' :  54, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # cesm2.0 (July 2018 - Dirk) Only double seasalt (no double pom)
    elif expid=='casesGT19_N1850OCBDRDDMS_f19_tn14_onlyssltx2' : des={'year0' :    1, 'year1' :  36, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # 
    # cesm2.0 (August/September 2018 - Yanchun)
    elif expid=='N1850OCBDRDDMS_f19_tn14_2rosc1'  : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1'  : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='N1850OCBDRDDMS_f19_tn14_rfnc'    : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_rfncnew' : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_rfncnew' : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='N1850OCBDRDDMS_f19_tn14_2rosc1dp': des={'year0' :    1, 'year1' :  405, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1dp': des={'year0' :    1, 'year1' :  285, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='N1850OCBDRDDMS_f19_tn14_tkepf0bgmdcs'   : des={'description' : 'empty' , 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_tkepf0bgmdcs'   : des={'year0' :  106, 'year1' :  300, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # 
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1dd'       : des={'year0' :  106, 'year1' :  285, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1dpbcldfrc': des={'year0' :  106, 'year1' :  180, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1dpbTkeNiw': des={'year0' :   61, 'year1' :  315, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1dpbtkepf0': des={'year0' :   61, 'year1' :  345, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_TkeNiwbFeSi'    : des={'year0' :   61, 'year1' :  135, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N185DDMS_f09_tn14_2rosc1dpbTkeNiw'      : des={'description' : 'empty' , 'chem' : '', 'project' : ''}
    #
    elif expid=='N1850OCBDRDDMS_f09_tn14_2rosc1dpbcplhist': des={'year0' :  226, 'year1' : 235 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} 
    # Oyvind tuning tests
    elif expid=='N1850OCBDRDDMS_f19_tn14_2rosc1dp_gmdcsd' : des={'year0' :    1, 'year1' :  60 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_2rosc1dp_gm2dcsd': des={'year0' :    1, 'year1' :  60 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_2rosc1dp_gm3dcsd': des={'year0' :    1, 'year1' :  60 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_2rosc1dp_gtdu'   : des={'year0' :    1, 'year1' :  60 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gamtun'          : des={'year0' :    1, 'year1' : 165 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMSI_f19_tn14_init'           : des={'year0' :    1, 'year1' : 105 , 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
#
    elif expid=='N1850OCBDRDDMS_f19_tn14_gmdcsd_hivel'     : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gmdcsd_inc4'      : des={'year0' :    1, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_bicehdms'    : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_idms_gmd001' : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_idms_gmd003' : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_idms_gmd008' : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_idms_gmd018' : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gmd008_idy30'     : des={'year0' :   31, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_vilje'       : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_vn18_idy100'      : des={'year0' :  121, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # Oyvind -- Christmass 2018
    elif expid=='NF200climo_f19_f19_vd18'                    : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF200climo_f19_f19_vd18_ice4'               : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF200climo_f19_f19_vd18_ice4_ss'            : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF200climo_f19_f19_vd18_ice4_ss_icef'       : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF200climo_f19_f19_vd18_ice4_ss_icef_gm288' : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}

    elif expid=='N1850OCBDRDDMS_f19_tn14_201218'            : des={'year0' :    1, 'year1' : 135, 'model' : 'NorESM2', 'subdir' : '../../../.snapshots/Tuesday-15-Jan-2019/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_201218_ss_icef'    : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : '../../../.snapshots/Tuesday-15-Jan-2019/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_201218_ss_icef850' : des={'year0' :    1, 'year1' : 135, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_201218_gm270'      : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2', 'subdir' : '../../../.snapshots/Tuesday-15-Jan-2019/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_250119'            : des={'year0' :   91, 'year1' : 645, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    #
    # Mats spinup Christmass 2018
#    elif expid=='N1850OCBDRDDMS_f09_tn14_20181220'             : des={'year0' :    1, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirfram+'/../../../.snapshots/Tuesday-15-Jan-2019/noresm/cases','cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_20181220'            : des={'year0' :    1, 'year1' : 180, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_ice4_gam288_20181220': des={'year0' :    1, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : basedirfram+'/../../../.snapshots/Tuesday-15-Jan-2019/noresm/cases', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_lrg_20181220'        : des={'year0' :   91, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirfram+'/../../../.snapshots/Tuesday-15-Jan-2019/noresm/cases', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_egc_1p15_20181220'   : des={'year0' :   91, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_rhmaxi_1p1_20181220' : des={'year0' :   91, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_dms_20181220'        : des={'year0' :   91, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_20190204'            : des={'year0' :  121, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_qmxrhmin_20190204'   : des={'year0' :  121, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_qmxrhmin_gam280'     : des={'year0' :  151, 'year1' : 180, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_qmnmxrhmin_20190314' : des={'year0' :  121, 'year1' : 210, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f09_tn14_gam290_20190204'     : des={'year0' :  151, 'year1' : 180, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    #
    # Dirk spinup February 2019 - cesm2.1.0
    elif expid=='N1850OCBDRDDMS_f19_tn14_cesm2.1.0_20190202'   : des={'year0' :   91, 'year1' : 135, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # Ada NorESM2-CESM2.1.0 on nebula
    elif expid=='N1850OCBDRDDMS_f19_tn14_030319' : des={'year0' :   391, 'year1' : 400, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # Jens : slabocean
    elif expid=='NF1850-C2OD_f19tn14_E1850-201812' : des={'year0' :   1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} 
    #
    # (sst+4K equivalent) 
    elif expid=='NF1850_f09_f09_mg17_20190108'                  : des={'year0' :    1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850_f09_f09_mg17_ice4_gam288_20190108'      : des={'year0' :    1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850sst4K_f09_f09_mg17_20190108'             : des={'year0' :    1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='NF1850sst4K_f09_f09_mg17_ice4_gam288_20190108' : des={'year0' :    1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # cesm2.0 (September - Dirk - reference and 4xCO2) for CRESCENDO
    elif expid=='GT23_N1850OCBDRDDMS_f19_tn14' : des={'year0' :    1, 'year1' : 300, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='GT24_N1850OCBDRDDMS_f19_tn14' : des={'year0' :    1, 'year1' : 285, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='GT25_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # ref          : F1850 - fixed pre-industrial SST     
    elif expid=='GT26_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # sst+4k       : F1850 - fixed pre-industrial SST+4K
    elif expid=='GT27_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # 4xco2        : F1850 - fixed pre-industrial SST     + 4xCO2
    elif expid=='GT28_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # 4xco2 sst+4k : F1850 - fixed pre-industrial SST     + 4xCO2
    #
    elif expid=='GT32_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # sst+4kequatorial : F1850 - fixed pre-industrial SST+4K
    elif expid=='GT33_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # sst+4kpolar      : F1850 - fixed pre-industrial SST+4K
    # March 2019
    elif expid=='GT42_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # fsst - 2xCO2
    elif expid=='GT43_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # fsst - 4xCO2
    elif expid=='GT44_NF1850_f19_f19_mg17'     : des={'year0' :    1, 'year1' :  20, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # fsst - 8xCO2
    #
    elif expid=='GT29_N1850OCBDRDDMS_f19_tn14'    : des={'year0' :  151, 'year1' : 270, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} # 4xco2 (w.r.t. GT23, started later)
    elif expid=='GT29REF_N1850OCBDRDDMS_f19_tn14' : des={'year0' :  151, 'year1' : 270, 'model' : 'NorESM2', 'subdir' : 'GT23_N1850OCBDRDDMS_f19_tn14'+'/atm/hist', \
                                                         'subdirexpid' : 'GT23_N1850OCBDRDDMS_f19_tn14'+'/atm/hist/GT23_N1850OCBDRDDMS_f19_tn14' , 'chem' : '', 'project' : ''}
    elif expid=='GT30_N1850OCBDRDDMS_f19_tn14'    : des={'year0' :    1, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='GT31_N1850OCBDRDDMS_f19_tn14'    : des={'year0' :    1, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    elif expid=='N1850OCBDRDDMS_f19_tn14_gm250_v1000'          : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gm250_v1400'          : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gm250_v1400_amf'      : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gm250_v1400_dmef'     : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gm250_v1400_amf_dmef' : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_gm250_v1400_flx0'     : des={'year0' :    1, 'year1' :  60, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # cesm2.0 (August 2018 - Dirk) F2000clime =MAM4)
    elif expid=='F2000climo_f19_f19_mg17_GT05'                 : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='F2000climo_f09_f09_mg17_GT04'                 : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''} 
    #
    # cesm2.0.1 (November 2018 - Dirk)
    elif expid=='F2000climo_f09_f09_mg17_CS01'                 : des={'year0' :    1, 'year1' :  10, 'model' : 'CESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='F2000climo_f09_f09_mg17_CS02'                 : des={'year0' :    1, 'year1' :  10, 'model' : 'CESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='F2000climo_f09_f09_mg17_CS03'                 : des={'year0' :    1, 'year1' :  10, 'model' : 'CESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # CLUBB / NOCLUBB (Alf)
    elif expid=='N1850Clubb'                 : des={'year0' :   61, 'year1' :  105, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850CO2X4Clubb'            : des={'year0' :   61, 'year1' :  105, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850noClubb2'              : des={'year0' :   61, 'year1' :  210, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850CO2X4noClubb2'         : des={'year0' :   61, 'year1' :  210, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # Dirk March 2019 NorESM2.1.0
    elif expid=='N1850OCBDRDDMS_f19_tn14_20190304' : des={'year0' : 391, 'year1' :  420, 'model' : 'NorESM2', 'subdir' : '../../../FRAM/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_20190305' : des={'year0' : 391, 'year1' :  420, 'model' : 'NorESM2', 'subdir' : '../../../FRAM/noresm/cases/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #
    # Ada March 2019 : ICEOPT 4XCO2
    elif expid=='N1850OCBDRDDMS_4XCO2_f19_tn14_010319' : des={'year0' : 1850, 'year1' : 2069, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_REF_f19_tn14_010319'   : des={'year0' :  301, 'year1' :  520, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : 'N1850OCBDRDDMS_f19_tn14_250119', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_CTRL_f19_tn14_010319'  : des={'year0' : 1850, 'year1' : 2069, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # ICEOPT 5 : 4XCO2
    elif expid=='N1850OCBDRDDMSOPT5_4XCO2_f19_tn14_070319' : des={'year0' : 1890, 'year1' : 2039, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif expid=='N1850OCBDRDDMSOPT5_CTRL_f19_tn14_070319'  : des={'year0' : 1850, 'year1' : 2029, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # 
    elif expid=='N1850OCBDRDDMSOPT5_CTRL_f19_tn14_180319' : des={'year0' : 556, 'year1' :  595, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif expid=='N1850OCBDRDDMSOPT5_DST_f19_tn14_180319'  : des={'year0' : 556, 'year1' :  595, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif expid=='N1850OCBDRDDMSOPT5_DMS_f19_tn14_180319'  : des={'year0' : 556, 'year1' :  595, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    #
    # spinup neubul
    elif expid=='N1850OCBDRDDMS_f19_tn14_03042019' : des={'year0' : 421, 'year1' :  560, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_12042019' : des={'year0' : 561, 'year1' :  625, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   elif expid=='N1850OCBDRDDMS_f19_tn14_12042019' : des={'year0' : 577, 'year1' :  625, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_15042019' : des={'year0' : 626, 'year1' :  795, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}  # 799
    elif expid=='N1850OCBDRDDMS_f19_tn14_25042019' : des={'year0' : 796, 'year1' :  995, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}  # 997
    elif expid=='N1850OCBDRDDMS_f19_tn14_08052019' : des={'year0' : 996, 'year1' :  1035, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_10052019' : des={'year0' :1036, 'year1' :  1100, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 1104
    elif expid=='N1850OCBDRDDMS_f19_tn14_13052019' : des={'year0' :1101, 'year1' :  1375, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850_f19_tn14_11062019' : des={'year0' :1566, 'year1' :  1600, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}

    #
    # Oyvind March 2019
    elif expid=='N1850OCBDRDDMS_f19_tn14_250119_8XCO2'  : des={'year0' : 301, 'year1' : 390, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850OCBDRDDMS_f19_tn14_250119_REF'    : des={'year0' : 301, 'year1' : 390, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : 'N1850OCBDRDDMS_f19_tn14_250119', 'chem' : '', 'project' : ''}
    #
    # CMIP6 - testing DMS : taylorisation
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test7'  : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test8'  : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # not taylorized
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test9'  : des={'year0' : 1, 'year1' : 3, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test10' : des={'year0' : 1, 'year1' : 3, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # not taylorized
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test11' : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test13' : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized (old Lana-climatology)
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test15' : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized 
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test17' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized
    elif expid=='NF1850nbc_BGC_f19_mg17_20190709_test19' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized
    #
    elif expid=='NF1850_BGC_f19_mg17_20191509_test1'     : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # reference : standard SST, standard Lana
    #
    elif expid=='NFHISTnbc_BGC_f19_mg17_20190715_test2'  : des={'year0' : 1850, 'year1' : 1859, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # yes taylorized
    #
    elif expid=='NF1850nbc_BGC_f19_mg17_20190717_test1'  : des={'year0' : 1, 'year1' : 1, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850nbc_BGC_f19_mg17_20190717_test2'  : des={'year0' : 1, 'year1' : 1, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    #
    elif expid=='NF1850norbc_BGC_f19_mg17_20190718_test1'  : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # ICEFRAC=0
    elif expid=='NF1850norbc_BGC_f19_mg17_20190718_test2'  : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # ICEFRAC=0
    elif expid=='NFHISTnorbc_BGC_f19_mg17_20190718_test1'  : des={'year0' : 1850, 'year1' : 1859, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # ICEFRAC=0
    elif expid=='NFHISTnorbc_BGC_f19_mg17_20190718_test2'  : des={'year0' : 1850, 'year1' : 1859, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # ICEFRAC=0
    #
    elif expid=='NF1850norbc_BGC_f19_mg17_20190720_test1'  : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 
    elif expid=='NF1850norbc_BGC_f19_mg17_20190720_test2'  : des={'year0' : 1, 'year1' : 5, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 
    elif expid=='NFHISTnorbc_BGC_f19_mg17_20190720_test1'  : des={'year0' : 1850, 'year1' : 1854, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 
    elif expid=='NFHISTnorbc_BGC_f19_mg17_20190720_test2'  : des={'year0' : 1850, 'year1' : 1854, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} #
    # Kine march 2019 - cems2.0
    # Kettle DMS emissions
    elif expid=='N1850_f19_tn14_cesm2.0_CTRL'           : des='on its way'
    elif expid=='NHIST19REF'                            : des={'year0' :  271, 'year1' :  435, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : 'N1850OCBDRDDMS_f19_tn14_250119', 'chem' : '', 'project' : ''}
    elif expid=='NHIST19'                               : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 2. NHIST_f19_tn14_cesm2.0_start1850  
    elif expid=='N1950_19'                              : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 4. NHIST_f19_tn14_cesm2.0_start1950
    #
    # HAMOCC DMS emissions
    elif expid=='CTRL2_19'                              : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 1. N1850OCBDRDDMS_f19_tn14_cesm2.0_CTRL
    elif expid=='NHISTOCBDRDDMS_f19_tn14_cesm2.0_s1850' : des='on its way'
    elif expid=='NHISTOCBDRDDMS_f19_tn14_cesm2.0_s1950' : des={'year0' : 1950, 'year1' : 2009, 'model' : 'NorESM2', 'subdir' : basedirfram, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 5.
    #
    # cam5.3 / noresm_c1.2 Alf
    elif expid=='7310AMIP20002' : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : basedirsnapshot+'/aeroCAM53Ref', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='AMIP_PI_wPDoxi': des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2', 'subdir' : basedirsnapshot                , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # CRESCENDO WP6
    # free running
    elif expid=='WP6CS001ctrl_f19_f19'    : des={'year0' :    1991, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS003ctrl_f09_f09'    : des={'year0' :    1991, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirsnapshot+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS003emi1850_f09_f09' : des={'year0' :    1991, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirsnapshot+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS003emi1750_f09_f09' : des={'year0' :    1992, 'year1' :  2013, 'model' : 'NorESM2', 'subdir' : basedirsnapshot+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS004emi1750_f09_f09' : des={'year0' :    1991, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirsnapshot+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # PI sst
    elif expid=='WP6CS003emi1750_sst1850_f09_f09' : des={'year0' :    1992, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : '../olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # nudged
    elif expid=='WP6CS006ctrl_nudge_f09_f09'    : des={'year0' :    2001, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # 2019-08-09 : basedirsnapshot -> basedir
    elif expid=='WP6CS006emi1850_nudge_f09_f09' : des={'year0' :    2001, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_f09_f09' : des={'year0' :    2001, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # nudged sensitivity experiment   
    #elif expid=='WP6CS006ctrl_nudge_dms0.8_f09_f09'    : des={'year0' :    2008, 'year1' :  2010, 'model' : 'NorESM2', 'subdir' : '../olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    #elif expid=='WP6CS006emi1750_nudge_dms0.8_f09_f09' : des={'year0' :    2008, 'year1' :  2010, 'model' : 'NorESM2', 'subdir' : '../olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # FIRST SET (2008-2009-2010-2011) : nudged sensitivity experiment [TEMPORARILY on FRAM]
    # present-day
    elif expid=='WP6CS006ctrl_nudge_dms0.0_f09_f09'   :des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_dms0.5_f09_f09'   :des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_dms0.8_f09_f09'   :des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_dms2.0_f09_f09'   :des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # 1750
    elif expid=='WP6CS006emi1750_nudge_dms0.0_f09_f09':des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_dms0.5_f09_f09':des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_dms0.8_f09_f09':des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_dms2.0_f09_f09':des={'year0':2008,'year1':2011,'model':'NorESM2','subdir':'../../../FRAM/noresm/olivie/crescendo/'+expid+'/atm/hist', 'chem' : '', 'project' : ''}
    # SECOND SET (2012-2013-2014)   
    # present-day
    # sslt  
    elif expid=='WP6CS006ctrl_nudge_sslt0.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_sslt0.5_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_sslt2.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # opom  
    elif expid=='WP6CS006ctrl_nudge_opom0.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_opom0.5_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_opom2.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # voc
    elif expid=='WP6CS006ctrl_nudge_voc0.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_voc0.5_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_voc2.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # dst  
    elif expid=='WP6CS006ctrl_nudge_dst0.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_dst0.5_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006ctrl_nudge_dst2.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # dms
    elif expid=='WP6CS007ctrl_nudge_dms0.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS007ctrl_nudge_dms0.5_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS007ctrl_nudge_dms2.0_f09_f09'     :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # 1750 
    # sslt  
    elif expid=='WP6CS006emi1750_nudge_sslt0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_sslt0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_sslt2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # opom  
    elif expid=='WP6CS006emi1750_nudge_opom0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_opom0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_opom2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # voc
    elif expid=='WP6CS006emi1750_nudge_voc0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_voc0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_voc2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # dst  
    elif expid=='WP6CS006emi1750_nudge_dst0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_dst0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1750_nudge_dst2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # dms
    elif expid=='WP6CS007emi1750_nudge_dms0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS007emi1750_nudge_dms0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS007emi1750_nudge_dms2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # 1850
    # sslt  
    elif expid=='WP6CS006emi1850_nudge_sslt0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_sslt0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_sslt2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # opom  
    elif expid=='WP6CS006emi1850_nudge_opom0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_opom0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_opom2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # voc
    elif expid=='WP6CS006emi1850_nudge_voc0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_voc0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_voc2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # dst  
    elif expid=='WP6CS006emi1850_nudge_dst0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_dst0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_dst2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    # dms
    elif expid=='WP6CS006emi1850_nudge_dms0.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_dms0.5_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='WP6CS006emi1850_nudge_dms2.0_f09_f09'  :des={'year0':2012,'year1':2014,'model':'NorESM2','subdir' : basedir+'/../olivie/crescendo', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# CMIP6 - cpl
#   piControl [2x2]
    elif expid=='N1850_f19_tn14_20190621'          : des={'year0' : 1600, 'year1' : 1800, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid,                     'clmh0' : 'monthlyuntil1700' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20190621len165'    : des={'year0' : 1600, 'year1' : 1764, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : 'N1850_f19_tn14_20190621', 'clmh0' : 'monthlyuntil1700' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850_f19_tn14_20190621_1701_1800': des={'year0' : 1701, 'year1' : 1800, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : 'N1850_f19_tn14_20190621', 'clmh0' : 'monthlyuntil1700' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850_f19_tn14_20190722'          : des={'year0' : 1801, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid,                     'clmh0' : 'annual' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850_f19_tn14_20190802'          : des={'year0' : 1901, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid,                     'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850_f19_tn14_20190621ext'       : des={'year0' : 1600, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : ''            , 'cexpid' : expid,                     'clmh0' : ''                 , 'chem' : '', 'globdatadir': '', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   piControl [1x1]    
    elif expid=='N1850frc2_f09_tn14_20191001'      : des={'year0' : 1200, 'year1' : 1299, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850frc2_f09_tn14_20191012'      : des={'year0' : 1300, 'year1' : 1449, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # contains also 1450
    elif expid=='N1850frc2_f09_tn14_20191012len65'      : des={'year0' : 1300, 'year1' : 1364, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : 'N1850frc2_f09_tn14_20191012', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#   elif expid=='N1850frc2_f09_tn14_20191012_1320_1349' : des={'year0' : 1320, 'year1' : 1349, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : 'N1850frc2_f09_tn14_20191012', 'chem' : '', 'project' : ''}
#   elif expid=='N1850frc2_f09_tn14_20191012_1351_1380' : des={'year0' : 1351, 'year1' : 1380, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : 'N1850frc2_f09_tn14_20191012', 'chem' : '', 'project' : ''}
    elif expid=='N1850frc2_f09_tn14_20191113'           : des={'year0' : 1450, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850frc2_f09_tn14_20191001ext'   : des={'year0' : 1200, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : ''            , 'cexpid' : expid, 'clmh0' : '' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#
#   abrupt-4xCO2
    elif expid=='NCO2x4_f19_tn14_20190624'         : des={'year0' :    1, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly',  'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # goes until 140
    elif expid=='NCO2x4_f19_tn14_20190705'         : des={'year0' :  121, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid,                       'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NCO2x4_f19_tn14_20190724'         : des={'year0' :  151, 'year1' : 500, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#   abrupt-4xCO2 f09
    elif expid=='NCO2x4frc2_f09_tn14_20191008'     : des={'year0' :    1, 'year1' : 120, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NCO2x4frc2_f09_tn14_20191028'     : des={'year0' :  121, 'year1' : 150, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#
#   1pctCO2
    elif expid=='N1PCT_f19_tn14_20190626'          : des={'year0' :    1, 'year1' :  120, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1PCT_f19_tn14_20190712'          : des={'year0' :  121, 'year1' :  165, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1PCTRADfrc2_f19_tn14_20191213'   : des={'year0' :    1, 'year1' :  140, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1PCTBGC_f19_tn14_20190629'       : des={'year0' :    1, 'year1' :  140, 'model' : 'NorESM2', 'subdir' : basedirns2345k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} 
#   1pctCO2 f09
    elif expid=='N1PCTfrc2_f09_tn14_20191008'      : des={'year0' :    1, 'year1' :  120, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}   
    elif expid=='N1PCTfrc2_f09_tn14_20191028'      : des={'year0' :  121, 'year1' :  150, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#
#   historical [2x2]
    elif expid=='NHIST_f19_tn14_20190625'          : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_f19_tn14_20190710'          : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_f19_tn14_20190625ext'       : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', 'project' : ''}
    elif expid=='NHIST_02_f19_tn14_20190801'       : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_02_f19_tn14_20190813'       : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_02_f19_tn14_20190801ext'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', 'project' : ''}
    elif expid=='NHIST_03_f19_tn14_20190801'       : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_03_f19_tn14_20190813'       : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}    
    elif expid=='NHIST_03_f19_tn14_20190801ext'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', 'project' : ''}

#   historical [1x1]
    elif expid=='NHISTfrc2_f09_tn14_20191001'      : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_f09_tn14_20191025'      : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_f09_tn14_20191001ext'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', 'project' : ''}
    elif expid=='NHISTfrc2_02_f09_tn14_20200427'   : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_02_f09_tn14_20200519'   : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_02_f09_tn14_20200427ext': des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', 'project' : ''}
    elif expid=='NHISTfrc2_03_f09_tn14_20200519'   : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} ; cdir='NHISTfrc2_03_f09_tn14_20200519.err'
    elif expid=='NHISTfrc2_03_f09_tn14_20200619'   : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual' , 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_03_f09_tn14_20200519ext': des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', 'project' : ''}
    elif expid=='NHISTfrc2_f09_tn14_20200718'      : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # identical to member 1 + AEROCOM output

#    
#   scenarios
    elif expid=='NSSP126frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245frc2_02_f19_tn14_20191014' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245frc2_03_f19_tn14_20191014' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP370frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP370frc2_02_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP370frc2_03_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP370LOWNTCFfrc2_f19_tn14_20191118'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP370LOWNTCFfrc2_02_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP370LOWNTCFfrc2_03_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP370REFGHGLOWNTCFfrc2_f19_tn14_20191220'    : des={'year0' : 2015, 'year1' : 2059, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP370REFGHGLOWNTCFfrc2_02_f19_tn14_20191220' : des={'year0' : 2015, 'year1' : 2059, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP370REFGHGLOWNTCFfrc2_03_f19_tn14_20191220' : des={'year0' : 2015, 'year1' : 2059, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP585frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#   
    elif expid=='NFSSP370frc2norbc_f19_20200110'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP370frc2norbc_aerlow_f19_20200110' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
    elif expid=='NFSSP245frc2norpibc_f19_20200520'                : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_02_f19_20200703'             : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_03_f19_20200703'             : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_ghgonly_f19_20200522'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_ghgonly_02_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_ghgonly_03_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_natonly_f19_20200522'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_natonly_02_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_natonly_03_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_aeroxidonly_f19_20200522'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_aeroxidonly_02_f19_20200703' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_aeroxidonly_03_f19_20200703' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_aeronly_f19_20200522'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_aeronly_02_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_aeronly_03_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
  
    elif expid=='NFSSP245frc2norpibc_ghgonly_f19_20200522' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
    elif expid=='b.e21.NSSP126frc2.f19_tn14.CMIP6-SSP1-2.6-SSP3-7.0Lu.001' : des={'year0' : 2015, 'year1' : 2099, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='b.e21.NSSP370frc2.f19_tn14.CMIP6-SSP3-7.0-SSP1-2.6Lu.001' : des={'year0' : 2015, 'year1' : 2099, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#
#   scenarios f09
    elif expid=='NSSP126frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '','globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '','globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP370frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '','globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP585frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '','globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP585frc2_f09_tn14_20200919'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns2345k, 'cexpid' : expid, 'clmh0' : 'annual', 'chem' : '','globdatadir': 'timeblocks-v2', 'project' : ''}
#
#   historical damip
    elif expid=='N1850aeroxidonly_f19_tn14_20190805'    : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850aeroxidonly_f19_tn14_20190815'    : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#    elif expid=='N1850aeroxidonly_f19_tn14_20190805ext' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': '', 'project' : ''}
    elif expid=='N1850aeroxidonly_02_f19_tn14_20190909' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850aeroxidonly_03_f19_tn14_20190913' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850ghgonly_f19_tn14_20190712'        : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850ghgonly_02_f19_tn14_20190909'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850ghgonly_03_f19_tn14_20190913'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850natonly_f19_tn14_20190805'        : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850natonly_f19_tn14_20190815'        : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#   elif expid=='N1850natonly_f19_tn14_20190805ext'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': '', 'project' : ''} 
    elif expid=='N1850natonly_02_f19_tn14_20190909'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850natonly_03_f19_tn14_20190913'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}

#   historical aerchemmip
    elif expid=='NHISTpiaer_f19_tn14_20190721'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTpiaer_02_f19_tn14_20190909'  : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTpiaer_03_f19_tn14_20190909'  : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTpintcf_f19_tn14_20190720'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTpintcf_02_f19_tn14_20190909' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTpintcf_03_f19_tn14_20190909' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}    
#
# CMIP6 - cpl on BETZY
#   piControl on betzy [2x2]
    elif expid=='N1850_f19_tn14_20210317b'         : des={'year0' : 1600, 'year1' : 1899, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # Dirk 
    elif expid=='N1850_f19_tn14_20210409b'         : des={'year0' : 1611, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # Dirk 
    elif expid=='N1850_f19_tn14_20210409c'         : des={'year0' : 1621, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # Dirk 
#   piControl on betzy [1x1]
    elif expid=='N1850_f09_tn14_keyClim20201217'   : des={'year0' : 1200, 'year1' : 1229, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Oyvind
    elif expid=='N1850frc2_betzy_v1'               : des={'year0' : 1200, 'year1' : 1238, 'model' : 'NorESM2', 'subdir' : basedirns9560k+'/../../users/heig/NorESM/archive', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Heiko
#   historical on betzy [1x1]
    elif expid=='NHIST_f09_tn14_20201218'          : des={'year0' : 1850, 'year1' : 1879, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Oyvind

# CMIP6 SP-aeroosl
#   piClim-spAer-aer
#   elif expid=='piClim-SpAer2014'                          : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Alf (on vilje)
#   elif expid=='NF1850norbc_spAer_aer2014_f19_20210523'    : des={'year0' :    1, 'year1' :   90, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Dirk (on betzy)
#   piClim-spAer-anthro
#   elif expid=='piClim-SpAer-anthro'                       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Alf (on vilje)
#   elif expid=='NF1850norbc_spAer_anthro2014_f19_20210523' : des={'year0' :    1, 'year1' :   90, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Dirk (on betzy)  
#   piClim-spAer-histaer
#   elif expid=='NFHISTnorpibc_spAer_aeronly_f19_20210523'  : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # Dirk (on betzy)
#   historical    
    elif expid=='NHIST_spAer_f19_tn14_20190925'             : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # Alf (on fram)
    elif expid=='NHIST_spAer_f19_tn14_20210523'             : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # Dirk (on Betzy)
#    
# CMIP6 - sst
    elif expid=='NF1850norbc_f19_mg17_20190721'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   30-year
    elif expid=='NF1850norbc_f19_20190727'              : des={'year0':1,'year1':170,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2','project' : ''}
    elif expid=='NF1850norbc_f19_20190727len30'         : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : 'NF1850norbc_f19_20190727', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_20190727len165'        : des={'year0':1,'year1':165,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : 'NF1850norbc_f19_20190727', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_f19_20190727len170'        : des={'year0':1,'year1':170,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : 'NF1850norbc_f19_20190727', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_4xco2_f19_20190727'        : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_2xco2_f19_20191007'        : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ghg2014_f19_20190727'      : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ghgnoh2o2014_f19_20190924' : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ch42014_f19_20190928'      : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ch4noh2o2014_f19_20190928' : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_n2o2014_f19_20190928'      : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}

    elif expid=='NF1850norbc_aer2014_f19_20190727'      : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_aeroxid2014_f19_20190811'  : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_bc2014_f19_20190727'  : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_oc2014_f19_20190727'  : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_so22014_f19_20190727' : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_so2oxid2014_f19_20190727' : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}

    elif expid=='NF1850norbc_ozone2014_f19_20190727'   : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_oxid2014_f19_20190914'    : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_h2o2014_f19_20190909'    : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ntcf2014_f19_20190811'    : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_anthro2014_f19_20190811'  : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='piClim-lu2deg'                        : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='piClim-SpAer2014'                     : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='piClim-SpAer-anthro'                  : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   30-year - flux=1 and cosz=true
    elif expid=='NF1850norbc_f19_20191025'             : des={'year0':1,'year1':200,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_f19_20191025len30'        : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : 'NF1850norbc_f19_20191025' , 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_f19_20191025len90'        : des={'year0':1,'year1': 90,'model':'NorESM2','subdir' : basedir, 'cexpid' : 'NF1850norbc_f19_20191025' , 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_f19_20191025len165'       : des={'year0':1,'year1':165,'model':'NorESM2','subdir' : basedir, 'cexpid' : 'NF1850norbc_f19_20191025', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_4xco2_f19_20191025'       : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2xco2_f19_20191025'       : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_ghg2014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ghgnoh2o2014_f19_20191025': des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_co22014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ch42014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ch4noh2o2014_f19_20191025': des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_n2o2014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # error : was identical to ch42014
    elif expid=='NF1850norbc_n2o2014_f19_20200908'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#    
    elif expid=='NF1850norbc_aer2014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aeroxid2014_f19_20191025' : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : '','globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_bc2014_f19_20191025'      : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_oc2014_f19_20191025'      : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_so22014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_so2oxid2014_f19_20191025' : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
    elif expid=='NF1850norbc_ozone2014_f19_20191025'   : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_oxid2014_f19_20191025'    : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_h2o2014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ntcf2014_f19_20191025'    : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_anthro2014_f19_20191025'  : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_lu2014_f19_20191025'      : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   spAer
    elif expid=='NF1850norbc_spAer_aer2014_f19_20210523'      : des={'year0':1,'year1': 90,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_spAer_aer2014_f19_20210523len30' : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : 'NF1850norbc_spAer_aer2014_f19_20210523', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_spAer_anthro2014_f19_20210523'   : des={'year0':1,'year1': 90,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}    
#         (correct Gahn diagnostics)
    elif expid=='NF1850norbc_spAer_aer2014_f19_20230127'       : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : scratchdir,     'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_spAer_anthro2014_f19_20230127'    : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : scratchdir,     'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   30-year - flux=1 and different DMS emissions
    elif expid=='NF1850norbc_f19_20200303'             : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   natural emissions
    elif expid=='NF1850norbc_f19_20190805'             : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2dms_f19_20190805'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2dust_f19_20190805'        : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2pom_f19_20190805'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2ss_f19_20190805'          : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2voc_f19_20190805'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
#   natural emissions : flux=1 and cosz=true [PROBLEM : missing months]
    elif expid=='NF1850norbc_f19_20191004'             : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2dms_f19_20191004'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2dust_f19_20191004'        : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2pom_f19_20191004'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2ss_f19_20191004'          : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2voc_f19_20191004'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
#   natural emissions : flux=1 and cosz=true
    elif expid=='NF1850norbc_f19_20200219'             : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2dms_f19_20200219'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc2dust_f19_20200219'        : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2pom_f19_20200219'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2ss_f19_20200219'          : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc2voc_f19_20200219'         : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# CMIP6 - fsst - f09
    elif expid=='NF1850frc2norbc_f09_20200108'             : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850frc2norbc_4xco2_f09_20200108'       : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
    elif expid=='NF1850frc2norbc_aeroxid2014_f09_20200108' : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
    elif expid=='NF1850frc2norbc_aer2014_f09_20200108'     : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
    elif expid=='NF1850frc2norbc_oxid2014_f09_20200108'    : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
#
#   aerchemmip fSST historical [flux=0]
    elif expid=='NFHISTnorbc_f19_20190730'          : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorbc_piaer_f19_20190730'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_pintcf_f19_20190730'   : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   aerchemmip fSST historical [flux=1]
    elif expid=='NFHISTnorbc_f19_20191107'          : des={'year0':1970,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorbc_piaer_f19_20191107'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorbc_pintcf_f19_20191107'   : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   rfmip fSST historical [flux=0]
    elif expid=='NFHISTnorpibc_f19_20190810'               : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_02_f19_20190909'            : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_03_f19_20190923'            : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeroxidonly_f19_20190810'   : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # aeroxidonly
    elif expid=='NFHISTnorpibc_aeroxidonly_02_f19_20190909': des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeroxidonly_03_f19_20190923': des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_ghgonly_f19_20190810'       : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # ghgonly
    elif expid=='NFHISTnorpibc_ghgonly_02_f19_20190909'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_ghgonly_03_f19_20190923'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir,        'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_natonly_f19_20190810'       : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # natonly
    elif expid=='NFHISTnorpibc_natonly_02_f19_20190909'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_natonly_03_f19_20190923'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_ozoneonly_f19_20190924'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''} # ozoneonly
    elif expid=='NFHISTnorpibc_ozoneonly_02_f19_20190925'  : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_ozoneonly_03_f19_20190925'  : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_f19_20191208'        : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_f19_20191129'        : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_02_f19_20191129'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_03_f19_20191129'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#   rfmip fSST historical [flux=1]
    elif expid=='NFHISTnorpibc_f19_20191208'                : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_02_f19_20200118'             : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_03_f19_20200118'             : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_ghgonly_f19_20191208'        : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_ghgonly_02_f19_20200118'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_ghgonly_03_f19_20200118'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeroxidonly_f19_20191208'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeroxidonly_02_f19_20200118' : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeroxidonly_03_f19_20200118' : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_natonly_f19_20191208'        : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_natonly_02_f19_20200118'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_natonly_03_f19_20200118'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
#
    elif expid=='NFHISTnorpibc_oxidonly_f19_20200204'    : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_oxidonly_02_f19_20200204' : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_oxidonly_03_f19_20200204' : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeronly_f19_20200204'     : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeronly_02_f19_20200204'  : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeronly_03_f19_20200204'  : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir': 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpibc_ozoneonly_f19_20200204'   : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_ozoneonly_02_f19_20200204': des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_ozoneonly_03_f19_20200204': des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_f19_20200204'      : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_02_f19_20200204'   : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_luonly_03_f19_20200204'   : des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}#
#   spAer
    elif expid=='NFHISTnorpibc_spAer_aeronly_f19_20210523' :  des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   amip 1975-2014 
    elif expid=='NFHISTnorpddmsbc_f19_mg17_20190807': des={'year0':1975,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
    elif expid=='NF1850norbc_2xdms60n90n_f19_20190924': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirnatsens, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_2xdms30n60n_f19_20190924': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirnatsens, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_2xdms00n30n_f19_20190924': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirnatsens, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_2xdms30s00s_f19_20190924': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirnatsens, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_2xdms60s30s_f19_20190924': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirnatsens, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_2xdms90s60s_f19_20190924': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirnatsens, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
#   COVID 19 : original (with error in 2015-2018 emissions) : factor two too large in 2015
#   member 01 (with error)
    elif expid=='NSSP245frc2covbaslin_01_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_01_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_01_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_01_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_01_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 02 (with error)
    elif expid=='NSSP245frc2covbaslin_02_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_02_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_02_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_02_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_02_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 03 (with error)
    elif expid=='NSSP245frc2covbaslin_03_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_03_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_03_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_03_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_03_f19_tn14_20200719'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 04 (corrected)
    elif expid=='NSSP245frc2covbaslin_04_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_04_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_04_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_04_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_04_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 05 (corrected)
    elif expid=='NSSP245frc2covbaslin_05_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_05_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_05_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_05_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_05_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 06 (corrected)
    elif expid=='NSSP245frc2covbaslin_06_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_06_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_06_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_06_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_06_f19_tn14_20200723'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   COVID 19 : corrected
#   member 01
    elif expid=='NSSP245frc2covbaslin_01_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_01_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_01_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_01_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_01_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 02
    elif expid=='NSSP245frc2covbaslin_02_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_02_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_02_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_02_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_02_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 03
    elif expid=='NSSP245frc2covbaslin_03_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_03_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_03_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_03_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_03_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
#   COVID 19 : corrected
#   member 07 = 01b
    elif expid=='NSSP245frc2covbaslin_01b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_01b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_01b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_01b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_01b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 08 = 02b
    elif expid=='NSSP245frc2covbaslin_02b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_02b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_02b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_02b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_02b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   member 09 = 03b
    elif expid=='NSSP245frc2covbaslin_03b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_03b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_03b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_03b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_03b_f19_tn14_20200922'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
#   member 10
    elif expid=='NSSP245frc2covbaslin_10_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covfosfue_10_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covmodgre_10_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covstrgre_10_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NSSP245frc2covtwobli_10_f19_tn14_20200823'   : des={'year0':2015,'year1':2050,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}   
#
#   COVID 19 : radiative forcing of aerosols
    elif expid=='NFSSP245frc2norpibc_covbaslin2020_f19_20201228'             : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2021_f19_20201228'             : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2023_f19_20201228'             : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2030_f19_20201228'             : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2040_f19_20201228'             : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2050_f19_20201228'             : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2020covtwobliaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2021covtwobliaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2030covfosfueaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2040covfosfueaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2050covfosfueaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2030covmodgreaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2040covmodgreaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2050covmodgreaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2030covstrgreaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2040covstrgreaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFSSP245frc2norpibc_covbaslin2050covstrgreaer_f19_20201228' : des={'year0': 1,'year1':60,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_2xco2_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2','project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_4xco2_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2','project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aeroxid2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2','project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_bc2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ch42014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ch4noh2o2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#    elif expid=='NF1850norbc_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_ghg2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_n2o2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_so22014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_so2oxid2014_f19_20191025': des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# AEROCOM2019 : Alf
    elif  expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20191101'          : des={'year0':2005,'year1':2013,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif  expid=='NFHISTnorpddmsbcsdyn_u3p41_f09_mg17_20200915'    : des={'year0' : 2005, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
# AEROCOM2019 for Maria Sand (run on Betzy) : initial setup -> results quite DIFFERENT from Alf's orginal simulation (which was on vilje)
    elif  expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20210415'          : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nodst_f09_mg17_20210415'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nobc_f09_mg17_20210415'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_noom_f09_mg17_20210415'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nopom_f09_mg17_20210415'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nosoa_f09_mg17_20210415'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
# AEROCOM2019 for Maria Sand (run on Betzy) : used Alf's repository -> results more SIMILAR to Alf's original simulation (which was on vilje)
    elif  expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20210420'          : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nodst_f09_mg17_20210420'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nobc_f09_mg17_20210420'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_noom_f09_mg17_20210420'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nopom_f09_mg17_20210420'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nosoa_f09_mg17_20210420'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
#
# Maria Sand
    elif expid=='NF_2016_AMAP_type0' : des={'year0' : 2016, 'year1' : 2016, 'model' : 'NorESM1', 'subdir' : '/scratch/olivie/backup', 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# BETZY fSST
    elif expid=='NF1850norbc_f19_20201226'                : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345k , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_sstp4k_f19_20201226'         : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345k , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}

# OZONE Dirk
    elif expid=='FC2010climo_f19_20210204_test1'                : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='FC2010climo_f19_mg17_20210204_test1'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='FC2010climo_f09_mg17_20210204_test1'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
#
    elif expid=='FC2010climo_prep_f19_20210204_test5'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test6'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test7'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test9'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test10'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test11'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test12'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test13'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test17'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
#
    elif expid=='NF1850norbc_tropstratchem_f19_20210331_test14' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test01' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test02' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test03' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test04' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test05' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test06' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test08' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test09' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test10' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test11' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test12' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
#
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test01' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test03' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test04' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test05' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test06' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test07' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test08' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test09' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test10' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test11' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test12' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test13' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test14' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test15' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test16' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test17' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test18' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test19' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test20' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test21' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
#
#   CAM-Nor standard, but with CESM2 settings (emissions, gamma, c0, c1, ...)
    elif expid=='NF2010norpddmsbc_prep_f19_20211214_test01' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF2010norpddmsbc_prep_f19_20211214_test02' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
#   N1850 f09/f19
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test03' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # no DMS emissions 
    elif expid=='N1850_tropstratchem_prep_f09_nt14_20211217_test04' : des={'year0' : 1, 'year1' : 25, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # no DMS emissions
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test05' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test06' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test07' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test08' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}

    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test01' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test02' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test03' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test04' : des={'year0' : 1, 'year1' :100, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test09' : des={'year0' : 1, 'year1' :100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test11' : des={'year0' : 1, 'year1' :60,  'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12' : des={'year0' : 1, 'year1' :120,  'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14' : des={'year0' : 1, 'year1' :160,  'model' : 'NorESM2', 'subdir' : lakedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   NHIST f09
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01' : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01_from1880' : des={'year0' : 1880, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : 'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02'          : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02_from1860' : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : 'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02' , 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03'          : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : lakedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   NSSPP585 f09 
    elif expid=='NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01'        : des={'year0' : 2015, 'year1' : 2100,  'model' : 'NorESM2', 'subdir' : lakedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   NFHIST fullchemistry    
#   [2x2]   
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test01' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test06' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test07' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test12' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test19' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test20' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test21' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test22' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test24' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test25' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   [1x1]
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test12' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test13' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test15' : des={'year0' : 1970, 'year1' : 1971, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
 
#   NF1850norbc_fullchemistry
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f09_20220105_test02' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test03' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test04' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test05' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f09_20220105_test07' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test08' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test09' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test10' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test11' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
# 
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test03' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test07' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test08' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test09' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test10' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test12' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test13' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test14' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test15' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test16' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test17' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test18' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_reduced_f19_20220105_test19' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
# 
#   FCHIST startign 1850-...
#   noresm repository
    elif expid=='FCHIST_f19_20220111_test1'               : des={'year0' : 1850, 'year1' : 1859, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='FCHIST_f19_mg17_20220111_test1'          : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='FCHIST_f19_mg17_20220111_test1_from1860' : des={'year0' : 1860, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : 'FCHIST_f19_mg17_20220111_test1', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='FCHIST_f09_mg17_20220111_test2'          : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='FCHIST_f19_mg17_20220111_test3'          : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # without cam/src/NorESM
    elif expid=='FCHIST_f09_mg17_20220111_test4'          : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # without cam/src/NorESM
    elif expid=='FCHIST_f19_mg17_20220111_test5'          : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # scaled lightning production to same as f09
    elif expid=='FCHIST_f19_mg17_20220111_test6'          : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='FCHIST_f09_mg17_20220111_test7'          : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
 
#   cesm2.1.3
    elif expid=='FCHIST_f09_f09_mg17_20211217_test01' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # CESM2.1.3 
    elif expid=='FCHIST_f19_f19_mg17_20211217_test02' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # CESM2.1.3 
    elif expid=='FCHIST_f19_f19_mg17_20211217_test03' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''} # CESM2.1.3, but (DCS=500.D-6, gamma=0.308, seasalt-scaling=1.0 back to old unscaled 1x1 values)
#   cesm2.1.0
    elif expid=='FCHIST_f09_f09_mg17_20220202_test01' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}
    elif expid=='FCHIST_f19_f19_mg17_20220202_test02' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'project' : ''}

# VSLS Dirk
    elif expid=='NF1850norbc_prep_f19_20210204_test5'     : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_prep_f19_20210204_test8'     : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='N1850frc2_bromo_f19_tn14_20210323_test3' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}     
    elif expid=='N1850frc2_bromo_f19_tn14_20210323_test4' : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}     
    elif expid=='N1850frc2_bromo_f19_tn14_20210323_test5' : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}    
#   to have extra output for the bromoform runs
#   test
    elif expid=='NHISTfrc2_bromo_prep_f19_tn14_20230912_test05' : des={'year0' : 1990, 'year1' :  1990, 'model' : 'NorESM2', 'subdir' : basedirns9560kbromo, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_bromo_prep_f19_tn14_20230912_test06' : des={'year0' : 1990, 'year1' :  1990, 'model' : 'NorESM2', 'subdir' : basedirns9560kbromo, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
#   actual simulation (rerunning brom_08)
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1850'   : des={'year0' : 1850, 'year1' :  1869, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1870'   : des={'year0' : 1870, 'year1' :  1989, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1990'   : des={'year0' : 1990, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1850ext': des={'year0' : 1850, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP585frc2_f19_tn14_bromo_08_r2015' : des={'year0' : 2015, 'year1' :  2079, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP585frc2_f19_tn14_bromo_08_r2080' : des={'year0' : 2080, 'year1' :  2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
# CAMS-VSLS-DMS
#   1st member
    elif expid=='NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01'   : des={'year0' : 1995, 'year1' :  2004, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   activate energy correction    
    elif expid=='NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim02'   : des={'year0' : 1995, 'year1' :  2004, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # energy correction active
    elif expid=='NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim03'   : des={'year0' : 1995, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # energy correction active
    elif expid=='NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03' : des={'year0' : 2015, 'year1' :  2023, 'model' : 'NorESM2', 'subdir' : basedirns9560kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03' : des={'year0' : 1995, 'year1' :  2023, 'model' : 'NorESM2', 'subdir' : basedirns9560kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   2nd member
    elif expid=='NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01' : des={'year0' : 1995, 'year1' :  2004, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   prolongtation 2024-2025
    elif expid=='NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03_2024_2025' : des={'year0' : 2024, 'year1' :  2025, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# VSLS Jerry
    elif expid=='N1850frc2_f19_tn14_bromo_02'             : des={'year0' :    1, 'year1' :   20, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}     
    elif expid=='N1850frc2_f19_tn14_bromo_04'             : des={'year0' :    1, 'year1' :   20, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}    
    elif expid=='N1850frc2_f19_tn14_bromo_07'             : des={'year0' :    1, 'year1' :  100, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} 
    elif expid=='N1850frc2_f19_tn14_bromo_08'             : des={'year0' : 1600, 'year1' : 2149, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='NHISTfrc2_f19_tn14_bromo_08'             : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='NSSP126frc2_f19_tn14_bromo_08'           : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='NSSP585frc2_f19_tn14_bromo_08'           : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
#
# N2O coupling Dirk/Joran 
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20230318_test02' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20230318_test04' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# N2O land coupling Dirk
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test01' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test02' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test03' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test04' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test05' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test07' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# N2O coupling Joeran
#   600 year spinup
    elif expid=='Ncyc-spinup-01-1deg-noresm2.1.3BLOM-enhanced-v1.6.9-NOINYOC' : des={'year0' : 1, 'year1' : 800, 'model' : 'NorESM2', 'subdir' : basedirns2980k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}

    elif expid=='NorESM-Ncyc_uncoupled-01_N1850vsls_tropstratchem_prep_f19_tn14_noresm2.0.2-BLOMv1.6.9enhanced_20250911T1754' : des={'year0' : 1, 'year1' : 52, 'model' : 'NorESM2', 'subdir' : basedirns2980k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}    
    elif expid=='NorESM-Ncyc_coupled-01_N1850vslsn2onh3_tropstratchem_prep_f19_tn14_noresm2.0.2-BLOMv1.6.9enhanced_20250917T1358' : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : basedirns2980k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}    
#
#   400 year spinup
    elif expid=='NorESM-Ncyc_N1850_f19_tn14_NorESM2.0.9_BLOMv1.6.X_20251128T2117' : des={'year0' : 1, 'year1' : 400, 'model' : 'NorESM2', 'subdir' : lakedirns2980k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '',  'globdatadir' : 'timeblocks-v2', 'project' : ''}

#
# N2O coupling Dirk
    elif expid=='N1850vslsn2onh3_f19_tn14_test01b' : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test02'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test03'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test04'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test05'  : des={'year0' : 31, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test06'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test07'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test08'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test09'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test10'  : des={'year0' : 31, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    
    elif expid=='N1850vslsn2onh3_f19_tn14_test11'  : des={'year0' : 31, 'year1' : 45, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}    

# CH4 coupling
    elif expid=='N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kch4test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}    
    elif expid=='N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test04' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns9560kch4test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}    
    elif expid=='N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test05' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns9560kch4test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}    
    elif expid=='N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test06' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns9560kch4test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}    
    elif expid=='N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test07' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kch4test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : ''}   
#
# CH4 coupling AMIP
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_f19_20250416_test01'                  : des={'year0' : 1979, 'year1' : 1983, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_nodfch4_s01_20250416'    : des={'year0' : 1960, 'year1' : 1964, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_1xdfch4_s01_20250416'    : des={'year0' : 1960, 'year1' : 1964, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_0.05xdfch4_s01_20250416' : des={'year0' : 1960, 'year1' : 1964, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_20xdfch4_s01_20250416'   : des={'year0' : 1960, 'year1' : 1964, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}

    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506'   : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s02_esm2025_20250506'   : des={'year0' : 1950, 'year1' : 1959, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s03_esm2025_20250506'   : des={'year0' : 1950, 'year1' : 1959, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506'   : des={'year0' : 1960, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ch4, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#
# HYWAY project
    elif expid=='NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   ssp245
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_20250521'       : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521'   : des={'year0' : 2000, 'year1' : 2019, 'model' : 'NorESM2', 'chem' : 'fullchem'}
#   ssp245 3hourly
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_3hr2015_20250521'       : des={'year0' : 2015, 'year1' : 2015, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_3hr2019_20250521'       : des={'year0' : 2019, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   ssp585
    elif expid=='NFSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_20250521'       : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTSSP585norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521'   : des={'year0' : 2000, 'year1' : 2019, 'model' : 'NorESM2', 'chem' : 'fullchem'}
#   H2 emissions test    
    elif expid=='NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep1p0_s01_hyway_20260315' : des={'year0' : 2010, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2010_h2emi_h2dep0p7_s01_hyway_20260315' : des={'year0' : 2010, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   H2 cntrl2019 : reference
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep1p0_s01_hyway_20260403'  : des={'year0' : 2019, 'year1' : 2023, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_s01_hyway_20260403' : des={'year0' : 2019, 'year1' : 2038, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p7_s01_hyway_20260403'  : des={'year0' : 2019, 'year1' : 2023, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p65_s01_hyway_20260403' : des={'year0' : 2019, 'year1' : 2023, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   H2 cntr2019 : CH4 x 1.1
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4x1p1_s01_hyway_20260403'        : des={'year0' : 2019, 'year1' : 2038, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   H2 cntr2019 : H2 + 100Tg
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_h2plus100tg_s01_hyway_20260403'    : des={'year0' : 2019, 'year1' : 2038, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   H2 1850
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr1850_h2emi_h2dep0p75_s01_hyway_20260403'                : des={'year0' : 2019, 'year1' : 2038, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#   H2 cntr2019 : CH4 + H2 emissions
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4emi_s01_hyway_20260403'             : des={'year0' : 2019, 'year1' : 2058, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
    elif expid=='NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4emi_h2plus100tg_s01_hyway_20260403' : des={'year0' : 2019, 'year1' : 2058, 'model' : 'NorESM2', 'subdir' : lakedirns2345khyway, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat':'rawnoresm'}
#
# Oyvind : testing dry deposition velocity correction
    elif expid=='NF1850norbc_aer2014_f19_f19_20210530'    : des={'year0' : 1, 'year1' :  40, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NF1850norbc_aer2014_f19_f19_20210530_vd' : des={'year0' : 1, 'year1' :  40, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# Ada : 4xCO2, 2.8xCO2, 2xCO2, 1.4xCO2
    elif expid=='NCO2x1.4_f19_tn14_20210914'   : des={'year0' : 1, 'year1' : 590, 'model' : 'NorESM2', 'subdir' : basedirns2345k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NCO2x2_f19_tn14_20210819'     : des={'year0' : 1, 'year1' : 680, 'model' : 'NorESM2', 'subdir' : basedirns2345k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NCO2x2.8_f19_tn14_20210914'   : des={'year0' : 1, 'year1' : 585, 'model' : 'NorESM2', 'subdir' : basedirns2345k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NCO2x4_f19_tn14_20210819'     : des={'year0' : 1, 'year1' : 160, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NCO2x4frc2_f19_tn14_20210429' : des={'year0' : 1, 'year1' : 360, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}

# CMIP6 with CMIP5 emissions
#   piControl - 200 year
    elif expid=='N1850_cmip5_f19_tn14_20210526'           : des={'year0' : 1600, 'year1' : 1799, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   historical + rcp8.5 (2000-2014)
    elif expid=='NHIST_cmip5_f19_tn14_20210627'           : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_02_f19_tn14_20210627'        : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_03_f19_tn14_20210627'        : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   rcp6.0 (2000-2014)
    elif expid=='NHIST_cmip5_rcp60_f19_tn14_20210627'     : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k  , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_rcp60_02_f19_tn14_20210627'  : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir      , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_rcp60_03_f19_tn14_20210627'  : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir      , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   rcp4.5 (2000-2014)
    elif expid=='NHIST_cmip5_rcp45_f19_tn14_20210627'     : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k  , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_rcp45_02_f19_tn14_20210627'  : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir      , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_rcp45_03_f19_tn14_20210627'  : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir      , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   rcp2-6 (2000-2014)
    elif expid=='NHIST_cmip5_rcp26_f19_tn14_20210627'     : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k  , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_rcp26_02_f19_tn14_20210627'  : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir      , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NHIST_cmip5_rcp26_03_f19_tn14_20210627'  : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir      , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
   
    elif expid=='NF1850norbc_cmip5_f19_20210911'             : des={'year0' :    1, 'year1' :  200, 'model' : 'NorESM2', 'subdir' : scratchdir        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeronly_cmip5_f19_20210911'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeronly_cmip5_02_f19_20210911': des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorpibc_aeronly_cmip5_03_f19_20210911': des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : scratchdir        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# KINE simulations
#   with NorESM
    elif expid=='NFHISTnorbc_f19_20210611'              : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_BCANTEUR_f19_20210611'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_BCANTNAM_f19_20210611'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_BCANTASIA_f19_20210611'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_SO2ANTEUR_f19_20210611'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_SO2ANTNAM_f19_20210611'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_SO2ANTASIA_f19_20210611'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='NFHISTnorbc_BCSO2BBGLO_f19_20210611'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#   with CESM2.1.3
    elif expid=='FHIST_f19_f19_mg17_20211015'           : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : '',  'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='FHIST_SO2ANTEUR_f19_f19_mg17_20211015' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
    elif expid=='FHIST_SO2ANTNAM_f19_f19_mg17_20211015' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''}
#
# EMISSIONS mip
#   phase a
    elif expid=='NFHISTnorpddmsbcsdyn_base_f09_mg17_20210226'         : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_bc_no_season_f09_mg17_20210226' : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_high_so4_f09_mg17_20210226'     : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_no_so4_f09_mg17_20210226'       : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_so2_at_height_f09_mg17_20210226': des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_so2_no_season_f09_mg17_20210226': des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_standard_f09_mg17_20210226'     : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   phase b
    elif expid=='NFHISTnorpddmsbcsdyn_high_so4_so2_at_height_f09_mg17_20220824'     : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#    
    elif expid=='NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824'                    : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # using different SO2 anthro file
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_30red_f09_mg17_20220824'              : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_60red_f09_mg17_20220824'              : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_atlanticshift_f09_mg17_20220824'      : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_indianshift_f09_mg17_20220824'        : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_base_f09_mg17_20220824'               : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_ship_60red_f09_mg17_20220824'         : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_ship_atlanticshift_f09_mg17_20220824' : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_ship_indianshift_f09_mg17_20220824'   : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#   
# MMPPE-cloud 
    elif expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20220928'         : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_dmsx0.5_f09_mg17_20220928' : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_dmsx2_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_z0.80_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_z1.79_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_z2.00_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_lwp2.1_f09_mg17_20220928'  : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_lwp3.3_f09_mg17_20220928'  : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_enechk_f09_mg17_20220928'  : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_actd3_f09_mg17_20221005'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : oyvindsns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_actx3_f09_mg17_20221005'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : oyvindsns2345kmmppecloud    , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#
# IMBALANCE CICERO
#   reference 1995-2014
    elif expid=='NFHISTnorpddmsbc_01_f19_mg17_20230110'              : des={'year0' : 1995, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_02_f19_mg17_20230110'              : des={'year0' : 1995, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_03_f19_mg17_20230110'              : des={'year0' : 1995, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_04_f19_mg17_20230110'              : des={'year0' : 1995, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_05_f19_mg17_20230110'              : des={'year0' : 1995, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_06_f19_mg17_20230110'              : des={'year0' : 1995, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#   aer2000 perturbations 2000-2014    
    elif expid=='NFHISTnorpddmsbc_aer2000_01_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_aer2000_02_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_aer2000_03_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_aer2000_04_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_aer2000_05_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_aer2000_06_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#   anthro2000 perturbations 2000-2014    
    elif expid=='NFHISTnorpddmsbc_anthro2000_01_f19_mg17_20230110'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_anthro2000_02_f19_mg17_20230110'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_anthro2000_03_f19_mg17_20230110'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_anthro2000_04_f19_mg17_20230110'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_anthro2000_05_f19_mg17_20230110'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_anthro2000_06_f19_mg17_20230110'   : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#   all2000 perturbations 2000-2014    
    elif expid=='NFHISTnorpddmsbc_all2000_01_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_all2000_02_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_all2000_03_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_all2000_04_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_all2000_05_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFHISTnorpddmsbc_all2000_06_f19_mg17_20230110'      : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#   ssp245 2015-2019 extension    
    elif expid=='NFSSP245norpddmsbc_01_f19_mg17_20230110'            : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_02_f19_mg17_20230110'            : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_03_f19_mg17_20230110'            : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_04_f19_mg17_20230110'            : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_05_f19_mg17_20230110'            : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_06_f19_mg17_20230110'            : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_aer2000_01_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_aer2000_02_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_aer2000_03_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_aer2000_04_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_aer2000_05_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_aer2000_06_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_anthro2000_01_f19_mg17_20230110' : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_anthro2000_02_f19_mg17_20230110' : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_anthro2000_03_f19_mg17_20230110' : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns2345kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_anthro2000_04_f19_mg17_20230110' : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_anthro2000_05_f19_mg17_20230110' : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_anthro2000_06_f19_mg17_20230110' : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_all2000_01_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_all2000_02_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_all2000_03_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_all2000_04_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_all2000_05_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
    elif expid=='NFSSP245norpddmsbc_all2000_06_f19_mg17_20230110'    : des={'year0' : 2015, 'year1' : 2019, 'model' : 'NorESM2', 'subdir' : basedirns9560kimbalancemip, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # (id.)
#
# OPOM for EMEP (David)
    elif expid=='NFHISTnorpddmsbcsdyn_standard_opom_f09_mg17_20210226' : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : scratchdir, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# TOAR (Fiona and Bill)
    elif expid=='NF1850norbc_tropstratchem_f19_20230515_test01'     : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_toar_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_toar_20230605_sim05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   new simulations (corrected heterogenous freezing and koagsub)
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''} 
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   prescribing the ozone climatologies
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01'     : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01'     : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }


#   perturbation simulation with CHBR3 boundary condition (for KeyCLIM)
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_chbr3x0.0_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_chbr3x2.0_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# METHANEMIP
#   member 1
    elif expid=='NHIST_tropstratchem_01_f19_tn14_r1990_s01_20241118' : des={'year0' : 1990, 'year1' : 1999, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_tropstratchem_01_f19_tn14_r2000_s01_20241118' : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245_tropstratchem_01_f19_tn14_s01_20241118'     : des={'year0' : 2015, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245TECH_tropstratchem_01_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245AMBI_tropstratchem_01_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   member 2
    elif expid=='NHIST_tropstratchem_02_f19_tn14_r1990_s01_20241118' : des={'year0' : 1990, 'year1' : 1999, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_tropstratchem_02_f19_tn14_r2000_s01_20241118' : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245_tropstratchem_02_f19_tn14_s01_20241118'     : des={'year0' : 2015, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245TECH_tropstratchem_02_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245AMBI_tropstratchem_02_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   member 3
    elif expid=='NHIST_tropstratchem_03_f19_tn14_r1990_s01_20241118' : des={'year0' : 1990, 'year1' : 1999, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_tropstratchem_03_f19_tn14_r2000_s01_20241118' : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245_tropstratchem_03_f19_tn14_s01_20241118'     : des={'year0' : 2015, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245TECH_tropstratchem_03_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245AMBI_tropstratchem_03_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   member 4
    elif expid=='NHIST_tropstratchem_04_f19_tn14_r2000_s01_20241118' : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245_tropstratchem_04_f19_tn14_s01_20241118'     : des={'year0' : 2015, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245TECH_tropstratchem_04_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245AMBI_tropstratchem_04_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   member 5
    elif expid=='NHIST_tropstratchem_05_f19_tn14_r2000_s01_20241118' : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245_tropstratchem_05_f19_tn14_s01_20241118'     : des={'year0' : 2015, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245TECH_tropstratchem_05_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245AMBI_tropstratchem_05_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   member 6
    elif expid=='NHIST_tropstratchem_06_f19_tn14_r2000_s01_20241118' : des={'year0' : 2000, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245_tropstratchem_06_f19_tn14_s01_20241118'     : des={'year0' : 2015, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245TECH_tropstratchem_06_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP245AMBI_tropstratchem_06_f19_tn14_s01_20241118' : des={'year0' : 2020, 'year1' : 2050, 'model' : 'NorESM2', 'subdir' : lakedirns2345kmethanemip,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# NAVIGATE
#   historical : 1950-2000
    elif expid=='NHIST_f19_tn14_20250311_test04'     : des={'year0' : 1950, 'year1' : 1999, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='NHIST_f19_tn14_20250311_test05'     : des={'year0' : 1950, 'year1' : 1999, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   pre-industrial
    elif expid=='N1850_f19_tn14_20250311_test01'        : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test02'        : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test03'        : des={'year0' : 1600, 'year1' : 1609, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test04'        : des={'year0' : 1600, 'year1' : 1609, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test05'        : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test06'        : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test05_15n60n' : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test05_20km'   : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test05_26km'   : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850_f19_tn14_20250311_test05_60s15s' : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   pre-industrial : fixed-SST to estimate ERF
    elif expid=='NF1850norbc_f19_20250311_test01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='NF1850norbc_f19_20250311_test05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='NF1850norbc_f19_20250311_test06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   impose-like - co2 emission driven : 0Tg/yr, 2Tg/yr [from 1890], 2Tg/yr [from 1910]
    elif expid=='N1850frc2esm_B3_r1890_0tg_f19_tn14_20250613' : des={'year0' : 1890, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3_r1890_2tg_f19_tn14_20250613' : des={'year0' : 1890, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3_r1910_2tg_f19_tn14_20250613' : des={'year0' : 1910, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   impos-line - varying S emissions to bring B3C1a to B4
#   wrong : cycleyear=1850 for SAI (always used the very small 1950 forcing)
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250716' : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250716' : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns2345knavigate,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   a) 1.0 (Tg[S]/yr)/(W/m2) - 30S-30N 
#   evolving : SAI + B3 scenario (member 1) : 1.0 (Tg[S]/yr)/(W/m2) 
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250721' : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   evolving :  SAI + B4 (member 1) : 1.0 (Tg[S]/yr)/(W/m2)
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250730' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   b) 1.5 (Tg[S]/yr)/(W/m2) - 30S-30N
#   evolving : SAI + B3 scenario (member 1+2+3) : 1.5 (Tg[S]/yr)/(W/m2)
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721'        : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721len100'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : 'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721', 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721'     : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721'     : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   evolving : SAI + B4 scenario (member 1+2+3) : 1.5 (Tg[S]/yr)/(W/m2)
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730'        : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730'     : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730'     : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   c) XX [strong] (Tg[S]/yr)/(W/m2) -- 15N-60N
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20250921' : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251005' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   d) XX [weak] (Tg[S]/yr)/(W/m2) -- 15N-60N (Jerry)
#   member 1    
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01a' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   member 2
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02a' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   member 3
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03a' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   e) XX [weak] (Tg[S]/yr)/(W/m2) -- 60S-15S (Jerry)
#   member 1
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens01'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens01a' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   member 2
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens02a' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
#   member 3
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens03'  : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }
    elif expid=='N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens03a' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : lakedirns1002k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' }

#   impose simulations of Jörg
#   B3 : B2000
    elif expid=='N1850frc2esm_ZECMIP_B3_f19_tn14_20200316'    : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # micom
    elif expid=='N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224' : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # blom
    elif expid=='N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224' : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # blom
#   B4 : B1500
    elif expid=='N1850frc2esm_ZECMIP_B4_f19_tn14_20200316'    : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # micom
    elif expid=='N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224' : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # blom
    elif expid=='N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224' : des={'year0' : 1850, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # blom
#   B3C1a
    elif expid=='N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316'      : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # micom
    elif expid=='N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # blom
    elif expid=='N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224' : des={'year0' : 1950, 'year1' : 2249, 'model' : 'NorESM2', 'subdir' : basedirns10054kimpose,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm' } # blom
#
# ESM2025 - WP1
#   aerosol-only
    elif expid=='NF1850norbc_f19_20240312_test01'          : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_aer2014_f19_20240312_test01'  : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_so22014_f19_20240312_test01'  : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   full-chemistry
    elif expid == 'NF1850norbc_tropstratchem_f19_20240312_test01'              : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid == 'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01'      : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid == 'NF1850norbc_tropstratchem_so22014_f19_20240312_test01'      : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
    elif expid == 'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   oxidants from full-chemistry
    elif expid == 'NF1850norbc_tropstratoxid_f19_20240312_test01'         : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid == 'NF1850norbc_tropstratoxid_so22014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid == 'NF1850norbc_tropstratoxid_aer2014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   oxidants from full-chemistry + mono-terpene emissions as in full-chemistry
    elif expid == 'NF1850norbc_tropstratoxidterp_f19_20240312_test01'         : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid == 'NF1850norbc_tropstratoxidterp_so22014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid == 'NF1850norbc_tropstratoxidterp_aer2014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025ozone, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# ESM2025 - WP1 - Øyvind
#   activation schemes
    elif expid=='nf1850norbc_aer2014.f19.f19_base2.0.9_20241025'   : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}        
    elif expid=='nf1850norbc_aer2014.f19.f19_BNForces_20241025'    : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}        
#   convective scavenging
    elif expid=='nf1850norbc_aer2014.f19.f19_convscavYu_20241104'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850norbc_aer2014.f19.f19_convact1_20241104'    : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850norbc_aer2014.f19.f19_noctran_20241104'     : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850norbc_aer2014.f19.f19_fraciscldc_20241105'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850norbc_aer2014.f19.f19_fracis2step_20241105' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850norbc_aer2014.f19.f19_updraftscav_20241106' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : lakedirns2345kesm2025oyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

# KEYCLIM - WP6
    elif expid=='NHISTpiaeroxid_f09_tn14_keyClim20201217'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP370piaeroxid_f09_tn14_keyClim20210210' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP585piaeroxid_f09_tn14_keyClim_20230705': des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_historical_Eddy_KeyCLim'         : des={'year0' : 1850, 'year1' : 1899, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2_histeddy2_KeyCLim'               : des={'year0' : 1900, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NSSP585frc2_Eddy_KeyCLIM'                  : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHISTfrc2G_f09_tn14_gl4_SMB1_celo'         : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252kheiko, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}                
    elif expid=='NSSP585frc2G_f09_tn14_gl4_SMB1_celo'       : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252kheiko, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}          
    elif expid=='NHISTfrc2_f09_tn14_cloudxpice_220629'      : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}         
    elif expid=='NSSP585frc2_f09_tn14_cloudxpice_220819'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : lakedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}       
    elif expid=='NHIST_hist_snow_KeyClim'                   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}                          
    elif expid=='NSSP585_snow_KeyClim'                      : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   combinations (historical + SSP)
    elif expid=='histssp585'           : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp370-piAerOxid' : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp585-piAerOxid' : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp585-eddy'      : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp585-iceSheet3' : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp585-cloud2'    : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp585-ozone'     : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='histssp585-snow'      : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# KEYCLIM - ERF
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug01'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug01diagc' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''} # correction only in diagnostics
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug02'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug02diagc' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug03'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug04'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug05'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug06'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug01'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug01diagc' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug02'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug02diagc' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug03'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug04'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug05'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug06'      : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# FORCeS - Øyvind
    elif expid=='N1850_f19_tn14_Forces_230512' : des={'year0' : 1601, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns2345koyvind,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NHIST_f19_tn14_Forces_230515' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345koyvind,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# INGVILD - NENES
    elif expid=='NFHISTnorpddmsbc_f19_f19_mg17_20231106142112' : des={'year0' : 1985, 'year1' : 2008, 'model' : 'NorESM2', 'subdir' : basedirns9560kingvild,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NFHISTnorpddmsbc_f19_f19_mg17_20231106140956' : des={'year0' : 1985, 'year1' : 2008, 'model' : 'NorESM2', 'subdir' : basedirns9560kingvild,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
# JERRY - CO2 emission driven
#   elif expid=='N1850_f19_tn14_20190730esm'                     : des={'year0' : 1751, 'year1' : 2200, 'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20190730esm'                     : des={'year0' : 1751, 'year1' : 2150, 'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NHIST_f19_tn14_20191104esm'                     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027' : des={'year0' : 1851, 'year1' : 4101, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
# JORG - CO2 emission driven 
#   534
    elif expid=='NSSP534frc2esm_f19_tn14_20230106'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NSSP534frc2esmext_f19_tn14_20230510' : des={'year0' : 2101, 'year1' : 2299, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NSSP534frc2esm_f19_tn14_20230106ext' : des={'year0' : 2015, 'year1' : 2299, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   585
    elif expid=='NSSP585_f19_tn14_20191223esm'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   
# NorESM2.1 tests by dirk
#   N1850 (fully-coupled)
    elif expid=='N1850_f19_tn14_20231204_test02'              : des={'year0' : 1600, 'year1' : 1749, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test03'              : des={'year0' : 1600, 'year1' : 1749, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test04'              : des={'year0' : 1600, 'year1' : 1749, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test05'              : des={'year0' : 1600, 'year1' : 1749, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test06'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test07'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test08'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test09'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test10'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test11'              : des={'year0' : 1600, 'year1' : 1749, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test12'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test13'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test14'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test15'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test16'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20231204_test17'              : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   NF1850norbc
    elif expid=='NF1850norbc_f19_f19_20231204_test01'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test02'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test03'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test04'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test05'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test06'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test07'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test08'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test09'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test10'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test11'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test12'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test13'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test14'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test15'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test16'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test17'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test18'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test19'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   2014 aerosol emissions (aerosol ERF)
    elif expid=='NF1850norbc_aer2014_f19_f19_20231204_test01' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_aer2014_f19_f19_20231204_test02' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_aer2014_f19_f19_20231204_test17' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_aer2014_f19_f19_20231204_test18' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   +4k NF1850norbc (climate sensitivity)
    elif expid=='NF1850norbc_p4k_f19_f19_20231204_test02' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knoresm21performance,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_p4k_f19_f19_20231204_test04' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knoresm21performance,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_p4k_f19_f19_20231204_test17' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knoresm21performance,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF1850norbc_p4k_f19_f19_20231204_test18' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns2345knoresm21performance,      'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}

#
# NorESM2.2 tests by Oyvind / Dirk
#   Oyvind 
    elif expid=='NF1850norbc_f19_f19_20210530'              : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2               (Oyvind)
    elif expid=='NF1850norbc_f19_f19_20210923'              : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2.2 with flux=0 (Oyvind)
    elif expid=='NF1850norbc_f19_f19_20211013'              : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2.2 with flux=1 (Oyvind)
    elif expid=='NF1850norbc_f19_20211113_test17'           : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2.2 with flux=1 and clubb 2.1.3 (Dirk)
    elif expid=='NF1850norbc_f19_20211113_test20'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2.2 with flux=1 and club_gammab=0.268
    elif expid=='F2000climo_f09_ver2.1.3_20211005'          : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # cesm 2.1.3             (Oyvind)
    elif expid=='F2000climo_f09_ver2.2_20211005'            : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # cesm 2                 (Oyvind)
    elif expid=='F2000climo_f09_20211109_cesm2.2_test04'    : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # cesm 2 with clubb 2.1.3 (Dirk)
#   Dirk
    elif expid=='NF1850norbc_f19_20211101_noresm2_test01'   : des={'year0' : 1,    'year1' : 20,   'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2          gamma=0.308 (Dirk)
    elif expid=='NF1850norbc_f19_20211101_noresm2.2_test01' : des={'year0' : 1,    'year1' : 20,   'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm 2.2 flux=1 gamma=0.308 (Dirk)
#   Coupled simulations
    elif expid=='N1850_f19_tn14_20211104_test13'            : des={'year0' : 1600, 'year1' : 1669, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm2.2 fully coupled
    elif expid=='N1850_f19_tn14_20211104_test18'            : des={'year0' : 1600, 'year1' : 1679, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm2.2 fully coupled and clubb 2.1.3
    elif expid=='N1850_f19_tn14_20211104_test19'            : des={'year0' : 1600, 'year1' : 1609, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm2.2 fully coupled and clubb_gammab=0.268
    elif expid=='N1850_f19_tn14_20211104_test21'            : des={'year0' : 1600, 'year1' : 1659, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'project' : ''} # noresm2.2 fully coupled and clubb_gammab=0.268
#
# NorESM2.3 tests by Dirk
    elif expid=='N1850_tropstratchem_f19_tn14_20240319_test08' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir'    : lakedirns2345knoresm23test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='N1850_tropstratchem_f19_tn14_20240319_test10' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir'    : lakedirns2345knoresm23test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#   tuning
#   N1850
    elif expid=='N1850_f19_tn14_20241127_test01'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test02'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test03'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test04'                    : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test05'                    : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test06'                    : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test07'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test08'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test11'                    : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test12'                    : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test13'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test14'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test15'                    : des={'year0' : 1600, 'year1' : 1699, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test16'                    : des={'year0' : 1600, 'year1' : 1919, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test17'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='N1850_f19_tn14_20241127_test18'                    : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   fSST   
    elif expid=='NF1850norbc_f19_f19_20241127_test01'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test05'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test06'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test09'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test10'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test13'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test14'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test15'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test16'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='NF1850norbc_f19_f19_20241127_test17'               : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
#   fSST aer2014
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test01'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test05'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test06'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test09'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test10'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test13'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test14'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test15'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test16'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_aer2014_f19_f19_20241127_test17'       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   nudged    
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test01'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test05'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test09'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test10'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test14'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test15'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test16'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20241127_test17'          : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   nudged aer2014   
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test01'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test05'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test09'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test10'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test14'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test15'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test16'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_aer2014_f19_f19_20241127_test17'  : des={'year0' : 1970, 'year1' : 1974, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   cmip7-volcaod-noresm2.3
    elif expid=='NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip6'        : des={'year0' : 1970, 'year1' : 1979, 'model' : 'NorESM2', 'subdir'    : lakedirns2345cmip7volcaodnoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7'        : des={'year0' : 1970, 'year1' : 1979, 'model' : 'NorESM2', 'subdir'    : lakedirns2345cmip7volcaodnoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7wghtavg' : des={'year0' : 1970, 'year1' : 1979, 'model' : 'NorESM2', 'subdir'    : lakedirns2345cmip7volcaodnoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone'         : des={'year0' : 1970, 'year1' : 1979, 'model' : 'NorESM2', 'subdir'    : lakedirns2345cmip7volcaodnoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   cmip7 forcing generation
#   1850
    elif expid=='NF1850norbc_tropstratchem_f19_f19_t00_20260829'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_tropstratchem_f19_f19_t01_20260829'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_tropstratchem_f19_f19_t02_20260829'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # finally used
#   historical
    elif expid=='NF1850norbc_1860climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1870climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1880climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1890climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1900climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1910climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1920climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1930climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1940climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1950climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1960climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1970climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1980climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_1990climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2000climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2010climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2020climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2023climo_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   scen-h
    elif expid=='NF1850norbc_2022scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2025scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2030scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2040scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2050scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2060scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2070scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2080scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2090scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2100scen-h_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   scen-vl
    elif expid=='NF1850norbc_2022scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2025scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2030scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2040scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2050scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2060scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2070scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2080scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2090scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_2100scen-vl_tropstratchem_f19_f19_t02_20260829' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir'    : lakedirns11118knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   full chemistry
    elif expid=='N1850_tropstratchem_f19_tn14_20241127_test01'          : des={'year0' : 1600, 'year1' : 1639, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_tropstratchem_f19_f19_20241127_test01'     : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_tropstratchem_f19_f19_20241127_test01_bis' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='NF1850norbc_tropstratchem_f19_f19_20241127_test16_bis' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir'    : lakedirns9560knoresm23, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#  
#   Eli Holm Hogemo
    elif expid=='NHIST_tropstratchem_f09_tn14_20250917_1975_2014'   : des={'year0' : 1975, 'year1' : 2009, 'model' : 'NorESM2', 'subdir'    : basedirns1004kelihho, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; cdir='NHIST_tropochem_250916'
#
# NorESM2.5 Mariana
#   fall 2023
    elif expid=='NF2000oslo.f19_f19_mtn14.2'                : des={'year0' :    1, 'year1' :    5, 'model' : 'NorESM2', 'subdir' : basedirns9560krefactor, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF2000oslo.f19_f19_mtn14.3'                : des={'year0' :    1, 'year1' :    5, 'model' : 'NorESM2', 'subdir' : basedirns9560krefactor, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
    elif expid=='NF2000oslo.f19_f19_mtn14.3.bug'            : des={'year0' :    1, 'year1' :    5, 'model' : 'NorESM2', 'subdir' : basedirns9560krefactor, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : ''}
#
#   summer 2024
    elif expid=="n1850.ne30_tn14.isopycnic.20240801"        : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid.20240801"           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid_coare.20240801"     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=="n1850.ne30_tn14.hybrid.20240808"           : des={'year0' :    1, 'year1' :   55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid.20240821"           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid.20240822"           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
    elif expid=="n1850.ne30_tn14.hybrid_fatessp.202401007"  : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid_fatessp.20241111"   : des={'year0' :    1, 'year1' :   28, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid_fatessp.20241204"   : des={'year0' :    1, 'year1' :   70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid_fatessp.20241219"   : des={'year0' :    1, 'year1' :  133, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid_wavparam_fatessp.20241226" : des={'year0' :    1, 'year1' :   49, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf2000_ne30pg3_ne30pg3_mtn14_20250120"          : des={'year0' :    1, 'year1' :  28, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf2000_ne30pg3_ne30pg3_mtn14.fatessp_20250120"  : des={'year0' :    1, 'year1' :  28, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf2000_ne30pg3_ne30pg3_mtn14.fatessp.dcs600_20250124"         : des={'year0' :    1, 'year1' :  14, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf2000_ne30pg3_ne30pg3_mtn14.fatessp.coare_20250124"          : des={'year0' :    1, 'year1' : 14, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf2000_ne30pg3_ne30pg3_mtn14.fatessp.clubbc8cesm121_20250124" : des={'year0' :    1, 'year1' :  14, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

    elif expid=="n1850.ne30_tn14.hybrid_fatessp.2_5a09a.20250219" : des={'year0' :    1, 'year1' :  21, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   Lana DMS
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250219"          : des={'year0' :    1, 'year1' :  35, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250219"  : des={'year0' :    1, 'year1' :  35, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   NorESM2 derived DMS
#   pi
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317"          : des={'year0' :    1, 'year1' :  21, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   aer2014
    elif expid=="nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317"  : des={'year0' :    1, 'year1' :  35, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   bc 
    elif expid=="nf1850_aer2014bc_ne30pg3_ne30pg3_mtn14.fatessp_20250320"  : des={'year0' :    1, 'year1' :  14, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   oc
    elif expid=="nf1850_aer2014OM_ne30pg3_ne30pg3_mtn14.fatessp_20250320"  : des={'year0' :    1, 'year1' :  14, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   so2/so4
    elif expid=="nf1850_aer2014S_ne30pg3_ne30pg3_mtn14.fatessp_20250320"  : des={'year0' :    1, 'year1' :  14, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

    elif expid=="n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408"        : des={'year0' :    1, 'year1' : 52, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.hybrid_fates-nocomp_spinup.3.0a02.20250415" : des={'year0' :    1, 'year1' :  8, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850esm.ne30_tn14.hybrid.3.0a01.20250410"                  : des={'year0' :    1, 'year1' : 16, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   cesm3
    elif expid=="n1850mam4.ne30_tn14.hybrid.clmbgc.20240826"         : des={'year0' :    1, 'year1' :    2, 'model' : 'CESM2.5', 'subdir' : lakedirns2345knoresm25test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152"      : des={'year0' :    1, 'year1' :   20, 'model' : 'CESM2.5', 'subdir' : lakedirns2345knoresm25test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="b.e30_beta06.B1850C_LTso.ne30_t232_wgx3.192"        : des={'year0' :    1, 'year1' :   19, 'model' : 'CESM2.5', 'subdir' : basedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316"      : des={'year0' :    1, 'year1' :   99, 'model' : 'CESM2.5', 'subdir' : basedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#
#   Oyvinds ERF simuliatons
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_dev_20250513"         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_aer2014_dev_20250513" : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_mam4_20250522"                              : des={'year0' :    1, 'year1' :   10, 'model' : 'CESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_mam4_aer2010_20250522"                      : des={'year0' :    1, 'year1' :   10, 'model' : 'CESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   tomas
    elif expid=="n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513" : des={'year0' :    1, 'year1' :  100, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_alpha03d.20250528"                      : des={'year0' :    1, 'year1' :   16, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
#   dirk ghg
    elif expid=="n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2" : des={'year0' :    1, 'year1' :   13, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}


#   ppe ada spinup
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_alpha03c.noresm3_0_002_cam6_4_085.19_to_35yr_2deg_ppe_spinup.20250524" : des={'year0' :    19, 'year1' :   34, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   oyvind BC_AX bug correction
    elif expid=="n1850_ne30pg3_tn14_alpha3d.BCAXtest_20250612"      : des={'year0' :    1, 'year1' :   12, 'model' : 'NorESM2.5', 'subdir' : lakedirns2345knoresm25test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   oyvinds ERF simulation : givin very low CLOUD ICE
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_beta3proto.20250616"         : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_aer2014.20250616" : des={'year0' :    1, 'year1' :   5, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_mam4.20250616"               : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_mam4_aer2010.20250616"       : des={'year0' :    1, 'year1' :  10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   oyvinds new ERF simulations : corrected global or local delimiter
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_homait.20250620"         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_homait_aer2014.20250620" : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_locallim.20250623"         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_locallim.20250623_aer2014" : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   oyvinds +4k simulations :
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_locallim_20250625"        : des={'year0' :    1, 'year1' :   11, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_locallim_sstp4K_20250625" : des={'year0' :    1, 'year1' :   11, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_globlim_20250625"         : des={'year0' :    1, 'year1' :   11, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=="nf1850_ne30pg3_ne30pg3_mtn14_globlim_sstp4K_20250625"  : des={'year0' :    1, 'year1' :   11, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560koyvind, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   beta01
#   beta01 : tomas
    elif expid=="n1850.ne30_tn14.nor3_rc-b01.20250628"                  : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_alpha07.20250628"            : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01.20250629"             : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh.20250630" : des={'year0' :    1, 'year1' :  50, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   beta01 : ada
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_alpha07.20250701"         : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_beta01.20250701"          : des={'year0' :    1, 'year1' :  45, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_beta01.20250704"          : des={'year0' :   46, 'year1' : 120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_beta01_hybrid.20250704"          : des={'year0' :   46, 'year1' : 55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # hybrid - gave identical results to Ada's simulation
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_beta01_branch.20250704"          : des={'year0' :   46, 'year1' : 55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # branch
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_beta01_hybrid_noinitcond.20250704"          : des={'year0' :   46, 'year1' : 55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # hybrdi - no IC (initial conditions for clm, cice and blom)
    elif expid=="n1850.ne16pg3_tn14.noresm3_0_beta01_branch_nosip.20250704"      : des={'year0' :   46, 'year1' : 55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # branch
#   beta01 : alok
    elif expid=="n1850.ne30_tn14.cice.beta01_set1" : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.cice.beta01_set2" : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.cice.beta01_set3" : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.cice.beta01_set4" : des={'year0' :    1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   beta01 : dirk sensitivities
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_0p5dust.20250703" : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_700dcs_3p5clubbc8.20250703" : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_800dcs.20250703" : des={'year0' :    1, 'year1' : 15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_4p0clubbc8.20250703" : des={'year0' :    1, 'year1' : 15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_0p5dms.20250703" : des={'year0' :    1, 'year1' : 15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_0p5seasalt.20250703" : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=="n1850.ne30_tn14.noresm3_0_beta01-FATES-noluh_0p33clubbgamma.20250703" : des={'year0' :    1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
# NORESM3.0 BETA01 LIGHT TUNING
#   n1850 1x1
    elif expid=='n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708' : des={'year0' :   1, 'year1' :  50, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='n1850.ne30_tn14.nor3_b01-cplhist-noLU.20250716'                           : des={'year0' :  51, 'year1' : 100, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # cplhst output
    elif expid=='n1850.ne30_tn14.nor3_b01-noLU_yr101.20250729'                             : des={'year0' : 101, 'year1' : 120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   n1850 2x2
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta01.20250708'                            : des={'year0' :   1, 'year1' :  40, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708' : des={'year0' :   1, 'year1' : 100, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} 
    elif expid=='n1850.ne16pg3_tn14.nor3_b01-cplhist.20250716'                            : des={'year0' : 101, 'year1' : 200, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # cplhst output
    elif expid=='n1850.ne16pg3_tn14.nor3_b01.20250731'                                    : des={'year0' : 201, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   nco2x4
    elif expid=='nco2x4.ne30pg3_tn14.noresm3_0_beta01_650dcs_4p0clubbc8_0p5dust.20250715'  : des={'year0' :   51, 'year1' : 150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nco2x4.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250710' : des={'year0' :   51, 'year1' : 200, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   nhist
    elif expid=='nhist.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250716' : des={'year0' : 1850, 'year1' : 1929, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716'  : des={'year0' : 1850, 'year1' : 2013, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   n1850ghg
    elif expid=='n1850ghg.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716' : des={'year0' :    1, 'year1' : 100, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
# NORESM3.0 BETA01 LIGHT TUNING + sensitivity simulations
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_zmconv_capelmt.20250815'                      : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_zmconv_tiedke_add.20250815'                   : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_coare.20250815'                               : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_dust_emis_fraction.20250815'                  : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_dcs.20250815'                                 : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_coare_dcs.20250815'                           : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_dcs800.20250815'                              : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_coare_dcs800.20250815'                        : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.nor3_b01_clubbc8.20250815'                             : des={'year0' : 271, 'year1' : 300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
# NORESM3.0 BETA02
    elif expid=='n1850.ne16_tn14.noresm3_0_beta02-run1_yr001.20250825'                     : des={'year0' :   1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16_tn14.noresm3_0_beta02-run2_yr001.20250829'                     : des={'year0' :   1, 'year1' :  50, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
# NorESM3.0 BETA03
    elif expid=='n1850esm.ne16_tn14.nor3_b03_20250926'                                     : des={'year0' :   1, 'year1' :  10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

    elif expid=='n1850.ne16_tn14.nor3_b03-rc3.20250925'                     : des={'year0' :   1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
    elif expid=='n1850.ne16_tn14.nor3_b03-rc3_yr0031.20250928'              : des={'year0' :  31, 'year1' :  70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
    elif expid=='n1850.ne16_tn14.nor3_b03-rc3_rafsipoff.20250928'           : des={'year0' :   1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
#
# NorESM3.0 BETA3a
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03_rafsipmasstonum.20250930'           : des={'year0' :   1, 'year1' :  90, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03a-run1_yr061.20251009'               : des={'year0' :  61, 'year1' :  85, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta03a.2025-10-10' : des={'year0' :  61, 'year1' : 120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   sensitivity Ada
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03.clubbdiffoff.20251007'           : des={'year0' :  61, 'year1' :  95, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03a.tayloralbedo.20251007'          : des={'year0' :  61, 'year1' :  95, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03a.tayloralbedo.20251010'          : des={'year0' :  61, 'year1' :  95, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   sensitivyt Mats
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03a.brnfac0p25.20251017'      : des={'year0' :  61, 'year1' :  90, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03a.no_iwd.20251017'          : des={'year0' :  61, 'year1' :  90, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16_tn14.noresm3_0_beta03b.egc3p0.20251017'          : des={'year0' :  61, 'year1' :  90, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   tuned continuation
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03a.landAndCAMupdate.2025-10-16' : des={'year0' : 121, 'year1' : 240, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.2025-10-24'  : des={'year0' : 231, 'year1' : 290, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.2025-10-29'          : des={'year0' : 291, 'year1' : 410, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST_C8_4p8.2025-11-01'   : des={'year0' : 321, 'year1' : 360, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   1x1
    elif expid=='n1850.ne30_tn14.noresm3_0_beta03a-run1_yr001.20251016'            : des={'year0' :   1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30_tn14.noresm3_0_beta03b-run1_yr001.20251021'            : des={'year0' :   1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023'            : des={'year0' :   1, 'year1' :  75, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   sensitivity jerry (reduced DMS emissions)
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.DMSbac.2025-10-30' : des={'year0' : 271, 'year1' : 310, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   sensitivity dirk (reduce natural emissions in 1x1)
    elif expid=='n1850.ne30_tn14.noresm3_0_beta03b-run2_yr031_eminatred.20251031'  : des={'year0' : 31, 'year1' :  55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   emission-driven ada
    elif expid=='n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251105' : des={'year0' : 2015, 'year1' : 2057, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251112' : des={'year0' : 2015, 'year1' : 2021, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   emission-driven jerry
    elif expid=='n1850esm.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.2025-10-30' : des={'year0' : 271, 'year1' : 330, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   NorESM3.0 BETA04
    elif expid=='n1850.ne30_tn14.noresm3_0_beta04-run1_yr001.20251103' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   NorESM3.0 BETA05
    elif expid=='n1850.ne30_tn14.nor3_b05-rc1-run1_yr001.20251110' : des={'year0' : 1, 'year1' : 15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   NorESM3.0 BETA06
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.20251114'                  : des={'year0' : 391, 'year1' : 425, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30_tn14.noresm3_0_beta06-run1_yr001.20251114'          : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850.ne16pg3_ne16pg3_tn14.noresm3_0_beta06.20251117'         : des={'year0' : 1, 'year1' : 9, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nf1850.ne16pg3_ne16pg3_tn14.aer2014.noresm3_0_beta06.20251117' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   test why BETA06 is drifting
#   sensitivity ada    
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.dmaxbo4.20251120' : des={'year0' : 371, 'year1' : 400, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   sensitivity Kjetil (group 1)
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.MedlSpit.2025-11-23'       : des={'year0' : 391, 'year1' : 410, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.b06_settingsV3.2025-11-23' : des={'year0' : 391, 'year1' : 410, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   sensitivty Kjetil (group 2)
    elif expid=='n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.revertall.2025-11-25' : des={'year0' : 391, 'year1' : 400, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.Best.2025-11-25'      : des={'year0' : 391, 'year1' : 400, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.oldDmax.2025-11-25'   : des={'year0' : 391, 'year1' : 400, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   kjetil
    elif expid=='n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.Best_c8_4p8.2025-11-26' : des={'year0' : 391, 'year1' : 468, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #276
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.Best_c8_4p7.2025-12-01'                     : des={'year0' : 471, 'year1' : 510, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #277
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.PPEbasedTuning.2025-12-04'                  : des={'year0' : 391, 'year1' : 445, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #280
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.PPEbasedV2.2025-12-08'                      : des={'year0' : 471, 'year1' : 490, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #286
#   ada
    elif expid=='n1850.ne16pg3_tn14.nor3_b06_floedim.20251205'                   : des={'year0' : 391, 'year1' : 455, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #284
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.BDMC21.8.20251209'          : des={'year0' : 471, 'year1' : 505, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #290
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.EGC2.5_EGIDFQ1.25.20251209' : des={'year0' : 471, 'year1' : 505, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #291
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.CombinedTuning.20251209'    : des={'year0' : 471, 'year1' : 490, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #292
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06.PPEbasedV3.2025-12-11'      : des={'year0' : 491, 'year1' : 505, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #292

#   NorESM3.0 BETA06/07/08 1x1
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta06-ref_yr001.20251209' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #287
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta07-ref_yr001.20251209' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #288
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta08-ref_yr001.20251209' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #289

#   NorESM3.0 BETA09 2x2
#   kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.2025-12-19'             : des={'year0' :   1, 'year1' :  60, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #297
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.OcnICppev3.2025-12-19'  : des={'year0' :   1, 'year1' :  30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.startupOCN2025-12-18'   : des={'year0' :   1, 'year1' :  15, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.LandSpinup.2025-12-24'  : des={'year0' :  51, 'year1' : 135, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #308
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run3.2025-12-30'        : des={'year0' : 136, 'year1' : 220, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #311
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run4.2026-01-06'        : des={'year0' : 221, 'year1' : 250, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #314
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08'        : des={'year0' : 251, 'year1' : 405, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #316
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118'            : des={'year0' :1850, 'year1' :2013, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='Reference' #313

    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2'                   : des={'year0' :1995, 'year1' :2013, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.convincld'         : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+convincl'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.convstratbelowcld' : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+convstratbelowcld' #    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.dust'              : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+dust'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.seasalt'           : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+salt'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.all'               : des={'year0' :2000, 'year1' :2013, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+all'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.seasaltdist'       : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+salt2'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.all2'              : des={'year0' :2000, 'year1' :2013, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+all'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.h2o2'                    : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='H2O2'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.h2o2.all2'               : des={'year0' :2000, 'year1' :2004, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='H2O2+all2'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.all3'                    : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='all3'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.all3chem'                : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='OH+H2O2+all3'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dfso2.all3'              : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='dfSO2+all3'#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dfso2.all3chem'          : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dfso2b.all3chem'         : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist'        : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
#
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1'         : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2'         : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2allmodes' : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1mode5'    : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p05mode5'   : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield'        : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p1': des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p2': des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk
    elif expid=='nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayieldx2'      : des={'year0' :2000, 'year1' :2009, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort=''#    Dirk

#   NorESM3.0 BETA09 1x1 + sensitivity
#   thomas    
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218'         : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 299
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr001.20251223'         : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 307
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr031.20251227'         : des={'year0' :31, 'year1' : 50, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 309
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr051_cplhist.20251230' : des={'year0' :51, 'year1' :100, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 310
#   dirk
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_lowmicromgautoconlwpexp'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 302
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_highmicromgautoconlwpexp' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 303
#   ada
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.20251220'    : des={'year0' :   1, 'year1' :  18, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.v2.20251222' : des={'year0' :   1, 'year1' :  45, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='nco2x4.ne16pg3_tn14.noresm3_0_beta09.Run3.20260105'             : des={'year0' : 136, 'year1' : 255, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #

    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.clubb_c_k10h.20260112'        : des={'year0' : 251, 'year1' : 280, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.combined_176.20260112'        : des={'year0' : 251, 'year1' : 270, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.combined_176.20260119'        : des={'year0' : 251, 'year1' : 270, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.hetfrz_dust_scalfac.20260112' : des={'year0' : 251, 'year1' : 270, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.zmconv_c0_lnd.20260112'       : des={'year0' : 251, 'year1' : 280, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.zmconv_c0_lnd_ocn.20260112'   : des={'year0' : 251, 'year1' : 270, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.CESM3devTuning.zmconv_c0_lnd_ocn.20260119'   : des={'year0' : 251, 'year1' : 280, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
#   alok
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_lowdp1'  : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #300
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_highdp1' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #304
#
#   NorESM3.0 BETA10 
#   2x2 kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta10.Run6.2026-01-23' : des={'year0' : 406, 'year1' : 455, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 326
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta10.Run7.2026-01-26' : des={'year0' : 456, 'year1' : 585, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 332
#   2x2 ovind fSST nf1850 / nf1850_aer2014
    elif expid=='nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta10.20260209' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}    
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta10.20260210' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}    
#
#   NorESM3.0 BETA11
#   2x2 kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.2026-02-07' : des={'year0' : 586, 'year1' : 810, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 338
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.Olivia.2026-03-08' : des={'year0' : 811, 'year1' : 855, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 362
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta11.Run8_CAMandOCNtuning.Olivia.2026-03-08' : des={'year0' : 811, 'year1' : 860, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 363
#   1x1 tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta11-run1_yr001.20260213' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 349
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta11-run2_yr001.20260213' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 350
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta11-run3_yr001.20260226' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 357

#   NorESM3.0 BETA10/BETA11 TESTS    
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta10.beff025.2026-02-20'   : des={'year0' : 456, 'year1' : 485, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 355 Oyvind
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta11.CAMtuning.20260220'   : des={'year0' : 456, 'year1' : 505, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 354 Mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta11.CAMtuning.20260224'   : des={'year0' : 456, 'year1' : 485, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 356 Mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta11.Run7.OcnTun.20260224' : des={'year0' : 586, 'year1' : 635, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 359 Ada

    elif expid=='nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225' : des={'year0' :1850, 'year1' :1879, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #   Jerry
    elif expid=='nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260311' : des={'year0' :1880, 'year1' :1969, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #   Jerry

#   NorESM3.0 BETA12
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11'                        : des={'year0' : 811, 'year1' : 925, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 365     Kjetil

    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff.2026-03-19'              : des={'year0' : 811, 'year1' : 820, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 372     Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff_TUNED.2026-03-20'        : des={'year0' : 811, 'year1' : 815, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 374     Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff_TUNED.Olivia.2026-03-22' : des={'year0' : 811, 'year1' : 870, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #         Kjetil

    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.ndiff_surface_align.20260317' : des={'year0' : 586, 'year1' : 635, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 380         
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.lamult_reduction.20260314'    : des={'year0' : 586, 'year1' : 635, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 381    
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_sameOcnDiff.2026-03-19'  : des={'year0' : 811, 'year1' : 880, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 373 
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.OcnTun.20260321'         : des={'year0' : 811, 'year1' : 840, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 383        

    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffNoMin.2026-03-26'         : des={'year0' : 811, 'year1' : 820, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #         Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffNoMinOsl.2026-03-27'      : des={'year0' : 811, 'year1' : 860, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 384 Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffOsl_TUNED.Olv.2026-03-30' : des={'year0' : 811, 'year1' : 910, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 388     Kjetil

#   Oyvind reduced Bergeron-Findeisen coefficient 
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.nl363c8beff.2026-03-16' : des={'year0' : 821, 'year1' : 890, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 370        Oyvind

#   Herman test    
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_albice_tuned.20260412'     : des={'year0' : 811, 'year1' : 845, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Herman
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_vtrmi0p8.20260412'         : des={'year0' : 811, 'year1' : 845, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 392 Herman
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_tiedkeadd_tuning.20260421' : des={'year0' : 811, 'year1' : 905, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #     Herman

#   cmip7 forcing tests
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref'         : des={'year0' : 811, 'year1' : 840, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #     Dirk
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc'    : des={'year0' : 811, 'year1' : 840, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #     Dirk
    elif expid=='n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc' : des={'year0' : 811, 'year1' : 840, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #     Dirk
#
#   dust and seasalt test coupled
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.dust.salt'           : des={'year0' :811, 'year1' :830, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='dust + salt2'#    Dirk
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.dust.salt.4p8'       : des={'year0' :811, 'year1' :840, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} ; expidshort='dust + salt2 + 4p8'#    Dirk

#   dus and seasalt ERF tests
#   reference
    elif expid=='nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.ref.startup'          : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.ref.startup'  : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
#   seasalt + dust + belowcloud scavenging    
    elif expid=='nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.all3.startup'         : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.all3.startup' : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
#   seasalt + dust
    elif expid=='nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.startup'         : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.startup' : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
#   seasalt + dust + hygr1.1mode5
    elif expid=='nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.hygr1p1mode5.startup'              : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.hygr1p1mode5.startup'      : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.hygr1p1mode5.startup-corr' : des={'year0' :1, 'year1' :20, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #    Dirk

#   oyvind fSST : nf1850 / nf1805_aer2014
    elif expid=='nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.20260326' : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Oyvind
    elif expid=='nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.20260327' : des={'year0' :1, 'year1' :30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Oyvind

#   NorESM3 BETA12a
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28'               : des={'year0' : 926, 'year1' : 1130, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 385     Kjetil

#   NorESM3 BETA13
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta13.Run11.2026-04-15'                    : des={'year0' : 1131, 'year1' : 1135, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 394   Kjetil

#   NorESM3 BETA13a
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_drydep_oldBLOM.2026-04-17'    : des={'year0' : 1131, 'year1' : 1150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #      Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_oldBLO_oldBLOMv32.2026-04-17' : des={'year0' : 1131, 'year1' : 1150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 396  Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11.OcnTune2026-04-19'            : des={'year0' : 1131, 'year1' : 1180, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #      Ada

#   NorESM3 BETA14
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-04-24'              : des={'year0' : 1136, 'year1' : 1230, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 404   Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-05-04'              : des={'year0' : 1131, 'year1' : 1150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 420   Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta14.Run12.OcnTune2026-04-29'              : des={'year0' : 1131, 'year1' : 1190, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 469   Ada

#   NorESM3 BETA15
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.Olivia.2026-05-05'              : des={'year0' : 1151, 'year1' : 1310, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 421   Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta15.Run12_ATMtune.Olivia.2026-05-10'      : des={'year0' : 1151, 'year1' : 1170, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 427   Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta15.Run12_ATMtune2.Olivia.2026-05-12'     : des={'year0' : 1151, 'year1' : 1190, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #       Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.c8_4p55.Olivia.2026-05-13'      : des={'year0' : 1151, 'year1' : 1180, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #       Kjetil

#   NorESM3 BETA16
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.Olivia.2026-05-18'              : des={'year0' : 1311, 'year1' : 1510, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 439   Kjetil'
#   sslt + dust test (Dirk)
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.4p95'        : des={'year0' : 1311, 'year1' : 1350, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}    
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.hygr1p1.4p8' : des={'year0' : 1311, 'year1' : 1340, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # WRONG NAME : clubb_c8=4.95 still
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.hygr1p1mode5.4p8' : des={'year0' : 1311, 'year1' : 1319, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}   
#   Greenland ice sheet
    elif expid=='n1850Gg.ne16pg3_tn14_gl4.noresm3_0_beta16.Run13.Olivia.2026-05-18_pseudo_hybrid' : des={'year0' : 1321, 'year1' : 1420, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560kmpet, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   NorESM3 BETA18
#   kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14.Olivia.2026-05-28'    : des={'year0' : 1511, 'year1' : 1580, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 442 Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A.Olivia.2026-06-01'  : des={'year0' : 1511, 'year1' : 1520, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A2.Olivia.2026-06-03' : des={'year0' : 1511, 'year1' : 1530, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-B.Olivia.2026-06-03'  : des={'year0' : 1511, 'year1' : 1540, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-C.Olivia.2026-06-04'  : des={'year0' : 1511, 'year1' : 1540, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-D.Olivia.2026-06-04'  : des={'year0' : 1511, 'year1' : 1550, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F.Olivia.2026-06-05'  : des={'year0' : 1511, 'year1' : 1550, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-G.Olivia.2026-06-06'  : des={'year0' : 1511, 'year1' : 1550, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-H.Olivia.2026-06-08'  : des={'year0' : 1511, 'year1' : 1550, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-I.Olivia.2026-06-08'  : des={'year0' : 1511, 'year1' : 1530, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F_blom_cv_1p2.2026-06-12'  : des={'year0' : 1511, 'year1' : 1550, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   BETA19
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta19.Run15.Olivia.2026-06-08'    : des={'year0' : 1551, 'year1' : 1610, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-B.Olivia.2026-06-11'  : des={'year0' : 1551, 'year1' : 1630, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-C.Olivia.2026-06-15'  : des={'year0' : 1551, 'year1' : 1670, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-D.Olivia.2026-06-17'  : des={'year0' : 1551, 'year1' : 1570, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-E.Olivia.2026-06-18'  : des={'year0' : 1551, 'year1' : 1750, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

    elif expid=='nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07'    : des={'year0' : 1850, 'year1' : 2021, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850esm.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07' : des={'year0' : 1531, 'year1' : 1670, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09'    : des={'year0' : 1850, 'year1' : 2021, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   test CO2 mass balance
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst'                      : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid'               : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid.singpre'       : des={'year0' : 1850, 'year1' : 1999, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid.singpre.r2000' : des={'year0' : 2000, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#   test radclimate
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000'        : des={'year0' : 2000, 'year1' : 2001, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000.aco2'   : des={'year0' : 2000, 'year1' : 2001, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000'        : des={'year0' : 2000, 'year1' : 2001, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000.o3clim' : des={'year0' : 2000, 'year1' : 2001, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhistghg.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000'     : des={'year0' : 2000, 'year1' : 2001, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
#
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_ksno04.Olivia.2026-06-23'      : des={'year0' : 1990, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_ksno02.Olivia.2026-06-23'      : des={'year0' : 1990, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnwfall100.Olivia.2026-06-23' : des={'year0' : 1990, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnw075.Olivia.2026-06-23'     : des={'year0' : 1990, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_rsnwfall300.Olivia.2026-06-23' : des={'year0' : 1990, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta19.Base_i449.CICE_phiimushy45.Olivia.2026-06-23' : des={'year0' : 1990, 'year1' : 2019, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   BETA20
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta20.Run15-F.Olivia.2026-06-22' : des={'year0' : 926, 'year1' : 975, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta20.Run16.Olivia.2026-07-02'   : des={'year0' :1751, 'year1' :1760, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 475 Kjetil
#   ada
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta20.470.ref461.20260626' : des={'year0' : 1651, 'year1' : 1750, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 470 Ada
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta20.473.ref461.20260630' : des={'year0' : 1651, 'year1' : 1730, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 473 Ada
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta20.474.ref461.20260630' : des={'year0' : 1651, 'year1' : 1730, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 474 Ada

#   1pctco2
    elif expid=='n1pctCO2.ne16pg3_tn14.beta20.2026-06-12'                       : des={'year0' :   1, 'year1' : 140, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1pctCO2-RAD.ne16pg3_tn14.beta20.2026-06-24'                   : des={'year0' :   1, 'year1' : 140, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    
#   BETA21
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.476.2026-07-03'    : des={'year0' : 926, 'year1' : 975, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 476 Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.i478.2026-07-06'   : des={'year0' : 926, 'year1' :1145, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 478 Kjetil 
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.i480.2026-07-16'   : des={'year0' : 926, 'year1' :1055, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 480 Kjetil 
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260717': des={'year0' : 926, 'year1' :1025, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 481 Mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.i482.2026-07-23'   : des={'year0' :1006, 'year1' :1125, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 482 Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260723': des={'year0' :1006, 'year1' :1105, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 483 Mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.cmeps-latent-heat-bugfix.2026-07-23': des={'year0' : 926, 'year1' :945, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 484 Jens
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta21.coare-const-i380.2026-07-27'        : des={'year0' : 926, 'year1' :975, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 485 Jens

#   BETA22
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.i486.2026-07-31'   : des={'year0' :1106, 'year1' :1185, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 486 Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2.20260730': des={'year0' :1106, 'year1' :1255, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 487 Mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.i489.2026-08-06'   : des={'year0' :1246, 'year1' :1265, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Kjetil
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2_cplhist.20260806': des={'year0' :1246, 'year1' :1345, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 490 Mats
    elif expid=='n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2.20260811': des={'year0' :1346, 'year1' :1395, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 495 Mat
    elif expid=='n1850Gaxg.ne16pg3_tn14_ais8gris4.noresm3_0_beta22.492.ref490.20260811': des={'year0' :1346, 'year1' :1415, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 492 Ada
#   hist
    elif expid=='nhist.ne16pg3_tn14.noresm3_0_beta22.i491.2026-08-10'   : des={'year0' :1850, 'year1' :1869, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 491 Kjetil
    
#   BETA23
    elif expid=='n1850Gaxg.n30b23LM.498.20260815': des={'year0' :1406, 'year1' :1465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 498 Ada
    elif expid=='n1850Gaxg.n30b23LM.502.20260818': des={'year0' :1456, 'year1' :1485, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 502 Ada
#
    elif expid=='n1850.LM.n30b22.507.GAaxg.20260820'         : des={'year0' :1406, 'year1' :1465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 507 Matvey
    elif expid=='n1850.LM.n30b22.507.GAaxg_lnd_ic.20260820'  : des={'year0' :1406, 'year1' :1465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 507 Matvey
    elif expid=='n1850.LM.n30b23.507.GAaxg.20260820'         : des={'year0' :1406, 'year1' :1465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 507 Matvey
    elif expid=='n1850.LM.n30b23.507.GAaxg_lnd_ic.20260820'  : des={'year0' :1406, 'year1' :1515, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 507 Matvey
    elif expid=='n1850.LM.n30b23.507.woGAaxg.20260820'       : des={'year0' :1406, 'year1' :1465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 507 Matvey
    elif expid=='n1850.LM.n30b23.507.woGAaxg_lnd_ic.20260820': des={'year0' :1406, 'year1' :1465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 507 Matvey

#   radiation profile test
    elif expid=='n1850Gaxg.n30b23LM.498.20260815.diagrad.r1446.latlon'        : des={'year0' :1446, 'year1' :1447, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk
    elif expid=='n1850Gaxg.n30b23LM.498.20260815.diagrad.r1446.latlon.co2corr': des={'year0' :1446, 'year1' :1447, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk
#
#   co2-emissiondriven
    elif expid=='n1850esmGaxg.n30b23LM.XYZ.20260820' : des={'year0' :1466, 'year1' :1485, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Jerry
    elif expid=='n1850esmGaxg.n30b23LM.508.20260824' : des={'year0' :1466, 'year1' :1615, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 508 Jerry
#
#   BETA24
    elif expid=='n1850Gaxg.LM.n30b24.511.betzy.20260904'     : des={'year0' :1406, 'year1' :1435, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 511 Ada
    elif expid=='n1850GaxgGHG.LM.n30b24.511.betzy.20260904'  : des={'year0' :1406, 'year1' :1425, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 511 Ada
    elif expid=='n1850Gaxg.LM.n30b24.516.20260909'           : des={'year0' :1426, 'year1' :1475, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 516 Ada - new spinup GrIS
    elif expid=='n1850GaxgGHG.LM.n30b24.516.20260909'        : des={'year0' :1426, 'year1' :1525, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 516 Ada - new spinup GrISn1850Gaxg.LM.n30b24.513.betzy.20260905.ubcnone
    elif expid=='n1850GaxgGHG.LM.n30b24.517.20260911'        : des={'year0' :1456, 'year1' :1525, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 517 Ada
    elif expid=='n1850GaxgGHG.LM.n30b24.517.branch.20260913' : des={'year0' :1456, 'year1' :1475, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 517 Ada
    elif expid=='n1850GaxgGHG.LM.nor30b24.525.20260923'      : des={'year0' :1526, 'year1' :1571, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 525 Ada
#   sensitivity Dirk
    elif expid=='n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcnone'   : des={'year0' :1406, 'year1' :1435, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 513 Dirk
    elif expid=='n1850Gaxg.LM.n30b24.513.betzy.20260905.o3clim'    : des={'year0' :1406, 'year1' :1435, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 513 Dirk
    elif expid=='n1850Gaxg.LM.n30b24.513.betzy.20260905.oxid'      : des={'year0' :1406, 'year1' :1435, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 513 Dirk
    elif expid=='n1850Gaxg.LM.n30b24.513.betzy.20260905.emish2o'   : des={'year0' :1406, 'year1' :1435, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 513 Dirk
    elif expid=='n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcfix'    : des={'year0' :1406, 'year1' :1425, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 513 Dirk
#   emission-driven  
    elif expid=='n1850esmGaxgGHG.LM.n30b24.20260916'    : des={'year0' :1476, 'year1' :1485, 'model' : 'NorESM2.5', 'subdir' : lakedirns11118knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Jerry
    elif expid=='n1850esmGaxgGHG.LM.n30b24.20260919'    : des={'year0' :1476, 'year1' :1485, 'model' : 'NorESM2.5', 'subdir' : lakedirns11118knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Jerry
#
#   BETA25
    elif expid=='n1850GaxgGHG.LM.nor30b25.526.redout.20260928'      : des={'year0' :1526, 'year1' :1545, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 526 Ada
    elif expid=='n1850GaxgGHG.LM.nor30b25.528.20260928'             : des={'year0' :1526, 'year1' :1715, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 528 Mariana
#   emission-driven
    elif expid=='n1850esmGaxgGHG.LM.n30b25.20260928'                : des={'year0' :1526, 'year1' :1585, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 523 Jerry
    elif expid=='n1850esmGaxgGHG.LM.n30b25.529.20261002'            : des={'year0' :1566, 'year1' :1755, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 523 Jerry
#
#   BETA27
    elif expid=='n1850esmGHGGaxg.LM.nor30b27.001.20261016'          : des={'year0' :  1, 'year1' :100, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 001 Jerry
    elif expid=='n1850GHGGaxg.LM.nor30b27.002.20261016'             : des={'year0' :  1, 'year1' :125, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 002 Kjetil

    elif expid=='n1850esmGHGGaxg.LM.nor30b27.003.20261024'          : des={'year0' :101, 'year1' :150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 003 Jerry
    elif expid=='n1pctCO2-bgcGHGGaxg.LM.nor30b27.007.20261027'      : des={'year0' :  1, 'year1' : 10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 003 Jerry

    elif expid=='n1850GHGGaxg.LM.nor30b27.002.20261022.oxidtest'    : des={'year0' :  1, 'year1' : 20, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}

#   CO2-emissiondriven tests 
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120'                                        : des={'year0' : 251, 'year1' : 280, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Jerry : only land and ocean flux
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120huit'                                    : des={'year0' : 251, 'year1' : 255, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Jerry : only land and ocean flux
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260120'                         : des={'year0' : 251, 'year1' : 265, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : no flux
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260121'                         : des={'year0' : 261, 'year1' : 275, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : no flux
    elif expid=='n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_surfacefossilfuelemis_only.20260120' : des={'year0' :2015, 'year1' :2074, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Ada   : only surface anthro flux
    elif expid=='n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_aircraftemis_only.20260120'          : des={'year0' :2015, 'year1' :2059, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Ada   : only aircraft anthro flux
    elif expid=='n1850esm.ne16pg3_tn14.noresm3_0_beta10_onlyOcnFx_20260123'                             : des={'year0' : 251, 'year1' : 270, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Jerry : only ocean flux
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxviacplocn.20260127'    : des={'year0' : 251, 'year1' : 260, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : lnd flux via ocn cpl (slightly different setup from beta10_20260120)
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxviacplocn.20260127bis' : des={'year0' : 251, 'year1' : 260, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : lnd flux via ocn cpl (exactly same setup from beta10_20260120)
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxviacplocn.20260127tris': des={'year0' : 251, 'year1' : 257, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : lnd flux via ocn cpl (exactly same setup from beta10_20260120)
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxonlyneg.20260127'      : des={'year0' : 251, 'year1' : 260, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : only neg lnd flux 
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxonlypos.20260127'      : des={'year0' : 251, 'year1' : 260, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : only neg lnd flux 

    elif expid=='n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120b'       : des={'year0' :2015, 'year1' :2064, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Dirk  : only neg lnd flux


#   1x1
#   BETA10
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run1_yr101.20260120'             : des={'year0' : 101, 'year1' : 150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #319
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run2_yr101.20260120'             : des={'year0' : 101, 'year1' : 120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #320
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run3_yr101.20260123'             : des={'year0' : 101, 'year1' : 150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #327
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run4_yr101.20260126'             : des={'year0' : 101, 'year1' : 150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #328
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run5_yr121.20260127'             : des={'year0' : 121, 'year1' : 125, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #330
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run6_yr121.20260128'             : des={'year0' : 121, 'year1' : 130, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #333
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run7_yr121.20260128'             : des={'year0' : 121, 'year1' : 130, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #334
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta10-run8_yr121.20260131'             : des={'year0' : 121, 'year1' : 150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #335
#   BETA12a
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta12a-run1_yr001.20260313'            : des={'year0' :  1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 367 Tomas 
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta12a-run2_yr031.20260321'            : des={'year0' : 31, 'year1' : 40, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta12a-run3_yr031.20260329'            : des={'year0' : 31, 'year1' : 40, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta12a-run5_yr061_olivia.20260403'     : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta12a-run4_yr031.20260403'            : des={'year0' : 31, 'year1' : 40, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta12a-run1_yr001_olivia.20260313'     : des={'year0' :  1, 'year1' : 60, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 368 Tomas
#   BETA13b
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta13b-run1_yr061.20260423'            : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 389 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta13b-run3_yr061.20260423'            : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 403
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta13b-run2_yr061.20260424'            : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 402 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta13b-run4_yr061.20260426'            : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 406
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta13b-run5_yr061.20260426'            : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 408 Tomas
#   BETA14
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run3_yr061.20260427'             : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run2_yr061.20260427'             : des={'year0' : 61, 'year1' : 70, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 417 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run4_yr061.20260429'             : des={'year0' : 61, 'year1' : 75, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 418 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run5_yr076.20260504'             : des={'year0' : 76, 'year1' :105, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 419 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run6_yr001.20260505'             : des={'year0' :  1, 'year1' : 30, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 422 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run7_yr101.20260508'             : des={'year0' :101, 'year1' :120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 425 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run10_yr101.20260513'            : des={'year0' :101, 'year1' :150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 428 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run12_yr101.20260516'            : des={'year0' :101, 'year1' :150, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 430 Tomas
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta14-run13_yr101.20260521'            : des={'year0' :101, 'year1' :130, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 441 Tomas
#   BETA15
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta15-run12_yr151.cplhist.20260529'    : des={'year0' :151, 'year1' :220, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 445 Tomas
#   BETA18
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta18.20260530'                        : des={'year0' :101, 'year1' :120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 443 Mats
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta18.20260606'                        : des={'year0' :101, 'year1' :120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 443 Mats
    elif expid=='n1850.ne30pg3_tn14.noresm3_0_beta18.egc_1p5.20260612'                : des={'year0' :101, 'year1' :120, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 443 Mats
#   BETA19
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta19-run13_yr151.20260618'            : des={'year0' :151, 'year1' :160, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Tomas
#   BETA20 
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta20-run13_yr151.20260619'            : des={'year0' :151, 'year1' :170, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Tomas
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta20-run13_yr151.20260626'            : des={'year0' :151, 'year1' :160, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Tomas
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta20-run14_yr151.20260630'            : des={'year0' :151, 'year1' :190, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 471 Tomas
#   BETA21
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta21-run1_yr101.20260711'             : des={'year0' :101, 'year1' :105, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Tomas
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta21-run2_yr101.20260711'             : des={'year0' :101, 'year1' :105, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Tomas
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta21-run3_yr101.20260711'             : des={'year0' :101, 'year1' :110, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # Tomas
#   BETA22
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta22.yr101.i488.20260810'             : des={'year0' :101, 'year1' :140, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 488 Tomas
    elif expid=='N1850.ne30pg3_tn14.noresm3_0_beta22.yr101.i493.20260810'             : des={'year0' :101, 'year1' :110, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 493 Tomas
#   BETA23
    elif expid=='N1850.n30b23MM.i496.20260815'             : des={'year0' :101, 'year1' :130, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 496 Tomas
    elif expid=='N1850.n30b23MM.506.20260821'              : des={'year0' :121, 'year1' :200, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 506 Tomas
    elif expid=='N1850.MM.nor30b23.509.20260901'           : des={'year0' :171, 'year1' :190, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 509 Tomas
#   BETA24
    elif expid=='N1850.MM.nor30b24.515.20260908'           : des={'year0' :171, 'year1' :310, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 515 Tomas
    elif expid=='N1850.MM.nor30b24.HF-output.512.20260904' : des={'year0' :171, 'year1' :175, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 512 Tomas
    elif expid=='N1850.MM.nor30b24.520.20260913'           : des={'year0' :201, 'year1' :280, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 520 Tomas
#   BETA25
    elif expid=='n1850GHG.MM.nor30b25.527.20260928'    : des={'year0' :296, 'year1' :300, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}
    elif expid=='n1850GHG.MM.nor30b25.527.redout.20260929' : des={'year0' :301, 'year1' :420, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} # 527 Ada


#
#   cmip7 forcing test
#   reference
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6.20260127'              : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #320
#   cmip7 emission
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip7.20260127'              : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv19cmip7.20260127'              : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emine16pg3cmip7.20260127'           : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emine16pg3cmip7bcocs.20260127'      : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emine16pg3cmip7bcocsall.20260127'   : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
#   cmip7 volcanic
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6_volcaodcmip7.20260127' : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
#   cmip7 ozone
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6_ozonecmip7.20260127' : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
#   cmip7 oxidants
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6_oxidantcmip7.20260127' : des={'year0' : 456, 'year1' : 465, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #
#   cmip7 no H2O UBC 
    elif expid=='n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6_ubcnone.20260127' : des={'year0' : 456, 'year1' : 460, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'} #

# Ove - PPE
    elif expid=='NFLTHIST_ne16pg3_ne16pg3_mtn14_Nudging_PPE_Baseline_20251110' : des=des={'year0' : 2017, 'year1' : 2017, 'model' : 'NorESM2.5', 'subdir' : lakedirns2345kovewh, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', 'project' : '', 'dataformat' : 'rawnoresm'}


# ESGF - CMIP6 - piControl
    elif expid=='ACCESS-CM2_piControl_r1i1p1f1_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='ACCESS-ESM1-5_piControl_r1i1p1f1_gn'          : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='BCC-CSM2-MR_piControl_r1i1p1f1_gn'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CAMS-CSM1-0_piControl_r1i1p1f1_gn'            : des={'year0' : 2900, 'year1' : 3399, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r10i1p1f1_gn'               : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r1i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r1i1p2f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r2i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r3i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r4i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r5i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r6i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r7i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r8i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_piControl_r9i1p1f1_gn'                : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5-CanOE_piControl_r1i1p2f1_gn'          : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CAS-ESM2-0_piControl_r1i1p1f1_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CESM2_piControl_r1i1p1f1_gn'                  : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CESM2-WACCM_piControl_r1i1p1f1_gn'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CMCC-CM2-SR5_piControl_r1i1p1f1_gn'           : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1-HR_piControl_r1i1p1f2_gr'          : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1_piControl_r1i1p1f2_gr'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1_piControl_r2i1p1f2_gr'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1_piControl_r3i1p1f2_gr'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-ESM2-1_piControl_r1i1p1f2_gr'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='EC-Earth3_piControl_r1i1p1f1_gr'              : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='EC-Earth3-Veg_piControl_r1i1p1f1_gr'          : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='FGOALS-f3-L_piControl_r1i1p1f1_gr'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='FGOALS-g3_piControl_r1i1p1f1_gn'              : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='FIO-ESM-2-0_piControl_r1i1p1f1_gn'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GFDL-CM4_piControl_r1i1p1f1_gr1'              : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GFDL-ESM4_piControl_r1i1p1f1_gr1'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GISS-E2-1-G_piControl_r1i1p1f2_gn'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GISS-E2-1-G_piControl_r1i1p3f1_gn'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_piControl_r1i1p1f1_gn'        : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_piControl_r1i1p1f3_gn'        : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_piControl_r2i1p1f3_gn'        : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_piControl_r3i1p1f3_gn'        : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='INM-CM4-8_piControl_r1i1p1f1_gr1'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='INM-CM5-0_piControl_r1i1p1f1_gr1'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='IPSL-CM6A-LR_piControl_r1i1p1f1_gr'           : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='IPSL-CM6A-LR_piControl_r2i1p1f1_gr'           : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='IPSL-CM6A-LR_piControl_r3i1p1f1_gr'           : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='KACE-1-0-G_piControl_r1i1p1f1_gr'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='KACE-1-0-G_piControl_r2i1p1f1_gr'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='KIOST-ESM_piControl_r1i1p1f1_gr1'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MCM-UA-1-0_piControl_r1i1p1f1_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MCM-UA-1-0_piControl_r1i1p1f2_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MIROC6_piControl_r1i1p1f1_gn'                 : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MIROC-ES2L_piControl_r1i1p1f2_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MPI-ESM1-2-HR_piControl_r1i1p1f1_gn'          : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MPI-ESM1-2-LR_piControl_r1i1p1f1_gn'          : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MRI-ESM2-0_piControl_r1i1p1f1_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NorESM2-LM_piControl_r1i1p1f1_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NorESM2-MM_piControl_r1i1p1f1_gn'             : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NESM3_piControl_r1i1p1f1_gn'                  : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='UKESM1-0-LL_piControl_r1i1p1f2_gn'            : des={'year0' : 1, 'year1' : 9999, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
#
# ESGF - CMIP6 -historical
    elif expid=='NorESM2-LM_historical_r1i1p1f1_gn'             : des={'year0' : 1850, 'year1' : 2014, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NorESM2-MM_historical_r1i1p1f1_gn'             : des={'year0' : 1850, 'year1' : 2014, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}


# ESGF - CMIP6 - ssp245
    elif expid=='ACCESS-CM2_ssp245_r1i1p1f1_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='ACCESS-ESM1-5_ssp245_r1i1p1f1_gn'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='AWI-CM-1-1-MR_ssp245_r1i1p1f1_gn'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='BCC-CSM2-MR_ssp245_r1i1p1f1_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CAMS-CSM1-0_ssp245_r1i1p1f1_gn'            : des={'year0' : 2015, 'year1' : 2099, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r10i1p1f1_gn'               : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r1i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r1i1p2f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r2i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r3i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r4i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r5i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r6i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r7i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r8i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5_ssp245_r9i1p1f1_gn'                : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CanESM5-CanOE_ssp245_r1i1p2f1_gn'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CAS-ESM2-0_ssp245_r1i1p1f1_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CESM2_ssp245_r1i1p1f1_gn'                  : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CESM2_ssp245_r4i1p1f1_gn'                  : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CESM2-WACCM_ssp245_r1i1p1f1_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CESM2-WACCM_ssp245_r2i1p1f1_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CMCC-CM2-SR5_ssp245_r1i1p1f1_gn'           : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CMCC-ESM2_ssp245_r1i1p1f1_gn'              : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1-HR_ssp245_r1i1p1f2_gr'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1_ssp245_r1i1p1f2_gr'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1_ssp245_r2i1p1f2_gr'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-CM6-1_ssp245_r3i1p1f2_gr'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='CNRM-ESM2-1_ssp245_r1i1p1f2_gr'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='EC-Earth3-CC_ssp245_r1i1p1f1_gr'           : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='EC-Earth3_ssp245_r1i1p1f1_gr'              : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='EC-Earth3-Veg_ssp245_r1i1p1f1_gr'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='EC-Earth3-Veg-LR_ssp245_r1i1p1f1_gr'       : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='FGOALS-f3-L_ssp245_r1i1p1f1_gr'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='FGOALS-g3_ssp245_r1i1p1f1_gn'              : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='FIO-ESM-2-0_ssp245_r1i1p1f1_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GFDL-CM4_ssp245_r1i1p1f1_gr1'              : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GFDL-ESM4_ssp245_r1i1p1f1_gr1'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GISS-E2-1-G_ssp245_r1i1p1f2_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GISS-E2-1-G_ssp245_r1i1p3f1_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GISS-E2-1-G_ssp245_r102i1p1f1_gn'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='GISS-E2-1-G-CC_ssp245_r102i1p1f1_gn'       : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_ssp245_r1i1p1f3_gn'        : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_ssp245_r2i1p1f3_gn'        : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='HadGEM3-GC31-LL_ssp245_r3i1p1f3_gn'        : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='INM-CM4-8_ssp245_r1i1p1f1_gr1'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='INM-CM5-0_ssp245_r1i1p1f1_gr1'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='IPSL-CM6A-LR_ssp245_r1i1p1f1_gr'           : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='IPSL-CM6A-LR_ssp245_r2i1p1f1_gr'           : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='IPSL-CM6A-LR_ssp245_r3i1p1f1_gr'           : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='KACE-1-0-G_ssp245_r1i1p1f1_gr'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='KACE-1-0-G_ssp245_r2i1p1f1_gr'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='KIOST-ESM_ssp245_r1i1p1f1_gr1'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MCM-UA-1-0_ssp245_r1i1p1f2_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MIROC6_ssp245_r1i1p1f1_gn'                 : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MIROC-ES2L_ssp245_r1i1p1f2_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MPI-ESM1-2-HR_ssp245_r1i1p1f1_gn'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MPI-ESM1-2-LR_ssp245_r1i1p1f1_gn'          : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='MRI-ESM2-0_ssp245_r1i1p1f1_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NorESM2-LM_ssp245_r1i1p1f1_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NorESM2-MM_ssp245_r1i1p1f1_gn'             : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='NESM3_ssp245_r1i1p1f1_gn'                  : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
    elif expid=='UKESM1-0-LL_ssp245_r1i1p1f2_gn'            : des={'year0' : 2015, 'year1' : 2100, 'model' : '', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v4', 'project' : ''}
#
#   TOAR [2023-2025] other models :
#   CESM2
    elif expid=='CESM2_pdClim-control_r1i1p1f1_gn'                 : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-control_r2i1p1f1_gn'                 : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-control_r1r2i1p1f1_gn'               : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # ensemble
    elif expid=='CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn'        : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn'        : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn'      : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # ensemble
    elif expid=='CESM2_pdClim-fixO3_r1i1p1f1_gn'                   : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-fixO3_r2i1p1f1_gn'                   : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-fixO3_r1r2i1p1f1_gn'                 : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # ensemble
    elif expid=='CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn'   : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn'   : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn' : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # ensemble
    elif expid=='CESM2_pdClim-2050ssp370fODS-radO3_r1i1p1f1_gn'    : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-2050ssp370fODS-radO3_r2i1p1f1_gn'    : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='CESM2_pdClim-2050ssp370fODS-radO3_r1r2i1p1f1_gn'  : des={'year0' : 1, 'year1' : 50, 'model' : 'CESM2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # ensemble

#   DLR-EMAC
    elif expid=='DLR-EMAC_pdClim-control_r1i1p1f1_gn'                 : des={'year0' : 2012, 'year1' : 2016, 'model' : 'DLR-EMAC',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn'        : des={'year0' : 2012, 'year1' : 2016, 'model' : 'DLR-EMAC',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='DLR-EMAC_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gn' : des={'year0' : 2012, 'year1' : 2016, 'model' : 'DLR-EMAC',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # not to be used anymore (too short spinup)
    elif expid=='DLR-EMAC_pdClim-2050ssp370onlyODS-radO3_r1i2p1f1_gn' : des={'year0' : 2012, 'year1' : 2016, 'model' : 'DLR-EMAC',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # longer spinup
#   GEOS-Chem
    elif expid=='GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr'         : des={'year0' : 2019, 'year1' : 2023, 'model' : 'GEOS-Chem-14.2.2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # 2015-2020 until 2024-10-24
    elif expid=='GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr': des={'year0' : 2019, 'year1' : 2023, 'model' : 'GEOS-Chem-14.2.2',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} # 2015-2020 until 2024-10-24
#   GFDL-ESM4
    elif expid=='GFDL-ESM4_pdClim-control_r1i1p1f1_gr'                 : des={'year0' :    1, 'year1' :   70, 'model' : 'GFDL-ESM4',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} 
    elif expid=='GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr'        : des={'year0' :    1, 'year1' :   70, 'model' : 'GFDL-ESM4',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} 
    elif expid=='GFDL-ESM4_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gr' : des={'year0' :    1, 'year1' :   70, 'model' : 'GFDL-ESM4',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'} 
#   GISS FREE RUNNING
    elif expid=='GISS-E2.1-G_pdClim-control_r1i1p1f1_gr'          : des={'year0' : 2015, 'year1' : 2044, 'model' : 'GISS-E2.1-G',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr' : des={'year0' : 2015, 'year1' : 2044, 'model' : 'GISS-E2.1-G',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
#   GISS NUDGED
    elif expid=='GISS-E2-1-G_pdClim-control_r1i1p3f2_gn'           : des={'year0' : 2019, 'year1' : 2034, 'model' : 'GISS-E2-1-G',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn'  : des={'year0' : 2019, 'year1' : 2034, 'model' : 'GISS-E2-1-G',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
#   NorESM2-LM
    elif expid=='NorESM2-LM_pdClim-control_r1i1p1f1_gn'         : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2-LM', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='NorESM2-LM_pdClim-2050ssp370-radO3_r1i1p1f1_gn'             : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2-LM', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='NorESM2-LM_pdClim-2050ssp370noAER-radO3_r1i1p1f1_gn'        : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2-LM', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn'                 : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2-LM', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='NorESM2-LM_pdClim-controlfixO3-2050ssp370_r1i1p1f1_gn'      : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2-LM', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn' : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2-LM', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
#   UKESM1-0-LL
    elif expid=='UKESM1-0-LL_pdClim-control_r1i1p1f2_gn'                 : des={'year0' : 2000, 'year1' : 2069, 'model' : 'UKESM1-0-LL',   'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn'        : des={'year0' : 2000, 'year1' : 2069, 'model' : 'UKESM1-0-LL',   'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
    elif expid=='UKESM1-0-LL_pdClim-2050ssp370onlyODS-radO3_r1i1p1f2_gn' : des={'year0' : 2000, 'year1' : 2069, 'model' : 'UKESM1-0-LL',   'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized'}
#
#   ESM2025 CH4 [2025] other models
    elif expid=='CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn' : des={'year0' : 1979, 'year1' : 2014, 'model' : 'CanESM5-1c-amip-ch4p-test5', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'esm2025ch4', 'dataformat':'cmorized'}
    elif expid=='CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr'           : des={'year0' : 1969, 'year1' : 2014, 'model' : 'CNRM-ESM2-1'               , 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'esm2025ch4', 'dataformat':'cmorized'}
    elif expid=='MIROC-ES2L-CHEM_amip_r1i1p1f1_gn'            : des={'year0' : 1979, 'year1' : 2014, 'model' : 'MIROC-ES2L-CHEM'           , 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'esm2025ch4', 'dataformat':'cmorized'}
    elif expid=='UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn'         : des={'year0' : 1979, 'year1' : 2014, 'model' : 'UKESM1-0-LL'               , 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'esm2025ch4', 'dataformat':'cmorized'}
#
#   HYWAY other models
    elif expid=='CESM2-v212_hyway_transient2010s_r1'         : des={'year0' : 2010, 'year1' : 2019, 'model' : 'CESM2-v212'       , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='EC-Earth3-AerChem_hyway_transient2010s_r1'  : des={'year0' : 2010, 'year1' : 2019, 'model' : 'EC-Earth3-AerChem', 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='EMAC-DLR_hyway_transient2010s_r1'           : des={'year0' : 2010, 'year1' : 2019, 'model' : 'EMAC-DLR'         , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='EMAC-DLR_hyway_transient2010s_r2'           : des={'year0' : 2010, 'year1' : 2019, 'model' : 'EMAC-DLR'         , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='LMDZ-INCA_hyway_transient2010s_r1'          : des={'year0' : 2010, 'year1' : 2019, 'model' : 'LMDZ-INCA'        , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='NorESM2-LM-C_hyway_transient2010s_r1i1p1f1' : des={'year0' : 2010, 'year1' : 2019, 'model' : 'NorESM2-LM-C'     , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='OsloCTM3v1-2_hyway_transient2010s_r1'       : des={'year0' : 2010, 'year1' : 2019, 'model' : 'OsloCTM3v1-2'     , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}
    elif expid=='UKESM1-0-LL_hyway_transient2010s_r1'        : des={'year0' : 2010, 'year1' : 2019, 'model' : 'UKESM1-0-LL'      , 'subdir' : basedirns11106k, 'cexpid' : expid, 'clmh0' : '', 'chem' : '',  'globdatadir' : 'timeblocks-cmip6-v5', 'project' : 'hyway', 'dataformat':'cmorized'}

    else : 
        print('*** experimentdefinition.py HALLO ***')
        print('MILJAAAAAAAAAAAAAAAAR')
        print('No expid recognized = ...'+str(expid)+'...')
        quit()
    #
#   ADD cdir to dictionary
    if ( cdir != None ) : des['cdir'] = cdir
    else                : des['cdir'] = des['cexpid']

#   ADD expidshort to dictionary
    if ( expidshort != None ) : des['expidshort'] = expidshort
    else                      : des['expidshort'] = des['cexpid']

#    print('YEAR0 : '+str(des['year0']))
#    print('YEAR1 : '+str(des['year1']))
#    print('SUBDIR : '+str(des['subdir']))
#    print('CEXPID : '+str(des['cexpid']))
    #
    return des
