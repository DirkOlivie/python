import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon-typevarcommon'
generalcode='n20240925_camsvsls'


# ALL EXPERIMENTS (NEW + BROMO-08 + FULLCHEM + CMIP6)
#------------------------------------------------------------------------
#
expidlist=[ \
           'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            ''] 
#
smoothlist=[0]
#
shiftlist=[0]
#
colorlist=[0]
#

# variables
variablelist=['SFDMS','SFCHBR3']
#
typevarlist=['glob']

code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

