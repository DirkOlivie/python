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
# 2025-06-20
# version='version20250620' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; periodlist=['2023-2023'] ; resolutionlist=['0.9x1.25'] ; activitylist=['anthrosurf','anthroprof','bb','air','volc'] ; i4mpdownload_anthro='CEDS-CMIP-2025-04-18' ; i4mpdownload_bb='DRES-CMIP-BB4CMIP7-2-0' ; scenariolist=['hist']
# 2026-01-05
#   version='version20260105' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; periodlist=['1849-2025'] ; resolutionlist=['0.9x1.25','ne30pg3','ne16pg3'] ; activitylist=['anthrosurf','anthroprof','bb','air','volc'] ; scenariolist=['hist']
#
# 2026-02-06 : trying with BC, OC, S
#   version='version20260206' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; periodlist=['1849-2025'] ; resolutionlist=['0.9x1.25','ne30pg3','ne16pg3'] ; activitylist=['anthrosurf','anthroprof','bb','air','volc'] ; scenariolist=['hist']
# 2026-10-07 : ALL -> SINGLE 
    version='version20261007' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; periodlist=['1849-2023'] ; resolutionlist=['ne16pg3'] ; activitylist=['anthrosurf','anthroprof','bb','air','volc']
#   version='version20260723'

    project='cmip7'
#
    overwrite=False
#   overwrite=True
#
    bb_desc        = []
    anthro_desc    = []
    volc_desc      = []

    bb_desc.append(       {'descriptiontype':'contiguous','period':'1849-2023-annual','scenario':'CMIP','i4mpdownload':'DRES-CMIP-BB4CMIP7-2-0'})
    anthro_desc.append(   {'descriptiontype':'contiguous','period':'1849-2023-annual','scenario':'CMIP','i4mpdownload':'CEDS-CMIP-2025-04-18'  })
    volc_desc.append(     {'descriptiontype':'contiguous','period':'1849-2023-annual','scenario':'CMIP','i4mpdownload':'Aerocom2006'           })

#   generate the description
    bb_desc        = origindescriptionlist_generate.origindescriptionlist_generate(bb_desc)
    anthro_desc    = origindescriptionlist_generate.origindescriptionlist_generate(anthro_desc)
    volc_desc      = origindescriptionlist_generate.origindescriptionlist_generate(volc_desc)

    activitydescriptionlist=[ \
                              { 'activity' : 'bb'        , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : bb_desc}, \
                              { 'activity' : 'anthrosurf', 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : anthro_desc}, \
                              { 'activity' : 'anthroprof', 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : anthro_desc}, \
                              { 'activity' : 'air'       , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'origindescriptionlist' : anthro_desc}, \
                              { 'activity' : 'volc'      , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']          , 'origindescriptionlist' : volc_desc}  \
                         ]
#
    scenariohybrid='historical'
#
    buildemissionloop2.buildemissionloop2(activitydescriptionlist=activitydescriptionlist, resolutionlist=resolutionlist, vertintplist=vertintplist, periodlist=periodlist,version=version, noresmversionlist=noresmversionlist, scenariohybrid=scenariohybrid, project=project, filelocation=filelocation, overwrite=overwrite)
#
if __name__ == '__main__':
    main()
