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
    figlayout=cfiglayout.CFigLayout(code='standard', colorscheme='keyclim-wp6')
    figlayoutlist=[figlayout]
#
# 1. NorESM2.5 and NorESM2
#----------------------------------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
               'n1850.ne30_tn14.hybrid.20240801', \
               'n1850.ne30_tn14.hybrid_coare.20240801', \
               'n1850.ne30_tn14.hybrid.20240808', \
               'n1850.ne30_tn14.hybrid.20240822', \
               'n1850.ne30_tn14.hybrid_fatessp.20241111', \
               'n1850.ne30_tn14.hybrid_fatessp.20241204', \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621']

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[6 ,6 ,6 , 6, 6,24,59,1205,1605]
    year1list=[10,10,10,10,10,28,63,1209,1609]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,4,3,5,6,7,8]
    legendlist=['isopycnic', \
                'hybrid (01)', \
                'hybrid-coare', \
                'hybrid (08)', \
                'hybrid (22)', \
                '20241111', \
                '20241204', \
                'CMIP6', \
                'CMIP6 [2x2]']
    regionlist=['glob']#['LAND','SEA','glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240826_noresm2.5'
#
#   variables
    varlist=['mmr_BC','mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT'] #,'DMS','SO2','H2SO4']
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
# 2. NorESM2.5 and NorESM2 and CESM3
#----------------------------------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
               'n1850.ne30_tn14.hybrid.20240801', \
               'n1850.ne30_tn14.hybrid_coare.20240801', \
               'n1850.ne30_tn14.hybrid.20240808', \
               'n1850.ne30_tn14.hybrid.20240822', \
               'n1850.ne30_tn14.hybrid_fatessp.20241111', \
               'n1850.ne30_tn14.hybrid_fatessp.20241204', \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621', \
               'n1850mam4.ne30_tn14.hybrid.clmbgc.20240826'] 

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[6 ,6 ,6 , 6, 6,24,59,1205,1605,2]
    year1list=[10,10,10,10,10,28,63,1209,1609,2]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,4,3,5,6,7,8,9]
    legendlist=['isopycnic', \
                'hybrid (01)', \
                'hybrid-coare', \
                'hybrid (08)', \
                'hybrid (22)', \
                '20241111', \
                '20241204', \
                'CMIP6', \
                'CMIP6 [2x2]', \
                'MAM4 [CESM3]']
    regionlist=['glob']#['LAND','SEA','glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240826_noresm2.5'
#
#   variables
    varlist=['CLDLIQ','DMS','SO2','H2SO4']
#  loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
# 3. NorESM2.5 and NorESM2 and CESM3
#----------------------------------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
               'n1850.ne30_tn14.hybrid.20240801', \
               'n1850.ne30_tn14.hybrid_coare.20240801', \
               'n1850.ne30_tn14.hybrid.20240808', \
               'n1850.ne30_tn14.hybrid.20240822', \
               'n1850.ne30_tn14.hybrid_fatessp.20241111', \
               'n1850.ne30_tn14.hybrid_fatessp.20241204', \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621', \
               'n1850mam4.ne30_tn14.hybrid.clmbgc.20240826'] 

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[6 ,6 ,6 , 6, 6,24,59,1205,1605,2]
    year1list=[10,10,10,10,10,28,63,1209,1609,2]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,4,3,5,6,7,8,9]
    legendlist=['isopycnic', \
                'hybrid (01)', \
                'hybrid-coare', \
                'hybrid (08)', \
                'hybrid (22)', \
                '20241111', \
                '20241204', \
                'CMIP6', \
                'CMIP6 [2x2]', \
                'MAM4 [CESM3]']
    regionlist=['glob']#['LAND','SEA','glob']
    verticalaxislist=['height']
#
    description=''
    code='n20240826_noresm2.5'
#
#   variables
    varlist=['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()
