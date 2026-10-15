import numpy as np
import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
import expidlist2attributelist

# MAIN PROGRAM
# CORRECTION


generalcode='n20260925_noresm2.5_picontrol'

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
expXlist=\
         ['N1850.n30b23MM.506.20260821']*8 \
        +['N1850.MM.nor30b23.509.20260901']*2 \
        +['N1850.MM.nor30b24.515.20260908']*4 \
        +['N1850.MM.nor30b24.520.20260913']*8 \
        +['n1850GHG.MM.nor30b25.527.redout.20260929']*10 \
          \
        +['b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']*3
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=[121,131,141,151,161,171,181,191, \
               171,181, \
               171,181,191,201, \
               201,211,221,231,241,251,261,271, \
               301,311,321,331,341,351,361,371,381,391, \
               70,80,90]
expXyear1list=[130,140,150,160,170,180,190,200, \
               180,190, \
               180,190,200,210, \
               210,220,230,240,250,260,270,280, \
               310,320,330,340,350,360,370,380,390,400, \
               79,89,99]
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
varYlist=['tempocn_trend']*(nexpid-3)+['thetaogaocn_trend']*3
typevarYlist=['glob']*nexpid
# 
legendlist=['']*(nexpid-1)+['CESM3 (#316)']
legendlist=['b23 (#506)','','','','','','','', \
            'b23 (#509)','', \
            'b24 (#515)','','','', \
            'b24 (#520)','','','','','','','', \
            'b25 (#527, GHG)','','','','','','','','','', \
            'CESM3 (#316)','','']

colorlist=[0]*8 \
         +[1]*2 \
         +[2]*4 \
         +[3]*8 \
         +[4]*10 \
         +[5]*3
linestylelist=[0]*(nexpid-3) + [2]*3
regressionlist=[0]*(nexpid-3) + [-1]*3

#
code=generalcode+'_ne30pg3_decadal'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout,regressionlist=regressionlist)
