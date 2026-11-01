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
#   CHECKING OXIDANT CONDITIONS - GLOBAL
#------------------------------

    code='n20261022_noresm2.3_oxidants'
    figlayoutlist=[figlayoutlog]
    expidlist= \
             ['NF1850norbc_tropstratchem_f19_f19_t02_20260829']*11
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[21,22,23,24,25,26,27,28,29,30,21]
    year1list=[21,22,23,24,25,26,27,28,29,30,30]
#   seasonlist=['YEA']*4
#    seasonlist=['JAN']*10
    linestylelist=[0,0,0,0,0,0,0,0,0,0,0]
    colorlist    =[0,0,0,0,0,0,0,0,0,1,2]
    legendlist=['']*9+['year 30']+['average']
    regionlist=['glob']*11
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['OH','HO2','NO3','O3']
#
    seasongrouplist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
#
    for season in seasongrouplist :

        seasonlist=[season]*11

        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
