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
    figlayout=cfiglayout.CFigLayout(code='standard', ytype='log')
    figlayoutlist=[figlayout]
#
# 1. NorESM2.5 and NorESM2
#----------------------------------------------------------------------------------------
    expidlist=['CESM2-v212_hyway_transient2010s_r1', \
               'EC-Earth3-AerChem_hyway_transient2010s_r1', \
               'EMAC-DLR_hyway_transient2010s_r1', \
               'LMDZ-INCA_hyway_transient2010s_r1', \
               'NorESM2-LM-C_hyway_transient2010s_r1i1p1f1', \
               'OsloCTM3v1-2_hyway_transient2010s_r1']                       
#
#    expidlist=['OsloCTM3v1-2_hyway_transient2010s_r1', \
#               'CESM2-v212_hyway_transient2010s_r1', \
#               'NorESM2-LM-C_hyway_transient2010s_r1i1p1f1', \
#               'OsloCTM3v1-2_hyway_transient2010s_r1']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010,2010,2010,2010,2010,2010]
    year1list=[2010,2010,2010,2010,2010,2010]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,3,4,5]
    linestylelist=[0,0,0,0,0,0]
    legendlist=['CESM2', \
                'EC-Earth3-AerChem', \
                'EMAC-DLR', \
                'LMDZ-INCA', \
                'NorESM2-LM-C', \
                'OsloCTM3']
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20250929_hyway'
#
#   variables
    varlist=['o3','o3_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
