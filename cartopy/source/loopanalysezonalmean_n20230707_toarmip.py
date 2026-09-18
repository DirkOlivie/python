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
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim01']
#               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['O3']

    seasonlist=['YEA']
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
#    
    code='n20230707_toarmip'

    year0=16
    year1=30
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)

    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['ozone']

    seasonlist=['YEA']
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
#    
    code='n20230707_toarmip'

    year0=16
    year1=30
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)

#   Evolution O3 first 10 years 
#--------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01'] 
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['O3']

    seasonlist=['YEA']
#    
    code='n20230707_toarmip'

    year0=1 ; year1=1
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
    year0=2 ; year1=2
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
    year0=3 ; year1=3
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
    year0=4 ; year1=4
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
    year0=5 ; year1=5
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
