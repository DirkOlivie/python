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
            \
           'N1850_f19_tn14_20241127_test01', \
           'N1850_f19_tn14_20241127_test02', \
            \
           'N1850_f19_tn14_20241127_test13', \
           'N1850_f19_tn14_20241127_test14']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'noresm2 (CMIP6)', \
            \
            'noresm2.3', \
            'noresm2.3 (SI)', \
            'noresm2.3 (hetfrz_aer_scalfac=1)', \
            'noresm2.3 (hetfrz_aer_scalfac=1, SI)']
#
smoothlist=[5,5,5,5,5]
#
colorlist=[0,1,2,3,4]
linestylelist=[0,0,2,0,2]
#            
shiftlist=[0,0,0,0,0]#-1200+1600]#,-1+1600]
#
variablelist=['PRECT']
#
code='n20241201_noresm2.3_cpl_sip'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob','NH','SH','60N90N']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
