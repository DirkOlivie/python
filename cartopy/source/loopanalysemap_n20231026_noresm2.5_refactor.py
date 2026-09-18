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
    code='n20231026_noresm2.5_refactor'
#
#   STANDARD ERF contribution plots (Stephanies manuscript)
#----------------------------------
    wlist=[1.,0.]
    seasonlist=['YEA']
    varlist=['BC_AC_OCWclcoagTend','cb_BC_AC','cb_BC_AC_OCW']
#
    year0list=[3]
    year1list=[5]
    expidlist=['NF2000oslo.f19_f19_mtn14.2','NF2000oslo.f19_f19_mtn14.3']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
