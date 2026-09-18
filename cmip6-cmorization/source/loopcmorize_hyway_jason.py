import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
version='v20241209'
overwrite=True
#
expidlist=['NHIST_tropstratchem_01_f19_tn14_r2000_s01_20241118']
#
varlist=['h2']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,version=version,overwrite=overwrite)
