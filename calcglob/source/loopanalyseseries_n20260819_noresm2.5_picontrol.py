import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[1000.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[1350.,1700.])
figlayout=cfiglayout.CFigLayout(xrange=[1530.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[ 925.,1700.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
           'n1850.ne16pg3_tn14.noresm3_0_beta14.Run11.Olivia.2026-04-24', \
           'n1850.ne16pg3_tn14.noresm3_0_beta15.Run12.Olivia.2026-05-05', \
           'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.Olivia.2026-05-18', \
           'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F.Olivia.2026-06-05', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.i480.2026-07-16', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.i482.2026-07-23', \
           'n1850.ne16pg3_tn14.noresm3_0_beta22.i486.2026-07-31', \
           'n1850.ne16pg3_tn14.noresm3_0_beta22.i489.2026-08-06', \
            \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260717', \
           'n1850.ne16pg3_tn14.noresm3_0_beta21.bdmc2_1p2.20260723', \
           'n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2.20260730', \
           'n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2_cplhist.20260806', \
           'n1850.ne16pg3_tn14.noresm3_0_beta22.bdmc2_1p2.20260811', \
            \
           'n1850Gaxg.ne16pg3_tn14_ais8gris4.noresm3_0_beta22.492.ref490.20260811', \
           'n1850Gaxg.n30b23LM.498.20260815', \
           'n1850Gaxg.n30b23LM.502.20260818',]
#
legendlist=['NorESM2-MM', \
            'NorESM2-LM', \
             \
            'b12a-16','','','','', \
             \
            'b21 (#480)', \
            'b21 (#482)', \
            'b22 (#486)', \
            'b22 (#KJE)', \
             \
            'b21 (#481, 1.2)', \
            'b21 (#483, 1.2)', \
            'b22 (#487, 1.2)', \
            'b22 (#490, 1.2)', \
            'b22 (#495, 1.2)', \
             \
            'b22 (#492, 1.2, GrIS)', \
            'b23 (#498, 1.2, GrIS)', \
            'b23 (#502, 1.2, GrIS)' \
]
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0, 0,0,0]
shiftlist=[-1199+901,-1599+901, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0, 0,0,0]
colorlist     =   [0,1, 2,2,2,2,2, 3,4,5,6, 7,8,9,10,11, 12,13,14]
linestylelist =   [2,2, 0,0,0,0,0, 0,0,0,0, 0,0,0,0,0, 0,0,0]
linewidthlist =   [1,1, 1,1,1,1,1, 2,2,2,2, 2,2,2,2,2, 2,2,2]

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
code='n20260819_noresm2.5_picontrol'
#
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

# AOD : AODVIS is missing !!
nexpid=len(expidlist)
description='typevarcommon'
freqtype='YEA'
typevarlist=['glob']
variablegrouplist=[\
#                   ['AOD_VISdivDAYFOC']*2+['AODVISdivDAYFOC']*(nexpid-2)
                   ['PRECCPRECL']*(nexpid-2)+['PRECT']*2, \
                   ['SFDMS']*(nexpid-2)+['emis_DMS']*2, \
                   ['EMI_DUST_TOT_noresm2']*(nexpid-2)+['emis_DUST']*2, \
                   ['EMI_SALT_TOT_noresm2']*(nexpid-2)+['emis_SALT']*2, \
                   ['SFisoprene']*(nexpid-2)+['emis_isoprene']*2, \
                   ['SFmonoterp']*(nexpid-2)+['emis_monoterp']*2 \
                  ]
for variablelist in variablegrouplist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)



# REMOVE LAST 2 eleemnts
del expidlist[    -2:]
del legendlist[   -2:]
del shiftlist[    -2:]
del smoothlist[   -2:]
del linestylelist[-2:]
del linewidthlist[-2:]
del colorlist[    -2:]

description='typevarcommon-varcommon'

# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)
