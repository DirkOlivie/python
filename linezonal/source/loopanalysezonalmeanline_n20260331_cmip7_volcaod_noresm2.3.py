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
    code='n20260331_cmip7_volcaod_noresm2.3'
#
# 1. 1850-1949 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['FSLNT','FSLNTC','FSDS','FSDSC']

    expidlist=[ \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip6', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7wghtavg']
#
    refidlist=[ \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
           'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone']
    wlist=[1.,-1.]
    legendlist=[ \
            'CMIP6', \
            'CMIP7', \
            'CMIP7-weighted']
#
    wlist=[1.,-1.]
#    
    seasonlist=['YEA','YEA','YEA']
    linestylelist=[0,0,0]
    linewidthlist=[1,1,1]
    colorlist=[0,1,2]
#
    year0list=[1970,1970,1970]
    year1list=[1979,1979,1979]
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#
if __name__ == '__main__':
    main()
