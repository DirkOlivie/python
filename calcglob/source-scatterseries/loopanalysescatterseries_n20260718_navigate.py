import loopanalysescatterseries2

# MAIN PROGRAM

description='varcommon'

# OBTAINING VOLCANIC EMISSION TOTAL
#----------------------------------
# [2x2 degree]
# x-axis : CMIP6 prescribed AOD from input4MIPs
expXlist=['NHIST_f19_tn14_20250311_test05']*3
refXlist=expXlist
expXyear0list=[1950]*3
expXyear1list=[1999]*3
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*3
wXlist=[1.,0.]
varXlist=['AOD_VISdivDAYFOC']*3
typevarXlist=['glob']*3

# y-axis : full-chemistry
expYlist=['NHIST_f19_tn14_20190710', \
          'NHIST_02_f19_tn14_20190813', \
          'NHIST_03_f19_tn14_20190813'] 
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=refXyear0list
refYyear1list=refXyear1list
seasonYlist=seasonXlist
wYlist=[1.,0.]
varYlist=['AOD_VISdivDAYFOC']*3
typevarYlist=['glob']*3
# 
legendlist=['NorESM2-LM (#1)', \
            'NorESM2-LM (#2)', \
            'NorESM2-LM (#3)']
#
colorlist=[0,1,2]
dolinearregressionlist=[1,1,1]
#
description='trial'

# ANNUAL
code='n20260718_navigate_YEA'
loopanalysescatterseries2.loopanalysescatterseries2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,dolinearregressionlist=dolinearregressionlist, \
        description=description,code=code)

# ANNUAL
code='n20260718_navigate_monthly'
seasonXlist=['monthly']*3
seasonYlist=seasonXlist
loopanalysescatterseries2.loopanalysescatterseries2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,dolinearregressionlist=dolinearregressionlist, \
        description=description,code=code)
