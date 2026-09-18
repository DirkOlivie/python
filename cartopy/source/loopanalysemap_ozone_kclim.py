import loopanalysemap2
import cfiglayout
#
def main():
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')

    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]

    wlist=[1.,-1.]
    year0=11
    year1=20
    seasonlist=['YEA']

    varlist=['cb_O3']
    varlist=['AOD_VIS']

#   NorESM2 - no chemistry
    expidlist=['NF1850norbc_tropstratchem_f19_20220105_test10']  # full-chemistry
    refidlist=['NF1850norbc_tropstratchem_f19_20220105_test09']  # reference
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)  
#
#
if __name__ == '__main__':
    main()
