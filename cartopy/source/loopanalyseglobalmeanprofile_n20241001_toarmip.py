import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
#
def main():
#-------
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard')
#
#   reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
    reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
    refcolorlist=[0,1,2,3,4,5,6,7]


# 1.a Absolue values : cl
#----------------------------------------------------------------------------------------
    expidlist=[\
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2013,61,2025,31,2060]
    year1list=[2016,70,2034,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM']
#    colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip'
#
#   variables
    varlist=['cl']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#
# 1.b Differences : cl 
#----------------------------------------------------------------------------------------
    expidlist=[\
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
    refidlist=[\
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    wlist=[1.,-1.]
#    
    year0list=[2013,61,2025,31,2060]
    year1list=[2016,70,2034,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM']
#   colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip_diff'
#
#   variables
    varlist=['cl']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#

# 2.a Absolue values : o3
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-control_r1i1p1f1_gn', \
               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr',\
               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[41,41,2013,2016,61,2035,2025,31,2060]
    year1list=[50,50,2016,2020,70,2044,2034,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#    colorlist=[0,0,1,2,3,4,5,6,7]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip'
#
#   variables
    varlist=['o3','o3_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#
# 2.b Difference : o3
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']

    refidlist=[\
               'CESM2_pdClim-control_r1i1p1f1_gn', \
               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr',\
               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    wlist=[1.,-1.]
#    
    year0list=[41,41,2013,2016,61,2035,2025,31,2060]
    year1list=[50,50,2016,2020,70,2044,2034,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#    colorlist=[0,0,1,2,3,4,5,6,7]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip_diff'
#
#   variables
    varlist=['o3','o3_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#
# 3.a Difference : o3 - EMAC
#----------------------------------------------------------------------------------------
    expidlist=[\
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gn']

    refidlist=[\
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn']
    wlist=[1.,-1.]
#    
    year0list=[2013,2013]
    year1list=[2016,2016]
    seasonlist=['YEA','YEA']
    legendlist=['EMAC','EMAC (ODS only)']
    colorlist=[0,1]
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip_diff_ODSonly'
#
#   variables
    varlist=['o3','o3_as_partpress','ta','cl']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#
# 4.a Absolue values : ta
#----------------------------------------------------------------------------------------
    expidlist=[\
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2013,2016,61,31,2060]
    year1list=[2016,2020,70,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['EMAC','GEOS-Chem','GFDL','NorESM2-LM','UKESM']
#    colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist) 
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip'
#
#   variables
    varlist=['ta']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
# 4.b Absolue values : ta
#----------------------------------------------------------------------------------------
    expidlist=[\
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
    refidlist=[\
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    wlist=[1.,-1.]
#    
    year0list=[2013,2016,61,31,2060]
    year1list=[2016,2020,70,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['EMAC','GEOS-Chem','GFDL','NorESM2-LM','UKESM']
#    colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241001_toarmip_diff'
#
#   variables
    varlist=['ta']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#
if __name__ == '__main__':
    main()



