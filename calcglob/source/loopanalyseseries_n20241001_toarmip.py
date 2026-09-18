import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist


freqtype='YEA'
typevar='glob'
description='varcommon-typevarcommon'
generalcode='n20241001_toarmip'

#reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
refcolorlist=[0,1,2,3,4,5,6,7]


# 1.a Absolute values : clt
#------------------------------------------------------------------------
#
expidlist=[ \
           'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
           'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM'] 
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[-2011,0,-2018,0,-1999]
#
#colorlist=[0,1,2,3,4]
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
#

# variables
variablelist=['clt']
#
typevarlist=['glob']

code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#
# 1.b differences : clt
#------------------------------------------------------------------------
#
expidlist=[ \
           'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
           'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refidlist=[ \
           'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
           'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
           'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
           'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
#
wlist=[1.,-1.]
#
legendlist=[ \
            'EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM']
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[-2011,0,-2018,0,-1999]
#
#colorlist=[0,1,2,3,4]
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
#

# variables
variablelist=['clt']
#
typevarlist=['glob']

code=generalcode+'_diff'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 2. Absolute values : toz
#------------------------------------------------------------------------
#
expidlist=[ \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'GFDL','NorESM2-LM','UKESM'] 
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,-1999]
#
#colorlist=[0,1,2]
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
#

# variables
variablelist=['toz']
#
typevarlist=['glob']

code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#
