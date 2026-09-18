import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,250.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,300.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
           'n1850.ne30pg3_tn14.noresm3_0_beta12a-run1_yr001_olivia.20260313', \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run4_yr061.20260429', \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run5_yr076.20260504', \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run7_yr101.20260508', \
            \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run6_yr001.20260505', \
            \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run10_yr101.20260513', \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run12_yr101.20260516', \
            \
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run13_yr101.20260521', \
            \
           'n1850.ne30pg3_tn14.noresm3_0_beta15-run12_yr151.cplhist.20260529', \
           'n1850.ne30pg3_tn14.noresm3_0_beta18.20260530', \
           'n1850.ne30pg3_tn14.noresm3_0_beta18.20260606' 
            ]
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
             \
            'b12a (1x1, #368)', \
            'b14 (1x1, #418)', \
            'b14 (1x1, #419)', \
            'b14 (1x1, #425)', \
             \
            'b14 (1x1, #422)', \
             \
            'b14 (1x1, #428)', \
            'b14 (1x1, #430)', \
             \
            'b14 (1x1, #441)', \
             \
            'b15 (1x1, #445)', \
            'b18 (1x1, #443)', \
            'b18 (1x1, #447)'  \
           ]
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0, 0, 0,0, 0,0,0,0]
#
shiftlist=[-1199,-1599, 0,0,0,0, 0, 0,0, 0,0,0,0]
#
colorlist     =   [0,1, 2,3,4,5, 6, 7,8, 9,10,11,12]

linestylelist =   [2,2, 0,0,0,0, 0, 0,0, 0,0,0,0]
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
code='n20260512_noresm2.5_picontrol_ne30pg3'
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
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

