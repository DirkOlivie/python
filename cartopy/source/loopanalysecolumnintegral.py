import loopanalysecolumnintegral2
import cfiglayout
#
def main():
#
    print('+++ loopanalysecolumnintegral +++')
    print('--- loopanalysecolumnintegral ---')

    figlayout0=cfiglayout.CFigLayout(contour_levels_type='imposed',code='imposed')
    figlayout1=cfiglayout.CFigLayout(contour_levels_type='free',code='free')
    figlayoutlist=[figlayout0,figlayout1]

#   CESM2 - full chemistry
    expid='FC2010climo_f19_20210204_test1'
    varlist=['O3']#,'NO2','T']
    year0=20 #16
    year1=20
#   seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']#'JJA','DJF','YEA']
    seasonlist=['DJF','MAM','JJA','SON']
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)
#
#   NorESM2 - test
    expid='NF1850norbc_tropstratchem_f19_20210517_test01'
    varlist=['O3']
    year0=20 # 16
    year1=20
#   seasonlist=['JUL','AUG','SEP','OCT']#''YEA']#'JJA','DJF','YEA']
    seasonlist=['DJF','MAM','JJA','SON']
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)

#   NorESM2 - NHIST
    expid='NHIST_f19_tn14_20190710'
    varlist=['ozone']
    varlist=['AOD_VIS']
    year0=2008 # 16
    year1=2012
#   seasonlist=['JUL','AUG','SEP','OCT']#''YEA']#'JJA','DJF','YEA']
    seasonlist=['DJF','MAM','JJA','SON']
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout0)
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expid=expid, varlist=varlist, year0=year0, year1=year1, seasonlist=seasonlist, figlayout=figlayout1)

#   COLCANOES
    expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
               'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
#
    varlist=['EXT_MODE01_AeroTab_NCONC_RELHUM', \
             'EXT_MODE01_AeroTab_NCONC', \
             'EXT_MODE05_AeroTab_NCONC_RELHUM', \
             'EXT_MODE05_AeroTab_NCONC']
#
    varlist=['EXT_MODE05_AeroTab_NCONC_SPEHUM']
    varlist=['EXT_MODE01_AeroTab_NCONC_SPEHUM']
    varlist=['NCONC01','VCONC01','NCONC05','VCONC05']
#    
    year0list=[1990,1992] # 16
    year1list=[1990,1992]
#   seasonlist=['JUL','AUG','SEP','OCT']#''YEA']#'JJA','DJF','YEA']
    seasonlist=['DJF','MAM','JJA','SON']
    seasonlist=['JUL']
#    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expidlist=expidlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
# 2023-10-26 - MARIANA
    expidlist=['NF2000oslo.f19_f19_mtn14.2', \
               'NF2000oslo.f19_f19_mtn14.3']
#
    varlist=['CCN1','CCN2','CCN3','CCN4','CCN5','CCN6','CCN7','N_AER']
    varlist=['CCN5','N_AER']
#    
    year0list=[3,3] # 16
    year1list=[5,5]
    seasonlist=['YEA']
    loopanalysecolumnintegral2.loopanalysecolumnintegral2(expidlist=expidlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist)
#
# 2023-10-26 - 
    expidlist=['NHISTfrc2_f09_tn14_20200718', \
               'NHISTpiaeroxid_f09_tn14_keyClim20201217', \
               'NHISTfrc2_histeddy2_KeyCLim', \
               'NHISTfrc2G_f09_tn14_gl4_SMB1_celo', \
               'NHISTfrc2_f09_tn14_cloudxpice_220629', \
               'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
               'NHIST_hist_snow_KeyClim']

    varlist=['CCN1','CCN2','CCN3','CCN4','CCN5','CCN6','CCN7','N_AER']
#    
    year0list=[2010,2010,2010,2010,2010,2010,2010] # 16
    year1list=[2014,2014,2014,2014,2014,2014,2014]
    seasonlist=['YEA']
#   loopanalysecolumnintegral2.loopanalysecolumnintegral2(expidlist=expidlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, figlayoutlist=figlayoutlist)


#
if __name__ == '__main__':
    main()
