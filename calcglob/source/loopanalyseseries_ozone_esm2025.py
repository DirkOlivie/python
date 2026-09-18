import loopanalyseseries2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# stratospheric aerosol

# 1. TOTAL AOD
#-------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
# CESM 1970-2014 (1x1)
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem (SO'+r'$_2$'+' 100%)', \
            'FullChem (SO'+r'$_4$'+' 100%)', \
            'FullChem (SO'+r'$_2$'+' 50%/SO'+r'$_4$'+' 50%)', \
            'FullChem (SO'+r'$_2$'+' 97.5%/SO'+r'$_4$'+' 2.5%)', \
            'CESM (1x1)']
smoothlist=[0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0]
#
variablelist=[ \
              'AOD_VISdivDAYFOC', \
              'DOD550divDAYFOC', \
              'DOD550divDAYFOC', \
              'DOD550divDAYFOC', \
              'DOD550divDAYFOC', \
              'AODVISdn']
#
code='kclim_ozone_esm2025'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)


# 2. TOTAL SO4 load
#-------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
# CESM 1970-2014
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem (SO2 100%)', \
            'FullChem (SO4 100%)', \
            'FullChem (SO2 50%/SO4 50%)', \
            'FullChem (SO2 97.5%/SO4 2.5%)', \
            'CESM (1x1)']
#            
shiftlist=[0,0,0,0,0,0]
smoothlist=[0,0,0,0,0,0]
#
variablelist=['cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_SULFATE','cb_so4_a123']
#
code='kclim_ozone_esm2025'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code)
#
# 3. D550_SO4
#------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05']
#
legendlist=['Oslo-Aero', \
            'FullChem (SO2 100%)', \
            'FullChem (SO4 100%)', \
            'FullChem (SO2 50%/SO4 50%)', \
            'FullChem (SO2 97.5%/SO4 2.5%)']
#            
shiftlist=[0,0,0,0,0]
smoothlist=[0,0,0,0,0]
#
variablelist=['D550_SO4']
#
code='kclim_ozone_esm2025'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
#
# 4. TOTAL OZONE COLUMN
#----------------------
expidlist=[ \
# Oslo-Aero 1850-2014
           'NFHISTnorbc_f19_20191107', \
# Full chemistry NorESM
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
# CESM 1970-2014
           'FCHIST_f19_mg17_20220111_test1', \
# CESM 1970-2014
           'FCHIST_f09_mg17_20220111_test7']
#
legendlist=['Oslo-Aero', \
            'FullChem', \
            'CESM (2x2)', \
            'CESM (1x1)']
#            
shiftlist=[0,0,0,0]
smoothlist=[0,0,0,0]
#
variablelist=['cb_O3']
#
code='kclim_ozone_esm2025'
#
# global mean
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code)
# 90S28SLAND
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,smoothlist=smoothlist,shiftlist=shiftlist,variablelist=['cb_O3'],typevar='90S28SLAND',freqtype='SON',description=description,code=code)
