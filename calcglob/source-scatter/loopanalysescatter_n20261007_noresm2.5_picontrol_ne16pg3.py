import numpy as np
import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
import expidlist2attributelist

# MAIN PROGRAM
# CORRECTION


generalcode='n20261007_noresm2.5_picontrol'

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
           'n1850Gaxg.n30b23LM.498.20260815', \
           'n1850Gaxg.n30b23LM.502.20260818', \
           \
           'n1850.LM.n30b22.507.GAaxg.20260820', \
           'n1850.LM.n30b22.507.GAaxg_lnd_ic.20260820', \
           'n1850.LM.n30b23.507.GAaxg.20260820', \
           'n1850.LM.n30b23.507.GAaxg_lnd_ic.20260820', \
           'n1850.LM.n30b23.507.woGAaxg.20260820', \
           'n1850.LM.n30b23.507.woGAaxg_lnd_ic.20260820', \
           \
           'n1850esmGaxg.n30b23LM.XYZ.20260820', \
           'n1850esmGaxg.n30b23LM.508.20260824', \
           \
           'n1850Gaxg.LM.n30b24.511.betzy.20260904', \
           'n1850GaxgGHG.LM.n30b24.511.betzy.20260904', \
           'n1850Gaxg.LM.n30b24.516.20260909', \
           'n1850GaxgGHG.LM.n30b24.516.20260909', \
           'n1850GaxgGHG.LM.n30b24.517.20260911', \
           'n1850GaxgGHG.LM.n30b24.517.branch.20260913', \
           'n1850GaxgGHG.LM.nor30b24.525.20260923', \
           \
           'n1850esmGaxgGHG.LM.n30b24.20260916', \
           'n1850esmGaxgGHG.LM.n30b24.20260919', \
           \
           'n1850GaxgGHG.LM.nor30b25.526.redout.20260928', \
           'n1850GaxgGHG.LM.nor30b25.528.20260928', \
           \
           'n1850esmGaxgGHG.LM.n30b25.20260928', \
           'n1850esmGaxgGHG.LM.n30b25.529.20261002']
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
varYlist=['tempocn_trend']*nexpid
typevarYlist=['glob']*nexpid
# 
legendlist=['']*nexpid
legendlist=expXlist

colorlist=np.arange(0,nexpid)
linestylelist=[0]*nexpid
linestylelist=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2]
regressionlist=[1]*nexpid

#
code=generalcode+'_ne16pg3'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout,regressionlist=regressionlist)
