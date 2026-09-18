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
#   1. NorESM2 - impact on heterogeneous reactions / aerosols
#------------------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO']
    varlist=['REFF_AERO']

    seasonlist=['YEA']
#    
    year0=1990 
    year1=1999
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
    year0=1990
    year1=1990
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
# 
    year0=1992
    year1=1992
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   2. NorESM2 - impact on ozone
#-------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14']
    refidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16']
    wlist=[1.,-1.]
#
    varlist=['O3']
#   varlist=['mmr_SULFATE']

    seasonlist=['YEA']
#    
    year0=1990 
    year1=1999
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
    year0=1990
    year1=1990
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
# 
    year0=1991
    year1=1995
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   3. NorESM2 - impact on ozone : 1992 versus 1990
#--------------------------------------------------
    expidlist=[ \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
#               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
#               'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test19', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test21', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test25' \
#               'FCHIST_f19_mg17_20220111_test1', \
#               'FCHIST_f19_mg17_20220111_test6', \
#               'FCHIST_f09_mg17_20220111_test7'
                 ]
    refidlist=expidlist
#
    wlist=[1.,-1.]
#
    varlist=['O3']
#   varlist=['mmr_SULFATE']
#    varlist=['SAD_AERO']

    seasonlist=['YEA']
#  
#   Absolute
#   Pinatubo
    year0=1990
    year1=1990
#   wlist=[1.,0.]
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

    year0=1992
    year1=1992
#   wlist=[1.,0.]
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)

#   Differences
#   Pinatubo
    year0=1992
    year1=1992
    refyear0=1990
    refyear1=1990
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   El Chichon
    year0=1983
    year1=1983
    refyear0=1981
    refyear1=1981
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)    
#
#   4. CESM2 - impact on ozone : FC2010
#--------------------------------------
#   FC2010climo_prep_f19_20210204_test5  : +/- reference
#   FC2010climo_prep_f19_20210204_test11 : +/- no volcanic SO2/SO4 emissions
#   FC2010climo_prep_f19_20210204_test13 : no volcanic SO2/SO4 emissions, no OCS


    expidlist=['FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test5']
    refidlist=['FC2010climo_prep_f19_20210204_test11', \
               'FC2010climo_prep_f19_20210204_test13', \
               'FC2010climo_prep_f19_20210204_test17']
    wlist=[1.,-1.]
#
    varlist=['O3']

    seasonlist=['YEA']
#   
#   Pinatubo
    year0=6
    year1=10
    refyear0=6
    refyear1=10
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, refyear0=refyear0, refyear1=refyear1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)    
#
if __name__ == '__main__':
    main()
