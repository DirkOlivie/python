import loopanalysemap2
import cfiglayout
#
def main():
#----------    
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')
#
    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]
#
    code='n20230525_ozone_sigrid'
#
#   STANDARD ERF contribution plots (Stephanies manuscript)
#----------------------------------
    wlist=[1.,0.]
    seasonlist=['JAN']#['YEA']
    varlist=['O3_SRF']
#
    year0list=[1980]
    year1list=[2014]
    expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test02']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
