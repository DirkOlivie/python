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
    version='version20261028' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; resolutionlist=['ne16pg3']

    periodlist=['2021-2105'] # still used
    project='cmip7'
#                       
    overwrite=False
#   overwrite=True
#
#    scenariolist=['h','hl','l','ln','m','l','vl']
    scenariolist=['h']

    for scenario in scenariolist :

        bb_desc        = []
        anthro_desc    = []
        air_desc       = []
        volc_desc      = []
        volcstrat_desc = []
#
#       --- YEAR 2021 : from historical ---
        year=2021
        bb_desc.append(       {'descriptiontype':'average','year':year,'origyearlist':[year+1],'scenariolist':['ScenarioMIP'],'i4mpdownloadlist':['IIASA-IAMC-'+scenario+'-1-1-1']})
        anthro_desc.append(   {'descriptiontype':'average','year':year,'origyearlist':[year+1],'scenariolist':['ScenarioMIP'],'i4mpdownloadlist':['IIASA-IAMC-'+scenario+'-1-1-1']})
        air_desc.append(      {'descriptiontype':'average','year':year,'origyearlist':[year+1],'scenariolist':['ScenarioMIP'],'i4mpdownloadlist':['IIASA-IAMC-'+scenario+'-1-1-2']}) # aircraft 1-1-2
        volc_desc.append(     {'descriptiontype':'average','year':year,'origyearlist':[year+1],'scenariolist':['ScenarioMIP'],'i4mpdownloadlist':['Aerocom2006'                  ]})


#       --- YEARS 2022-2023-2024-2025-20300-2035-...-2100 ---
        yearlist = [2022,2023,2024, \
                    2025,2030,2035,2040,2045,2050,2055,2060,2065,2070,2075,2080,2085,2090,2095,2100]        

        for year in yearlist :

            print('year : ', year)
            cyear=cyear=str("%4.4i"% year)
            period=cyear+'-'+cyear+'-annual'

            bb_desc.append(       {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'IIASA-IAMC-'+scenario+'-1-1-1'})
            anthro_desc.append(   {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'IIASA-IAMC-'+scenario+'-1-1-1'})    
            air_desc.append(      {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'IIASA-IAMC-'+scenario+'-1-1-2'}) # aircraft 1-1-2     
            volc_desc.append(     {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'Aerocom2006'                  })

#       --- YEAR 2105 ---
        yearlist = [2105]

        for year in yearlist :

            print('year : ', year)
            cyear=cyear=str("%4.4i"% year)
            period=cyear+'-'+cyear+'-annual'

            bb_desc.append(       {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'IIASA-IAMC-'+scenario+'-ext-1-1-1'})
            anthro_desc.append(   {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'IIASA-IAMC-'+scenario+'-ext-1-1-1'})
            air_desc.append(      {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'IIASA-IAMC-'+scenario+'-ext-1-1-2'}) # aircraft 1-1-2     
            volc_desc.append(     {'descriptiontype':'contiguous','period':period,'scenario':'ScenarioMIP','i4mpdownload':'Aerocom2006'                  })


#       generate the description
        bb_desc        = origindescriptionlist_generate.origindescriptionlist_generate(bb_desc)
        anthro_desc    = origindescriptionlist_generate.origindescriptionlist_generate(anthro_desc)    
        air_desc       = origindescriptionlist_generate.origindescriptionlist_generate(air_desc)        # aircraft 1-1-2
        volc_desc      = origindescriptionlist_generate.origindescriptionlist_generate(volc_desc)

#
        activitydescriptionlist=[ \
                                { 'activity' : 'bb'                    , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']    , 'origindescriptionlist' : bb_desc}, \
                                { 'activity' : 'anthrosurf'            , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']    , 'origindescriptionlist' : anthro_desc}, \
                                { 'activity' : 'anthroprof'            , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']    , 'origindescriptionlist' : anthro_desc}, \
                                { 'activity' : 'air'                   , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']    , 'origindescriptionlist' : air_desc}, \
                                { 'activity' : 'volc'                  , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']              , 'origindescriptionlist' : volc_desc} \
                                ]

        scenariohybrid='scenario-'+scenario

        buildemissionloop2.buildemissionloop2(activitydescriptionlist=activitydescriptionlist, resolutionlist=resolutionlist, vertintplist=vertintplist, periodlist=periodlist,version=version, noresmversionlist=noresmversionlist, scenariohybrid=scenariohybrid, project=project, filelocation=filelocation, overwrite=overwrite)
#
if __name__ == '__main__':
    main()
