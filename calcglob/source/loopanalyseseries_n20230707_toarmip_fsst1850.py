import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon'
generalcode='n20230707_toarmip'


# TOA imbalance
#------------------------------------------------------------------------
#
expidlist=[ \
           'NF1850norbc_tropstratchem_f19_20230515_test01', \
           'NF1850norbc_tropstratchem_f19_toar_20230605_sim01', \
           'NF1850norbc_tropstratchem_f19_toar_20230605_sim05']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2 (esm2025)', \
            'NorESM2-toar sim1', \
            'NorESM2-toar sim5']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#
variablelist=['FSLNT']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# cb_CO2, cb_CO2_c, cb_CO2CHEM
#------------------------------------------------------------------------
#
description=''
#
expidlist=[ \
           'NF1850norbc_tropstratchem_f19_toar_20230605_sim01', \
           'NF1850norbc_tropstratchem_f19_toar_20230605_sim01', \
           'NF1850norbc_tropstratchem_f19_toar_20230605_sim05', \
           'NF1850norbc_tropstratchem_f19_toar_20230605_sim05']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2-toar sim1', \
            'NorESM2-toar sim1', \
            'NorESM2-toar sim5', \
            'NorESM2-toar sim5']
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,0,0]
#
colorlist=[0,1,2,4]
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
variablelist=['cb_CO2','cb_CO2_c','cb_CO2CHEM','cb_CO2_c']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CH4','cb_CH4_c','cb_CH4CHEM','cb_CH4_c']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_N2O','cb_N2O_c','cb_N2OCHEM','cb_N2O_c']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CFC11','cb_CFC11STAR_c','cb_CFC11CHEM','cb_CFC11_c']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#
variablelist=['cb_CFC12','cb_CFC12_c','cb_CFC12CHEM','cb_CFC12_c']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
