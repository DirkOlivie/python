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
    code='n20230801_keyclim_wp6'
#
#   STANDARD ERF contribution plots (Stephanies manuscript)
#----------------------------------
    wlist=[1.,0.]
    seasonlist=['YEA']
    varlist=['BC_AC_OCWclcoagTend']
#
    year0list=[2010]
    year1list=[2014]
    expidlist=['NHISTfrc2_f09_tn14_20200718', \
               'NHISTpiaeroxid_f09_tn14_keyClim20201217', \
               'NHISTfrc2_histeddy2_KeyCLim', \
               'NHISTfrc2G_f09_tn14_gl4_SMB1_celo', \
               'NHISTfrc2_f09_tn14_cloudxpice_220629', \
               'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
               'NHIST_hist_snow_KeyClim']

    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
