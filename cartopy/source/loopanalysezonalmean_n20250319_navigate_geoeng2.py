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
#   O3 years 16-30
#--------------------------------------------------------------
    expidlist=['N1850_f19_tn14_20190621', \
               'N1850_f19_tn14_20250311_test01', \
               'N1850_f19_tn14_20250311_test05_20km', \
               'N1850_f19_tn14_20250311_test05', \
               'N1850_f19_tn14_20250311_test05_26km', \
               'N1850_f19_tn14_20250311_test05_15n60n', \
               'N1850_f19_tn14_20250311_test05_60s15s']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0=1615
    year1=1619
    seasonlist=['YEA']
#
    varlist=['SO2_as_concentration', \
             'mmr_SULFATE_as_concentration']
#
    code='n20250319_navigate_geoeng2'
#
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
