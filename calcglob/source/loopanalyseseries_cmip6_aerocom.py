import numpy as np

import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
typevar='SEA' # 'NH'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol

# 0. AEROCOM
#-----------
expidlist=[ \
           'NFHISTnorpddmsbcsdyn_f09_mg17_20191101', \
           'NFHISTnorpddmsbcsdyn_f09_mg17_20210415', \
           'NFHISTnorpddmsbcsdyn_f09_mg17_20210420']
#
refidlist=expidlist
wlist=[1.,0.]
#
legendlist=refidlist
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)
shiftlist=[0,0,0]
#            
variablelist=['SFDMS']
#
code='cmip6_aerocom'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#
# 1. AEROCOM + HISTORICAL
#------------------------
expidlist=[ \
           'NFHISTnorpddmsbcsdyn_f09_mg17_20191101', \
           'NFHISTnorpddmsbcsdyn_f09_mg17_20210415', \
           'NFHISTnorpddmsbcsdyn_f09_mg17_20210420', \
            \
           'NFHISTnorbc_f19_20190730', \
           'NFHISTnorbc_f19_20191107', \
           'NHIST_f19_tn14_20190710']

#
refidlist=expidlist
wlist=[1.,0.]
#
legendlist=refidlist
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)
shiftlist=[0,0,0,0,0,0]
#            
variablelist=['SFDMS']
#
code='cmip6_aerocom_hist'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
