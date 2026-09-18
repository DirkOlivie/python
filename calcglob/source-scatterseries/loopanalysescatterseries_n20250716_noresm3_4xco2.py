import loopanalysescatterseries2

# MAIN PROGRAM

description='varcommon'

# OBTAINING VOLCANIC EMISSION TOTAL
#----------------------------------
# [2x2 degree]
# x-axis : CMIP6 prescribed AOD from input4MIPs
expXlist=['nco2x4.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250710', \
          'nco2x4.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250710', \
          'nco2x4.ne30pg3_tn14.noresm3_0_beta01_650dcs_4p0clubbc8_0p5dust.20250715', \
          'NCO2x4_f19_tn14_20190624ext', \
          'NCO2x4_f19_tn14_20190624ext']           
refXlist=['n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext', \
          'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext', \
          'n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708ext', \
          'N1850_f19_tn14_20190621ext', \
          'N1850_f19_tn14_20190621ext']

expXyear0list=[ 51,121, 51,  1, 71] # expX
expXyear1list=[120,200,120, 70,500]
refXyear0list=[ 51,121, 51,1600,1670]
refXyear1list=[120,200,120,1669,2099]
seasonXlist=['YEA','YEA','YEA','YEA','YEA']
wXlist=[1.,-1.]
varXlist=['TREFHT']
typevarXlist=['glob']

# y-axis : full-chemistry
expYlist=expXlist           
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=refXyear0list
refYyear1list=refXyear1list
seasonYlist=seasonXlist
wYlist=[1.,-1.]
varYlist=['FSLNT']
typevarYlist=['glob']
# 
legendlist=['NorESM3.0 (2x2, yr 1-70)', \
            'NorESM3.0 (2x2, yr 71-150)', 
            'NorESM3.0 (1x1, yr 1-70)', \
            'CMIP6 (2x2, yr 1-70)', \
            'CMIP6 (2x2, yr 71-500)']  
#
colorlist=[0,1,2,3,4]
dolinearregressionlist=[1,0,1,1,0]
#
description='trial'
code='n20250716_noresm2.5_4xco2'

#
loopanalysescatterseries2.loopanalysescatterseries2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,dolinearregressionlist=dolinearregressionlist, \
        description=description,code=code)
