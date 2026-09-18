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
#   NorESM : black carbon
#----------------------------------------------------------------

    expidlist=['NF1850norbc_f19_f19_20241127_test16', \
               'NF1850norbc_aer2014_f19_f19_20241127_test16', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_dev_20250513', \
               'nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_aer2014_dev_20250513']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5,5,5]
    year1list=[8,8,8,8,8,8]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,2,0,2,0,2]
    colorlist=[0,0,1,1,2,2]
    legendlist=['NorESM2.3','', \
                'NorESM2.5','', \
                'NorESM3','']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250527_noresm2.5_cesm3'
#
#   0-45 km
############
    varlist=['BC_N','BC_A','BC_NI','BC_AI','BC_AX','BC_AC']
    
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

if __name__ == '__main__':
    main()
