import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
version='v20251218'
#overwrite=False
overwrite=True
#
expidlist=['N1850vslsn2onh3_f19_tn14_test10']
#
varlist=['n2o']
freqfilelist=['monthly']
filenameformat='cmor'
prodlossunits=''
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,freqfilelist=freqfilelist,version=version,filenameformat=filenameformat,prodlossunits=prodlossunits,overwrite=overwrite)
