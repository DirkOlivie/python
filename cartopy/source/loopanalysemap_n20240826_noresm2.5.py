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
    code='n20240826_noresm2.5'
    description=''
#
#   NorESM2.5 and NorES2-MM and NorESM2-LM
#------------------------------------------------------------------
    wlist=[1.,0.]
    seasonlist=['YEA']
    varlist=['EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','SFdst_a123']
#
    year0list=[1,1200,1600,1]
    year1list=[2,1201,1601,2]
    expidlist=['n1850.ne30_tn14.hybrid.20240822','N1850frc2_f09_tn14_20191001','N1850_f19_tn14_20190621','n1850mam4.ne30_tn14.hybrid.clmbgc.20240826']
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
