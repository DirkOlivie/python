def getvartrend(var):
#---------------------------
    '''
    MODIFICATIONS
	(2025-10-14) creation

    INPUT
        var 

    RETURN dictionary containing 2 elements :
        'dotrend' : '' | 'offset' | 'differential' | 'integral'
        'varorig' : 

    '''

#   default value
#   offset - offset
    if   ( var=='TMCO2_offset'           ) : des={'dotrend':'offset', 'varorig': 'TMCO2' }
    elif ( var=='TMCO2_FFF_offset'       ) : des={'dotrend':'offset', 'varorig': 'TMCO2_FFF' }
    elif ( var=='TMCO2_LND_offset'       ) : des={'dotrend':'offset', 'varorig': 'TMCO2_LND' }
    elif ( var=='TMCO2_OCN_offset'       ) : des={'dotrend':'offset', 'varorig': 'TMCO2_OCN' }
    elif ( var=='TMCO2_FFFLNDOCN_offset' ) : des={'dotrend':'offset', 'varorig': 'TMCO2_FFFLNDOCN' }
#   trend - differential
    elif ( var=='TMCO2_trend'           ) : des={'dotrend':'differential', 'varorig': 'TMCO2' }
    elif ( var=='TMCO2_FFF_trend'       ) : des={'dotrend':'differential', 'varorig': 'TMCO2_FFF' }
    elif ( var=='TMCO2_LND_trend'       ) : des={'dotrend':'differential', 'varorig': 'TMCO2_LND' }
    elif ( var=='TMCO2_OCN_trend'       ) : des={'dotrend':'differential', 'varorig': 'TMCO2_OCN' }
    elif ( var=='TMCO2_FFFLNDOCN_trend' ) : des={'dotrend':'differential', 'varorig': 'TMCO2_FFFLNDOCN' }
#   cumulative - integral
    elif ( var=='SFCO2_cumulative'           ) : des={'dotrend':'integral', 'varorig': 'SFCO2' }
    elif ( var=='SFCO2_FFF_cumulative'       ) : des={'dotrend':'integral', 'varorig': 'SFCO2_FFF' }
    elif ( var=='SFCO2_LND_cumulative'       ) : des={'dotrend':'integral', 'varorig': 'SFCO2_LND' }
    elif ( var=='SFCO2_OCN_cumulative'       ) : des={'dotrend':'integral', 'varorig': 'SFCO2_OCN' }
    elif ( var=='SFCO2_FFFLNDOCN_cumulative' ) : des={'dotrend':'integral', 'varorig': 'SFCO2_FFFLNDOCN' }
#   cumulative - integral
    elif ( var=='SFCO2_ac_CO2_columnburden_cumulative'     ) : des={'dotrend':'integral', 'varorig': 'SFCO2_ac_CO2_columnburden' }
    elif ( var=='SFCO2_FFF_ac_CO2_columnburden_cumulative' ) : des={'dotrend':'integral', 'varorig': 'SFCO2_FFF_ac_CO2_columnburden' }
    elif ( var=='SFCO2_FFFLNDOCN_ac_CO2_columnburden_cumulative' ) : des={'dotrend':'integral', 'varorig': 'SFCO2_FFFLNDOCN_ac_CO2_columnburden' }
#
    elif ( var=='SFCO2_LNDxLANDFRAC_cumulative' ) : des={'dotrend':'integral', 'varorig': 'SFCO2_LNDxLANDFRAC' }
#   offsetlast30yr
    elif ( var=='EMI_SO2SO4_as_SO2_TOT_noresm2_offsetlast30yr' ) : des={'dotrend':'offsetlast30yr', 'varorig': 'EMI_SO2SO4_as_SO2_TOT_noresm2' }
    elif ( var=='EMI_SO2SO4_as_S_TOT_noresm2_offsetlast30yr'   ) : des={'dotrend':'offsetlast30yr', 'varorig': 'EMI_SO2SO4_as_S_TOT_noresm2' }
    elif ( var=='cb_SULFATE_offsetlast30yr' ) : des={'dotrend':'offsetlast30yr', 'varorig': 'cb_SULFATE' }
#
#   trend - differential
    elif ( var=='tempocn_trend'           ) : des={'dotrend':'differential', 'varorig': 'tempocn' }
    elif ( var=='tempgaocn_trend'         ) : des={'dotrend':'differential', 'varorig': 'tempgaocn' }
    elif ( var=='thetaogaocn_trend'       ) : des={'dotrend':'differential', 'varorig': 'thetaogaocn' } # MOM6

#   else
    else                            : des={'dotrend':'', 'varorig':  var}
# 
    return des
