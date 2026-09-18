import loopanalyseglobalmeanoceanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
#
def main():
#-------
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout0=cfiglayout.CFigLayout()
    figlayoutlist=[figlayout0]
#
#   Reference
#----------------------------------------------------------------------------------------
    expidlist=[\
               'N1850_f19_tn14_20190621', \
               'N1850_f19_tn14_20241127_test01', \
               'N1850_f19_tn14_20241127_test03', \
               'N1850_f19_tn14_20241127_test07', \
               'N1850_f19_tn14_20241127_test08', \
               'N1850_f19_tn14_20241127_test02', \
               'N1850_f19_tn14_20241127_test04']
# 
    refidlist=expidlist
#
    wlist=[1.,0.]
#    
    expyear0list=[1680,1680,1680,1680,1680,1680,1680] 
    expyear1list=[1680,1680,1680,1680,1680,1680,1680] 
    refyear0list=[1600,1600,1600,1600,1600,1600,1600] 
    refyear1list=[1600,1600,1600,1600,1600,1600,1600]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['NorESM2','gamma=0.264','gamma=0.274','gamma=0.276','gamma=0.278','gamma=0.284','gamma=0.294']
    colorlist=[0,1,2,3,4,5,6]
    linestylelist=[0,0,0,0,0,0,0]
    regionlist=['90S28S','28S28N','28N60N','60N90N','glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250211_noresm2.3'
#
#   variables
    varlist=['templvl']
    loopanalyseglobalmeanoceanprofile2.loopanalyseglobalmeanoceanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, expyear0list=expyear0list, expyear1list=expyear1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   CMIP6
#--------
    expidlist=[\
               'N1850_f19_tn14_20190621ext', \
               'N1850_f19_tn14_20190621ext', \
               'N1850_f19_tn14_20190621ext', \
               'N1850_f19_tn14_20190621ext', \
               'N1850_f19_tn14_20190621ext', \
               'N1850_f19_tn14_20190621ext']
#
    refidlist=expidlist
#
    wlist=[1.,-1.]
#    
    expyear0list=[1600,1690,1790,1890,1990,2090]
    expyear1list=[1609,1699,1799,1899,1999,2099]
    refyear0list=[1600,1600,1600,1600,1600,1600]
    refyear1list=[1609,1609,1609,1609,1609,1609]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['1600','1699','1799','1899','1999','2099']
    colorlist=[0,1,2,3,4,5]
    linestylelist=[0,0,0,0,0,0]
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250211_noresm2.3'
#
#   variables
    varlist=['templvl']
#    loopanalyseglobalmeanoceanprofile2.loopanalyseglobalmeanoceanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, expyear0list=expyear0list, expyear1list=expyear1list, refyear0list=refyear0list, refyear1list=refyear1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()

