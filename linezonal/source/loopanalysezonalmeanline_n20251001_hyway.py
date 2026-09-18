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
    code='n20251001_hyway'
#
    varlist=['o3_surfacelayer','ch4_surfacelayer','h2_surfacelayer']

#
# 1. CESM / LMDZ / NorESM / OsloCTM
#----------------------------------------------------------------
    expidlist=['CESM2-v212_hyway_transient2010s_r1', \
               'LMDZ-INCA_hyway_transient2010s_r1', \
               'NorESM2-LM-C_hyway_transient2010s_r1i1p1f1', \
               'OsloCTM3v1-2_hyway_transient2010s_r1']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010,2010,2010,2010]
    year1list=[2019,2019,2019,2019]
    seasonlist=['YEA','YEA','YEA','YEA']
    linestylelist=[0,0,0,0]
    colorlist=[0,1,2,3]
    legendlist=['CESM2-v212', \
               'LMDZ-INCA', \
               'NorESM2-LM-C', \
               'OsloCTM3v1-2']
#
    description='varcommon'
    varlist=['o3_surfacelayer','ch4_surfacelayer','h2_surfacelayer']
#
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)


if __name__ == '__main__':
    main()
