import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. N1850
#-----------------------
expidlist=[ \
           'NHISTpiaer_f19_tn14_20190721', \
           'NHISTpiaer_02_f19_tn14_20190909', \
           'NHISTpiaer_03_f19_tn14_20190909', \
            \
           'NHISTpintcf_f19_tn14_20190720', \
           'NHISTpintcf_02_f19_tn14_20190909', \
           'NHISTpintcf_03_f19_tn14_20190909', \
            \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['hist-piAer','','','hist-piSLCF','','','historical','','']
#
smoothlist=[0,0,0,0,0,0,0,0,0]
#
colorlist=[2,2,2,1,1,1,0,0,0]
linestylelist=[0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0,0]
#
variablelist=['TREFHT']
#
code='n20250328_aerchemmip2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
