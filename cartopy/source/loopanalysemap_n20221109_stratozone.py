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

    wlist=[1.,0.]
    year0list=[1991,1994]
    year1list=[1994,1994]
    seasonlist=['YEA']

    varlist=['O3_SRF']

    code = 'n20221109_stratozone'

#   NorESM2 - no chemistry
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08',
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test18']  # full-chemistry
    refidlist=expidlist
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)  
#
#
if __name__ == '__main__':
    main()
