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
    expidlist=['NF1850norbc_f19_20191025', \
               'NF1850norbc_aer2014_f19_20191025', \
               'NF1850norbc_f19_f19_20241127_test13', \
               'NF1850norbc_aer2014_f19_f19_20241127_test13', \
#               'NF1850norbc_f19_f19_20241127_test16', \
#               'NF1850norbc_aer2014_f19_f19_20241127_test16', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_dev_20250513', \
               'nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_aer2014_dev_20250513', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_20250522', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_aer2010_20250522', \
               'nf1850_ne30pg3_ne30pg3_mtn14_beta3proto.20250616', \
               'nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_aer2014.20250616', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4.20250616', \
               'nf1850_ne30pg3_ne30pg3_mtn14_mam4_aer2010.20250616', \
               'nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_homait.20250620', \
               'nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_homait_aer2014.20250620', \
               'nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_locallim.20250623', \
               'nf1850_ne30pg3_ne30pg3_mtn14_beta3proto_locallim.20250623_aer2014']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5,5,5,5,5,5,5,2,2,2,2,2,2,2,2]
    year1list=[8,8,8,8,8,8,8,8,8,8,5,5,5,5,5,5,5,5]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,0,2]
    colorlist=[6,6,0,0,1,1,2,2,3,3,4,4,5,5,7,7,8,8]
    legendlist=['NorESM2','', \
                'NorESM2.3', '',\
#               'NorESM2.3 (SI)', '',\
                'NorESM2.5','', \
                'NorESM3','', \
                'CESM3','', \
                'NorESM3 (beta)','', \
                'CESM3 (beta)','', \
                'NorESM3 (glob. del.)','', \
                'NorESM3 (loc. del.)','']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250527_noresm2.5_cesm3'
#
#   0-45 km
############
    vargrouplist=[['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123','so4_a123','mmr_SULFATE','mmr_SULFATE'], \
                  ['mmr_BC','mmr_BC','mmr_BC','mmr_BC','mmr_BC','mmr_BC','bc_a14','bc_a14','mmr_BC','mmr_BC'], \
                  ['OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','pom_a14','pom_a14','OM_NIAIAC','OM_NIAIAC'], \
                  ['SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','soa_a12','soa_a12','SOA_NAA1','SOA_NAA1'], \
                  ['SO2','SO2','SO2','SO2','SO2','SO2','SO2','SO2','SO2','SO2'], \
                  ['H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4']]
    
    ngroup=len(vargrouplist)

    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

#   0-20 km
############    
    vargrouplist=[['mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','dst_a123','dst_a123','mmr_DUST','mmr_DUST','dst_a123','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','ncl_a123','ncl_a123','mmr_SALT','mmr_SALT','ncl_a123','ncl_a123'], \
                  ['CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD','CLOUD' ,'CLOUD','CLOUD' ,'CLOUD'], \
                  ['T' ,'T' ,'T' ,'T' ,'T','T' ,'T' ,'T']]

    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE']]

#   regionlist=['glob','90S60S','60S28S','28S28N','28N60N','60N90N']
    regionlist=['glob']

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=[figlayout20km], description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

if __name__ == '__main__':
    main()
