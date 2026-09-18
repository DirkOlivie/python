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
#
#  NORESM2.5 + CESM2.5 : DMS, SO2, H2SO4
#----------------------------------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
               'n1850.ne30_tn14.hybrid.20240801', \
               'n1850.ne30_tn14.hybrid_coare.20240801', \
               'n1850.ne30_tn14.hybrid.20240808', \
               'n1850.ne30_tn14.hybrid.20240822', \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621', \
               'n1850mam4.ne30_tn14.hybrid.clmbgc.20240826']

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2,2,2,2,2,1201,1601,2]
    year1list=[2,2,2,2,2,1201,1601,2]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,4,3,5,6,7]
    legendlist=['isopycnic', \
                'hybrid (01)', \
                'hybrid-coare', \
                'hybrid (08)', \
                'hybrid (22)', \
                'CMIP6', \
                'CMIP6 [2x2]', \
                'mam4']
    regionlist=['glob']#['LAND','SEA','glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240826_cesm2.5'
#
#   variables
    varlist=['DMS','SO2','H2SO4']
#    varlist=['RELHUM']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#  NORESM2.5 + CESM2.5 : mmr_SULFATE / so4_a123
#----------------------------------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.isopycnic.20240801', \
               'n1850.ne30_tn14.hybrid.20240801', \
               'n1850.ne30_tn14.hybrid_coare.20240801', \
               'n1850.ne30_tn14.hybrid.20240808', \
               'n1850.ne30_tn14.hybrid.20240822', \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621', \
               'n1850mam4.ne30_tn14.hybrid.clmbgc.20240826', \
               'FHIST_f19_f19_mg17_20211015']

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2,2,2,2,2,1201,1601,2,1861]
    year1list=[2,2,2,2,2,1201,1601,2,1861]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,4,3,5,6,7,8]
    legendlist=['isopycnic', \
                'hybrid (01)', \
                'hybrid-coare', \
                'hybrid (08)', \
                'hybrid (22)', \
                'CMIP6', \
                'CMIP6 [2x2]', \
                'mam4',
                'mam4 [2x2, CMIP6]']
    regionlist=['glob']#['LAND','SEA','glob']
    verticalaxislist=['height']
#
    description=''
    code='n20240826_cesm2.5'
#
#   variables
    varlist=['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123','so4_a123']
#    varlist=['RELHUM']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()
