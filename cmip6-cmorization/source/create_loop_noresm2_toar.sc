#! /bin/ksh
#
expidlist="NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01 \
           NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01 \
           NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01 \
           \
           NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01 \
           NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01 \
           NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01"
#
varlist=" \
         cl cli clivi clt clw clwvi \
         evspsbl \
         hfls hfss \
         hur \
         hus huss \
         o3 \
         pr prc prsn prw \
         ps psl \
         rlds rlus rlut rlutcs \
         rsds rsdscs rsdt rsus rsuscs rsut rsutcs \
         rtmt \
         sfcWind \
         ta tas \
         tauu tauv \
         ts \
         ua \
         va \
         wap \
         zg \
         \
         abs550aer \
         airmass \
         bldep \
         chepsoa \
         co \
         cod \
         dms \
         drybc drydust dryoa dryso2 dryso4 dryss \
         emibc emibvoc emidms emidust emiisop emioa emiso2 emiso4 emiss \
         isop \
         lwp \
         mmraerh2o \
         mmrbc mmrdust mmroa mmrso4 mmrsoa mmrss \
         toz \
         n2o,no,no2,o3 \
         od440aer od550aer od550aerh2o od550bc od550csaer od550dust od550lt1aer od550oa od550so4 od550ss od870aer \
         oh \
         pfull phalf ps \
         rlutaf rlutcsaf rsutaf rsutcsaf \
         so2 \
         ua va \
         wetbc wetdust wetoa wetso2 wetso4 wetss \
         zg ztp"

# tropoz

overwrite=False

version=v20240617
version=v20241001 # correct units in 3D fields

listfile=ALL_noresm2_toar.parallel

> ${listfile}

for var in ${varlist} ; do
    for expid in ${expidlist} ; do

        echo ${expid} ${var} ${overwrite}
        echo "python cmorize_wrapper.py ${expid} ${var} ${version} ${overwrite}" >> ${listfile}

    done
done
