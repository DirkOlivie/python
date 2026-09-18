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
    figlayout=cfiglayout.CFigLayout(code='standard', colorscheme='keyclim-wp6')
    figlayoutlist=[figlayout]
#
# 1. NorESM2.5 and NorESM2
#----------------------------------------------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s02_esm2025_20250506']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1955]
    year1list=[1959]
    seasonlist=['YEA']
    colorlist=[0]
    legendlist=['fullchem']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250509_esm2025_ch4'
#
#   variables
    varlist=['OCS','S','SO','SO2','O','OH']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()
