import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


description='varcommon-typevarcommon'
generalcode='n20250701_oyvind_cfmip'
figlayout=cfiglayout.CFigLayout(legendlocation='')
typevarlist=['glob']
freqtype='YEA'

# 1. METHANEMIP + HYWAY
#------------------------------------------------------------------------
#
expidlist=[ \
           'nf1850_ne30pg3_ne30pg3_mtn14_locallim_20250625', \
           'nf1850_ne30pg3_ne30pg3_mtn14_locallim_sstp4K_20250625', \
           \
           'nf1850_ne30pg3_ne30pg3_mtn14_globlim_20250625', \
           'nf1850_ne30pg3_ne30pg3_mtn14_globlim_sstp4K_20250625']

refidlist=expidlist
wlist=[1.,0.]
legendlist=[\
            'local', \
            'local (+4K)', \
            'global', \
            'global (+4K)'] 
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
colorlist=[0,1,2,3]

variablelist=[ \
               'FSLNT', 'TREFHT']
#
code=generalcode
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
