import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
#version='v20250416'
version='v20250821'
overwrite=False
#
expidlist=['NSSP245_tropstratchem_01_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_02_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_03_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_04_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_05_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_06_f19_tn14_s01_20241118', \
            \
           'NSSP245TECH_tropstratchem_01_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_02_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_03_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_04_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_05_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_06_f19_tn14_s01_20241118', \
            \
           'NSSP245AMBI_tropstratchem_01_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_02_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_03_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_04_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_05_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_06_f19_tn14_s01_20241118']
#
#expidlist=['NSSP245_tropstratchem_01_f19_tn14_s01_20241118']
#
varlist=['tas','ta','ps','o3','hus']
varlist=['o3surface']
varlist=['siconc']
varlist=['o3','oh','no3','ho2']
#varlist=['zg','pfull','phalf']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,version=version,overwrite=overwrite)
