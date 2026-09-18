#! /bin/ksh
#
#
version=version20250620
vertintplist="native"
noresmversionlist="noresm3" 
periodlist="1995-2025" 
#resolutionlist="0.9x1.25"
resolutionlist="1.9x2.5"
activitylist="anthrosurf anthroprof bb air volc" 
i4mpdownload_anthro=CEDS-CMIP-2025-04-18
i4mpdownload_bb=DRES-CMIP-BB4CMIP7-2-0
scenariolist="hist"
overwrite=False
# overwrite=True
listfile=ALL_emissions_rachael.parallel


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

      echo "python buildemission_wrapper.py ${period} ${species} ${activity} ${sectorliststring} ${vertdist} ${resolution} ${vertintp} ${version} ${noresmversion} ${scenario} ${i4mpdownload_anthro} ${i4mpdownload_bb} ${overwrite}" >> ${listfile}

   done

done
done
done
done
done
done

