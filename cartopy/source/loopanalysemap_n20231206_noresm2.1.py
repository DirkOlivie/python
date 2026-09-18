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
    code='n20231206_noresm2.1'
#
#   STANDARD ERF contribution plots (Stephanies manuscript)
#----------------------------------
    wlist=[1.,-1.]
    seasonlist=['YEA']
    varlist=['SST']
#
    year0list=[1690]
    year1list=[1719]
    expidlist=['N1850_f19_tn14_20231204_test02','N1850_f19_tn14_20231204_test03','N1850_f19_tn14_20231204_test04','N1850_f19_tn14_20190621']
    refidlist=['N1850_f19_tn14_20231204_test05','N1850_f19_tn14_20231204_test05','N1850_f19_tn14_20231204_test05','N1850_f19_tn14_20231204_test05']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
