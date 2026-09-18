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
    code='n20240822_camsvsls'
#
#   U10, SFDMS, SFCHBR3 : simulation with bromoform
#------------------------------------------------------------------
    wlist=[1.,0.]
    seasonlist=['DJF','MAM','JJA','SON']
    varlist=['U10','SFDMS','SFCHBR3']
#
    year0list=[1995]
    year1list=[2004]
    expidlist=['NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
#
#   U10, SFDMS : simulations withlout bromoform
#------------------------------------------------------------------
    wlist=[1.,0.]
    seasonlist=['DJF','MAM','JJA','SON']
    varlist=['U10','SFDMS']
#
    year0list=[1995]
    year1list=[2004]
    expidlist=['NHIST_f19_tn14_20190710', \
               'NHISTfrc2_f09_tn14_20191025']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
