import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard')
#
    generalcode='n20230908_kl_seminar'
#
#   CMIP6 - 20010-2014 O3
#------------------------
    expidlist=['NHISTfrc2_f09_tn14_20191025', \
               'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f09_mg17_20220111_test7']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2005,2005,2005,2005]
    year1list=[2014,2014,2014,2014]
    seasonlist=['YEA','YEA','YEA','YEA']
    legendlist=['NorESM2', \
                'NorESM2-chem', \
                'CESM2-chem (2x2)', \
                'CESM2-chem']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['O3','SO2','H2SO4','DMS']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
#   CMIP6 - 20010-2014 O3
#------------------------
    expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
               'FCHIST_f19_mg17_20220111_test1', \
               'FCHIST_f09_mg17_20220111_test7']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2005,2005,2005]
    year1list=[2014,2014,2014]
    seasonlist=['YEA','YEA','YEA']
    legendlist=['NorESM2-chem', \
                'CESM2-chem (2x2)', \
                'CESM2-chem']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['CO','NO','NO2']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#


if __name__ == '__main__':
    main()
