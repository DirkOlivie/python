import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
version='v20240704'
overwrite=False
#
expidlist=['NF1850norbc_f19_20240312_test01', \
           'NF1850norbc_aer2014_f19_20240312_test01', \
           'NF1850norbc_so22014_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_so22014_f19_20240312_test01']
#
expidlist=['NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01']
#
expidlist=['NF1850norbc_tropstratoxid_f19_20240312_test01', \
           'NF1850norbc_tropstratoxid_aer2014_f19_20240312_test01', \
           'NF1850norbc_tropstratoxid_so22014_f19_20240312_test01']
#
varlist=['pr','tas', \
         'rlds', 'rlus', 'rlut', 'rlutcs', \
         'rsds', 'rsdscs', 'rsdt', 'rsus', 'rsuscs', 'rsut', 'rsutcs', \
         'rlutaf', 'rlutcsaf', 'rsutaf', 'rsutcsaf', \
         'od550aer'] 
#
#varlist=['tas']
#varlist=['o3']
#varlist=['CDNUMC']
#varlist=['cdnc']
#
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,version=version,overwrite=overwrite)
