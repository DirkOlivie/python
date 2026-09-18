import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[1000.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[1300.,1700.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.2025-12-19', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.LandSpinup.2025-12-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run3.2025-12-30', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run4.2026-01-06', \
           'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08', \
           'n1850.ne16pg3_tn14.noresm3_0_beta10.Run6.2026-01-23', \
           'n1850.ne16pg3_tn14.noresm3_0_beta10.Run7.2026-01-26', \
           'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.2026-02-07', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta13.Run11.2026-04-15', \
#
           'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-04-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-05-04', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.Olivia.2026-05-05', \
           'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12_ATMtune.Olivia.2026-05-10', \
           'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12_ATMtune2.Olivia.2026-05-12', \
           'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.c8_4p55.Olivia.2026-05-13', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.Olivia.2026-05-18', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.4p95', \
           'n1850Gg.ne16pg3_tn14_gl4.noresm3_0_beta16.Run13.Olivia.2026-05-18_pseudo_hybrid', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14.Olivia.2026-05-28', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A.Olivia.2026-06-01', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A2.Olivia.2026-06-03', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-B.Olivia.2026-06-03', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-C.Olivia.2026-06-04', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-D.Olivia.2026-06-04', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F.Olivia.2026-06-05']
          
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
            'b09/10/11/12/12a (2x2, #385)','','','','','','','','','', \
             \
            'b13 (2x2)', \
             \
            'b14 (2x2, #404)', \
            'b14 (2x2, #420)', \
             \
            'b15 (2x2, #421)', \
            'b15 (2x2, #427)', \
            'b15 (2x2, ATMtun2)', \
            'b15 (2x2, c8=4.55)', \
             \
            'b16 (2x2, #439)', \
#           'b16 (2x2, dstssltc8)', \
            'b16 (2x2, #444)', \
             \
            'b18 (2x2, #442, R14)', \
            'b18 (2x2, R14-A)', \
            'b18 (2x2, R14-A2)', \
            'b18 (2x2, R14-B)', \
            'b18 (2x2, R14-C)', \
            'b18 (2x2, R14-D)', \
            'b18 (2x2, R14-F)', \
           ]
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0,0,0,0,0,0,0, 0, 0,0, 0,0,0,0, 0,0, 0,0,0,0,0,0,0]
#
shiftlist=[-1199+1300,-1599+1300, 0,0,0,0,0,0,0,0,0,0, 0, 0,0, 0,0,0,0, 0,0, 0,0,0,0,0,0,0]
#
colorlist     =   [0,1, 2,2,2,2,2,2,2,2,2,2, 3, 4,5, 6,7,8,9, 10,11, 12,13,14,15,16,17,18]

linestylelist =   [2,0, 0,0,0,0,0,0,0,0,0,0, 0, 0,0, 0,0,0,0, 0,0, 0,0,0,0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=[\
#              'SOLIN', \
              'SFDST_A2','SFDST_A3', \
              'DF_SO2', 'DF_H2O2', 'DF_H2SO4', \
              'FSDS','FSDSC', \
              'PRECC','PRECL', \
              'TREFHT','QREFHT','LHFLX','FSLNT','SWCF','LWCF','PRECT','CLDTOT', \
              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp','U10', \
              'tempocn','sssgaocn','sstgaocn','salngaocn', \
              'cb_DMS','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT']
#              'SOA_A1NA_columnburden']
#              'cb_SOA_A1NA']
#             'AODVISdivDAYFOC'
typevarlist=['glob']
freqtype='YEA'
#
code='n20260512_noresm2.5_picontrol'
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
nexpid=len(expidlist)
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablegrouplist=[\
                   ['AOD_VISdivDAYFOC']*2+['AODVISdivDAYFOC']*(nexpid-2)]
#                   ['cb_SOA_A1']*2+['SOA_A1_columnburden']*(nexpid-2), \
#                   ['cb_SOA_NA']*2+['SOA_NA_columnburden']*(nexpid-2), \
#                   ['cb_SOA_A1NA']*2+['SOA_A1NA_columnburden']*(nexpid-2)]    
#                    'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
#                    'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
#                    'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', 
#                    'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']
for variablelist in variablegrouplist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

