import buildconcentrationloop2

'''
VARIABLES TO BE DEFINED
    version
    i4mpdownload
    specieslist        : variable name in final file
    overwrite          : True | False
    timeresolutionlist : 'monthly'
    periodlist         : 
    region             : 'GLOBAL' | 'ZONAL'            : original spatial resolution
    nlatlist           : 1 | 360                       : final spatial resolution    

CALLS
    buildconcentrationloop2

'''

if ( 1 == 1 ) :
#
    overwrite    = True
#   version      = 'version20260207'
#   version      = 'version20260522'
    version      = 'version20260727'
    specieslist  = ['CO2_LBC','CH4_LBC','N2O_LBC','CFCL3_LBC','CFC11eq_LBC','CF2CL2_LBC']
    nlatlist     = [1,360] # [360]       # [360] # final data
    time_units   = 'days since 1850-01-01'
    calendar     = 'noleap'

#   I. 1pctco2
    scenariolist     = ['CMIP-1pctco2'] ; i4mpdownloadlist = ['CR-CMIP-1-0-0'] ; periodlist = ['0-166']

    timeresolutionlist = ['monthly'] ; regionlist = ['ZONAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units='days since 0000-01-01', calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
#
    timeresolutionlist = ['annual','monthly'] ; regionlist = ['GLOBAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units='days since 0000-01-01', calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
#
#   II. abruptx4co2
    scenariolist     = ['CMIP-abrupt4xco2'] ; i4mpdownloadlist = ['CR-CMIP-1-0-0'] ; periodlist = ['1850-1850']

    timeresolutionlist = ['monthly'] ; regionlist = ['ZONAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
#
    timeresolutionlist = ['annual','monthly'] ; regionlist = ['GLOBAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)


#   III. piControl / historical
    scenariolist     = ['CMIP'] ; i4mpdownloadlist = ['CR-CMIP-1-0-0'] ; periodlist         = ['1850-1850']

    timeresolutionlist = ['monthly'] ; regionlist = ['ZONAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
#
    timeresolutionlist = ['annual','monthly'] ; regionlist = ['GLOBAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)

    timeresolutionlist = ['monthly']
    periodlist         = ['1750-2023']
#   
    regionlist = ['GLOBAL','ZONAL'] # ['ZONAL'] #,'GLOBAL']  # original data
#
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units='days since 1750-01-01', calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
#
#   
    timeresolutionlist = ['annual']
    regionlist = ['GLOBAL']
    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units='days since 1750-01-01', calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
#
#   V. scenarios
    scenariolist       = ['ScenarioMIP']
    i4mpdownloadlist   = ['CR-h-1-0-0','CR-vl-1-0-0']

    timeresolutionlist = ['monthly']
    periodlist         = ['2022-2100']
#   
    regionlist = ['GLOBAL','ZONAL'] # ['ZONAL'] #,'GLOBAL']  # original data
#
#    buildconcentrationloop2.buildconcentrationloop2(scenariolist=scenariolist, timeresolutionlist=timeresolutionlist, time_units=time_units, calendar=calendar, specieslist=specieslist, periodlist=periodlist, regionlist=regionlist, version=version, i4mpdownloadlist=i4mpdownloadlist, nlatlist=nlatlist, overwrite=overwrite)
