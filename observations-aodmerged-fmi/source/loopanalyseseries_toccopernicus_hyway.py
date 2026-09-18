import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

'''
REMARK
    1970-1978 : data on lower resolution
       

CALLS
    loopanalyseseries2
''' 

# NorESM2 raw data
#-----------------
year0=2000
year1=2019
#
expidlist=['toccopernicus','toccopernicus','toccopernicus','toccopernicus', \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521', \
           'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521']
regionlist=['60N90N','28N60N','28S28N','90S28S','60N90N','28N60N','28S28N','90S28S']
legendlist=['60N90N','28N60N','28S28N','90S28S',None, None, None, None]
dolegendlist=[1,1,1,1,0,0,0,0]
colorlist=[0,1,2,3,0,1,2,3]
linestylelist=[0,0,0,0,1,1,1,1]
varlist=['toc','toc','toc','toc','toc','toc','toc','toc']
#
refidlist=expidlist
xdifflist=['abs']

code='obsmodel_4zones_hyway'
description=' '
typelist=['timeseries','timeseries-season','seasonalcycle']
typelist=['timeseries']
#
figlayout=cfiglayout.CFigLayout(legendlocation='')

#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist, refidlist=refidlist, xdifflist=xdifflist, regionlist=regionlist, legendlist=legendlist, dolegendlist=dolegendlist, colorlist=colorlist, linestylelist=linestylelist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=typelist, description=description,figlayout=figlayout)
#
# ALL HYwya models cmorized data
#-------------------------------
year0=2010
year1=2019
#
expidlist=['toccopernicus'                             ]*4 \
         +['NorESM2-LM-C_hyway_transient2010s_r1i1p1f1']*4 \
         +['CESM2-v212_hyway_transient2010s_r1'        ]*4 \
         +['OsloCTM3v1-2_hyway_transient2010s_r1'      ]*4 \
         +['EMAC-DLR_hyway_transient2010s_r1'          ]*4 \
         +['EC-Earth3-AerChem_hyway_transient2010s_r1' ]*4
#           
regionlist=['60N90N','28N60N','28S28N','90S28S', \
            '60N90N','28N60N','28S28N','90S28S', \
            '60N90N','28N60N','28S28N','90S28S', \
            '60N90N','28N60N','28S28N','90S28S', \
            '60N90N','28N60N','28S28N','90S28S', \
            '60N90N','28N60N','28S28N','90S28S']
legendlist=['60N90N','28N60N','28S28N','90S28S', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
dolegendlist=[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
colorlist=[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
linestylelist=[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
varlist=['toc']*24
#
refidlist=expidlist
xdifflist=['abs']

code='obsmodel_4zones_hyway_v2'
description=' '
typelist=['timeseries','timeseries-season','seasonalcycle']
#
figlayout=cfiglayout.CFigLayout(legendlocation='')

#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist, refidlist=refidlist, xdifflist=xdifflist, regionlist=regionlist, legendlist=legendlist, dolegendlist=dolegendlist, colorlist=colorlist, linestylelist=linestylelist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=typelist, description=description,figlayout=figlayout)


# ALL HYwya models cmorized data : single zone
#---------------------------------------------
year0=2010
year1=2019
#
expidlist=['toccopernicus',                              \
           'CESM2-v212_hyway_transient2010s_r1',         \
           'EC-Earth3-AerChem_hyway_transient2010s_r1',  \
           'EMAC-DLR_hyway_transient2010s_r1',           \
           'NorESM2-LM-C_hyway_transient2010s_r1i1p1f1', \
           'OsloCTM3v1-2_hyway_transient2010s_r1']
#           
regiongrouplist=['60N90N','28N60N','28S28N','90S28S','glob']
legendlist=['Observations',                               \
            'CESM2-v212',         \
            'EC-Earth3-AerChem',  \
            'EMAC-DLR_hyway',           \
            'NorESM2-LM-C', \
            'OsloCTM3v1-2']
dolegendlist=[1,1,1,1,1,1]
colorlist=[0,1,2,3,4,5]
linestylelist=[2,0,0,0,0,0]
varlist=['toc']*6
#
refidlist=expidlist
xdifflist=['abs']

description=' '
typelist=['timeseries','timeseries-season','seasonalcycle']
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
for regiongroup in regiongrouplist:
    code='obsmodel_'+regiongroup+'_hyway_v2'

    regionlist=[regiongroup]*6    

    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist, refidlist=refidlist, xdifflist=xdifflist, regionlist=regionlist, legendlist=legendlist, dolegendlist=dolegendlist, colorlist=colorlist, linestylelist=linestylelist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=typelist, description=description,figlayout=figlayout)






