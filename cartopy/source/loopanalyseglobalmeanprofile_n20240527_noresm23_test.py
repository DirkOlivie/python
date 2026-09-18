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
    expidlist=['NF1850norbc_tropstratchem_f19_20240312_test01', \
               'N1850_tropstratchem_f19_tn14_20240319_test08', \
               'N1850_tropstratchem_f19_tn14_20240319_test10']

    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[36,2,2]
    year1list=[40,4,4]
    seasonlist=['YEA','YEA','YEA']
    legendlist=['noresm2-chem (fsst, esm2025)', \
                'noresm2.3-chem', \
                'noresm2.3-chem']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240527_noresm23_test'
#
#   variables
    varlist=['mmr_SULFATE','O3_as_partpress']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)
#
if __name__ == '__main__':
    main()
