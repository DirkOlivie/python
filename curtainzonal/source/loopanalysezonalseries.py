import loopanalysezonalseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

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
#
    expidlist=['FCHIST_f19_mg17_20220111_test6', \
               'FCHIST_f09_mg17_20220111_test7', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
               'NFHISTnorbc_f19_20191107']                             
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']   
    year0=1970 ; year1=2014
#   expidlist=['NF1850norbc_f19_20191025len30'] ; year0=1 ; year1=30
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['cb_O3']
#
    typevarlist=['glob'] #,'SEA','LAND']
    freqtypelist=['seasonalcycle','monthlyseries','annualseries','seasonalseries']
    freqtypelist=['seasonalseries'] ; seasonlist=['SON']
#    seasonlist=['YEA']                                           # only applies to annualseries (you can pick one month, one season, ...)
#   freqtypelist=['annualseries'] ; seasonlist=['YEA']
    code='trial_ozone_fsst_hist'
    description='varcommon-typecommon'
#
    loopanalysezonalseries2.loopanalysezonalseries2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, year0=year0, year1=year1, seasonlist=seasonlist, freqtypelist=freqtypelist, description=description, code=code,figlayoutlist=figlayoutlist)

if __name__ == '__main__':
    main()
