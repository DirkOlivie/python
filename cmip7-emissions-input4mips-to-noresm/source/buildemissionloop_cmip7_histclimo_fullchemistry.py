import cfilelocation
import buildemissionloop2
import origindescriptionlist_generate


def main():
#---------------------------------
    '''
    CALLS
        buildemissionloop2

    REMARK : not needed as identical to grid in topo files [checked on 2026-01-07]
         grid_fv09=dir+'/cases/SOA_r610_PD/atm/hist/SOA_r610_PD.cam.h0.1979-01.nc'
         grid_fv19=dir+'/cases/Test149f19_f19/atm/hist/Test149f19_f19.cam.h0.0001-01.nc'

    '''
#
    print('+++ Starting : buildemissionloop +++')
#
    anthrovocspecieslist=['BENZENE','BIGALK','BIGENE'  ,'C2H2'   ,'C2H4'   , \
                          'C2H5OH' ,'C2H6'  ,'C3H6'    ,'C3H8'   ,'CH2O'   , \
                          'CH3CHO' ,'CH3CN' ,'CH3COCH3'          ,'CH3COOH', \
                          'CH3OH'                      , 'HCN'   ,'HCOOH'  , \
                                    'MEK'              ,'TOLUENE','XYLENES']
#
    bbvocspecieslist=['BENZENE','BIGALK','BIGENE'  ,'C2H2'    ,'C2H4'   , \
                      'C2H5OH' ,'C2H6'  ,'C3H6'    ,'C3H8'    ,'CH2O'   , \
                      'CH3CHO' ,'CH3CN' ,'CH3COCH3','CH3COCHO','CH3COOH', \
                      'CH3OH'  ,'DMS'   ,'GLYALD'  ,'HCN'     ,'HCOOH'  , \
                      'ISOP'   ,'MEK'   ,'MTERP'   ,'TOLUENE','XYLENES']



#   define auxiliary file locations    
    dir='/nird/datalake/NS2345K/olivie/emissions-auxiliary'
    weights_360x720_to_ne16pg3=dir+'/esmf/weights/WEIGHT_lat0.5xlon0.5_lon0minus179.75_lat0minus89.75_scrip_v20251011_TO_ne16pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc'
    weights_360x720_to_ne30pg3=dir+'/esmf/weights/WEIGHT_lat0.5xlon0.5_lon0minus179.75_lat0minus89.75_scrip_v20251011_TO_ne30pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc'
    weights_720x1440_to_ne16pg3=dir+'/esmf/weights/WEIGHT_lat0.25xlon0.25_lon0minus179.875_lat0plus89.875_scrip_v20251011_TO_ne16pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc'
    weights_720x1440_to_ne30pg3=dir+'/esmf/weights/WEIGHT_lat0.25xlon0.25_lon0minus179.875_lat0plus89.875_scrip_v20251011_TO_ne30pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc'
    topo_fv09=dir+'/inputdata/atm/cam/topo/fv_0.9x1.25_nc3000_Nsw042_Nrs008_Co060_Fi001_ZR_sgh30_24km_GRNL_c170103.nc'
    topo_fv19=dir+'/inputdata/atm/cam/topo/fv_1.9x2.5_nc3000_Nsw084_Nrs016_Co120_Fi001_ZR_061116.nc'
    topo_ne16pg3=dir+'/inputdata/atm/cam/topo/se/ne16pg3_gmted2010_modis_bedmachine_nc3000_Laplace0200_20230202.nc'
    topo_ne30pg3=dir+'/inputdata/atm/cam/topo/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_20240720.nc'
#
#   put the information in object
    filelocation=cfilelocation.CFileLocation( weights_360x720_to_ne16pg3  = weights_360x720_to_ne16pg3, \
                                              weights_360x720_to_ne30pg3  = weights_360x720_to_ne30pg3, \
                                              weights_720x1440_to_ne16pg3 = weights_720x1440_to_ne16pg3, \
                                              weights_720x1440_to_ne30pg3 = weights_720x1440_to_ne30pg3, \
# 
                                              topo_fv09    = topo_fv09, \
                                              topo_fv19    = topo_fv19, \
                                              topo_ne16pg3 = topo_ne16pg3, \
                                              topo_ne30pg3 = topo_ne30pg3)
# 2026-09-27
    version='version20260927' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; resolutionlist=['1.9x2.5']

    periodlist=['1850-2023'] # still used
    project='cmip7'
#                       
    overwrite=False
#   overwrite=True
#
    yearlist = [                              1850, 1860, 1870, 1880, 1890, \
                1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, \
                2000, 2010, 2020, 2023]

#   
    bb_desc        = []
    anthro_desc    = []
    volc_desc      = []
    volcstrat_desc = []

    for year in yearlist :

        print('year : ', year)


        if ( year == 2023 ) :
            origyearlist=[2021,2022,2023]    # averaging over 3 years
        else :
            origyearlist=list(range(year-2,year+2+1)) # averaging over 5 years

        print('origyearlist : ', origyearlist)

        


        nlen=len(origyearlist)

        bb_desc.append(       {'descriptiontype':'average','year':year,'origyearlist':origyearlist,'scenariolist':['CMIP']*nlen,'i4mpdownloadlist':['DRES-CMIP-BB4CMIP7-2-0']*nlen})
        anthro_desc.append(   {'descriptiontype':'average','year':year,'origyearlist':origyearlist,'scenariolist':['CMIP']*nlen,'i4mpdownloadlist':['CEDS-CMIP-2025-04-18'  ]*nlen})    
        volc_desc.append(     {'descriptiontype':'average','year':year,'origyearlist':origyearlist,'scenariolist':['CMIP']*nlen,'i4mpdownloadlist':['Aerocom2006'           ]*nlen})
        volcstrat_desc.append({'descriptiontype':'average','year':year,'origyearlist':origyearlist,'scenariolist':['CMIP']*nlen,'i4mpdownloadlist':['UOEXETER-CMIP-2-2-1'   ]*nlen})

#   generate the description
    bb_desc        = origindescriptionlist_generate.origindescriptionlist_generate(bb_desc)
    anthro_desc    = origindescriptionlist_generate.origindescriptionlist_generate(anthro_desc)    
    volc_desc      = origindescriptionlist_generate.origindescriptionlist_generate(volc_desc)
    volcstrat_desc = origindescriptionlist_generate.origindescriptionlist_generate(volcstrat_desc)







#    bb_origindescriptionlist    =[ {'year' : 2001, 'i4mpdownloadlist':['DRES-CMIP-BB4CMIP7-2-0'], 'scenariolist':['CMIP'], 'origyearlist' : [2001], 'origweightlist' : [1.]}, \
#                                   {'year' : 2002, 'i4mpdownloadlist':['DRES-CMIP-BB4CMIP7-2-0'], 'scenariolist':['CMIP'], 'origyearlist' : [2002], 'origweightlist' : [1.]}, \
#                                   {'year' : 2003, 'i4mpdownloadlist':['DRES-CMIP-BB4CMIP7-2-0'], 'scenariolist':['CMIP'], 'origyearlist' : [2003], 'origweightlist' : [1.]}  \
#                                 ]

#    anthro_origindescriptionlist=[ {'year' : 2001, 'i4mpdownloadlist':['CEDS-CMIP-2025-04-18'], 'scenariolist':['CMIP'], 'origyearlist' : [2001], 'origweightlist' : [1.]}, \
#                                   {'year' : 2002, 'i4mpdownloadlist':['CEDS-CMIP-2025-04-18'], 'scenariolist':['CMIP'], 'origyearlist' : [2002], 'origweightlist' : [1.]}, \
#                                   {'year' : 2003, 'i4mpdownloadlist':['CEDS-CMIP-2025-04-18'], 'scenariolist':['CMIP'], 'origyearlist' : [2003], 'origweightlist' : [1.]}  \
#                                 ]  

#    volc_origindescriptionlist  =[ {'year' : 2001, 'i4mpdownloadlist':['AeroCom2006'], 'scenariolist':['CMIP'], 'origyearlist' : [2001], 'origweightlist' : [1.]}, \
#                                   {'year' : 2002, 'i4mpdownloadlist':['AeroCom2006'], 'scenariolist':['CMIP'], 'origyearlist' : [2002], 'origweightlist' : [1.]}, \
#                                   {'year' : 2003, 'i4mpdownloadlist':['AeroCom2006'], 'scenariolist':['CMIP'], 'origyearlist' : [2003], 'origweightlist' : [1.]}  \
#                                 ]




##    scenario='IIASA-IAMC-vl'
#    anthro_origindescriptionlist=[ {'year' : 2095, 'i4mpdownloadlist':['IIASA-IAMC-vl-1-1-1']    , 'scenariolist':['ScenarioMIP'],  'origyearlist' : [2095], 'origweightlist' : [1.]}, \
#                                   {'year' : 2100, 'i4mpdownloadlist':['IIASA-IAMC-vl-1-1-1']    , 'scenariolist':['ScenarioMIP'],  'origyearlist' : [2100], 'origweightlist' : [1.]}, \
#                                   {'year' : 2105, 'i4mpdownloadlist':['IIASA-IAMC-vl-ext-1-1-1'], 'scenariolist':['ScenarioMIP'],  'origyearlist' : [2105], 'origweightlist' : [1.]}, \
#                                   {'year' : 2110, 'i4mpdownloadlist':['IIASA-IAMC-vl-ext-1-1-1'], 'scenariolist':['ScenarioMIP'],  'origyearlist' : [2110], 'origweightlist' : [1.]} \
#                                 ]
#    anthro_origindescriptionlist=origindescriptionlist_generate.origindescriptionlist_generate([ \
#                                                                                                 {'descriptiontype':'contiguous','period':'1990-1991-annual','scenario':'CMIP','i4mpdownload':'CEDS-CMIP-2025-04-18'}, \
#                                                                                                 {'descriptiontype':'contiguous','period':'2001-2003-annual','scenario':'CMIP','i4mpdownload':'CEDS-CMIP-2025-04-18'}]) 

#    anthro_origindescriptionlist=origindescriptionlist_generate.origindescriptionlist_generate([ \
#                                                                                                 {'descriptiontype':'average','year':2000,'origyearlist':[1998,1999,2000,2001,2002],'scenariolist':['CMIP']*5,'i4mpdownloadlist':['CEDS-CMIP-2025-04-18']*5}])
#

#
    activitydescriptionlist=[ \
                              { 'activity' : 'bb'                    , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']                        , 'origindescriptionlist' : bb_desc}, \
                              { 'activity' : 'bbsurf'                , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['NO','CO','NH3','H2']+bbvocspecieslist, 'origindescriptionlist' : bb_desc}, \
                              { 'activity' : 'anthrosurf'            , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']                        , 'origindescriptionlist' : anthro_desc} \
#                              { 'activity' : 'anthrosurfgas'         , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['NO','CO','NH3']+anthrovocspecieslist , 'origindescriptionlist' : anthro_desc}, \
#                              { 'activity' : 'anthroprof'            , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']                        , 'origindescriptionlist' : anthro_desc}, \
#                              { 'activity' : 'air'                   , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC','NO2','CO']             , 'origindescriptionlist' : anthro_desc}, \
#                              { 'activity' : 'volc'                  , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']                                  , 'origindescriptionlist' : volc_desc}, \
#                              { 'activity' : 'volcstratclim1850-2021', 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']                                  , 'origindescriptionlist' : volcstrat_desc}  \
                         ]


#    activitydescriptionlist=[ \
#                              { 'activity' : 'bb'        , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : bb_origindescriptionlist}, \
#                              { 'activity' : 'anthrosurf', 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : anthro_origindescriptionlist  } \
#                              { 'activity' : 'anthroprof', 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : anthro_origindescriptionlist  }, \
#                              { 'activity' : 'air'       , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : anthro_origindescriptionlist  }, \
#                              { 'activity' : 'volc'      , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']          , 'origindescriptionlist' : volc_origindescriptionlist }  \
#                         ]

#        scenariohybrid = str("%4.4i"% year)+'climo'
    scenariohybrid='histclimo'

    buildemissionloop2.buildemissionloop2(activitydescriptionlist=activitydescriptionlist, resolutionlist=resolutionlist, vertintplist=vertintplist, periodlist=periodlist,version=version, noresmversionlist=noresmversionlist, scenariohybrid=scenariohybrid, project=project, filelocation=filelocation, overwrite=overwrite)
#
if __name__ == '__main__':
    main()
