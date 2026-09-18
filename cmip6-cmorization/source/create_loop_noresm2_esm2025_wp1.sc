#! /bin/ksh
#
expidlist="NF1850norbc_f19_20240312_test01 \
           NF1850norbc_aer2014_f19_20240312_test01 \
           NF1850norbc_so22014_f19_20240312_test01 \
           \
           NF1850norbc_tropstratchem_f19_20240312_test01 \
           NF1850norbc_tropstratchem_aer2014_f19_20240312_test01 \
           NF1850norbc_tropstratchem_so22014_f19_20240312_test01 \
           \
           NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01"
#
expidlist="NF1850norbc_f19_20240312_test01 \
           NF1850norbc_aer2014_f19_20240312_test01 \
           NF1850norbc_so22014_f19_20240312_test01"
#
varlist="pr tas \
         rlds rlus rlut rlutcs \
         rsds rsdscs rsdt rsus rsuscs rsut rsutcs \
         rlutaf rlutcsaf rsutaf rsutcsaf \
         od550aer \
         o3"
# CDNUMC cdnc"

overwrite=False

version=v20240614

listfile=ALL_noresm2_toar.parallel

> ${listfile}

for var in ${varlist} ; do
    for expid in ${expidlist} ; do

        echo ${expid} ${var} ${overwrite}
        echo "python cmorize_wrapper.py ${expid} ${var} ${version} ${overwrite}" >> ${listfile}

    done
done
