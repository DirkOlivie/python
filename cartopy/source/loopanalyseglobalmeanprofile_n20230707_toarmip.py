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
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[21,21]
    year1list=[30,30]
    seasonlist=['YEA','YEA']
    legendlist=['(ref 2015)','(pert 2050)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20230707_toarmip'
#
#   variables
    varlist=['Q','O3','H2O']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#

# O3, NO2 and NO2CHEM profiles - seperate for year 1, 2, 3, 4, 5 and 10 
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01']
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
    code='n20230707_toarmip_spinup'
#
#   variables
    varlist=['O3','NO2','N2OCHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
# CO2, CH4, N2O, CFC11, CFC12 profiles
#--------------------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_20230605_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[21,21,21,21]
    year1list=[30,30,30,30]
    seasonlist=['YEA','YEA','YEA','YEA']
    legendlist=['rad (ref 2015)','chem (ref 2015)','rad (pert 2050)','chem (pert 2050)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20230707_toarmip'
#
#   CO2
    varlist=['m_CO2_c_as_vmr','CO2CHEM','m_CO2_c_as_vmr','CO2CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#   CH4
    varlist=['m_CH4_c_as_vmr','CH4CHEM','m_CH4_c_as_vmr','CH4CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#   N2O
    varlist=['m_N2O_c_as_vmr','N2OCHEM','m_N2O_c_as_vmr','N2OCHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
    varlist=['m_CFC11_c_as_vmr','CFC11CHEM','m_CFC11_c_as_vmr','CFC11CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
    varlist=['m_CFC12_c_as_vmr','CFC12CHEM','m_CFC12_c_as_vmr','CFC12CHEM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)


# O3 profiles - mean over year 16-30
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20230605_sim02']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[16,16]
    year1list=[30,30]
    seasonlist=['YEA','YEA']
    legendlist=['(ref 2015)','(ref 2050) + clim. O3']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20230707_toarmip_rad'
#
#   variables
    varlist=['O3','ozone']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
if __name__ == '__main__':
    main()
