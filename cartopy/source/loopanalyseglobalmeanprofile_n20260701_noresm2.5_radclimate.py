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
#    figlayout20km=cfiglayout.CFigLayout(code='standard',yrange=[0.,20.])
    
#
#   1. prescribed versus online-calculated [global] : CO2
#-----------------------------------------
    code='n20260701_noresm2.5_radclimate'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000', \
               'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000', \
               'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000,2000]
    year1list=[2001,2001,2001]
    seasonlist=['YEA','YEA','YEA']
    linestylelist=[0,0,0]
    colorlist    =[0,1,2]
    legendlist=['b19 (2x2, conCO2-rad)', \
                'b19 (2x2, emiCO2-rad)', \
                'b19 (2x2, emiCO2-trc)']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='regioncommon'
#
    varlist=['m_CO2_c_as_vmr','m_CO2_c_as_vmr','CO2_as_vmr']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   2. prescribed : NH versus SH 
#-------------------------------
    code='n20260701_noresm2.5_radclimate_conc_region'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000', \
               'nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000', \
               'nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000,2000]
    year1list=[2001,2001,2001]
    seasonlist=['YEA','YEA','YEA']
    linestylelist=[0,0,0]
    colorlist    =[0,1,2]
    legendlist=['b19 (2x2, conCO2-rad, NH)', \
                'b19 (2x2, conCO2-rad, TR)',\
                'b19 (2x2, conCO2-rad, SH)']
    regionlist=['NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['m_CO2_c_as_vmr']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
#   3. interactive : NH versus SH [CO2]
#-------------------------------
    code='n20260701_noresm2.5_radclimate_emis_region'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000', \
               'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000', \
               'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000,2000]
    year1list=[2001,2001,2001]
    seasonlist=['YEA','YEA','YEA']
    linestylelist=[0,0,0]
    colorlist    =[0,1,2]
    legendlist=['b19 (2x2, conCO2-rad, NH)', \
                'b19 (2x2, conCO2-rad, TR)',\
                'b19 (2x2, conCO2-rad, SH)']
    regionlist=['NH','28S28N','SH']
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['CO2_as_vmr']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

#   4. nhist : NH, seasonal cycle
#--------------------------------
    code='n20260701_noresm2.5_radclimate_hist_conc_season'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000']*36
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000]*36
    year1list=[2000]*36
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0, \
                   1,1,1,1,1,1,1,1,1,1,1,1, \
                   2,2,2,2,2,2,2,2,2,2,2,2]
    colorlist    =[0,1,2,3,4,5,6,7,8,9,10,11, \
                   0,1,2,3,4,5,6,7,8,9,10,11,
                   0,1,2,3,4,5,6,7,8,9,10,11]
    legendlist=['NH','','','','','','','','','','','', \
                '28S28N','','','','','','','','','','','', \
                'SH','','','','','','','','','','','']
    regionlist=['NH']*12+['28S28N']*12+['SH']*12
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['m_CO2_c_as_vmr','m_CH4_c_as_vmr','m_N2O_c_as_vmr']
    varlist=['m_CO2_c_as_vmr_drytest','m_CH4_c_as_vmr_drytest','m_N2O_c_as_vmr_drytest']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

#   5. nhistesm : NH, seasonal cycle
#-------------------------------
    code='n20260701_noresm2.5_radclimate_histesm_conc_season'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.radclimate.r2000.aco2']*36
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000]*36
    year1list=[2000]*36
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0, \
                   1,1,1,1,1,1,1,1,1,1,1,1, \
                   2,2,2,2,2,2,2,2,2,2,2,2]
    colorlist    =[0,1,2,3,4,5,6,7,8,9,10,11, \
                   0,1,2,3,4,5,6,7,8,9,10,11,
                   0,1,2,3,4,5,6,7,8,9,10,11]
    legendlist=['NH','','','','','','','','','','','', \
                '28S28N','','','','','','','','','','','', \
                'SH','','','','','','','','','','','']
    regionlist=['NH']*12+['28S28N']*12+['SH']*12
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['m_CO2_c_as_vmr','m_CH4_c_as_vmr','m_N2O_c_as_vmr']
    varlist=['m_CO2_c_as_vmr_drytest','m_CH4_c_as_vmr_drytest','m_N2O_c_as_vmr_drytest']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#

#   6. histghg : NH, seasonal cycle
#-------------------------------
    code='n20260701_noresm2.5_radclimate_histghg_conc_season'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhistghg.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000']*36
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000]*36
    year1list=[2000]*36
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0, \
                   1,1,1,1,1,1,1,1,1,1,1,1, \
                   2,2,2,2,2,2,2,2,2,2,2,2]
    colorlist    =[0,1,2,3,4,5,6,7,8,9,10,11, \
                   0,1,2,3,4,5,6,7,8,9,10,11,
                   0,1,2,3,4,5,6,7,8,9,10,11]
    legendlist=['NH','','','','','','','','','','','', \
                '28S28N','','','','','','','','','','','', \
                'SH','','','','','','','','','','','']
    regionlist=['NH']*12+['28S28N']*12+['SH']*12
    verticalaxislist=['height']
#
    description='varcommon'
#
#   varlist=['m_CO2_c_as_vmr','m_CH4_c_as_vmr','m_N2O_c_as_vmr']
    varlist=['m_CO2_c_as_vmr_drytest','m_CH4_c_as_vmr_drytest','m_N2O_c_as_vmr_drytest']
#   varlist=['CO2','CH4','N2O'] 
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#


if __name__ == '__main__':
    main()
