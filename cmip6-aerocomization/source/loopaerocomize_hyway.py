import loopaerocomize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
#
version='v20250521'

#overwrite=True
overwrite=False

filetype='one-year-per-file'


expidlist=['NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_20250503']
varlist  =['vmro3']
freqfile = 'monthly'
loopaerocomize2.loopaerocomize2(expidlist=expidlist,varlist=varlist,version=version,filetype=filetype,freqfile=freqfile,overwrite=overwrite)
