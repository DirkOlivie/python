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
    code='n20260522_noresm2.3'
#
# 1. 1850-1949 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['SFisoprene','SFmonoterp','cb_SOA_LV','cb_SOA_SV','cb_SOA_A1NA']
#
    expidlist=['N1850_f19_tn14_20241127_test16', \
               'N1850_f19_tn14_20241127_test17']
#
    refidlist=expidlist
    wlist=[1.,0.]
    legendlist=[ \
            'NorESM2.3 (test 16)', \
            'NorESM2.3 (test 17)']
#
    wlist=[1.,0.]
#    
    seasonlist=['YEA','YEA']
    linestylelist=[0,0]
    linewidthlist=[1,1]
    colorlist=[0,1]
#
    year0list=[1600,1600]
    year1list=[1739,1739]

    ensembletypelist=['','']

    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)
#
if __name__ == '__main__':
    main()
