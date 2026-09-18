def getidlunits (units) :
#------------------------
# column burden
    if   units==''          : idlunits=''
    elif units=='m s-1'     : idlunits='m s'+r'$^{-1}$'
    elif units=='m-2'       : idlunits='m'+r'$^{-2}$'
    elif units=='kg m-2'    : idlunits='kg m'+r'$^{-2}$'
    elif units=='kg m-3'    : idlunits='kg m'+r'$^{-3}$'
    elif units=='kg m-2 s-1': idlunits='kg m'+r'$^{-2}$'+' s'+r'$^{-1}$'
    elif units=='kg kg-1'   : idlunits='kg kg'+r'$^{-1}$'
    elif units=='kg-1'      : idlunits='kg'+r'$^{-1}$'
    elif units=='W/m2'      : idlunits='W m'+r'$^{-2}$'
    elif units=='W m-2'     : idlunits='W m'+r'$^{-2}$'
    elif units=='W/m**2'    : idlunits='W m'+r'$^{-2}$'
    elif units=='C'         : idlunits=r'$^\circ$''C'
    elif units=='degC'      : idlunits=r'$^\circ$''C'
    elif units=='degC year-1' : idlunits=r'$^\circ$''C yr'+r'$^{-1}$'
    elif units=='mm day-1'  : idlunits='mm day'+r'$^{-1}$'
    elif units=='mol mol-1' : idlunits='mol mol'+r'$^{-1}$'
    elif units=='Tg yr-1'   : idlunits='Tg yr'+r'$^{-1}$'
    elif units=='Tg N yr-1'   : idlunits='Tg N yr'+r'$^{-1}$'
    elif units=='Tg NH3 yr-1'   : idlunits='Tg NH'+r'$_3$'+' yr'+r'$^{-1}$'
    elif units=='Tg N2O yr-1'   : idlunits='Tg N'+r'$_2$'+'O yr'+r'$^{-1}$'
    elif units=='Pg(C) yr-1'   : idlunits='Pg(C) yr'+r'$^{-1}$'    
    elif units=='km2'       : idlunits='km'+r'$^{2}$'
    elif units=='1e6km2'       : idlunits='10'+r'$^{6}$'+' km'+r'$^{2}$'
#
    else : idlunits=units
#
    return idlunits
