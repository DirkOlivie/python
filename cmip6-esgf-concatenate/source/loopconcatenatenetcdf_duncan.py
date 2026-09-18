import numpy as np
import loopconcatenatenetcdf2

# MAIN PROGRAM

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
varlist=['pr','tas']
#
#expidlist=['FIO-ESM-2-0_ssp245_r1i1p1f1_gn']
#
#varlist=['tas']
#
loopconcatenatenetcdf2.loopconcatenatenetcdf2(expidlist=expidlist,varlist=varlist)
#
# tasmax, tasmin
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

#expidlist=['NorESM2-LM_ssp245_r1i1p1f1_gn', \
#           'NorESM2-MM_ssp245_r1i1p1f1_gn']

varlist=['tasmax','tasmin']
#
loopconcatenatenetcdf2.loopconcatenatenetcdf2(expidlist=expidlist,varlist=varlist)
