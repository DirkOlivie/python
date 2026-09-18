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
    expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
               'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010,2010,2010,2010]
    year1list=[2014,2014,2014,2014]
    seasonlist=['YEA','YEA','YEA','YEA']
    colorlist=[0,1,1,2]
    linestylelist=[0,0,2,0]
    legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
                'NorESM2.3-LM-C (AMIP-ch4ems)', \
                'NorESM2.3-LM-C (AMIP)', \
                'UKESM1-0-LL (AMIP-ch4ems)']
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description=''
    code='n20250602_esm2025_ch4'
#
#   variables
    varlist=['ch4','CH4','CH4','ch4']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
