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
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['SOA_SV','SOA_LV']
    varlist=['DMS','SO2']
#
    seasonlist=['YEA']
#    
    code='n20250407_noresm2.5'
#
    year0=5
    year1=7
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=year0, refyear1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code)
#
if __name__ == '__main__':
    main()
