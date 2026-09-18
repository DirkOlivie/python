import numpy as np

import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
typevar='SEA' # 'NH'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol

# 0. AEROCOM EXCESS MASS
#-----------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625', \
           'NHIST_f19_tn14_20190710', \
           'NFHISTnorbc_f19_20191107']

refidlist=expidlist
wlist=[1.,0.]

#
legendlist=refidlist
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)
shiftlist=[0,0,0]

#            
variablelist=['ICEFRAC']
#
code='cmip6_icefrac'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
