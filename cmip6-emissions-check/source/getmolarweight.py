def getmolarweight(long_name) :
#------------------------------
#
    if ( long_name == 'NH3 CEDS anthropogenic emissions' \
      or long_name == 'NH3 CEDS biomass burning emissions' \
      or long_name == 'NH3 soil emissions' \
      or long_name == 'NH3 ocean emissions' \
      \
      or long_name == 'Emissions of NH3 from AGRENEINDTRADOMSOLWSTSHP in anthrosurfgas' \
      or long_name == 'Emissions of NH3 from AGRIBORFDEFOPEATSAVATEMF in bbsurf' ) :
        Mw = 17.
    else :
        print('No long_name recognized : '+long_name)
        quit()
#
    return Mw    
