import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
version='v20251022'
overwrite=True
#
expidlist=['NHIST_f19_tn14_20190625ext','NHISTfrc2_f09_tn14_20191001ext']
#
varlist=['aodvisvolso4']
freqfilelist=['monthly']
filenameformat='cmor'
prodlossunits=''
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,freqfilelist=freqfilelist,version=version,filenameformat=filenameformat,prodlossunits=prodlossunits,overwrite=overwrite)
