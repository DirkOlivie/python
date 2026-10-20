import buildconcentrationloop2

'''
VARIABLES TO BE DEFINED
    overwrite          : True | False
    version
    i4mpdownloadlist   :
    specieslist        : variable name in final file
    overwrite          : True | False
    timeresolutionlist : 'monthly'
    periodlist         : 
    region             : 'GLOBAL' | 'ZONAL'            : ORIGINAL spatial resolution
    nlatlist           : 1 | 360                       : FINAL    spatial resolution    

CALLS
    buildconcentrationloop2

'''
specieslist  = ['CCL4_LBC', 'CF2CLBR_LBC', 'CF3BR_LBC', 'CFCL3_LBC', 'CFC113_LBC', 'CF2CL2_LBC', 'CH3BR_LBC', 'CH3CCL3_LBC', 'CH3CL_LBC', 'CH4_LBC', \
                'CO2_LBC', 'H2_LBC', 'HCFC22_LBC', 'N2O_LBC', 'CFC114_LBC', 'CFC115_LBC', 'HCFC141B_LBC', 'HCFC142B_LBC', 'CH2BR2_LBC', 'CHBR3_LBC', 'H2402_LBC', \
                'OCS_LBC', 'SF6_LBC']
nlatlist     = [360]
time_units   = 'days since 1750-01-01'
calendar     = 'noleap'
timeresolutionlist = ['monthly']
regionlist = ['ZONAL']



if ( False ) :
#
#   piControl / historical
#
    overwrite    = True
    version      = 'version20260829'
#
    scenariolist = ['CMIP'] ; i4mpdownloadlist = ['CR-CMIP-1-0-0'] 
    periodlist   = ['1850-1850','1750-2023']
#
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)

if ( True ) :
#
    overwrite    = True
    version      = 'version20260829'
#
    scenariolist     = ['ScenarioMIP'] ; i4mpdownloadlist = ['CR-h-1-1-0' , \
                                                             'CR-hl-1-1-0', \
                                                             'CR-l-1-1-0' , \
                                                             'CR-ln-1-1-0', \
                                                             'CR-m-1-1-0' , \
                                                             'CR-ml-1-1-0', \
                                                             'CR-vl-1-1-0']
    periodlist = ['2022-2100']
#    
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
