import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

#
typevarlist=['glob']
wlist=[1.,0.]
description='typevarcommon'
figlayout=cfiglayout.CFigLayout()
freqtypelist=['YEA']
code='n20250602_esm2025_ch4_amip'
#
#
# dry deposition, emissions [CNRM/NorESM]
#--------------------------------------------------
#
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506']
refidlist=expidlist
smoothlist=[0,0]
shiftlist=[0,0]
colorlist=[0,1]
linestylelist=[0,0]
#
description='typevarcommon'
variablegrouplist=[['minusdrych4','DF_CH4']]
legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)']
for freqtype in freqtypelist : 
    for variablelist in variablegrouplist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

#
# emissions : online + presribed [NorESM]
#--------------------------------------------------
#
expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506']

refidlist=expidlist
smoothlist=[0,0,0]
shiftlist=[0,0,0]
colorlist=[1,2,3]
linestylelist=[0,0,0]
#
description='typevarcommon'
variablegrouplist=[['SFCH4','FCH4xLANDFRAC','FCH4xLANDFRAC']]
legendlist=['NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)']
#for freqtype in freqtypelist :
#    for variablelist in variablegrouplist : 
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ch4 surface concentration [CNRM / NorESM / UKESM / CanESM5]
#------------------------------------------------------------
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn', \
           'CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn', \
           'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']
          
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,1,2,3,4]
linestylelist=[0,0,2,0,0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['ch4_surfacelayer','CH4_SRF','CH4_SRF','ch4_surfacelayer','ch4_surfacelayer','ch4_surfacelayer'], \
                   ['ch4_columnburden','cb_CH4','cb_CH4','ch4_columnburden','ch4_columnburden','ch4_columnburden'], \
                   ['ch4lossoh_columnburden','r_CH4_OH_columnburden','r_CH4_OH_columnburden','lossch4_columnburden','ch4lossoh_columnburden','ch4lossoh_columnburden'], \
#                   ['tau_ch4_ohtrop','TAU_CH4_OHTROP','TAU_CH4_OHTROP','tau_ch4_lossch4_trop','tau_ch4_ohtrop'], \
                   ['tas','TREFHT','TREFHT','tas','tas','tas'], \
                   ['clt', 'CLDTOT','CLDTOT','clt','clt','clt'], \
                   ['pr','PRECT','PRECT','pr','pr','pr'] \
                  ]
legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)', \
            'UKESM1-0-LL (AMIP-ch4ems)', \
            'CanESM5-1c (AMIP-ch4ems)', \
            'MIROC-ES2L-CHEM (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ch4 dry deposition [CNRM / NorESM / CanESM5]
#------------------------------------------------------------
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn']
          
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,3]
linestylelist=[0,0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['minusdrych4','DF_CH4','ch4losssoil'] \
                  ]
legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'CanESM5-1c (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# ch4 surface concentration [CNRM / NorESM / CanESM5 / MIROC]
#------------------------------------------------------------
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn', \
           'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']          
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,3,4]
linestylelist=[0,0,0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['emich4','SFCH4','emich4_canesm5','emich4'] \
                  ]
legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'CanESM5-1c (AMIP-ch4ems)', \
            'MIROC-ES2L-CHEM (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# surface concentration [CNRM / NorESM / UKESM]
#----------------------------------------------
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,1,2]
linestylelist=[0,0,2,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['o3_surfacelayer','O3_SRF','O3_SRF','o3_surfacelayer'], \
                   ['tau_ch4_ohtrop','TAU_CH4_OHTROP','TAU_CH4_OHTROP','tau_ch4_lossch4_trop'] \
                    ]

legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)', \
            'UKESM1-0-LL (AMIP-ch4ems)']

#for variablelist in variablegrouplist :
#    for freqtype in freqtypelist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# LOSS PROCESSES [CNRM / NorESM / MIROC]
#----------------------------------------
expidlist=[\
           'CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,1,1,4]
linestylelist=[0,0,2,0]
#
description='typevarcommon'
variablegrouplist=[ \
#                    ['ch4lossoh_columnburden','r_CH4_OH_columnburden','r_CH4_OH_columnburden'], \
                    ['ch4losscl_columnburden','r_CL_CH4_columnburden','r_CL_CH4_columnburden','ch4losscl_columnburden'], \
                    ['ch4losso1d_columnburden','r_O1D_CH4abc_columnburden','r_O1D_CH4abc_columnburden','ch4losso1d_columnburden']]
#                    ['tau_ch4_ohtrop','TAU_CH4_OHTROP','TAU_CH4_OHTROP']]
legendlist=[ \
            'CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)', \
            'MIROC-ES2L-CHEM (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# LOSS PROCESSES [CNRM / UKESM]
#----------------------------------------------
expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[0,2]
linestylelist=[0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['lossch4_columnburden','lossch4_columnburden'] \
                    ]
legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
            'UKESM1-0-LL (AMIP-ch4ems)']

#for variablelist in variablegrouplist :
#    for freqtype in freqtypelist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# LOSS PROCESSES [CNRM / NorESM]
#----------------------------------------
expidlist=[\
#           'CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[1,1]
linestylelist=[0,2]
#
description='typevarcommon'
#variablegrouplist=[ \
#                    ['r_CH4_OH_columnburden','r_CH4_OH_columnburden'], \
#                    ['r_CL_CH4_columnburden','r_CL_CH4_columnburden'], \
#                    ['r_O1D_CH4abc_columnburden','r_O1D_CH4abc_columnburden']]
#                    ['TAU_CH4_OHTROP','TAU_CH4_OHTROP']]
legendlist=[ \
#            'CNRM-ESM2-1 (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)']

#for variablelist in variablegrouplist :
#    for freqtype in freqtypelist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




# OH columnburden [NorESM / UKESM]
#----------------------------------------------
expidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[1,1,2]
linestylelist=[0,2,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['CO_SRF','CO_SRF','co_surfacelayer'] \
                    ]
legendlist=[ \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)', \
            'UKESM1-0-LL (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# OH columnburden [NorESM / UKES / MIROC]
#----------------------------------------------
expidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn', \
           'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[1,1,2,4]
linestylelist=[0,2,0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['OH_columnburden','OH_columnburden','oh_columnburden','oh_columnburden'], \
                    ]
legendlist=[ \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)', \
            'UKESM1-0-LL (AMIP-ch4ems)', \
            'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# OH columnburden [NorESM / UKESM / CanESM /MIROC]
#-------------------------------------------------
expidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
           'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn', \
           'CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn', \
           'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[1,1,2,3,4]
linestylelist=[0,2,0,0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['OH_columnburden','OH_columnburden','oh_columnburden','oh_columnburden','oh_columnburden'], \
                    ]
legendlist=[ \
            'NorESM2.3-LM-C (AMIP-ch4ems)', \
            'NorESM2.3-LM-C (AMIP)', \
            'UKESM1-0-LL (AMIP-ch4ems)', \
            'CanESM5-1c (AMIP-ch4ems)', \
            'UKESM1-0-LL (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# lightning NOx [UKESM / MIROC]
#----------------------------------------------
expidlist=[ \
           'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn', \
           'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']
refidlist=expidlist
nexpid=len(expidlist)
smoothlist=[0] * nexpid
shiftlist=[0] * nexpid
colorlist=[2,4]
linestylelist=[0,0]
#
description='typevarcommon'
variablegrouplist=[ \
                   ['emilnox_columnburden','emilnox_columnburden'], \
                    ]
legendlist=[ \
            'UKESM1-0-LL (AMIP-ch4ems)', \
            'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn (AMIP-ch4ems)']

for variablelist in variablegrouplist :
    for freqtype in freqtypelist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


