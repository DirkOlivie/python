import loopanalyseoceancolumnintegral2
import cfiglayout
#
def main():
#
    print('+++ loopanalyseoceancolumnintegral +++')
    print('--- loopanalyseoceancolumnintegral ---')

    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]

#   NorESM2.1
    expidlist=['N1850_f19_tn14_20231204_test04']
    refidlist=['N1850_f19_tn14_20231204_test04']
    wlist=[1.,-1.]
#
    varlist=['templvl']
#    
    year0list=[1600] # 16
    year1list=[1603]
    seasonlist=['DEC']

    code='n20231206_ocn'

    loopanalyseoceancolumnintegral2.loopanalyseoceancolumnintegral2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
