import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard',colorscheme='keyclim-wp6')
#
    generalcode='n20240220_shadoz'
#
#   CMIP6 - 20010-2014 O3
#------------------------
    expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000]
    year1list=[2000]
    seasonlist=['YEA']
    legendlist=['Ozone']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['O3','O3_as_partpress']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

if __name__ == '__main__':
    main()
