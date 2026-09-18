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
#   Difference
    code='n20260718_navigate_diff'
    figlayout0=cfiglayout.CFigLayout(filetype=filetype,contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(filetype=filetype,contour_levels_type='free'   ,code='free')
    figlayoutlist=[figlayout0,figlayout1]
#
#
    expidlist=['NHIST_f19_tn14_20190710']
#               'NHIST_02_f19_tn14_20190813', \
#               'NHIST_03_f19_tn14_20190813', \
#               \
#               'NHIST_f19_tn14_20250311_test04', \
#               'NHIST_f19_tn14_20250311_test05']
#    
    year0=1950
    year1=1999
#
    refidlist=['N1850_f19_tn14_20190621']
    refyear0=1600
    refyear1=1649
#
    dorefyearaverage=True
#
    wlist=[1.,-1.]
#
    varlist=['AOD_VIS']
#
    typevarlist=['glob'] 
    freqtypelist=['monthlyseries','annualseries']
    seasonlist=['YEA']
    description='varcommon-typecommon'
#
    loopanalysezonalseries2.loopanalysezonalseries2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, seasonlist=seasonlist, freqtypelist=freqtypelist, dorefyearaverage=dorefyearaverage, description=description, code=code,figlayoutlist=figlayoutlist)
#
#   Absolute
    code='n20260718_navigate'
    wlist=[1.,0.]
#    loopanalysezonalseries2.loopanalysezonalseries2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, seasonlist=seasonlist, freqtypelist=freqtypelist, dorefyearaverage=dorefyearaverage, description=description, code=code,figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
