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

    code='n20260907_noresm2.5_cmip7forcing_oxid_glob'
    figlayoutlist=[figlayoutlog]
    expidlist= \
              ['n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcnone']*1 \
             +['n1850Gaxg.LM.n30b24.513.betzy.20260905.oxid']*1 \
             +['NF1850norbc_tropstratchem_f19_f19_t02_20260829']*1 \
             +['NF1850norbc_tropstratchem_f19_f19_t02_20260829']*1
#             +['NF1850norbc_tropstratchem_f19_f19_20241127_test01_bis']*1 \
#             +['NF1850norbc_tropstratchem_f19_f19_20241127_test16_bis']*1 \
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
#   year0list=[1406]*2+[21]*3+[30]*1
#   year1list=[1415]*2+[30]*3+[30]*1
    year0list=[1406]*2+[21]*1+[30]*1
    year1list=[1415]*2+[30]*1+[30]*1
#   seasonlist=['YEA']*4
    seasonlist=['JUL']*4
    linestylelist=[0,0,0,0]
    colorlist    =[0,1,2,4]
#   legendlist=['glob (cmip6)','glob (new)','glob (fullchem)','test01','test16','glob (fullchem - 1 yr)']
    legendlist=['glob (cmip6)','glob (new)','glob (fullchem)','glob (fullchem - 1 yr)']
    regionlist=['','','','']#,'','']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['OH','HO2','NO3','O3']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   CHECKING OXIDANT CONDITIONS - NH - SH - TROP
#------------------------------

    code='n20260907_noresm2.5_cmip7forcing_oxid'
    figlayoutlist=[figlayoutlog]
    expidlist=['n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcnone']*3 \
             +['n1850Gaxg.LM.n30b24.513.betzy.20260905.oxid']*3 \
             +['NF1850norbc_tropstratchem_f19_f19_t02_20260829']*3 \
             +['NF1850norbc_tropstratchem_f19_f19_t02_20260829']*3
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1406]*6+[21]*6
    year1list=[1415]*6+[30]*6
    seasonlist=['YEA']*9
    linestylelist=[0,1,2,0,1,2,0,1,2,0,1,2]
    colorlist    =[0,0,0,1,1,1,2,2,2,3,3,3]
    legendlist=['NH (cmip6)','28S28N (cmip6)','SH (cmip6)', \
                'NH (new)','28S28N (new)','SH (new)', \
                'NH (fullchem)','28S28N (fullchem)','SH (fullchem)', \
                'NH (fullchem - 1 yr)','28S28N (fullchem- 1 yr)','SH (fullchem - 1 yr)']
    regionlist=['NH','28S28N','SH', \
                'NH','28S28N','SH', \
                'NH','28S28N','SH', \
                'NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['OH','HO2','NO3','O3']
#
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   CHECKING OXIDANT CONDITIONS
#------------------------------

    code='n20260907_noresm2.5_cmip7forcing_oxid'
    figlayoutlist=[figlayoutlog]
    expidlist=['n1850Gaxg.LM.n30b24.513.betzy.20260905.ubcnone']*3 \
             +['n1850Gaxg.LM.n30b24.513.betzy.20260905.oxid']*3
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1406]*6
    year1list=[1415]*6
    seasonlist=['YEA']*6
    linestylelist=[0,1,2,0,1,2]
    colorlist    =[0,0,0,1,1,1]
    legendlist=['NH (cmip6)','28S28N (cmip6)','SH (cmip6)','NH (new)','28S28N (new)','SH (new)']
    regionlist=['NH','28S28N','SH','NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['DMS','SO2','isoprene','monoterp','H2SO4','mmr_SULFATE','SOA_NAA1']
#
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#




if __name__ == '__main__':
    main()
