def getidlregion (region) :
#---------------    
#
# column burden
    if   region==''           : idlregion='Global'
    elif region=='glob'       : idlregion='Global'
#   elif region=='28S28N'     : idlregion='28'+r'$^\circ$'+'S-28'+r'$^\circ$'+'N'
#   elif region=='60N90N'     : idlregion='60'+r'$^\circ$'+'N-90'+r'$^\circ$'+'N'
    elif region=='60N90N'     : idlregion='60'+u'\N{DEGREE SIGN}'+'N-90'+u'\N{DEGREE SIGN}'+'N'
    elif region=='28N60N'     : idlregion='28'+u'\N{DEGREE SIGN}'+'N-60'+u'\N{DEGREE SIGN}'+'N'
    elif region=='28S28N'     : idlregion='28'+u'\N{DEGREE SIGN}'+'S-28'+u'\N{DEGREE SIGN}'+'N'
    elif region=='60S28S'     : idlregion='60'+u'\N{DEGREE SIGN}'+'S-28'+u'\N{DEGREE SIGN}'+'S'
    elif region=='90S60S'     : idlregion='90'+u'\N{DEGREE SIGN}'+'S-60'+u'\N{DEGREE SIGN}'+'S'
    elif region=='90S28S'     : idlregion='90'+u'\N{DEGREE SIGN}'+'S-28'+u'\N{DEGREE SIGN}'+'S'
    elif region=='NORTHATL'   : idlregion='North Atlantic'
    elif region=='INDIANOCN'  : idlregion='Indian Ocean' 
    elif region=='BAYOFBENGA' : idlregion='Bay of Bengal' 
    elif region=='NORTHATL2'  : idlregion='North Atlantic'
    elif region=='SOUTHOCNIO' : idlregion='Southern Ocean (IO)' 
    elif region=='SOUTHOCNNF' : idlregion='Southern Ocean (negative flux)' 
    elif region=='TROPEASTPAC': idlregion='Tropical East Pacific' 
    elif region=='TROPWESTPAC': idlregion='Tropical West Pacific'
#
    else : idlregion=region
#
    return idlregion
