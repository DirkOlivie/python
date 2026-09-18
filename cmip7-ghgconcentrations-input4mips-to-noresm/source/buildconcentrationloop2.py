import buildconcentration
#
def buildconcentrationloop2(scenariolist, timeresolutionlist, time_units, calendar, regionlist, specieslist, periodlist, version, i4mpdownloadlist, nlatlist, overwrite):
#-----------------------------
    '''
    INPUT
	    scenario           : 'hist'
        timeresolutionlist : list of time-resolution : 'montly' | 'annual'
        regionlist         : 'ZONAL'                                                     [original resolution]
	    specieslist        : list of GHGs : 'CO2', 'CH4', 'N2O', 'CFC11eq', 'CFC12'
	    periodlist         : 2-elements array : [year0, year1]
	    version            : string describing the version date, e.g., 'version20180330'
	    i4mpdownload       :
	    nlatlist           : 0 or 360 or ...                                              [final resolution]
        overwrite          : True | False

    CALLED BY 
        buildconcentrationloop

    CALLS 
	    builconcentration
    '''
#
#----------------------------
#
    for period in periodlist :

#       converting string period -> 2-element arrya [year0,year1]
        line=period.split('-')
        yearrange=[int(line[0]), int(line[1])]

#       loop over all resolutions
        for timeresolution in timeresolutionlist :
            for region in regionlist :
                for nlat in nlatlist : 
                    for scenario in scenariolist :
                        for i4mpdownload in i4mpdownloadlist :
    
                            buildconcentration.buildconcentration(scenario=scenario, timeresolution=timeresolution, time_units=time_units, calendar=calendar, region=region, specieslist=specieslist, yearrange=yearrange, version=version, i4mpdownload=i4mpdownload, nlat=nlat, overwrite=overwrite)
