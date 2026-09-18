import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
figlayout=cfiglayout.CFigLayout(legendlocation='')
# 
# OUTPUT ON SE GRID

#   JERRY, DIRK1, DIRK2, ADA
#------------------------------------------
expidlist=['n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120b']

refidlist=expidlist
#
wlist=[1.,0.]
#
variablelist=['FCO2xLANDFRAC_minus_SFCO2_LND']

legendlist=['']

shiftlist=[0]

smoothlist=[0]
#
colorlist=[0]
#            
code='n20260303_co2_jerry_overview_ssp534'
#
typevarlist=['glob']
freqtypelist=['monthly']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
#   JERRY, DIRK1, DIRK2, ADA
#------------------------------------------
expidlist=['nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225']

refidlist=expidlist
#
wlist=[1.,0.]
#
variablelist=['FCO2xLANDFRAC_minus_SFCO2_LND']

legendlist=['']

shiftlist=[0]

smoothlist=[0]
#
colorlist=[0]
#            
code='n20260303_co2_jerry_overview_nhist'
#
typevarlist=['glob']
freqtypelist=['monthly']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#


