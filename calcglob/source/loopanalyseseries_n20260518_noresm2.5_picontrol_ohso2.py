import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
figlayout=cfiglayout.CFigLayout()
#figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6)
#------------------------------------------------------------------------
#
code='n20260518_noresm2.5_picontrol_ohso2'
#
# name of n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.hygr1p1.4p8 : it has clubb_c8=4.95 (not 4.8)
expidlist=[ \
            'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.Olivia.2026-05-18', \
            'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.4p95', \
            'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.hygr1p1.4p8', \
            'n1850.ne16pg3_tn14.noresm3_0_beta16.Run13.2026-05-18.dstsslt.hygr1p1mode5.4p8'] 
#
legendlist=[ \
           'Reference (Kjetil, c8=4.65)', \
           'dust.salt2 (c8=4.95)', \
           'dust.salt2+rh1.1 (c8=4.95)', \
           'dust.salt2+rh1.1+mode5 (c8=4.8)']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0]
#
shiftlist=[0,0,0,0]
#
colorlist     =   [0,1,2,3]

linestylelist =   [0,0,0,0]
#

description='typevarcommon-varcommon'
variablelist=[\
              'FSDS','FSDSC', \
              'PRECC','PRECL', \
              'TREFHT', \
#              'SWCF','LWCF','PRECT','CLDTOT','CLDLOW','CLDMED','CLDHGH', \
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
variablelist=['ICEFRAC']
typevarlist=['SH']
freqtype='seasonalcycle'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

