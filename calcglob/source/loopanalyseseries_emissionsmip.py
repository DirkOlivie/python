import numpy as np

import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
freqtype='YEA'
description='varcommon'


# EMISSIONMIP
#------------
expidlist=[ \
           'NFHISTnorpddmsbcsdyn_standard_f09_mg17_20210226', \
            \
           'NFHISTnorpddmsbcsdyn_base_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_bc_no_season_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_so2_no_season_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_no_so4_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_high_so4_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_so2_at_height_f09_mg17_20210226', \
           'NFHISTnorpddmsbcsdyn_high_so4_so2_at_height_f09_mg17_20220824', \
            \
           'NFHISTnorpddmsbcsdyn_f2_base_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_ship_30red_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_ship_60red_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_ship_atlanticshift_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_ship_indianshift_f09_mg17_20220824', \
            \
           'NFHISTnorpddmsbcsdyn_f2_1950_base_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_1950_ship_60red_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_1950_ship_atlanticshift_f09_mg17_20220824', \
           'NFHISTnorpddmsbcsdyn_f2_1950_ship_indianshift_f09_mg17_20220824']
#
refidlist=expidlist
wlist=[1.,0.]
#
legendlist=refidlist
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)
shiftlist=np.zeros(nexpid,dtype=int)
#            
variablelist=['SFSO2','SFSO4_PR','EMI_SO2SO4_as_SO2_TOT_noresm2', \
              'cb_SO2','cb_SULFATE','SWCF']
#
code='emissionsmip'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
