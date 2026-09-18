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
# 1. NorESM2.5 : Lana vs norbc
#----------------------------------------------------------------------------------------
    expidlist=['nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250219', \
               'nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250219', \
                \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014bc_ne30pg3_ne30pg3_mtn14.fatessp_20250320', \
               'nf1850_aer2014OM_ne30pg3_ne30pg3_mtn14.fatessp_20250320', \
               'nf1850_aer2014S_ne30pg3_ne30pg3_mtn14.fatessp_20250320']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[7,7,7,7,7,7,7]
    year1list=[7,7,7,7,7,7,7]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,3,4,5,6]
    legendlist=['Lana', \
                'Lana (aer 2014)', \
                'Norbc', \
                'Norbc (aer 2014)', \
                'Norbc (bc 2014)', \
                'Norbc (om 2014)', \
                'Norbc (so2 2014)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250407_noresm2.5_only2.5'
#
#   variables
    varlist=['mmr_BC','mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT','DMS','SO2','H2SO4','H2O2','isoprene','monoterp','SOA_LV','SOA_SV','OH_bef','NO3_bef','HO2_bef']
    varlist=['CLDLIQ','CLDICE','NUMLIQ','NUMICE']
    varlist=['CLOUD']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
# 2. NorESM2 : 1x1, 2x2, dmsx2
#---------------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850frc2norbc_aer2014_f09_20200108', \
                \
               'NF1850norbc_f19_20191025', \
               'NF1850norbc_aer2014_f19_20191025', \
               'NF1850norbc_bc2014_f19_20191025', \
               'NF1850norbc_oc2014_f19_20191025', \
               'NF1850norbc_so22014_f19_20191025', \
                \
               'NF1850norbc2dms_f19_20200219']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[7,7,7,7,7,7,7,7]
    year1list=[7,7,7,7,7,7,7,7]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,3,4,5,6,7]
    legendlist=['1x1', \
                '1x1 (aer 2014)', \
                '2x2', \
                '2x2 (aer 2014)', \
                '2x2 (bc 2014)', \
                '2x2 (om 2014)', \
                '2x2 (so2 2014)', \
                '2x2 (dms x 2)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250407_noresm2.5_noresm2_only2.0'
#
#   variables
    varlist=['mmr_BC','mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT','DMS','SO2','H2SO4','H2O2','isoprene','monoterp','SOA_LV','SOA_SV','OH_bef','NO3_bef','HO2_bef']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)

# 3. NorESM2/NorESM2.5
#---------------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5]
    year1list=[7,7]
    seasonlist=['YEA','YEA']
    colorlist=[0,1]
    legendlist=['1x1 NorESM2', \
                '1x1 NorESM2.5']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250407_noresm2.5_comp'
#
#   variables
    varlist=['mmr_BC','mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT','DMS','SO2','H2SO4','H2O2','isoprene','monoterp','SOA_LV','SOA_SV', \
             'CLDLIQ','CLDICE', \
             'XPH_LWC', \
             'SOA_A1','SOA_NA','SOA_NAA1','OM_NIAIAC']
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
#   LOGARITHMIC
    varlist=['OH_bef','NO3_bef','HO2_bef']
    figlayoutlist2=[figlayoutlog]
#    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist2, description=description, code=code, colorlist=colorlist)

# 4. NorESM2/NorESM2.5 - increased DMS emissions
#---------------------------------------------------------------------
    expidlist=['NF1850norbc_f19_20191025', \
               'NF1850norbc2dms_f19_20200219', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250219'] 
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5]
    year1list=[7,7,7,7]
    seasonlist=['YEA','YEA','YEA','YEA']
    colorlist=[0,0,1,1]
    linestylelist=[0,1,0,1]
    legendlist=['2x2 NorESM2', \
                '2x2 NorESM2 (DMS)', \
                '1x1 NorESM2.5', \
                '1x1 NorESM2.5 (DMS)']   
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20250407_noresm2.5_dmsx2'
#
#   variables
    varlist=['mmr_SULFATE','DMS','SO2','H2SO4']
#   loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
# 5. NorESM2/NorESM2.5/CESM2
#----------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152'] 
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5]
    year1list=[7,7,7]
    seasonlist=['YEA','YEA','YEA']
    colorlist=[0,1,2]
    legendlist=['1x1 NorESM2', \
                '1x1 NorESM2.5', \
                '1x1 CESM3']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250407_noresm2.5_cesm3'
#
#   variables
    vargrouplist=[['mmr_SULFATE','mmr_SULFATE','so4_a123'], \
                  ['mmr_BC','mmr_BC','bc_a14'], \
                  ['OM_NIAIAC','OM_NIAIAC','pom_a14'], \
                  ['SOA_NAA1','SOA_NAA1','soa_a12'], \
                  ['mmr_DUST','mmr_DUST','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','ncl_a123']]

    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE'], \
                  ['CLOUD' ,'CLOUD' ,'CLOUD' ]]

    ngroup=len(vargrouplist)  
  
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#       loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
# 6. NorESM2/NorESM2.5/CESM2 + aer2014
#----------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850frc2norbc_aer2014_f09_20200108', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5,5]
    year1list=[7,7,7,7,7]
    seasonlist=['YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,0,1,1,2]
    linestylelist=[0,2,0,2,0]
    legendlist=['1x1 NorESM2', \
                '', \
                '1x1 NorESM2.5', \
                '', \
                '1x1 CESM3']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250407_noresm2.5_cesm3_plus2014'
#
#   0-45 km
###########
    vargrouplist=[['mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','mmr_SULFATE','so4_a123'], \
                  ['mmr_BC','mmr_BC','mmr_BC','mmr_BC','bc_a14'], \
                  ['OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','OM_NIAIAC','pom_a14'], \
                  ['SOA_NAA1','SOA_NAA1','SOA_NAA1','SOA_NAA1','soa_a12'], \
                  ['mmr_DUST','mmr_DUST','mmr_DUST','mmr_DUST','dst_a123'], \
                  ['mmr_SALT','mmr_SALT','mmr_SALT','mmr_SALT','ncl_a123']]

    ngroup=len(vargrouplist)

    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   0-20 km
###########
    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE'], \
                  ['CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ]]

    ngroup=len(vargrouplist)

    figlayoutlist3=[figlayout20km]
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
#        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist3, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

# 7. NorESM2/NorESM2.5/CESM2 + aer2014 + bc2014 + oc2014 + sulfate2014
#---------------------------------------------------------------------
    expidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850frc2norbc_aer2014_f09_20200108', \
               'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
               'nf1850_aer2014bc_ne30pg3_ne30pg3_mtn14.fatessp_20250320', \
               'nf1850_aer2014OM_ne30pg3_ne30pg3_mtn14.fatessp_20250320', \
               'nf1850_aer2014S_ne30pg3_ne30pg3_mtn14.fatessp_20250320', \
               'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[5,5,5,5,5,5,5,5]
    year1list=[7,7,7,7,7,5,5,5]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,0,1,1,3,3,3,2]
    linestylelist=[0,2,0,2,1,3,4,0]
    legendlist=['1x1 NorESM2', \
                'aer 2014', \
                '1x1 NorESM2.5', \
                'aer 2014', \
                'bc 2014', \
                'om 2014', \
                'so2 2014', \
                '1x1 CESM3']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description=''
    code='n20250407_noresm2.5_cesm3_plus2014all'
#
#   0-20 km
###########
    vargrouplist=[['CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ','CLDLIQ'], \
                  ['CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE','CLDICE'], \
                  ['NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ','NUMLIQ'], \
                  ['NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE','NUMICE'], \
                  ['CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ,'CLOUD' ]]

    ngroup=len(vargrouplist)

    figlayoutlist3=[figlayout20km]
    for igroup in range(ngroup) :

        varlist=vargrouplist[igroup]
        loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist3, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()
