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
    description='varcommon'
#
#   piControl - reference - absolute
#------------------------------------------------------------------
#
    code='n20251203_navigate_esm_picontrol'
#
    wlist      = [1.,0.]
    seasonlist = ['YEA']
    varlist    = ['PRECT']
#
    expidlist=['N1850_f19_tn14_20190730esm']
    refidlist=expidlist
    year0list=[ 1850 ]
    year1list=[ 1879 ]
    seasonlist=['YEA']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
#   B3 minus picontrol
#------------------------------------------------------------------
#
    code='n20251203_navigate_esm_B3_picontrol'
#
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['PRECT']
#
    expidlist=['N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316']
    refidlist=['N1850_f19_tn14_20190730esm']
    year0list=[ 1930 ]
    year1list=[ 1949 ]
    seasonlist=['YEA']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
# SAI (TR, NH, SH) minus B3
#------------------------------------
#
    code='n20251203_navigate_esm'
#
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['PRECT']
#
    expidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens123']
    refidlist=['N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316']*3
    year0list=[ 1930 ]*3
    year1list=[ 1949 ]*3
    seasonlist=['YEA']*3
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
