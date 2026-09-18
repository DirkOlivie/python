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

#   1. CESM-only 2010-climo : perturbation simulations
#-----------------------------------------------------
    expidlist=['FC2010climo_prep_f19_20210204_test5',
               'FC2010climo_prep_f19_20210204_test11',
               'FC2010climo_prep_f19_20210204_test17',
               'FC2010climo_prep_f19_20210204_test13',
               'FC2010climo_prep_f19_20210204_test9']
    varlist=['SAD_AERO','OCS','so4_a123','SO2','O3']
    year0list=[9,9,9,9,9]
    year1list=[10,10,10,10,10]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['reference', \
                'no volc.', \
                'no ocs', \
                'no volc., no ocs', \
                'cesm2.2']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20230213_volc_to_stratozone_cesm2_climo2010'
#
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
#   2. CESM-only 2010-climo : perturbation simulations : differences
#-------------------------------------------------------------------
    expidlist=['FC2010climo_prep_f19_20210204_test11',
               'FC2010climo_prep_f19_20210204_test17',
               'FC2010climo_prep_f19_20210204_test13',
               'FC2010climo_prep_f19_20210204_test9']
    refidlist=['FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test5']
    wlist=[1.,-1.]
#
    varlist=['SAD_AERO','OCS','so4_a123','SO2','O3']
    year0list=[9,9,9,9]
    year1list=[10,10,10,10]
    seasonlist=['YEA','YEA','YEA','YEA']
    legendlist=['no volc.', \
                'no ocs', \
                'no volc., no ocs', \
                'cesm2.2']
    regionlist=['glob']#,'glob','glob','glob']
    verticalaxislist=['pressure'] #,'height']
#
    description='varcommon'
    code='n20230213_volc_to_stratozone_cesm2_climo2010_diff'
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
    print('--- loopanalyseglobalmeanprofile ---')
#
if __name__ == '__main__':
    main()
