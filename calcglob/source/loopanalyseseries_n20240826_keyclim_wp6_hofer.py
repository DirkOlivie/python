import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
description='varcommon-typevarcommon'
generalcode='n20240826_keyclim_wp6_hofer'


# ALL VARIABLES (except ozone)
#------------------------------------------------------------------------
#
expidlist=[ \
           'histssp585', \
           'histssp585-cloud2']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Cloud'] 
#
smoothlist=[0,0]
#smoothlist=[5,5]
#
shiftlist=[0,0]
#
colorlist=[0,1]
#

# tempocn
variablelist=['SWCF','LWCF', \
              'cb_BC','cb_OM','cb_SULFATE']
typevarlist=['glob']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
