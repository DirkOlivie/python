import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# stratospheric aerosol

# 1. NorESM-only
#---------------
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test19', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test21', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test25']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['2x2', \
            '2x2 no volc.', \
            '1x1', \
            '1x1 no volc.', \
            '2x2 SO4(na)', \
            '2x2 corr. sad', \
            '2x2 corr. sad (mod 1,2,4,5,12,14)', \
            '2x2 corr. sad (SO2 100%)']
#
smoothlist=[0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=['cb_SULFATE','cb_O3']
#
code='n20221109_stratozone_noresm2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob','90S28SLAND']
freqtypelist=['YEA','SON']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
#
# 2.1 NorESM + CESM : cb_O3
#--------------------------
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['2x2', \
            '2x2 no volc.', \
            '1x1', \
            '1x1 no volc.', \
            '2x2 SO4(na)',
            'CESM2 2x2',
            'CESM2 2x2', 
            'CESM2 1x1']
#
smoothlist=[0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=['cb_O3']
#
code='n20221109_stratozone_noresm2cesm2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',xrange=[1980,2015])
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
#
# 2.2 NorESM + CESM : cb_SULFATE and cb_so4_a123 
#--------------------
expidlist=['NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test14', \
           'NFHISTnorpddmsbc_tropstratchem_f09_mg17_20220105_test16', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11', \
           'FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['2x2', \
            '2x2 no volc.', \
            '1x1', \
            '1x1 no volc.', \
            '2x2 SO4(na)',
            'CESM2 2x2',
            'CESM2 2x2', 
            'CESM2 1x1']
#
smoothlist=[0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=['cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_so4_a123','cb_so4_a123','cb_so4_a123']
#
code='n20221109_stratozone_noresm2cesm2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',xrange=[1980,2015])
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout)
#
# 3. CESM
#--------
expidlist=['FCHIST_f19_mg17_20220111_test1', \
           'FCHIST_f19_mg17_20220111_test6', \
           'FCHIST_f09_mg17_20220111_test7']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['CESM2 2x2',
            'CESM2 2x2',
            'CESM2 1x1']
#
smoothlist=[0,0,0]
#            
shiftlist=[0,0,0]
#
variablelist=['cb_O3']
#
code='n20221109_stratozone_cesm2'
#
figlayout=cfiglayout.CFigLayout(legendlocation='',xrange=[1980,2015])
#
typevarlist=['glob','90S28SLAND']
freqtypelist=['YEA','SON']
#
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
#
#
# 


