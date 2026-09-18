import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# I. IMPOSE SIMULATIONS + TEST SIMULATIONS
#-----------------------
code='n20250719_navigate_esm_geoeng'
figlayout=cfiglayout.CFigLayout(xrange=[1850,1990])

expidlist=[ \
           'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316', \
           'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224', \
           'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
            \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250716', \
#           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250716', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250730', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20250921', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251005', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01a', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02a', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03a']    

#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'B3','','', \
            'B3C1a','','', \
            'B4','','', \
#            '1 (Tg[S]/yr)/(W/m2)', \
#            '1.5 (Tg[S]/yr)/(W/m2)',\
            '1 (Tg[S]/yr)/(W/m2)', \
            '1 (Tg[S]/yr)/(W/m2)', \

            '1.5 (Tg[S]/yr)/(W/m2)','','', \
            '1.5 (Tg[S]/yr)/(W/m2)','','', \
#
            '1.95 (Tg[S]/yr)/(W/m2) [15N-60N]', \
            '', \
#
            '1.5 (Tg[S]/yr)/(W/m2) [15N-60N]','','', \
            '','','']
#
smoothlist=[0,0,0, 0,0,0, 0,0,0, 0, 0, 0,0,0, 0,0,0, 0, 0, 0,0,0, 0,0,0]
#smoothlist=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#smoothlist=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
colorlist=[0,0,0, 1,1,1, 2,2,2, 3, 4, 5,5,5, 6,6,6, 7, 7, 8,8,8, 8,8,8]
linestylelist=smoothlist
shiftlist=smoothlist
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['cb_SO2','cb_SULFATE','TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden', \
              'AOD_VISdivDAYFOC'] 
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



# II. LONGER TIMESERIES
#----------------------
code='n20250719_navigate_esm_geoeng_long'
figlayout=cfiglayout.CFigLayout()
# atmosphere
variablelist=['cb_SO2','cb_SULFATE','TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden']
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
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.0TgSperRF_f19_tn14_20250730', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20250921', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251005', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01a', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02a', \
            \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03a']
#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            '1 (Tg[S]/yr)/(W/m2)', \
            '1 (Tg[S]/yr)/(W/m2)', \
            '1.5 (Tg[S]/yr)/(W/m2)', \
            '1.5 (Tg[S]/yr)/(W/m2)', \
            '15N-60N (strong)', \
            '15N-60N (strong)', \
            '15N-60N (weak)', \
            '15N-60N (weak)', \
            '', \
            '', \
            '', \
            '']

#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
colorlist=[0,1,2,3,4,5,6,7,6,7,6,7]
linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['EMI_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2']
typevarlist=['glob']


figlayout=cfiglayout.CFigLayout()
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
