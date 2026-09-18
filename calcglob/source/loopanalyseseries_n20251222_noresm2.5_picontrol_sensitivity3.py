import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[800.,1300.])


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
#           'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.Olivia.2026-03-08', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8_CAMandOCNtuning.Olivia.2026-03-08', \
            \
#           'n1850.ne16pg3_tn14.noresm3_0_beta10.beff025.2026-02-20', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta11.CAMtuning.20260220', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta11.CAMtuning.20260224', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta11.Run7.OcnTun.20260224'] 
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
            \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff.2026-03-19', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff_TUNED.2026-03-20', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff_TUNED.Olivia.2026-03-22', \
            \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.ndiff_surface_align.20260317', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.lamult_reduction.20260314', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_sameOcnDiff.2026-03-19', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.OcnTun.20260321', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOff_TUNED.Olivia.2026-03-22', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffNoMin.2026-03-26', \
#           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffNoMinOsl.2026-03-27', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_preIceOffOsl_TUNED.Olv.2026-03-30', \
#
           'n1850.ne16pg3_tn14.noresm3_0_beta12.nl363c8beff.2026-03-16', \
#
           'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9_vtrmi0p8.20260412' \
          ]
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
            'b09/10/11/12 (2x2, #365)','','','','','','','','', \
#            'b10 (2x2, beff025)', \
#            'b11 (2x2, #354)', \
#            'b11 (2x2, #356)', \
#            'b11 (2x2, OcnTun)']
            'b12a (2x2, #385)', \
             \
#            'b12 (2x2, #372)', \
#            'b12 (2x2, #374)', \
            'b12 (2x2, #374, Olivia)', \
             \
#            'b12 (2x2, #380)', \
#            'b12 (2x2, #381)', \
#            'b12 (2x2, #373)', \
#            'b12 (2x2, #383)', \
             \
            'b12 (2x2, #373)', \
            'b12 (2x2)', \
            'b12 (2x2, #384)', \
            'b12 (2x2)']
#
legendlist=['MM (1x1)', \
            'LM (2x2)', \
#
            '','','','','','','','','b09/10/11/12', \
#            'b10 (2x2, beff025)', \
#            'b11 (2x2, #354)', \
#            'b11 (2x2, #356)', \
#            'b11 (2x2, OcnTun)']
            'b12a #385', \
             \
#            'iOff #372', \
#            'iOff_TN #374', \
#            'iOFF_TN.Ol #374', \
             \
#            '#380', \
#            '#381', \
#            '#373', \
#            '#383', \
             \
#            'sameOcnDiff #373', \
#            'iOffNoMin', \            
            'iOFF_TN.Ol #374', \
#            'iOffNoMinOsl #384', \
            'iOffOsl_TN.Ol #388', \
#
            'Berg-Find #370', \
#
            'vtrmix0.8 #392']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0,0,0,0,0,0, 0, 0,0, 0, 0]#, 0,0,0,0]
#
shiftlist=[-1199+800,-1599+800, 0,0,0,0,0,0,0,0,0, 0, 0,0, 0, 0]#, 0,0,0,0]
#
#colorlist     =   [0,1, 2,3,4,5,6,7,8, 9,10,11,12, 13,14,15,16,17,18,19,20]
colorlist     =   [0,1, 2,2,2,2,2,2,2,2,2, 3, 4,5, 7, 8]# ,11,12,13,14]

linestylelist =   [2,0, 0,0,0,0,0,0,0,0,0, 0, 0,0, 0, 0]#, 0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=[\
              'SOLIN', \
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
code='n20251222_noresm2.5_picontrol_sensitivity3'
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
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC', \
#              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']


loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# DRAKE PASSAGE
description='typevarcommon-varcommon'
#i=15
#del expidlist[i:i+2]
#del legendlist[i:i+2]
#del smoothlist[i:i+2]
#del shiftlist[i:i+2]
#del colorlist[i:i+2]
#del linestylelist[i:i+2]


i=11
del expidlist[i]
del legendlist[i]
del smoothlist[i]
del shiftlist[i]
del colorlist[i]
del linestylelist[i]

reflist=expidlist

freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



