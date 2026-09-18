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
    code='n20260522_noresm2.5_hist_soayield'
    description='varcommon'
#
#   Individual
#------------------------------------------------------------------
    wlist      = [1.,0.]
    seasonlist = ['YEA']
    varlist    = ['AODVIS']
#
    expidlist=['nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2allmodes', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p1', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p2', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayieldx2', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1mode5', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p05mode5']
#
    nexpid=len(expidlist)
    year0list=[ 2000]*nexpid
    year1list=[ 2009]*nexpid
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,-1.]
    seasonlist = ['YEA']
    varlist    = ['AODVIS']
#
    expidlist=['nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2allmodes', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p1', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p2', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayieldx2', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1mode5', \
               'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p05mode5']

    nexpid=len(expidlist)        
    refidlist=['nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist']*nexpid
    year0list=[ 2000]*nexpid
    year1list=[ 2009]*nexpid
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
