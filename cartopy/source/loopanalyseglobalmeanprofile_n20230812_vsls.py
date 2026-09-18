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
    generalcode='n20230812_vsls'
#
#   PROFILE OF CHBR3
#----------------------
    expidlist=['NHISTfrc2_f19_tn14_bromo_08_r1850ext']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1990]
    year1list=[2014]
    seasonlist=['YEA']
    legendlist=['1990-2014']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['CHBR3']
    varlist=['CHBR3_as_concentration']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

#
#   PROFILE IF jCHBR3 for 3 periods [1850-1869, 1995-2014, 2080-2099]
#----------------------------------
    expidlist=['NHISTfrc2_f19_tn14_bromo_08_r1850', \
               'NHISTfrc2_f19_tn14_bromo_08_r1990', \
               'NSSP585frc2_f19_tn14_bromo_08_r2080']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1850,1995,2080]
    year1list=[1869,2014,2099]
    seasonlist=['YEA','YEA','YEA']
    legendlist=['1850-1869','1995-2014','2080-2099']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['jchbr3']
#
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

if __name__ == '__main__':
    main()
