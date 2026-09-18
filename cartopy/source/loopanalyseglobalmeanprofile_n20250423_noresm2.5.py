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
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850norbc_f19_f19_20241127_test13', \
               'NF1850norbc_f19_f19_20241127_test14', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408', \
               'n1850.ne30_tn14.hybrid_fates-nocomp_spinup.3.0a02.20250415', \
               'FHIST_f19_f19_mg17_20211015', \
               'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5,5,35,5,1855,5]
#   year1list=[7,7,7,7,7]
    year1list=[8,8,8,8,8,38,8,1858,8]
 #   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0,0,1,2,0,0]
    colorlist=[0,1,1,2,3,3,3,4,5]
    legendlist=['NorESM2', \
                'NorESM2.3', \
                'NorESM2.3 (with SI)', \
                'NorESM2.5', \
                'NorESM3 (3.0a02, DCS=500-(600))', \
                'NorESM3 (3.0a02, DCS=(500)-600)', \
                'NorESM3 (3.0a02, DCS=600)', \
                'CESM2', \
                'CESM3']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250423_noresm2.5_cesm3'
#
#   0-45 km
############
    vargrouplist=[['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123','so4_a123'], \
                  ['mmr_BC','mmr_BC','mmr_BC','mmr_BC','mmr_BC','mmr_BC','bc_a14','bc_a14'], \
                  ['OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','pom_a14','pom_a14'], \
                  ['SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','soa_a12','soa_a12']]
    
    ngroup=len(vargrouplist)

    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

#   0-20 km
############    
    vargrouplist=[['mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','ncl_a123'], \
                  ['CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ]]
    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE'], \
                  ['T' ,'T' ,'T' ,'T' ,'T' ,'T' ,'T' ]]

#   vargrouplist=[['T' ,'T' ,'T' ,'T' ,'T' ,'T' ,'T' ]]
    vargrouplist=[['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE']]

    regionlist=['glob']
#   regionlist=['90S60S','60S28S','28S28N','28N60N','60N90N']

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=[figlayout20km], description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

# 2. NorESM2/NorESM2.5/CESM2 [WITHOUT CEMS3]
#----------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850norbc_f19_f19_20241127_test13', \
               'NF1850norbc_f19_f19_20241127_test14', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408', \
               'n1850.ne30_tn14.hybrid_fates-nocomp_spinup.3.0a02.20250415', \
               'FHIST_f19_f19_mg17_20211015']
#              'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5,5,5,1855]
#   year1list=[7,7,7,7,7]
    year1list=[8,8,8,8,8,8,1858]
#   year1list=year0list
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0,0,2,0]
    colorlist=[0,1,1,2,3,3,4]
    legendlist=['NorESM2', \
                'NorESM2.3', \
                'NorESM2.3 (with SI)', \
                'NorESM2.5', \
                'NorESM3 (3.0a02, DCS=500)', \
                'NorESM3 (3.0a02, DCS=600)', \
                'CESM2']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250423_noresm2.5_cesm3'
#
#   0-45 km
############
    vargrouplist=[['SO2','SO2','SO2','SO2','SO2','SO2','SO2'], \
                  ['H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4','H2SO4']]
    
    ngroup=len(vargrouplist)

    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)


if __name__ == '__main__':
    main()
