import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
figlayout=cfiglayout.CFigLayout()
figlayoutcmip6=cfiglayout.CFigLayout(xrange=[-5,55])
code='n20251107_n2olandocean_coupling'


# stratospheric aerosol

# 1. WITHOUT ANY N2O DIAGNOSTICS
#-------------------------------
expidlist=['N1850_f19_tn14_20190621', \
           'NorESM-Ncyc_uncoupled-01_N1850vsls_tropstratchem_prep_f19_tn14_noresm2.0.2-BLOMv1.6.9enhanced_20250911T1754', \
           'NorESM-Ncyc_coupled-01_N1850vslsn2onh3_tropstratchem_prep_f19_tn14_noresm2.0.2-BLOMv1.6.9enhanced_20250917T1358', \
           'N1850vslsn2onh3_f19_tn14_test02', \
           'N1850vslsn2onh3_f19_tn14_test03', \
           'N1850vslsn2onh3_f19_tn14_test04', \
           'N1850vslsn2onh3_f19_tn14_test05', \
           'N1850vslsn2onh3_f19_tn14_test06', \
           'N1850vslsn2onh3_f19_tn14_test07', \
           'N1850vslsn2onh3_f19_tn14_test08', \
           'N1850vslsn2onh3_f19_tn14_test09', \
           'N1850vslsn2onh3_f19_tn14_test10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2-LM', \
            'SIMA (J)', \
            'SIMB (J)', \
            'SIM2 (D)', \
            'SIM3 (D)', \
            'SIM4 (D)', \
            'SIM5 (D)', \
            'SIM6 (D)', \
            'SIM7 (D)', \
            'SIM8 (D)', \
            'SIM9 (D)', \
            'SIM10 (D)']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,6,7,8,9,10,11]
#            
shiftlist=[-1599,0,0,0,0,0,0,0,0,0,0,0]
#
variablelist=['TREFHT', 'PRECT', \
#             'F_N2O_DENIT','F_N2O_NIT', \
#              'emin2oland', \
#              'F_N2O_DENITxLANDFRAC','F_N2O_NITxLANDFRAC', 'F_N2O_DENIT_NITxLANDFRAC',\
              'F_N2O_DENIT_NITxLANDFRAC_as_N2O', \
              'F_N2O_DENIT_NITxLANDFRAC', \
              'NDEP_TO_SMINNxLANDFRAC', \
              'NDEP_TO_SMINNxLANDFRAC', \
              'NFERTILIZATIONxLANDFRAC', \
#               'cb_N2O','N2O_SRF','SFN2O','SFN2O_as_N', \
#              'TAU2_N2O','minusGS_N2O']
              'co2vmr','ch4vmr','n2ovmr','f11vmr','f12vmr', \
              'tempocn']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayoutcmip6,colorlist=colorlist)

# 2. WITH N2O DIAGNOSTICS (EXCLUDING NORESM2-LM)
#-----------------------------------------------
expidlist=[ \
           'NorESM-Ncyc_uncoupled-01_N1850vsls_tropstratchem_prep_f19_tn14_noresm2.0.2-BLOMv1.6.9enhanced_20250911T1754', \
           'NorESM-Ncyc_coupled-01_N1850vslsn2onh3_tropstratchem_prep_f19_tn14_noresm2.0.2-BLOMv1.6.9enhanced_20250917T1358', \
           'N1850vslsn2onh3_f19_tn14_test02', \
           'N1850vslsn2onh3_f19_tn14_test03', \
           'N1850vslsn2onh3_f19_tn14_test04', \
           'N1850vslsn2onh3_f19_tn14_test05', \
           'N1850vslsn2onh3_f19_tn14_test06', \
           'N1850vslsn2onh3_f19_tn14_test07', \
           'N1850vslsn2onh3_f19_tn14_test08', \
           'N1850vslsn2onh3_f19_tn14_test09', \
           'N1850vslsn2onh3_f19_tn14_test10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'SIMA (J)', \
            'SIMB (J)', \
            'SIM2 (D)', \
            'SIM3 (D)', \
            'SIM4 (D)', \
            'SIM5 (D)', \
            'SIM6 (D)', \
            'SIM7 (D)', \
            'SIM8 (D)', \
            'SIM9 (D)', \
            'SIM10 (D)']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0]
#
colorlist=[1,2,3,4,5,6,7,8,9,10,11]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0,0]
#
variablelist=[ \
              'cb_O3', \
              'SFNH3','NH3_SRF','cb_NH3','WD_NH3','DF_NH3', \
              'SFNH4','NH4_SRF','cb_NH4','WD_NH4','DF_NH4', \
              'SFNHDEP','NHDEP_SRF','cb_NHDEP','WD_NHDEP', \
              'cb_N2O','N2O_SRF','SFN2O','SFN2O_as_N', \
              'TAU2_N2O','minusGS_N2O', \
              'emin2oocean','eminh3ocean', \
              'ndepnoyocn','ndepnhxocn', \
              'nh3fluxocn','n2ofluxocn', \
              'atmnh3ocn','atmn2oocn','atmco2ocn']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

#
variablelist=['NH3_SRF']
typevarlist=['SEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



# 3. WITH N2O LAND COUPLING DIAGNOSTICS (EXCLUDING NORESM2-LM)
#-----------------------------------------------
expidlist=[ \
           'N1850vslsn2onh3_f19_tn14_test02', \
           'N1850vslsn2onh3_f19_tn14_test03', \
           'N1850vslsn2onh3_f19_tn14_test04', \
           'N1850vslsn2onh3_f19_tn14_test05', \
           'N1850vslsn2onh3_f19_tn14_test06', \
           'N1850vslsn2onh3_f19_tn14_test07', \
           'N1850vslsn2onh3_f19_tn14_test08', \
           'N1850vslsn2onh3_f19_tn14_test09', \
           'N1850vslsn2onh3_f19_tn14_test10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'SIM2 (D)', \
            'SIM3 (D)', \
            'SIM4 (D)', \
            'SIM5 (D)', \
            'SIM6 (D)', \
            'SIM7 (D)', \
            'SIM8 (D)', \
            'SIM9 (D)', \
            'SIM10 (D)']
#
smoothlist=[0,0,0,0,0,0,0,0,0]
#
colorlist=[3,4,5,6,7,8,9,10,11]
#            
shiftlist=[0,0,0,0,0,0,0,0,0]
#
variablelist=[ \
              'emin2oland', \
              'emin2oland_as_N2O']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 3. WITH N2O LAND COUPLING DIAGNOSTICS (EXCLUDING NORESM2-LM)
#-----------------------------------------------
expidlist=[ \
           'N1850vslsn2onh3_f19_tn14_test01b', \
           'N1850vslsn2onh3_f19_tn14_test04', \
           'N1850vslsn2onh3_f19_tn14_test05', \
           'N1850vslsn2onh3_f19_tn14_test06', \
           'N1850vslsn2onh3_f19_tn14_test07', \
           'N1850vslsn2onh3_f19_tn14_test08', \
           'N1850vslsn2onh3_f19_tn14_test09', \
           'N1850vslsn2onh3_f19_tn14_test10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'SIM1b (D)', \
            'SIM4 (D)', \
            'SIM5 (D)', \
            'SIM6 (D)', \
            'SIM7 (D)', \
            'SIM8 (D)', \
            'SIM9 (D)', \
            'SIM10 (D)']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
colorlist=[2,5,6,7,8,9,10,11]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=[ \
              'wet_deposition_NHx_as_N', \
              'dry_deposition_NHx_as_N', \
              'wetdry_deposition_NHx_as_N', \
              'wet_deposition_NOy_as_N', \
              'dry_deposition_NOy_as_N', \
              'wetdry_deposition_NOy_as_N', \
              'wetdry_deposition_NHxNOy_as_N', \
#              'r_jn2o_columnburden', \
              'r_O1D_N2Oa_columnburden', \
              'r_O1D_N2Ob_columnburden', \
              'r_N_NO2a_columnburden']
#
typevarlist=['glob','LAND','SEA']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 
variablelist=['r_jn2o_columnburden','r_jn2o_columnburden','r_jn2o_columnburden','r_jn2o_columnburden','r_jn2o_columnburden', \
              'r_jn2o_mod_columnburden', \
              'r_jn2o_mod_columnburden', \
              'r_jn2o_columnburden']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description='typevarcommon',code=code,figlayout=figlayout,colorlist=colorlist)


# 3. WITH N2O LAND COUPLING DIAGNOSTICS (EXCLUDING NORESM2-LM)
#-----------------------------------------------
expidlist=[ \
           'N1850vslsn2onh3_f19_tn14_test02', \
           'N1850vslsn2onh3_f19_tn14_test03', \
           'N1850vslsn2onh3_f19_tn14_test05', \
           'N1850vslsn2onh3_f19_tn14_test06', \
           'N1850vslsn2onh3_f19_tn14_test07', \
           'N1850vslsn2onh3_f19_tn14_test08', \
           'N1850vslsn2onh3_f19_tn14_test09', \
           'N1850vslsn2onh3_f19_tn14_test10']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'SIM2 (D)', \
            'SIM3 (D)', \
            'SIM5 (D)', \
            'SIM6 (D)', \
            'SIM7 (D)', \
            'SIM8 (D)', \
            'SIM9 (D)', \
            'SIM10 (D)']
#
smoothlist=[0,0,0,0,0,0,0,0]
#
colorlist=[3,4,6,7,8,9,10,11]
#            
shiftlist=[0,0,0,0,0,0,0,0]
#
variablelist=[ \
              'FN2OxLANDFRAC_as_N2O']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
