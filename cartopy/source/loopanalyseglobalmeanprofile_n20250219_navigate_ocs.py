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
    expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010]
    year1list=[2014]
    seasonlist=['YEA']
    colorlist=[0]
    legendlist=['fullchem']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250219_navigate_ocs'
#
#   variables
    varlist=['OCS','S','SO','SO2','O','OH']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()
