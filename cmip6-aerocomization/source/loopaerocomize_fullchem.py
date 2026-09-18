import loopaerocomize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
#
version='v20240626'

#overwrite=True
overwrite=False

filetype='one-year-per-file'


expidlist=['NHIST_f19_tn14_20190710', \
           'NSSP585frc2_f19_tn14_20191014']
varlist  =['concbc','concoa','concso4','concss', \
           'vmro3','vmrso2', \
           'od550aer']
loopaerocomize2.loopaerocomize2(expidlist=expidlist,varlist=varlist,version=version,filetype=filetype,overwrite=overwrite)

# member 2+3 do not have od550aer
expidlist=['NHIST_02_f19_tn14_20190813','NHIST_03_f19_tn14_20190813', \
           'NHISTfrc2_f09_tn14_20191025', \
           'NSSP585frc2_f09_tn14_20191105']
varlist  =['concbc','concoa','concso4','concss', \
           'vmro3','vmrso2']
loopaerocomize2.loopaerocomize2(expidlist=expidlist,varlist=varlist,version=version,filetype=filetype,overwrite=overwrite)


expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
           'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01']
varlist=['concbc','concoa','concso4','concss', \
         'vmro3','vmrso2', \
         'vmrno','vmrno2','vmrco', \
         'od550aer']
loopaerocomize2.loopaerocomize2(expidlist=expidlist,varlist=varlist,version=version,filetype=filetype,overwrite=overwrite)

