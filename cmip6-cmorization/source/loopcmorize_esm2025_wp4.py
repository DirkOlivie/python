import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
version='v20250515'
overwrite=False
#overwrite=True
#
#expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506']
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506']
#
varlist=['drych4', \
         'ch4','oh','o1d','o3','isop','emico','emiisop','eminox', \
         'ch4losscl', 'ch4lossf', 'ch4lossoh', 'ch4losso1d', \
         'ptp',  \
         'clt','pr','prw','ps','psl','rlut','rsut','tas','ts','ua','va','wap','zg'] 
#varlist=['lossch4']
#
#varlist=['tas']
#varlist=['o3']
#varlist=['CDNUMC']
#varlist=['cdnc']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,version=version,overwrite=overwrite)
