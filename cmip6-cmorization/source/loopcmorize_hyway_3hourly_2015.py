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
#expidlist=['NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521']
expidlist=['NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_3hr2015_20250521']
#
varlist=['airmass', \
         'c2h2','c2h4','c2h6','c3h6','c3h8','c6h6','ch3cho', 'ch3coch3', 'ch3cooh', 'ch3oh', 'ch4', 'co', \
         'h2', 'h2o', 'hcho', 'hcooh', 'hno3', \
         'isop', \
         'mtp', \
         'nh3', 'no2', 'no', \
         'o3', \
         'pan', \
         'pfull', \
         'zg', \
         'ps', \
         'pfull']
#
freqfilelist=['3hourly']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,freqfilelist=freqfilelist,version=version,filenameformat=filenameformat,prodlossunits=prodlossunits,overwrite=overwrite)
