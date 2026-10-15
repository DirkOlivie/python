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
expXlist=\
         ['n1850Gaxg.LM.n30b24.516.20260909']*5 \
        +['n1850GaxgGHG.LM.n30b24.516.20260909']*10 \
        +['n1850GaxgGHG.LM.n30b24.517.20260911']*7 \
        +['n1850GaxgGHG.LM.nor30b24.525.20260923']*5 \
          \
        +['n1850esmGaxgGHG.LM.n30b24.20260916'] \
        +['n1850esmGaxgGHG.LM.n30b24.20260919'] \
           \
        +['n1850GaxgGHG.LM.nor30b25.526.redout.20260928']*2 \
        +['n1850GaxgGHG.LM.nor30b25.528.20260928']*15 \
           \
        +['n1850esmGaxgGHG.LM.n30b25.20260928']*6 \
        +['n1850esmGaxgGHG.LM.n30b25.529.20261002']*16
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=[1426,1436,1446,1456,1466, \
               1426,1436,1446,1456,1466,1476,1486,1496,1506,1516, \
                              1456,1466,1476,1486,1496,1506,1516, \
                                                                 1526,1536,1546,1556,1566, \
                                        1476, \
                                        1476, \
                                                                 1526,1536, \
                                                                 1526,1536,1546,1556,1566,1576,1586,1596,1606,1616,1626,1636,1646,1656,1666, \
                                                                 1526,1536,1546,1556,1566,1576, \
                                                                                     1566,1576,1586,1596,1606,1616,1626,1636,1646,1656,1666,1676,1686,1696,1706,1716]                                                   
expXyear1list=[1435,1445,1455,1465,1475, \
               1435,1445,1455,1465,1475,1485,1495,1505,1515,1525, \
                              1465,1475,1485,1495,1505,1515,1525, \
                                                                 1535,1545,1555,1565,1571, \
                                        1485, \
                                        1485, \
                                                                 1535,1545, \
                                                                 1535,1545,1555,1565,1575,1585,1595,1605,1615,1625,1635,1645,1655,1665,1675, \
                                                                 1535,1545,1555,1565,1575,1585, \
                                                                                     1575,1585,1595,1605,1615,1625,1635,1645,1655,1665,1675,1685,1695,1705,1715,1725] 
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
legendlist=['b24 (#516, no GHG)','','','','', \
            'b24 (#516, no GHG, esm)','','','','','','','','','', \
            'b24 (#517)', '','','','','','', \
            'b24 (#525)', '','','','', \
            'b24 (esm)', \
            'b24 (esm)', \
            'b25 (#526)','', \
            'b25 (#528)']+['']*14 \
          +['b25 (#523, esm)','','','','','', \
            'b25 (#529,esm)']+['']*15

colorlist=[0]*5  \
         +[1]*10 \
         +[2]*7  \
         +[3]*5  \
         +[4]    \
         +[5]    \
         +[6]*2  \
         +[7]*15  \
         +[8]*6  \
         +[9]*16  

linestylelist=[0]*nexpid
linestylelist=[0]*nexpid
regressionlist=[1]*nexpid

#
code=generalcode+'_ne16pg3_decadal'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout,regressionlist=regressionlist)
