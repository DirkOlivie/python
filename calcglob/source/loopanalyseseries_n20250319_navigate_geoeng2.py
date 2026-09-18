import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. NHIST
#-----------------------
expidlist=[ \
           'N1850_f19_tn14_20190621', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test05_20km', \
           'N1850_f19_tn14_20250311_test05', \
           'N1850_f19_tn14_20250311_test05_26km', \
           'N1850_f19_tn14_20250311_test05_15n60n', 
           'N1850_f19_tn14_20250311_test05_60s15s']            
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'CMIP6', \
            '0 Tg[S] yr'+r'$^{-1}$', \
            '5 Tg[S] yr'+r'$^{-1}$, 20km, 30S-30N', \
            '5 Tg[S] yr'+r'$^{-1}$, 23km, 30S-30N', \
            '5 Tg[S] yr'+r'$^{-1}$, 26km, 30S-30N', \
            '5 Tg[S] yr'+r'$^{-1}$, 23km, 15N-60N', \
            '5 Tg[S] yr'+r'$^{-1}$, 23km, 60S-15S']
#
smoothlist=[0,0,0,0,0,0,0]
colorlist=[0,1,2,3,4,5,0]
linestylelist=[1,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0]
#
code='n20250319_navigate_geoeng2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='', xrange=[1595, 1625], regionintitle=True)
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['AOD_VISdivDAYFOC','cb_SULFATE','TREFHT','PRECT','EMI_SO2SO4_as_SO2_TOT_noresm2']
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['glob','atlarc']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

