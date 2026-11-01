import numpy as np

import getblackbodyirradiance

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import wvl2wvlbnds

def readspectrum_blackbody(origin, wvl0, wvl1, dwvl, wvl_units, temperature, prefactor):
#-------------------------
    '''
    INPUT
        origin        : 'AeroTab' | 'SP2006'
        wvl0          :
        wvl1          :
        dwvl          :
        wvl_units     :
        temperature   : [K]   
        prefactor     : multiplicative factor for calculated irradiances
        
    RETURN
        structure containing :

    CALLS
        getblackbodyirradiance [calculates for 1 wavelength]    

    '''    

#   generate wavelengths in nm [HARDCODED]
#    wavelength_units='nm'    
#    wvl0 = 100      # smalles wavelength
#    wvl1 = 20000    # largest wavelength
#    wvl1 = 1000000  # largest wavelength
#    dwvl = 1        # wavelength resolution

#   generate wavelengths : from wvl0 to wvl1
    wavelength=np.arange(wvl0,wvl1+dwvl,dwvl,dtype=float)
    nwvl=len(wavelength)

#   derive wavelengths_bnds
    wavelength_bnds=wvl2wvlbnds.wvl2wvlbnds(wavelength=wavelength)

#   radiance to be calculated
    valuelist= np.zeros(nwvl, dtype=float)

#   black body radiation in [W m-2 m-1] : return is always in W m-2 m-1
    for iwvl in range(0,nwvl) :
        valuelist[iwvl] = getblackbodyirradiance.getblackbodyirradiance(wvl=wavelength[iwvl], wvl_units=wvl_units, T=temperature, origin=origin)
#   
#   conversions of [W m-2 m-1] to [W m-2 nm-1]
    units='W m-2 nm-1' # desired units hardcoded
    if ( units == 'W m-2 nm-1' ) :
        valuelist = valuelist * 1.e-9
    else :
        print('+++ readspectrum_blackbody +++')
        print('No units recognized : ', units)    
        quit()

#   apply prefactor
    if ( prefactor != None) :
        valuelist = valuelist * prefactor   
    
#   return data
    data= { 'variable'         : 'irradiance', \
            'valuelist'        : valuelist, \
            'units'            : units, 
            'wavelength'       : wavelength, \
            'wavelength_bnds'  : wavelength_bnds, \
            'wavelength_units' : wvl_units}
#
    return data




