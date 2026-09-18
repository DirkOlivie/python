def getmolarweight(var) :
#########################    
#
    if   ( var=='ozone' or var == 'O3' )        : mw=48.
    elif ( var=='CH4'   or var == 'CH4CHEM' )   : mw=16.
    elif ( var=='N2O'   or var == 'N2OCHEM' )   : mw=44.
    elif ( var=='CO2'   or var == 'CO2CHEM' )   : mw=44
    elif ( var=='CO'    )                       : mw=28.     
    elif ( var=='NO2'   )                       : mw=46.
    elif ( var=='SO2'   )                       : mw=64.
    elif ( var=='H2SO4'   )                     : mw=98.
    elif ( var=='CFC11' or var == 'CFC11CHEM' ) : mw=137.367503
    elif ( var=='CFC12' or var == 'CFC12CHEM' ) : mw=120.913206  
    elif ( var=='CHBR3' )                       : mw=252.730400

    else               : 
        print ('getmolarweight : no var recognized = '+var)         
        quit()    
#
    return mw
