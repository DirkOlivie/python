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
    code='n20250312_noresm2.5'
    description='varcommon'
#
#   NorESM2.5 and NorES2-MM and NorESM2-LM
#------------------------------------------------------------------
    wlist=[1.,-1.]
    seasonlist=['YEA']
    varlist=['FSLNT']
#
    year0list=[ 2,  2] #1] #, 5, 5]
    year1list=[21, 21] #35] #,30,30]
    expidlist=['nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317','nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250219']#,'NF1850frc2norbc_aer2014_f09_20200108','NF1850norbc_aer2014_f19_20191025']
    refidlist=['nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317'        ,'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250219'        ]#,'NF1850frc2norbc_f09_20200108'        ,'NF1850norbc_f19_20191025']
#
    loopanalysemap2.loopanalysemap2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist, code=code, description=description)
#
if __name__ == '__main__':
    main()
