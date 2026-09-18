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
    figlayout=cfiglayout.CFigLayout(code='standard', xtype='')
    figlayoutlog=cfiglayout.CFigLayout(code='standard',xtype='log')
    
#
#   1. absolute
#-----------------------------------------
    code='n20260906_noresm2.5_ghg_zonalgradient'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['n1850Gaxg.LM.n30b24.511.betzy.20260904', \
               'n1850Gaxg.LM.n30b24.511.betzy.20260904', \
               'n1850Gaxg.LM.n30b24.511.betzy.20260904', \
               'n1850GaxgGHG.LM.n30b24.511.betzy.20260904', \
               'n1850GaxgGHG.LM.n30b24.511.betzy.20260904', \
               'n1850GaxgGHG.LM.n30b24.511.betzy.20260904']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1414]*6
    year1list=[1415]*6
    seasonlist=['YEA']*6
    linestylelist=[0,1,2,0,1,2]
    colorlist    =[0,0,0,1,1,1]
    legendlist=['NH','28S28N','SH','NH (GHG)','28S28N (GHG)','SH (GHG)']
    regionlist=['NH','28S28N','SH','NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['CO2','CH4','N2O']
    varlist=['T','QRS','QRL']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   2. difference
#-----------------------------------------
    code='n20260906_noresm2.5_ghg_zonalgradient_diff'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['n1850GaxgGHG.LM.n30b24.511.betzy.20260904', \
               'n1850GaxgGHG.LM.n30b24.511.betzy.20260904', \
               'n1850GaxgGHG.LM.n30b24.511.betzy.20260904']
    refidlist=['n1850Gaxg.LM.n30b24.511.betzy.20260904', \
               'n1850Gaxg.LM.n30b24.511.betzy.20260904', \
               'n1850Gaxg.LM.n30b24.511.betzy.20260904']
#
    wlist=[1.,-1.]
#    
    year0list=[1411]*3
    year1list=[1425]*3
    seasonlist=['YEA']*3
    linestylelist=[0,1,2]
    colorlist    =[0,0,0]
    legendlist=['NH','28S28N','SH']
    regionlist=['NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['CO2','CH4','N2O']
    varlist=['T','QRS','QRL']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

if __name__ == '__main__':
    main()
