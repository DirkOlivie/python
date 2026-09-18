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
    year0=2091
    year1=2100
    seasonlist=['YEA']

    varlist=['TREFMXMNAV']
#   varlist=['TREFHT','TREFMXAV','TREFMNAV','TREFMXMNAV']
    varlist=['TREFHT']

#   NorESM2 - no chemistry
    expidlist=['NSSP245frc2_f19_tn14_20191014']  # full-chemistry
    refidlist=['N1850_f19_tn14_20190621']  # reference
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)  
#
#
if __name__ == '__main__':
    main()
