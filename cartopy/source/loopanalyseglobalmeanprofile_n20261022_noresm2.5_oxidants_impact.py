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

    code='n20261022_noresm2.5_oxidants_impact'
    figlayoutlist=[figlayout, figlayoutlog]
    expidlist=['n1850GHGGaxg.LM.nor30b27.002.20261016']*11 \
             +['n1850GHGGaxg.LM.nor30b27.002.20261022.oxidtest']*11
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1,2,3,4,5,6,7,8,9,10, 1  ,1,2,3,4,5,6,7,8,9,10, 1]
    year1list=[1,2,3,4,5,6,7,8,9,10, 10 ,1,2,3,4,5,6,7,8,9,10, 10]
    linestylelist=[1,1,1,1,1,1,1,1,1,1, 0, 1,1,1,1,1,1,1,1,1,1, 0]
    colorlist    =[0,0,0,0,0,0,0,0,0,0, 0, 1,1,1,1,1,1,1,1,1,1, 1]
    legendlist=['','','','','','','','','','','old','','','','','','','','','','','new']
    verticalaxislist=['height']
    regionlist=['glob']*22
#
    description='varcommon'
#
    varlist=['DMS','SO2','isoprene','mmr_SULFATE']
#
#    regiongrouplist=['glob','SEA','LAND','NAM','SAM','NAF','SAF','SA','EA','IND','AUS','NEUR','SEUR','EUR','MED','USW','USE','US','CHN','CHNW','CHNE']
#    regiongrouplist=['glob',             'NAM','SAM','NAF','SAF','SA','EA','IND','AUS','NEUR','SEUR','EUR','MED','USW','USE','US','CHN','CHNW','CHNE']
#    regiongrouplist=['glob']
#
    seasongrouplist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']


    for season in seasongrouplist :

        seasonlist=[season]*22

        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
