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
    figlayout=cfiglayout.CFigLayout(code='standard', xtype='log')
#    figlayoutlog=cfiglayout.CFigLayout(code='standard',xtype='log')
#    figlayout20km=cfiglayout.CFigLayout(code='standard',yrange=[0.,20.])
    figlayoutlist=[figlayout]
    
#
# 1. NorESM2/NorESM2.5/CESM3 (including NCAR simulation)
#----------------------------------------------------------------
    expidlist=['n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6.20260127', \
               'n1850esm.ne16pg3_tn4.noresm3_0_beta10.run7.emifv09cmip6_ubcnone.20260127']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[456,456]
    year1list=[460,460]
 #   year1list=year0list
    seasonlist=['YEA','YEA']
    linestylelist=[0,0]
    colorlist    =[0,1]
    legendlist=['with H2O ubc', \
                'without H2O ubc']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20260308_noresm2.5_ubch2o'
#
#   0-20 km
############    
    varlist=['Q','H2O']


#   regionlist=['glob','90S60S','60S28S','28S28N','28N60N','60N90N']
    regionlist=['glob']

    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
