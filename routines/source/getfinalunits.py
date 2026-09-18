import math

def getfinalunits(var, units):
#----------------
#
    print('+++ getfinalunits +++')
    print('units : '+units+'XXX')    
    print('var : '+var)
#
    pi = math.pi
    Rearth = 6370e+3           # Radius Earth [m]
    Mw_co2 = (12. + 16. + 16.) # Molar weight CO2 [[gram/mole]]   
    Mw_air = 28.97             # Molar weight air
    ps_mean = 98500.           # Mean surface pressure including orograph [Pa]
    g = 9.81                   # gravitational acceleration [m/s2]

#   ozone column
    if (   var=='cb_O3'          and units =='kg m-2' ) : newunits='DU' ; factor=1./2.1415e-5
    elif ( var=='column_O3'    and units =='kg m-2' ) : newunits='DU' ; factor=1./2.1415e-5
    elif ( var=='column_ozone' and units =='kg m-2' ) : newunits='DU' ; factor=1./2.1415e-5
    elif ( var=='toc'          and units =='kg m-2' ) : newunits='DU' ; factor=1./2.1415e-5
#   surface ozone mixing ratio
    elif ( var=='O3_SRF'          and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='O3_surfacelayer' and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='o3_surfacelayer' and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_1000hPa' and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_925hPa'  and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_850hPa'  and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_800hPa'  and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_700hPa'  and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_600hPa'  and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='vmro3_500hPa'  and units=='mol mol-1' ) : newunits='ppb' ; factor=1.e9
    elif ( var=='CH4'    and units=='mol mol-1' ) : newunits='ppm' ; factor=1.e6
#   CO2 vmr
    elif ( var=='CO2_columnburden_as_vmr' and units=='Tg' ) : newunits='mol mol-1' ; factor= 1.e9 / ( 4. * pi * Rearth * Rearth) / (ps_mean / g ) * Mw_air / Mw_co2
    elif ( var=='CO2_columnburden_as_RF'  and units=='Tg' ) : newunits='mol mol-1' ; factor= 1.e9 / ( 4. * pi * Rearth * Rearth) / (ps_mean / g ) * Mw_air / Mw_co2
#   PRECT
    elif ( var=='PRECT' and units=='m s-1' ) : newunits='mm day-1' ; factor=86400*1000
#
    else : newunits=units ; factor=1.

    print('newunits : '+newunits)
    print('--- getfinalunits ---')

    return newunits, factor
