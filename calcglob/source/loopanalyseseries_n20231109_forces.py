import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon'
generalcode='n20231109_forces'


# I. ALL VARIABLES 2014
#######################
#
expidlist=[ \
            'NHIST_f19_tn14_20190625ext', \
            'NHIST_f19_tn14_Forces_230515']            
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['Reference', \
            'Nenes']
#
smoothlist=[0,0]
#
shiftlist=[0,0]
#
colorlist=[0,1]
#

# tempocn no PRECT
variablelist=[ \
              'cb_SULFATE','cb_DUST','cb_SALT','cb_BC','cb_OM']
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='',colorscheme='keyclim-wp6')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
