import loopcmorize2

# MAIN PROGRAM

# precipitation and temperature
#------------------------------
#
expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01']
#
varlist=['pr','tas', \
         'rlds', 'rlus', 'rlut', 'rlutcs', \
         'rsds', 'rsdscs', 'rsdt', 'rsus', 'rsuscs', 'rsut', 'rsutcs', \
         'rlutaf', 'rlutcsaf', 'rsutaf', 'rsutcsaf', \
         'od550aer', \
         'o3', 'no', 'no2', 'co', \
         'clt', \
         'hfls', 'hfss', \
         'hurs', 'huss', \
         'ua', 'va']
#
varlist=['pr','o3','hur','hus']
#
varlist=[ \
#        'ccb', \ # not in Yanchuns table
#        'cct', \ # not in Yanchuns table
         'cl', 'cli', 'clivi', 'clt', 'clw', 'clwvi', \
         'evspsbl', \
         'hfls', 'hfss', \
         'hur', \
#        'hurs', \ # not in h0 file !!
         'hus', 'huss', \
         'o3', \
         'pr', 'prc', 'prsn', 'prw', \
         'ps', 'psl', \
         'rlds', 'rlus', 'rlut', 'rlutcs', \
         'rsds', 'rsdscs', 'rsdt', 'rsus', 'rsuscs', 'rsut', 'rsutcs', \
         'rtmt', \
         'sfcWind', \
         'ta', 'tas', \
         'tauu', 'tauv', \
         'ts', \
         'ua', \
         'va', \
         'wap', \
         'zg']

#varlist=['abs550aer', \
#         'airmass', \
#         'bldep', \
#         'ccn', 'cdnc', 'chepsoa', \
#         'co', \
#         'cod', \
#         'dms', \
#         'drybc', 'drydust', 'dryoa', 'dryso2', 'dryso4', 'dryss', \
#         'emibc', 'emibvoc', 'emidms', 'emidust', 'emiisop', 'emioa', 'emiso2', 'emiso4', 'emiss', 'emivoc', \
#         'isop', \
#         'lwp', \
#         'mmraerh2o', 'mmrbc', 'mmrdust', 'mmroa', 'mmrpm1', 'mmrpm2p5', 'mmrso4', 'mmrsoa', 'mmrss', \
#         'n2o','no','no2','o3','o3st', \
#         'o3loss','o3prod', \
#         'od440aer', 'od550aer', 'od550aerh2o', 'od550bc', 'od550csaer', 'od550dust', 'od550lt1aer', 'od550oa', 'od550so4', 'od550ss', 'od870aer', \
#         'oh', \
#         'pfull', 'phalf', 'ps', \
#         'reffclwtop', \
#         'rlutaf', 'rlutcsaf', 'rsutaf', 'rsutcsaf', \
#         'so2', \
#         'ua', 'va', \
#         'wetbc', 'wetdust', 'wetoa', 'wetso2', 'wetso4', 'wetss' \
#         'zg', 'ztp']


overwrite=True
#overwrite=False
loopcmorize2.loopcmorize2(expidlist=expidlist,varlist=varlist,overwrite=overwrite)
