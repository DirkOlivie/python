import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
version='v20250627'
overwrite=False
#overwrite=True
filenameformat='hyway'
prodlossunits='hyway'
#
# transient2010s
#expidlist=['NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521'] # transient2010s
# cntr2019 - ... 
expidlist=[\
# cntr2019
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_s01_hyway_20260403', \
# cntr2019 CH4+10%
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4x1p1_s01_hyway_20260403', \
# cntr2019 H2+100Tg/yr
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_h2plus100tg_s01_hyway_20260403', \
# cntr1850
           'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr1850_h2emi_h2dep0p75_s01_hyway_20260403']
#
varlist=[\
'airmass', \
'c2h2', \
'c2h4', \
'c2h6', \
'c3h6', \
'c3h8', \
'c6h6', \
'ch3cho', \
'ch3coch3', \
'ch3cooh', \
'ch3oh', \
'ch4', \
'co', \
'dms', \
'drych3oh', \
#'drych4', \
'dryco', \
'dryh2', \
'drych3coch3', \
'drych3cooh', \
'drych3oh', \
'dryhcooh', \
'dryhcho', \
'drymhp', \
'dryo3', \
'drypan', \
'emic2h2', \
'emic2h4', \
'emic2h6', \
'emic3h6', \
'emic3h8', \
'emic6h6', \
'emich3cho', \
'emich3coch3', \
'emich3cooh', \
'emich3oh', \
'emico', \
'emidms', \
'emih2', \
'emihcho', \
'emihcooh', \
'emiisop', \
'emimtp', \
'eminh3', \
'eminox', \
'emiso2', \
'emiso4', \
'h2', \
'h2o', \
'hcho', \
'hcooh', \
'hno3', \
'isop', \
#'lossch3cho', \
'lossch3coch3', \
'lossch3cooh', \
'lossch3oh', \
'lossch4', \
#'losschocho', \
'lossco', \
'lossh2', \
'lossh2o', \
'losshcho', \
'losshcooh', \
#'lossisop', \
'losspan', \
'mhp', \
'mmroa', \
'mmrso4', \
'mtp', \
'nh3', \
'no2', \
'no', \
'o3', \
'oh', \
'pan', \
#
'toluene', \
'pfull', \
'phalf', \
'prodch3coch3', \
'prodch3cooh', \
'prodch3oh', \
'prodco', \
'prodh2', \
'prodh2o', \
'prodhcho', \
'prodhcooh', \
'prodmhp', \
'prodpan', \
'ps', \
'rlutcs', \
'rlut', \
'rsds', \
'rsdt', \
'rsutcs', \
'rsut', \
'so2', \
'ta', \
'volume', \
'wetch3cho', \
'wetch3coch3', \
'wetch3oh', \
'wethcho', \
'wethcooh', \
'wetmhp', \
'wetnh3', \
'zg']
#
freqfilelist=['monthly']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,freqfilelist=freqfilelist,version=version,filenameformat=filenameformat,prodlossunits=prodlossunits,overwrite=overwrite)


varlist=['areacella','orog']
#
freqfilelist=['fixed']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,freqfilelist=freqfilelist,version=version,filenameformat=filenameformat,prodlossunits=prodlossunits,overwrite=overwrite)



