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

    wlist=[1.,0.]
    year0=1990
    year1=1990
    seasonlist=['YEA']

    varlist=['AOD_VIS','D550_SO4']

#   NorESM2 - no chemistry
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']


    refidlist=expidlist
#    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)  
#
    year0list=[1990,1992]
    year1list=[1990,1992]
    seasonlist=['JUL','YEA']
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
