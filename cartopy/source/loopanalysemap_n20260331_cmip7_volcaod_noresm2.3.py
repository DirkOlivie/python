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
    code='n20260331_cmip7_volcaod_noresm2.3'
    description='varcommon'
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['FSLNT','FSLNTC','FSDS','FSDSC']
#
    expidlist=[ \
               'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip6', \
               'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7', \
               'NF1850norbc_sdyn_f19_f19_20260330_test16_volccmip7wghtavg']
    refidlist=[ \
               'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
               'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone', \
               'NF1850norbc_sdyn_f19_f19_20260330_test16_volcnone']
#
    year0list=[ 1970,1970,1970]
    year1list=[ 1979,1979,1979]
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
