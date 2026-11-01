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
    inputversion='UOEXETER-CMIP-2-2-1' # for the final filename
#   outputversion='v20260105' # used in NorESM3 simulations for CMIP7
#   outputversion='v20261030' # was bit-identical with v20260105 [NICE]
    outputversion='v20261031'

#   desired units
    desiredheightunits     = 'km'         # height     [what was used in CMIP6 file given to NorESM]
    desiredextinctionunits = 'km-1'       # extinction [what was used in CMIP6 file given to NorESM]

#   time frequencies
#    periodlist     = ['185001-202112-clim','175001-202312']
#    periodlist     = ['185001-202112-clim']
#    periodlist     = ['185001-202112-clim-wghtavg']
#    intpmethodlist = ['intpmidpoint','intpwghtavg']
    intpmethodlist = ['intpwghtavg']
#
#   picontrol
    origindescriptionlist=[]
#
    yearlist=[1850]
    hybridperiod='185001-202112-clim' # for the final filename
    for year in yearlist :
        tmp = { 'year' : year, 'origyear': year, 'origperiod' : '185001-202112-clim', 'i4mpdownload' : 'UOEXETER-CMIP-2-2-1', 'scenario' : 'CMIP'}
        origindescriptionlist.append(tmp)

    buildvolcaodbenjohnsonloop2.buildvolcaodbenjohnsonloop2(inputversion=inputversion, \
                                                            origindescriptionlist=origindescriptionlist, \
                                                            outputversion=outputversion, \
                                                            hybridperiod=hybridperiod, \
                                                            desiredheightunits=desiredheightunits,desiredextinctionunits=desiredextinctionunits, \
                                                            intpmethodlist=intpmethodlist, \
                                                            overwrite=overwrite)
#
#   historical
    origindescriptionlist=[]
#
    yearlist=list(range(1750,2023+1))
    hybridperiod='175001-202312' # for the final filename
    for year in yearlist :
        tmp = { 'year' : year, 'origyear': year, 'origperiod' : '175001-202312', 'i4mpdownload' : 'UOEXETER-CMIP-2-2-1', 'scenario' : 'CMIP'}
        origindescriptionlist.append(tmp)

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
