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
    code='n20251203_navigate_esm_picontrol'
#
# 1. 1850-1949 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['FSLNT','TREFHT','PRECT','TROP_P','TROP_Z']

    expidlist=['N1850_f19_tn14_20190730esm']
    refidlist=expidlist
#
    wlist=[1.,0.]
#    
    seasonlist=['YEA']
    linestylelist=[0]
    linewidthlist=[1]
    colorlist=[4]
    legendlist=['piControl-esm']
#
    year0list=[1751]
    year1list=[2200]
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#
if __name__ == '__main__':
    main()
