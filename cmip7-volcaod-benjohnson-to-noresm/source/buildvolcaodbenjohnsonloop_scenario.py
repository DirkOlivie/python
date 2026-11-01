import buildvolcaodbenjohnsonloop2

def main():
#----------
    '''
    Original file : 
        - has a lot of NaNs (probably the troposphere)
        - CMIP6 NorESM2 : no NaNs

    The averaging period :
        1850-2021 (?) or 2023 (?)

    Dimensions :
        keep the latitude, altitude, altitude_int from the original CMIP7 file

    Units :
                   | ORIGINAL FILE | FINAL FILE |
        -----------|---------------|------------|
        altitude   | m             | km         | 
        extinction | m-1           | km-1       |
        wavelength | m             | um         |

    Wavelength :
        original file 
        how to interpolate    
    '''


#   overwriting : True : will make new file (and overwrite old file if exists)
#                 False : if file exists, will not make new file  
    overwrite=True
#   overwrite=False

#   version INPUT/OUTPUT
    inputversion='UOEXETER-ScenarioMIP-2-2-2' # only used in final filename
    outputversion='v20261031'

#   desired units
    desiredheightunits     = 'km'         # height     [what was used in CMIP6 file given to NorESM]
    desiredextinctionunits = 'km-1'       # extinction [what was used in CMIP6 file given to NorESM]

#   time frequencies
#    periodlist     = ['185001-202112-clim','175001-202312']
#    periodlist     = ['185001-202112-clim']
#    periodlist     = ['185001-202112-clim-wghtavg']
    hybridperiod='202101-250112'
    origindescriptionlist=[]
#   year 2021
    yearlist=[2021]
    for year in yearlist :
        tmp = { 'year' : year, 'origyear': year, 'origperiod' : '175001-202312', 'i4mpdownload' : 'UOEXETER-CMIP-2-2-1', 'scenario' : 'CMIP'}
        origindescriptionlist.append(tmp)
#   years 2022-2100
    yearlist=list(range(2022,2100+1))
    for year in yearlist :
        tmp = { 'year' : year, 'origyear': year, 'origperiod' : '202201-210012', 'i4mpdownload' : 'UOEXETER-ScenarioMIP-2-2-2', 'scenario' : 'ScenarioMIP'}
        origindescriptionlist.append(tmp)
#   years 2022-2100
    yearlist=[2200,2300,2400,2500,2501]
    for year in yearlist :
        tmp = { 'year' : year, 'origyear': 2100, 'origperiod' : '202201-210012', 'i4mpdownload' : 'UOEXETER-ScenarioMIP-2-2-2', 'scenario' : 'ScenarioMIP'} # repeat year 2100
        origindescriptionlist.append(tmp)

#    intpmethodlist = ['intpmidpoint','intpwghtavg']
    intpmethodlist = ['intpwghtavg']
#
    buildvolcaodbenjohnsonloop2.buildvolcaodbenjohnsonloop2(inputversion=inputversion, \
                                                            origindescriptionlist=origindescriptionlist, \
                                                            outputversion=outputversion, \
                                                            hybridperiod=hybridperiod, \
                                                            desiredheightunits=desiredheightunits,desiredextinctionunits=desiredextinctionunits, \
                                                            intpmethodlist=intpmethodlist, \
                                                            overwrite=overwrite)
#
if __name__ == '__main__':
    main()
