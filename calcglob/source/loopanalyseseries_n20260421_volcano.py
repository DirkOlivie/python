import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM
figlayout=cfiglayout.CFigLayout()

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
freqtype='monthly'
description='varcommon-typevarcommon'
code='n20260421_volcano'


# OTHER VARIABLES
#----------------
#
expidlist=[ \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test12', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test06', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test11']
#
refidlist=[ \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
#           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test13']
#
wlist=[1.,0.]

legendlist=[ \
#            'SO2 100%/SO4 0%', \
            'SO2 97.5%/SO4 2.5%', \
            'SO2 95%/SO4 5%', \
            'SO2 90%/SO4 10%', \
            'SO2 80%/SO4 20%', \
            'SO2 50%/SO4 50%', \
#            'SO2 0%/SO4 100%', \
            'SO2 0%/SO4 100% (na)']
#
smoothlist=[0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0]
colorlist=[0,1,2,3,4,5]
linestylelist=[0,0,0,0,0,0]

#
variablelist=['mmr_SULFATE_columnburden_abovetropopause', \
              'SO4_NA_columnburden_abovetropopause', \
              'SO4_PR_columnburden_abovetropopause', \
              'SO4_A1_columnburden_abovetropopause', \
              'SO4_A2_columnburden_abovetropopause', \
              'SO4_AC_columnburden_abovetropopause']
#
typevarlist=['glob']
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
