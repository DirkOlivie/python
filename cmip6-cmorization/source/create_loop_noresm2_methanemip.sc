#! /bin/ksh
#
expidlist="NSSP245_tropstratchem_01_f19_tn14_s01_20241118 \
           NSSP245_tropstratchem_02_f19_tn14_s01_20241118 \
           NSSP245_tropstratchem_03_f19_tn14_s01_20241118 \
           NSSP245_tropstratchem_04_f19_tn14_s01_20241118 \
           NSSP245_tropstratchem_05_f19_tn14_s01_20241118 \
           NSSP245_tropstratchem_06_f19_tn14_s01_20241118 \
           \
           NSSP245TECH_tropstratchem_01_f19_tn14_s01_20241118 \
           NSSP245TECH_tropstratchem_02_f19_tn14_s01_20241118 \
           NSSP245TECH_tropstratchem_03_f19_tn14_s01_20241118 \
           NSSP245TECH_tropstratchem_04_f19_tn14_s01_20241118 \
           NSSP245TECH_tropstratchem_05_f19_tn14_s01_20241118 \
           NSSP245TECH_tropstratchem_06_f19_tn14_s01_20241118 \
           \
           NSSP245AMBI_tropstratchem_01_f19_tn14_s01_20241118 \
           NSSP245AMBI_tropstratchem_02_f19_tn14_s01_20241118 \
           NSSP245AMBI_tropstratchem_03_f19_tn14_s01_20241118 \
           NSSP245AMBI_tropstratchem_04_f19_tn14_s01_20241118 \
           NSSP245AMBI_tropstratchem_05_f19_tn14_s01_20241118 \
           NSSP245AMBI_tropstratchem_06_f19_tn14_s01_20241118"
#
varlist="tas ta ps o3 hus \
         o3surface siconc"
#
varlist="o3"
#varlist="oh"
#varlist="ho2"
#varlist="no3"

overwrite=False

version=v20250416
version=v20250821

listfile=ALL_noresm2_methanemip.parallel2

> ${listfile}

for var in ${varlist} ; do
    for expid in ${expidlist} ; do

        echo ${expid} ${var} ${overwrite}
        echo "python cmorize_wrapper.py ${expid} ${var} ${version} ${overwrite}" >> ${listfile}

    done
done
