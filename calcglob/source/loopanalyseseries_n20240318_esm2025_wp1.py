import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# 

# 1. NorESM2-LM and NorESM2-LM-C : absolute
#------------------------------------------
expidlist=['NF1850norbc_f19_20240312_test01', \
           'NF1850norbc_aer2014_f19_20240312_test01', \
           'NF1850norbc_so22014_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_so22014_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['noresm2 (piClim-control)', \
            'noresm2 (piClim-aer)', \
            'noresm2 (piClim-so2)', \
            \
            'noresm2-chem (piClim-control)', \
            'noresm2-chem (piClim-aer)', \
            'noresm2-chem (piClim-so2)', \
            \
            'noresm2-chem (piClim-o3)']
#
smoothlist=[0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6]
#            
shiftlist=[0,0,0,0,0,0,0]
#
variablelist=['SFisoprene','SFmonoterp', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'FSLNT', \
              'CDNUMC']
#
code='n20240318_esm2025_wp1'
#
#figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 2. NorESM2-LM and NorESM2-LM-C : difference
#------------------------------------------
expidlist=['NF1850norbc_aer2014_f19_20240312_test01', \
           'NF1850norbc_so22014_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_so22014_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01']
#
refidlist=['NF1850norbc_f19_20240312_test01', \
           'NF1850norbc_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_f19_20240312_test01']
#

#
wlist=[1.,-1.]
#
legendlist=['noresm2 (piClim-aer)', \
            'noresm2 (piClim-so2)', \
            \
            'noresm2-chem (piClim-aer)', \
            'noresm2-chem (piClim-so2)', \
            \
            'noresm2-chem (piClim-o3)']
#
smoothlist=[0,0,0,0,0]
#
colorlist=[1,2,4,5,6]
#            
shiftlist=[0,0,0,0,0]
#
variablelist=['SFisoprene','SFmonoterp', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'CDNUMC', \
              'FSLNT']
#
code='n20240318_esm2025_wp1-diff'
#
#figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 2. NorESM2-LM and NorESM2-LM-C
#-------------------------------
expidlist=['NF1850norbc_tropstratchem_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01', \
           'NF1850norbc_tropstratchem_so22014_f19_20240312_test01', \
            \
           'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['noresm2-chem (piClim-control)', \
            'noresm2-chem (piClim-aer)', \
            'noresm2-chem (piClim-so2)', \
            \
            'noresm2-chem (piClim-o3)']
#
smoothlist=[0,0,0,0]
#
colorlist=[3,4,5,6]
#            
shiftlist=[0,0,0,0]
#
variablelist=['cb_CH4','cb_N2O','cb_O3']
#
code='n20240318_esm2025_wp1'
#
#figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)





