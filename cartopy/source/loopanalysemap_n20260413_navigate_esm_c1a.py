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
#   C1a minus picontrol
#------------------------------------------------------------------
#
    code='n20260413_navigate_esm_c1a_picontrol'
#
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['PRECT','TREFHT']
#
    expidlist=['N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316']*2
    refidlist=['N1850_f19_tn14_20190730esm']*2
    year0list=[ 1930 ,2030]
    year1list=[ 1949 ,2049]
    seasonlist=['YEA','YEA']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
# SAI (TR, NH, SH) minus B3 : years 1930-1949
#--------------------------------------------
#
    code='n20260413_navigate_esm'
#
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['PRECT','TREFHT']
#
    expidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123a']
    refidlist=['N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316']*6
    year0list=[ 1930,1930,1930,2030,2030,2030 ]
    year1list=[ 1949,1949,1949,2049,2049,2049 ]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
