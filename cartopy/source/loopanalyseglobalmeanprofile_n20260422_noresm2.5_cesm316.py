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
    

    code='n20260422_noresm2.5_cesm316'    
#
# 1. NorESM3 : CMIP6 / CMIP7 / CMIP7+GHG /CESM316
#------------------------------------------------
    figlayoutlist=[figlayout,figlayoutlog]

    code='n20260422_noresm2.5_cesm316'
    expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
               'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
               'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
               'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[816,816,816,70]
    year1list=[830,830,830,84]
    seasonlist=['YEA','YEA','YEA','YEA']
    linestylelist=[0,0,0,4]
    colorlist    =[1,2,3,4]
    legendlist=['CMIP6', \
                'CMIP7', \
                'GHG+CMIP7', \
                'CESM #316']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
#
    vargrouplist=[['mmr_BC','mmr_BC','mmr_BC','bc_a14'], \
                  ['mmr_OM','mmr_OM','mmr_OM','pom_a14'], \
                  ['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123'], \
                  ['mmr_DUST','mmr_DUST','mmr_DUST','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','mmr_SALT','ncl_a123'], \
                  ['T','T','T','T']]

    vargrouplist=[['T','T','T','T']] 
#
    for varlist in vargrouplist :
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
# 2. NorESM3 : CMIP6 / CMIP7 / CMIP7+GHG /CESM316
#------------------------------------------------
    figlayoutlist=[figlayout,figlayoutlog]

    code='n20260422_noresm2.5_cesm316_diff'
    expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
               'n1850ghg.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.cmip7frc', \
               'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']
#
    refidlist=['n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
               'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref', \
               'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11.ref']
    wlist=[1.,-1.]
#    
    year0list=[816,816,70]
    year1list=[830,830,84]
    refyear0list=[816,816,816]
    refyear1list=[830,830,830]
#
    seasonlist=['YEA','YEA','YEA']
    linestylelist=[0,0,4]
    colorlist    =[2,3,4]
    legendlist=['CMIP7 - CMIP6', \
                'GHG+CMIP7 - CMIP6', \
                'CESM #316 - CMIP6']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
#
    vargrouplist=[['T','T','T']]
#
    for varlist in vargrouplist :
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, refyear0list=refyear0list, refyear1list=refyear1list)
#
if __name__ == '__main__':
    main()
