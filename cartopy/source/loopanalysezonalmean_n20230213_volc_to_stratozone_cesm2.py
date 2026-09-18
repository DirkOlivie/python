import loopanalysezonalmean2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------    
#
    print('+++ loopanalysezonalmean +++')
    print('--- loopanalysezonalmean ---')
#
    filetype='ps'
#
    figlayout0=cfiglayout.CFigLayout(filetype=filetype,contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(filetype=filetype,contour_levels_type='free'   ,code='free'   )
    figlayoutlist=[figlayout0,figlayout1]
#
#   1. CESM2 - climo2010
#------------------------------------------------------------
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
    varlist=['O3']

    seasonlist=['YEA']
#    
    year0=6
    year1=10

    code='n20230213_volc_to_stratozone_cesm2'

    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
