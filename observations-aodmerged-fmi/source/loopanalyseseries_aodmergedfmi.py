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
#
#-------------------------------------------------------------
#
# only observations
year0=1995
year1=2017
#
expidlist=['aodmergedfmi','aodmergedfmi','aodmergedfmi','aodmergedfmi','aodmergedfmi','aodmergedfmi']
refidlist=expidlist
#
xdifflist=['abs']
regionlist=['global','NH','SH','90S28S','28S28N','28N60N']
legendlist=regionlist 
varlist=['od550aer','od550aer','od550aer','od550aer','od550aer','od550aer']
code='observations'
description=' '
typelist=['timeseries','timeseries-season','seasonalcycle']
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist, refidlist=refidlist, xdifflist=xdifflist, regionlist=regionlist, legendlist=legendlist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=typelist, description=description,figlayout=figlayout)

# only model
year0=1995
year1=2017
#
expidlist=['histssp585-ozone', \
           'histssp585-ozone', \
           'histssp585-ozone', \
           'histssp585-ozone', \
           'histssp585-ozone', \
           'histssp585-ozone']

refidlist=expidlist

xdifflist=['abs']
regionlist=['global','NH','SH','90S28S','28S28N','28N60N']
legendlist=regionlist
varlist=['od550aer','od550aer','od550aer','od550aer','od550aer','od550aer']
code='model'
description=' '
typelist=['timeseries','timeseries-season','seasonalcycle']
#
figlayout=cfiglayout.CFigLayout(legendlocation='')

loopanalyseseries2.loopanalyseseries2(expidlist=expidlist, refidlist=refidlist, xdifflist=xdifflist, regionlist=regionlist, legendlist=legendlist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=typelist, description=description,figlayout=figlayout)

# observations+model  
year0=1995
year1=2017
#
#expidlist=['toccopernicus','toccopernicus','toccopernicus','toccopernicus','toccopernicus','toccopernicus', \
#           'histssp585-ozone', 'histssp585-ozone', 'histssp585-ozone', 'histssp585-ozone', 'histssp585-ozone', 'histssp585-ozone']
#regionlist=['global','NH','SH','90S28S','28S28N','28N60N','global','NH','SH','90S28S','28S28N','28N60N']
#legendlist=['global','NH','SH','90S28S','28S28N','28N60N', None, None, None, None, None, None]
#dolegendlist=[1,1,1,1,1,1,0,0,0,0,0,0]
#colorlist=[0,1,2,3,4,5,0,1,2,3,4,5]
#linestylelist=[0,0,0,0,0,0,1,1,1,1,1,1]
#varlist=['toc','toc','toc','toc','toc','toc','toc','toc','toc','toc','toc','toc']
#
expidlist=['toccopernicus','toccopernicus','toccopernicus','toccopernicus', \
           'histssp585-ozone', 'histssp585-ozone', 'histssp585-ozone', 'histssp585-ozone']
regionlist=['60N90N','28N60N','28S28N','90S28S','60N90N','28N60N','28S28N','90S28S']
legendlist=['60N90N','28N60N','28S28N','90S28S',None, None, None, None]
dolegendlist=[1,1,1,1,0,0,0,0]
colorlist=[0,1,2,3,0,1,2,3]
linestylelist=[0,0,0,0,1,1,1,1]
varlist=['od550aer','od550aer','od550aer','od550aer','od550aer','od550aer']
#
refidlist=expidlist
xdifflist=['abs']

code='obsmodel_4zones'
description=' '
typelist=['timeseries','timeseries-season','seasonalcycle']
#
figlayout=cfiglayout.CFigLayout(legendlocation='')

loopanalyseseries2.loopanalyseseries2(expidlist=expidlist, refidlist=refidlist, xdifflist=xdifflist, regionlist=regionlist, legendlist=legendlist, dolegendlist=dolegendlist, colorlist=colorlist, linestylelist=linestylelist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=typelist, description=description,figlayout=figlayout)
