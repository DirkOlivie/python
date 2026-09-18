import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
figlayout=cfiglayout.CFigLayout(xrange=[-5,30])
code='n20251107_n2olandocean_deliverable7_1'


# stratospheric aerosol

# 1. WITHOUT ANY N2O DIAGNOSTICS
#-------------------------------
description='varcommon-typevarcommon'
expidlist=['N1850vslsn2onh3_f19_tn14_test10']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['']
smoothlist=[0]
colorlist=[1]
shiftlist=[-30]
#
variablelist=[ \
              'F_N2O_DENIT_NITxLANDFRAC_as_N2O', \
              'F_N2O_DENIT_NITxLANDFRAC', \
              'FN2OxLANDFRAC_as_N2O', \
              'cb_N2O','N2O_SRF','SFN2O','SFN2O_as_N', \
              'r_jn2o_columnburden', \
              'TAU2_N2O','minusGS_N2O', \
              'emin2oocean','eminh3ocean', \
              'ndepnoyocn','ndepnhxocn', \
              'nh3fluxocn','n2ofluxocn', \
              'atmnh3ocn','atmn2oocn','atmco2ocn']  

#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 1. WITHOUT ANY N2O DIAGNOSTICS
#-------------------------------
description='typevarcommon'
expidlist=['N1850vslsn2onh3_f19_tn14_test10', \
           'N1850vslsn2onh3_f19_tn14_test10']  
refidlist=expidlist
wlist=[1.,0.]
legendlist=['land','ocean']
smoothlist=[0,0]
colorlist=[2,0]
shiftlist=[-30,-30]
#
variablelist=[ \
              'F_N2O_DENIT_NITxLANDFRAC', \
              'emin2oocean_as_N']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
