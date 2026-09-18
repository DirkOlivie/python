import numpy as np

import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol

# 0. AEROCOM EXCESS MASS
#-----------------------
expidlist=[ \
            'N1850vsls_tropstratchem_prep_f19_nt14_20220223_test04', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test09']
refidlist=expidlist
wlist=[1.,0.]

#
legendlist=['2x2', \
            '1x1']
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)
shiftlist=np.zeros(nexpid,dtype=int)
#            
#variablelist=['TAU_CHBR3','TAU2_CHBR3','SFCHBR3','CHBR3_SRF','CHBR3_surfacelayer','cb_CHBR3']
variablelist=['TAU_CHBR3',             'SFCHBR3','CHBR3_SRF','CHBR3_surfacelayer','cb_CHBR3']
variablelist=['SFDMS']
variablelist=['cb_O3']
#
code='kclim_ozone_cpl'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
