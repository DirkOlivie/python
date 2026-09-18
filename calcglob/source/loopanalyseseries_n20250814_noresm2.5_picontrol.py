import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout(xrange=[0.,500.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
#           'n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513', \
            \
#           'n1850.ne30_tn14.noresm3_0_beta01-noLU_650dcs_4p0clubbc8_0p5dust.20250708ext', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708ext', \
            \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
#           'n1850.ne16_tn14.noresm3_0_beta02-run1_yr001.20250825', \
#           'n1850.ne16_tn14.noresm3_0_beta02-run2_yr001.20250829', \
            \
#           'n1850.ne16_tn14.nor3_b03-rc3.20250925ext', \
#           'n1850.ne16_tn14.nor3_b03-rc3_rafsipoff.20250928', \
           'n1850.ne16_tn14.noresm3_0_beta03_rafsipmasstonum.20250930', \
            \
           'n1850.ne16_tn14.noresm3_0_beta03a-run1_yr061.20251009', \
           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta03a.2025-10-10', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta03a.landAndCAMupdate.2025-10-16', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.2025-10-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.2025-10-29', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST_C8_4p8.2025-11-01', \
            \
#           'n1850.ne30_tn14.noresm3_0_beta03a-run1_yr001.20251016', \
#           'n1850.ne30_tn14.noresm3_0_beta03b-run1_yr001.20251021', \
#           'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023', \
#           'n1850.ne30_tn14.noresm3_0_beta04-run1_yr001.20251103', \
#           'n1850.ne30_tn14.nor3_b05-rc1-run1_yr001.20251110', \
#           n1850.ne30_tn14.noresm3_0_beta03b-run2_yr031_eminatred.20251031']
           'n1850.ne16pg3_tn14.noresm3_0_beta06.20251114', \
#
#           'n1850.ne16pg3_tn14.noresm3_0_beta06.dmaxbo4.20251120', \
#
#           'n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.MedlSpit.2025-11-23', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.b06_settingsV3.2025-11-23', \
#           \
#           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.revertall.2025-11-25', \
#           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.Best.2025-11-25', \
#           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.oldDmax.2025-11-25', \
#           \
           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.Best_c8_4p8.2025-11-26', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.Best_c8_4p7.2025-12-01', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.PPEbasedTuning.2025-12-04', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.PPEbasedV2.2025-12-08', \
            \
           'n1850.ne16pg3_tn14.nor3_b06_floedim.20251205', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.BDMC21.8.20251209', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.EGC2.5_EGIDFQ1.25.20251209', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.CombinedTuning.20251209', \
            \
           'n1850.ne30_tn14.noresm3_0_beta06-run1_yr001.20251114', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta06-ref_yr001.20251209', \
           'n1850.ne16pg3_tn14.noresm3_0_beta07-ref_yr001.20251209', \
           'n1850.ne16pg3_tn14.noresm3_0_beta08-ref_yr001.20251209']  
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
#            'a03b (1x1)', \
#            'b01 (1x1, tuned)', \
#            'b01 (2x2, tuned)', \
            'NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
#            'b02 (2x2, run1)', \
#            'b02 (2x2, run2)', \
#            'b03 (2x2)', \
#            'b03 (2x2, rafsip off)', \
#            'b03 (2x2, corr.)', \
#            'b03a (2x2)', \
#            'b03a (2x2, lnd)', \
#            'b03a (2x2, lnd+c0)', \
#            'b03b (2x2, ocn)', \
#            'b03b (2x2, lnd+c0+ocn)', \
#            'b03b (2x2, lnd+c0+ocn)', 
             'b03/b03a/b03b (2x2)','','','','','','', \
#            'b03a (1x1, lnd+c0)', \
#            'b03b (1x1, lnd+c0+)', \
#            'b03b (1x1)', \
#            'b04 (1x1)', \
#            'b05 (1x1)', \
#           'b03b (1x1, nat emi)' ]
            'b06 (2x2)', \
#            'b06 (2x2, dmax b04)', \
#            'b06 (2x2, MedlSpit)', \
#            'b06 (2x2, settingsV3)', \
#            'b06 (2x2, revertall)', \
#            'b06 (2x2, best)', \
#            'b06 (2x2, dmax old)', \
            'b06 (2x2, tuning 1)', \
            'b06 (2x2, tuning 2)', \
            'b06 (2x2, PPEbasedTuning)', \
            'b06 (2x2, PPEbasedV2)', \
#
            'b06 (2x2, floedim)', \
            'b06 (2x2, BDMC2=1.8)', \
            'b06 (2x2, EGC=2.5 and EGIDFQ=1.25)', \
            'b06 (2x2, combined)', \
#        
            'b06 (1x1, 20251114)', \
            'b06 (1x1)', \
            'b07 (1x1)', \
            'b08 (1x1)']

#
smoothlist=[0,0, 0,0,0,0,0,0,0, 0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
#
shiftlist=[-1199,-1599, 0,0,0,0,0,0,0, 0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
#
colorlist     =   [0,1, 2,2,2,2,2,2,2, 3, 4,5,6,7, 8,9,10,11, 12,13,14,15]
linestylelist =   [2,0, 0,0,0,0,0,0,0, 0, 0,0,0,0, 0,0,0,0,  0,0,0,2]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=['SOLIN', \
              'FSDS','FSDSC', \
              'PRECC','PRECL', \
              'TREFHT','QREFHT','LHFLX','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
              'tempocn','sssgaocn','sstgaocn','salngaocn', \
              'cb_DMS','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT']
#             'AODVISdivDAYFOC'
typevarlist=['glob']
freqtype='YEA'
#
code='n20250814_noresm2.5_picontrol'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# AMOC
freqtype='YEA'
typevarlist=['glob','atlarc']
variablelist=['mmflxdmax26.0Nocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# AOD 
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablelist=[\
#             'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']


loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
