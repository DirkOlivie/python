import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. N1850
#-----------------------
expidlist=[ \
           'N1850_f19_tn14_20190621ext', \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20241127_test16', \
           'N1850_f19_tn14_20241127_test17']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'NorESM2-LM (2x2)', \
            'NorESM2-MM (1x1)', \
            'NorESM2.3 - test16 (2x2)', \
            'NorESM2.3 - test17 (2x2)']
#
smoothlist=[0,0,0,0]
colorlist=[0,1,2,3]
linestylelist=[0,0,0,0]
#            
shiftlist=[-1599,-1199,-1599,-1599]
#
variablelist=['cb_OM','SFisoprene','SFmonoterp','cb_SOA_LV','cb_SOA_SV','cb_SOA_A1NA','AOD_VISdivDAYFOC']
#
code='n20260522_noresm2.3_cpl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


typevarlist=['LAND','SEA']
variablelist=['AOD_VISdivDAYFOC']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


