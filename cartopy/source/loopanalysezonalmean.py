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

#   CESM2 - full chemistry
    expidlist=['FC2010climo_prep_f19_20210204_test5', \
               'FC2010climo_prep_f19_20210204_test11', \
               'FC2010climo_prep_f19_20210204_test12',\
               'FC2010climo_prep_f19_20210204_test13']
#   expidlist=['FC2010climo_prep_f19_20210204_test5', \
#              'FC2010climo_prep_f19_20210204_test7']
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP']#['SO2']#['so4_a123']#['OCS','SO2']#['O3']#['SO2','NO2','CO','O3','CH4']#['O3']#,'NO2','T']
    varlist=['SAD_AERO','SAD_TROP']
    varlist=['SAD_SULFC']
    varlist=['SAD_ICE','SAD_LNAT','REFF_AERO']
    varlist=['REFF_AERO']
    varlist=['OH','O1D']
    varlist=['O3']
    varlist=['so4_a123']
    varlist=['OCS','SO2']
    varlist=['NH3','NH4']
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP']
    varlist=['SAD_AERO']
    varlist=['so4_a1','so4_a2','so4_a3','so4_a123','H2SO4']
    varlist=['O3','SO2','NO','NO2','CO','N2O5','CH4','OH', \
             'SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO', \
             'so4_a123','H2SO4']
    varlist=['SAD_AERO','SAD_SULFC']
#    varlist=['H2SO4','SO2','OCS']
#    varlist=['SO2']
#    varlist=['NH3','NH4']
#    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO']
#    varlist=['H2SO4M_C']
#    varlist=['H2SO4']
#    varlist=['RAD_ICE','RAD_LNAT','RAD_SULFC']
#    varlist=['HNO3_GAS','HNO3_STS','HNO3_NAT']
#    varlist=['dgnumwet1','dgnumwet2','dgnumwet3']
#    varlist=['O3']
#    varlist=['SO2','NO2','CO','N2O5','CH4']
#    varlist=['OH']
    year0=6#6
    year1=10
#   seasonlist=['YEA','DJF','MAM','JJA','SON']
    seasonlist=['YEA']
#   seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=1, year1=1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=2, year1=2, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=3, year1=3, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=4, year1=4, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=5, year1=5, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=6, year1=6, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=7, year1=7, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=8, year1=8, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=9, year1=9, seasonlist=seasonlist, figlayout=figlayout0#)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=10,year1=10, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)
#
#   NorESM2 - test
    expidlist=['NF1850norbc_tropstratchem_f19_20210331_test14']
    varlist=['O3']#,'NO2','T']
    year0=20#16
    year1=20
    seasonlist=['YEA']#'JJA','DJF','YEA']
#   loopanalysezonalmean2.loopanalysezonalmean2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#
#   NorESM2 - test
    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test01', \
               'NF1850norbc_tropstratchem_f19_20210517_test02', \
               'NF1850norbc_tropstratchem_f19_20210517_test03', \
               'NF1850norbc_tropstratchem_f19_20210517_test04', \
               'NF1850norbc_tropstratchem_f19_20210517_test05', \
               'NF1850norbc_tropstratchem_f19_20210517_test06', \
               'NF1850norbc_tropstratchem_f19_20210517_test08', \
               'NF1850norbc_tropstratchem_f19_20210517_test09']
    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test08', \
               'NF1850norbc_tropstratchem_f19_20210517_test09']
    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test10'] 
    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test11'] 
    expidlist=['NF1850norbc_tropstratchem_f19_20210517_test12'] 
#   expidlist=['NF1850norbc_tropstratchem_f19_20210517_test01', \
#              'NF1850norbc_tropstratchem_f19_20210517_test05', \
#              'NF1850norbc_tropstratchem_f19_20210517_test09'] 
    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test06', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test07']
    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test09', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test10', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test13', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test14', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test15', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test16']
    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test17', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test18']
    expidlist=['NF2010norpddmsbc_tropstratchem_f19_20210517_test11', \
               'NF2010norpddmsbc_tropstratchem_f19_20210517_test12']
    varlist=['O3']#['SO2']#,'mmr_SULFATE']#['OCS','SO2']#['O3']#['N2O5']#['NO2','SO2','NO2','CO','O3','CH4']#,'NO2','T']
    varlist=['SO2','NO2','CO','N2O5','CH4']
    varlist=['CO']
    varlist=['OH']
    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP']
    varlist=['SAD_AERO','SAD_TROP']   
    varlist=['SAD_SULFC']
    varlist=['SAD_ICE','SAD_LNAT','REFF_AERO']
    varlist=['REFF_AERO']
    varlist=['O3','SO2','NO','NO2','CO','N2O5','CH4','OH',\
             'SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO', \
             'mmr_SULFATE','H2SO4']
    varlist=['mmr_SULFATE']
    varlist=['SAD_AERO','SAD_SULFC']
#    varlist=['OH','O1D']
#    varlist=['O3']
#    varlist=['mmr_SULFATE']
#    varlist=['OCS','SO2']
#    varlist=['SAD_AERO']#,'mmr_SULFATE','SO2']
#    varlist=['H2SO4','SO2','OCS']
#    varlist=['mmr_SULFATE','H2SO4']
#    varlist=['SAD_AERO','SAD_ICE','SAD_LNAT','SAD_SULFC','SAD_TROP','REFF_AERO']
#    varlist=['H2SO4M_C']
#    varlist=['H2SO4']
#    varlist=['SO2']
    year0=6
    year1=10
#   seasonlist=['YEA','DJF','MAM','JJA','SON']
    seasonlist=['YEA']
#    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=1, year1=1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=2, year1=2, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=3, year1=3, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=4, year1=4, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=5, year1=5, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=6, year1=6, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=7, year1=7, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=8, year1=8, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=9, year1=9, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=10,year1=10, seasonlist=seasonlist, figlayout=figlayout0)


    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysezonalmean2.loopanalysezonalmean2(expidlist=expidlist, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)

#   Historical simulation
    expidlist=['NHIST_f19_tn14_20190710']
    varlist=['ozone']
    year0=2008
    year1=2012
    seasonlist=['DJF','MAM','JJA','SON','YEA']
#    loopanalysezonalmean2.loopanalysezonalmean2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#   loopanalysezonalmean2.loopanalysezonalmean2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)
#
if __name__ == '__main__':
    main()
