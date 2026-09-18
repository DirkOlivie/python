import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard')
#
# Q,  O3  and H2O profiles - mean over year 21-30
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[31,31,31]
    year1list=[40,40,40]
    seasonlist=['YEA','YEA','YEA']
    legendlist=['(1a)','(2a)','(3a)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240418_toarmip'
#
#   variables
    varlist=['Q','O3','O3_as_partpress','H2O']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#

# O3, NO2 and NO2CHEM profiles - seperate for year 1, 2, 3, 4, 5 and 10 
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1,2,3,4,5,10]
    year1list=[1,2,3,4,5,10]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['(year 1)','(year 2)','(year 3)','(year 4)','(year 5)','(year 10)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240418_toarmip_spinup'
#
#   variables
    varlist=['O3','NO2','N2OCHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
# CO2, CH4, N2O, CFC11, CFC12 profiles
#--------------------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[31,31,31,31,31,31]
    year1list=[40,40,40,40,40,40]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['rad (1a)','chem (1a)','rad (2a)','chem (2a)','rad (3a)','chem (3a)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20240418_toarmip'
#
#   CO2
    varlist=['m_CO2_c_as_vmr','CO2CHEM','m_CO2_c_as_vmr','CO2CHEM','m_CO2_c_as_vmr','CO2CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#   CH4
    varlist=['m_CH4_c_as_vmr','CH4CHEM','m_CH4_c_as_vmr','CH4CHEM','m_CH4_c_as_vmr','CH4CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#   N2O
    varlist=['m_N2O_c_as_vmr','N2OCHEM','m_N2O_c_as_vmr','N2OCHEM','m_N2O_c_as_vmr','N2OCHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
    varlist=['m_CFC11_c_as_vmr','CFC11CHEM','m_CFC11_c_as_vmr','CFC11CHEM','m_CFC11_c_as_vmr','CFC11CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
    varlist=['m_CFC12_c_as_vmr','CFC12CHEM','m_CFC12_c_as_vmr','CFC12CHEM','m_CFC12_c_as_vmr','CFC12CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)


# O3 profiles - mean over year 21-40
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01', \
                \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[21,21,21,21,21,21]
    year1list=[40,40,40,40,40,40]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['(1a)','(2a)','(3a)','(1b)','(2b)','(2c)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20240418_toarmip_rad'
#
#   variables
    varlist=['O3','O3','O3','ozone','ozone','ozone']
    varlist=['O3_as_partpress','O3_as_partpress','O3_as_partpress','ozone_as_partpress','ozone_as_partpress','ozone_as_partpress']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#


# O3 profiles - why is climatology different from average
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[21,21,21]
    year1list=[40,40,40]
#    year0list=[22,22]
#    year1list=[22,22]
#   year1list=[40,40,40]
#    seasonlist=['OCT','OCT']#,'OCT','OCT']
    seasonlist=['YEA','YEA','YEA']
    legendlist=['(1a h0)','(1b int.)','(1b ext.)']#,'(1b, 21)','(1b, 22)']
    regionlist=['90S28S','glob']
    verticalaxislist=['height']#,'pressure']
#
#   description
    description=''
    code='n20240418_toarmip_radclim'
#
#   variables
    varlist=['O3_as_partpress','O3_as_partpress','O3_as_partpress','O3_as_partpress']#
#    varlist=['ozone_extclim','ozone_extclim']
#    varlist=['ozone','ozone']
#    varlist=['ozone','ozone']
    varlist=['O3_as_partpress','ozone_as_partpress','ozone_extclim_as_partpress']#,'ozone_as_partpress']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
# O3 profiles - why is climatology different from average
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5]
    year1list=[5,5,5]
    seasonlist=['OCT','OCT','OCT']
    legendlist=['ozone_extclim_as_partpress','ozone_as_partpress','m_ozone_c_as_vmr_as_partpress']
    regionlist=['90S28S']#,'28S28N','28N60N','60N90N','glob']
    regionlist=['INSITULON0LAT-10','INSITULON0LAT-20','INSITULON0LAT-30','INSITULON0LAT-40','INSITULON0LAT-50','INSITULON0LAT-60','INSITULON0LAT-70','INSITULON0LAT-80']
    regionlist=['INSITULON0LAT0','INSITULON30LAT0','INSITULON60LAT0','INSITULON90LAT0','INSITULON120LAT0','INSITULON150LAT0','INSITULON180LAT0','INSITULON210LAT0']
#    regionlist=['INSITULON0LAT0']
#   regionlist=['SEA','LAND']
    verticalaxislist=['height']#,'pressure']
#
#   description
    description=''
    code='n20240418_toarmip_radclim_test'
#
#   variables
#    varlist=['O3_as_partpress','O3_as_partpress','O3_as_partpress','O3_as_partpress']#
    varlist=['ozone_as_partpress']#,
    varlist=['ozone_extclim_as_partpress']
    varlist=['ozone_extclim_as_partpress','ozone_as_partpress','m_ozone_c_as_vmr_as_partpress']
#    varlist=['T','T','T']
#    varlist=['ozone','ozone']
#    varlist=['ozone','ozone']
#    varlist=['ozone_as_partpress','ozone_as_partpress','ozone_as_partpress','ozone_extclim_as_partpress','ozone_extclim_as_partpress','ozone_extclim_as_partpress']#,'ozone_as_partpress']
#    varlist=['ozone','ozone','ozone','ozone_extclim','ozone_extclim','ozone_extclim']#,'ozone_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

    seasonlist=['SEP','SEP','SEP']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

    seasonlist=['NOV','NOV','NOV']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

    seasonlist=['JUL','JUL','JUL']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

    seasonlist=['MAR','MAR','MAR']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

# O3 profiles - why is climatology different from average
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[21,21]
    year1list=[21,21]
    seasonlist=['OCT','OCT']
    legendlist=seasonlist
    regionlist=['90S28S','glob']
    verticalaxislist=['height']#,'pressure']
#
#   description
    description=''
    code='n20240418_toarmip_radclim_test2'
#
#   variables
#    varlist=['O3_as_partpress','O3_as_partpress','O3_as_partpress','O3_as_partpress']#
#    varlist=['ozone_extclim','ozone_extclim']
#    varlist=['ozone','ozone']
#    varlist=['O3','m_O3_c_as_vmr']
    varlist=['O3_as_partpress','m_O3_c_as_vmr_as_partpress']
#    varlist=['ozone_as_partpress','ozone_as_partpress','ozone_as_partpress','ozone_extclim_as_partpress','ozone_extclim_as_partpress','ozone_extclim_as_partpress']#,'ozone_as_partpress']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
if __name__ == '__main__':
    main()
