import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist

figlayout=cfiglayout.CFigLayout(colorscheme='toar')

freqtype='YEA'
typevar='glob'
description='varcommon-typevarcommon'
generalcode='n20241022_toarmip'

#reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
refcolorlist=[0,1,2,3,4,5,6,7]


# 1.a Absolute values : clt
#------------------------------------------------------------------------
#
expidlist=[ \
           'CESM2_pdClim-control_r1i1p1f1_gn', \
           'CESM2_pdClim-control_r2i1p1f1_gn', \
           'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
           'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
           'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
           'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'CESM2','','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM'] 
#
smoothlist=[0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,-2011,-2018,0,-2014,-2018,0,-1999]
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
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#
# 1.b differences : clt
#------------------------------------------------------------------------
#
expidlist=[ \
           'CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
           'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
           'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
           'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
           'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refidlist=[ \
           'CESM2_pdClim-control_r1i1p1f1_gn', \
           'CESM2_pdClim-control_r2i1p1f1_gn', \
           'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
           'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
           'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
           'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
           'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
           'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
#
refid2list=[\
           'CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn', \
           'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
           '', \
           '', \
           '', \
           '', \
           '', \
           '', \
           '']
#
refid3list=[\
           'CESM2_pdClim-fixO3_r1i1p1f1_gn', \
           'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
           '', \
           '', \
           '', \
           '', \
           '', \
           '', \
           '']
#
wlist=[1.,-1.,-1.,1.]
#
legendlist=[ \
            'CESM2','','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#
smoothlist=[0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,-2011,-2018,0,-2014,-2018,0,-1999]
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
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 2. Absolute values : toz
#------------------------------------------------------------------------
#
expidlist=[ \
           'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'GEOS-Chem','GFDL','NorESM2-LM','UKESM'] 
#
smoothlist=[0,0,0,0]
#
shiftlist=[-2018,0,0,-1999]
#
#colorlist=[0,1,2]
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
#

# variables
variablelist=['toz','rlutcloud']
#
typevarlist=['glob']

code=generalcode
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 3. clt CEMS only 
#------------------------------------------------------------------------
#
expidlist=[ \
          'CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
          'CESM2_pdClim-control_r1i1p1f1_gn', \
          'CESM2_pdClim-control_r2i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
          'CESM2_pdClim-fixO3_r1i1p1f1_gn', \
          'CESM2_pdClim-fixO3_r2i1p1f1_gn']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            '2050ssp370-radO3','','control','','2050ssp370fixO3-radO3','','fixO3','']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0]
#
colorlist=[0,0,1,1,2,2,3,3]
#colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
#

# variables
variablelist=['clt']
#
typevarlist=['glob']

code=generalcode+'_cesm2'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
