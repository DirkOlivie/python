import buildvolcaodloop2

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

#   wavelength interpolation : for weighting of the spectrum
    wvl_interpolation_type_list=['constant','blackbody']

#   var weighting : is not used in volcaodbuild.py
    var_weighting_type='single'
    var_weighting_type='combined'

#   version INPUT/OUTPUT
#    inputversion='UOEXETER-CMIP-2-1-0'
#    outputversion='v20250115'
    inputversion='UOEXETER-CMIP-2-2-1'
#    outputversion='v20260105'
    outputversion='v20261028' # 20261028

#   desired units
    desiredheightunits     = 'km'         # height     [what was used in CMIP6 file given to NorESM]
    desiredextinctionunits = 'km-1'       # extinction [what was used in CMIP6 file given to NorESM]

#   MAKE MEAN CLIMATOLOGY
#   time frequencies
    inputperiod  = '185001-202112-clim'
    outputperiod = '1850-2021-meanseasonalcycle' # only used for naming

    buildvolcaodloop2.buildvolcaodloop2(inputperiod=inputperiod,outputperiod=outputperiod,inputversion=inputversion,outputversion=outputversion,desiredheightunits=desiredheightunits,desiredextinctionunits=desiredextinctionunits,wvl_interpolation_type_list=wvl_interpolation_type_list, var_weighting_type=var_weighting_type,overwrite=overwrite)

#   MAKE HISTORICAL SERIES
#   time frequencies
    inputperiod='175001-202312'
    outputperiod='1750-2023-monthly'  # only used for naming

    buildvolcaodloop2.buildvolcaodloop2(inputperiod=inputperiod,outputperiod=outputperiod,inputversion=inputversion,outputversion=outputversion,desiredheightunits=desiredheightunits,desiredextinctionunits=desiredextinctionunits,wvl_interpolation_type_list=wvl_interpolation_type_list, var_weighting_type=var_weighting_type,overwrite=overwrite)

if __name__ == '__main__':
    main()
