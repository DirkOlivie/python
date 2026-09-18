import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# stratospheric aerosol

# 1. N2O EMISSION DRIVEN
#-----------------------
expidlist=['NF1850norbc_f19_20191025len30', \
#           'NF1850norbc_f19_20201226', \
           'NF1850norbc_f19_f19_20231204_test04', \
           'NF1850norbc_f19_f19_20231204_test02', \
           'NF1850norbc_f19_f19_20231204_test03', \
           'NF1850norbc_f19_f19_20231204_test05', \
           'NF1850norbc_f19_f19_20231204_test06', \
           'NF1850norbc_f19_f19_20231204_test10', \
           'NF1850norbc_f19_f19_20231204_test11', \
           'NF1850norbc_f19_f19_20231204_test12', \
           'NF1850norbc_f19_f19_20231204_test13', \
           'NF1850norbc_f19_f19_20231204_test01', \
           'NF1850norbc_f19_f19_20231204_test14']
#           'NF1850norbc_f19_f19_20231204_test07', \
#           'NF1850norbc_f19_f19_20231204_test08', \
#           'NF1850norbc_f19_f19_20231204_test09']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['noresm2', \
#            'noresm2', \
            'noresm2.1 (no CAM corr.)', \
            'noresm2.1 (no ice-delimiter corr.)', \
            'noresm2.1 (no het. freez. corr.)', \
            'noresm2.1 (no koagsub corr.)', \
            'noresm2.1 (no dry dep. corr.)', \
            'noresm2.1 (only ice-delimiter corr.)', \
            'noresm2.1 (only het. freez. corr.)', \
            'noresm2.1 (only koagsub corr.)', \
            'noresm2.1 (only dry dep. corr.)', \
            'noresm2.1', \
            'noresm2.1 + Hofer']
#            'noresm2.1 + Hofer ', \
#            'noresm2.1 + Hofer (2)', \
#            'noresm2.1 + Hofer (3)']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6,7,8,9,10,11]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
variablelist=['FSDS','FSDSC','SFDMS','U10','CDNUMC','NUMLIQ_columnburden','NUMICE_columnburden', \
              'FSLNT','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT','cb_DUST','PRECT', \
              'cb_BC_AC_OCW','cb_BC_AC','D550_BCdivDAYFOC', \
              'SWCF','LWCF']
#
code='n20231206_noresm2.1_fsst'
#
#figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob','SH','NH','SHSEA','NHLAND']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
