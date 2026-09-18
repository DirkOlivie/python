def getstandardunits(units) :
####################


    if   units=='kg/m2/s'     : standardname='kg m-2 s-1'
    elif units=='kg/m2/sec'   : standardname='kg m-2 s-1'
    elif units=='kg S/m2 s-1' : standardname='kg m-2 s-1'
    elif units=='gN/m^2/s'    : standardname='g m-2 s-1'  # CLM : F_N2O_NIT, F_N2O_DENIT, NDEP_TO_SMINN
    elif units=='gN/m^2'      : standardname='g m-2'      # CLM
    elif units=='gN/m2/sec'   : standardname='g m-2 s-1'  # CAM (introduced by me)
    elif units=='gC/m^2/s'    : standardname='g m-2 s-1'  # CLM : NPP, GPP
    elif units=='gC/m2/s'     : standardname='g m-2 s-1'  # CLM : CH4PROD, FCH4TOCO2
    elif units=='gC/m2'       : standardname='g m-2'      # CLM : TOTCOLCH4
    elif units=='kgC/m2/s'    : standardname='kg m-2 s-1' # CLM : FCH4, FCH4_DFSAT
    elif units=='kg/m2'       : standardname='kg m-2'
    elif units=='kg/m^2'      : standardname='kg m-2'
    elif units=='mg/m2'       : standardname='mg m-2'
    elif units=='molec/cm2/s' : standardname='molecules cm-2 s-1'
    elif units=='molecules/cm3/sec' : standardname='molecules cm-3 s-1'
    elif units=='molec cm-3 s-1' : standardname='molecules cm-3 s-1'
    elif units=='/cm3/s'      : standardname='molecules cm-3 s-1'    
    elif units=='mol/mol'     : standardname='mol mol-1'
    elif units=='mole mole-1' : standardname='mol mol-1'
    elif units=='kg/kg'       : standardname='kg kg-1'
    elif units=='1/kg'        : standardname='kg-1'
    elif units=='m/s'         : standardname='m s-1'
    elif units=='1/m2'        : standardname='m-2'
    elif units=='m^2/m^2'     : standardname='m2 m-2'
    elif units=='mm3/mm3'     : standardname='mm3 mm-3'
    elif units=='m3/m3'       : standardname='m3 m-3'
    elif units=='#/m3'        : standardname='m-3'
    elif units=='1/cm3'       : standardname='cm-3'
    elif units=='mol/m2/s'    : standardname='mol m-2 s-1'
    elif units=='1/km'        : standardname='km-1'
    elif units=='#/cm3'       : standardname='cm-3' 
    elif units=='W/m2'        : standardname='W m-2' 
    elif units=='W/m^2'       : standardname='W m-2' 
    elif units=='percent'     : standardname='%' 
    elif units=='N/m2'        : standardname='Pa'        # NEWTON <-> NOT TO BE MIXED WITH Nitrogen !!!
    elif units=='Pa/s'        : standardname='Pa s-1'
    elif units=='kg CH$_4$ m$^{-2}$ s$^{-1}$' : standardname = 'kg m-2 s-1'
    elif units=='kg (CH4) m-2 s-1'            : standardname = 'kg m-2 s-1'
    elif units=='kg CH4 m-2 s-1'              : standardname = 'kg m-2 s-1'
    elif units=='kgCH4 m-2 s-1'               : standardname = 'kg m-2 s-1'
    elif units=='kgCH4/m2/s'                  : standardname = 'kg m-2 s-1'
    elif units=='1'           : standardname='1'                    
#   default 
    else : standardname=units      

    return standardname
