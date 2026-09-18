import readspectrum_aerotab
import readspectrum_cdr
import readspectrum_blackbody


def readspectrum(var, origin, wvlresolution, wvl0, wvl1, dwvl, year0, year1, temperature, prefactor, desired_wvl_units):
#---------------
#
    '''
    REMARK
        wvl0, wvl1, dwvl : are assumed to be in the same units as desired_wvl_units

    INPUT
        var            : 'SSI' (solar spectral irradiance),
        origin         : 'AeroTab', 'ClimateDataRecord', 
        wvlresolution  : 'standard' or 'high' (when ClimateDataRecord)
        wvl0           : 
        wvl1           :
        dwvl
        year0          : [only applicable when origin =
        year1            [onl
        temperature    : 
        prefactor      : [only applicable when var         
        desired_wvl_units

    CALLED BY :
        interpolatefield [../../cmip7-volcaod-input4mips-to-noresm/source]

    CALLS
        readspectrum_aerotab
        readspectrum_cdr
        readspectrum_blackbody

    '''
#
#   read data
    if   ( var == 'SSI' and origin == 'AeroTab'           ) : data = readspectrum_aerotab.readspectrum_aerotab(    var=var                                                                                                                                                   )
    elif ( var == 'SSI' and origin == 'ClimateDataRecord' ) : data = readspectrum_cdr.readspectrum_cdr(            var=var,                wvlresolution=wvlresolution,                                  year0=year0, year1=year1                                            )
    elif ( var == 'BBI' and ( origin == 'AeroTab' \
                           or origin == 'SP2006' ) )        : data = readspectrum_blackbody.readspectrum_blackbody(         origin=origin,                             wvl0=wvl0, wvl1=wvl1, dwvl=dwvl, wvl_units=desired_wvl_units, temperature=temperature,prefactor=prefactor)
    else :
        print('+++ readspectrum +++')
        print('No var or origin recognized : ', var, origin)
        quit()
#
#   convert to desired units
    if   ( data['wavelength_units'] == desired_wvl_units )                  : factor=1.       # in case equal units
    elif ( data['wavelength_units'] == 'nm' and desired_wvl_units == 'um' ) : factor=1.e-3    # in case different units
    elif ( data['wavelength_units'] == 'um' and desired_wvl_units == 'nm' ) : factor=1.e+3    # in case different units  
    else :
        print('+++ readspectrum +++')
        print('No unit conversion available between : ', data['wavelength_units'], desired_wvl_units)
        quit()
#
    data['wavelength']       = data['wavelength'] * factor
    data['wavelength_bnds']  = data['wavelength_bnds'] * factor
    data['wavelength_units'] = desired_wvl_units
#
    return data
