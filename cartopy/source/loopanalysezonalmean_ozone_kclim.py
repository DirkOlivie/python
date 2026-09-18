import loopanalysezonalmean2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
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
#   1. NorESM2 : effect of no volc SO2, effect of no OCS
#-------------------------------------------------------
    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test11', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test12']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['mmr_SULFATE']
    year0=6
    year1=10
    seasonlist=['YEA']
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   2. CESM : effect of no volc SO2, effect of no OCS
#----------------------------------------------------
    expidlist=['FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test11', \
               'FC2010climo_prep_f19_20210204_test13', \
               'FC2010climo_prep_f19_20210204_test16']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['so4_a123']
    year0=6
    year1=10
    seasonlist=['YEA']
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   3. NorESM2 : effect of Pinatubo (before / after)
#---------------------------------------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['NMR01','NMR05','SO4_NA','SO4_A1','mmr_SULFATE']
    varlist=['SO4_PR','SO4_AC']
    seasonlist=['YEA']
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=1989, year1=1989, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=1992, year1=1992, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   4. CESM2 : effect of Pinatubo (before / after)
#-------------------------------------------------
    expidlist=['FCHIST_f19_mg17_20220111_test6']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['dgnum1','dgnum2','dgnum3','dgnum4','dgnumwet1','dgnumwet2','dgnumwet3','dgnumwet4']
    varlist=['rgnum1','rgnum2','rgnum3','rgnum4','rgnumwet1','rgnumwet2','rgnumwet3','rgnumwet4']
    varlist=['so4_a123','so4_a1','so4_a2','so4_a3']
    seasonlist=['YEA']
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=1989, year1=1989, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#   loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=1992, year1=1992, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
#   5. NorESM2 : ozone
#---------------------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'FCHIST_f19_mg17_20220111_test6', \
               'FCHIST_f09_mg17_20220111_test7']
    refidlist=expidlist
    wlist=[1.,0.]
#
    varlist=['O3']
    seasonlist=['YEA']
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, year0=2000, year1=2009, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
if __name__ == '__main__':
    main()
