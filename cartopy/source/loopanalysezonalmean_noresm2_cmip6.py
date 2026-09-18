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
#   NorESM2 - cmip6
#   2x2
    expidlist=['NF1850norbc_f19_20191025']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['NO3_bef','NO3_aft','OH_bef','OH_aft']
    varlist=['NO3','OH','O3','HO2']
    year0=1
    year1=1
    seasonlist=['YEA']
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   NorESM2 - cmip6
#   2x2
    expidlist=['N1850_f19_tn14_20190621']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['NO3_bef','NO3_aft','OH_bef','OH_aft']
    year0=1600
    year1=1609
    seasonlist=['YEA']
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   1x1
    expidlist=['N1850frc2_f09_tn14_20191001']
    refidlist=expidlist
    year0=1200
    year1=1209
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   NorESM2 - full chemistry
    expidlist=['N1850_tropstratchem_prep_f19_nt14_20211217_test03','N1850_tropstratchem_prep_f09_nt14_20211217_test04']
    refidlist=expidlist
    varlist=['NO3','OH','O3']
    year0=11
    year1=20
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
