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
    figlayoutlist=[figlayout]
#
    generalcode='n20251107_n2olandocean_coupling'
#
#   CMIP6
#------------------------
    expidlist=['N1850vslsn2onh3_f19_tn14_test01b', \
               'N1850vslsn2onh3_f19_tn14_test02', \
               'N1850vslsn2onh3_f19_tn14_test03', \
               'N1850vslsn2onh3_f19_tn14_test04', \
               'N1850vslsn2onh3_f19_tn14_test05', \
               'N1850vslsn2onh3_f19_tn14_test06', \
               'N1850vslsn2onh3_f19_tn14_test07', \
               'N1850vslsn2onh3_f19_tn14_test08', \
               'N1850vslsn2onh3_f19_tn14_test09',\
               'N1850vslsn2onh3_f19_tn14_test10']
    refidlist=expidlist
    refidlist=expidlist
    wlist=[1.,0.]
# 
    legendlist=['SIM1b (D)', \
                'SIM2 (D)', \
                'SIM3 (D)', \
                'SIM4 (D)', \
                'SIM5 (D)', \
                'SIM6 (D)', \
                'SIM7 (D)', \
                'SIM8 (D)', \
                'SIM9 (D)', \
                'SIM10 (D)']
#    
    year0list=[41,41,41,41,41,41,41,41,41,41]
    year1list=[45,45,45,45,45,45,45,45,45,45]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['N2O']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code)

if __name__ == '__main__':
    main()
