import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


description='varcommon-typevarcommon'
generalcode='n20250604_cmip6_fdms'
figlayout=cfiglayout.CFigLayout(legendlocation='')
typevarlist=['glob']
freqtype='YEA'

# 1. METHANEMIP + HYWAY
#------------------------------------------------------------------------
#
expidlist=[ 'N1850_f19_tn14_20190621', \
            'NF1850norbc_f19_20191025', \
            'NF1850norbc_f19_20200303']
#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[\
            'fully-coupled', \
            'fSST (standard)', \
            'fSST (modified)']
smoothlist=[0,0,0]
shiftlist=[-1599,0,0]
colorlist=[0,1,2]

variablelist=[ \
              'SFDMS','U10']
#
code=generalcode
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
