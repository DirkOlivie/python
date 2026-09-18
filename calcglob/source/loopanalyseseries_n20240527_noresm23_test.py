import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
# 

# 1. NorESM2-LM and NorESM2-LM-C : absolute
#------------------------------------------
expidlist=['NF1850norbc_tropstratchem_f19_20240312_test01', \
           'N1850_tropstratchem_f19_tn14_20240319_test08', \
           'N1850_tropstratchem_f19_tn14_20240319_test10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['noresm2-chem (fsst, esm2025)', \
            'noresm2.3-chem', \
            'noresm2.3-chem']
#
smoothlist=[0,0,0]
#
colorlist=[0,1,2]
#            
shiftlist=[0,0,0]
#
variablelist=['SFisoprene','SFmonoterp', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'FSLNT', \
              'CDNUMC', \
              'LNO_COL_PROD', \
              'SFCO','SFNO','SFNO2','SFSO2','SFNH3','SFBC_N','SFBC_NI','SFBC_AX','SFOM_NI','SFSO4_PR', 
              'O3_SRF','OH_SRF','CO_SRF','NO_SRF','NO2_SRF','SO2_SRF']
#
code='n20240527_noresm23_test'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
