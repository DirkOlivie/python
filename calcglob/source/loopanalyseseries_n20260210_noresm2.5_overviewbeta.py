import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1500.])
#figlayout=cfiglayout.CFigLayout(xrange=[0.,500.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
#           b01
           'n1850.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250708', \
           'n1850.ne16pg3_tn14.nor3_b01-cplhist.20250716', \
           'n1850.ne16pg3_tn14.nor3_b01.20250731', \
#           b02
#          'n1850.ne16_tn14.noresm3_0_beta02-run1_yr001.20250825', \
           'n1850.ne16_tn14.noresm3_0_beta02-run2_yr001.20250829', \
#           b03/b06                    
           'n1850.ne16_tn14.noresm3_0_beta03_rafsipmasstonum.20250930', \
           'n1850.ne16_tn14.noresm3_0_beta03a-run1_yr061.20251009', \
           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta03a.2025-10-10', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03a.landAndCAMupdate.2025-10-16', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.2025-10-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST.2025-10-29', \
           'n1850.ne16pg3_tn14.noresm3_0_beta03b.CPLHIST_C8_4p8.2025-11-01', \
           'n1850.ne16pg3_tn14.hybrid_fates-nocomp.noresm3_0_beta06.Best_c8_4p8.2025-11-26', \
           'n1850.ne16pg3_tn14.noresm3_0_beta06.Best_c8_4p7.2025-12-01', \
#           b09/b10/b11
           'n1850.ne16pg3_tn14.noresm3_0_beta09.2025-12-19', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.LandSpinup.2025-12-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run3.2025-12-30', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run4.2026-01-06', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08', \
           'n1850.ne16pg3_tn14.noresm3_0_beta10.Run6.2026-01-23', \
           'n1850.ne16pg3_tn14.noresm3_0_beta10.Run7.2026-01-26', \
           'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.2026-02-07']
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
             \
            'b01 (2x2)','','', \
            'b02 (2x2)', \
            'b03/b06 (2x2)','','','','','','','','', \
            'b09/b10/b11 (2x2)','','','','','','','']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
a=300
b=a+50
c=b+510


smoothlist=[0,0, 0,0,0, 0, 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0]
#
shiftlist=[-1199,-1599, 0,0,0, a ,b,b,b,b,b,b,b,b,b, c,c,c,c,c,c,c,c]
#shiftlist=[-1199,-1599, 0,0,0, a,a,a,a,a,a,a,a,a,a,a,a, a,a,a,a,a,a,a,a]
#shiftlist=[-1199,-1599, 0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0]
#shiftlist=[-1199,-1599, 0,0,0, 300,300,300,300,300,300,300,300,300, 810,810,810,810,810,810,810,810]
#
#colorlist     =   [0,1, 2,3,4,5,6,7,8, 9,10,11,12, 13,14,15,16,17,18,19,20]
colorlist     =   [0,1, 2,2,2, 5, 3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4]
linestylelist =   [2,0, 0,0,0, 0, 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=[\
#             'SOLIN', \
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
code='n20260210_noresm2.5_overviewbeta'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# FSLNT
freqtype='YEA'
typevarlist=['90S28S','28S28N','28N60N','60N90N']
variablelist=['FSLNT']
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
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC',
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']

loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
