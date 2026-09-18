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
    expidlist=['NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
               'NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01', \
               'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim02']

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000,2000]
    year1list=[2004,2004,2004]
    seasonlist=['YEA','YEA','YEA']
    colorlist=[0,1,2]
    legendlist=['memb 1', \
                'memb 2', \
                'memb 1 [energy]']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240822_camsvsls'
#
#   variables
    varlist=['T','Q','RELHUM']
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#
#  NORESM2.5 + CESM2.5 : DMS, SO2, H2SO4
#----------------------------------------------------------------------------------------
    expidlist=['NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01', \
               'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim02', \
               'NFHISTnorpddmsbcsdyn_enechk_f09_mg17_20220928'] 
    refidlist=['NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
               'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
               'NFHISTnorpddmsbcsdyn_f09_mg17_20220928']

    wlist=[1.,-1.]
#    
    year0list=[2000,2000,2009]
    year1list=[2004,2004,2010]
    seasonlist=['YEA','YEA','YEA']
    colorlist=[0,1,2]
    legendlist=['memb 2', \
                'memb 1 [energy]', \
                'cloud ppe [energy]']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240822_camsvsls_xdiff'
#
#   variables
    varlist=['T','Q','RELHUM']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code, colorlist=colorlist)
#




if __name__ == '__main__':
    main()
