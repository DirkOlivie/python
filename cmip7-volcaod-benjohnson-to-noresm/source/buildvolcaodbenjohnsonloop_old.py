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
#   overwrite=True
    overwrite=False

#   version INPUT/OUTPUT
    inputversion='UOEXETER-CMIP-2-2-1'
#   outputversion='v20260105'
    outputversion='v20261030'

#   desired units
    desiredheightunits     = 'km'         # height     [what was used in CMIP6 file given to NorESM]
    desiredextinctionunits = 'km-1'       # extinction [what was used in CMIP6 file given to NorESM]

#   time frequencies
    periodlist     = ['185001-202112-clim','175001-202312']
#    periodlist     = ['185001-202112-clim']
#    periodlist     = ['185001-202112-clim-wghtavg']
#    intpmethodlist = ['intpmidpoint','intpwghtavg']
    intpmethodlist = ['intpwghtavg']
#
    buildvolcaodbenjohnsonloop2.buildvolcaodbenjohnsonloop2(periodlist=periodlist, \
                                                            inputversion=inputversion,outputversion=outputversion, \
                                                            desiredheightunits=desiredheightunits,desiredextinctionunits=desiredextinctionunits, \
                                                            intpmethodlist=intpmethodlist, \
                                                            overwrite=overwrite)
#
if __name__ == '__main__':
    main()
