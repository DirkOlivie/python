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
# 1. NorESM2/NorESM2.5/CESM2/CESM3
#----------------------------------------------------------------
    expidlist=['NF1850norbc_f19_f19_20241127_test01', \
               'NF1850norbc_aer2014_f19_f19_20241127_test01', \
               'NF1850norbc_f19_f19_20241127_test13', \
               'NF1850norbc_aer2014_f19_f19_20241127_test13']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5]
    year1list=[8,8,8,8]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA']
    linestylelist=[0,2,0,2]
    colorlist=[0,0,1,1]
    legendlist=['NorESM2.3 (0.001)','', \
                'NorESM2.3 (1.000)','']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250618_noresm2.3_scalfac'
#
#   0-20 km
############    
    vargrouplist=[['CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD'], \
                  ['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE'], \
                  ['T' ,'T' ,'T' ,'T']]


    regionlist=['glob']#,'90S60S','60S28S','28S28N','28N60N','60N90N']

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=[figlayout20km], description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

if __name__ == '__main__':
    main()
