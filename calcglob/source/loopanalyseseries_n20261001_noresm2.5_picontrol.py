import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout(xrange=[1000.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[1350.,1700.])
figlayout=cfiglayout.CFigLayout(xrange=[1530.,1850.])
figlayout=cfiglayout.CFigLayout(xrange=[ 925.,1800.])
figlayout=cfiglayout.CFigLayout(xrange=[1350.,1750.])
figlayout=cfiglayout.CFigLayout(xrange=[1400.,1710.])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20190621ext', \
            \
           'n1850Gaxg.LM.n30b24.511.betzy.20260904', \
           'n1850GaxgGHG.LM.n30b24.511.betzy.20260904', \
            \
           'n1850Gaxg.LM.n30b24.516.20260909', \
           'n1850GaxgGHG.LM.n30b24.516.20260909', \
           'n1850GaxgGHG.LM.n30b24.517.20260911', \
           'n1850GaxgGHG.LM.nor30b24.525.20260923', \
            \
           'n1850GaxgGHG.LM.nor30b25.526.redout.20260928', \
           'n1850GaxgGHG.LM.nor30b25.528.20260928', \
            \
           'n1850esmGaxgGHG.LM.n30b25.20260928', \
           'n1850esmGaxgGHG.LM.n30b25.529.20261002'] 
#
legendlist=['NorESM2-MM', \
            'NorESM2-LM', \
             \
            'b24 (#511)', \
            'b24 (#511, GHG)', \
             \
            'b24 (#516)', \
            'b24 (#516, GHG)', \
            'b24 (#517, GHG)', \
            'b24 (#525, GHG)', \
             \
            'b25 (#526, GHG)', \
            'b25 (#528, GHG)', \
            'b25 (#523, GHG, esm)', \
            'b25 (#529, GHG, esm)']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0,                  0,0, 0,0,0,0, 0,0,0,0]
shiftlist=[-1199+1400,-1599+1400, 0,0, 0,0,0,0, 0,0,0,0]
colorlist     =   [0,1,           2,3, 4,5,6,7, 8,9,10,11]
linestylelist =   [2,2,           0,0, 0,0,0,0, 0,0,0,0]
linewidthlist =   [1,1,           1,2, 1,2,2,2, 2,2,2,2]

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
code='n20261001_noresm2.5_picontrol'
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
                   ['PRECCPRECL']*2+['PRECT']*(nexpid-6)+['PRECCPRECL']*4, \
                   ['SFDMS']*2+['emis_DMS']*(nexpid-2), \
                   ['EMI_DUST_TOT_noresm2']*2+['emis_DUST']*(nexpid-2), \
                   ['EMI_SALT_TOT_noresm2']*2+['emis_SALT']*(nexpid-2) \
#                   ['SFisoprene']*(nexpid-9)+['emis_isoprene']*9, \
#                   ['SFmonoterp']*(nexpid-9)+['emis_monoterp']*9 \
                  ]
for variablelist in variablegrouplist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist)



# REMOVE LAST 2 eleemnts
#del expidlist[    -9:-7]
#del legendlist[   -9:-7]
#del shiftlist[    -9:-7]
#del smoothlist[   -9:-7]
#del linestylelist[-9:-7]
#del linewidthlist[-9:-7]
#del colorlist[    -9:-7]


# REMOVE LAST element
#del expidlist[    -8]
#del legendlist[   -8]
#del shiftlist[    -8]
#del smoothlist[   -8]
#del linestylelist[-8]
#del linewidthlist[-8]
#del colorlist[    -8]

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
