import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout(xrange=[1950,2015])
#figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
code='n20260423_noresm2.5_hist_ohso2'
#
expidlist=[ \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.convincld', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.convstratbelowcld', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.dust', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.seasalt', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.all', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.seasaltdist', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.all2', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.h2o2', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.h2o2.all2']
#
legendlist=[ \
           'Reference', \
           'ohso2', \
           'ohso2.convincld', \
           'ohso2.convstratbelowcld', \
           'ohso2.dust', \
           'ohso2.seasalt', \
           'ohso2.all', \
           'ohso2.seasaltdist', \
           'ohso2.all2', \
           'h2o2', \
           'h2o2.all2']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0,0,0,0]
#
colorlist     =   [0,1,2,3,4,5,6,7,8,9,10]

linestylelist =   [0,0,0,0,0,0,0,0,0,0,0]
#

description='typevarcommon-varcommon'
variablelist=[\
              'FSDS','FSDSC', \
              'PRECC','PRECL', \
              'TREFHT', \
              'SWCF','LWCF','PRECT','CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'U10', \
              'TGCLDLWP','TGCLDIWP', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'AODVISdivDAYFOC']
typevarlist=['glob','90S28SSEA']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

variablelist=['tempocn']
typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

#################################
# SEASONAL CYCLE
#################################
figlayout=cfiglayout.CFigLayout()
#
expidlist=[ \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.all', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.ohso2.all2']
#
legendlist=[ \
           'ohso2', \
           'ohso2.all', \
           'ohso2.all2']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist     =   [0,1,2]

linestylelist =   [0,0,0]
#

description='typevarcommon-varcommon'
variablelist=['ICEFRAC']
typevarlist=['SH']
freqtype='seasonalcycle'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

