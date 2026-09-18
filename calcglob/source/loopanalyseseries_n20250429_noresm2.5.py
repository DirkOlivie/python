import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
figlayout=cfiglayout.CFigLayout(xrange=[0.,60.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['NF1850frc2norbc_f09_20200108', \
           'NF1850norbc_f19_f19_20241127_test13', \
           'NF1850norbc_f19_f19_20241127_test14', \
           'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
           'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408', \
           'n1850.ne30_tn14.hybrid_fates-nocomp_spinup.3.0a02.20250415', \
           'FHIST_f19_f19_mg17_20211015']
#           'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2.3', \
            'NorESM2.3 (with SI)', \
            'NorESM2.5', \
            'NorESM3 (3.0a02, DCS=500)', \
            'NorESM3 (3.0a02, DCS=600)', \
            'CESM2']
#            'CESM3']
#
smoothlist=[0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,-1849]
#
colorlist=[0,1,1,2,3,3,4]
linestylelist=[0,0,2,0,0,2,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
typevarlist=['glob']
#
code='n20250429_noresm2.5_cesm3'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['NF1850frc2norbc_f09_20200108', \
           'NF1850norbc_f19_f19_20241127_test13', \
           'NF1850norbc_f19_f19_20241127_test14', \
           'nf1850_ne30pg3_ne30pg3_mtn14.fatessp_20250317', \
           'n1850.ne30_tn14.hybrid_fates-nocomp.3.0a02.20250408', \
           'n1850.ne30_tn14.hybrid_fates-nocomp_spinup.3.0a02.20250415', \
           'FHIST_f19_f19_mg17_20211015', \
           'b.e30_alpha06b.B1850C_LTso.ne30_t232_wgx3.152']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2', \
            'NorESM2.3', \
            'NorESM2.3 (with SI)', \
            'NorESM2.5', \
            'NorESM3 (3.0a02, DCS=500)', \
            'NorESM3 (3.0a02, DCS=600)', \
            'CESM2', \
            'CESM3']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,-1849,0]
#
colorlist=[0,1,1,2,3,3,4,5]
linestylelist=[0,0,2,0,0,2,0,0]
#

# tempocn
description='typevarcommon'
vargrouplist=[['SFDMS','SFDMS','SFDMS','SFDMS','SFDMS','SFDMS','SFDMS','OCN_FLUX_DMS']]
typevarlist=['glob']
#
code='n20250429_noresm2.5_cesm3'
#
ngroup=len(vargrouplist)
for igroup in range(ngroup) :

    variablelist=vargrouplist[igroup]
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
