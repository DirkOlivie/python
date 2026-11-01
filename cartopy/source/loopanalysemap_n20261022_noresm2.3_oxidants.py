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
    code='n20261022_noresm2.3_oxidants'
    description='varcommon'
#
#   Difference
#------------------------------------------------------------------
    wlist      = [1.,0.]
    seasonlist = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    varlist    = ['OH_SRF','HO2_SRF','NO3_SRF','O3_SRF']
#
    expidlist=['NF1850norbc_tropstratchem_f19_f19_t02_20260829']*2
#
    refidlist=expidlist

    nexpid=len(expidlist)        
    year0list=[30,21]
    year1list=[30,30]
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
