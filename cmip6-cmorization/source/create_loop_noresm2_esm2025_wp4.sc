#! /bin/ksh
#
#expidlist="NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506 \
#           NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506"
expidlist="NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506"
#
varlist="drych4 \
         ch4 oh o1d o3 isop emico emiisop eminox \
         ch4losscl ch4lossf ch4lossoh ch4losso1d \
         ptp \
         clt pr prw ps psl rlut rsut tas ts ua va wap zg"
#
varlist="o3"

overwrite=False

version=v20250515

listfile=ALL_noresm2_esm2025_wp4.parallel

> ${listfile}

for var in ${varlist} ; do
    for expid in ${expidlist} ; do

        echo ${expid} ${var} ${overwrite}
        echo "python cmorize_wrapper.py ${expid} ${var} ${version} ${overwrite}" >> ${listfile}

    done
done
