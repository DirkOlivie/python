#! /bin/ksh
#
#
version=version20260105
vertintplist="native"
noresmversionlist="noresm3" 
periodlist="1849-2025" 
#resolutionlist="0.9x1.25"
resolutionlist="1.9x2.5 0.9x1.25 ne16pg3 ne30pg3"
activitylist="anthrosurf anthroprof bb air volc" 
i4mpdownload_anthro=CEDS-CMIP-2025-04-18
i4mpdownload_bb=DRES-CMIP-BB4CMIP7-2-0
scenariolist="hist"
overwrite=False
# overwrite=True
listfile=ALL_emissions_cmip7.parallel

dir=/nird/datalake/NS2345K/olivie/emissions-auxiliary
weights_360x720_to_ne16pg3=${dir}/esmf/weights/WEIGHT_lat0.5xlon0.5_lon0minus179.75_lat0minus89.75_scrip_v20251011_TO_ne16pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc
weights_360x720_to_ne30pg3=${dir}/esmf/weights/WEIGHT_lat0.5xlon0.5_lon0minus179.75_lat0minus89.75_scrip_v20251011_TO_ne30pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc
weights_720x1440_to_ne16pg3=${dir}/esmf/weights/WEIGHT_lat0.25xlon0.25_lon0minus179.875_lat0plus89.875_scrip_v20251011_TO_ne16pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc
weights_720x1440_to_ne30pg3=${dir}/esmf/weights/WEIGHT_lat0.25xlon0.25_lon0minus179.875_lat0plus89.875_scrip_v20251011_TO_ne30pg3_ESMFmesh_cdf5_c20211018_VERSION20251018.nc
topo_fv09=${dir}/inputdata/atm/cam/topo/fv_0.9x1.25_nc3000_Nsw042_Nrs008_Co060_Fi001_ZR_sgh30_24km_GRNL_c170103.nc
topo_fv19=${dir}/inputdata/atm/cam/topo/fv_1.9x2.5_nc3000_Nsw084_Nrs016_Co120_Fi001_ZR_061116.nc
topo_ne16pg3=${dir}/inputdata/atm/cam/topo/se/ne16pg3_gmted2010_modis_bedmachine_nc3000_Laplace0200_20230202.nc
topo_ne30pg3=${dir}/inputdata/atm/cam/topo/se/ne30pg3_gmted2010_modis_bedmachine_nc3000_Laplace0100_noleak_20240720.nc


> ${listfile}

for vertintp in ${vertintplist} ; do
for noresmversion in ${noresmversionlist} ; do
for period in ${periodlist} ; do
for resolution in ${resolutionlist} ; do 
for activity in ${activitylist} ; do
for scenario in ${scenariolist} ; do 

   case ${activity} 
   in
      bb)         vertdist=surface-to-profile ; sectorliststring=AGRI-BORF-DEFO-PEAT-SAVA-TEMF ; specieslist="SO2               BC_NI  OM_NI  SO4_PR" ;;
      anthrosurf) vertdist=surface-to-surface ; sectorliststring=AGR-TRA-DOM-SOL-WST-SHP       ; specieslist="SO2  BC_N  BC_AX         OM_NI  SO4_PR" ;;
      anthroprof) vertdist=surface-to-profile ; sectorliststring=ENE-IND                       ; specieslist="SO2  BC_N  BC_AX         OM_NI  SO4_PR" ;;
      air)        vertdist=profile-to-profile ; sectorliststring=ALL                           ; specieslist="SO2  BC_N  BC_AX         OM_NI  SO4_PR" ;;
      volc)       vertdist=profile-to-profile ; sectorliststring=CONT-EXPL                     ; specieslist="SO2                             SO4_PR" ;;
      *)
         echo "No activity recognized : ${activity}"
         exit() ;;
   esac

   for species in ${specieslist} ; do		

      echo "python buildemission_wrapper.py ${period} ${species} ${activity} ${sectorliststring} ${vertdist} ${resolution} ${vertintp} ${version} ${noresmversion} ${scenario} ${i4mpdownload_anthro} ${i4mpdownload_bb} ${overwrite} ${weights_360x720_to_ne16pg3} ${weights_360x720_to_ne30pg3} ${weights_720x1440_to_ne16pg3} ${weights_720x1440_to_ne30pg3} ${topo_fv09} ${topo_fv19} ${topo_ne16pg3} ${topo_ne30pg3}" >> ${listfile}

   done

done
done
done
done
done
done

