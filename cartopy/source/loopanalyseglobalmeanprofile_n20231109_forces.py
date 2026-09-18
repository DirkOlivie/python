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
    generalcode='n20231109_forces'
#
#   CMIP6 - 20010-2014 O3
#------------------------
    expidlist=[ \
               'NHIST_f19_tn14_20190710', \
               'NHIST_f19_tn14_Forces_230515'] 
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000]
    year1list=[2000,2000]
    seasonlist=['YEA','YEA']
    legendlist=['Reference', \
                'Nenes']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT','mmr_BC']
    varlist=['DST_A2','DST_A3','SS_A1','SS_A2','SS_A3']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

if __name__ == '__main__':
    main()
