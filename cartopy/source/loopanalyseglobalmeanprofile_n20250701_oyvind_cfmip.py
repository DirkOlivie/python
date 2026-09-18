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
# 1. NorESM2/NorESM2.5/CESM2/CESM3 (including NCAR simulation)
#----------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'nf1850_ne30pg3_ne30pg3_mtn14_locallim_20250625', \
               'nf1850_ne30pg3_ne30pg3_mtn14_locallim_sstp4K_20250625', \
                \
               'nf1850_ne30pg3_ne30pg3_mtn14_globlim_20250625', \
               'nf1850_ne30pg3_ne30pg3_mtn14_globlim_sstp4K_20250625']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2,2,2,2,2]
    year1list=[11,11,11,11,11]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0,2]
    colorlist    =[0,1,1,2,2]
    legendlist=['NorESM2', \
                'NorESM3 (loc. del., dcs=600)','', \
                'NorESM3 (glob. del., dcs=600)','']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250701_oyvind_cfmip'
#
#   0-20 km
############    
    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE']]

#   regionlist=['glob','90S60S','60S28S','28S28N','28N60N','60N90N']
    regionlist=['glob']

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :
#
        varlist=vargrouplist[igroup]
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=[figlayout20km], description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

if __name__ == '__main__':
    main()
