def getconversionfactorunits(origunits,finalunits) :
#---------------------------------------------------
    
    if ( origunits == finalunits )                  : scaling=1.
    elif ( origunits == '1'        and finalunits == '%' ) : scaling=100.
    elif ( origunits == 'fraction' and finalunits == '%' ) : scaling=100.
    elif ( origunits == 'm s-1'    and finalunits == 'kg m-2 s-1' ) : scaling=1000. # precipitation
    elif ( origunits == 'unitless' and finalunits == '1' ) : scaling=1.
    elif ( origunits == 'kg kg-1'  and finalunits == '1' ) : scaling=1.

    else : 
        print('Units cannot be converted')
        print('origunits : ', origunits)
        print('finalunits: ', finalunits)
        quit()

    return scaling
