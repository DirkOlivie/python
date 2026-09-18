import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
figlayout=cfiglayout.CFigLayout(xrange=[0.,30.])


# 1. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
expidlist=['NF1850frc2norbc_f09_20200108', \
           'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['1x1 NorESM2', \
            '1x1 NorESM2.5']
#
smoothlist=[0,0]
#
shiftlist=[0,0]
#
colorlist=[0,1]
linestylelist=[0,0]
#

# tempocn
description='varcommon-typevarcommon'
variablelist=['EMI_SO2_TOT_noresm2','AQSO4_H2O2','AQSO4_O3','TGCLDCWP','TGCLDIWP','TGCLDLWP', \
              'TAU_DMS','cb_SULFATE', \
              'TAU_isoprene','TAU_monoterp', \
              'TAU_SOA_SV','TAU_SOA_LV', \
              'TAU_BC_noresm2','TAU_SALT_noresm2','TAU_DUST_noresm2', \
              'cb_isoprene','cb_monoterp','cb_SOA_SV','cb_SOA_LV']
typevarlist=['glob']
#
code='n20250407_noresm2.5'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['NF1850frc2norbc_f09_20200108', \
           'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
           'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['1x1 NorESM2', \
            '1x1 NorESM2.5', \
            '1x1 CEMS3']  
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
linestylelist=[0,0,0]
#

# tempocn
description='typevarcommon'
vargrouplist=[['AQSO4_H2O2','AQSO4_H2O2','AQSO4_H2O2'], \
              ['AQSO4_O3','AQSO4_O3','AQSO4_O3'], \
              ['TGCLDIWP','TGCLDIWP','TGCLDIWP'], \
              ['TGCLDLWP','TGCLDLWP','TGCLDLWP'], \
              ['cb_SULFATE','cb_SULFATE','so4_a123_columnburden'], \
              ['TAU_BC_noresm2','TAU_BC_noresm2','TAU_bc_a14_cesm2'], \
              ['TAU_SALT_noresm2','TAU_SALT_noresm2','TAU_ncl_a123_cesm2'], \
              ['TAU_DUST_noresm2','TAU_DUST_noresm2','TAU_dst_a123_cesm2'], \
              ['U10','U10','U10']]
typevarlist=['glob']
#
code='n20250407_noresm2.5_cesm3'
#
ngroup=len(vargrouplist)
for igroup in range(ngroup) :

    variablelist=vargrouplist[igroup]
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

