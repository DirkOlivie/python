import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

freqtypelist=['YEA']
description='varcommon'


# stratospheric aerosol

# 0. historical simulations
#--------------------------
expidlist=[ \
            'N1850_f19_tn14_20190621ext', \
            'N1850frc2_f09_tn14_20191001ext', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test12']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['CMIP6 2x2', \
            'CMIP6 1x1', \
            'Full chemistry 1x1']
#
smoothlist=[5,5,5]
#            
shiftlist=[-1599,-1199,0]
#
variablelist=['TREFHT']
#
code='n20221109_keyclimreport'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
