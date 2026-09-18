import buildozoneloop2


def main():
#---------------------------------
    '''
    CALLS
        buildozoneloop2

    REMARK

    VARIABLES TO DEFINE
        species : 'vmro3'
        version
        periodlist
        scenarionlist
        i4mpdownload
        dolon : True (have explicit longitudes) | False (use zonal mean)
        fromclim : '-clim' | ''

    '''

#   I. piControl climatology
#---------------------------
    species='vmro3' ; version='version20260722' ; periodlist=['1850-1850'] ; scenariolist=['CMIP'] ; i4mpdownloadlist=['FZJ-CMIP-ozone-1-2'] ; fromclim='-clim' ; calendar='noleap' ; time_units='days since 1850-01-01'
#
#   overwrite=False
    overwrite=True
#
    dolon=True
#   buildozoneloop2
    buildozoneloop2.buildozoneloop2(species=species, periodlist=periodlist,version=version, scenariolist=scenariolist, i4mpdownloadlist=i4mpdownloadlist, fromclim=fromclim, dolon=dolon, overwrite=overwrite, calendar=calendar, time_units=time_units)

#   II. historical
#-----------------
    species='vmro3' ; version='version20260722' ; periodlist=['1849-2022'] ; scenariolist=['CMIP'] ; i4mpdownloadlist=['FZJ-CMIP-ozone-2-0'] ; fromclim='' ; calendar='noleap' ; time_units='days since 1750-01-01'
#
#   overwrite=False
    overwrite=True
#
    dolon=True
#   buildozoneloop2
    buildozoneloop2.buildozoneloop2(species=species, periodlist=periodlist,version=version, scenariolist=scenariolist, i4mpdownloadlist=i4mpdownloadlist, fromclim=fromclim, dolon=dolon, overwrite=overwrite, calendar=calendar, time_units=time_units)
#
#   III. scenario
#----------------
    species='vmro3' ; version='version20260722' ; periodlist=['2022-2101'] ; scenariolist=['ScenarioMIP'] ; i4mpdownloadlist=['FZJ-CMIP-ozone-h-1-0'] ; fromclim='' ; calendar='noleap' ; time_units='days since 1750-01-01'
#
#   overwrite=False
    overwrite=True
#
#   buildozoneloop2
#   buildozoneloop2.buildozoneloop2(species=species, periodlist=periodlist,version=version, scenariolist=scenariolist, i4mpdownloadlist=i4mpdownloadlist, fromclim=fromclim, dolon=dolon, overwrite=overwrite, calendar=calendar, time_units=time_units)


if __name__ == '__main__':
    main()
