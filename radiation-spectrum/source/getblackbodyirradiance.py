import math

def getblackbodyirradiance(wvl, wvl_units, T, origin):
#-------------------------
    '''
    https://galileo.phys.virginia.edu/classes/252/black_body_radiation.html

    https://en.wikipedia.org/wiki/Planck%27s_law

    INPUT
        wvl       : wavelength
        wvl_units : 'm' | 'um' | 'nm' (wavelength units)
        T         : temperature [K]
        origin    : 'AeroTab' | 'SP2006'

    RETURN
        flux [W m-2 m-1] 

    '''

    c = 2.9979e8 # m/s
    h = 6.626e-34 # Js
    k = 1.381e-23 # J/K 

    pi = math.pi
    e = math.e

    if ( origin == 'SP2006' ) :
#       formula expects [m]    
        if (   wvl_units == 'm'  ) : L = wvl      # m
        elif ( wvl_units == 'um' ) : L = wvl*1e-6 # um -> m
        elif ( wvl_units == 'nm' ) : L = wvl*1e-9 # nm -> m
        else :
            print('+++ getblackbodyirradiance +++')
            print('No wavelength units recognized : ', wvl_units)
            quit()

        flux = 2. * pi * c**2 * h / L**5 / (math.exp(c * h /  (k * L * T) ) - 1 ) # wvl in m

    elif ( origin == 'AeroTab' ) : 
#       formula expects [um] 
        if   ( wvl_units == 'm'  ) : L = wvl*1.e+6  # m -> um
        elif ( wvl_units == 'um' ) : L = wvl        # um
        elif ( wvl_units == 'nm' ) : L = wvl*1.e-3  # nm -> um
        else :
            print('+++ getblackbodyirradiance +++')
            print('No wavelength units recognized : ', wvl_units)
            quit()        

        flux = (3.74e8/L**5) /(2.718281828**(1.44e4/(T*L))-1.0) # wvl in um
#
    else :
        print('+++ getblackbodyirradiance +++')
        print('No origin recognized : ', origin)
        quit()

    return flux
