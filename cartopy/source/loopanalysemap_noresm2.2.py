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

#   CESM2 - full chemistry
#   expidlist=['FC2010climo_f19_20210204_test1']
    expidlist=['NF1850norbc_f19_f19_20210530', \
               'NF1850norbc_f19_f19_20211013', \
               'NF1850norbc_f19_20211113_test17']
    varlist=['SFisoprene','SFmonoterp']
    year0=11 #16
    year1=20
    seasonlist=['YEA']
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
