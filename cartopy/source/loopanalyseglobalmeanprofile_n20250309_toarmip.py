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
    figlayout0=cfiglayout.CFigLayout(code='log',ytype='log',colorscheme='toar'                                      ) # log scale for y-axis (height or pressure)
    figlayout1=cfiglayout.CFigLayout(code=''   ,ytype=''   ,colorscheme='toar'                      , csvoutput=True) # linear scale
    figlayout2=cfiglayout.CFigLayout(code=''   ,ytype=''   ,colorscheme='toar', ysplit='split400hPa'                ) # linear scale + split at 400hPa
    figlayoutlist=[figlayout0,figlayout1,figlayout2]
#
#   reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#   reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
    reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL-ESM4','GISS-E2.1_FR','GISS-E2.1_nudged','NorESM2','UKESM1-0-LL']
    refcolorlist=[0,1,2,3,4,5,6,7]


# 1.a Absolue values : cl
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-control_r1i1p1f1_gn', \
               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[11,11,2012,2019,31,2015,2025,21,2030]
    year1list=[50,50,2016,2023,70,2044,2034,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','','EMAC','GEOS-Chem','GFDL-ESM4','GISS-E2.1_FR','GISS-E2.1_nudged','NorESM2','UKESM1-0-LL']
#    colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip'
#
#   variables
    varlist=['cl']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
#
# 1.b Differences : cl 
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#               'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#               'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
    refidlist=[\
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
#               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']

    refid2list=[\
               'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
#               '', \
               '', \
               '']     
 
    refid3list=[\
               'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
#               '', \
               '', \
               '']     
# 
    wlist=[1.,-1.,-1.,1.]
#    
    year0list=[11,2013,31,2015,11,2030] # 2019 2025
    year1list=[50,2016,70,2044,40,2069] # 2023 2034
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL'] # GEOS-Chem GISS-E2.1_nudged
#   colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip_diff'
#
#   variables
    varlist=['cl']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, refid2list=refid2list, refid3list=refid3list)
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
    year0list=[11,11,2012,2019,31,2015,2025,21,2030]
    year1list=[50,50,2016,2023,70,2044,2034,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','','EMAC','GEOS-Chem','GFDL-ESM4','GISS-E2.1_FR','GISS-E2.1_nudged','NorESM2','UKESM1-0-LL']
#    colorlist=[0,0,1,2,3,4,5,6,7]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip'
#
#   variables
    varlist=['o3','o3_as_partpress']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
#
# 2.b Difference : o3
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#               'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
#               'GISS-E2-1-G_pdClim-2050ssp370-radO3_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']

    refidlist=[\
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr',\
#               'GISS-E2-1-G_pdClim-control_r1i1p3f2_gn', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']

    refid2list=[\
               'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
#               '', \
               '', \
               '']

    refid3list=[\
               'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
#               '', \
               '', \
               '']
# 
    wlist=[1.,-1.,-1.,1.]
#    
    year0list=[11,2012,31,2015,21,2030] # 2019 2025
    year1list=[50,2016,70,2044,40,2069] # 2023 2034
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL']
#    colorlist=[0,0,1,2,3,4,5,6,7]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip_diff'
#
#   variables
    varlist=['o3','o3_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist) 
# , refid2list=refid2list, refid3list=refid3list) DOES NOT WORK WELL
#
#
# 3. Perturbation experiments : difference o3/ta/cl - EMAC / GFDL / UKESM
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
               'CESM2_pdClim-2050ssp370fODS-radO3_r1r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gn', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370onlyODS-radO3_r1i1p1f1_gr', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370onlyODS-radO3_r1i1p1f2_gn']

    refidlist=[\
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']

    refid2list=[\
               'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
               'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
               '', \
               '', \
               '', \
               '', \
               '', \
               '']

    refid3list=[\
               'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
               'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
               '', \
               '', \
               '', \
               '', \
               '', \
               '']

    wlist=[1.,-1.,-1.,1.]
#    
    year0list=[11,11,2012,2012,31,31,2030,2030]
    year1list=[50,50,2016,2016,70,70,2069,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
#   legendlist=['EMAC','EMAC (ODS only)','GFDL','GFDL (ODS only)','UKESM','UKESM (ODS only)']
    legendlist=['CESM2','','EMAC','','GFDL-ESM4','','UKESM1-0-LL','']
#    colorlist=[0,0,1,1,2,2]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    linestylelist=[0,1,0,1,0,1,0,1]
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip_diff_ODSonly'
#
#   variables
    varlist=['o3','o3_as_partpress','ta','cl']
#    varlist=['o3_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist,linestylelist=linestylelist)
#
#
# 4.a Absolue values : ta
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-control_r1i1p1f1_gn', \
               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[11,11,2012,2019,31,21,2030]
    year1list=[50,50,2016,2023,70,40,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','','EMAC','GEOS-Chem','GFDL-ESM4','NorESM2','UKESM1-0-LL']
#    colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist) 
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip'
#
#   variables
    varlist=['ta']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
# 4.b Difference : ta
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-2050ssp370-radO3_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#              'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']
#
    refidlist=[\
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-control_r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#              'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'GISS-E2.1-G_pdClim-control_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-control_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
#
    refid2list=[\
               'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-2050ssp370fixO3-radO3_r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
               '', \
               '']
#
    refid3list=[\
               'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
#               'CESM2_pdClim-fixO3_r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
               '', \
               '']
    wlist=[1.,-1.,-1.,1.]
#    
    year0list=[11,2012,31,2015,11,2030] # 2019
    year1list=[50,2016,70,2044,40,2069] # 2023
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','EMAC','GFDL-ESM4','GISS-E2.1_FR','NorESM2','UKESM1-0-LL'] # 'GEOS-Chem'
#    colorlist=[0,1,2,3,4]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250309_toarmip_diff'
#
#   variables
    varlist=['ta']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, refid2list=refid2list, refid3list=refid3list)
#
#
if __name__ == '__main__':
    main()



