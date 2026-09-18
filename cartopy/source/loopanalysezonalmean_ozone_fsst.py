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
#   NorESM2 - no chemistry
    expidlist=['NF1850norbc_f19_20191025']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['OH','NO3','HO2','O3', \
             'NO3_bef','NO3_aft','OH_bef','OH_aft']
    varlist=['NO3']
    year0=1
    year1=1
    seasonlist=['YEA']
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   NorESM2 - full chemistry
    expidlist=['NF1850norbc_tropstratchem_f19_20220105_test01', \
               'NF1850norbc_tropstratchem_f09_20220105_test02', \
               'NF1850norbc_tropstratchem_f19_20220105_test06']                 
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['OH','NO3','HO2','O3']
    year0=11
    year1=20
    seasonlist=['YEA']
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   Difference
    expidlist=['NF1850norbc_tropstratchem_f19_20220105_test01']
    refidlist=['NF1850norbc_f19_20191025len30']
#
    varlist=['T','CLOUD','CLOUDFRAC_CLUBB']#,'CLOUDCOVER_CLUBB']
    varlist=['CONCLD']
    year0=11
    year1=20
    seasonlist=['YEA'] 
#
    wlist=[1.,-1.]
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist) 
#
if __name__ == '__main__':
    main()
