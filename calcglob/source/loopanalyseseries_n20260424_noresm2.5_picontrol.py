import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[800.,1450.])


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
#           'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_drydep_oldBLOM.2026-04-17', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_oldBLO_oldBLOMv32.2026-04-17', \
           'n1850.ne16pg3_tn14.noresm3_0_beta13.Run11.2026-04-15', \
           'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-04-24', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff_TUNED.Olivia.2026-03-22', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffOsl_TUNED.Olv.2026-03-30', \
#
           'n1850.ne16pg3_tn14.noresm3_0_beta12.nl363c8beff.2026-03-16', \
#
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_vtrmi0p8.20260412', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_tiedkeadd_tuning.20260421', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11.OcnTune2026-04-19' \
          ]
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
            'b09/10/11/12/12a (2x2, #385)','','','','','','','','','', \
             \
#            'b13a (2x2)', \
#            'b13a (2x2, #396)', \
            'b13 (2x2)', \
            'b14 (2x2, #404)', \
             \
            'b12 (2x2, no PI)', \
            'b12 (2x2, #388)', \
             
            'b12 (2x2, #370, BF)', \
            'b12 (2x2, #392, vtrmi)', \
            'b12 (2x2, tiedke)', \
            'b12 (2x2, Ada)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0, 0,0,0,0]
#
shiftlist=[-1199+800,-1599+800, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0, 0,0,0,0]
#
colorlist     =   [0,1, 2,2,2,2,2,2,2,2,2,2, 3,4,5,6, 7,8,9,10]

linestylelist =   [2,0, 0,0,0,0,0,0,0,0,0,0,  0,0,0,0, 0,0,0,0]#, 0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=[\
#              'SOLIN', \
              'DF_SO2', 'DF_H2O2', 'DF_H2SO4', \
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
code='n20260424_noresm2.5_picontrol'
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
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']


loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

