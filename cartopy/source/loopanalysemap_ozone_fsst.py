import loopanalysemap2
import cfiglayout
#
def main():
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')

    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]

    wlist=[1.,-1.]
    year0=11 #16
    year1=11
    seasonlist=['JUL']

    varlist=['CLDTOT','CLDMED','CLDLOW','CLDHGH','SWCF']
    varlist=['SWCF']

#   NorESM2 - no chemistry
    expidlist=['NF1850norbc_f19_20191025']  # full-chemistry
    refidlist=expidlist                       # reference
    year0=1 #16
    year1=1
    seasonlist=['YEA']
    varlist=['OH_surfacelayer','NO3_surfacelayer','O3_surfacelayer','HO2_surfacelayer', \
             'NO3_bef_surfacelayer','NO3_aft_surfacelayer','OH_bef_surfacelayer','OH_aft_surfacelayer']
    wlist=[1.,0.]
#   loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)  
#
# NorESM2 - full chemistry
    expidlist=['NF1850norbc_tropstratchem_f19_20220105_test01']
    expidlist=['NF1850norbc_tropstratchem_f09_20220105_test02', \
               'NF1850norbc_tropstratchem_f19_20220105_test06']  # full-chemistry
    refidlist=expidlist                                          # reference
    year0=11 #16
    year1=20
    seasonlist=['YEA']
    varlist=['OH_surfacelayer','NO3_surfacelayer','O3_surfacelayer','HO2_surfacelayer', \
             'OH_SRF','NO3_SRF','O3_SRF','HO2_SRF']
    varlist=['NO3_SRF','O3_SRF']
    wlist=[1.,0.]
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

#   Reference : how mych variability
    expidlist=['NF1850norbc_f19_20201226']  # full-chemistry
    refidlist=['NF1850norbc_f19_20191025']                       # reference
#   loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
