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
#   CHECKING H2O UPPER BOUNDARY CONDITIONS
#-----------------------------------------

    code='n20260907_noresm2.5_cmip7forcing_ubcnone'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['n1850Gaxg.LM.n30b24.511.betzy.20260904']*3 \
             +['n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcnone']*3 \
             +['n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcfix']*3
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1406]*9
    year1list=[1425]*9
    seasonlist=['YEA']*9
    linestylelist=[0,1,2,0,1,2,0,1,2]
    colorlist    =[0,0,0,1,1,1,2,2,2]
    legendlist=['NH','28S28N','SH','NH (no UBC)','28S28N (no UBC)','SH (no UBC)','NH (fix UBC)','28S28N (fix UBC)','SH (fix UBC)']
    regionlist=['NH','28S28N','SH','NH','28S28N','SH','NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['Q']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   CHECKING H2O UPPER BOUNDARY CONDITIONS
#-----------------------------------------

    code=code+'_diff'
    figlayoutlist=[figlayout]
    expidlist=['n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcfix']*3
    refidlist=['n1850Gaxg.LM.n30b24.511.betzy.20260904']*3
#
    wlist=[1.,-1.]
#    
    year0list=[1406]*3
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
    varlist=['Q','T']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
