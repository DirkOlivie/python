import numpy as np

import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(axhline=[0.])
#figlayout=cfiglayout.CFigLayout()

generalcode='n20260426_noresm2.5_picontrol_energydiag'


# 1. NORESM2.5 : ne16pg3
#------------------------------------------------------------------------
#
expidlist=[ \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.2025-12-19', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.LandSpinup.2025-12-24', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run3.2025-12-30', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run4.2026-01-06', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08', \
          'n1850.ne16pg3_tn14.noresm3_0_beta10.Run6.2026-01-23', \
          'n1850.ne16pg3_tn14.noresm3_0_beta10.Run7.2026-01-26', \
          'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.2026-02-07', \
          'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11', \
          'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28']
#
nexpid=len(expidlist)
#
legendlist=[ \
            '2025-12-19', \
            '2025-12-24', \
            'Run3','Run4','Run5','Run6','Run7','Run8','Run9','Run10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0]*nexpid
#
shiftlist=[0]*nexpid
#
colorlist     =  [0,1,2,3,4,5,6,7,8,9]

linestylelist =   [0]*nexpid
#

description='typevarcommon-varcommon'
variablelist=[\
             'diagsumheatsum','diagsumheatatm','diagsumheatlnd','diagsumheatrof','diagsumheatice','diagsumheatglc','diagsumheatocn'] 
typevarlist=['glob']
freqtype='YEA'
#
code=generalcode+'_ne16pg3'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# 2. NORESM2.5 : ne30pg3
#------------------------------------------------------------------------
#
expidlist=[ \
          'n1850.ne30_tn14.noresm3_0_beta03a-run1_yr001.20251016', \
#          'n1850.ne30_tn14.noresm3_0_beta03b-run1_yr001.20251021', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr031_eminatred.20251031', \
#          'n1850.ne30_tn14.noresm3_0_beta04-run1_yr001.20251103', \ very much out of balance
#          'n1850.ne30_tn14.nor3_b05-rc1-run1_yr001.20251110', \
          'n1850.ne30_tn14.noresm3_0_beta06-run1_yr001.20251114', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr001.20251223', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr031.20251227', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr051_cplhist.20251230', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_lowmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_highmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.20251220', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.v2.20251222', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_lowdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_highdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run1_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run2_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run3_yr001.20260226', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run1_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run2_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run3_yr101.20260123', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run4_yr101.20260126', \
#         'n1850.ne30pg3_tn14.noresm3_0_beta10-run5_yr121.20260127', \
#          'n1850.ne30pg3_tn14.noresm3_0_beta10-run6_yr121.20260128', \
#          'n1850.ne30pg3_tn14.noresm3_0_beta10-run7_yr121.20260128', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run8_yr121.20260131']
#
nexpid=len(expidlist)
#
legendlist=['']*nexpid
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0]*nexpid
#
shiftlist=[0]*nexpid
#
colorlist     =  range(0,nexpid)

linestylelist =   [0]*nexpid
#

description='typevarcommon-varcommon'
variablelist=[\
             'diagsumheatsum','diagsumheatatm','diagsumheatlnd','diagsumheatrof','diagsumheatice','diagsumheatglc','diagsumheatocn'] 
typevarlist=['glob']
freqtype='YEA'
#
code=generalcode+'_ne30pg3'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# 3. CESM3 (#316)
#------------------------------------------------------------------------
#
expidlist=[ \
           'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']
#
nexpid=len(expidlist)
#
legendlist=['CESM3 (#316)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0]*nexpid
#
shiftlist=[0]*nexpid
#
colorlist     =  range(0,nexpid)

linestylelist =   [0]*nexpid
#

description='typevarcommon-varcommon'
variablelist=[\
             'diagsumheatsum','diagsumheatatm','diagsumheatlnd','diagsumheatrof','diagsumheatice','diagsumheatglc','diagsumheatocn'] 
typevarlist=['glob']
freqtype='YEA'
#
code=generalcode+'_cesm3'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
