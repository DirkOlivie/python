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
    basedirns2345kaerocom='/projects/NS2345K/noresm/olivie/aerocom'
    basedirns2345knoresm22='/projects/NS2345K/noresm/olivie/noresm2.2'
    basedirns2345kemissionmip='/projects/NS2345K/noresm/olivie/emissionmip'
    basedirns2345kmmppecloud='/projects/NS2345K/noresm/olivie/mmppe-cloud'
    oyvindsns2345kmmppecloud='/projects/NS2345K/oyvinds/mmppe-cloud'
    basedirns2345kimbalancemip='/projects/NS2345K/noresm/olivie/imbalancemip'
    basedirns2345kesm2025ozone='/projects/NS2345K/noresm/olivie/esm2025-ozone'
    basedirns2345koyvind='/projects/NS2345K/oyvinds/cases'
    basedirns9252kheiko='/projects/NS9252K/users/heig/NorESM/archive'
    basedirns9560kn2otest='/projects/NS9560K/users/olivie/noresm/cases/n2o-tests'
    basedirns9560kn2olandtest='/projects/NS9560K/users/olivie/noresm/cases/n2o-land-tests'
    lakedirns2345kn2olandtest='/datalake/NS2345K/olivie/noresm/cases-group/n2o-land-tests'
    basedirns9560kch4test='/projects/NS9560K/users/olivie/noresm/cases/ch4-tests'
    basedirns9560kimbalancemip='/projects/NS9560K/users/olivie/noresm/cases/imbalancemip'
    basedirns9560ktoarmip='/projects/NS9560K/users/olivie/noresm/cases/toarmip'
    lakedirns2345ktoarmip='/datalake/NS2345K/olivie/noresm/cases-group/toarmip'
    basedirns9560kbromo='/projects/NS9560K/users/olivie/noresm/cases/bromoform'
    basedirns9560krefactor='/projects/NS9560K/users/olivie/noresm/cases/refactor'
    basedirns9560kkeyclimerf='/projects/NS9560K/users/olivie/noresm/cases/keyclim-erf'
    basedirns9560kingvild='/projects/NS9560K/users/ingvisau'
    lakedirns9560k='/datalake/NS9560K/noresm/cases'
    lakedirns2345knoresm23test='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.3-test'
    scratchdir='/scratch/olivie/archive/'    
    esgfdir='/projects/NS9252K/CMIP6'
    #
    # noresm1 (official) : 4xco2 and picontrol
    if   expid=='N18504XAERCN_f19_g16_01' : des={'year0' :  1, 'year1' : 150, 'model' : 'NorESM1', 'subdir' : expid+'/atm/hist', 'chem' : ''} # 4xCO2
#
# TOAR (Fiona and Bill)
    elif expid=='NF1850norbc_tropstratchem_f19_20230515_test01'     : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NF1850norbc_tropstratchem_f19_toar_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NF1850norbc_tropstratchem_f19_toar_20230605_sim05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
#   new simulations (corrected heterogenous freezing and koagsub)
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'} 
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
#   prescribing the ozone climatologies
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01'     : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01'     : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2'}
#
    else : 
        print('*** experimentdefinition.py HALLO ***')
        print('No expid recognized = ...'+str(expid)+'...')
        quit()
    #
    print('YEAR0 : '+str(des['year0']))
    print('YEAR1 : '+str(des['year1']))
    print('SUBDIR : '+str(des['subdir']))
    print('CEXPID : '+str(des['cexpid']))
    #
    return des
