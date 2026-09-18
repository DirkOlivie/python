import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard', xtype='')
    figlayoutlog=cfiglayout.CFigLayout(code='standard',xtype='log')
#    figlayout20km=cfiglayout.CFigLayout(code='standard',yrange=[0.,20.])
    
#
# 1. NorESM3 : CMIP6 / CMIP7 / CMIP7+GHG 
#---------------------------------------
    code='n20260328_noresm2.5_cmip7frc'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
               'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
               'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[816,816,816]
    year1list=[830,830,830]
    seasonlist=['YEA','YEA','YEA']
    linestylelist=[0,0,0]
    colorlist    =[1,2,3]
    legendlist=['Reference', \
                'CMIP7', \
                'GHG+CMIP7']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['DMS','SO2','H2SO4','isoprene','monoterp','SOA_SV','SOA_LV', \
             'mmr_BC','mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT', \
             'H2O2','HO2_aft','NO3_aft','OH_aft', \
             'T'] 
#
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
# 2. NorESM3 : CMIP7 / CMIP7+GHG compared to CMIP6
#-------------------------------------------------
    code='n20260328_noresm2.5_cmip7frc_diff'
    figlayoutlist=[figlayout]
    expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
               'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']
#
    refidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
               'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref']
#
    wlist=[1.,-1]
#    
    year0list=[816,816]
    year1list=[830,830]
    seasonlist=['YEA','YEA']
    linestylelist=[0,0]
    colorlist    =[2,3]
    legendlist=['CMIP7 - Reference', \
                'GHG+CMIP7 - Reference']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['DMS','SO2','H2SO4','isoprene','monoterp','SOA_SV','SOA_LV', \
             'mmr_BC','mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT', \
             'H2O2','HO2_aft','NO3_aft','OH_aft', \
             'T'] 

#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
# 3. NorESM3 : CMIP7+GHG : initial time-evolution of profile [IN YEARS]
#-----------------------------------------------------------
    code='n20260328_noresm2.5_cmip7frc_ghg'
    figlayoutlist=[figlayout]
    expidlist=['n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']*7
#
    refidlist=expidlist
#
    wlist=[1.,0.]
#    
    year0list=[816,817,818,819,820,821,831]
    year1list=[816,817,818,819,820,830,840]
    seasonlist=['YEA']*7
    linestylelist=[0,0,0,0,0,0,0]
    colorlist    =[0,1,2,3,4,5,6]
    legendlist=['816','817','818','819','820','821-830','831-840']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['CO2','CH4','N2O','CFC11','CFC12']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

# 4. NorESM3 : CMIP7+GHG : initial time-evolution of profile [IN MONTHS]
#-----------------------------------------------------------
    code='n20260328_noresm2.5_cmip7frc_ghg_season'
    figlayoutlist=[figlayout]
    expidlist=['n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc']*12
#
    refidlist=expidlist
#
    wlist=[1.,0.]
#    
    year0list=[816,816,816,816,816,816,816,816,816,816,816,816]
    year1list=[816,816,816,816,816,816,816,816,816,816,816,816]
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0]
    colorlist    =[0,1,2,3,4,5,6,7,8,9,10,11]
    legendlist=['JAN','FEB','MAR','APR','MAI','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    regionlist=['glob','NH','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['CO2','CH4','N2O','CFC11','CFC12']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

#
if __name__ == '__main__':
    main()
