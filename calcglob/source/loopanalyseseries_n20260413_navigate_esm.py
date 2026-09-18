import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'

###############################################
# 1. IMPOSE SIMULATIONS ALONE : absolute values
#       B4C1a
#       B4
###############################################

code='n20260413_navigate_esm_impose'
figlayout=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200])

expidlist=[ \
           'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316pre', \
            \
           'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316']
#
refidlist=['N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm']
dorefaverage=True
#
wlist=[1.,-1.]

ensembletypelist=['minmax','minmax']
legendlist=['2000 Pg[C] + CDR (500 Pg[C])', \
            '1500 Pg[C]'] 
#
smoothlist=[5,5]
colorlist=[7,9]
linestylelist=[0,0]
shiftlist=[-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
variablelist=['TREFHT','SFCO2_FFF_cumulative','SFCO2_FFF','co2vmr','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
typevarlist=['glob']
#for freqtype in freqtypelist : 
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist, ensembletypelist=ensembletypelist)



#############################################
# 2. IMPOSE SIMULATIONS ALONE DIFFERENCES
################################################

code='n20260413_navigate_esm_diff'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=[ 'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316pre']
        
refidlist=['N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316']
#
dorefaverage=None
#
wlist=[1.,-1.]

ensembletypelist=['minmax']
legendlist=['2000 Pg[C] + CDR (500 Pg[C]) minus 1500 Pg[C]'] 
#
smoothlist=[5]
colorlist=[7]
linestylelist=[0]
shiftlist=[-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['CO2_columnburden_as_RF','TREFHT']
typevarlist=['glob']
#for freqtype in freqtypelist : 
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
#
# amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)



###################################
# 3. NAVIGATE 30S-30N 
###################################
 
code='n20260413_navigate_esm_diff'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=['N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250730pre']
refidlist=expidlist        
#
dorefaverage=None
#
wlist=[1.,0.]

ensembletypelist=['minmax','minmax','minmax','']
legendlist=['2000 Pg[C] + CDR (500 Pg[C]) + SAI (TR)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (NH)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (SH)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (TR, weak)']  
#
smoothlist=[5,5,5,5]
colorlist=[3,2,0,3]
linestylelist=[0,0,0,2]
shiftlist=[-1849,-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['EMI_SO2SO4_as_SO2_TOT_noresm2_offsetlast30yr', \
              'EMI_SO2SO4_as_S_TOT_noresm2_offsetlast30yr']
typevarlist=['glob']
#for freqtype in freqtypelist : 
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

#
###############################################
# 4. IMPOSE SIMULATIONS + NAVIGATE (TR) 
#       B4C1a
#       B4
###############################################

code='n20260413_navigate_esm'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=[ \
           'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316pre', \
            \
           'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre']
#
refidlist=['N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm']
dorefaverage=True
#
wlist=[1.,-1.]

ensembletypelist=['minmax','minmax','minmax']
legendlist=['2000 Pg[C] + CDR (500 Pg[C])', \
            '1500 Pg[C]', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (TR)'] 
#
smoothlist=[5,5,5]
colorlist=[7,9,3]
linestylelist=[0,0,0]
shiftlist=[-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
variablelist=['PRECT','TREFHT','SFCO2_FFF_cumulative','SFCO2_FFF','co2vmr','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
typevarlist=['glob']
#for freqtype in freqtypelist : 
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
#
# amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

###############################################
# 5.a IMPOSE SIMULATIONS + NAVIGATE (TR, NH, SH) 
#       B4C1a
#       B4
###############################################

code='n20260413_navigate_esm_trnhsh'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=[ \
           'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316pre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre']

#
refidlist=['N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm']
dorefaverage=True
#
wlist=[1.,-1.]

ensembletypelist=['minmax','minmax','minmax','minmax']
legendlist=['2000 Pg[C] + CDR (500 Pg[C])', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (TR)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (NH)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (SH)'] 
#
legendlist=['CDR', \
            'CDR+SAI(TR)', \
            'CDR+SAI(NH)', \
            'CDR+SAI(SH)']  
#
smoothlist=[5,5,5,5]
colorlist=[7,3,2,0]
linestylelist=[0,0,0,0]
shiftlist=[-1849,-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
variablelist=['PRECT','TREFHT','SFCO2_FFF_cumulative','SFCO2_FFF','co2vmr','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['PRECT']
typevarlist=['glob','NH','SH','28S28N','LAND','SEA']
#for freqtype in freqtypelist : 
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# atmosphere : 60N90N
variablelist=['TREFHT']
typevarlist=['60N90N']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

# amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

###############################################
# 5.b IMPOSE SIMULATIONS + NAVIGATE (TR, NH, SH)  [ONLY MEMBER 2+3 FROM IMPOSE]
#       B4C1a
#       B4
###############################################

code='n20260413_navigate_esm_trnhsh_ref'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=[ \
           'N1850frc2esm_IMPOSE_C1a_23_f19_tn14_20200316pre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre']

#
refidlist=['N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm']
dorefaverage=True
#
wlist=[1.,-1.]

ensembletypelist=['minmax','minmax','minmax','minmax']
legendlist=['2000 Pg[C] + CDR (500 Pg[C])', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (TR)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (NH)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (SH)'] 
#
legendlist=['CDR', \
            'CDR+SAI(TR)', \
            'CDR+SAI(NH)', \
            'CDR+SAI(SH)']  
#
smoothlist=[5,5,5,5]
colorlist=[7,3,2,0]
linestylelist=[0,0,0,0]
shiftlist=[-1849,-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['AOD_VISdivDAYFOC','U10','cb_isoprene','cb_monoterp','cb_DUST','cb_SALT']
typevarlist=['glob']
#for freqtype in freqtypelist : 
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)

###############################################
# 6. NAVIGATE (TR, NH, SH) 
#       B4C1a
#       B4
###############################################

code='n20260413_navigate_esm_trnhsh'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=[\
           'N1850_f19_tn14_20190730esm', \
            \
           'N1850frc2esm_IMPOSE_C1a_23_f19_tn14_20200316pre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre', \
            \
           'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
            \
           'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316']
#
refidlist=expidlist
dorefaverage=True
#
wlist=[1.,0.]

ensembletypelist=['minmax','minmax','minmax','minmax','minmax','minmax','minmax']
legendlist=['piControl', \
            '2000 Pg[C] + CDR (500 Pg[C]', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (TR)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (NH)', \
            '2000 Pg[C] + CDR (500 Pg[C]) + SAI (SH)', \
            'B3', \
            'B4'] 
#
smoothlist=[5,5,5,5,5,5,5]
colorlist=[1,7,3,2,0,4,5]
linestylelist=[0,0,0,0,0,0,0]
shiftlist=[-1750,-1849,-1849,-1849,-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
variablelist=['PRECT','TREFHT','SFCO2_FFF_cumulative','SFCO2_FFF','co2vmr','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['cb_isoprene','cb_monoterp','cb_SULFATE_offsetlast30yr','cb_SULFATE','AOD_VISdivDAYFOC','cb_DUST','cb_SALT','cb_OM','cb_SULFATE','cb_SOA_A1NA'] 
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
# amoc
#variablelist=['mmflxdmax26.0Nocn']
#typevarlist=['atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)


###############################################
# 7. NAVIGATE (TR, NH, SH) 
#       B4C1a
#       B4
###############################################

code='n20260413_navigate_esm_trnhsh_impose'
#figlayout=cfiglayout.CFigLayout(axhline=0)

expidlist=[\
           'N1850_f19_tn14_20190730esm', \
            \
           'N1850frc2esm_IMPOSE_C1a_23_f19_tn14_20200316pre', \
            \
           'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
            \
           'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316']
#
refidlist=expidlist
dorefaverage=True
#
wlist=[1.,0.]

ensembletypelist=['minmax','minmax','minmax','minmax']
legendlist=['piControl', \
            '2000 Pg[C] + CDR (500 Pg[C]', \
            'B3', \
            'B4'] 
#
smoothlist=[5,5,5,5]
colorlist=[1,7,4,5]
linestylelist=[0,0,0,0]
shiftlist=[-1750,-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
variablelist=['PRECT','TREFHT','SFCO2_FFF_cumulative','SFCO2_FFF','co2vmr','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['cb_SULFATE'] 
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)
# amoc
#variablelist=['mmflxdmax26.0Nocn']
#typevarlist=['atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,dorefaverage=dorefaverage,colorlist=colorlist,linestylelist=linestylelist,ensembletypelist=ensembletypelist)


