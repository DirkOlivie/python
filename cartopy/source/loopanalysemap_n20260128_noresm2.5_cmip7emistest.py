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
    code='n20260128_noresm2.5_cmip7emistest'
    description='varcommon'
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,0.]
    seasonlist = ['YEA']
    varlist    = ['EMI_BC_TOT_noresm2','EMI_OM_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2']
#
    expidlist=['n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6.20260127', \
               'n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv19cmip7.20260127', \
               'n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emine16pg3cmip7.20260127']
    year0list=[ 456, 456, 456]
    year1list=[ 460, 460, 460]
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
