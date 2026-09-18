import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'
# 
# 1. NorESM2-LM and NorESM2-LM-C : absolute
#------------------------------------------
expidlist=['NHIST_f19_tn14_20190625', \
           'NHIST_f19_tn14_20190710',
           'NSSP126frc2_f19_tn14_20191014', \
           'NSSP245frc2_f19_tn14_20191014', \
           'NSSP370frc2_f19_tn14_20191014', \
           'NSSP585frc2_f19_tn14_20191014', \
           'b.e21.NSSP126frc2.f19_tn14.CMIP6-SSP1-2.6-SSP3-7.0Lu.001', \
           'b.e21.NSSP370frc2.f19_tn14.CMIP6-SSP3-7.0-SSP1-2.6Lu.001']
#
refidlist=expidlist
legendlist=['historical','historical','ssp1-2.6','ssp2-4.5','ssp3-7.0','ssp5-8.5','ssp126-lu370','ssp370-lu126']
#
wlist=[1.,0.]
#
variablelist=['TREFHT','U10','PS']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6,7]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
code='n20240411_james_gomez'
#
#figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
