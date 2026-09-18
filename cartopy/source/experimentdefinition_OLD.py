def getexpidinfo (expid) :
    '''
    MODIFICATION
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
    basedirns9560koyvind='/projects/NS9560K/oyvinds/cases'
    basedirns2345kmmppecloud='/projects/NS2345K/noresm/olivie/mmppe-cloud'
    oyvindsns2345kmmppecloud='/projects/NS2345K/oyvinds/mmppe-cloud'
    basedirns2345kimbalancemip='/projects/NS2345K/noresm/olivie/imbalancemip'
    basedirns2345kesm2025ozone='/projects/NS2345K/noresm/olivie/esm2025-ozone'
    lakedirns2345kesm2025ozone='/datalake/NS2345K/olivie/noresm/cases-group/esm2025-ozone'
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
    lakedirns9252k='/datalake/NS9252K/cases'
    lakedirns2345knoresm21performance='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.1-performance'
    lakedirns2345knoresm23test='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.3-test'
    lakedirns2345knoresm25test='/datalake/NS2345K/olivie/noresm/cases-group/noresm2.5-test'
    lakedirns2345kcamsvsls='/datalake/NS2345K/olivie/noresm/cases-group/cams-vsls'
    basedirns9560kcamsvsls='/projects/NS9560K/users/olivie/noresm/cases/cams-vsls'
    lakedirns9560knoresm3='/datalake/NS9560K/noresm3/cases'
    scratchdir='/scratch/olivie/archive/'    
    esgfdir='/projects/NS9252K/CMIP6'
    #
# CMIP6 NHIST
    if expid=='NHIST_f19_tn14_20190710'                 : des={'year0' : 1950, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}  

# CMIP6 - cpl
#   piControl [2x2]
    elif expid=='N1850_f19_tn14_20190621'          : des={'year0' : 1600, 'year1' : 1800, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthlyuntil1700' , 'chem' : '', project : ''}
    elif expid=='N1850_f19_tn14_20190722'          : des={'year0' : 1801, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual' , 'chem' : '', project : ''}
    elif expid=='N1850_f19_tn14_20190802'          : des={'year0' : 1901, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', project : ''}
#
#   piControl [1x1]    
    elif expid=='N1850frc2_f09_tn14_20191001'      : des={'year0' : 1200, 'year1' : 1299, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', project : ''}
    elif expid=='N1850frc2_f09_tn14_20191012'      : des={'year0' : 1300, 'year1' : 1449, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual' , 'chem' : '', project : ''} # contains also 1450
    elif expid=='N1850frc2_f09_tn14_20191012len65'      : des={'year0' : 1300, 'year1' : 1364, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : 'N1850frc2_f09_tn14_20191012', 'chem' : '', project : ''}
#   elif expid=='N1850frc2_f09_tn14_20191012_1320_1349' : des={'year0' : 1320, 'year1' : 1349, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : 'N1850frc2_f09_tn14_20191012', 'chem' : '', project : ''}
#   elif expid=='N1850frc2_f09_tn14_20191012_1351_1380' : des={'year0' : 1351, 'year1' : 1380, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : 'N1850frc2_f09_tn14_20191012', 'chem' : '', project : ''}
    elif expid=='N1850frc2_f09_tn14_20191113'           : des={'year0' : 1450, 'year1' : 1699, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', project : ''}

#   historical [2x2]
    elif expid=='NHIST_f19_tn14_20190625'          : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHIST_f19_tn14_20190710'          : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHIST_f19_tn14_20190625ext'       : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', project : ''}
    elif expid=='NHIST_02_f19_tn14_20190801'       : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHIST_02_f19_tn14_20190813'       : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHIST_02_f19_tn14_20190801ext'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', project : ''}
    elif expid=='NHIST_03_f19_tn14_20190801'       : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHIST_03_f19_tn14_20190813'       : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}    
    elif expid=='NHIST_03_f19_tn14_20190801ext'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', project : ''}

#   historical [1x1]
    elif expid=='NHISTfrc2_f09_tn14_20191001'      : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_f09_tn14_20191025'      : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_f09_tn14_20191001ext'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', project : ''}
    elif expid=='NHISTfrc2_02_f09_tn14_20200427'   : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_02_f09_tn14_20200519'   : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual'  , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_02_f09_tn14_20200427ext': des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', project : ''}
    elif expid=='NHISTfrc2_03_f09_tn14_20200519'   : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_03_f09_tn14_20200619'   : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'annual' , 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_03_f09_tn14_20200519ext': des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'clmh0' : ''        , 'chem' : '', 'globdatadir': '', project : ''}
    elif expid=='NHISTfrc2_f09_tn14_20200718'      : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''} # identical to member 1 + AEROCOM output
    elif expid=='NSSP245frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP245frc2_02_f19_tn14_20191014' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP245frc2_03_f19_tn14_20191014' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP370frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP370frc2_02_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370frc2_03_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370LOWNTCFfrc2_f19_tn14_20191118'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370LOWNTCFfrc2_02_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370LOWNTCFfrc2_03_f19_tn14_20191118' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370REFGHGLOWNTCFfrc2_f19_tn14_20191220'    : des={'year0' : 2015, 'year1' : 2059, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370REFGHGLOWNTCFfrc2_02_f19_tn14_20191220' : des={'year0' : 2015, 'year1' : 2059, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP370REFGHGLOWNTCFfrc2_03_f19_tn14_20191220' : des={'year0' : 2015, 'year1' : 2059, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NSSP585frc2_f19_tn14_20191014'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
#   
    elif expid=='NFSSP370frc2norbc_f19_20200110'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP370frc2norbc_aerlow_f19_20200110' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
#
    elif expid=='NFSSP245frc2norpibc_f19_20200520'                : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NFSSP245frc2norpibc_02_f19_20200703'             : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NFSSP245frc2norpibc_03_f19_20200703'             : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NFSSP245frc2norpibc_ghgonly_f19_20200522'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_ghgonly_02_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_ghgonly_03_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_natonly_f19_20200522'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NFSSP245frc2norpibc_natonly_02_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NFSSP245frc2norpibc_natonly_03_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NFSSP245frc2norpibc_aeroxidonly_f19_20200522'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_aeroxidonly_02_f19_20200703' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_aeroxidonly_03_f19_20200703' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_aeronly_f19_20200522'        : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_aeronly_02_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NFSSP245frc2norpibc_aeronly_03_f19_20200703'     : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
  
    elif expid=='NFSSP245frc2norpibc_ghgonly_f19_20200522' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
#
#   scenarios f09
    elif expid=='NSSP126frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '','globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP245frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '','globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP370frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '','globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP585frc2_f09_tn14_20191105'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '','globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='NSSP585frc2_f09_tn14_20200919'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns2345k, 'cexpid' : expid, 'chem' : '','globdatadir': 'timeblocks-v2', project : ''}
#
#   historical damip
    elif expid=='N1850aeroxidonly_f19_tn14_20190805'    : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850aeroxidonly_f19_tn14_20190815'    : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
#    elif expid=='N1850aeroxidonly_f19_tn14_20190805ext' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': '', project : ''}
    elif expid=='N1850aeroxidonly_02_f19_tn14_20190909' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850aeroxidonly_03_f19_tn14_20190913' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850ghgonly_f19_tn14_20190712'        : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850ghgonly_02_f19_tn14_20190909'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850ghgonly_03_f19_tn14_20190913'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850natonly_f19_tn14_20190805'        : des={'year0' : 1850, 'year1' : 1949, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850natonly_f19_tn14_20190815'        : des={'year0' : 1950, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
#   elif expid=='N1850natonly_f19_tn14_20190805ext'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : '',             'cexpid' : expid, 'chem' : '', 'globdatadir': '', project : ''} 
    elif expid=='N1850natonly_02_f19_tn14_20190909'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}
    elif expid=='N1850natonly_03_f19_tn14_20190913'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir,        'cexpid' : expid, 'chem' : '', 'globdatadir': 'timeblocks-v2', project : ''}

#   historical aerchemmip
    elif expid=='NHISTpiaer_f19_tn14_20190721'     : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NHISTpiaer_02_f19_tn14_20190909'  : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NHISTpiaer_03_f19_tn14_20190909'  : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NHISTpintcf_f19_tn14_20190720'    : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NHISTpintcf_02_f19_tn14_20190909' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NHISTpintcf_03_f19_tn14_20190909' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}    
#
# CMIP6 - cpl on BETZY
#   piControl on betzy [2x2]
    elif expid=='N1850_f19_tn14_20210317b'         : des={'year0' : 1600, 'year1' : 1899, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', project : ''} # Dirk 
    elif expid=='N1850_f19_tn14_20210409b'         : des={'year0' : 1611, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', project : ''} # Dirk 
    elif expid=='N1850_f19_tn14_20210409c'         : des={'year0' : 1621, 'year1' : 1900, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', project : ''} # Dirk 
#   piControl on betzy [1x1]
    elif expid=='N1850_f09_tn14_keyClim20201217'   : des={'year0' : 1200, 'year1' : 1229, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', project : ''} # Oyvind
    elif expid=='N1850frc2_betzy_v1'               : des={'year0' : 1200, 'year1' : 1238, 'model' : 'NorESM2', 'subdir' : basedirns9560k+'/../../users/heig/NorESM/archive', 'cexpid' : expid, 'chem' : '', project : ''} # Heiko
#   historical on betzy [1x1]
    elif expid=='NHIST_f09_tn14_20201218'          : des={'year0' : 1850, 'year1' : 1879, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', project : ''} # Oyvind

# CMIP6 SP-aeroosl
#   piClim-spAer-aer
#   elif expid=='piClim-SpAer2014'                          : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''} # Alf (on vilje)
#   elif expid=='NF1850norbc_spAer_aer2014_f19_20210523'    : des={'year0' :    1, 'year1' :   90, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''} # Dirk (on betzy)
#   piClim-spAer-anthro
#   elif expid=='piClim-SpAer-anthro'                       : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''} # Alf (on vilje)
#   elif expid=='NF1850norbc_spAer_anthro2014_f19_20210523' : des={'year0' :    1, 'year1' :   90, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''} # Dirk (on betzy)  
#   piClim-spAer-histaer
#   elif expid=='NFHISTnorpibc_spAer_aeronly_f19_20210523'  : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''} # Dirk (on betzy)
#   historical    
    elif expid=='NHIST_spAer_f19_tn14_20190925'             : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # Alf (on fram)
    elif expid=='NHIST_spAer_f19_tn14_20210523'             : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # Dirk (on Betzy)
    elif expid=='NF1850norbc_f19_20190727'              : des={'year0':1,'year1':170,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NF1850norbc_f19_20190727len30'         : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : 'NF1850norbc_f19_20190727', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_aer2014_f19_20190727'      : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='piClim-SpAer2014'                     : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='piClim-SpAer-anthro'                  : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_20191025'             : des={'year0':1,'year1':200,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='NF1850norbc_f19_20191025len30'        : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : 'NF1850norbc_f19_20191025' , 'chem' : '', project : ''}
    elif expid=='NF1850norbc_aer2014_f19_20191025'     : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   spAer
    elif expid=='NF1850norbc_spAer_aer2014_f19_20210523'    : des={'year0':1,'year1': 90,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_spAer_anthro2014_f19_20210523' : des={'year0':1,'year1': 90,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}    
#         (correct Gahn diagnostics)
    elif expid=='NF1850norbc_spAer_aer2014_f19_20230127'       : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : scratchdir,     'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_spAer_anthro2014_f19_20230127'    : des={'year0':1,'year1': 30,'model':'NorESM2','subdir' : scratchdir,     'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# CMIP6 - fsst - f09
    elif expid=='NF1850frc2norbc_f09_20200108'             : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_4xco2_f09_20200108'       : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}   
    elif expid=='NF1850frc2norbc_aeroxid2014_f09_20200108' : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}   
    elif expid=='NF1850frc2norbc_aer2014_f09_20200108'     : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}   
    elif expid=='NF1850frc2norbc_oxid2014_f09_20200108'    : des={'year0':1,'year1':30,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}   
#
#   spAer
    elif expid=='NFHISTnorpibc_spAer_aeronly_f19_20210523' :  des={'year0':1850,'year1':2014,'model':'NorESM2','subdir' : basedirns9560k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
# AEROCOM2019 : Alf
    elif  expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20191101'          : des={'year0':2005,'year1':2013,'model':'NorESM2','subdir' : basedir, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif  expid=='NFHISTnorpddmsbcsdyn_u3p41_f09_mg17_20200915'    : des={'year0' : 2005, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedir, 'cexpid' : expid, 'chem' : '', project : ''} 
# AEROCOM2019 for Maria Sand (run on Betzy) : initial setup -> results quite DIFFERENT from Alf's orginal simulation (which was on vilje)
    elif  expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20210415'          : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nodst_f09_mg17_20210415'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nobc_f09_mg17_20210415'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_noom_f09_mg17_20210415'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nopom_f09_mg17_20210415'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nosoa_f09_mg17_20210415'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
# AEROCOM2019 for Maria Sand (run on Betzy) : used Alf's repository -> results more SIMILAR to Alf's original simulation (which was on vilje)
    elif  expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20210420'          : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nodst_f09_mg17_20210420'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nobc_f09_mg17_20210420'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_noom_f09_mg17_20210420'     : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nopom_f09_mg17_20210420'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
    elif  expid=='NFHISTnorpddmsbcsdyn_nosoa_f09_mg17_20210420'    : des={'year0' : 2005, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kaerocom, 'cexpid' : expid, 'chem' : '', project : ''} 
#
# Maria Sand
    elif expid=='NF_2016_AMAP_type0' : des={'year0' : 2016, 'year1' : 2016, 'model' : 'NorESM1', 'subdir' : '/scratch/olivie/backup', 'cexpid' : expid, 'chem' : '', project : ''}
#
# BETZY fSST
    elif expid=='NF1850norbc_f19_20201226'                : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345k , 'cexpid' : expid, 'chem' : '', project : ''}

# OZONE Dirk
    elif expid=='FC2010climo_f19_20210204_test1'                : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls , 'cexpid' : expid, 'chem' : 'fullchem', project : ''}



    elif expid=='FC2010climo_prep_f19_20210204_test5'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test6'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} 
    elif expid=='FC2010climo_prep_f19_20210204_test7'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test9'           : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test10'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test11'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test12'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test13'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test14'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FC2010climo_prep_f19_20210204_test17'          : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}

    elif expid=='NF1850norbc_tropstratchem_f19_20210331_test14' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test01' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test02' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test03' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test04' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test05' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test06' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test08' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test09' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test10' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test11' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20210517_test12' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
#
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test01' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test06' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test07' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test08' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test09' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test10' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test11' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test12' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test13' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test14' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test15' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test16' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test17' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test18' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test19' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test20' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF2010norpddmsbc_tropstratchem_f19_20210517_test21' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
#
#   N1850 f09/f19
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test03' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # no DMS emissions
    elif expid=='N1850_tropstratchem_prep_f09_nt14_20211217_test04' : des={'year0' : 1, 'year1' : 25, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # no DMS emissions
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test05' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test06' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test07' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='N1850_tropstratchem_prep_f19_nt14_20211217_test08' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}

    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test01' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test02' : des={'year0' : 1, 'year1' : 60, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test03' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test04' : des={'year0' : 1, 'year1' :100, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20220223_test06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test09' : des={'year0' : 1, 'year1' :100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test11' : des={'year0' : 1, 'year1' :60,  'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12' : des={'year0' : 1, 'year1' :120,  'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14' : des={'year0' : 1, 'year1' :160,  'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#
#   NHIST f09
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01' : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01_from1880' : des={'year0' : 1880, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : 'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test01', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02'          : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02_from1860' : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : 'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02' , 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03'          : des={'year0' : 1850, 'year1' : 2014,  'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#
#   NSSPP585 f09 
    elif expid=='NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01'        : des={'year0' : 2015, 'year1' : 2100,  'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}

#   NFHIST fullchemistry    
#   [2x2]   
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test01' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test06' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test07' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test12' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test19' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test20' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test21' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test22' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test24' : des={'year0' : 1990, 'year1' : 1994, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test25' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#   [1x1]
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test12' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test13' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test15' : des={'year0' : 1970, 'year1' : 1971, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16' : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
 
#   NF1850norbc_fullchemistry
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test01' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f09_20220105_test02' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test03' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test06' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test09' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_20220105_test10' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
#   FCHIST startign 1850-...
#   noresm repository
    elif expid=='FCHIST_f19_20220111_test1'           : des={'year0' : 1850, 'year1' : 1859, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FCHIST_f19_mg17_20220111_test1'      : des={'year0' : 1850, 'year1' : 1889, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FCHIST_f09_mg17_20220111_test2'      : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FCHIST_f19_mg17_20220111_test3'      : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # without cam/src/NorESM
    elif expid=='FCHIST_f09_mg17_20220111_test4'      : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # without cam/src/NorESM
    elif expid=='FCHIST_f19_mg17_20220111_test5'      : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # scaled lightning production to same as f09
    elif expid=='FCHIST_f19_mg17_20220111_test6'      : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FCHIST_f09_mg17_20220111_test7'      : des={'year0' : 1970, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
 
#   cesm2.1.3
    elif expid=='FCHIST_f09_f09_mg17_20211217_test01' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # CESM2.1.3 
    elif expid=='FCHIST_f19_f19_mg17_20211217_test02' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # CESM2.1.3 
    elif expid=='FCHIST_f19_f19_mg17_20211217_test03' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''} # CESM2.1.3, but (DCS=500.D-6, gamma=0.308, seasalt-scaling=1.0 back to old unscaled 1x1 values)
#   cesm2.1.0
    elif expid=='FCHIST_f09_f09_mg17_20220202_test01' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}
    elif expid=='FCHIST_f19_f19_mg17_20220202_test02' : des={'year0' : 1850, 'year1' : 1869, 'model' : 'NorESM2', 'subdir' : basedirns2345kozone, 'cexpid' : expid, 'chem' : 'fullchem', project : ''}

# VSLS Dirk
    elif expid=='NF1850norbc_prep_f19_20210204_test5'     : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, project : ''}
    elif expid=='NF1850norbc_prep_f19_20210204_test8'     : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, project : ''}
    elif expid=='N1850frc2_bromo_f19_tn14_20210323_test3' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, project : ''}     
    elif expid=='N1850frc2_bromo_f19_tn14_20210323_test4' : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, project : ''}     
    elif expid=='N1850frc2_bromo_f19_tn14_20210323_test5' : des={'year0' : 1, 'year1' :  5, 'model' : 'NorESM2', 'subdir' : basedirns2345kvsls, 'cexpid' : expid, project : ''}     
#   to have extra output for the bromoform runs
    elif expid=='NHISTfrc2_bromo_prep_f19_tn14_20230912_test05' : des={'year0' : 1990, 'year1' :  1990, 'model' : 'NorESM2', 'subdir' : basedirns9560kbromo, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_bromo_prep_f19_tn14_20230912_test06' : des={'year0' : 1990, 'year1' :  1990, 'model' : 'NorESM2', 'subdir' : basedirns9560kbromo, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} 
#   actual simulation (rerunning brom_08)
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1850'   : des={'year0' : 1850, 'year1' :  1869, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1870'   : des={'year0' : 1870, 'year1' :  1989, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1990'   : des={'year0' : 1990, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_f19_tn14_bromo_08_r1850ext': des={'year0' : 1850, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NSSP585frc2_f19_tn14_bromo_08_r2015' : des={'year0' : 2015, 'year1' :  2079, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NSSP585frc2_f19_tn14_bromo_08_r2080' : des={'year0' : 2080, 'year1' :  2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
# CAMS-VSLS-DMS
#   1st member
    elif expid=='NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01'   : des={'year0' : 1995, 'year1' :  2004, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   activate energy correction    
    elif expid=='NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim02'   : des={'year0' : 1995, 'year1' :  2004, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # energy correction active
    elif expid=='NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim03'   : des={'year0' : 1995, 'year1' :  2014, 'model' : 'NorESM2', 'subdir' : basedirns9560kcamsvsls, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # energy correction active
    elif expid=='NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03' : des={'year0' : 2015, 'year1' :  2023, 'model' : 'NorESM2', 'subdir' : basedirns9560kcamsvsls, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03' : des={'year0' : 1995, 'year1' :  2023, 'model' : 'NorESM2', 'subdir' : basedirns9560kcamsvsls, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   2nd member
    elif expid=='NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01' : des={'year0' : 1995, 'year1' :  2004, 'model' : 'NorESM2', 'subdir' : lakedirns2345kcamsvsls, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# VSLS Jerry
    elif expid=='N1850frc2_f19_tn14_bromo_02'             : des={'year0' :    1, 'year1' :   20, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''}     
    elif expid=='N1850frc2_f19_tn14_bromo_04'             : des={'year0' :    1, 'year1' :   20, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''}    
    elif expid=='N1850frc2_f19_tn14_bromo_07'             : des={'year0' :    1, 'year1' :  100, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''} 
    elif expid=='N1850frc2_f19_tn14_bromo_08'             : des={'year0' : 1600, 'year1' : 2149, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''} 
    elif expid=='NHISTfrc2_f19_tn14_bromo_08'             : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : lakedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''} 
#
# N2O coupling Dirk/Joran 
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20230318_test02' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850vsls_tropstratchem_prep_f19_nt14_20230318_test04' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2otest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# N2O land coupling Dirk
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test01' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test02' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test03' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test04' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test05' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test07' : des={'year0' : 1, 'year1' : 50, 'model' : 'NorESM2', 'subdir' : lakedirns2345kn2olandtest, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}
#
# CH4 coupling
    elif expid=='N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02' : des={'year0' : 1, 'year1' : 10, 'model' : 'NorESM2', 'subdir' : basedirns9560kch4test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem',  'globdatadir' : 'timeblocks-v2', project : ''}    
#
#   with CESM2.1.3
    elif expid=='FHIST_f19_f19_mg17_20211015'           : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='FHIST_SO2ANTEUR_f19_f19_mg17_20211015' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''}
    elif expid=='FHIST_SO2ANTNAM_f19_f19_mg17_20211015' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k    , 'cexpid' : expid, 'chem' : '', project : ''}
#
# EMISSIONS mip
#   phase a
    elif expid=='NFHISTnorpddmsbcsdyn_base_f09_mg17_20210226'         : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_bc_no_season_f09_mg17_20210226' : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_high_so4_f09_mg17_20210226'     : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_no_so4_f09_mg17_20210226'       : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_so2_at_height_f09_mg17_20210226': des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_so2_no_season_f09_mg17_20210226': des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFHISTnorpddmsbcsdyn_standard_f09_mg17_20210226'     : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   phase b
    elif expid=='NFHISTnorpddmsbcsdyn_high_so4_so2_at_height_f09_mg17_20220824'     : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#    
    elif expid=='NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824'                    : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # using different SO2 anthro file
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_30red_f09_mg17_20220824'              : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_60red_f09_mg17_20220824'              : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_atlanticshift_f09_mg17_20220824'      : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_ship_indianshift_f09_mg17_20220824'        : des={'year0' : 2001, 'year1' : 2005, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
#
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_base_f09_mg17_20220824'               : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_ship_60red_f09_mg17_20220824'         : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_ship_atlanticshift_f09_mg17_20220824' : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_f2_1950_ship_indianshift_f09_mg17_20220824'   : des={'year0' : 2001, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kemissionmip    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
#   
# MMPPE-cloud 
    elif expid=='NFHISTnorpddmsbcsdyn_f09_mg17_20220928'         : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_dmsx0.5_f09_mg17_20220928' : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_dmsx2_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_z0.80_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_z1.79_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_z2.00_f09_mg17_20220928'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_lwp2.1_f09_mg17_20220928'  : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_lwp3.3_f09_mg17_20220928'  : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_enechk_f09_mg17_20220928'  : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : basedirns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_actd3_f09_mg17_20221005'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : oyvindsns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_actx3_f09_mg17_20221005'   : des={'year0' : 2009, 'year1' : 2010, 'model' : 'NorESM2', 'subdir' : oyvindsns2345kmmppecloud    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
# TOAR (Fiona and Bill)
    elif expid=='NF1850norbc_tropstratchem_f19_20230515_test01'     : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_toar_20230605_sim01' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_tropstratchem_f19_toar_20230605_sim05' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#   new simulations (corrected heterogenous freezing and koagsub)
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''} 
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#   prescribing the ozone climatologies
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01'     : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01'     : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}


#   perturbation simulation with CHBR3 boundary condition (for KeyCLIM)
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_chbr3x0.0_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_chbr3x2.0_fxemiyear_20240315_sim01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : lakedirns2345ktoarmip,      'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# ESM2025 - WP1
#   aerosol-only
    elif expid=='NF1850norbc_f19_20240312_test01'          : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_aer2014_f19_20240312_test01'  : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_so22014_f19_20240312_test01'  : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   full-chemistry
    elif expid == 'NF1850norbc_tropstratchem_f19_20240312_test01'         : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid == 'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid == 'NF1850norbc_tropstratchem_so22014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}

    elif expid == 'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01' : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns2345kesm2025ozone, 'cexpid' : expid, 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# OYVIND NOSA CONFERENCE
    elif expid=='NFHISTnorpddmsbcsdyn_std_f09_f09_mg17_080323'     : des={'year0' : 2009, 'year1' : 2012, 'model' : 'NorESM2', 'subdir' : basedirns9560koyvind    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_conv1_f09_f09_mg17_080323'   : des={'year0' : 2009, 'year1' : 2012, 'model' : 'NorESM2', 'subdir' : basedirns9560koyvind    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_convbc0_f09_f09_mg17_080323' : des={'year0' : 2009, 'year1' : 2012, 'model' : 'NorESM2', 'subdir' : basedirns9560koyvind    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_convmix_f09_f09_mg17_080323' : des={'year0' : 2009, 'year1' : 2012, 'model' : 'NorESM2', 'subdir' : basedirns9560koyvind    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
    elif expid=='NFHISTnorpddmsbcsdyn_newact_f09_f09_mg17_080323'  : des={'year0' : 2009, 'year1' : 2012, 'model' : 'NorESM2', 'subdir' : basedirns9560koyvind    , 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} # (id.)
#
# NORESM2.2
    elif expid=='NF1850norbc_f19_f19_20210530'              : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, project : ''} # noresm 2               (Oyvind)
    elif expid=='NF1850norbc_f19_f19_20210923'              : des={'year0' : 1, 'year1' : 40, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, project : ''} # noresm 2.2 with flux=0 (Oyvind)
    elif expid=='NF1850norbc_f19_f19_20211013'              : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, project : ''} # noresm 2.2 with flux=1 (Oyvind)
    elif expid=='NF1850norbc_f19_20211113_test17'           : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, project : ''} # noresm 2.2 with flux=1 and clubb 2.1.3 (Dirk)
    elif expid=='F2000climo_f09_ver2.1.3_20211005'          : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, project : ''} # cesm 2.1.3             (Oyvind)
    elif expid=='F2000climo_f09_ver2.2_20211005'            : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns9560k        , 'cexpid' : expid, project : ''} # cesm 2                 (Oyvind)
    elif expid=='F2000climo_f09_20211109_cesm2.2_test04'    : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir' : basedirns2345knoresm22, 'cexpid' : expid, project : ''} # cesm 2 with clubb 2.1.3 (Dirk)
# KEYCLIM - WP6
    elif expid=='NHISTpiaeroxid_f09_tn14_keyClim20201217'   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NSSP370piaeroxid_f09_tn14_keyClim20210210' : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NSSP585piaeroxid_f09_tn14_keyClim_20230705': des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_historical_Eddy_KeyCLim'         : des={'year0' : 1850, 'year1' : 1899, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2_histeddy2_KeyCLim'               : des={'year0' : 1900, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NSSP585frc2_Eddy_KeyCLIM'                  : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NHISTfrc2G_f09_tn14_gl4_SMB1_celo'         : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252kheiko, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}                
    elif expid=='NSSP585frc2G_f09_tn14_gl4_SMB1_celo'       : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252kheiko, 'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}          
    elif expid=='NHISTfrc2_f09_tn14_cloudxpice_220629'      : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}         
    elif expid=='NSSP585frc2_f09_tn14_cloudxpice_220819'    : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}       
    elif expid=='NHIST_hist_snow_KeyClim'                   : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}                          
    elif expid=='NSSP585_snow_KeyClim'                      : des={'year0' : 2015, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   combinations (historical + SSP)
    elif expid=='histssp585'           : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp370-piAerOxid' : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp585-piAerOxid' : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp585-eddy'      : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp585-iceSheet3' : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp585-cloud2'    : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp585-ozone'     : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='histssp585-snow'      : des={'year0' : 1850, 'year1' : 2100, 'model' : 'NorESM2', 'subdir' : basedirns9252k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# KEYCLIM - ERF
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug03' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug04' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_f09_20231029_pesbug06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug01' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug02' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug03' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug04' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug05' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850frc2norbc_aer2014_f09_20231029_pesbug06' : des={'year0' : 1, 'year1' : 30, 'model' : 'NorESM2', 'subdir' : basedirns9560kkeyclimerf,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# FORCeS - Øyvind
    elif expid=='NHIST_f19_tn14_Forces_230515' : des={'year0' : 1850, 'year1' : 2014, 'model' : 'NorESM2', 'subdir' : basedirns2345koyvind,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# JERRY - CO2 emission driven
    elif expid=='N1850_f19_tn14_20190730esm'                     : des={'year0' : 1751, 'year1' : 2200, 'model' : 'NorESM2', 'subdir' : basedirns2345k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027' : des={'year0' : 1851, 'year1' : 4101, 'model' : 'NorESM2', 'subdir' : basedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
# NorESM2.1 tests by dirk
    elif expid=='N1850_f19_tn14_20231204_test02'              : des={'year0' : 1600, 'year1' : 1749, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test03'              : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test04'              : des={'year0' : 1600, 'year1' : 1739, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test05'              : des={'year0' : 1600, 'year1' : 1719, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test06'              : des={'year0' : 1600, 'year1' : 1659, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test07'              : des={'year0' : 1600, 'year1' : 1659, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test08'              : des={'year0' : 1600, 'year1' : 1619, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test11'              : des={'year0' : 1600, 'year1' : 1692, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_f19_tn14_20231204_test12'              : des={'year0' : 1600, 'year1' : 1709, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test01'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test02'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test03'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test04'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test05'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test06'         : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test07'         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test08'         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_f19_f19_20231204_test09'         : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF1850norbc_aer2014_f19_f19_20231204_test01' : des={'year0' :    1, 'year1' :   30, 'model' : 'NorESM2', 'subdir' : lakedirns9560k,      'cexpid' : expid, 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
# NorESM2.3 tests by Dirk
    elif expid=='N1850_tropstratchem_f19_tn14_20240319_test08' : des={'year0' : 1, 'year1' : 20, 'model' : 'NorESM2', 'subdir'    : lakedirns2345knoresm23test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='N1850_tropstratchem_f19_tn14_20240319_test10' : des={'year0' : 1, 'year1' :  4, 'model' : 'NorESM2', 'subdir'    : lakedirns2345knoresm23test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : 'fullchem', 'globdatadir' : 'timeblocks-v2', project : ''}
# NorESM2.5 Mariana
    elif expid=='NF2000oslo.f19_f19_mtn14.2'                : des={'year0' :    1, 'year1' :    5, 'model' : 'NorESM2', 'subdir' : basedirns9560krefactor, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=='NF2000oslo.f19_f19_mtn14.3'                : des={'year0' :    1, 'year1' :    5, 'model' : 'NorESM2', 'subdir' : basedirns9560krefactor, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#   summer 204
    elif expid=="n1850.ne30_tn14.isopycnic.20240801"        : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=="n1850.ne30_tn14.hybrid.20240801"           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=="n1850.ne30_tn14.hybrid_coare.20240801"     : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''} 
    elif expid=="n1850.ne30_tn14.hybrid.20240808"           : des={'year0' :    1, 'year1' :   55, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=="n1850.ne30_tn14.hybrid.20240821"           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
    elif expid=="n1850.ne30_tn14.hybrid.20240822"           : des={'year0' :    1, 'year1' :   10, 'model' : 'NorESM2.5', 'subdir' : lakedirns9560knoresm3, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}
#
#   cesm
    elif expid=="n1850mam4.ne30_tn14.hybrid.clmbgc.20240826"         : des={'year0' :    1, 'year1' :    2, 'model' : 'CESM2.5', 'subdir' : lakedirns2345knoresm25test, 'cexpid' : expid, 'clmh0' : 'monthly', 'chem' : '', 'globdatadir' : 'timeblocks-v2', project : ''}

#   TOAR [2023-2024] other models :
    elif expid=='DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn' : des={'year0' : 2012, 'year1' : 2016, 'model' : 'DLR-EMAC','subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized', project : ''}
    elif expid=='GFDL-ESM4_pdClim-control_r1i1p1f1_gr'         : des={'year0' :    1, 'year1' :   70, 'model' : 'GFDL',    'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized', project : ''} 
    elif expid=='NorESM2-LM_pdClim-control_r1i1p1f1_gn'        : des={'year0' :    1, 'year1' :   40, 'model' : 'NorESM2', 'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized', project : ''}
    elif expid=='UKESM1-0-LL_pdClim-control_r1i1p1f2_gn'       : des={'year0' : 2000, 'year1' : 2069, 'model' : 'UKESM',   'subdir' : esgfdir, 'cexpid' : expid, 'clmh0' : '', 'chem' : '', 'globdatadir': 'timeblocks-cmip6-v5', 'project' : 'toar', 'dataformat' : 'cmorized', project : ''}
#
    else : 
        print('+++ experimentdefinition.py ---')
        print('No expid recognized = '+'...'+str(expid)+'...')
        quit()
    #
    print('YEAR0 : '+str(des['year0']))
    print('YEAR1 : '+str(des['year1']))
    print('SUBDIR : '+str(des['subdir']))
    print('CEXPID : '+str(des['cexpid']))
    #
    return des
