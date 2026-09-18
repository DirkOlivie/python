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
    figlayout3=cfiglayout.CFigLayout(code=''   ,ytype=''   ,colorscheme='toar', ysplit='above500hPa'                ) # linear scale + only above 400hPa
    figlayout4=cfiglayout.CFigLayout(code=''   ,ytype=''   ,colorscheme='toar', ysplit='above200hPa'                ) # linear scale + only above 400hPa
    figlayout5=cfiglayout.CFigLayout(code=''   ,ytype=''   ,colorscheme='toar', ysplit='above150hPa'                ) # linear scale + only above 400hPa
    figlayout6=cfiglayout.CFigLayout(code=''   ,ytype=''   ,colorscheme='toar', ysplit='above100hPa'                ) # linear scale + only above 400hPa
    figlayoutlistLOW=[figlayout0,figlayout1,figlayout2]
    figlayoutlistHGH=[figlayout3,figlayout4,figlayout5,figlayout6]
    figlayoutlist=[figlayout0,figlayout1,figlayout2,figlayout3,figlayout4,figlayout5,figlayout6]
#
#   reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#   reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
    reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL-ESM4','GISS-E2.1_FR','GISS-E2.1_nudged','NorESM2','UKESM1-0-LL']
    refcolorlist=[0,1,2,3,4,5,6,7]


# 1.a reference : 400-0 hPa, 150-0 hPa, ...
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']
# 
    refidlist=expidlist
#
    wlist=[1.,0.]
#    
    year0list=[11,2013,2019,31,11,2030] # 11  2015 2019 2025
    year1list=[50,2016,2023,70,40,2069] # 250 2044 2023 2034
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','EMAC','GEOS-Chem','GFDL-ESM4','NorESM2','UKESM1-0-LL'] # CESM2 GEOS-Chem GISS-E2.1_nudged
#   colorlist=[0,1,2,3,4]
    linestylelist=[0,0,0,0,0,0]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250210_toarmip'
#
#   variables
    varlist=['hus']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
# 2.a perturbation minus reference : 400-0 hPa, 150-0 hPa, ...
#----------------------------------------------------------------------------------------
    expidlist=[\
               'CESM2_pdClim-2050ssp370-radO3_r1r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-2050ssp370-radO3_r1i1p1f1_gn', \
#               'GEOS-Chem-14.2.2_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-2050ssp370-radO3_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-controlfixO3-2050ssp370_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-2050ssp370-radO3_r1i1p1f2_gn']

    refidlist=[\
               'CESM2_pdClim-control_r1r2i1p1f1_gn', \
               'DLR-EMAC_pdClim-control_r1i1p1f1_gn', \
#               'GEOS-Chem-14.2.2_pdClim-control_r1i1p1f1_gr', \
               'GFDL-ESM4_pdClim-control_r1i1p1f1_gr', \
               'NorESM2-LM_pdClim-controlfixO3_r1i1p1f1_gn', \
               'UKESM1-0-LL_pdClim-control_r1i1p1f2_gn']

    refid2list=[\
               'CESM2_pdClim-2050ssp370fixO3-radO3_r1r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
               '']

    refid3list=[\
               'CESM2_pdClim-fixO3_r1r2i1p1f1_gn', \
               '', \
#               '', \
               '', \
               '', \
               '']
#
    wlist=[1.,-1.,-1.,1.]
    wNRlist=[0.,1.,0.,0.]   # USES NUMERATOR FOR FRACTIONS
#    
    year0list=[11,2013,31,11,2030] # 11  2015 2019 2025 
    year1list=[50,2016,70,40,2069] # 250 2044 2023 2034
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','EMAC','GFDL-ESM4','NorESM2','UKESM1-0-LL'] # CESM2 GEOS-Chem GISS-E2.1_nudged
#   colorlist=[0,1,2,3,4]
    linestylelist=[0,0,0,0,0]
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250210_toarmip_diff_extra'
    coderel='n20250210_toarmip_diffrel_extra'

#   absolute difference
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, refid2list=refid2list, refid3list=refid3list)
#
#   relative difference
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=coderel, colorlist=colorlist, linestylelist=linestylelist, wNRlist=wNRlist, refid2list=refid2list, refid3list=refid3list)
#
# 3.a perturbation minus reference : 400-0 hPa, 150-0 hPa, ...
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
    wNRlist=[0.,1.,0.,0.]
#    
    year0list=[11,11,2012,2012,31,31,2030,2030]
    year1list=[50,50,2016,2016,70,70,2069,2069]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['CESM2','','EMAC','','GFDL-ESM4','','UKESM1-0-LL','']
    colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    linestylelist=[0,1,0,1,0,1,0,1]
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250210_toarmip_diff_sens_extra'
    coderel='n20250210_toarmip_diffrel_sens_extra'
#
#   variables
    varlist=['hus']

#   absolute difference
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, refid2list=refid2list, refid3list=refid3list)

#   relative difference
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=coderel, colorlist=colorlist, linestylelist=linestylelist, wNRlist=wNRlist, refid2list=refid2list, refid3list=refid3list)
#
if __name__ == '__main__':
    main()

