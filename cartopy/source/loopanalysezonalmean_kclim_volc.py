import loopanalysezonalmean2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalysezonalmean +++')
    print('--- loopanalysezonalmean ---')
#
    filetype='ps'
#
    figlayout0=cfiglayout.CFigLayout(filetype=filetype,contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(filetype=filetype,contour_levels_type='free'   ,code='free'   )
    figlayoutlist=[figlayout0,figlayout1]
#
#   1. NorESM2 : effect of no volc SO2, effect of no OCS
#-------------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['NMR01','NMR05','SO4_NA','SO4_A1','mmr_SULFATE','SO4_PR','SO4_AC','NCONC01','NCONC05','VCONC01','VCONC05']
    year0=1992
    year1=1992
    seasonlist=['JUL']

    print('hallo')

    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

if __name__ == '__main__':
    main()
