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
    figlayout=cfiglayout.CFigLayout(code='standard')
    figlayoutlog=cfiglayout.CFigLayout(code='standard',xtype='log')
    figlayout20km=cfiglayout.CFigLayout(code='standard',yrange=[0.,20.])
    figlayoutlist=[figlayout]
    
#
# 1. GHGMAM4 simulation
#----------------------------------------------------------------
    expidlist=[\
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_20250522', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_20250522', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_20250522', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_20250522']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1,4,7,10]
    year1list=[1,4,7,10]
 #   year1list=year0list
    seasonlist=['JAN','JAN','JAN','JAN']
    linestylelist=[0,0,0,0]
    colorlist=[0,1,2,3]
    legendlist=['year 1','year 4','year 7','year 10'] 
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250607_cesm2.5_ghg'
#
    varlist=['CO2','CH4','N2O','CFC11','CFC12']
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

# 2. GHGCAMoslo simulation
#----------------------------------------------------------------
    expidlist=[ \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2']
#
    refidlist=expidlist
    wlist=[1.,-1.]
#    
    year0list=[1,4,7,10,13]
    year1list=[1,4,7,10,13]
 #   year1list=year0list
    seasonlist=['JAN','JAN','JAN','JAN','JAN']
    linestylelist=[0,0,0,0,0]
    colorlist=[0,1,2,3,4]
    legendlist=['year 1','year 4','year 7','year 10','year13']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250607_noresm2.5_ghg'
#
    varlist=['CO2','CH4','N2O','CFC11','CFC12']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

# 2. GHGCAMoslo simulation
#----------------------------------------------------------------
    expidlist=[ \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2']
#
    refidlist=[ \
               'n1850.ne30_tn14.noresm3_0_alpha03d.20250528', \
               'n1850.ne30_tn14.noresm3_0_alpha03d.20250528', \
               'n1850.ne30_tn14.noresm3_0_alpha03d.20250528', \
               'n1850.ne30_tn14.noresm3_0_alpha03d.20250528', \
               'n1850.ne30_tn14.noresm3_0_alpha03d.20250528']
    wlist=[1.,-1.]
#    
    year0list=[9,10,11,12,13]
    year1list=[9,10,11,12,13]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,0,0,0]
    colorlist=[0,1,2,3,4]
    legendlist=['year 9','year 10','year 11','year 12','year 13']
    regionlist=['glob','glob','glob','glob','glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250607_noresm2.5_ghg'
#
    varlist=['T']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

if __name__ == '__main__':
    main()
