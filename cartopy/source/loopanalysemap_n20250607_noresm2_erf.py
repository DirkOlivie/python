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
    code='n20250607_noresm2_erf'
    description='varcommon'
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['FSLNT']
#
    expidlist=['NF1850frc2norbc_4xco2_f09_20200108', \
               'NF1850frc2norbc_aer2014_f09_20200108', \
               'NF1850frc2norbc_aeroxid2014_f09_20200108', \
                \
               'NF1850norbc_4xco2_f19_20191025', \
               'NF1850norbc_aer2014_f19_20191025', \
               'NF1850norbc_aeroxid2014_f19_20191025']
    year0list=[ 5, 5, 5, 5, 5, 5]
    year1list=[30,30,30,30,30,30]
    refidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850frc2norbc_f09_20200108', \
               'NF1850frc2norbc_f09_20200108', \
                \
               'NF1850norbc_f19_20191025', \
               'NF1850norbc_f19_20191025', \
               'NF1850norbc_f19_20191025']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
