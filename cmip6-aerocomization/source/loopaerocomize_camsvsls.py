import loopaerocomize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
#
version='v20240925'

#overwrite=True
overwrite=False

# monthly output
expidlist=['NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim03', \
           'NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03', \
           'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03']
expidlist=['NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03_2024_2025']

varlist  =['emichbr3','emidms']
filetype ='all-years-in-one-file'
freqfile ='monthly'

#loopaerocomize2.loopaerocomize2(expidlist=expidlist,varlist=varlist,version=version,filetype=filetype,freqfile=freqfile,overwrite=overwrite)

# daily output
#expidlist=['NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim03']
#           'NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03', \
#expidlist=['NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03']
expidlist=['NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03_2024_2025']

varlist  =['emichbr3','emidms','sfcWind']
filetype ='all-years-in-one-file'
freqfile ='daily'

loopaerocomize2.loopaerocomize2(expidlist=expidlist,varlist=varlist,version=version,filetype=filetype,freqfile=freqfile,overwrite=overwrite)
