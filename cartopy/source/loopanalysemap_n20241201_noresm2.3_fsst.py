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
    code='n20241201_noresm2.3_fsst'
    description='yearcommon-varcommon'
#
#   NorESM2 -> NorESM2.3 


#   standard N1850 background state
#------------------------------------------------------------------
    wlist=[1.,0.]
    seasonlist=['YEA']
    varlist=['CDNUMC','cb_SOA_A1']
    varlist=['cb_SOA_A1']
#
    year0list=[5]
    year1list=[30]
    expidlist=['NF1850norbc_f19_20191025'        ] #,'NF1850norbc_f19_f19_20231204_test17'        ,'NF1850norbc_f19_f19_20241127_test01'        ,'NF1850norbc_f19_f19_20241127_test05'        ,'NF1850norbc_f19_f19_20241127_test06'        ]
    refidlist=expidlist
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
#   NorESM2 -> NorESM2.3 : impact of anthropogenic aerosol
#------------------------------------------------------------------
    wlist=[1.,-1]
    seasonlist=['YEA']
    varlist=['FSLNT']
    varlist=['CDNUMC']
#
    year0list=[5]
    year1list=[30]
    expidlist=['NF1850norbc_aer2014_f19_20191025','NF1850norbc_aer2014_f19_f19_20231204_test17','NF1850norbc_aer2014_f19_f19_20241127_test01','NF1850norbc_aer2014_f19_f19_20241127_test05','NF1850norbc_aer2014_f19_f19_20241127_test06']
    refidlist=['NF1850norbc_f19_20191025'        ,'NF1850norbc_f19_f19_20231204_test17'        ,'NF1850norbc_f19_f19_20241127_test01'        ,'NF1850norbc_f19_f19_20241127_test05'        ,'NF1850norbc_f19_f19_20241127_test06'        ]
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
