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
#   N1850
#--------------------------------------------------------------
    expidlist=['N1850_f19_tn14_20190621']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0=1600
    year1=1609
    seasonlist=['YEA']
#
    varlist=['BVISVOLC']
#
    code='n20251026_volc'
#
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
#   N1850
#--------------------------------------------------------------
    expidlist=['NHIST_f19_tn14_20190625ext']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0=1850
    year1=2014
    seasonlist=['YEA']
#
    varlist=['BVISVOLC']
#
    code='n20251026_volc'
#
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)



if __name__ == '__main__':
    main()
