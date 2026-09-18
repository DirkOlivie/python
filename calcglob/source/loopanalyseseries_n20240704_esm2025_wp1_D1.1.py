import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon-typevarcommon'
generalcode='n20240704_esm2025_wp1_D1.1'


# ALL VARIABLES (except ozone)
#------------------------------------------------------------------------
#
expidlist=[ \
           'histssp585', \
           'histssp585-ozone']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Ozone'] 
#
#smoothlist=[0,0,0,0,0,0,0,0]
smoothlist=[5,5]
#
shiftlist=[0,0]
#
colorlist=[0,1]
#

# variables
variablelist=['tempocn','TREFHT','PRECT']
#
typevarlist=['glob']

code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
