import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
code='n20251203_navigate_esm_geoeng_long'
figlayout=cfiglayout.CFigLayout()



# I. IMPOSE SIMULATIONS + TEST SIMULATIONS
#-----------------------

expidlist=[ \
           'N1850_f19_tn14_20190730esm', \
#           'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
           'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316pre', \
            \
#           EQ
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
#           NH
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
#           SH
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre']
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens01a', \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens02a', \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens03a']

#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'piControl-esm', \
#            'B3', \
            '1500Pg', \
            '2000Pg+CDR', \
            '2000Pg+CDR+SAI(TR)', \
            '2000Pg+CDR+SAI(NH)', \
            '2000Pg+CDR+SAI[SH]']
#
smoothlist=[5,5,5,5,5,5]
colorlist=[4,1,7,3,2,0]
linestylelist=[0,0,0,0,0,0]
shiftlist=[-1750,-1849,-1849,-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['cb_SO2','cb_SULFATE','TREFHT','PRECT','CLDTOT','PRECT','FSDS','FSDSC','SFCO2_FFF','co2vmr','CO2_columnburden', \
              'AOD_VISdivDAYFOC','FSNT','FLNT'] 
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['glob','atlarc']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# III. EMISSIONS (NOT AVAILABLE IN IMPOSE)
#-----------------------------------------
expidlist=[ \
#           'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
#           'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
#           'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316', \
            \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
            \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
#
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre']
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens01a', \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens02a', \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens03a']
#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
#            'B3', \
#            'B4', \
#            'B3C1a', \
            'CDR+SAI(TR)', \
            'CDR+SAI(NH)', \
            'CDR+SAI(SH)']
#
smoothlist=[5,5,5]
colorlist=[3,2,0]
linestylelist=[0,0,0]
shiftlist=[-1849,-1849,-1849]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['EMI_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2']
typevarlist=['glob']


figlayout=cfiglayout.CFigLayout()
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
