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
# 1. NorESM2/NorESM2.5/CESM3 (including NCAR simulation)
#----------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513', \
                \
               'n1850.ne30_tn14.nor3_b01-noLU_yr101.20250729', \
               'n1850.ne16pg3_tn14.nor3_b01-cplhist.20250716', \
                \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621ext', \
                \
               'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152', \
               'b.e30_beta06.B1850C_LTso.ne30_t232_wgx3.192']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[ 96,116,116,1200,1600,15,15]
    year1list=[100,120,120,1204,1604,19,19]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0,2,0,0]
    colorlist    =[0,1,2,3,4,5,6]
    legendlist=['NorESM3 (a03b, 1x1)', \
                'NorESM3 (b01, 1x1)', \
                'NorESM3 (b01, 2x2)', \
                'NorESM2-MM (1x1)', \
                'NorESM2-LM (2x2)', \
                'CESM3 (1x1, 152)', \
                'CESM3 (1x1, 192)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250814_noresm2.5_cesm3'
#
#   0-20 km
############    
    vargrouplist=[['mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','dst_a123','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','ncl_a123','ncl_a123'], \
                  ['CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD'], \
                  ['T' ,'T' ,'T' ,'T' ,'T','T' ,'T']]

    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE'], \
                  ['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123','so4_a123'], \
                  ['mmr_BC'     ,'mmr_BC'     ,'mmr_BC'     ,'mmr_BC'     ,'mmr_BC'     ,'bc_a14'  ,'bc_a14'  ], \
                  ['OM_NIAIAC'  ,'OM_NIAIAC'  ,'OM_NIAIAC'  ,'OM_NIAIAC'  ,'OM_NIAIAC'  ,'pom_a14' ,'pom_a14' ], \
                  ['SOA_NAA1'   ,'SOA_NAA1'   ,'SOA_NAA1'   ,'SOA_NAA1'   ,'SOA_NAA1'   ,'soa_a12' ,'soa_a12' ]]

    vargrouplist=[['mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','dst_a123','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','ncl_a123','ncl_a123']]

#   regionlist=['glob','90S60S','60S28S','28S28N','28N60N','60N90N']
    regionlist=['glob']

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=[figlayout20km], description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#
# 2. NorESM2/NorESM2.5 (including NCAR simulation)
#----------------------------------------------------------------
    expidlist=['n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513', \
                \
               'n1850.ne30_tn14.nor3_b01-noLU_yr101.20250729', \
               'n1850.ne16pg3_tn14.nor3_b01-cplhist.20250716', \
                \
               'N1850frc2_f09_tn14_20191001', \
               'N1850_f19_tn14_20190621ext']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[ 96,116,116,1200,1600]
    year1list=[100,120,120,1204,1604]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0,2]
    colorlist    =[0,1,2,3,4]
    legendlist=['NorESM3 (a03b, 1x1)', \
                'NorESM3 (b01, 1x1)', \
                'NorESM3 (b01, 2x2)', \
                'NorESM2-MM (1x1)', \
                'NorESM2-LM (2x2)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250814_noresm2.5_cesm3'
#
#   0-20 km
############    
    vargrouplist=[['SO2','SO2','SO2','SO2','SO2'], \
                  ['H2SO4','H2SO4','H2SO4','H2SO4','H2SO4']]

    vargrouplist=[['DMS','DMS','DMS','DMS','DMS']]

#   regionlist=['glob','90S60S','60S28S','28S28N','28N60N','60N90N']
    regionlist=['glob']

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=[figlayout20km], description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#
if __name__ == '__main__':
    main()
