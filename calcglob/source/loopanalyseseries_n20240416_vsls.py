import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

typevarlist=['glob']
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# TOAR SIMULATIONS + sensitivity simulations
#-------------------------------------------
expidlist=[ \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_chbr3x0.0_fxemiyear_20240315_sim01', \
           'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_chbr3x2.0_fxemiyear_20240315_sim01' ]

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['1 ppt[CHBR'+r'$_3$'+']', \
            '0 ppt[CHBR'+r'$_3$'+']', \
            '2 ppt[CHBR'+r'$_3$'+']']
#
smoothlist=[0,0,0]
#            
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#
variablelist=['cb_CHBR3', 'cb_O3', 'FSLNT']
#
code='n20240416_vsls'
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.5')
#
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
