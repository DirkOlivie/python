import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

freqtypelist=['YEA','SON']
description='varcommon'


# stratospheric aerosol

# 0. historical simulations
#--------------------------
expidlist=[ \
            'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
            'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['f19', \
            'f09']
#
smoothlist=[0,0]
#            
shiftlist=[0,0]
#
variablelist=['CLY_SCALED_layer00','BRY_SCALED_layer00', \
              'CLY_SCALED_layer06','BRY_SCALED_layer06', \
              'cb_O3', \
              'O3_layer06','O3_layer00']
#
code='kclim_ozone_vsls'
#
figlayout=cfiglayout.CFigLayout(xrange=[1980,2015], legendlocation='')
#
typevarlist=['glob','90S28S','28S28N','28N60N','60N90N','90S28SLAND']
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
#
# 1. 1850 simulations with CHBR3 lower boundary condition : 0 ppt, 1 ppt, 2 ppt 
#--------------------
expidlist=['NF1850norbc_tropstratchem_f19_20220105_test09', \
           'NF1850norbc_tropstratchem_f19_20220105_test06', \
           'NF1850norbc_tropstratchem_f19_20220105_test10']

refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['0 ppt CHBr3', \
            '1 ppt CHBr3', \
            '2 ppt CHBr3']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
variablelist=['CLY_SCALED_layer00','BRY_SCALED_layer00', \
              'CLY_SCALED_layer06','BRY_SCALED_layer06', \
              'cb_O3']
#
code='kclim_ozone_vsls_nf1850'
#
figlayout=cfiglayout.CFigLayout(xrange=[11,30], legendlocation='')
#
typevarlist=['glob','90S28S','28S28N','28N60N','60N90N','90S28SLAND']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 3. test simulations
#--------------------------
freqtype='YEA'

expidlist=[ \
            'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
            'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
            'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0]
#            
shiftlist=[0,0,0]
#
variablelist=['BRY_layer06','BRY_SUM_layer06','BRY_SCALED_layer06']
#
legendlist=variablelist
#
code='kclim_ozone_vsls'
#
figlayout=cfiglayout.CFigLayout(xrange=[1970,2015],legendlocation='')
#
typevarlist=['glob']
for typevar in typevarlist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout)

variablelist=['CLY_layer06','CLY_SUM_layer06','CLY_SCALED_layer06']
legendlist=variablelist
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout)
