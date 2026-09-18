import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. NHIST
#-----------------------
expidlist=[ \
           'NF1850norbc_f19_20191025len30', \
           'NF1850norbc_f19_20250311_test01', \
           'NF1850norbc_f19_20250311_test06', \
           'NF1850norbc_f19_20250311_test05', \
            \
           'N1850_f19_tn14_20190621', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test06', \
           'N1850_f19_tn14_20250311_test05']
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'CMIP6', \
            '0 Tg[S] yr'+r'$^{-1}$', \
            '2 Tg[S] yr'+r'$^{-1}$, 23km, 30S-30N', \
            '5 Tg[S] yr'+r'$^{-1}$, 23km, 30S-30N', \
            '', \
            '', \
            '', \
            '']
#
smoothlist=[0,0,0,0,0,0,0,0]
colorlist=[0,1,2,3,0,1,2,3]
linestylelist=[0,0,0,0,2,2,2,2]
shiftlist=[0,0,0,0,-1599,-1599,-1599,-1599]
#
code='n20250319_navigate_geoeng3'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', regionintitle=True, xrange=[0,30])
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['AOD_VISdivDAYFOC','cb_SULFATE','TREFHT','PRECT','EMI_SO2SO4_as_SO2_TOT_noresm2','FSLNT']
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

