import numpy as np
import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol



# precipitation and temperature
#------------------------------
expidlist=[ \
           'ACCESS-CM2_ssp245_r1i1p1f1_gn', \
#           'ACCESS-ESM1-5_ssp245_r1i1p1f1_gn', \
           'BCC-CSM2-MR_ssp245_r1i1p1f1_gn', \
#           'CAMS-CSM1-0_ssp245_r1i1p1f1_gn', \
           'CanESM5_ssp245_r1i1p1f1_gn', \
           'CESM2_ssp245_r1i1p1f1_gn', \
           'CESM2-WACCM_ssp245_r1i1p1f1_gn', \
           'CMCC-CM2-SR5_ssp245_r1i1p1f1_gn', \
           'CNRM-CM6-1-HR_ssp245_r1i1p1f2_gr', \
           'CNRM-CM6-1_ssp245_r1i1p1f2_gr', \
           'CNRM-ESM2-1_ssp245_r1i1p1f2_gr', \
           'EC-Earth3_ssp245_r1i1p1f1_gr', \
           'EC-Earth3-Veg_ssp245_r1i1p1f1_gr', \
#           'FGOALS-f3-L_ssp245_r1i1p1f1_gr', \
           'FGOALS-g3_ssp245_r1i1p1f1_gn', \
#           'FIO-ESM-2-0_ssp245_r1i1p1f1_gn', \ because of pr
#           'GFDL-CM4_ssp245_r1i1p1f1_gr1', \ \ because of pr
#           'GFDL-ESM4_ssp245_r1i1p1f1_gr1', \ because of pr
#           'GISS-E2-1-G_ssp245_r1i1p1f2_gn', \ because of pr
#           'GISS-E2-1-G_ssp245_r1i1p3f1_gn', \ because of pr
           'HadGEM3-GC31-LL_ssp245_r1i1p1f3_gn', \
           'INM-CM4-8_ssp245_r1i1p1f1_gr1', \
           'INM-CM5-0_ssp245_r1i1p1f1_gr1', \
#           'IPSL-CM6A-LR_ssp245_r1i1p1f1_gr', \ because of pr
#           'KACE-1-0-G_ssp245_r1i1p1f1_gr', \ because of pr
#          'KIOST-ESM_ssp245_r1i1p1f1_gr1', \
           'MCM-UA-1-0_ssp245_r1i1p1f2_gn', \
           'MIROC6_ssp245_r1i1p1f1_gn', \
           'MIROC-ES2L_ssp245_r1i1p1f2_gn', \
#           'MPI-ESM1-2-HR_ssp245_r1i1p1f1_gn', \
           'MPI-ESM1-2-LR_ssp245_r1i1p1f1_gn', \
           'MRI-ESM2-0_ssp245_r1i1p1f1_gn', \
#           'NESM3_ssp245_r1i1p1f1_gn', \
           'NorESM2-LM_ssp245_r1i1p1f1_gn', \
           'NorESM2-MM_ssp245_r1i1p1f1_gn']
#          'UKESM1-0-LL_ssp245_r1i1p1f2_gn']
#
refidlist=expidlist # find automatically the piControl
# 
wlist=[1.,-1.]
#
nexpid=len(expidlist)
#
legendlist=expidlist
#
smoothlist=np.zeros(nexpid,dtype=int)
#            
shiftlist=np.zeros(nexpid,dtype=int)
#
code='duncan_ssp245'
#
#variablelist=['tas']
#variablelist=['pr']
variablelist=['tas','pr']
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#
#
# tasmaxmin
#----------

expidlist=[\
#             'ACCESS-CM2_ssp245_r1i1p1f1_gn', \
#             'ACCESS-ESM1-5_ssp245_r1i1p1f1_gn', \
             'BCC-CSM2-MR_ssp245_r1i1p1f1_gn', \
             'CanESM5-CanOE_ssp245_r1i1p2f1_gn', \
             'CanESM5_ssp245_r1i1p2f1_gn', \
#            'CAS-ESM2-0_ssp245_r1i1p1f1_gn', \ problems with tasmaxmin
#            'CMCC-ESM2_ssp245_r1i1p1f1_gn', \
#             'CNRM-CM6-1-HR_ssp245_r1i1p1f2_gr', \
#             'CNRM-CM6-1_ssp245_r1i1p1f2_gr', \
#             'CNRM-ESM2-1_ssp245_r1i1p1f2_gr', \
#             'EC-Earth3-CC_ssp245_r1i1p1f1_gr', \
#             'EC-Earth3-Veg-LR_ssp245_r1i1p1f1_gr', \
             'FGOALS-g3_ssp245_r1i1p1f1_gn', \
#             'GISS-E2-1-G-CC_ssp245_r102i1p1f1_gn', \
             'GISS-E2-1-G_ssp245_r1i1p3f1_gn', \
             'MIROC6_ssp245_r1i1p1f1_gn', \
             'MIROC-ES2L_ssp245_r1i1p1f2_gn', \
             'MRI-ESM2-0_ssp245_r1i1p1f1_gn', \
             'NorESM2-LM_ssp245_r1i1p1f1_gn', \
             'NorESM2-MM_ssp245_r1i1p1f1_gn']
#
refidlist=expidlist # find automatically the piControl

wlist=[1.,-1.]
#
nexpid=len(expidlist)
#
legendlist=expidlist
#
smoothlist=np.zeros(nexpid,dtype=int)
#
shiftlist=np.zeros(nexpid,dtype=int)
#
code='duncan_ssp245'
#
variablelist=['tasmaxmin']
#        
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#
quit()
#
# tasmaxmin
#---------- 
#'AWI-CM-1-1-MR_ssp245_r1i1p1f1_gn'
#'CESM2_ssp245_r4i1p1f1_gn'
#'CESM2-WACCM_ssp245_r2i1p1f1_gn'
#'NESM3_ssp245_r1i1p1f1_gn'

expidlist=[\
#             'ACCESS-CM2_ssp245_r1i1p1f1_gn', \
#             'ACCESS-ESM1-5_ssp245_r1i1p1f1_gn', \
             'BCC-CSM2-MR_ssp245_r1i1p1f1_gn', \
             'CanESM5-CanOE_ssp245_r1i1p2f1_gn', \
             'CanESM5_ssp245_r1i1p2f1_gn', \
             'CAS-ESM2-0_ssp245_r1i1p1f1_gn', \
#            'CMCC-ESM2_ssp245_r1i1p1f1_gn', \
#             'CNRM-CM6-1-HR_ssp245_r1i1p1f2_gr', \
#             'CNRM-CM6-1_ssp245_r1i1p1f2_gr', \
#             'CNRM-ESM2-1_ssp245_r1i1p1f2_gr', \
#             'EC-Earth3-CC_ssp245_r1i1p1f1_gr', \
#             'EC-Earth3-Veg-LR_ssp245_r1i1p1f1_gr', \
             'FGOALS-g3_ssp245_r1i1p1f1_gn', \
#             'GISS-E2-1-G-CC_ssp245_r102i1p1f1_gn', \
             'GISS-E2-1-G_ssp245_r1i1p3f1_gn', \
             'MIROC6_ssp245_r1i1p1f1_gn', \
             'MIROC-ES2L_ssp245_r1i1p1f2_gn', \
             'MRI-ESM2-0_ssp245_r1i1p1f1_gn',\
             'NorESM2-LM_ssp245_r1i1p1f1_gn', \
             'NorESM2-MM_ssp245_r1i1p1f1_gn', \
             'NSSP245frc2_f19_tn14_20191014', \
             'NSSP245frc2_f09_tn14_20191105']
#
refidlist=[\
           'BCC-CSM2-MR_piControl_r1i1p1f1_gn', \
           'CanESM5-CanOE_piControl_r1i1p2f1_gn', \
           'CanESM5_piControl_r1i1p1f1_gn', \
           'CAS-ESM2-0_piControl_r1i1p1f1_gn', \
           'FGOALS-g3_piControl_r1i1p1f1_gn', \
           'GISS-E2-1-G_piControl_r1i1p3f1_gn', \
           'MIROC6_piControl_r1i1p1f1_gn', \
           'MIROC-ES2L_piControl_r1i1p1f2_gn', \
           'MRI-ESM2-0_piControl_r1i1p1f1_gn',\
           'NorESM2-LM_piControl_r1i1p1f1_gn', \
           'NorESM2-MM_piControl_r1i1p1f1_gn', \
           'N1850_f19_tn14_20190802', \
           'N1850frc2_f09_tn14_20191113'] 
#
wlist=[1.,-1.]
#
nexpid=len(expidlist)
#
legendlist=expidlist
#
smoothlist=np.zeros(nexpid,dtype=int)
#
shiftlist=np.zeros(nexpid,dtype=int)
#
code='duncan_ssp245_piControl'
#
variablelist=['tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin', \
              'tasmaxmin','tasmaxmin', \
              'TREFMXMNAV','TREFMXMNAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# maximum
variablelist=['tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax', \
              'tasmax','tasmax', \
              'TREFMXAV','TREFMXAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# minimum
variablelist=['tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin', \
              'tasmin','tasmin', \
              'TREFMNAV','TREFMNAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
# 
#
# SSP245
wlist=[1.,0.]
#
code='duncan_ssp245'
#
variablelist=['tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin', \
              'tasmaxmin','tasmaxmin', \
              'TREFMXMNAV','TREFMXMNAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# maximum
variablelist=['tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax', \
              'tasmax','tasmax', \
              'TREFMXAV','TREFMXAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# minimum
variablelist=['tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin', \
              'tasmin','tasmin', \
              'TREFMNAV','TREFMNAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
# 
#
# ONLY PICONTROL
expidlist=refidlist
wlist=[1.,0.]
#
code='duncan_piControl'
#
variablelist=['tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin', \
              'tasmaxmin','tasmaxmin', \
              'TREFMXMNAV','TREFMXMNAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# maximum
variablelist=['tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax','tasmax', \
              'tasmax','tasmax', \
              'TREFMXAV','TREFMXAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# minimum
variablelist=['tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin','tasmin', \
              'tasmin','tasmin', \
              'TREFMNAV','TREFMNAV']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
# 








# SENSITIVITIES
#--------------



expidlist=['NorESM2-LM_ssp245_r1i1p1f1_gn', \
#           'NorESM2-MM_ssp245_r1i1p1f1_gn', \
           'NSSP245frc2_f19_tn14_20191014']
#           'NSSP245frc2_f09_tn14_20191105']
#
refidlist=['NorESM2-LM_piControl_r1i1p1f1_gn', \
#           'NorESM2-MM_piControl_r1i1p1f1_gn', \
           'N1850_f19_tn14_20190722']
#          'N1850frc2_f09_tn14_20191001']
#
wlist=[1.,-1.]
#
nexpid=len(expidlist)
#
legendlist=expidlist
#
smoothlist=np.zeros(nexpid,dtype=int)
#
shiftlist=np.zeros(nexpid,dtype=int)
#
code='duncan_ssp245'
#
variablelist=['tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin', \
              'tasmaxmin']
variablelist=['tasmaxmin','tasmaxmin', \
              'TREFMXMNAV','TREFMXMNAV']
variablelist=['tasmaxmin','TREFMXMNAV']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)

#
variablelist=['tasmin','TREFMNAV']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
variablelist=['tasmax','TREFMXAV']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# Only piControl
expidlist=['NorESM2-LM_piControl_r1i1p1f1_gn', \
#           'NorESM2-MM_piControl_r1i1p1f1_gn', \
           'N1850_f19_tn14_20190722']
#          'N1850frc2_f09_tn14_20191001']
refidlist=expidlist
#
wlist=[1.,-1.]
#
nexpid=len(expidlist)
#
legendlist=expidlist
smoothlist=np.zeros(nexpid,dtype=int)
#
shiftlist=np.zeros(nexpid,dtype=int)
#
code='duncan_piControl'
#
variablelist=['tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin','tasmaxmin', \
              'tasmaxmin']
variablelist=['tasmaxmin','tasmaxmin', \
              'TREFMXMNAV','TREFMXMNAV']
variablelist=['tasmaxmin','TREFMXMNAV']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)

#
variablelist=['tasmin','TREFMNAV']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
variablelist=['tasmax','TREFMXAV']
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#





