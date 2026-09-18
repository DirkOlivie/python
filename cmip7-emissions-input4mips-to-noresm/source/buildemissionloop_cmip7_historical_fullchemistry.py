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
# 2026-08-20 
    version='version20260820' ; vertintplist=['native'] ; noresmversionlist=['noresm3'] ; periodlist=['1850-1850'] ; resolutionlist=['1.9x2.5'] ; scenariolist=['CMIP']
#   periodlist=['1849-2023']   

    project='cmip7'
#
    overwrite=False
#   overwrite=True

    groupdescriptionlist=[ \
                              { 'activity' : 'bb'                    , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']                        , 'i4mpdownload':'DRES-CMIP-BB4CMIP7-2-0'}, \
                              { 'activity' : 'bbsurf'                , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['NO','CO','NH3','H2']+bbvocspecieslist, 'i4mpdownload':'DRES-CMIP-BB4CMIP7-2-0'}, \
                              { 'activity' : 'anthrosurf'            , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']                        , 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'anthrosurfgas'         , 'vertdist':'surface-to-surface' , 'sectorliststring': 'ALL', 'specieslist':['NO','CO','NH3']+anthrovocspecieslist , 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'anthroprof'            , 'vertdist':'surface-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC']                        , 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'air'                   , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S','BC','OC','NO2','CO']             , 'i4mpdownload':'CEDS-CMIP-2025-04-18'  }, \
                              { 'activity' : 'volc'                  , 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']                                  , 'i4mpdownload':'AeroCom2006'           }, \
                              { 'activity' : 'volcstratclim1850-2021', 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']                                  , 'i4mpdownload':'UOEXETER-CMIP-2-2-1'   },  \
                              { 'activity' : 'volcstratclim1750-2023', 'vertdist':'profile-to-profile' , 'sectorliststring': 'ALL', 'specieslist':['S']                                  , 'i4mpdownload':'UOEXETER-CMIP-2-2-1'   }  \
                         ]


    buildemissionloop2.buildemissionloop2(groupdescriptionlist=groupdescriptionlist, resolutionlist=resolutionlist, vertintplist=vertintplist, periodlist=periodlist,version=version, noresmversionlist=noresmversionlist, scenariolist=scenariolist, project=project, filelocation=filelocation, overwrite=overwrite)

if __name__ == '__main__':
    main()
