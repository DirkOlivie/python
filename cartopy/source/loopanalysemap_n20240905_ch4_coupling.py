import loopanalysemap2
import cfiglayout
#
def main():
#----------    
#
    print('+++ loopanalysemap +++')
    print('--- loopanalysemap ---')
#
    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]
#
    code='n20240905_ch4_coupling'
#
#   STANDARD ERF contribution plots
#----------------------------------
#   piControl 2x2 1600-1609
#   piControl 1x1 1200-1209
#   SSP585    2x2 2091-2100
#   SSP558    1x1 2091-2100
#   N1PCT_f19_tn14_20190712        131-140
#   N1PCTRADfrc2_f19_tn14_20191213 131-140
#   N1PCTBGC_f19_tn14_20190629     131-140

    wlist=[1.,0.]
    seasonlist=['YEA']
    varlist=['FCH4']
#
    year0list=[1600,1200,2091,2091,131,131,131]
    year1list=[1609,1209,2100,2100,140,140,140]
    expidlist=['N1850_f19_tn14_20190621','N1850frc2_f09_tn14_20191001','NSSP585frc2_f19_tn14_20191014','NSSP585frc2_f09_tn14_20191105','N1PCT_f19_tn14_20190712','N1PCTRADfrc2_f19_tn14_20191213','N1PCTBGC_f19_tn14_20190629']
    refidlist=expidlist
    description='varcommon'
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
