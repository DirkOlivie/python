import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
    print('--- loopanalyseglobalmeanprofile ---')

    figlayout=cfiglayout.CFigLayout(code='standard')

#   CESM2 - full chemistry
    expidlist=['FC2010climo_f19_20210204_test1', \
               'NF1850norbc_tropstratchem_f19_20210517_test01', \
               'NHIST_f19_tn14_20190710']
    legendlist=['CESM2 (cam-chem)','NorESM2 (full chemistry)','NorESM2 (climatology from WACCM)']
    varlist=['O3','O3','ozone']
    year0list=[16,16,2008]
    year1list=[20,20,2012]
    seasonlist=['YEA']#'JJA','DJF','YEA']
    regionlist=['glob','28S28N']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, figlayout=figlayout)
#
if __name__ == '__main__':
    main()
