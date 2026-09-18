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
    code='n20230411_ch4_coupling'
#
#   STANDARD ERF contribution plots (Stephanies manuscript)
#----------------------------------
    wlist=[1.,0.]
    seasonlist=['DJF']#['YEA']
    varlist=['FCH4','emich4land']
#
    year0list=[10]
    year1list=[10]
    expidlist=['N1850vsls_ch4_tropstratchem_prep_f19_nt14_20230331_test02']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
