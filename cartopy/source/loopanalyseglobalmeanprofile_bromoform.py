import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile2 +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard')

#   CESM2 - full chemistry
    expidlist=['NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08', \
               'NHISTfrc2_f19_tn14_bromo_08']
    varlist=['CHBR3','CHBR3','CHBR3','CHBR3','CHBR3']
#   year0list=[2006]
#   year1list=[2014]
    year0list=[2006,2006,2006,2006,2006]
#    year1list=[2006,2006,2006,2006,2006]
    year1list=[2014,2014,2014,2014,2014]
    seasonlist=['YEA','DJF','MAM','JJA','SON']
    legendlist=seasonlist
    regionlist=['glob','28S28N','NORTHATL','INDIANOCN','BAYOFBENGA','NORTHATL2','SOUTHOCNIO','SOUTHOCNNF','TROPEASTPAC','TROPWESTPAC']
    verticalaxislist=['pressure','height']
#
    description='regioncommon'
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, legendlist=seasonlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description)
#
    print('--- loopanalyseglobalmeanprofile2 ---')
#
if __name__ == '__main__':
    main()
