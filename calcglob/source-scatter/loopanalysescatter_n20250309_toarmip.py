import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist

# MAIN PROGRAM
# CORRECTION
#   2024-11-24 : replaced NorESM2-LM_pdClim-controlfixO3-2050ssp370_r1i1p1f1_gn by NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn



description='varcommon-typevarcommon'
generalcode='n20250309_toarmip'

figlayout=cfiglayout.CFigLayout(colorscheme='toar', csvoutput=True)

#reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL-ESM4','GISS-E2.1_FR','GISS-E2.1_nudged','NorESM2','UKESM1-0-LL']
refcolorlist=[0,1,2,3,4,5,6,7]

# 1. REFERENCE EXPERIMENTS
#----------------------------------
# x-axis
expXlist=[ \
          'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
#          'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#         'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refXlist=[ \
          'CESM2_pdClim-control_r1r2i1p1f1_gn', \
#         'CESM2_pdClim-control_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#        'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
#
refX2list=[\
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
#          'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '']
#refX2list=['','','','','','','']
#
refX3list=[\
          'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
#          'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '']
#refX3list=['','','','','','','']

expXyear0list=[11,2012,31,2015,11,2030] # 2019, 2025
expXyear1list=[50,2016,70,2044,40,2069] # 2023, 2034 
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA','YEA','YEA','YEA']
wXlist=[1.,-1.,-1.,1.]
#wXlist=[1.,-1.,0.,0.]

# y-axis
expYlist=expXlist
refYlist=refXlist
refY2list=refX2list
refY3list=refX3list

expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['clt','clt','clt','clt','clt']
typevarXlist=['glob','glob','glob','glob','glob']
varYlist=['rsut','rlut','minusrsutcloud','minusrlutcloud','minusrsutrlutcloud']
typevarYlist=['glob','glob','glob','glob','glob']
# 
legendlist=[ \
            'CESM2','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL'] # GEOS-Chem and GISS nudged removed
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
linestylelist=[0,0,0,0,0,0]
#
code=generalcode

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout, \
        refX2list=refX2list,refX3list=refX3list,refY2list=refY2list,refY3list=refY3list)
#
# 2. SENSITIVITY EXPERIMENTS
#------------------------
# x-axis
expXlist=[ \
           'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
           'DLR-EMAC_pdClim-2050ssp370onlyODS-radO3_r1i2p1f1_gn', \
           'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
           'GFDL-ESM4_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gr', \
           'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn', \
           'UKESM1-0-LL_pdClim-2050ssp370onlyODS-radO3_r1i1p1f2_gn']
#
refXlist=[ \
           'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
           'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
           'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
           'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
           'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn', \
           'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']

expXyear0list=[2012,2012,31,31,2030,2030]
expXyear1list=[2016,2016,70,70,2069,2069]
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA','YEA','YEA','YEA']
wXlist=[1.,-1.]

# y-axis
expYlist=expXlist
refYlist=refXlist

expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=[1.,-1.]

# variables
varXlist=['clt','clt','clt','clt','clt']
typevarXlist=['glob','glob','glob','glob','glob']
varYlist=['rsut','rlut','minusrsutcloud','minusrlutcloud','minusrsutrlutcloud']
typevarYlist=['glob','glob','glob','glob','glob']
# 
legendlist=[ \
            'EMAC','','GFDL-ESM4','','UKESM1-0-LL',''] #,''] # GISS nudged
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
linestylelist=[0,1,0,1,0,1]
#
code=generalcode+'_sensitivity'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)
#
# 3. REFERENCE+SENSITIVITY EXPERIMENTS
#----------------------------------
# x-axis
expXlist=['CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fODS-radO3_r1r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
          'DLR-EMAC_pdClim-2050ssp370onlyODS-radO3_r1i2p1f1_gn', \
#          'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn', \
          'UKESM1-0-LL_pdClim-2050ssp370onlyODS-radO3_r1i1p1f2_gn']
#
refXlist=['CESM2_pdClim-control_r1r2i1p1f1_gn', \
          'CESM2_pdClim-control_r1r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
          'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#          'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn', \
          'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
#
refX2list=[\
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '', \
          '', \
          '', \
          '']
#
refX3list=[\
          'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
          'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '', \
          '', \
          '', \
          '']

expXyear0list=[11,11,2012,2012,31,31,2015,11,2030,2030] # 2019, 2025
expXyear1list=[50,50,2016,2016,70,70,2044,40,2069,2069] # 2023, 2034 
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
wXlist=[1.,-1.,-1.,1.]

# y-axis
expYlist=expXlist
refYlist=refXlist
refY2list=refX2list
refY3list=refX3list


expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist


# variables
varXlist=['clt','clt','clt','clt','clt']
typevarXlist=['glob','glob','glob','glob','glob']
varYlist=['rsut','rlut','minusrsutcloud','minusrlutcloud','minusrsutrlutcloud']
typevarYlist=['glob','glob','glob','glob','glob']
# 
legendlist=[ \
            'CESM2','','EMAC','','GFDL-ESM4','','GISS-E2.1_FR','NorESM2','UKESM1-0-LL',''] # GEOS-Chem and GISS nudged remove
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
linestylelist=[0,1,0,1,0,1,0,0,0,1]
#
code=generalcode+'_all'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout, \
        refX2list=refX2list,refX3list=refX3list,refY2list=refY2list,refY3list=refY3list)
#
# 4. SW, LW and SW+LW in one plot - different orientation of figure
#------------------------------------------------------------------
description=''
figlayout=cfiglayout.CFigLayout(colorscheme='toar',figsize=[8,4])

# x-axis
expXlist=[ \
          'CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#         'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn', \
#
          'CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#         'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn', \
#
          'CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#         'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
refXlist=[ \
          'CESM2_pdClim-control_r1i1p1f1_gn', \
          'CESM2_pdClim-control_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#        'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn', \
#
          'CESM2_pdClim-control_r1i1p1f1_gn', \
          'CESM2_pdClim-control_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#        'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn', \
#
          'CESM2_pdClim-control_r1i1p1f1_gn', \
          'CESM2_pdClim-control_r2i1p1f1_gn', \
          'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#        'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
          'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
          'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
#         'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
          'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
          'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
#
#
refX2list=[\
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '', \
#
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '', \
#
          'CESM2_pdClim-2050ssp370fixO3-radO3_r1i1p1f1_gn', \
          'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '']
#
refX3list=[\
          'CESM2_pdClim-fixO3_r1i1p1f1_gn', \
          'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '', \
#
          'CESM2_pdClim-fixO3_r1i1p1f1_gn', \
          'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '', \
#
          'CESM2_pdClim-fixO3_r1i1p1f1_gn', \
          'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
          '', \
          '', \
          '', \
          '', \
          '']
#
expXyear0list=[11,11,2012,31,2015,11,2030, \
               11,11,2012,31,2015,11,2030, \
               11,11,2012,31,2015,11,2030] # 2019, 2025
expXyear1list=[50,50,2016,70,2044,40,2069, \
               50,50,2016,70,2044,40,2069, \
               50,50,2016,70,2044,40,2069] # 2023, 2034 
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA', \
             'YEA','YEA','YEA','YEA','YEA','YEA','YEA', \
             'YEA','YEA','YEA','YEA','YEA','YEA','YEA']
wXlist=[1.,-1.,-1.,1.]

# y-axis
expYlist=expXlist
refYlist=refXlist
refY2list=refX2list
refY3list=refX3list

expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varYlist=['clt','clt','clt','clt','clt','clt','clt', \
          'clt','clt','clt','clt','clt','clt','clt', \
          'clt','clt','clt','clt','clt','clt','clt']
typevarXlist=['glob','glob','glob','glob','glob','glob','glob', \
              'glob','glob','glob','glob','glob','glob','glob', \
              'glob','glob','glob','glob','glob','glob','glob']
varXlist=['minusrsutcloud','minusrsutcloud','minusrsutcloud','minusrsutcloud','minusrsutcloud','minusrsutcloud','minusrsutcloud', \
          'minusrlutcloud','minusrlutcloud','minusrlutcloud','minusrlutcloud','minusrlutcloud','minusrlutcloud','minusrlutcloud', \
          'minusrsutrlutcloud','minusrsutrlutcloud','minusrsutrlutcloud','minusrsutrlutcloud','minusrsutrlutcloud','minusrsutrlutcloud','minusrsutrlutcloud']
typevarYlist=['glob','glob','glob','glob','glob','glob','glob', \
              'glob','glob','glob','glob','glob','glob','glob', \
              'glob','glob','glob','glob','glob','glob','glob']
# 
# to find the good colors
legendlist=[ \
            'CESM2','','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL', \
            'CESM2','','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL', \
            'CESM2','','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL']  
colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
colorlist=[0,0,0,0,0,0,0, \
           1,1,1,1,1,1,1, \
           2,2,2,2,2,2,2]

# to actually be used 
legendlist=[ \
            'CESM2','','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL', \
            '','','','','','','', \
            '','','','','','','']

legendlist=['','','','','','','', \
            '','','','','','','', \
            '','','','','','','']



linestylelist=[0,0,0,0,0,0,0, \
               1,1,1,1,1,1,1, \
               2,2,2,2,2,2,2]
#
code=generalcode+'_combined'

#
#loopanalysescatter2.loopanalysescatter2(\
#        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
#        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
#        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout, \
#        refX2list=refX2list,refX3list=refX3list,refY2list=refY2list,refY3list=refY3list)
#
