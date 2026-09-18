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
    year0list=[2006]
    year1list=[2014]
    seasonlist=['YEA']

    varlist=['PBLH']

    expidlist=['NHISTfrc2_f19_tn14_bromo_08']
    refidlist=expidlist
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
