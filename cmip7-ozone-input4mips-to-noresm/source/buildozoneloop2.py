import numpy as np

import buildozone

def buildozoneloop2(species, periodlist, version, scenariolist, i4mpdownloadlist, fromclim, dolon, overwrite, calendar, time_units):
#------------------
    '''
    INPUT
        species : 'vmro3'
        periodlist : 
        version  
        scenariolist
        i4mpdownload
        fromclim
        dolon
        overwrite
        calendar
        time_units

    CALLED BY
        buildozoneloop

    CALLS
        buildozone

    '''

    #
    for period in periodlist :
        for scenario in scenariolist :
            for i4mpdownload in i4mpdownloadlist : 

                print('Hallo')  

                buildozone.buildozone(species=species, period=period, version=version, scenario=scenario, i4mpdownload=i4mpdownload, fromclim=fromclim, dolon=dolon, overwrite=overwrite, calendar=calendar, time_units=time_units)
