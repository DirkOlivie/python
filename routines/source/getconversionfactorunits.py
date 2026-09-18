def getconversionfactorunits(origunits,finalunits,var=None) :
#---------------------------------------------------
    '''
    (2025-05-16)
        Adding Nav = Avogadro number

    MODIFICATIONS
    '''
    print('+++ getconversionfactorunits +++')
    print('var : ', var)

    grav=9.81
    Nav=6.022e+23

    if   ( var == 'lossch3oh'    or var == 'prodch3oh' ) : Mw = 32.0400                # 32  
    elif ( var == 'lossch3coch3' or var == 'prodch3coch3'   ) : Mw = 58.0768                   # 58
    elif ( var == 'lossch3cooh'  or var == 'prodch3cooh'   ) : Mw = 60.0504                   # 60
    elif ( var == 'lossch4'      or var == 'prodch4'   ) : Mw = 16.0406                # 16
    elif ( var == 'lossco'       or var == 'prodco'    ) : Mw = 28.0104                # 28
    elif ( var == 'losshcho'     or var == 'prodhcho'  ) : Mw = 30.0252                # 30
    elif ( var == 'losshcooh'    or var == 'prodhcooh' ) : Mw = 46.0246                # 46
    elif ( var == 'lossh2'       or var == 'prodh2'    ) : Mw = 2.0148                 # 2
    elif ( var == 'lossisop'     or var == 'prodisop'  ) : Mw = 68.1142                # 68
    elif ( var == 'lossh2o'      or var == 'prodh2o'   ) : Mw = 18.0142                # 18
    elif ( var == 'lossmhp'      or var == 'prodmhp'   ) : Mw = 48.0394                # 48 mhp = ch3ooh methyl hydroperoxide
    elif ( var == 'losspan'      or var == 'prodpan'   ) : Mw = 121.04794              # 121
    

    if ( origunits == finalunits )                  : scaling=1.
    elif ( origunits == '1'         and finalunits == '%' ) : scaling=100.
    elif ( origunits == 'fraction'  and finalunits == '%' ) : scaling=100.
    elif ( origunits == 'm s-1'     and finalunits == 'kg m-2 s-1' ) : scaling=1000. # precipitation
    elif ( origunits == 'unitless'  and finalunits == '1' ) : scaling=1.
    elif ( origunits == 'kg kg-1'   and finalunits == '1' ) : scaling=1.
    elif ( origunits == 'kg m-2'    and finalunits == 'm' ) : scaling=1. / 2.1415   # kg[ozone]/m2 -> m [ozone]
    elif ( origunits == 'mol mol-1' and finalunits == 'nmol mol-1' ) : scaling=1.e9 #
    elif ( origunits == 'mol mol-1' and finalunits == 'ppb' ) : scaling=1.e9        #
    elif ( origunits == 'mol mol-1' and finalunits == 'ppt' ) : scaling=1.e12       #
    elif ( origunits == 'mol mol-1' and finalunits == 'mole mole-1' ) : scaling=1.  #
    elif ( origunits == 'mol mol-1' and finalunits == '1'   ) : scaling=1.  #
    elif ( origunits == 'kg m-3'    and finalunits == 'ug m-3' ) : scaling=1.e9  #
    elif ( origunits == 'molecules cm-3 s-1' and finalunits == 'mol m-3 s-1' ) : scaling =          1.e+6/Nav # molecules/cm3 -> moles/m3
    elif ( origunits == 'molecules cm-3 s-1' and finalunits == 'kg m-3 s-1' )  : scaling = Mw*1.e-3*1.e+6/Nav # molecules/cm3 -> kg/m3
    elif ( origunits == 'm2/s2' and finalunits == 'm' ) : scaling = 1/grav
    elif ( origunits == 'mg m-2 d-1' and finalunits == 'kg m-2 s-1' ) : scaling = 1.e-6/86400.

    else : 
        print('+++ getconversionfactorunits +++')
        print('Units cannot be converted')
        print('origunits : ', origunits)
        print('finalunits: ', finalunits)
        quit()

    return scaling
