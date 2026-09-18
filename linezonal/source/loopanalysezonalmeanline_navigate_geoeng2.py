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
    code='n20250319_navigate_geoeng2'
#
    varlist=['FSLNT','TREFHT','PRECT','cb_SULFATE']

#
# 1. NorESM2
#----------------------------------------------------------------
    expidlist=['N1850_f19_tn14_20250311_test05_20km', \
               'N1850_f19_tn14_20250311_test05', \
               'N1850_f19_tn14_20250311_test05_26km', \
               'N1850_f19_tn14_20250311_test05_15n60n', \
               'N1850_f19_tn14_20250311_test05_60s15s'] 
    year0list=[1615,1615,1615,1615,1615]
    year1list=[1619,1619,1619,1619,1619]
    refidlist=['N1850_f19_tn14_20250311_test01', \
               'N1850_f19_tn14_20250311_test01', \
               'N1850_f19_tn14_20250311_test01', \
               'N1850_f19_tn14_20250311_test01', \
               'N1850_f19_tn14_20250311_test01']
#
    wlist=[1.,-1.]
#    
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,0,0,0]
    colorlist=[0,1,2,3,4]
    legendlist=['5 Tg[S] yr'+r'$^{-1}$, 20km, 30S-30N', \
                '5 Tg[S] yr'+r'$^{-1}$, 23km, 30S-30N', \
                '5 Tg[S] yr'+r'$^{-1}$, 26km, 30S-30N', \
                '5 Tg[S] yr'+r'$^{-1}$, 23km, 15N-60N', \
                '5 Tg[S] yr'+r'$^{-1}$, 23km, 60S-15S']
#
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

if __name__ == '__main__':
    main()
