import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='monthly'
figlayout=cfiglayout.CFigLayout()
figlayoutlog=cfiglayout.CFigLayout(ytype='log',xrange=[0,20])


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
expidlist=['nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_dev_20250513', \
           'nf1850_ne30pg3_ne30pg3_mtn14_fatesnocomp_leungdust_aer2014_dev_20250513', \
           'n1850.ne30_tn14.noresm3_0_alpha03d.20250528', \
           'n1850.ne16pg3_tn14.noresm3_0_alpha03c.noresm3_0_002_cam6_4_085.19_to_35yr_2deg_ppe_spinup.20250524', \
           'n1850.ne30_tn14.rest-NOIIAJRARYF8485OC_20250506.3.0a03b.20250513', \
           'n1850_ne30pg3_tn14_alpha3d.BCAXtest_20250612']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['03d (fSST, aer1850)', \
            '03d (fSST, aer2014)', \
            '03d', \
            '03d (2x2)', \
            '03b', \
            '03d (bugfix)']
#legendlist=['','','']
#
smoothlist=[0,0,0,0,0,0]
#
shiftlist=[0,0,0,-18,0,0]
#
colorlist=[7,1,2,3,4,0]
linestylelist=[0,0,0,0,0,0]
#

# tempocn
description='typevarcommon-varcommon'
variablelist=['cb_BC_N','cb_BC_NI','cb_BC_A','cb_BC_AI','cb_BC_AX','cb_BC_AC', \
              'cb_BC', \
              'EMI_BC_TOT_noresm2', \
              'AODVISdivDAYFOC']
typevarlist=['glob']
#
code='n20250605_noresm2.5'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayoutlog,colorlist=colorlist,linestylelist=linestylelist)
#
variablelist=['FSLNT','FSDS']
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
