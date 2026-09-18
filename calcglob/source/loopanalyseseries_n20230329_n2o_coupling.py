import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# stratospheric aerosol

# 1. CESM-only historical
#------------------------
expidlist=['N1850vsls_tropstratchem_prep_f19_nt14_20230318_test02', \
           'N1850vsls_tropstratchem_prep_f19_nt14_20230318_test04']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['test02', \
            'test04']
#
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
variablelist=['NDEP_TO_SMINN']
#
code='n20230329_n2o_coupling'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
