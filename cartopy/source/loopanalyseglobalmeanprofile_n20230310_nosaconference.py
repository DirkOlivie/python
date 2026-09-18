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
#   CMIP6 - 2009-2011 - NOSA CONFERENCE
#--------------------------------------
    expidlist=['NFHISTnorpddmsbcsdyn_f09_mg17_20191101', \
               'NHIST_f19_tn14_20190710', \
               'NHISTfrc2_f09_tn14_20191025', \
               'FHIST_f19_f19_mg17_20211015']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2009,2009,2009,2009]
    year1list=[2011,2011,2011,2011]
    seasonlist=['YEA','YEA','YEA','YEA']
    legendlist=['NorESM2 (1x1) nudg.', \
                'NorESM2 (2x2) cpl.', \
                'NorESM2 (1x1) cpl.', \
                'CESM2 (2x2) fSST']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20230310_nosaconference_cmip6'
#
    varlist=['mmr_BC','mmr_BC','mmr_BC','bc_a1a4']
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
    varlist=['mmr_SALT','mmr_SALT','mmr_SALT','ncl_a1a2a3']
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
#   OYVIND - 2009-2011 - NOSA CONFERENCE
#---------------------------------------
    expidlist=['NFHISTnorpddmsbcsdyn_std_f09_f09_mg17_080323', \
               'NFHISTnorpddmsbcsdyn_conv1_f09_f09_mg17_080323', \
               'NFHISTnorpddmsbcsdyn_convbc0_f09_f09_mg17_080323', \
               'NFHISTnorpddmsbcsdyn_convmix_f09_f09_mg17_080323', \
               'NFHISTnorpddmsbcsdyn_newact_f09_f09_mg17_080323']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    varlist=['mmr_BC','mmr_SALT']
    year0list=[2009,2009,2009,2009,2009]
    year1list=[2011,2011,2011,2011,2011]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    legendlist=['std', \
                'conv1', \
                'convbc0', \
                'convmix', \
                'newact']
    regionlist=['glob']
    verticalaxislist=['height'] 
#
    description='varcommon'
    code='n20230310_nosaconference_oyvind'
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
    print('--- loopanalyseglobalmeanprofile ---')
#
if __name__ == '__main__':
    main()
