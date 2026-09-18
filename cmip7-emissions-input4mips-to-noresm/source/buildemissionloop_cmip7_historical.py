import cfilelocation
import buildemissionloop2


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
# 2026-02-09 : ALL -> SINGLE 
    version='version20260209' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; periodlist=['1849-2025'] ; resolutionlist=['0.9x1.25','ne30pg3','ne16pg3'] ; activitylist=['anthrosurf','anthroprof','bb','air','volc'] ; scenariolist=['CMIP']
#   version='version20260723'

#   periodlist=['1850-1850']#,'1849-2025']
#   periodlist=['1849-2023']
    periodlist=['1850-1850']
#    resolutionlist=['1.9x2.5','ne16pg3']#,'0.9x1.25','ne16pg3','ne30pg3']
    resolutionlist=['0.9x1.25'] 
#   resolutionlist=['ne16pg3']
#   resolutionlist=['ne30pg3']
    project='cmip7'
#
    overwrite=False
#   overwrite=True
#
#   do something for commonblock
#
#    groupdescriptionlist=[ \
#                              { 'activity' : 'bb'        , 'vertdist':'surface-to-profile' , 'sectorliststring':'AGRI-BORF-DEFO-PEAT-SAVA-TEMF', 'specieslist':['SO2','BC_NI','OM_NI','SO4_PR'       ], 'i4mpdownload':'DRES-CMIP-BB4CMIP7-2-0'}, \
#                              { 'activity' : 'anthrosurf', 'vertdist':'surface-to-surface' , 'sectorliststring':'AGR-TRA-DOM-SOL-WST-SHP'      , 'specieslist':['SO2','BC_N','BC_AX','OM_NI','SO4_PR'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
#                              { 'activity' : 'anthroprof', 'vertdist':'surface-to-profile' , 'sectorliststring':'ENE-IND'                      , 'specieslist':['SO2','BC_N','BC_AX','OM_NI','SO4_PR'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
#                              { 'activity' : 'air'       , 'vertdist':'profile-to-profile' , 'sectorliststring': 'SINGLE'                         , 'specieslist':['SO2','BC_N','BC_AX','OM_NI','SO4_PR'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
#                              { 'activity' : 'volc'      , 'vertdist':'profile-to-profile' , 'sectorliststring': 'CONT-EXPL'                   , 'specieslist':['SO2','SO4_PR']                       , 'i4mpdownload':'AeroCom2006'           }  \
#                         ] 

#    groupdescriptionlist=[ \
#                              { 'activity' : 'bb'        , 'vertdist':'surface-to-profile' , 'sectorliststring':'AGRI-BORF-DEFO-PEAT-SAVA-TEMF', 'specieslist':['S','BC','OC'], 'i4mpdownload':'DRES-CMIP-BB4CMIP7-2-0'}, \
#                              { 'activity' : 'anthrosurf', 'vertdist':'surface-to-surface' , 'sectorliststring':'AGR-TRA-DOM-SOL-WST-SHP'      , 'specieslist':['S','BC','OC'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
#                              { 'activity' : 'anthroprof', 'vertdist':'surface-to-profile' , 'sectorliststring':'ENE-IND'                      , 'specieslist':['S','BC','OC'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
#                              { 'activity' : 'air'       , 'vertdist':'profile-to-profile' , 'sectorliststring': 'SINGLE'                         , 'specieslist':['S','BC','OC'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
#                              { 'activity' : 'volc'      , 'vertdist':'profile-to-profile' , 'sectorliststring': 'CONT-EXPL'                   , 'specieslist':['S']          , 'i4mpdownload':'AeroCom2006'           }  \
#                         ]

    groupdescriptionlist=[ \
                              { 'activity' : 'bb'        , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'i4mpdownload':'DRES-CMIP-BB4CMIP7-2-0'}, \
                              { 'activity' : 'anthrosurf', 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'anthroprof', 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'air'       , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC'], 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'volc'      , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']          , 'i4mpdownload':'AeroCom2006'           }  \
                         ]


    buildemissionloop2.buildemissionloop2(groupdescriptionlist=groupdescriptionlist, resolutionlist=resolutionlist, vertintplist=vertintplist, periodlist=periodlist,version=version, noresmversionlist=noresmversionlist, scenariolist=scenariolist, project=project, filelocation=filelocation, overwrite=overwrite)



#    for activity in activitylist :

#     fill_commonblock

#        if (   activity == 'bb'         ) : vertdist='surface-to-profile' ; sectorliststring='AGRI-BORF-DEFO-PEAT-SAVA-TEMF' ; speciesliststring='SO2-BC_NI-OM_NI-SO4_PR'
#        elif ( activity == 'anthrosurf' ) : vertdist='surface-to-surface' ; sectorliststring='AGR-TRA-DOM-SOL-WST-SHP'       ; speciesliststring='SO2-BC_N-BC_AX-OM_NI-SO4_PR'
#        elif ( activity == 'anthroprof' ) : vertdist='surface-to-profile' ; sectorliststring='ENE-IND'                       ; speciesliststring='SO2-BC_N-BC_AX-OM_NI-SO4_PR'
#        elif ( activity == 'air'        ) : vertdist='profile-to-profile' ; sectorliststring='ALL'                           ; speciesliststring='SO2-BC_N-BC_AX-OM_NI-SO4_PR'
#        elif ( activity == 'volc'       ) : vertdist='profile-to-profile' ; sectorliststring='CONT-EXPL'                     ; speciesliststring='SO2-SO4_PR'
#        else : 
#            print('+++ buildemissionloop +++')
#            print('No activity recognized : ', activity) 
#            quit()
#    IF ALL SECTORS SHOULD BE SUMMED UP 
#    sectorlist=['ALL']

#        buildemissionloop2.buildemissionloop2(vertdist=vertdist, resolutionlist=resolutionlist, vertintplist=vertintplist, activity=activity, sectorliststring=sectorliststring,speciesliststring=speciesliststring,periodlist=periodlist,version=version, noresmversionlist=noresmversionlist, scenariolist=scenariolist, i4mpdownload_anthro=i4mpdownload_anthro, i4mpdownload_bb=i4mpdownload_bb, filelocation=filelocation, overwrite=overwrite)
#
if __name__ == '__main__':
    main()
