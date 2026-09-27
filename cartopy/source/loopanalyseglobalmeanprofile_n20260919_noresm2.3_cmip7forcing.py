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

    code='n20260919_noresm2.3_cmip7forcing_oxid_glob'
    figlayoutlist=[figlayout, figlayoutlog]
    expidlist=['NF1850norbc_tropstratchem_f19_f19_20241127_test01', \
               'NF1850norbc_tropstratchem_f19_f19_20241127_test01_bis', \
               'NF1850norbc_tropstratchem_f19_f19_20241127_test16_bis', \
               'NF1850norbc_tropstratchem_f19_f19_t00_20260829', \
               'NF1850norbc_tropstratchem_f19_f19_t01_20260829', \
               'NF1850norbc_tropstratchem_f19_f19_t02_20260829']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1,1,1,1,1,1]
    year1list=[30,30,30,30,30,30]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,0,0,0,0]
    colorlist    =[0,1,2,4,5,6]
    legendlist=['test01','test01-bis','test16-bis','t00','t01','t02']
    regionlist=['glob','glob','glob','glob','glob','glob']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['CCL4', 'CF2CLBR', 'CF3BR', 'CFC11', 'CFC113', 'CFC12', 'CH3BR', 'CH3CCL3', 'CH3CL', 'CH4', \
             'CO2', 'H2', 'HCFC22', 'N2O', 'CFC114', 'CFC115', 'HCFC141B', 'HCFC142B', 'CH2BR2', 'CHBR3', \
             'H2402', 'OCS', 'SF6']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
