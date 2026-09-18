import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout()
    figlayoutlist=[figlayout]
#
# 1. NorESM2.5 and NorESM2
#----------------------------------------------------------------------------------------
    expidlist=['N1850_f19_tn14_20190621', \
               'N1850_f19_tn14_20250311_test01', \
               'N1850_f19_tn14_20250311_test05_20km', \
               'N1850_f19_tn14_20250311_test05', \
               'N1850_f19_tn14_20250311_test05_26km', \
               'N1850_f19_tn14_20250311_test05_15n60n',
               'N1850_f19_tn14_20250311_test05_60s15s']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1615,1615,1615,1615,1615,1615,1615]
    year1list=[1619,1619,1619,1619,1619,1619,1619]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,3,4,5,6]
    legendlist=['N1850_f19_tn14_20190621', \
                'N1850_f19_tn14_20250311_test01', \
                'N1850_f19_tn14_20250311_test05_20km', \
                'N1850_f19_tn14_20250311_test05', \
                'N1850_f19_tn14_20250311_test05_26km', \
                'N1850_f19_tn14_20250311_test05_15n60n',
                'N1850_f19_tn14_20250311_test05_60s15s']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250319_navigate_geoeng2'
#
#   variables
    varlist=['mmr_SULFATE']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()
