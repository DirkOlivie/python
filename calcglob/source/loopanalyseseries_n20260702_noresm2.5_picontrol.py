import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[1000.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[1350.,1700.])
figlayout=cfiglayout.CFigLayout(xrange=[1530.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[ 900.,1780.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
#           'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15.Olivia.2026-06-08', \
#           'n1850esm.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07', \
           'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
           'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-04-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.Olivia.2026-05-05', \
           'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.Olivia.2026-05-18', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F.Olivia.2026-06-05', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-B.Olivia.2026-06-11', \
           'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-C.Olivia.2026-06-15', \
           'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-D.Olivia.2026-06-17', \
           'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-E.Olivia.2026-06-18', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta20.Run15-F.Olivia.2026-06-22', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta20.470.ref461.20260626', \
           'n1850.ne16pg3_tn14.noresm3_0_beta20.473.ref461.20260630', \
           'n1850.ne16pg3_tn14.noresm3_0_beta20.474.ref461.20260630', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.476.2026-07-03', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.i478.2026-07-06', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.i480.2026-07-16', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260717', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.i482.2026-07-23', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260723', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.cmeps-latent-heat-bugfix.2026-07-23']


#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
             \
            'b12a-16 (2x2)','','','','', \
\
#            'b19 (2x2, R15)', \
#            'b19 (2x2, CO2, #451)', \
             \
            'b19 (2x2, R15-B, #455)', \
            'b19 (2x2, R15-C, #459)', \
            'b19 (2x2, R15-D)', \
            'b19 (2x2, R15-E, #461)', \
             \
            'b20 (2x2, R15-F, #463)', \
             \
            'b20 (2x2, #470)', \
            'b20 (2x2, #473)', \
            'b20 (2x2, #474)', \
             \
            'b21 (2x2, #476)', \
            'b21 (2x2, #478)', \
            'b21 (2x2, #480)', \
            'b21 (2x2, #481)', \
             \
            'b21 (2x2, #482)', \
            'b21 (2x2, #483)', \
            'b21 (2x2, #484)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0, 0,0,0,0, 0, 0,0,0, 0,0,0]
shiftlist=[-1199+1531,-1599+1531, 0,0, 0,0,0,0, 1531-926, 0,0,0, 1531-926,1531-926,1531-926]
colorlist     =   [0,1, 2,3, 4,5,6,7, 8, 9,10,11, 12,13,14]
linestylelist =   [2,2, 0,0, 0,0,0,0, 0, 0,0,0, 0,0,0]
#
smoothlist=[0,0, 0,0,0,0,0, 0,0,0,0, 0, 0,0,0, 0,0,0,0, 0,0,0]
shiftlist=[-1199+1531,-1599+1531, 0,0,0,0, 1531-926, 0,0,0, 1531-926,1531-926,1531-926,1531-926,1531-926,1531-926]
shiftlist=[-1199+901,-1599+901, 0,0,0,0,0, 0,0,0,0, 0, 0,0,0, 0,0,0,0, 0,0,0]
colorlist     =   [0,1, 2,2,2,2,2, 4,5,6,7, 8, 9,10,11, 12,13,14,15, 16,17,18]
linestylelist =   [1,1, 0,0,0,0,0, 0,0,0,0, 0, 0,0,0, 0,0,0,0, 0,0,0]
linewidthlist = [1,1, 1,1,1,1,1, 1,1,1,1, 1, 1,1,1, 2,2,2,2, 2,2,2]

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
code='n20260702_noresm2.5_picontrol'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)


# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)

# AMOC
freqtype='YEA'
typevarlist=['glob','atlarc']
variablelist=['mmflxdmax26.0Nocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)

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
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)

