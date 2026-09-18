import loopanalysezonalseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

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
#
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test01', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test06', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test07', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
#    
    year0=1970 ; year1=2014
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['AOD_VIS']
#
    typevarlist=['glob'] #,'SEA','LAND']
    freqtypelist=['seasonalcycle','monthlyseries','annualseries','seasonalseries']
    freqtypelist=['seasonalseries'] ; seasonlist=['SON']
#    seasonlist=['YEA']                                           # only applies to annualseries (you can pick one month, one season, ...)
#   freqtypelist=['annualseries'] ; seasonlist=['YEA']
    code='keyclim_volc'
    description='varcommon-typecommon'
#
    loopanalysezonalseries2.loopanalysezonalseries2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, year0=year0, year1=year1, seasonlist=seasonlist, freqtypelist=freqtypelist, description=description, code=code,figlayoutlist=figlayoutlist)

if __name__ == '__main__':
    main()
