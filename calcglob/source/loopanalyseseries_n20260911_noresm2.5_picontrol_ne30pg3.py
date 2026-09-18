import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


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
           'n1850.ne30pg3_tn14.noresm3_0_beta14-run12_yr101.20260516', \
            \
           'N1850.n30b23MM.i496.20260815', \
           'N1850.n30b23MM.506.20260821', \
           'N1850.MM.nor30b23.509.20260901', \
           'N1850.MM.nor30b24.515.20260908', \
           'N1850.MM.nor30b24.520.20260913' \
            ]
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
             \
            'b12a (1x1, #368)', \
            'b14 (1x1, #418)', \
            'b14 (1x1, #419)', \
            'b14 (1x1, #425)', \
            'b14 (1x1, #430)', \
             \
            'b23 (1x1, #496)', \
            'b23 (1x1, #506)', \
            'b23 (1x1, #509)', \
            'b24 (1x1, #515)', \
            'b24 (1x1, #520)'  \
           ]
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0,0, 0,0,0,0,0]
#
shiftlist=[-1199,-1599, 0,0,0,0,0, 0,0,0,0,0]
#
colorlist     =   [0,1, 2,2,2,2,2, 3,4,5,6,7]

linestylelist =   [2,2, 0,0,0,0,0, 0,0,0,0,0]

linewidthlist = [1,1, 1,1,1,1,1, 2,2,2,2,2]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=[\
#              'SFDST_A2','SFDST_A3', \
#              'DF_SO2', 'DF_H2O2', 'DF_H2SO4' : only DF_SO2 in new output
              'FSDS','FSDSC', \
#              'PRECC','PRECL', \  # PRECL not in new output
#              'PRECT'
              'TREFHT','QREFHT','LHFLX','FSLNT','SWCF','LWCF','CLDTOT', \
#              'SFDMS','EMI_DUST_TOT_noresm2','EMI_SALT_TOT_noresm2','SFisoprene','SFmonoterp',
              'U10', \
              'tempocn','sssgaocn','sstgaocn','salngaocn']
#              'cb_DMS','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT' : not in new output

typevarlist=['glob']
freqtype='YEA'
#
code='n20260911_noresm2.5_picontrol_ne30pg3'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)


# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)

# AMOC
freqtype='YEA'
typevarlist=['glob','atlarc']
variablelist=['mmflxdmax26.0Nocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)

# DRAKE PASSAGE
freqtype='YEA'
typevarlist=['drake_passage']
variablelist=['voltrocn']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)

# AOD 
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablelist=[\
              'AOD_VISdivDAYFOC','AOD_VISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC', \
              'AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC','AODVISdivDAYFOC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)

# MISCELANEOUS
nexpid=len(expidlist)
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablegrouplist=[\
#                   ['AOD_VISdivDAYFOC']*2+['AODVISdivDAYFOC']*(nexpid-2)
                   ['PRECCPRECL']*(nexpid)+['PRECT']*0, \
                   ['SFDMS']*(nexpid)+['emis_DMS']*0, \
                   ['EMI_DUST_TOT_noresm2']*(nexpid)+['emis_DUST']*0, \
                   ['EMI_SALT_TOT_noresm2']*(nexpid)+['emis_SALT']*0 \
#                   ['SFisoprene']*(nexpid-9)+['emis_isoprene']*9, \
#                   ['SFmonoterp']*(nexpid-9)+['emis_monoterp']*9 \
                  ]
for variablelist in variablegrouplist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist, linewidthlist=linewidthlist)



