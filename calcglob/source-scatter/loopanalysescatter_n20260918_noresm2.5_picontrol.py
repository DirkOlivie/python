import numpy as np
import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
import expidlist2attributelist

# MAIN PROGRAM
# CORRECTION


generalcode='n20260918_noresm2.5_picontrol'

figlayout=cfiglayout.CFigLayout('')

##############
# 2. ne30pg3 #
##############
#
# 2.a ne30pg3 - n1850
#----------------------------------
#
# x-axis
description=''
# 5th very much out of balance [excluded from regression]
expXlist=[\
          'N1850.ne30pg3_tn14.noresm3_0_beta22.yr101.i488.20260810', \
          'N1850.ne30pg3_tn14.noresm3_0_beta22.yr101.i493.20260810', \
          'N1850.n30b23MM.i496.20260815', \
          'N1850.n30b23MM.506.20260821', \
          'N1850.MM.nor30b23.509.20260901', \
          'N1850.MM.nor30b24.515.20260908', \
          'N1850.MM.nor30b24.520.20260913', \
          \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year0')
expXyear1list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year1')
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT']*nexpid
typevarXlist=['glob']*nexpid
varYlist=['tempocn_trend']*(nexpid-1)+['thetaogaocn_trend']
typevarYlist=['glob']*nexpid
# 
legendlist=['']*(nexpid-1)+['CESM3 (#316)']
legendlist=['#488','#493','#496','#506','#509','#515','#520', \
            'CESM3 (#316)']

colorlist=np.arange(0,nexpid)
linestylelist=[0]*(nexpid-1) + [2]
regressionlist=[0,0,0,1,1,1,1,-1]

#
code=generalcode+'_ne30pg3'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout,regressionlist=regressionlist)
