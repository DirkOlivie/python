import loopanalysezonalmean2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------    
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
#   1. NorESM2 - 1850 : effect of VSLS (0 ppt, 1 ppt, 2 ppt at surface)
#---------------------------------------------------------------
    expidlist=['NF1850norbc_tropstratchem_f19_20220105_test06', \
               'NF1850norbc_tropstratchem_f19_20220105_test09', \
               'NF1850norbc_tropstratchem_f19_20220105_test10']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['BRY_SCALED','CLY_SCALED']
    year0=11
    year1=30
    seasonlist=['YEA']
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

#   2. NorESM2 - historical : effect of VSLS (0 ppt, 1 ppt, 2 ppt at surface)
#---------------------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['BRY_SCALED','CLY_SCALED']
    year0=2000
    year1=2014
    seasonlist=['YEA']
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)


#
if __name__ == '__main__':
    main()
