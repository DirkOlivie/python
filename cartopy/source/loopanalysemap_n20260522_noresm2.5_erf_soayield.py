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
    code='n20260522_noresm2.5_erf_soayield'
    description='varcommon'
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['AODVIS']
#
    expidlist=[ \
            'nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.ref.startup', \
            'nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.all3.startup', \
            'nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.startup', \
            'nf1850_aer2014.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.hygr1p1mode5.startup']
#
    refidlist=[
            'nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.ref.startup', \
            'nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.all3.startup', \
            'nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.startup', \
            'nf1850.ne16pg3_ne16pg3_mtn14.noresm3_0_beta12.Run9.2026-03-11.dust.seasaltdist.hygr1p1mode5.startup']

    nexpid=len(expidlist)        
    year0list=[ 5, 5, 5, 2]
    year1list=[30,30,30,15]
#
    varlist=['direct_ERF_noresm2','cloud_ERF_noresm2','surfalb_ERF_noresm2','FSLNT']     
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
