import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard',colorscheme='keyclim-wp6')
#
    generalcode='n20240410_co2_jerry'
#
#   CMIP6 - 20010-2014 O3
#------------------------
    expidlist=['N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm', \
               'N1850_f19_tn14_20190730esm']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1751,1751,1751,1751,2200,2200,2200,2200]
    year1list=[1751,1751,1751,1751,2200,2200,2200,2200]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code=generalcode
#
    varlist=['CO2','CO2_FFF','CO2_LND','CO2_OCN','CO2','CO2_FFF','CO2_LND','CO2_OCN']
    legendlist=varlist
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

if __name__ == '__main__':
    main()
