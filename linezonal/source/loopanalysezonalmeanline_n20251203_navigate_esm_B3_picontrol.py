import loopanalysezonalmeanline2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalysezonalmeanline +++')
#
    figlayout=cfiglayout.CFigLayout()
    figlayoutlist=[figlayout]
    horizontalaxislist=['']    
    regionlist=['glob']
#
    description='varcommon'
    code='n20251203_navigate_esm_B3_picontrol'
#
# 1. 1910-1929 and 1930-1949 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['FSLNT','TREFHT','PRECT']

    expidlist=['N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
#               'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
                \
               'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316']
#               'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
#               'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224']

    refidlist=['N1850_f19_tn14_20190730esm']*2
#
    ensembletypelist=['minmax','minmax']

    wlist=[1.,-1.]
#    
    seasonlist=['YEA']*2
    linestylelist=[0]*2
#    linewidthlist=[3,0.1,0.1,0.1, \
#                   3,0.1,0.1,0.1]
    linewidthlist=[1.,1.]
    colorlist=[1, \
               7]
    legendlist=['1500Pg', \
                '2000Pg+CDR']
#   1910-1929
    year0list=[1910]*2
    year1list=[1929]*2
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist, ensembletypelist=ensembletypelist)
#   1930-1949
    year0list=[1930]*2
    year1list=[1949]*2
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist, ensembletypelist=ensembletypelist)

# 2. 2030-2049 and 2130-2149 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['FSLNT','TREFHT','PRECT']

    expidlist=['N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
               'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
               'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
               'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
                \
               'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316', \
               'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316', \
               'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224', \
               'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224']
#
#   2030-2049
    year0list=[2030]*8
    year1list=[2049]*8
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#   2130-2149
    year0list=[2130]*8
    year1list=[2149]*8
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#
if __name__ == '__main__':
    main()
