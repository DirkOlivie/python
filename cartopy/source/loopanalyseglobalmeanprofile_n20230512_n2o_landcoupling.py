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
    generalcode='n20230512_n2o_landcoupling'
#
#   CMIP6
#------------------------
    expidlist=['NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test01', \
               'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test02', \
               'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test03', \
               'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test04']
    refidlist=expidlist
    wlist=[1.,0.]
# 
    legendlist=['prescribed N'+r'$_2$'+'O', \
                'land emiss. (cold start)', \
                'land emiss. (warm start)', \
                'land+ocean (30%) emiss. (warm start)']
#    
    year0list=[41,41,41,41]
    year1list=[50,50,50,50]
    seasonlist=['YEA','YEA','YEA','YEA']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['N2O']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

if __name__ == '__main__':
    main()
