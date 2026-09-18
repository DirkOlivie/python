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
#
#  NORESM2.5 + CESM2.5 : DMS, SO2, H2SO4
#----------------------------------------------------------------------------------------
    expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
               'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03']

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1855,2010]
    year1list=[1859,2014]
    seasonlist=['YEA','YEA']
    colorlist=[0,1]
    legendlist=['1855-1859', \
                '2010-2014']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240901_hyway'
#
#   variables
    varlist=['H2']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()
