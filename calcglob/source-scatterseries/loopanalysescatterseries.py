import loopanalysescatterseries2

# MAIN PROGRAM

description='varcommon'

# OBTAINING VOLCANIC EMISSION TOTAL
#----------------------------------
# [2x2 degree]
# x-axis : CMIP6 prescribed AOD from input4MIPs
expXlist=['NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710', \
          'NHIST_f19_tn14_20190710']
refXlist=expXlist
expXyear0list=[1975,1975,1975,1975,1975,1975,1975,1975] # expX
expXyear1list=[2014,2014,2014,2014,2014,2014,2014,2014]
refXyear0list=[1975,1975,1975,1975,1975,1975,1975,1975] # refX
refXyear1list=[2014,2014,2014,2014,2014,2014,2014,2014]
seasonXlist=['monthly','monthly','monthly','monthly','monthly','monthly','monthly','monthly']
wXlist=[1.,0.]
varXlist=['AODVVOLCdivDAYFOC']
typevarXlist=['glob']

# y-axis : full-chemistry
expYlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test12', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
           
refYlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
          'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13']
expYyear0list=[1975,1975,1975,1975,1975,1975,1975,1975] # exp
expYyear1list=[2014,2014,2014,2014,2014,2014,2014,2014]
refYyear0list=[1975,1975,1975,1975,1975,1975,1975,1975]
refYyear1list=[2014,2014,2014,2014,2014,2014,2014,2014]
seasonYlist=['monthly','monthly','monthly','monthly','monthly','monthly','monthly','monthly']
wYlist=[1.,-1.]
varYlist=['AOD_VISdivDAYFOC']
typevarYlist=['glob']
# 
legendlist=['0% SO4','2.5% SO4','5% SO4','10% SO4','20% SO4','50% SO4','100% SO4','100% SO4(na)']
#
description='trial'
code='2022-09-02-volcano'

#
loopanalysescatterseries2.loopanalysescatterseries2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,description=description,code=code)
#
# [1x1 degree]
# x-axis : CMIP6 prescribed AOD from input4MIPs
expXlist=['NHISTfrc2_f09_tn14_20191025', \
          'NHISTfrc2_f09_tn14_20191025', \
          'NHISTfrc2_f09_tn14_20191025']
refXlist=expXlist
expXyear0list=[1975,1975,1975] # expX
expXyear1list=[2014,2014,2014]
refXyear0list=[1975,1975,1975] # refX
refXyear1list=[2014,2014,2014]
seasonXlist=['monthly','monthly','monthly']
wXlist=[1.,0.]
varXlist=['AODVVOLCdivDAYFOC']
typevarXlist=['glob']

# y-axis : full-chemistry
expYlist=['NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test12', \
          'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
          'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test13']
refYlist=['NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
          'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
          'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16']
expYyear0list=[1975,1975,1975] # exp
expYyear1list=[2014,2014,2014]
refYyear0list=[1975,1975,1975]
refYyear1list=[2014,2014,2014]
seasonYlist=['monthly','monthly','monthly']
wYlist=[1.,-1.]
varYlist=['AOD_VISdivDAYFOC']
typevarYlist=['glob']
# 
legendlist=['0% SO4','10% SO4','100% SO4']
#
description='trial'
code='2022-09-02-volcano-1x1'

#
loopanalysescatterseries2.loopanalysescatterseries2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,description=description,code=code)
#
