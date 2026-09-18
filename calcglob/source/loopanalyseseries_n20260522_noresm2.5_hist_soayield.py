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
code='n20260522_noresm2.5_hist_soayield'
#
expidlist=[ \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p2allmodes', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p1', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayield.hygr1p2', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.soayieldx2', \
            \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p1mode5', \
           'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118.dust.seasaltdist.hygr1p05mode5' \
           ] 
#
legendlist=[ \
           'Reference', \
           'dst+sslt', \
           'dst+sslt+rhx1.1', \
           'dst+sslt+rhx1.2', \
           'dst+sslt+rhx1.2allmodes', \
           'dst+sslt+soayield',  \
           'dst+sslt+soayield+rhx1.1', \
           'dst+sslt+soayield+rhx1.2', \
           'dst+sslt+soayieldx2', \
            \
           'dst+sslt+rhx1.1mode5', \
           'dst+sslt+rhx1.05mode5' \
           ]
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

linestylelist =   [0,0,0,0,0,0,0,0,0,2,2]
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
typevarlist=['glob']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

variablelist=[\
              'AODVISdivDAYFOC']
typevarlist=['LAND','SEA']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
#
# long historical does not have DOD550divDAYFOC
del expidlist[0]
#del refidlist[0] 
del legendlist[0]
del shiftlist[0]
del smoothlist[0]
del colorlist[0]
del linestylelist[0]

variablelist=['DOD550divDAYFOC']
typevarlist=['glob','LAND','SEA']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



