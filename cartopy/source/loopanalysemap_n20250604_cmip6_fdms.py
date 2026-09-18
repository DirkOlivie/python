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
    code='n20250604_cmip6_fdms'
    description='varcommon'
#
#   Absoloute
#------------------------------------------------------------------
    wlist      = [1.,0.]
    seasonlist = ['YEA']
    varlist    = ['SFDMS','U10']
#
    year0list=[1751,  1, 1]
    year1list=[1780, 30,30]
    expidlist=['N1850_f19_tn14_20190621','NF1850norbc_f19_20191025','NF1850norbc_f19_20200303']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['SFDMS','U10']
#
    expidlist=['NF1850norbc_f19_20191025','NF1850norbc_f19_20200303']
    year0list=[ 1, 1]
    year1list=[30,30]
    refidlist=['N1850_f19_tn14_20190621','N1850_f19_tn14_20190621']
    refyear0list=[1751,1751]
    refyear1list=[1780,1780]
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description, refyear0list=refyear0list, refyear1list=refyear1list)
#
if __name__ == '__main__':
    main()
